# Autoresearch Program — Vault Override

This file overrides and extends the default `references/program.md` from the autoresearch skill.
Read this file whenever `/autoresearch` is invoked in this vault.

---

## Domain Scope

**NLP ONLY.** All research is restricted to Natural Language Processing.

Topics in scope:
- Text domain adaptation (sentiment, topic, genre, formality shifts)
- Cross-lingual transfer and multilingual NLP
- Biomedical / clinical NLP
- Social media NLP (Twitter, Reddit domain adaptation)
- Pre-trained language models (BERT, RoBERTa, GPT, T5, LLaMA) for domain adaptation
- NLP-specific UDA methods (adversarial text DA, pivot-based DA, self-training on text)
- Named entity recognition, relation extraction, question answering — cross-domain variants

Topics out of scope (skip unless explicitly requested):
- Image / vision domain adaptation
- Medical imaging
- Speech and audio
- Multimodal — include only if there is a primary NLP component

---

## Source Preferences (NLP-specific)

Priority order:
1. ACL Anthology (aclanthology.org) — ACL, EMNLP, NAACL, COLING, EACL proceedings
2. arXiv cs.CL
3. NeurIPS / ICML / ICLR — NLP papers only
4. Hugging Face blog (huggingface.co/blog)
5. Papers with Code (NLP leaderboards)

Avoid unless primary sources unavailable:
- Medium / Towards Data Science blog posts
- Reddit or forum discussions (use as pointers only)

---

## Confidence Rules (NLP additions)

- **High confidence**: results on established NLP benchmarks (GLUE, SuperGLUE, SQuAD, MultiNLI, CoNLL-2003, Amazon Reviews, MNLI) with multiple independent verifications
- **Medium confidence**: single peer-reviewed source, or arXiv preprint with code
- **Low confidence**: blog post, no benchmark, undated
- **LLM claims**: always record model scale, evaluation mode (zero-shot / few-shot / fine-tuned), and whether the benchmark is saturated

---

## Max Constraints

(Same as default program.md unless overridden here)
- Max search rounds: 3
- Max wiki pages per session: 15
- Max sources fetched per round: 5

---

## NLP Benchmark Reference

When filing entity pages for benchmarks, use these standard abbreviations:

| Benchmark | Task | Notes |
|-----------|------|-------|
| GLUE | Multi-task NLU | Largely saturated |
| SuperGLUE | Multi-task NLU | Harder successor to GLUE |
| SQuAD 1.1 / 2.0 | QA | |
| MultiNLI / MNLI | NLI | Cross-genre |
| CoNLL-2003 | NER | English |
| Amazon Reviews | Sentiment DA | Classic DA benchmark for NLP |
| DARM / FDU-MTL | Multi-domain sentiment | |
