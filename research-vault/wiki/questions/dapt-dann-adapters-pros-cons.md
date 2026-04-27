---
type: question
title: "DAPT vs DANN vs Adapters: Pros and Cons"
question: "List pros and cons for DAPT, DANN, and adapters."
answer_quality: solid
created: 2026-04-27
updated: 2026-04-27
tags: [question, dapt, dann, adapter, comparison, domain-adaptation, nlp]
related:
  - "[[Domain-Adaptive Pre-Training (DAPT)]]"
  - "[[DANN for NLP Text Domain Adaptation]]"
  - "[[Adapters (NLP)]]"
  - "[[Alignment-Discriminability Tradeoff]]"
  - "[[Research - DAPT Adapter DANN Full Stack]]"
sources:
  - "[[Adversarial and Domain-Aware BERT (Guo ACL2020)]]"
  - "[[Domain Adaptation PLM Survey (arXiv2022)]]"
  - "[[AdSPT Adversarial Soft Prompt Tuning (ACL2022)]]"
status: developing
---

# DAPT vs DANN vs Adapters: Pros and Cons

## DAPT

**Pros**
- Directly fixes the input distribution gap — the root cause of PLM failure on new domains
- Stable training: plain MLM, no adversarial dynamics to tune
- Strong empirical gains on BERT/RoBERTa (+0.4–12.4pp over baseline across NLP tasks)
- Orthogonal to every other method — stacks cleanly on top of DANN or adapters
- Works with any amount of unlabeled target text

**Cons**
- Computationally expensive — runs full MLM training on the target corpus
- Does not address feature-level misalignment ($P_S(Z) \neq P_T(Z)$ remains after DAPT)
- Diminishing returns if the target corpus is small or very noisy
- No mechanism for enforcing domain invariance — just better input coverage

## DANN (adversarial alignment / GRL)

**Pros**
- Directly optimises for domain-invariant features — targets the right problem (feature shift)
- Principled theoretical grounding (Ben-David et al. H-divergence bound)
- Works without any target labels
- Flexible: GRL can be inserted at any layer

**Cons**
- Unstable on raw BERT — adversarial gradient disrupts pretrained representations; degrades without DAPT first (Guo et al. ACL2020 showed this empirically)
- Aligns *marginal* distributions $P(Z)$, ignoring class structure → can hurt discriminability (see [[Alignment-Discriminability Tradeoff]])
- Sensitive to hyperparameters: $\lambda$ schedule for GRL needs careful tuning
- Training instability: adversarial objectives can oscillate or collapse

## Adapters

**Pros**
- Parameter-efficient: only 0.1–3% of base model parameters trained
- Preserve pretrained knowledge: frozen base prevents catastrophic forgetting
- Stable target for adversarial training — GRL gradient absorbed by small adapter, not full BERT
- Domain-specific: train separate adapters per domain, compose at inference
- Storage-efficient: one frozen base + $N$ small adapter sets vs. $N$ full model copies

**Cons**
- Small parameter budget limits capacity — may not capture very large domain gaps alone
- Do not directly address feature misalignment; need adversarial augmentation for hard DA tasks
- Interpretability: especially soft prompts have no human-readable meaning
- LoRA/prefix tuning add architecture complexity compared to full fine-tuning

## Quick Comparison

| | Fixes input shift | Fixes feature shift | Training stability | Param cost |
|---|---|---|---|---|
| DAPT | ✓ | ✗ | High | High (MLM) |
| DANN | ✗ | ✓ | Low (on raw BERT) | Low |
| Adapters | Partial | Partial | High | Very low |
| DAPT + Adapters + DANN | ✓ | ✓ | Medium | Medium |
