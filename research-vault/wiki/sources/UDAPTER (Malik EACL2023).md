---
type: source
status: summarized
source_type: paper
author: Bhavitvya Malik, Abhinav Ramesh Kashyap, Min-Yen Kan, Soujanya Poria
year: 2023
venue: EACL 2023
url: https://aclanthology.org/2023.eacl-main.165
confidence: medium
key_claims:
  - Adapter-based UDA outperforms DANN and DSN on cross-domain sentiment classification
  - Parameter-efficient adapter methods achieve competitive results with far fewer trainable parameters than full fine-tuning
  - Within 0.85% F1 of full fine-tuning methods on MNLI
  - "Two architectures: sequential (domain adapter → task adapter) and joint (classifier + divergence minimization)"
tags:
  - source
  - paper
  - adapter
  - domain-adaptation
  - nlp
  - uda
  - divergence
  - eacl
created: 2026-04-27
updated: 2026-04-27
---

# UDApter: Efficient Domain Adaptation Using Adapters (Malik et al., EACL 2023)

Parameter-efficient UDA using adapter modules. Proposes two adapter-based architectures that outperform DANN and DSN on cross-domain sentiment while fine-tuning only a fraction of total parameters.

## Two Architectures

**Method 1 — Sequential adapters:**
1. Train a *domain adapter* on source+target unlabeled data to learn domain-invariant representations
2. Freeze domain adapter; add a *task adapter* trained on labeled source data for task-specific learning
3. At inference: domain adapter → task adapter → classifier

**Method 2 — Joint learning with divergence minimization:**
- Jointly trains a supervised classifier and minimizes the divergence between source and target feature distributions
- Divergence measure reduces domain discrepancy without adversarial dynamics

Neither method uses DAPT (continued domain MLM) — the domain alignment is handled entirely within the adapter modules via divergence minimization.

## Key Results

- **Sentiment (Amazon Reviews)**: outperforms DANN and DSN — specific accuracy numbers not in abstract
- **MNLI**: within 0.85% F1 of full fine-tuning baselines
- Achieves this while training only a small fraction of the model parameters

## Significance

Demonstrates that adapters can perform domain alignment (previously the job of DANN/GRL) more efficiently and stably. Directly competes with adversarial methods and wins on sentiment DA tasks.

## Related

[[Adapters (NLP)]], [[DANN for NLP Text Domain Adaptation]], [[Adapter + Adversarial Combination for NLP DA]], [[NLP UDA Method Combinations]]
