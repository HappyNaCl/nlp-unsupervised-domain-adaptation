---
type: meta
title: "Wiki Overview"
created: 2026-04-27
updated: 2026-04-27
tags: [meta, overview]
status: seed
---

# Unsupervised Domain Adaptation — Research Wiki

## Purpose

This wiki tracks the Unsupervised Domain Adaptation (UDA) research landscape. It synthesizes papers, extracts concepts, maps methods, and surfaces open questions. Every ingest adds to a compounding knowledge base.

## Core Problem

Unsupervised Domain Adaptation addresses the distribution shift between a labeled source domain and an unlabeled target domain. The goal is to train a model that generalizes to the target domain without requiring target labels.

## Dominant Paradigms

> [!gap] Not yet sourced
> This section will be filled as papers are ingested.

- **Adversarial training** — align distributions via a domain discriminator ([[DANN (Domain-Adversarial Neural Networks)|DANN]], [[ADDA]], [[CDAN]])
- **Discrepancy minimization** — minimize statistical distance (MMD, CORAL, [[MDD]])
- **Self-training / pseudo-labels** — iteratively assign labels to target samples
- **Normalization-based** — align batch statistics across domains

## Key NLP Benchmarks

| Benchmark | Task | Domains | Notes |
|-----------|------|---------|-------|
| Amazon Reviews | Sentiment | Books, DVD, Electronics, Kitchen | Most-studied NLP DA benchmark |
| FDU-MTL | Sentiment | 16 domains | Multi-task variant |
| CoNLL-2003 | NER | News → Social media | Cross-domain NER |
| MultiNLI | NLI | 10 genres | Cross-genre NLI |

## Adaptation Scenarios

- [[Closed-Set DA]] — standard setting, shared label space
- [[Partial DA]] — target ⊂ source label space
- [[Open-Set DA]] — target contains unknown classes
- [[Universal DA]] — no label set assumption

## Open Questions

See [[wiki/gaps/_index]] for tracked open questions.
