---
type: question
title: "UDA Problem Formulation From Scratch"
question: "Can you explain from the beginning what UDA tries to solve from the different distributions needed to be handled?"
answer_quality: solid
created: 2026-04-27
updated: 2026-04-27
tags: [question, uda, distribution-shift, covariate-shift, domain-adaptation, theory]
related:
  - "[[Distribution Shift]]"
  - "[[Covariate Shift]]"
  - "[[Domain Invariant Features]]"
  - "[[Domain-Adaptive Pre-Training (DAPT)]]"
  - "[[DANN for NLP Text Domain Adaptation]]"
  - "[[Unsupervised Domain Adaptation]]"
sources:
  - "[[DANN Original Paper (Ganin 2016)]]"
  - "[[Adversarial and Domain-Aware BERT (Guo ACL2020)]]"
  - "[[Neural UDA in NLP Survey (Ramponi COLING2020)]]"
status: developing
---

# UDA Problem Formulation From Scratch

## The Setup

You have:
- **Source domain**: labeled data $(X_S, Y_S)$ — e.g., Amazon Books reviews with sentiment labels
- **Target domain**: unlabeled data $X_T$ only — e.g., Amazon Electronics reviews, no labels

You train a model on source, deploy on target. It performs worse than expected. Why?

## The Core Problem: $P_S \neq P_T$

The source and target data don't come from the same distribution. A model that learns $P(Y|X)$ from source data is really learning a function that works well *given source inputs*. When target inputs arrive looking different, the learned function no longer applies correctly.

## Three Ways Distributions Can Differ

| Type | What shifts | What stays the same | UDA assumes this? |
|------|-------------|--------------------|--------------------|
| **[[Covariate Shift]]** | $P(X)$ — the inputs look different | $P(Y\|X)$ — the meaning of labels given input is the same | **Yes — standard assumption** |
| **Label shift** | $P(Y)$ — class frequencies differ | $P(X\|Y)$ — what each class looks like is the same | Sometimes |
| **Concept drift** | $P(Y\|X)$ — same input means something different | Nothing | No — breaks most UDA methods |

The **covariate shift assumption** is critical. UDA methods are only valid if the label function is the same across domains — just that vocabulary and writing style differ. If the definition of the label itself shifts, no alignment method saves you.

## What UDA Methods Therefore Try to Do

Under covariate shift, $P(Y|X)$ is identical in both domains. If you could make the model *see* both domains as looking the same, a classifier trained on source labels would automatically generalise to target.

This is **distribution alignment**: transform representations so $P_S(Z) \approx P_T(Z)$ in feature space, where $Z = f(X)$ is the encoder output.

## Two Levels of Shift to Fix (PLM-specific)

**Level 1 — Input distribution: $P_S(X) \neq P_T(X)$**

The raw text is already different before the model touches it. Target-domain vocabulary ("HDMI", "firmware") appears rarely or never in source. The encoder's representations for those tokens are undertrained and noisy. Feature alignment downstream cannot compensate for bad upstream representations.

**Fix**: [[Domain-Adaptive Pre-Training (DAPT)]] — continue MLM on unlabeled target text so the encoder learns to handle target-domain inputs.

**Level 2 — Feature distribution: $P_S(Z) \neq P_T(Z)$**

Even after DAPT, BERT encodes source and target into statistically distinguishable clusters in feature space. The classifier trained on the source cluster draws decision boundaries that don't transfer to the target cluster.

**Fix**: Adversarial alignment ([[DANN for NLP Text Domain Adaptation|DANN]]/GRL) — force the encoder to produce features a domain discriminator cannot distinguish.

## The Full Picture

```
Raw text → [DAPT fixes this gap] → Encoder → [DANN fixes this gap] → Classifier → Label
           P_S(X) ≠ P_T(X)                   P_S(Z) ≠ P_T(Z)
```

UDA is two nested problems. The input distribution determines what the encoder *can* represent; the feature distribution determines whether the classifier *generalises*. Methods that only address one level work partially at best.
