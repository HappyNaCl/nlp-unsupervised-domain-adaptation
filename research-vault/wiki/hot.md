---
type: meta
title: "Hot Cache"
created: 2026-04-27
updated: 2026-04-27T17:00:00
tags: [meta, hot-cache]
---

# Recent Context

## Last Updated
2026-04-27. Wiki-lint run #2 complete. 37 issues found, 25 auto-fixed. Vault is now clean and well-connected.

## What Was Fixed (lint autofix)

- **5 new concept/entity stubs**: [[ADDA]], [[CDAN]], [[MDD]] (previously dead links in 16 places), [[BERT]], [[LoRA]]
- **2 new folder indexes**: `wiki/sources/_index.md`, `wiki/questions/_index.md`
- **CV remnant cleanup**: `entities/_index.md` purged of Office-31/Home/DomainNet/VisDA-2017; [[Unsupervised Domain Adaptation]] and [[Closed-Set DA]] updated to NLP benchmarks
- **Cross-reference gaps closed** (6 items): new concept pages are now cited from their parent concept pages; the 4 to-ingest source pages are now integrated into concept pages

## Vault State (NLP-only, post-lint)

**Sources (13):** DANN Original, BERT-DAAT (Guo ACL2020), AdSPT (ACL2022), NLP Survey (Ramponi COLING2020), Don't Stop Pretraining (ACL2020), PLM Survey (arXiv2022), UDAPTER (EACL2023), DaMSTF (ACL2023), Source-Free NLP DA Comparison (Su ACL2022), Adversarial MLM (Vu EMNLP2020), UDAA NER (Li CCL2024), CPT Generative UDA (Uppaal RepL4NLP2024), Bangla DAPT (Fahim BLP2025)

**Concepts (26):**
Core: UDA, Distribution Shift, Covariate Shift, Domain Invariant Features
Scenarios: Closed-Set DA, Open-Set DA, Partial DA, Universal DA
Adversarial: DANN, GRL, ADDA (stub), CDAN (stub), MDD (stub), Alignment-Discriminability Tradeoff
Pretraining: Pre-training for DA, DAPT (with Variants section), LoRA (stub)
Adapters: Adapters (NLP), DANN for NLP Text DA, Adapter+Adversarial Combo
Method families: NLP UDA Method Combinations, Self-Training for NLP DA, Contrastive Learning for NLP DA, Source-Free NLP DA, Pivot-Based Methods for NLP DA, Discrepancy Minimization for NLP DA

**Entities (1):** BERT (stub)

**Synthesis (3):** Research-Adapters+DANN, Research-DAPT vs DANN, Research-DAPT Adapter DANN Full Stack

## Remaining Open Issues (from lint report)

- Dead links still not fully resolved: `[[ADDA]]`, `[[CDAN]]`, `[[MDD]]`, `[[BERT]]`, `[[LoRA]]` — stubs now exist so links resolve
- Missing entity pages: Amazon Reviews benchmark, Ben-David bound concept
- `wiki/thesis/UDA Field Overview.md`: timeline row still has dead links [[ADDA]] + [[CDAN]] — now resolved via stubs
- `sources: []` on 11 concept pages (non-blocking, informational)
- `## Papers` vestigial section — removed from index.md ✓

## Remaining Coverage Gaps (research scope)
- Multi-source DA for NLP — no concept page
- Cross-lingual transfer — in scope, not covered
- Instance weighting / importance sampling — not covered
- Data augmentation for DA (EDA, back-translation) — not covered
- LLM-based DA (in-context learning, prompting) — mentioned briefly, not covered
