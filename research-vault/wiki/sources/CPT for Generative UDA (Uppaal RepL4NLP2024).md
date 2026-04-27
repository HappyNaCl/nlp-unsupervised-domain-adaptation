---
type: source
status: summarized
source_type: paper
author: "Rheeya Uppaal, Yixuan Li, Junjie Hu"
year: 2024
venue: "RepL4NLP 2024 (9th Workshop on Representation Learning for NLP, ACL)"
url: "https://aclanthology.org/2024.repl4nlp-1.9"
confidence: medium
key_claims:
  - "Continued pre-training (CPT/DAPT) has been underexplored for generative models in UDA compared to discriminative classification"
  - "CPT implicitly learns the downstream task while predicting masked words informative to that task"
  - "CPT trade-offs with domain-invariant representation methods vary across architectures, tuning approaches, and data regimes"
tags: [source, paper, dapt, cpt, generative, uda, nlp, instruction-tuning, representation-learning, 2024]
created: 2026-04-27
updated: 2026-04-27
---

# How Useful is Continued Pre-Training for Generative UDA? (Uppaal et al., RepL4NLP 2024)

Investigates the role of continued pre-training (CPT — essentially DAPT applied to generative models) for unsupervised domain adaptation in generative architectures. Most prior DAPT work targets discriminative classifiers (BERT, RoBERTa); this paper focuses on generative models (T5, GPT-style).

## Research Question

Does CPT help generative models for UDA the same way DAPT helps discriminative models?

## Key Findings

- CPT *implicitly* learns task-relevant information via domain-specific masked word prediction — even without explicit task supervision
- Trade-offs between CPT and domain-invariant representation methods depend on architecture, fine-tuning approach, and data availability
- Bridges the DAPT literature with instruction tuning methodology — CPT can serve as a stepping stone toward instruction-tuned domain specialists

## Significance

As the field moves toward generative LLMs (T5, LLaMA) for NLP tasks, the discriminative-focused DAPT literature needs re-evaluation. This paper begins that bridge.

> [!gap] Specific benchmark numbers not available from abstract
> No task-specific performance table accessible without full paper.

> [!gap] Generative DAPT vs. instruction tuning comparison
> The paper raises but does not fully resolve whether DAPT on a generative model is better or worse than few-shot prompting or instruction tuning with domain examples. This is an active open question.

## Relation to Existing Vault Concepts

- Extends [[Domain-Adaptive Pre-Training (DAPT)]] to generative architectures
- Connects DAPT to the instruction tuning paradigm — relevant as [[BERT]] (discriminative) is replaced by decoder-only LLMs in many applications

## Related

[[Domain-Adaptive Pre-Training (DAPT)]], [[Pre-training for Domain Adaptation]], [[NLP UDA Method Combinations]]
