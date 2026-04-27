---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags: [concept, domain-adaptation, scenario]
sources:
  - "[[Neural UDA in NLP Survey (Ramponi COLING2020)]]"
---

# Partial DA

A variant of [[Unsupervised Domain Adaptation]] where the target label space is a **subset** of the source label space: $\mathcal{Y}_T \subset \mathcal{Y}_S$.

## Challenge

Standard alignment methods suffer from **negative transfer**: aligning source classes absent in the target domain introduces noise. Methods must identify and upweight source samples whose classes appear in the target.

## Related Scenarios

[[Open-Set DA]], [[Universal DA]], [[Closed-Set DA]]
