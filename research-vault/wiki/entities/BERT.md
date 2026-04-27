---
type: entity
entity_type: model
status: seed
created: 2026-04-27
updated: 2026-04-27
tags: [entity, model, bert, transformer, nlp, pretraining]
---

# BERT

**BERT** (Bidirectional Encoder Representations from Transformers) by Devlin et al. (NAACL 2019). The foundational masked language model that established transformer-based pre-training as the dominant NLP paradigm. Trained on masked language modeling (MLM) and next sentence prediction (NSP) on BookCorpus + Wikipedia.

## Relevance to UDA

BERT is the primary backbone model in NLP UDA research. Key findings:

- Vanilla [[DANN (Domain-Adversarial Neural Networks)|DANN]] on raw BERT layers is unstable and adds near-zero benefit — see [[DANN for NLP Text Domain Adaptation]]
- [[Domain-Adaptive Pre-Training (DAPT)]] was validated on BERT and RoBERTa (Gururangan ACL 2020)
- [[Adapter + Adversarial Combination for NLP DA]]: the fix for DANN instability is to apply GRL to adapter output, not BERT layers

## Variants Used in NLP UDA

| Model | Parameters | Notes |
|-------|-----------|-------|
| BERT-base | 110M | Original; still common baseline |
| BERT-large | 340M | Higher capacity |
| RoBERTa | 125M / 355M | Improved training; most used in DAPT literature |
| BUET-BERT | — | Bangla-domain BERT; used in [[DAPT Bangla Hate Speech (Fahim BLP2025)]] |

## Related

[[Domain-Adaptive Pre-Training (DAPT)]], [[Adapters (NLP)]], [[DANN for NLP Text Domain Adaptation]]
