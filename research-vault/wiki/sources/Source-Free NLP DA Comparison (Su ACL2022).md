---
type: source
status: summarized
source_type: paper
author: Xin Su, Yiyun Zhao, Steven Bethard
year: 2022
venue: ACL 2022
url: https://aclanthology.org/2022.acl-long.572
confidence: medium
key_claims:
  - Active learning yields consistent gains across all SemEval 2021 tasks and domains in source-free settings
  - Self-training and data augmentation are unreliable for source-free NLP DA
  - Source-free DA is particularly relevant for clinical NLP where data sharing is restricted
tags:
  - source
  - paper
  - source-free
  - domain-adaptation
  - nlp
  - active-learning
  - self-training
  - clinical
  - acl
created: 2026-04-27
updated: 2026-04-27
---

# A Comparison of Strategies for Source-Free Domain Adaptation (Su et al., ACL 2022)

First systematic comparison of source-free NLP DA strategies. Adapts methods that traditionally assume source data access — active learning, self-training, data augmentation — for the setting where only the trained model and unlabeled target data are available.

## Motivation

Data-sharing restrictions are common in clinical NLP (HIPAA, GDPR). Hospitals can share a trained model but not the patient records used to train it. Standard UDA methods cannot be applied in this setting.

## Strategies Compared

| Strategy | Source-Free Reliability | Notes |
|----------|------------------------|-------|
| **Active learning** | High — consistent gains | Requests labels for informative target samples; doesn't need source data |
| **Self-training** | Unreliable | Works without source regularization only when initial model is already strong |
| **Data augmentation** | Unreliable | Without source signal to anchor augmentation, representations drift |

## Key Finding

Active learning is the most reliable strategy for source-free NLP DA across all tasks tested. Self-training and data augmentation fail to consistently improve over the source model.

## Tasks Tested

SemEval 2021 Task 10 tasks and domains (including clinical NER and named entity disambiguation). Specific domain names and per-domain accuracy not reported in abstract.

## Significance

Establishes the source-free NLP DA problem as a distinct research area. Demonstrates that not all standard DA methods transfer to the source-free setting.

## Related

[[Source-Free NLP DA]], [[Self-Training for NLP DA]], [[NLP UDA Method Combinations]]
