---
type: concept
status: developing
created: 2026-04-27
updated: 2026-04-27
tags: [concept, nlp, dapt, pretraining, domain-adaptation, bert, roberta]
sources:
  - "[[Don't Stop Pretraining (Gururangan ACL2020)]]"
  - "[[Adversarial and Domain-Aware BERT (Guo ACL2020)]]"
  - "[[Adversarial MLM for NLP DA (Vu EMNLP2020)]]"
  - "[[CPT for Generative UDA (Uppaal RepL4NLP2024)]]"
  - "[[DAPT Bangla Hate Speech (Fahim BLP2025)]]"
---

# Domain-Adaptive Pre-Training (DAPT)

Continued masked language model (MLM) pre-training on large amounts of unlabeled text from the target domain, performed on top of a pretrained language model (BERT, RoBERTa) before task fine-tuning. DAPT does not require any labeled data — it is purely self-supervised.

## How It Works

1. Start from a pretrained LM (e.g., RoBERTa)
2. Collect unlabeled text from the target domain (e.g., biomedical publications, product reviews)
3. Continue MLM training on this corpus for ~12.5K steps
4. Fine-tune the DAPT model on the downstream task as usual

The training objective is identical to the original pre-training — no new supervision signal. DAPT simply shifts the model's internal representations toward the target domain distribution.

## DAPT vs TAPT

| Technique | Data | Scale | Cost | When to use |
|-----------|------|-------|------|-------------|
| **DAPT** | Unlabeled domain text (broad) | Billions of tokens | 47 GB, 12.5K steps | When large in-domain unlabeled corpus is available |
| **TAPT** | Unlabeled task training set | KB–MB | 80 KB, 0.2K steps | Always; cheap and consistently helpful |
| **DAPT+TAPT** | Both, sequentially | Both | Additive | Best performance when compute allows |
| **500NN-TAPT** | kNN-selected domain-similar subset | MB | 24 MB, 9K steps | When full DAPT is too expensive |

TAPT is 60× faster and uses orders of magnitude less storage while often competitive with DAPT. The combination DAPT → TAPT → fine-tune achieves the best results on 7 of 8 tasks tested. (Source: [[Don't Stop Pretraining (Gururangan ACL2020)]])

## DAPT Gains Over Baseline (Gururangan ACL 2020)

Gains over RoBERTa vary significantly by domain and task:

| Domain | Max gain | Min gain | Notes |
|--------|---------|---------|-------|
| Computer Science | +12.4pp (ACL-ARC) | +3.5pp | Largest gains; domain far from web text |
| Biomedical | +2.3pp | +0.4pp | Moderate; biomedical text well-represented in pretrain |
| News | +1.6pp | 0.0pp | Small; news-like text already in RoBERTa pretrain |
| Reviews | +1.4pp | +0.4pp | Small; sentiment tasks somewhat domain-insensitive |

## DAPT vs DANN in NLP

| Aspect | DAPT | DANN (adversarial) |
|--------|------|--------------------|
| Supervision needed | None (self-supervised MLM) | None (UDA) |
| Stability on PLMs | High — standard gradient descent | Low — GRL on PLM layers causes instability |
| Gains on PLMs | Consistent +0.4 to +12.4pp | Near-zero or negative on raw BERT/RoBERTa |
| Compute cost | High (domain corpus, 12.5K steps) | Moderate (fine-tuning scale) |
| Domain gap addressed | Input distribution P(X) | Feature distribution P(Z) |
| Combine with adversarial? | Yes — DAPT first stabilizes adversarial | Recommended after DAPT, not before |

> [!key-insight] DAPT shifts the input distribution; adversarial aligns the feature distribution
> They operate on different levels of the pipeline and are complementary, not competing. DAPT first, adversarial second is the validated order.

## Combining DAPT + Adversarial Training

The combination is strictly better than either alone when applied correctly:
- DAPT first normalizes the PLM toward the target domain
- Adversarial training then closes the residual feature-level gap
- Crucially: DAPT stabilizes adversarial training by reducing the initial domain gap the GRL must bridge

Evidence: [[Adversarial and Domain-Aware BERT (Guo ACL2020)]] achieves 90.12% avg accuracy on Amazon cross-domain sentiment (12 tasks), +4.22% over prior SOTA, by combining domain-aware BERT post-training (a DAPT-like step) with adversarial training.

See [[Research - DAPT vs DANN and Combining Them]] for full synthesis.

## DAPT Variants

- **Adversarial masking** ([[Adversarial MLM for NLP DA (Vu EMNLP2020)]]): replaces random 15% token masking with adversarially-selected harder tokens, forcing the model to learn domain-specific distributions more effectively. Up to +1.64 F1 on 6 NER cross-domain tasks over standard DAPT. Drop-in improvement — same pipeline, better masking strategy.
- **Generative DAPT / CPT** ([[CPT for Generative UDA (Uppaal RepL4NLP2024)]]): applies continued pre-training to generative architectures (T5, GPT-style). Trade-offs with domain-invariant methods vary by architecture; bridges DAPT literature to instruction tuning paradigm.
- **Cross-lingual / low-resource DAPT** ([[DAPT Bangla Hate Speech (Fahim BLP2025)]]): DAPT on 315K+ Bangla social media comments achieves 0.7265 micro-F1 on hate speech detection — demonstrates DAPT generalizes to non-English low-resource settings with informal/social-media text.

## Open Questions

> [!gap] DAPT vs adapter as pre-training substitute
> Is continued domain MLM (DAPT, expensive) replaceable by a domain-specific LoRA adapter (cheap)? No direct head-to-head comparison exists as of 2024.

> [!gap] DAPT for instruction-tuned models
> DAPT was validated on BERT/RoBERTa. Its effect on instruction-tuned LLMs (LLaMA-3, Mistral) is less studied — 2023 biomedical work (BioNLP 2023) suggests gains persist but with different dynamics.

## Related

[[Pre-training for Domain Adaptation]], [[DANN for NLP Text Domain Adaptation]], [[Adapter + Adversarial Combination for NLP DA]], [[Don't Stop Pretraining (Gururangan ACL2020)]], [[Adversarial MLM for NLP DA (Vu EMNLP2020)]]
