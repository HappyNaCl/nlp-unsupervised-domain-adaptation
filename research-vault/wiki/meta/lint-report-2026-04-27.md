---
type: meta
title: "Lint Report 2026-04-27"
created: 2026-04-27
updated: 2026-04-27
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-04-27

> Note: replaces the stale pre-purge lint report from the same date.

## Summary

- Pages scanned: 52 total (40 non-meta content pages checked)
- Issues found: 37
- Auto-fixed: 0
- Needs review: 37
- Address validation: skipped (DragonScale not present)
- Semantic tiling: skipped (tiling-check.py not available)

---

## Orphan Pages

Pages with no inbound wikilinks from non-catalog content pages (only linked from index.md / log.md):

**Concept pages — not linked from any other concept or synthesis page:**
- [[Contrastive Learning for NLP DA]]: no inbound links. Suggest: link from [[Alignment-Discriminability Tradeoff]] (directly addresses that tradeoff) and [[NLP UDA Method Combinations]].
- [[Pivot-Based Methods for NLP DA]]: no inbound links. Suggest: link from [[Domain-Adaptive Pre-Training (DAPT)]] (DAPT superseded pivot-based methods) and [[NLP UDA Method Combinations]].
- [[Discrepancy Minimization for NLP DA]]: no inbound links. Suggest: link from [[NLP UDA Method Combinations]] and [[DANN (Domain-Adversarial Neural Networks)]] (alternative to adversarial alignment).

**Source pages — not cited from any concept or synthesis page:**
- [[Adversarial MLM for NLP DA (Vu EMNLP2020)]]: no inbound links. Suggest: cite from [[Domain-Adaptive Pre-Training (DAPT)]] — adversarial masking is a direct DAPT improvement.
- [[UDAA Cross-Domain NER (Li CCL2024)]]: no inbound links. Suggest: cite from [[DANN for NLP Text Domain Adaptation]] and [[NLP UDA Method Combinations]].
- [[CPT for Generative UDA (Uppaal RepL4NLP2024)]]: no inbound links. Suggest: cite from [[Domain-Adaptive Pre-Training (DAPT)]] under a generative-models note.
- [[DAPT Bangla Hate Speech (Fahim BLP2025)]]: no inbound links. Suggest: cite from [[Domain-Adaptive Pre-Training (DAPT)]] as cross-lingual / low-resource evidence.

**Synthesis page:**
- [[Research - Adapters and DANN for NLP Domain Adaptation]]: no inbound links from content pages. Suggest: link from [[Adapter + Adversarial Combination for NLP DA]].

---

## Dead Links

Wikilinks that resolve to no existing page.

### CV remnants (pages deleted in purge)

- `[[Office-31]]` (deleted): in [[Unsupervised Domain Adaptation]] (Benchmarks), [[Closed-Set DA]] (Why It's the Baseline)
- `[[Office-Home]]` (deleted): same two pages
- `[[DomainNet]]` (deleted): in [[Unsupervised Domain Adaptation]] (Benchmarks)
- `[[VisDA-2017]]` (deleted): in [[Unsupervised Domain Adaptation]] (Benchmarks)

**Suggest**: replace the "Key Benchmarks" section of [[Unsupervised Domain Adaptation]] with NLP benchmarks (Amazon Reviews, CoNLL-2003, MultiNLI). Remove CV benchmark mentions from [[Closed-Set DA]] and update with NLP examples.

### NLP concept stubs referenced but never created

- `[[ADDA]]` (Adversarial Discriminative Domain Adaptation): **6 pages** — [[Gradient Reversal Layer]], [[Neural UDA in NLP Survey (Ramponi COLING2020)]], [[DANN (Domain-Adversarial Neural Networks)]] ×3, [[DANN for NLP Text Domain Adaptation]], [[Closed-Set DA]], [[UDA Field Overview]]. Suggest: create concept stub or convert to plain text.
- `[[CDAN]]` (Conditional Domain Adversarial Network): **5 pages** — [[DANN (Domain-Adversarial Neural Networks)]], [[Alignment-Discriminability Tradeoff]], [[overview]], [[Closed-Set DA]], [[UDA Field Overview]]. Suggest: create concept stub or convert to plain text.
- `[[MDD]]` (Margin Disparity Discrepancy): **5 pages** — [[UDA Field Overview]], [[Unsupervised Domain Adaptation]], [[DANN Original Paper (Ganin 2016)]], [[DANN (Domain-Adversarial Neural Networks)]], [[Alignment-Discriminability Tradeoff]]. Suggest: create concept stub or convert to plain text.
- `[[BERT]]` (used as wikilink target): **4 pages** — [[Adapter + Adversarial Combination for NLP DA]] ×2, [[Adapters (NLP)]], [[CPT for Generative UDA (Uppaal RepL4NLP2024)]]. Suggest: create a minimal BERT entity page or convert to plain text.
- `[[LoRA]]` (used as wikilink target): **3 pages** — [[Adapters (NLP)]] (table), [[Adapter + Adversarial Combination for NLP DA]] ×2. Suggest: already described in [[Adapters (NLP)]] table; convert to plain text or create a one-line entity page.

---

## Stale Claims

- [[Unsupervised Domain Adaptation]] "Key Benchmarks" section lists only CV benchmarks (Office-31, Office-Home, DomainNet, VisDA-2017). Conflicts with NLP-only vault scope. Suggest: replace with Amazon Reviews, CoNLL-2003, MultiNLI, FDU-MTL.

- [[Closed-Set DA]]: "Benchmarks like [[Office-31]] and [[Office-Home]] are evaluated in this setting" — CV-only. Suggest: replace with NLP equivalents (Amazon Reviews 4-domain sentiment split, ACL-ARC / ChemProt for scientific text).

- [[UDA Field Overview]] Timeline row `~2016–2018`: links `[[ADDA]]` and `[[CDAN]]` — both dead links. Timeline remains CV-era in flavor; consider annotating NLP relevance once more sources are ingested.

---

## Missing Pages

Concepts or entities mentioned in ≥2 pages but lacking their own wiki page:

- `"ADDA"` — major DANN variant, 6 mentions across the vault. Warrants a concept stub.
- `"CDAN"` — conditional DANN extension, 5 mentions. Warrants a concept stub.
- `"MDD"` — discrepancy-based alternative with tight theoretical bound, 5 mentions. Warrants a concept stub.
- `"BERT"` — wikilinked in 4 places. Warrants a minimal entity page (`type: entity`, `entity_type: model`).
- `"LoRA"` — wikilinked in 3 places; already described in [[Adapters (NLP)]]. Could convert to plain text or add a one-line entity page.
- `"Amazon Reviews"` — primary NLP DA benchmark; used in 3+ source papers; no entity page.
- `"Ben-David bound"` — mentioned in [[DANN Original Paper (Ganin 2016)]], [[DANN (Domain-Adversarial Neural Networks)]], [[Unsupervised Domain Adaptation]]; theoretical cornerstone; warrants a concept stub.

---

## Missing Cross-References

Entities mentioned in a page without a wikilink, where a link to an existing page would be appropriate:

- [[Domain-Adaptive Pre-Training (DAPT)]]: does not link to [[Adversarial MLM for NLP DA (Vu EMNLP2020)]] — adversarial masking is a direct DAPT improvement that belongs here.
- [[DANN for NLP Text Domain Adaptation]]: does not cite [[UDAA Cross-Domain NER (Li CCL2024)]] — strongest recent evidence for DAPT+adversarial effectiveness on NER.
- [[NLP UDA Method Combinations]]: omits [[Contrastive Learning for NLP DA]], [[Pivot-Based Methods for NLP DA]], and [[Discrepancy Minimization for NLP DA]] — all documented NLP UDA method families now in the vault.
- [[Alignment-Discriminability Tradeoff]]: does not link to [[Contrastive Learning for NLP DA]], which directly addresses this tradeoff via class-conditioned contrastive objectives.
- [[Source-Free NLP DA]]: frontmatter `sources` lists only `[[Neural UDA in NLP Survey (Ramponi COLING2020)]]` — should also include [[Source-Free NLP DA Comparison (Su ACL2022)]], the primary empirical source for this concept.

---

## Frontmatter Gaps

All 40 content pages have the required fields (type, status, created, updated, tags). No blocking errors.

**Non-blocking (informational):** many concept pages have `sources: []` (empty): [[Unsupervised Domain Adaptation]], [[Closed-Set DA]], [[Distribution Shift]], [[Domain Invariant Features]], [[Covariate Shift]], [[Open-Set DA]], [[Partial DA]], [[Universal DA]], [[Gradient Reversal Layer]], [[Alignment-Discriminability Tradeoff]], [[UDA Field Overview]]. Populate as sources are ingested.

---

## Empty Sections

- [[index]] → `## Papers` heading: contains only the placeholder comment `<!-- one line per paper -->`. Papers are actually filed under `wiki/sources/` — this heading is vestigial and confusing. Suggest: rename to `## Sources` (already present below) or remove the Papers section.
- [[index]] → `## Entities — Datasets/Benchmarks`: contains only `<!-- add NLP benchmarks as ingested -->`. Suggest: add Amazon Reviews, CoNLL-2003, MultiNLI entity pages, or remove the placeholder once entity pages exist.

---

## Stale Index Entries

- `wiki/entities/_index.md`: lists [[Office-31]], [[Office-Home]], [[DomainNet]], [[VisDA-2017]] — all four deleted in the CV purge. File was not cleaned up. **Safe to auto-fix**: remove those 4 entries, replace with a NLP benchmarks placeholder comment.

---

## Missing Folder Indexes

- `wiki/sources/` has 13 source pages but no `_index.md`. Suggest: create a minimal index listing all 13 sources with one-line descriptions.
- `wiki/questions/` has 3 synthesis pages but no `_index.md`. Suggest: create a minimal index.

---

## Address Validation

Skipped — DragonScale not configured (no `scripts/allocate-address.sh` or `.vault-meta/address-counter.txt`).

---

## Semantic Tiling

Skipped — `scripts/tiling-check.py` not available.

---

## Prioritized Fix List

### High priority (dead links / stale entries)
1. Clean CV benchmark links from [[Unsupervised Domain Adaptation]] and [[Closed-Set DA]] → replace with NLP benchmarks
2. Clean `wiki/entities/_index.md` → remove 4 deleted CV entries
3. Resolve `[[ADDA]]`, `[[CDAN]]`, `[[MDD]]` dead links (16 occurrences) — create stubs or convert to plain text
4. Resolve `[[BERT]]` and `[[LoRA]]` dead links (7 occurrences) — create minimal entity pages or convert to plain text

### Medium priority (cross-reference gaps / orphan connections)
5. Link [[Contrastive Learning for NLP DA]] from [[Alignment-Discriminability Tradeoff]] and [[NLP UDA Method Combinations]]
6. Link [[Pivot-Based Methods for NLP DA]] and [[Discrepancy Minimization for NLP DA]] from [[NLP UDA Method Combinations]]
7. Cite [[Adversarial MLM for NLP DA (Vu EMNLP2020)]] from [[Domain-Adaptive Pre-Training (DAPT)]]
8. Cite [[UDAA Cross-Domain NER (Li CCL2024)]] from [[DANN for NLP Text Domain Adaptation]]
9. Add [[Source-Free NLP DA Comparison (Su ACL2022)]] to [[Source-Free NLP DA]] frontmatter sources
10. Link [[Research - Adapters and DANN for NLP Domain Adaptation]] from [[Adapter + Adversarial Combination for NLP DA]]

### Low priority (structure)
11. Create `wiki/sources/_index.md` and `wiki/questions/_index.md`
12. Remove vestigial `## Papers` heading from index.md
13. Add NLP benchmark entity pages: Amazon Reviews, CoNLL-2003, MultiNLI
14. Populate `sources: []` on concept pages that have relevant sources in the vault
