---
type: source
status: summarized
source_type: paper
author: Suchin Gururangan, Ana Marasović, Swabha Swayamditta, Kyle Lo, Iz Beltagy, Doug Downey, Noah A. Smith
year: 2020
venue: ACL 2020
url: https://aclanthology.org/2020.acl-main.740
confidence: high
key_claims:
  - Domain-adaptive pretraining (DAPT) on unlabeled in-domain text consistently improves over generic RoBERTa baseline
  - Task-adaptive pretraining (TAPT) on task-specific unlabeled text adds further gains, even after DAPT
  - DAPT+TAPT achieves best performance on 7 of 8 classification tasks across 4 domains
  - 500-nearest-neighbor TAPT approximates DAPT-scale gains at far lower cost
tags:
  - source
  - paper
  - dapt
  - pretraining
  - nlp
  - domain-adaptation
  - roberta
created: 2026-04-27
updated: 2026-04-27
---

# Don't Stop Pretraining (Gururangan et al., ACL 2020)

Canonical paper introducing DAPT (domain-adaptive pretraining) and TAPT (task-adaptive pretraining) as continued pre-training strategies for NLP domain adaptation. ACL 2020 Honorable Mention for Best Overall Paper.

## Core Contribution

Two continued pre-training strategies on top of RoBERTa:

| Strategy | Data | Scale | Steps |
|----------|------|-------|-------|
| **DAPT** | Unlabeled text from the target domain (broad) | Billions of tokens | ~12.5K |
| **TAPT** | Unlabeled text from the task's training set | KB–MB | ~100 epochs |
| **DAPT+TAPT** | DAPT first, then TAPT | Both | Additive |

Both use continued masked language modeling (MLM) — same objective as BERT/RoBERTa pre-training, no new training signal.

## Benchmark Results: DAPT Gains Over RoBERTa

Tested across 4 domains, 8 classification tasks:

| Domain | Task | RoBERTa | DAPT | Δ |
|--------|------|---------|------|---|
| Biomedical | ChemProt | 81.9 | 84.2 | +2.3 |
| Biomedical | RCT | 87.2 | 87.6 | +0.4 |
| CS | ACL-ARC | 63.0 | 75.4 | **+12.4** |
| CS | SciERC | 77.3 | 80.8 | +3.5 |
| News | HyperPartisan | 86.6 | 88.2 | +1.6 |
| News | AGNews | 93.9 | 93.9 | 0.0 |
| Reviews | Helpfulness | 65.1 | 66.5 | +1.4 |
| Reviews | IMDB | 95.0 | 95.4 | +0.4 |

## DAPT+TAPT Combined (Best Results)

DAPT+TAPT wins on 7/8 tasks. Only exception: HyperPartisan (TAPT alone = 90.4, DAPT+TAPT = 90.0).

## Comparison to Adversarial Methods

The paper contains **no comparison to DANN or adversarial domain adaptation**. The authors treat continued pretraining as the adaptation strategy and do not evaluate adversarial alignment baselines.

## Computational Cost (RCT-500 example)

| Method | Steps | Storage |
|--------|-------|---------|
| TAPT | 0.2K | 80 KB |
| 500NN-TAPT | 9.0K | 24 MB |
| DAPT | 12.5K | 47 GB |
| DAPT+TAPT | 12.6K | 47 GB |

TAPT is 60× faster and uses far less storage while often competitive with DAPT.

## Significance

Establishes DAPT as the standard NLP domain adaptation baseline. Every subsequent NLP DA paper (including adapter+adversarial work) benchmarks against a DAPT baseline.

## Related

[[Domain-Adaptive Pre-Training (DAPT)]], [[Pre-training for Domain Adaptation]], [[DANN for NLP Text Domain Adaptation]]
