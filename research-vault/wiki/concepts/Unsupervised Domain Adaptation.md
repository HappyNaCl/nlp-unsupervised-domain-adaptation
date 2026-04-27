---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags: [concept, domain-adaptation, core]
sources:
  - "[[DANN Original Paper (Ganin 2016)]]"
  - "[[Neural UDA in NLP Survey (Ramponi COLING2020)]]"
  - "[[Domain Adaptation PLM Survey (arXiv2022)]]"
---

# Unsupervised Domain Adaptation

The task of adapting a model trained on a labeled **source domain** to perform well on an unlabeled **target domain**, where the two domains exhibit [[Distribution Shift]].

## Problem Setup

Given:
- Source domain: $\mathcal{D}_S = \{(x_i^s, y_i^s)\}_{i=1}^{n_s}$ — labeled samples
- Target domain: $\mathcal{D}_T = \{x_j^t\}_{j=1}^{n_t}$ — unlabeled samples
- Shared label space (in [[Closed-Set DA]])

Goal: learn a model $f: X \to Y$ that minimizes target risk $\mathcal{R}_T(f)$.

## Why It's Hard

> [!gap] Theoretical grounding needed
> Add Ben-David et al. bound once paper is ingested.

Without target labels, the model risks optimizing only for the source distribution, which does not transfer when $P_S(X) \neq P_T(X)$.

## Main Approaches

- **Adversarial alignment** — train a domain discriminator and a feature extractor adversarially to produce [[Domain Invariant Features]]
- **Discrepancy minimization** — directly minimize a distance metric (MMD, CORAL, [[MDD]]) between source and target feature distributions
- **Self-training** — assign pseudo-labels to confident target predictions and iteratively retrain
- **Normalization alignment** — match batch statistics across domains

## Scenarios

- [[Closed-Set DA]], [[Partial DA]], [[Open-Set DA]], [[Universal DA]]

## Key NLP Benchmarks

- **Amazon Reviews** (sentiment): 4 domains (Books, DVD, Electronics, Kitchen) — primary cross-domain sentiment benchmark
- **CoNLL-2003 / Twitter NER**: cross-domain NER (news → social media)
- **MultiNLI**: cross-genre NLI (10 genres)
- **FDU-MTL**: 16-domain multi-task sentiment
