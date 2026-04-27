---
type: concept
status: developing
created: 2026-04-27
updated: 2026-04-27
tags: [concept, nlp, source-free, domain-adaptation, privacy, clinical, no-source-data]
sources:
  - "[[Neural UDA in NLP Survey (Ramponi COLING2020)]]"
  - "[[Source-Free NLP DA Comparison (Su ACL2022)]]"
---

# Source-Free NLP DA

Domain adaptation setting where the source dataset is unavailable at adaptation time. Only the trained source model and unlabeled target data are provided. Motivated by privacy constraints (clinical NLP, legal NLP) and data licensing restrictions.

## Problem Setup

| Standard UDA | Source-Free DA |
|-------------|---------------|
| Access to labeled $D_S$ and unlabeled $D_T$ | Only trained model $f_S$ + unlabeled $D_T$ |
| Can compute source loss during adaptation | No source loss signal |
| Can run adversarial training on both domains | No cross-domain training possible |

## Why It Matters

- **Clinical NLP**: patient data cannot be shared across institutions; hospitals can only share a trained model
- **Legal / IP constraints**: source domain data may be proprietary
- **Federated settings**: each node adapts a shared model to local domain without exposing its data

## Adaptation Strategies (Su et al., ACL 2022)

A direct NLP study comparing strategies on SemEval tasks and clinical NER:

| Strategy | Reliability | Notes |
|----------|-----------|-------|
| **Active learning** | High — consistent gains | Selects informative target samples for labeling; most reliable in source-free setting |
| **Self-training** | Unreliable | Pseudo-label noise without source signal to regularize; works only with good initial model |
| **Data augmentation** | Unreliable | Without source data, augmentation can drift the representation unpredictably |

> [!key-insight] Without source data, active learning dominates
> Self-training and data augmentation assume implicit access to a good initialization. Without source data to regularize, their benefits become inconsistent. Active learning sidesteps this by simply asking for more labels.

## Prompt-Assisted Source-Free DA (2024)

A 2024 approach (NAACL 2024) applies source-free DA to Question Answering:
- Uses prompt engineering + self-learning to adapt a QA model to target domain without source data
- LLM prompting provides a natural interface for source-free adaptation — the model's in-context knowledge substitutes for explicit source domain supervision

> [!gap] LLM prompting as universal source-free DA
> For LLM-scale models, in-context learning (ICL) with target-domain examples may be a better "source-free DA" strategy than traditional self-training. This connection has not been systematically explored.

## Relationship to Other Methods

- **Self-training** becomes more important and more risky in source-free settings: more important because it's one of few self-supervised signals; more risky because there's no source correction signal
- **DAPT is still applicable**: if unlabeled target text is available, DAPT can be run on the source model without needing the original source labels
- **Contrastive methods**: can be applied source-free using only target-domain pairs if pseudo-labels are available

## Key Papers

- [[Source-Free NLP DA Comparison (Su ACL2022)]]: systematic comparison of source-free strategies for NLP
- NAACL 2024: prompt-assisted source-free DA for QA

## Related

[[Self-Training for NLP DA]], [[Domain-Adaptive Pre-Training (DAPT)]], [[NLP UDA Method Combinations]], [[Source-Free NLP DA Comparison (Su ACL2022)]]
