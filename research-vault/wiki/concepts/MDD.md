---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags: [concept, domain-adaptation, discrepancy, theory, margin, nlp]
sources:
  - "[[Neural UDA in NLP Survey (Ramponi COLING2020)]]"
  - "[[Domain Adaptation PLM Survey (arXiv2022)]]"
---

# MDD (Margin Disparity Discrepancy)

Distribution discrepancy measure for domain adaptation by Zhang et al. (ICML 2019). Provides a tighter theoretical upper bound on target error than the H-divergence used in [[DANN (Domain-Adversarial Neural Networks)]].

## Core Idea

Replaces the binary domain discriminator loss with a **margin-based** criterion: the discrepancy is measured in terms of the task classifier's margin on source vs. target — penalizing only misalignment that hurts the task objective.

## Vs. H-divergence (DANN)

| | DANN / H-divergence | MDD |
|--|---------------------|-----|
| Bound tightness | Loose (binary discriminator) | Tighter (margin-based) |
| Task coupling | Discriminator is separate | Directly uses task classifier margin |
| Implementation | GRL + domain head | Adversarial training on task head output |

## Significance

MDD achieves state-of-the-art on image DA benchmarks and has tighter generalization guarantees than DANN-style methods. Classified under [[Discrepancy Minimization for NLP DA]] method family.

> [!gap] NLP application
> MDD is documented primarily on image DA. Its direct application to NLP domain adaptation has not been covered in this vault.

## Related

[[DANN (Domain-Adversarial Neural Networks)]], [[Discrepancy Minimization for NLP DA]], [[Alignment-Discriminability Tradeoff]]
