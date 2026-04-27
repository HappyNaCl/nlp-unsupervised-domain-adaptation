---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags: [concept, domain-adaptation, scenario]
sources:
  - "[[DANN Original Paper (Ganin 2016)]]"
  - "[[Neural UDA in NLP Survey (Ramponi COLING2020)]]"
---

# Closed-Set DA

The standard [[Unsupervised Domain Adaptation]] setting. Source and target domains share the same label space: $\mathcal{Y}_S = \mathcal{Y}_T$.

## Why It's the Baseline

Most foundational UDA methods ([[DANN (Domain-Adversarial Neural Networks)|DANN]], [[ADDA]], CORAL, [[CDAN]]) assume closed-set. In NLP, the Amazon Reviews 4-domain sentiment split (Books, DVD, Electronics, Kitchen) is the canonical closed-set benchmark — all domains share the same binary sentiment label space.

## Limitations

Unrealistic for real-world deployment where target data may include novel or unknown categories. See [[Open-Set DA]] and [[Universal DA]].
