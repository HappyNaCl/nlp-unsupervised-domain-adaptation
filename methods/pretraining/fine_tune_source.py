"""
Fine-tune Domain-Adapted IndoBERT on Source Dataset

This script fine-tunes the domain-adapted IndoBERT (from MLM training) for sentiment 
classification using source_balanced.csv
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
    pipeline
)
from datasets import Dataset
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, classification_report


def compute_metrics(eval_pred):
    """Calculate evaluation metrics"""
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    
    # Calculate metrics
    accuracy = accuracy_score(labels, predictions)
    precision, recall, f1, _ = precision_recall_fscore_support(
        labels, predictions, average='weighted'
    )
    
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1
    }


def main():
    # ========================================================================
    # Check GPU availability
    # ========================================================================
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    # ========================================================================
    # Load Source Dataset
    # ========================================================================
    print("\n" + "="*60)
    print("Loading source dataset...")
    print("="*60)
    
    # Load source_balanced.csv
    df = pd.read_csv('./datasets/source_balanced.csv')
    
    print(f"Dataset shape: {df.shape}")
    print(f"\nColumns: {df.columns.tolist()}")
    print(f"\nLabel distribution:")
    print(df['label'].value_counts())
    print(f"\nFirst few rows:")
    print(df.head())
    
    # Create label mapping
    label2id = {'negative': 0, 'positive': 1}
    id2label = {0: 'negative', 1: 'positive'}
    
    # Convert labels to numeric
    df['label_id'] = df['label'].map(label2id)
    
    print("\nLabel mapping:")
    print(f"  negative → 0")
    print(f"  positive → 1")
    print(f"\nLabel distribution (numeric):")
    print(df['label_id'].value_counts().sort_index())
    
    # ========================================================================
    # Load Domain-Adapted Model
    # ========================================================================
    print("\n" + "="*60)
    print("Loading domain-adapted model...")
    print("="*60)
    
    model_path = "./models/indobert_mlm_target_final"
    
    print(f"Loading domain-adapted model from: {model_path}")
    
    # Load tokenizer (same as before)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    
    # Load model for sequence classification (not MLM)
    # This will add a classification head on top of the MLM-adapted base model
    model = AutoModelForSequenceClassification.from_pretrained(
        model_path,
        num_labels=2,
        id2label=id2label,
        label2id=label2id,
        ignore_mismatched_sizes=True  # Ignore the MLM head, use classification head instead
    )
    
    print(f"Model loaded successfully!")
    print(f"Model type: {model.__class__.__name__}")
    print(f"Number of labels: {model.config.num_labels}")
    
    # ========================================================================
    # Prepare Data for Training
    # ========================================================================
    print("\n" + "="*60)
    print("Preparing data for training...")
    print("="*60)
    
    # Create dataset from DataFrame
    dataset_dict = {
        "text": df['content'].tolist(),
        "label": df['label_id'].tolist()
    }
    
    dataset = Dataset.from_dict(dataset_dict)
    
    print(f"Dataset size: {len(dataset)}")
    print(f"Dataset features: {dataset.features}")
    print(f"\nFirst example:")
    print(dataset[0])
    
    # Tokenize the dataset
    def tokenize_function(examples):
        return tokenizer(
            examples["text"],
            truncation=True,
            max_length=512,
            padding=False  # Dynamic padding will be handled by data collator
        )
    
    print("\nTokenizing dataset...")
    tokenized_dataset = dataset.map(
        tokenize_function,
        batched=True,
        remove_columns=["text"],
        desc="Tokenizing"
    )
    
    print(f"Tokenization complete!")
    print(f"Tokenized dataset features: {tokenized_dataset.features}")
    
    # Split dataset into train and test (80/20 split)
    train_test_split = tokenized_dataset.train_test_split(test_size=0.2, seed=42)
    train_dataset = train_test_split['train']
    test_dataset = train_test_split['test']
    
    print(f"\nTraining samples: {len(train_dataset)}")
    print(f"Test samples: {len(test_dataset)}")
    
    # Create data collator for dynamic padding
    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
    
    print("\nData collator created for dynamic padding")
    
    # ========================================================================
    # Configure Training Parameters
    # ========================================================================
    print("\n" + "="*60)
    print("Configuring training parameters...")
    print("="*60)
    
    # Define training arguments
    training_args = TrainingArguments(
        output_dir="./models/indobert_source_finetuned",
        num_train_epochs=3,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        learning_rate=2e-5,
        weight_decay=0.01,
        warmup_steps=500,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="f1",
        greater_is_better=True,
        logging_steps=50,
        fp16=torch.cuda.is_available(),
        push_to_hub=False,
        report_to="none"
    )
    
    print("Training configuration:")
    print(f"  Epochs: {training_args.num_train_epochs}")
    print(f"  Batch size: {training_args.per_device_train_batch_size}")
    print(f"  Learning rate: {training_args.learning_rate}")
    print(f"  FP16: {training_args.fp16}")
    
    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
        data_collator=data_collator,
        compute_metrics=compute_metrics
    )
    
    print("\nTrainer initialized successfully!")
    
    # ========================================================================
    # Train the Model
    # ========================================================================
    print("\n" + "="*60)
    print("Starting fine-tuning on source domain data...")
    print("="*60)
    
    train_result = trainer.train()
    
    print("\n" + "="*60)
    print("Training completed!")
    print(f"Training loss: {train_result.training_loss:.4f}")
    print(f"Training time: {train_result.metrics['train_runtime']:.2f} seconds")
    
    # ========================================================================
    # Evaluate the Model
    # ========================================================================
    print("\n" + "="*60)
    print("Evaluating model on test set...")
    print("="*60)
    
    eval_results = trainer.evaluate()
    
    print("\nTest Set Results:")
    print(f"  Accuracy:  {eval_results['eval_accuracy']:.4f}")
    print(f"  Precision: {eval_results['eval_precision']:.4f}")
    print(f"  Recall:    {eval_results['eval_recall']:.4f}")
    print(f"  F1 Score:  {eval_results['eval_f1']:.4f}")
    print(f"  Loss:      {eval_results['eval_loss']:.4f}")
    
    # Get detailed predictions for classification report
    predictions = trainer.predict(test_dataset)
    pred_labels = np.argmax(predictions.predictions, axis=1)
    true_labels = predictions.label_ids
    
    # Print detailed classification report
    print("\nDetailed Classification Report:")
    print("="*60)
    print(classification_report(
        true_labels, 
        pred_labels, 
        target_names=['negative', 'positive'],
        digits=4
    ))
    
    # ========================================================================
    # Save the Fine-tuned Model
    # ========================================================================
    print("\n" + "="*60)
    print("Saving the fine-tuned model...")
    print("="*60)
    
    output_dir = "./models/indobert_source_final"
    
    print(f"Saving model to {output_dir}...")
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)
    
    # Verify saved files
    if os.path.exists(output_dir):
        files = os.listdir(output_dir)
        print(f"\nSaved files in {output_dir}:")
        for file in files:
            file_path = os.path.join(output_dir, file)
            if os.path.isfile(file_path):
                size_mb = os.path.getsize(file_path) / (1024 * 1024)
                print(f"  - {file:30s} ({size_mb:.2f} MB)")
    
    print(f"\n✓ Model and tokenizer saved successfully to: {output_dir}")
    print(f"\nTo load the model later, use:")
    print(f"  from transformers import AutoModelForSequenceClassification, AutoTokenizer")
    print(f"  model = AutoModelForSequenceClassification.from_pretrained('{output_dir}')")
    print(f"  tokenizer = AutoTokenizer.from_pretrained('{output_dir}')")
    
    # ========================================================================
    # Test Predictions on Mixed Test Set (Source + Target)
    # ========================================================================
    print("\n" + "="*60)
    print("Testing on mixed_test.csv (source + target domains)...")
    print("="*60)
    
    # Load mixed test set
    mixed_test_df = pd.read_csv('./datasets/mixed_test.csv')
    print(f"\nMixed test set shape: {mixed_test_df.shape}")
    print(f"Columns: {mixed_test_df.columns.tolist()}")
    print(f"\nDistribution by origin:")
    print(mixed_test_df['origin'].value_counts())
    
    # Convert labels to numeric
    mixed_test_df['label_id'] = mixed_test_df['label'].map(label2id)
    
    # Create dataset
    mixed_test_dict = {
        "text": mixed_test_df['content'].tolist(),
        "label": mixed_test_df['label_id'].tolist()
    }
    
    mixed_test_dataset = Dataset.from_dict(mixed_test_dict)
    
    # Tokenize
    print("\nTokenizing mixed test data...")
    mixed_test_tokenized = mixed_test_dataset.map(
        tokenize_function,
        batched=True,
        remove_columns=["text"],
        desc="Tokenizing mixed test"
    )
    
    # Make predictions
    print("\nMaking predictions on mixed test set...")
    mixed_predictions = trainer.predict(mixed_test_tokenized)
    mixed_pred_labels = np.argmax(mixed_predictions.predictions, axis=1)
    mixed_true_labels = mixed_predictions.label_ids
    
    # Add predictions to dataframe
    mixed_test_df['predicted_label_id'] = mixed_pred_labels
    mixed_test_df['predicted_label'] = mixed_test_df['predicted_label_id'].map(id2label)
    
    # Overall accuracy
    overall_accuracy = accuracy_score(mixed_true_labels, mixed_pred_labels)
    print(f"\n{'='*60}")
    print(f"OVERALL ACCURACY: {overall_accuracy:.4f} ({overall_accuracy*100:.2f}%)")
    print(f"{'='*60}")
    
    # Accuracy by origin
    print("\n" + "="*60)
    print("ACCURACY BY ORIGIN (SOURCE/TARGET)")
    print("="*60)
    
    for origin in mixed_test_df['origin'].unique():
        origin_mask = mixed_test_df['origin'] == origin
        origin_df = mixed_test_df[origin_mask]
        
        origin_true = origin_df['label_id'].values
        origin_pred = origin_df['predicted_label_id'].values
        
        origin_accuracy = accuracy_score(origin_true, origin_pred)
        origin_precision, origin_recall, origin_f1, _ = precision_recall_fscore_support(
            origin_true, origin_pred, average='weighted'
        )
        
        print(f"\n{origin.upper()} Domain:")
        print(f"  Samples:   {len(origin_df)}")
        print(f"  Accuracy:  {origin_accuracy:.4f} ({origin_accuracy*100:.2f}%)")
        print(f"  Precision: {origin_precision:.4f}")
        print(f"  Recall:    {origin_recall:.4f}")
        print(f"  F1 Score:  {origin_f1:.4f}")
        
        # Show classification report for this origin
        print(f"\n  Classification Report for {origin.upper()}:")
        print("  " + "-"*56)
        report = classification_report(
            origin_true, 
            origin_pred, 
            target_names=['negative', 'positive'],
            digits=4
        )
        # Indent the report
        for line in report.split('\n'):
            print(f"  {line}")
    
    print("\n" + "="*60)
    print("Testing complete!")
    print("="*60)


if __name__ == "__main__":
    main()
