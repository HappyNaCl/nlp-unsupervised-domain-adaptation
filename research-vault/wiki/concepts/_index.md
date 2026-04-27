---
type: meta
title: "Concepts Index"
created: 2026-04-27
updated: 2026-04-27
tags: [meta, concepts]
---

# Concepts

Core ideas, methods, frameworks, and theoretical foundations.

## Problem Formulation
- [[Unsupervised Domain Adaptation]]
- [[Distribution Shift]]
- [[Covariate Shift]]
- [[Domain Invariant Features]]

## Adaptation Scenarios
- [[Closed-Set DA]]
- [[Open-Set DA]]
- [[Partial DA]]
- [[Universal DA]]

## Methods / Techniques
- [[DANN (Domain-Adversarial Neural Networks)]] — adversarial alignment via GRL; pros, cons, extensions
- [[Gradient Reversal Layer]] — backprop trick enabling adversarial domain training in one pass
- [[Alignment-Discriminability Tradeoff]] — core tension between domain invariance and class discriminability
- [[Pre-training for Domain Adaptation]] — DAPT and LM pre-training as NLP DA prior; relationship to adapter+adversarial methods
- [[Domain-Adaptive Pre-Training (DAPT)]] — continued MLM on target-domain text; DAPT vs TAPT; combination with adversarial training
- [[NLP UDA Method Combinations]] — map of validated 2-way and 3-way NLP DA method combinations; practical guidance
- [[Adapters (NLP)]] — Houlsby, LoRA, prefix, soft prompts; parameter-efficient modules for LMs
- [[DANN for NLP Text Domain Adaptation]] — why vanilla DANN fails on BERT; fixes; benchmarks
- [[Adapter + Adversarial Combination for NLP DA]] — GRL on adapter output → stable, SOTA
- [[Self-Training for NLP DA]] — pseudo-label iteration; variants (CST, meta self-training); failure modes
- [[Contrastive Learning for NLP DA]] — class-conditioned alignment; avoids alignment-discriminability tradeoff
- [[Source-Free NLP DA]] — no source data at adaptation time; active learning most reliable
- [[Pivot-Based Methods for NLP DA]] — SCL and neural variants; largely superseded by DAPT in PLM era
- [[Discrepancy Minimization for NLP DA]] — MMD/CORAL on text features; stable non-adversarial baseline

## Theoretical Foundations
<!-- add as ingested -->

## Metrics & Evaluation
<!-- add as ingested -->
