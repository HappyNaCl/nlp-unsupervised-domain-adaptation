---
type: concept
status: developing
created: 2026-04-27
updated: 2026-04-27
tags: [concept, nlp, adapter, peft, domain-adaptation]
sources:
  - "[[AdSPT Adversarial Soft Prompt Tuning (ACL2022)]]"
  - "[[Neural UDA in NLP Survey (Ramponi COLING2020)]]"
---

# Adapters (NLP)

Lightweight parameter-efficient modules inserted into or prepended to a frozen pretrained language model. During fine-tuning, only the adapter weights are updated — the base model (BERT, RoBERTa, LLaMA, etc.) remains frozen.

## Common Adapter Types

| Type | Where inserted | Parameters | Notes |
|------|---------------|------------|-------|
| **Houlsby bottleneck** | After each transformer sub-layer | ~0.5–3% of base | Original adapter (2019) |
| **Prefix tuning** | Prepended to each layer's key/value | Very small | Tunable "virtual tokens" |
| **Soft prompts** | Prepended to input embeddings | Tiny | Simplest form |
| **[[LoRA]]** | Low-rank decomposition of weight matrices | ~0.1–1% | Most popular 2023–present |
| **Adapter fusion** | Combines pre-trained adapters | Variable | Multi-task composition |

## Why Adapters Matter for Domain Adaptation

1. **Preserve pre-trained knowledge**: frozen base model prevents catastrophic forgetting — the critical failure mode of DANN on [[BERT]]
2. **Domain-specific modules**: train separate adapters per domain, compose at inference
3. **Stable training target**: adversarial signals can be applied to the small adapter parameters without destabilizing the full model

## Adapters vs. Full Fine-Tuning for DA

| Criterion | Full fine-tuning | Adapters |
|-----------|-----------------|---------|
| Pre-trained knowledge preservation | Low (risk of forgetting) | High (base frozen) |
| Training stability with adversarial | Poor | Better |
| Domain-specific parameters | Shared | Isolated per domain |
| Storage cost | N × full model | 1 base + N × small adapter |
| Performance on easy DA | Competitive | Competitive |
| Performance on large domain gap | Better | Needs adversarial augmentation |

## Combining with Adversarial Training

See [[Adapter + Adversarial Combination for NLP DA]] for the recommended pattern.

## Related

[[DANN for NLP Text Domain Adaptation]], [[Adapter + Adversarial Combination for NLP DA]], [[Pre-training for Domain Adaptation]]
