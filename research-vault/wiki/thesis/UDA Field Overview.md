---
type: thesis
status: seed
created: 2026-04-27
updated: 2026-04-27
tags: [thesis, domain-adaptation, synthesis]
sources:
  - "[[DANN Original Paper (Ganin 2016)]]"
  - "[[Neural UDA in NLP Survey (Ramponi COLING2020)]]"
  - "[[Don't Stop Pretraining (Gururangan ACL2020)]]"
  - "[[Domain Adaptation PLM Survey (arXiv2022)]]"
---

# UDA Field Overview

The evolving state of the Unsupervised Domain Adaptation field. Updated as papers are ingested.

## Current Consensus

> [!gap] Not yet sourced
> This section will develop as papers are ingested. Initial structure based on general field knowledge.

[[Unsupervised Domain Adaptation]] is now a mature subfield of transfer learning. The dominant paradigms are adversarial feature alignment and self-training with pseudo-labels. Attention-based and transformer architectures are the current backbone of choice.

## Dominant Paradigms

### 1. Adversarial Alignment (DANN lineage)
Feature extractor trained adversarially against a domain discriminator to produce [[Domain Invariant Features]].

### 2. Discrepancy Minimization
Directly minimize distribution distance (MMD, CORAL, [[MDD]]) between source and target in feature space.

### 3. Self-Training / Pseudo-Labels
Assign pseudo-labels to high-confidence target predictions; iteratively retrain. Risk: error accumulation.

### 4. Pre-trained Language Model Adaptation
PLMs (BERT, RoBERTa) as backbones have become dominant in NLP DA. Domain-adaptive pre-training (DAPT) and adapter-mediated adversarial alignment are the current techniques of choice.

## Open Debates

> [!gap] Populate as papers are ingested

- How much does pre-training on large-scale data reduce the need for explicit adaptation?
- Is distribution alignment necessary or sufficient for adaptation?
- How to handle the alignment-discriminability trade-off?

## Timeline

| Era | Dominant Methods | Notes |
|-----|-----------------|-------|
| ~2015 | CORAL, MMD-based | Hand-crafted feature alignment |
| ~2016–2018 | [[DANN (Domain-Adversarial Neural Networks)|DANN]], [[ADDA]], [[CDAN]] | Adversarial training era |
| ~2019–2020 | Self-training, pseudo-labels | SHOT, MCC |
| ~2020–2022 | BERT + adversarial (NLP) | DANN fails on raw BERT; DAPT + adapter fixes emerge |
| ~2022–present | Adapter + adversarial (NLP) | LoRA/soft-prompt + GRL on adapter output; AdSPT SOTA |

## Related Pages

[[Unsupervised Domain Adaptation]], [[Distribution Shift]], [[Domain Invariant Features]]
