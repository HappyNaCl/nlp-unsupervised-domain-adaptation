# UDA Research Wiki: LLM Wiki

Mode: E (Research)
Purpose: Knowledge base for Unsupervised Domain Adaptation research — papers, concepts, methods, datasets, open questions.
Owner: yudhistira.fadly@gmail.com
Created: 2026-04-27

## Structure

```
research-vault/
├── .raw/               # PDFs, web clips, arXiv exports — never modify
├── wiki/
│   ├── index.md        # master catalog — update on every ingest
│   ├── log.md          # append-only operation log — new entries at top
│   ├── hot.md          # ~500-word hot cache — overwrite after every session
│   ├── overview.md     # executive summary of the field
│   ├── papers/         # one page per paper
│   ├── concepts/       # methods, techniques, theoretical ideas
│   ├── entities/       # datasets, benchmarks, authors, labs
│   ├── thesis/         # evolving field synthesis
│   ├── gaps/           # open questions and contradictions
│   ├── domains/        # adaptation scenarios
│   ├── comparisons/    # side-by-side method analyses
│   └── meta/           # dashboard, lint reports
├── _templates/         # frontmatter templates per note type
└── CLAUDE.md           # this file
```

## Conventions

- All notes use YAML frontmatter: type, status, created, updated, tags (minimum)
- Wikilinks use [[Note Name]] format: filenames are unique across the vault
- .raw/ contains source documents: never modify them
- wiki/index.md is the master catalog: update on every ingest
- wiki/log.md is append-only: never edit past entries; new entries at TOP
- wiki/hot.md is a ~500-word cache: overwrite completely after every session

## Operations

- **Ingest**: drop PDF or URL in .raw/, say "ingest [filename]" or "ingest [url]"
- **Query**: ask any question — Claude reads hot.md first, then index.md, then drills in
- **Lint**: say "lint the wiki" to run a health check
- **Save**: say "save this" to file the current exchange as a structured note

## Frontmatter Types

| type | folder | key fields |
|------|--------|------------|
| paper | wiki/papers/ | year, authors, venue, key_claim, methodology |
| concept | wiki/concepts/ | status (seed/developing/mature) |
| entity | wiki/entities/ | entity_type (dataset/author/lab/model) |
| thesis | wiki/thesis/ | status, sources |
| gap | wiki/gaps/ | status (open/resolved), area |
| meta | wiki/meta/ | (system pages) |

## Autoresearch Constraints

When running `/autoresearch` in this vault, apply the following domain-specific constraints **in addition to** the default program.md rules. These take precedence.

**Scope: NLP only.**
- All research must be focused on Natural Language Processing applications, methods, and datasets.
- For UDA topics: only pursue NLP/text domain adaptation (e.g., sentiment adaptation, cross-lingual transfer, biomedical NLP, news→Twitter domain shift). Do NOT research image/vision DA unless explicitly asked.
- Preferred sources: ACL Anthology (aclanthology.org), arXiv cs.CL, EMNLP/ACL/NAACL/COLING proceedings, Hugging Face blog, papers with code (NLP leaderboards)
- Source preference order: peer-reviewed NLP venues > arXiv cs.CL preprints > blog posts from major NLP labs > other
- Exclude: computer vision papers, medical imaging, remote sensing, audio — unless they contain an NLP component
- When a topic spans CV and NLP (e.g., multimodal DA), restrict synthesis to the NLP side

**NLP-specific confidence rules:**
- Benchmark claims: mark as low confidence unless evaluated on established NLP benchmarks (GLUE, SuperGLUE, SQuAD, MultiNLI, Amazon Reviews, etc.)
- LLM-related claims: always note the model scale and whether results are zero-shot, few-shot, or fine-tuned

See also: `_config/autoresearch-program.md` for the full override config.

## Reading Strategy (token-efficient)

1. Read wiki/hot.md first (~500 tokens) — recent context
2. If insufficient, read wiki/index.md (~1000 tokens) — full catalog
3. If you need domain specifics, read wiki/<folder>/_index.md
4. Only then read individual wiki pages

Do NOT read .raw/ files directly — read the wiki/papers/ summaries instead.
