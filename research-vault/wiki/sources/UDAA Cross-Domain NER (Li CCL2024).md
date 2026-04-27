---
type: source
status: summarized
source_type: paper
author: "Baofeng Li, Jianguo Tang, Yu Qin, Yuelou Xu, Yan Lu, Kai Wang, Lei Li, Yanquan Zhou"
year: 2024
venue: "CCL 2024 (23rd Chinese National Conference on Computational Linguistics)"
url: "https://aclanthology.org/2024.ccl-1.87"
confidence: medium
key_claims:
  - "Combining MLM auxiliary task with domain adversarial network achieves SOTA on three cross-domain NER datasets"
  - "Framework addresses zero-resource cross-domain NER (no labeled target domain data)"
tags: [source, paper, ner, adversarial, dapt, domain-adaptation, nlp, cross-domain, ccl, 2024]
created: 2026-04-27
updated: 2026-04-27
---

# UDAA: Unsupervised Domain Adaptation Adversarial Framework for Cross-Domain NER (Li et al., CCL 2024)

Combines masked language model auxiliary task with domain adversarial training for zero-resource cross-domain NER. The two components address complementary aspects of domain shift in NER.

## Architecture

Two components:
1. **MLM auxiliary task**: domain-adaptive pre-training signal — continued MLM on target domain text to shift representations toward the target domain
2. **Domain adaptive adversarial network**: domain discriminator trained adversarially to learn domain-invariant NER features

The combination follows the DAPT+adversarial pattern validated in sentiment DA (Du et al. ACL 2020), applied here to NER.

## Benchmarks

Cross-domain NER tested on three datasets:
- **CBS** (news/broadcast)
- **Twitter** (social media)
- **WNUT2016** (social media, emerging entities)

Claimed SOTA on all three.

## Significance

Demonstrates that the DAPT+adversarial combination pattern, validated on sentiment classification, extends to NER. Social media and news domains represent the most common cross-domain NER scenarios.

> [!gap] Specific benchmark numbers not available from abstract
> Exact F1 scores not recoverable without full paper access.

## Related

[[DANN for NLP Text Domain Adaptation]], [[Domain-Adaptive Pre-Training (DAPT)]], [[NLP UDA Method Combinations]], [[Adversarial and Domain-Aware BERT (Guo ACL2020)]]
