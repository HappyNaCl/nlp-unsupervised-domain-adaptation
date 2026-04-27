---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags: [concept, domain-adaptation, representation-learning]
sources:
  - "[[DANN Original Paper (Ganin 2016)]]"
  - "[[Neural UDA in NLP Survey (Ramponi COLING2020)]]"
---

# Domain Invariant Features

Learned representations that are statistically indistinguishable across domains — i.e., the feature extractor maps source and target inputs to overlapping distributions in the feature space.

## Motivation

If the feature distribution is identical across domains, a classifier trained on source features should transfer to target features.

## How They're Learned

- **Adversarial training**: feature extractor fools a domain discriminator (DANN paradigm)
- **Distance minimization**: minimize MMD, CORAL, or other discrepancy measures directly
- **Contrastive learning**: pull together cross-domain samples of the same class

## Limitations

> [!gap] No source yet
> The alignment-discriminability trade-off is a known open problem. Add relevant papers.

Domain invariance can conflict with class discriminability. Perfectly domain-invariant features may lose class-relevant structure needed for accurate classification.

## Related Concepts

[[Unsupervised Domain Adaptation]], [[Distribution Shift]]
