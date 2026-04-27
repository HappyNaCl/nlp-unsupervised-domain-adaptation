---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags: [concept, domain-adaptation, theory]
sources:
  - "[[Neural UDA in NLP Survey (Ramponi COLING2020)]]"
---

# Covariate Shift

A specific form of [[Distribution Shift]] where the marginal input distribution differs between source and target ($P_S(X) \neq P_T(X)$) but the conditional label distribution is assumed identical ($P_S(Y|X) = P_T(Y|X)$).

## Why It Matters for UDA

Most UDA methods are designed under this assumption. If it holds, aligning the marginal feature distributions is sufficient for transfer.

## Standard Correction

Importance weighting: reweight source samples by $w(x) = P_T(x) / P_S(x)$ to minimize target risk. Impractical in high dimensions.

## When the Assumption Breaks

If $P(Y|X)$ also shifts (concept drift), feature alignment alone will not suffice.

## Related

[[Distribution Shift]], [[Unsupervised Domain Adaptation]]
