---
type: meta
title: "Wiki Index"
created: 2026-04-27
updated: 2026-04-27
tags: [meta, index]
status: developing
---

# Unsupervised Domain Adaptation — Wiki Index

Master catalog of all pages. Update on every ingest.

---

## Sources (filed from research)
- [[DANN Original Paper (Ganin 2016)]] — JMLR 2016; foundational GRL + adversarial alignment
- [[Adversarial and Domain-Aware BERT (Guo ACL2020)]] — ACL 2020; DANN fails on raw BERT; DAPT+adversarial → 90.12% Amazon, +4.22% SOTA
- [[AdSPT Adversarial Soft Prompt Tuning (ACL2022)]] — ACL 2022; soft prompt adapter + adversarial → SOTA cross-domain sentiment
- [[Neural UDA in NLP Survey (Ramponi COLING2020)]] — COLING 2020; survey of neural NLP UDA methods
- [[Don't Stop Pretraining (Gururangan ACL2020)]] — ACL 2020; canonical DAPT + TAPT; gains +0.4–12.4pp over RoBERTa across 8 tasks
- [[Domain Adaptation PLM Survey (arXiv2022)]] — arXiv 2022; DAPT > DANN alone; combination best; combined loss formulation
- [[UDAPTER (Malik EACL2023)]] — EACL 2023; adapter + divergence minimization beats DANN/DSN; parameter-efficient UDA
- [[DaMSTF (ACL2023)]] — ACL 2023; DANN as initialization + meta self-training; +4% over BERT on cross-domain sentiment
- [[Source-Free NLP DA Comparison (Su ACL2022)]] — ACL 2022; active learning most reliable strategy; self-training unreliable without source data
- [[Adversarial MLM for NLP DA (Vu EMNLP2020)]] — EMNLP 2020; adversarial masking replaces random MLM in DAPT; up to +1.64 F1 on 6 NER tasks
- [[UDAA Cross-Domain NER (Li CCL2024)]] — CCL 2024; MLM auxiliary + domain adversarial network; SOTA on CBS/Twitter/WNUT2016 zero-resource NER
- [[CPT for Generative UDA (Uppaal RepL4NLP2024)]] — RepL4NLP 2024; DAPT for generative models (T5/GPT); bridges to instruction tuning paradigm
- [[DAPT Bangla Hate Speech (Fahim BLP2025)]] — BLP 2025; DAPT on 315K Bangla social media comments; 0.7265 micro-F1; single-shot > hierarchical classification

## Concepts
<!-- one line per concept: [[Name]] — one-sentence description -->
- [[Unsupervised Domain Adaptation]] — transferring knowledge from a labeled source domain to an unlabeled target domain
- [[Distribution Shift]] — statistical mismatch between source and target data distributions
- [[Domain Invariant Features]] — representations that generalize across domains by removing domain-specific information
- [[Covariate Shift]] — distribution shift where P(X) differs but P(Y|X) is assumed constant
- [[DANN (Domain-Adversarial Neural Networks)]] — adversarial alignment via GRL; pros, cons, extensions
- [[Gradient Reversal Layer]] — backprop trick enabling adversarial domain training in one forward pass
- [[Alignment-Discriminability Tradeoff]] — core tension between domain invariance and class discriminability
- [[Pre-training for Domain Adaptation]] — DAPT and general LM pre-training as NLP DA prior; relationship to adapter+adversarial methods
- [[Domain-Adaptive Pre-Training (DAPT)]] — continued MLM on target-domain text; DAPT vs TAPT comparison; combination with adversarial
- [[NLP UDA Method Combinations]] — map of 6 validated NLP DA combination patterns; full-stack analysis
- [[Self-Training for NLP DA]] — pseudo-label iteration; CST, meta self-training variants; failure modes
- [[Contrastive Learning for NLP DA]] — class-conditioned alignment; DCCL and MCL; bypasses alignment-discriminability tradeoff
- [[Source-Free NLP DA]] — no source data setting; active learning dominant; privacy-motivated
- [[Pivot-Based Methods for NLP DA]] — SCL and neural variants; historically important; largely superseded by DAPT
- [[Discrepancy Minimization for NLP DA]] — MMD/CORAL on text features; stable non-adversarial baseline
- [[Adapters (NLP)]] — Houlsby, LoRA, prefix, soft prompts; parameter-efficient modules for LMs
- [[DANN for NLP Text Domain Adaptation]] — why vanilla DANN fails on BERT; fixes; NLP benchmarks
- [[Adapter + Adversarial Combination for NLP DA]] — GRL on adapter output (not BERT layers) → stable, SOTA
- [[ADDA]] — DANN variant with decoupled source/target encoders; GAN loss instead of GRL; seed
- [[CDAN]] — conditional adversarial alignment; discriminator conditioned on classifier predictions; addresses alignment-discriminability tradeoff; seed
- [[MDD]] — margin disparity discrepancy; tighter theoretical bound than H-divergence; seed
- [[LoRA]] — low-rank adapter matrices; dominant PEFT variant 2023–present; see [[Adapters (NLP)]]

## Entities
### Datasets / Benchmarks
<!-- add NLP benchmarks as ingested -->

### Authors / Labs

### Models / Architectures
- [[BERT]] — foundational masked LM (Devlin et al. 2019); primary NLP UDA backbone; DANN unstable on raw BERT layers

## Thesis
<!-- evolving synthesis of the field -->
- [[UDA Field Overview]] — current state of the field, dominant paradigms, open debates

## Questions / Synthesis
- [[Research - Adapters and DANN for NLP Domain Adaptation]] — can adapters + DANN work? Yes; GRL on adapter not BERT; AdSPT SOTA
- [[Research - DAPT vs DANN and Combining Them]] — DAPT > DANN alone on PLMs; combination best; order matters (DAPT first)
- [[Research - DAPT Adapter DANN Full Stack]] — full three-way combination analysis; open research gap; proposed recipe
- [[soft-vs-hard-prompt-tuning]] — hard prompts = discrete templates; soft prompts = learnable continuous vectors; AdSPT uses soft for GRL compatibility
- [[uda-problem-formulation-from-scratch]] — UDA setup, covariate shift assumption, two-level alignment (input DAPT + feature DANN)
- [[dapt-dann-adapters-pros-cons]] — pros/cons comparison table; DAPT fixes input shift, DANN fixes feature shift, adapters stable but limited alone

## Gaps
<!-- open questions and contradictions -->

## Domains
<!-- adaptation scenarios and domain taxonomy -->
- [[Closed-Set DA]] — source and target share identical label space
- [[Open-Set DA]] — target contains classes not in source
- [[Partial DA]] — target label space is a subset of source
- [[Universal DA]] — no assumption on label set relationship

## Comparisons
<!-- side-by-side method analyses -->
