"""
Direct Fine-tuning of IndoBERT on Target Dataset (Baseline)

This script fine-tunes base IndoBERT directly on target_balanced.csv for
sentiment classification — no domain adaptation step, pure baseline approach.
"""

import os
import pandas as pd
import torch
import numpy as np
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
    DataCollatorWithPadding,
)
from datasets import Dataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    classification_report,
    confusion_matrix,
)


# ============================================================================
# Config
# ============================================================================
BASE_MODEL      = "indobenchmark/indobert-base-p1"
DATA_PATH       = "target_balanced.csv"
OUTPUT_DIR      = "./indobert_target_direct"
TEXT_COL        = "reviewContent"
LABEL_COL       = "label"

LABEL2ID = {"negative": 0, "positive": 1}
ID2LABEL = {0: "negative", 1: "positive"}

MAX_LENGTH      = 128
NUM_EPOCHS      = 5
TRAIN_BATCH     = 16
EVAL_BATCH      = 32
LEARNING_RATE   = 2e-5
WEIGHT_DECAY    = 0.01
WARMUP_RATIO    = 0.1
TEST_SIZE       = 0.2
SEED            = 42


# ============================================================================
# Metrics
# ============================================================================
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=1)
    accuracy = accuracy_score(labels, preds)
    precision, recall, f1, _ = precision_recall_fscore_support(
        labels, preds, average="weighted"
    )
    return {
        "accuracy":  accuracy,
        "precision": precision,
        "recall":    recall,
        "f1":        f1,
    }


# ============================================================================
# Main
# ============================================================================
def main():
    # ---- Device ----
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device : {device}")
    if device.type == "cuda":
        print(f"GPU    : {torch.cuda.get_device_name(0)}")

    # ---- Load Data ----
    print("\n" + "=" * 60)
    print("Loading target_balanced.csv ...")
    print("=" * 60)

    df = pd.read_csv(DATA_PATH)
    print(f"Shape  : {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print(f"\nLabel distribution:")
    print(df[LABEL_COL].value_counts().to_string())

    # Drop rows with missing text or label
    before = len(df)
    df = df.dropna(subset=[TEXT_COL, LABEL_COL])
    df[TEXT_COL] = df[TEXT_COL].astype(str).str.strip()
    df = df[df[TEXT_COL] != ""]
    print(f"\nRows after cleaning: {len(df)}  (dropped {before - len(df)})")

    # Encode labels
    df["label_id"] = df[LABEL_COL].map(LABEL2ID)

    # ---- Train / Validation / Test split (70 / 10 / 20) ----
    train_val_df, test_df = train_test_split(
        df, test_size=TEST_SIZE, stratify=df["label_id"], random_state=SEED
    )
    train_df, val_df = train_test_split(
        train_val_df, test_size=0.125, stratify=train_val_df["label_id"], random_state=SEED
    )  # 0.125 of 80% ≈ 10% of total

    print(f"\nSplit  : train={len(train_df)}  val={len(val_df)}  test={len(test_df)}")

    # ---- Tokenizer & Model ----
    print("\n" + "=" * 60)
    print(f"Loading model: {BASE_MODEL}")
    print("=" * 60)

    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)

    model = AutoModelForSequenceClassification.from_pretrained(
        BASE_MODEL,
        num_labels=2,
        id2label=ID2LABEL,
        label2id=LABEL2ID,
    )
    model.to(device)

    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Total parameters    : {total_params:,}")
    print(f"Trainable parameters: {trainable_params:,}")

    # ---- Tokenize ----
    def make_hf_dataset(dataframe):
        ds = Dataset.from_dict({
            "text":  dataframe[TEXT_COL].tolist(),
            "label": dataframe["label_id"].tolist(),
        })
        return ds.map(
            lambda ex: tokenizer(
                ex["text"],
                truncation=True,
                max_length=MAX_LENGTH,
                padding=False,
            ),
            batched=True,
            remove_columns=["text"],
            desc="Tokenizing",
        )

    print("\nTokenizing splits ...")
    train_dataset = make_hf_dataset(train_df)
    val_dataset   = make_hf_dataset(val_df)
    test_dataset  = make_hf_dataset(test_df)

    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

    # ---- Training Arguments ----
    print("\n" + "=" * 60)
    print("Training configuration")
    print("=" * 60)

    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        num_train_epochs=NUM_EPOCHS,
        per_device_train_batch_size=TRAIN_BATCH,
        per_device_eval_batch_size=EVAL_BATCH,
        learning_rate=LEARNING_RATE,
        weight_decay=WEIGHT_DECAY,
        warmup_ratio=WARMUP_RATIO,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="f1",
        greater_is_better=True,
        logging_steps=50,
        logging_dir=os.path.join(OUTPUT_DIR, "logs"),
        fp16=torch.cuda.is_available(),
        push_to_hub=False,
        report_to="none",
        seed=SEED,
    )

    for key in ["num_train_epochs", "per_device_train_batch_size",
                "learning_rate", "weight_decay", "warmup_ratio", "fp16"]:
        print(f"  {key}: {getattr(training_args, key)}")

    # ---- Trainer ----
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
    )

    # ---- Train ----
    print("\n" + "=" * 60)
    print("Training started ...")
    print("=" * 60)

    train_result = trainer.train()

    print(f"\nTraining loss : {train_result.training_loss:.4f}")
    print(f"Training time : {train_result.metrics['train_runtime']:.1f} s")

    # ---- Validation Evaluation (per epoch already printed above) ----
    print("\n" + "=" * 60)
    print("Validation set evaluation (best checkpoint)")
    print("=" * 60)

    val_results = trainer.evaluate(val_dataset)
    print(f"  Loss      : {val_results['eval_loss']:.4f}")
    print(f"  Accuracy  : {val_results['eval_accuracy']:.4f}")
    print(f"  Precision : {val_results['eval_precision']:.4f}")
    print(f"  Recall    : {val_results['eval_recall']:.4f}")
    print(f"  F1        : {val_results['eval_f1']:.4f}")

    # ---- Test Evaluation ----
    print("\n" + "=" * 60)
    print("Test set evaluation")
    print("=" * 60)

    test_output   = trainer.predict(test_dataset)
    test_preds    = np.argmax(test_output.predictions, axis=1)
    test_labels   = test_output.label_ids

    test_accuracy  = accuracy_score(test_labels, test_preds)
    test_precision, test_recall, test_f1, _ = precision_recall_fscore_support(
        test_labels, test_preds, average="weighted"
    )
    test_loss = test_output.metrics["test_loss"]

    print(f"  Loss      : {test_loss:.4f}")
    print(f"  Accuracy  : {test_accuracy:.4f}  ({test_accuracy * 100:.2f}%)")
    print(f"  Precision : {test_precision:.4f}")
    print(f"  Recall    : {test_recall:.4f}")
    print(f"  F1        : {test_f1:.4f}")

    # Per-class classification report
    print("\nClassification Report:")
    print("-" * 60)
    print(classification_report(
        test_labels,
        test_preds,
        target_names=["negative", "positive"],
        digits=4,
    ))

    # Confusion matrix
    cm = confusion_matrix(test_labels, test_preds)
    print("Confusion Matrix  (rows=true, cols=predicted):")
    print(f"               negative  positive")
    print(f"  negative      {cm[0][0]:6d}    {cm[0][1]:6d}")
    print(f"  positive      {cm[1][0]:6d}    {cm[1][1]:6d}")

    # Per-label accuracy breakdown
    print("\nPer-class accuracy:")
    for idx, name in ID2LABEL.items():
        mask = test_labels == idx
        if mask.sum() > 0:
            cls_acc = accuracy_score(test_labels[mask], test_preds[mask])
            print(f"  {name:10s}: {cls_acc:.4f}  ({mask.sum()} samples)")

    # ---- Save ----
    print("\n" + "=" * 60)
    print(f"Saving model to {OUTPUT_DIR}_final ...")
    print("=" * 60)

    final_dir = OUTPUT_DIR + "_final"
    trainer.save_model(final_dir)
    tokenizer.save_pretrained(final_dir)

    if os.path.exists(final_dir):
        files = os.listdir(final_dir)
        for f in sorted(files):
            fpath = os.path.join(final_dir, f)
            if os.path.isfile(fpath):
                size_mb = os.path.getsize(fpath) / (1024 * 1024)
                print(f"  {f:40s} {size_mb:.2f} MB")

    # ---- Summary ----
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Model        : {BASE_MODEL}")
    print(f"  Dataset      : {DATA_PATH}  ({len(df)} samples)")
    print(f"  Train / Val / Test split: {len(train_df)} / {len(val_df)} / {len(test_df)}")
    print(f"  Epochs       : {NUM_EPOCHS}")
    print(f"  Best val F1  : {val_results['eval_f1']:.4f}")
    print(f"  Test Accuracy: {test_accuracy:.4f}")
    print(f"  Test F1      : {test_f1:.4f}")
    print(f"  Saved to     : {final_dir}")
    print("=" * 60)

    print(f"\nTo load the saved model:")
    print(f"  model = AutoModelForSequenceClassification.from_pretrained('{final_dir}')")
    print(f"  tokenizer = AutoTokenizer.from_pretrained('{final_dir}')")


if __name__ == "__main__":
    main()
