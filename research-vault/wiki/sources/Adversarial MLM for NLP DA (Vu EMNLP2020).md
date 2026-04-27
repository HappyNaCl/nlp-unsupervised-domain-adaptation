---
type: source
status: summarized
source_type: paper
author: "Thuy-Trang Vu, Dinh Phung, Gholamreza Haffari"
year: 2020
venue: "EMNLP 2020"
url: "https://aclanthology.org/2020.emnlp-main.497"
confidence: high
key_claims:
  - "Adversarial masking of harder-to-reconstruct tokens outperforms random masking in DAPT by up to +1.64 F1"
  - "Token selection for masking is framed as a combinatorial optimization problem solved via variational relaxation and dynamic programming"
  - "Strategic masking allocation more effectively bridges domain knowledge gaps than standard MLM"
tags: [source, paper, dapt, adversarial-masking, mlm, ner, domain-adaptation, nlp, emnlp, 2020]
created: 2026-04-27
updated: 2026-04-27
---

# Effective UDA with Adversarially Trained Language Models (Vu et al., EMNLP 2020)

Proposes **adversarial masking** as a replacement for random masking in domain-adaptive pre-training (DAPT). Instead of randomly masking tokens during MLM, the method selects tokens that are *harder to reconstruct* — making the pre-training signal more informative for bridging the domain gap.

## Core Contribution

Standard DAPT uses random 15% masking (same as BERT pre-training). This paper argues that random masking is suboptimal for domain adaptation: it treats all tokens equally, but domain-specific tokens carry disproportionate information about the target domain.

**Adversarial masking** frames token selection as a minimax problem:
- The *masker* selects tokens that maximize the MLM reconstruction difficulty
- The *MLM* minimizes reconstruction loss on the adversarially selected tokens
- Result: the model is forced to learn harder, domain-specific token distributions

The combinatorial optimization is made tractable via variational lower bound + dynamic programming.

## Results

Tested on 6 NER cross-domain tasks:
- Up to **+1.64 F1** improvement over random masking baseline
- All 6 tasks show improvement

## Significance for DAPT

This is a DAPT *variant*, not a standalone method. It improves the pre-training step without changing the downstream fine-tuning pipeline. It can in principle be combined with any other adaptation method (adversarial alignment, adapters) on top.

> [!key-insight] Adversarial masking uses adversarial principles *inside* DAPT, not after it
> Unlike DANN which applies adversarial pressure to the feature extractor during fine-tuning, this method applies it within the pre-training masking strategy. The two mechanisms are orthogonal and potentially complementary.

## Relation to Other Methods

- **vs. Standard DAPT**: same architecture, better masking strategy — drop-in improvement
- **vs. DANN**: operates at different pipeline stage; could be combined
- **vs. Adversarial fine-tuning**: adversarial pressure here is on the *masking distribution*, not the *feature representation*

## Related

[[Domain-Adaptive Pre-Training (DAPT)]], [[DANN for NLP Text Domain Adaptation]], [[Pre-training for Domain Adaptation]]
