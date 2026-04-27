---
type: source
status: summarized
source_type: survey
author: Alan Ramponi, Barbara Plank
year: 2020
venue: COLING 2020
url: https://aclanthology.org/2020.coling-main.603
confidence: high
key_claims:
  - Comprehensive taxonomy of neural UDA methods in NLP as of 2020
  - Adversarial methods (DANN-style) are a major category but underperform on pretrained models
  - Sentiment classification is the most-studied NLP DA task
tags:
  - source
  - survey
  - nlp
  - domain-adaptation
  - dann
  - coling
created: 2026-04-27
updated: 2026-04-27
---

# Neural UDA in NLP: A Survey (Ramponi & Plank, COLING 2020)

Comprehensive survey of neural UDA methods in NLP up to 2020. Foundational reference for the field.

## Main Categories Covered

1. **Adversarial alignment** ([[DANN (Domain-Adversarial Neural Networks)|DANN]], [[ADDA]] variants): learn domain-invariant representations via discriminator
2. **Discrepancy minimization** (MMD, CORAL in text): directly minimize feature distribution distance
3. **Self-training / pseudo-labeling**: iteratively assign labels to target samples
4. **Domain-adversarial pre-training**: inject adversarial signals into the pre-training stage

## Known Limitation of DANN in NLP

Adversarial training is effective for feature-based models (BiLSTM, CNN-based) but becomes unstable and less beneficial when applied to BERT-scale pre-trained models. The survey notes this as an open problem.

> [!gap] Pre-BERT focus
> This survey predates the mass adoption of BERT-based UDA methods. The landscape has shifted significantly since 2020 — adapter-based methods and prompt-tuning approaches are now mainstream.

## Benchmark Landscape (as of 2020)

Amazon Reviews (sentiment) and CoNLL-2003 (NER) are the primary NLP DA benchmarks. DomainNet-text and MultiNLI cross-genre splits emerged later.

## Related

[[DANN for NLP Text Domain Adaptation]], [[Adapters (NLP)]]
