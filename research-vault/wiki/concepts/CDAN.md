---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags: [concept, dann, adversarial, domain-adaptation, conditional, nlp]
sources:
  - "[[DANN Original Paper (Ganin 2016)]]"
  - "[[Neural UDA in NLP Survey (Ramponi COLING2020)]]"
---

# CDAN (Conditional Domain Adversarial Network)

Extension of [[DANN (Domain-Adversarial Neural Networks)]] by Long et al. (NeurIPS 2018) that conditions the domain discriminator on classifier predictions, aligning class-conditional distributions rather than marginals.

## Core Idea

Standard DANN aligns the marginal feature distribution $P(Z)$, which can destroy class-discriminative structure when class distributions overlap across domains. CDAN aligns $P(Z \mid \hat{y})$ via multilinear conditioning:

$$h = z \otimes \hat{y}$$

The outer product of feature $z$ and classifier prediction $\hat{y}$ is the discriminator input, forcing domain alignment to respect class boundaries.

## Significance

Directly addresses the [[Alignment-Discriminability Tradeoff]]. Widely adopted as a stronger baseline over vanilla DANN on image DA benchmarks.

> [!gap] NLP evaluation
> CDAN has been evaluated primarily on image DA benchmarks. Its performance on NLP tasks (text classification, NER) is not documented in this vault.

## Related

[[DANN (Domain-Adversarial Neural Networks)]], [[Alignment-Discriminability Tradeoff]], [[Gradient Reversal Layer]]
