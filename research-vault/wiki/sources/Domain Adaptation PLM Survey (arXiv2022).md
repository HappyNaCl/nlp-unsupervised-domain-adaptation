---
type: source
status: summarized
source_type: survey
author: Unknown (arXiv 2211.03154)
year: 2022
venue: arXiv cs.CL
url: https://arxiv.org/abs/2211.03154
confidence: medium
key_claims:
  - Domain adversarial training (DANN) on top of BERT is unstable and has little effect on cross-domain performance
  - Continual pretraining (DAPT) generally outperforms pure adversarial approaches for PLM-based DA
  - Combining DAPT with adversarial methods yields better results than either alone
  - No single method is universally optimal; tailored combinations work best
tags:
  - source
  - survey
  - nlp
  - dapt
  - dann
  - adversarial
  - plm
  - domain-adaptation
  - arxiv
created: 2026-04-27
updated: 2026-04-27
---

# On the Domain Adaptation and Generalization of PLMs: A Survey (arXiv 2022)

Survey of domain adaptation and generalization methods for pretrained language models (PLMs), covering DAPT, adversarial methods, adapters, and their combinations.

## Core Taxonomy

| Category | Methods |
|----------|---------|
| **Data Augmentation** | Importance sampling, pseudo-labeling, prompting |
| **Model Optimization** | Continual learning (DAPT), adversarial learning (domain discriminators), metric learning |
| **Personalization** | Posterior adaptation, parameter-efficient methods (adapters, LoRA) |

## Key Finding: DANN on PLMs Fails

> "Domain adversarial training on top of BERT is unstable and has little effect on cross-domain performance."

This is consistent with findings in [[Adversarial and Domain-Aware BERT (Guo ACL2020)]] and [[Neural UDA in NLP Survey (Ramponi COLING2020)]].

## Key Finding: DAPT > Adversarial Alone

Continual pretraining on unlabeled target-domain data (DAPT) generally outperforms pure adversarial domain alignment when applied to PLM-scale models.

## Key Finding: Combination Is Best

The survey recommends a combined loss function for optimal performance:

$$\mathcal{L}_{all} = \mathcal{L}_C(x_s, y_s) + \lambda_1 \cdot \mathcal{L}_{AT}(x_s, y_s) + \lambda_2 \cdot \mathcal{L}_{AD}(x_s, x_t)$$

Where $\mathcal{L}_C$ = task classification, $\mathcal{L}_{AT}$ = adversarial perturbation/robustness, $\mathcal{L}_{AD}$ = domain discrimination.

## Limitation

Survey is qualitative — no comparative benchmark tables with numerical results. Claims are drawn from literature synthesis, not new experiments.

## Related

[[Domain-Adaptive Pre-Training (DAPT)]], [[DANN for NLP Text Domain Adaptation]], [[Adapter + Adversarial Combination for NLP DA]]
