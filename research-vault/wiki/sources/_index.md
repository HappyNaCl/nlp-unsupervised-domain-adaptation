---
type: meta
title: "Sources Index"
created: 2026-04-27
updated: 2026-04-27
tags: [meta, sources]
---

# Sources

All ingested papers and research sources. One line per source.

## Foundational

- [[DANN Original Paper (Ganin 2016)]] — JMLR 2016; foundational GRL + adversarial alignment

## NLP Surveys

- [[Neural UDA in NLP Survey (Ramponi COLING2020)]] — COLING 2020; survey of neural NLP UDA methods
- [[Domain Adaptation PLM Survey (arXiv2022)]] — arXiv 2022; DAPT > DANN alone; combination best

## Domain-Adaptive Pre-Training

- [[Don't Stop Pretraining (Gururangan ACL2020)]] — ACL 2020; canonical DAPT + TAPT benchmark
- [[Adversarial MLM for NLP DA (Vu EMNLP2020)]] — EMNLP 2020; adversarial masking in DAPT; +1.64 F1
- [[CPT for Generative UDA (Uppaal RepL4NLP2024)]] — RepL4NLP 2024; DAPT for generative models
- [[DAPT Bangla Hate Speech (Fahim BLP2025)]] — BLP 2025; DAPT in low-resource Bangla; 0.7265 micro-F1

## Adapter + Adversarial

- [[Adversarial and Domain-Aware BERT (Guo ACL2020)]] — ACL 2020; DAPT + adversarial; 90.12% Amazon
- [[AdSPT Adversarial Soft Prompt Tuning (ACL2022)]] — ACL 2022; soft prompt adapter + adversarial → SOTA
- [[UDAPTER (Malik EACL2023)]] — EACL 2023; adapter + divergence minimization; beats DANN

## Self-Training + Combinations

- [[DaMSTF (ACL2023)]] — ACL 2023; adversarial init + meta self-training; +4% over BERT
- [[UDAA Cross-Domain NER (Li CCL2024)]] — CCL 2024; MLM auxiliary + adversarial; SOTA cross-domain NER

## Source-Free DA

- [[Source-Free NLP DA Comparison (Su ACL2022)]] — ACL 2022; active learning most reliable strategy
