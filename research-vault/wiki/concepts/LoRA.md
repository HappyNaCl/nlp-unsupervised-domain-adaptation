---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags: [concept, adapter, peft, lora, fine-tuning, nlp]
sources:
  - "[[AdSPT Adversarial Soft Prompt Tuning (ACL2022)]]"
  - "[[UDAPTER (Malik EACL2023)]]"
---

# LoRA (Low-Rank Adaptation)

Parameter-efficient fine-tuning method by Hu et al. (ICLR 2022). Decomposes weight updates into low-rank matrices instead of updating all parameters:

$$W' = W_0 + BA, \quad B \in \mathbb{R}^{d \times r},\ A \in \mathbb{R}^{r \times k},\ r \ll \min(d,k)$$

During training only $A$ and $B$ are updated; the original weight matrix $W_0$ is frozen. Typical rank $r = 4$–$16$ yields ~0.1–1% trainable parameters.

## Relevance to NLP DA

LoRA is the dominant adapter variant as of 2023–present and is directly applicable to [[Adapter + Adversarial Combination for NLP DA]]:
- Insert LoRA matrices into BERT attention layers → serve as the trainable adapter
- Apply [[Gradient Reversal Layer]] to LoRA output → adversarial pressure absorbed by low-rank matrices, base model stays frozen

> [!gap] LoRA + GRL vs. soft-prompt + GRL
> AdSPT (SOTA) uses soft prompts as the adversarial target. Whether LoRA + GRL achieves comparable results is an open question — no systematic comparison exists as of 2024.

## Comparison to Other Adapters

See [[Adapters (NLP)]] for the full comparison table (Houlsby, LoRA, prefix tuning, soft prompts).

## Related

[[Adapters (NLP)]], [[Adapter + Adversarial Combination for NLP DA]]
