---
type: meta
title: "Wiki Log"
created: 2026-04-27
updated: 2026-04-27
tags: [meta, log]
status: active
---

# Wiki Log

Append-only. New entries go at the TOP. Never edit past entries.

---

## 2026-04-27 — query | DAPT vs DANN vs Adapters pros and cons

- Question: list pros and cons for DAPT, DANN, and adapters
- Filed: [[dapt-dann-adapters-pros-cons]]
- Key answer: DAPT stable but only fixes input shift; DANN targets feature shift but unstable on raw BERT; adapters parameter-efficient and stable but limited capacity alone; all three together covers both shift levels

---

## 2026-04-27 — query | UDA problem formulation from scratch

- Question: explain what UDA tries to solve from the different distributions needed to be handled
- Filed: [[uda-problem-formulation-from-scratch]]
- Key answer: UDA assumes covariate shift ($P(X)$ differs, $P(Y|X)$ same); two nested problems — input distribution mismatch fixed by DAPT, feature distribution mismatch fixed by DANN; methods that address only one level work partially at best

---

## 2026-04-27 — query | Soft prompt vs. hard prompt tuning (AdSPT context)

- Question: what is soft/hard prompt tuning; how does AdSPT use soft prompts
- Filed: [[soft-vs-hard-prompt-tuning]]
- Key answer: hard prompts = discrete human-readable templates, non-differentiable; soft prompts = learnable continuous vectors prepended to input, gradient-trainable; AdSPT uses soft prompts because GRL requires backpropagation through the adapter — discrete tokens have no gradient

---

## 2026-04-27 — lint + autofix | wiki-lint run #2 (post-purge)

- Pages scanned: 52 (40 content pages)
- Issues found: 37 | Auto-fixed: 25
- New stubs created (5): [[ADDA]], [[CDAN]], [[MDD]], [[BERT]], [[LoRA]]
- New folder indexes (2): `wiki/sources/_index.md`, `wiki/questions/_index.md`
- CV remnants cleaned: `wiki/entities/_index.md` (4 dead CV entries removed); [[Unsupervised Domain Adaptation]] and [[Closed-Set DA]] (CV benchmarks → NLP benchmarks)
- Cross-reference gaps fixed (6): [[Alignment-Discriminability Tradeoff]] → [[Contrastive Learning for NLP DA]]; [[NLP UDA Method Combinations]] → [[Contrastive Learning for NLP DA]], [[Pivot-Based Methods for NLP DA]], [[Discrepancy Minimization for NLP DA]]; [[Domain-Adaptive Pre-Training (DAPT)]] → [[Adversarial MLM for NLP DA (Vu EMNLP2020)]], [[CPT for Generative UDA (Uppaal RepL4NLP2024)]], [[DAPT Bangla Hate Speech (Fahim BLP2025)]] (DAPT Variants section added); [[DANN for NLP Text Domain Adaptation]] → [[UDAA Cross-Domain NER (Li CCL2024)]]; [[Source-Free NLP DA]] → [[Source-Free NLP DA Comparison (Su ACL2022)]]; [[Adapter + Adversarial Combination for NLP DA]] → [[Research - Adapters and DANN for NLP Domain Adaptation]]
- Remaining open issues (12): dead links to [[ADDA]], [[CDAN]], [[MDD]], [[BERT]], [[LoRA]] are now resolved (stubs created); 4 orphan source pages (to-ingest batch) now cited from concept pages; remaining gaps in lint report
- Lint report: [[lint-report-2026-04-27]]

---

## 2026-04-27 — ingest | to-ingest.md batch (4 papers)

- Sources filed (4): [[Adversarial MLM for NLP DA (Vu EMNLP2020)]], [[UDAA Cross-Domain NER (Li CCL2024)]], [[CPT for Generative UDA (Uppaal RepL4NLP2024)]], [[DAPT Bangla Hate Speech (Fahim BLP2025)]]
- Key findings:
  - Adversarial masking (Vu EMNLP 2020): replacing random 15% MLM masking with adversarially-selected hard tokens improves DAPT by up to +1.64 F1; orthogonal to downstream adversarial alignment
  - UDAA (Li CCL 2024): MLM auxiliary task + domain adversarial network achieves SOTA on 3 cross-domain NER benchmarks; validates DAPT+adversarial for NER (extends beyond sentiment)
  - CPT for Generative UDA (Uppaal RepL4NLP 2024): DAPT on generative models (T5/GPT-style); trade-offs with domain-invariant methods vary by architecture/tuning; bridges DAPT to instruction tuning
  - Bangla DAPT (Fahim BLP 2025): DAPT effective on low-resource non-English; 315K Bangla social media → 0.7265 micro-F1 hate speech; single-shot 6-way > hierarchical classification

---

## 2026-04-27 — autoresearch | Gap-filling: Missing NLP UDA Method Families

- Rounds: 3 | Searches: 6 | Fetches: 4
- Sources filed: [[Source-Free NLP DA Comparison (Su ACL2022)]]
- Concepts filed (5): [[Self-Training for NLP DA]], [[Contrastive Learning for NLP DA]], [[Source-Free NLP DA]], [[Pivot-Based Methods for NLP DA]], [[Discrepancy Minimization for NLP DA]]
- Coverage gaps addressed: self-training, contrastive DA, source-free DA, pivot-based SCL methods, MMD/CORAL for NLP
- Key findings:
  - Contrastive learning (DCCL NAACL 2022, MCL COLING 2022) directly addresses alignment-discriminability tradeoff
  - Source-free NLP DA: active learning most reliable; self-training unreliable without source regularization
  - Pivot-based methods (SCL): largely superseded by DAPT in PLM era but still conceptually important
  - Discrepancy minimization (MMD/CORAL): stable non-adversarial baseline; understudied in PLM context
  - Self-training works best when initialized by DAPT or adversarial warm-start

---

## 2026-04-27 — autoresearch | DAPT + Adapters + DANN Full Stack and Popular Combinations

- Rounds: 3 | Searches: 6 | Fetches: 5
- Sources filed: [[UDAPTER (Malik EACL2023)]], [[DaMSTF (ACL2023)]]
- Concepts filed: [[NLP UDA Method Combinations]]
- Synthesis: [[Research - DAPT Adapter DANN Full Stack]]
- Key findings:
  - Full stack (DAPT+adapter+DANN) not validated in a single paper — confirmed open gap
  - 6 validated NLP UDA combination patterns mapped (see NLP UDA Method Combinations)
  - UDAPTER (EACL 2023): adapter + divergence minimization beats DANN without adversarial instability
  - DaMSTF (ACL 2023): DANN as initialization only → meta self-training does the adaptation work (+4% over BERT)
  - Theoretical recipe for full stack proposed; each component addresses a different pipeline level

---

## 2026-04-27 — autoresearch | DAPT vs DANN and Combining Them

- Rounds: 3 | Searches: 4 | Fetches: 4
- Sources filed: [[Don't Stop Pretraining (Gururangan ACL2020)]], [[Domain Adaptation PLM Survey (arXiv2022)]]
- Concepts filed: [[Domain-Adaptive Pre-Training (DAPT)]]
- Synthesis: [[Research - DAPT vs DANN and Combining Them]]
- Updated: [[Pre-training for Domain Adaptation]] (seed → developing)
- Key findings:
  - DAPT alone: +0.4–12.4pp over RoBERTa (best on ACL-ARC); no adversarial comparison in the paper
  - DANN alone on PLMs: unstable, near-zero gains (confirmed multi-source)
  - DAPT + adversarial (Du et al. ACL 2020): 90.12% avg Amazon sentiment, +4.22% SOTA — combination strictly better than either alone
  - Order matters: DAPT first stabilizes adversarial by reducing initial domain gap
  - TAPT: 60× cheaper than DAPT, often competitive; DAPT+TAPT best on 7/8 tasks

---

## 2026-04-27 — purge | CV content removed

- Deleted sources (5): TVT (WACV2023), CDTrans (ICLR2022), PMTrans (CVPR2023), TriDA (2023), DANN for Domain Generalization (Zhao 2021)
- Deleted entities (4): Office-31, Office-Home, DomainNet, VisDA-2017
- Deleted synthesis (1): Research - Pretrain vs DANN and Combining Them
- Cleaned concepts: DANN, Alignment-Discriminability Tradeoff, Pre-training for Domain Adaptation (reframed for NLP/DAPT)
- Cleaned overview.md (CV benchmark table → NLP benchmark table), UDA Field Overview (timeline updated to NLP era), index.md
- Reason: vault scope restricted to NLP only

---

## 2026-04-27 — autoresearch | Adapters and DANN for NLP Domain Adaptation

- Rounds: 3 | Searches: 6 | Fetches: 5
- Sources filed: [[Adversarial and Domain-Aware BERT (Guo ACL2020)]], [[AdSPT Adversarial Soft Prompt Tuning (ACL2022)]], [[Neural UDA in NLP Survey (Ramponi COLING2020)]]
- Concepts filed: [[Adapters (NLP)]], [[DANN for NLP Text Domain Adaptation]], [[Adapter + Adversarial Combination for NLP DA]]
- Synthesis: [[Research - Adapters and DANN for NLP Domain Adaptation]]
- Key finding: Vanilla DANN on BERT fails (unstable, no gains). Fix: freeze BERT, insert adapters, apply GRL to adapter output. AdSPT (ACL 2022) validates this pattern → SOTA cross-domain sentiment.
- Note: NLP-only scope applied (per vault constraints).

---

## 2026-04-27 — autoresearch | Pretrain vs DANN and Combining Them

- Rounds: 3 | Searches: 6 | Fetches: 7
- Sources filed: [[DANN Original Paper (Ganin 2016)]], [[DANN for Domain Generalization (Zhao 2021)]], [[TVT Transferable Vision Transformer (Yang WACV2023)]], [[CDTrans Cross-Domain Transformer (Xu ICLR2022)]], [[PMTrans Patch-Mix Transformer (Zhu CVPR2023)]], [[TriDA Pre-training Data Matters (2023)]]
- Concepts filed: [[DANN (Domain-Adversarial Neural Networks)]], [[Gradient Reversal Layer]], [[Alignment-Discriminability Tradeoff]], [[Pre-training for Domain Adaptation]]
- Synthesis: [[Research - Pretrain vs DANN and Combining Them]]
- Key finding: Pretraining + DANN are complementary — pretraining reduces the initial gap, adversarial alignment closes the residual. PMTrans (ViT + PatchMix) achieves 95.3% Office-31, 27.0% DomainNet as of CVPR 2023.

---

## 2026-04-27 — Vault scaffold

- Initialized wiki structure for Unsupervised Domain Adaptation research
- Created: wiki/, .raw/, _templates/, wiki/meta/
- Created seed concept pages: [[Unsupervised Domain Adaptation]], [[Distribution Shift]], [[Domain Invariant Features]], [[Covariate Shift]]
- Created seed entity pages: [[Office-31]], [[Office-Home]], [[DomainNet]], [[VisDA-2017]]
- Created scenario pages: [[Closed-Set DA]], [[Open-Set DA]], [[Partial DA]], [[Universal DA]]
- Created thesis page: [[UDA Field Overview]]
- Mode: E (Research)
