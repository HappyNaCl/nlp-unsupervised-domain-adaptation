---
type: concept
status: developing
created: 2026-04-27
updated: 2026-04-27
tags: [concept, nlp, self-training, pseudo-label, domain-adaptation, iterative]
sources:
  - "[[DaMSTF (ACL2023)]]"
  - "[[Neural UDA in NLP Survey (Ramponi COLING2020)]]"
---

# Self-Training for NLP DA

An iterative UDA method: train on labeled source data, generate pseudo-labels for unlabeled target samples using model predictions, retrain on the expanded labeled set, repeat. Requires no architectural changes to the base model — only a labeling loop around standard supervised training.

## Core Algorithm

```
1. Train model on labeled source data D_S
2. Run inference on unlabeled target data D_T
3. Select high-confidence predictions as pseudo-labels
4. Retrain on D_S ∪ {high-confidence D_T pseudo-labels}
5. Repeat 2–4 until convergence
```

The confidence threshold for accepting pseudo-labels is a key hyperparameter. Too high: too few target samples added each round. Too low: noise accumulates.

## Variants

| Variant | Key idea | Notes |
|---------|---------|-------|
| **Vanilla self-training** | Fixed confidence threshold | Simple; error accumulation risk |
| **Cycle self-training (CST)** | Forward: pseudo-labels from target; Reverse: update shared features to perform on source | Prevents representation drift |
| **Meta self-training** | Meta-learning weights each pseudo-instance by quality | DaMSTF (ACL 2023) — combines with adversarial init |
| **TAPT self-training** | TAPT pre-training initializes before self-training | Gains are "strongly additive" (EMNLP 2021) |

## Relationship to Other Methods

**vs. DAPT**: DAPT shifts the LM representation; self-training directly adapts the classifier decision boundary on the target distribution. They are complementary: DAPT provides better initialized representations, self-training exploits them with target signal.

**vs. Adversarial**: adversarial alignment is done during training (pushes features to be domain-invariant); self-training is done after initial training (expands training set with target samples). DaMSTF combines adversarial as initialization → self-training as the main adaptation loop.

**vs. Contrastive DA**: contrastive methods learn a better representation space; self-training leverages whatever representation exists to expand labeled data.

## When Self-Training Works Well in NLP

- Large domain gap where explicit feature alignment (adversarial) fails
- Sufficient unlabeled target data for stable pseudo-label quality
- After DAPT or adversarial initialization (reduces initial pseudo-label noise)
- Tasks with low label ambiguity (sentiment: easier; NER: harder due to entity type confusion)

## Failure Modes

- **Error accumulation**: noise in early pseudo-labels propagates; model becomes overconfident on wrong labels
- **Confirmation bias**: model reinforces its own mistakes — the pseudo-label distribution skews toward majority class
- **Domain gap too large**: first-round pseudo-labels are too noisy; early stopping without initialization

> [!key-insight] Self-training is downstream of representation quality
> The better the initial model (via DAPT or adversarial init), the cleaner the pseudo-labels, and the more effective self-training becomes. This is why DaMSTF uses adversarial training as initialization only.

## Key Papers

- [[DaMSTF (ACL2023)]]: adversarial init + meta self-training; +4% over BERT
- Cycle Self-Training (Liu et al. arXiv 2021): cycles between target pseudo-labels and source domain to prevent representation drift
- Task-Adaptive Pre-training + Self-Training (EMNLP 2021 Findings): TAPT+self-training gains are strongly additive

## Related

[[DANN for NLP Text Domain Adaptation]], [[Domain-Adaptive Pre-Training (DAPT)]], [[NLP UDA Method Combinations]], [[DaMSTF (ACL2023)]]
