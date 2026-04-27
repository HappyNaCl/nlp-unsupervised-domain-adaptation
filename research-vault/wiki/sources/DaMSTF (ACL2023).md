---
type: source
status: summarized
source_type: paper
author: Hao Sun, Guangluan Xu, et al.
year: 2023
venue: ACL 2023
url: https://aclanthology.org/2023.acl-long.92
confidence: medium
key_claims:
  - Domain adversarial learning used as initialization for meta self-training — not as the main alignment method
  - Meta-learning module estimates pseudo-instance importance to reduce label noise in self-training
  - Combination of adversarial initialization + meta self-training improves BERT by ~4% on cross-domain sentiment
tags:
  - source
  - paper
  - adversarial
  - self-training
  - meta-learning
  - domain-adaptation
  - nlp
  - sentiment
  - acl
created: 2026-04-27
updated: 2026-04-27
---

# DaMSTF: Domain Adversarial Learning Enhanced Meta Self-Training (ACL 2023)

Combines domain adversarial learning (DANN-style) with meta self-training for NLP domain adaptation. Key insight: adversarial training is used as an *initialization* to prevent training guidance vanishment in self-training, not as the primary alignment signal.

## Architecture

Three components:
1. **Domain adversarial initialization**: DANN-style training to initialize feature extractor before self-training begins — gives the model a domain-invariant starting point
2. **Meta self-training**: assigns pseudo-labels to target samples, then uses meta-learning to weight each pseudo instance by quality
3. **Meta constructor**: builds the validation set used to evaluate pseudo-instance quality during meta-learning

## Key Insight

Standard self-training fails because pseudo-label noise accumulates. Standard DANN alone is limited on PLMs. DaMSTF uses DANN to warm-start the model (remove obvious domain artifacts), then lets self-training with meta-quality-weighting do the heavy lifting.

> [!key-insight] Adversarial as initialization, not alignment
> DANN here is a bootstrapping tool, not the end goal. It solves "training guidance vanishment" — the self-training loop collapsing if the initial pseudo-labels are too noisy.

## Results

- ~+4% improvement over BERT on cross-domain sentiment classification
- No specific per-task Amazon Reviews numbers in abstract

## Combination Pattern

`DANN (init) → pseudo-label generation → meta-weighted self-training`

This is a novel combination pattern: adversarial training is ephemeral (used for initialization only), and self-training is the actual adaptation driver.

## Related

[[DANN for NLP Text Domain Adaptation]], [[NLP UDA Method Combinations]], [[Adapter + Adversarial Combination for NLP DA]]
