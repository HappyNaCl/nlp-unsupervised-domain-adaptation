---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags: [concept, dann, adversarial, domain-adaptation, nlp]
sources:
  - "[[DANN Original Paper (Ganin 2016)]]"
  - "[[Neural UDA in NLP Survey (Ramponi COLING2020)]]"
---

# ADDA (Adversarial Discriminative Domain Adaptation)

DANN variant by Tzeng et al. (CVPR 2017) that decouples feature extraction from domain alignment. Unlike DANN's joint training via a [[Gradient Reversal Layer]], ADDA uses separate pre-training and fine-tuning stages.

## How It Differs from DANN

| | DANN | ADDA |
|--|------|------|
| Training | Joint (one network) | Two-stage (separate source/target encoders) |
| Adversarial mechanism | Gradient Reversal Layer | GAN discriminator (separate optimizer) |
| Source weights | Shared with target | Frozen after pre-training |

**Stages:**
1. Pre-train source encoder + task classifier on labeled source data
2. Freeze source encoder; train a separate target encoder to fool a domain discriminator (GAN objective)

## Significance

Demonstrated that decoupled training (freeze source, adapt target) can outperform DANN's joint training. Knowledge distillation from source to target encoder is a common ADDA extension.

> [!gap] NLP evaluation
> ADDA has not been widely benchmarked in NLP domain adaptation; most NLP work uses DANN-style GRL or adapter-based methods. Its performance on text classification or NER is not documented in this vault.

## Related

[[DANN (Domain-Adversarial Neural Networks)]], [[Gradient Reversal Layer]], [[DANN for NLP Text Domain Adaptation]]
