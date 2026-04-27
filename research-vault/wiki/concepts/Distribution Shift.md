---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags: [concept, domain-adaptation, core]
sources:
  - "[[Neural UDA in NLP Survey (Ramponi COLING2020)]]"
  - "[[Domain Adaptation PLM Survey (arXiv2022)]]"
---

# Distribution Shift

The statistical mismatch between the distribution of training data (source) and deployment data (target). The root cause of [[Unsupervised Domain Adaptation|UDA's]] core challenge.

## Types

| Type | Formal definition | UDA relevance |
|------|------------------|---------------|
| [[Covariate Shift]] | $P_S(X) \neq P_T(X)$, $P_S(Y\|X) = P_T(Y\|X)$ | Most common assumption in UDA |
| Label shift | $P_S(Y) \neq P_T(Y)$, $P_S(X\|Y) = P_T(X\|Y)$ | Relevant to [[Partial DA]] |
| Concept drift | $P_S(Y\|X) \neq P_T(Y\|X)$ | Hardest; violates most UDA assumptions |

## Implications

Most UDA methods implicitly assume covariate shift. If concept drift is present, feature alignment alone cannot close the gap.

> [!gap] No source yet
> Add formal treatment from Ben-David et al. or Sugiyama et al. once ingested.
