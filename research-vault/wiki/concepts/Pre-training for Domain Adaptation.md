---
type: concept
status: developing
created: 2026-04-27
updated: 2026-04-27
tags: [concept, nlp, pretraining, domain-adaptation, bert, dapt]
sources:
  - "[[Don't Stop Pretraining (Gururangan ACL2020)]]"
  - "[[Adversarial and Domain-Aware BERT (Guo ACL2020)]]"
---

# Pre-training for Domain Adaptation

Using large-scale pre-training as a prior before applying domain adaptation techniques — specifically in NLP. Pre-training on general corpora (BERT, RoBERTa) implicitly reduces [[Distribution Shift]] by providing generic, semantically rich representations; domain-adaptive continued pre-training (DAPT) narrows the gap further by pre-training on target-domain text before fine-tuning.

## Two Levels of Pre-training for NLP DA

| Level | What it is | Example |
|-------|-----------|---------|
| **General LM pre-training** | Train on large mixed corpus (Wikipedia, BooksCorpus) | BERT, RoBERTa, GPT-2 |
| **Domain-adaptive pre-training (DAPT)** | Continue MLM pre-training on target-domain unlabeled text | BERT → continued training on Amazon reviews before sentiment fine-tuning |

## Why DAPT Helps

Pre-training on general corpora leaves a residual domain gap: BERT trained on Wikipedia performs worse on biomedical or Twitter text. Continued pre-training on target-domain text narrows this gap by adjusting the language model's internal representations toward the target distribution — before any labeled data is used.

> [!gap] Sources needed
> Key reference: "Don't Stop Pretraining" (Gururangan et al., ACL 2020). Not yet ingested.

## Relationship to Adapter + Adversarial Methods

Domain-aware post-training (target MLM / DAPT) serves as an implicit initialization step for subsequent adversarial fine-tuning. It shifts the PLM toward the target domain, reducing the initial domain gap and stabilizing the GRL training signal.

See [[Adversarial and Domain-Aware BERT (Guo ACL2020)]] for direct evidence: domain-aware BERT post-training + adversarial achieves 90.12% avg on Amazon cross-domain sentiment (+4.22% over SOTA).

See [[Research - DAPT vs DANN and Combining Them]] for full synthesis of when to use DAPT alone, DANN alone, or combined.

See [[Adapter + Adversarial Combination for NLP DA]] for the adapter-mediated adversarial pattern.

## Open Questions

> [!gap] DAPT vs adapter comparison
> Is domain-adaptive pre-training (full continued MLM) better or worse than inserting a domain-specific adapter (LoRA, Houlsby) and skipping the pre-training step? No direct head-to-head comparison found.

## Related

[[DANN for NLP Text Domain Adaptation]], [[Adapter + Adversarial Combination for NLP DA]], [[Adapters (NLP)]], [[Adversarial and Domain-Aware BERT (Guo ACL2020)]]
