---
type: source
status: summarized
source_type: paper
author: "Huiyun Yang, Huadong Chen, Xin Zhou, Daniel Povey"
year: 2022
venue: "ACL 2022"
url: "https://aclanthology.org/2022.acl-long.174"
confidence: high
key_claims:
  - "Separate domain-specific soft prompts (per-domain adapters) + adversarial alignment achieves SOTA cross-domain sentiment"
  - "Domain-specific soft prompts alleviate domain discrepancy at the input level"
  - "Adversarial training between each source and target domain learns domain-invariant representations"
  - "SOTA on both single-source and multi-source domain adaptation"
tags: [source, paper, adapter, soft-prompt, adversarial, dann, sentiment, nlp, cross-domain]
created: 2026-04-27
updated: 2026-04-27
---

# AdSPT: Adversarial Soft Prompt Tuning for Cross-Domain Sentiment Analysis (ACL 2022)

The most direct evidence for adapter + DANN working in NLP. Uses soft prompts (a form of input-side adapter) combined with adversarial domain alignment.

## What Are Soft Prompts Here?

Soft prompts are learnable continuous vectors prepended to the input — effectively a lightweight, parameter-efficient adapter operating at the input/embedding level. AdSPT trains **separate soft prompts per domain**, allowing the model to capture domain-specific distributional patterns without modifying BERT's weights.

## How Adversarial Training Is Applied

- Domain adversarial training is applied **per source-target pair**, not globally
- The adversarial objective is applied on top of the soft prompt representations — meaning the GRL operates on the adapter output, not BERT's internal layers
- BERT backbone remains largely frozen; the adversarial pressure is absorbed by the small prompt parameters

## Why This Avoids BERT's DANN Failure Mode

- The adversarial signal is applied to a small, task-specific parameter space (soft prompts)
- BERT's pre-trained representations are not disrupted by the GRL
- Domain-specific prompts already provide domain separation, so adversarial training has a cleaner signal to work with

## Key Insight

> [!key-insight] Adapter-first, adversarial-second
> Apply adversarial alignment through the adapter (soft prompt / bottleneck), not through BERT's full layers. This stabilizes training and achieves better domain invariance.

## Results

SOTA on cross-domain sentiment (single-source and multi-source settings). Specific numbers not recoverable from abstract alone.

## Related

[[DANN for NLP Text Domain Adaptation]], [[Adapters (NLP)]], [[Adapter + Adversarial Combination for NLP DA]]
