---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags: [concept, domain-adaptation, scenario]
sources:
  - "[[Neural UDA in NLP Survey (Ramponi COLING2020)]]"
---

# Universal DA

The most general [[Unsupervised Domain Adaptation]] setting. No assumption is made about the relationship between source and target label spaces. Subsumes [[Closed-Set DA]], [[Partial DA]], and [[Open-Set DA]].

## Challenge

The model must simultaneously:
1. Transfer knowledge for shared classes
2. Reject target-private unknown classes
3. Ignore source-private classes to avoid negative transfer

> [!gap] No source yet
> Add UAN (You et al. 2019) or equivalent once ingested.
