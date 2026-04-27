---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags: [concept, domain-adaptation, scenario]
sources:
  - "[[Neural UDA in NLP Survey (Ramponi COLING2020)]]"
---

# Open-Set DA

A variant of [[Unsupervised Domain Adaptation]] where the target domain contains samples from classes **not present in the source**. The model must recognize and reject (or label as "unknown") these novel categories.

## Challenge

Feature alignment methods optimized for [[Closed-Set DA]] risk aligning unknown-class target samples to source classes, degrading performance.

## Related Scenarios

[[Partial DA]], [[Universal DA]]
