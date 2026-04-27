---
type: source
status: summarized
source_type: paper
author: "Tamjid Hasan Fahim, Kaif Ahmed Khan"
year: 2025
venue: "BLP-2025 (2nd Workshop on Bangla Language Processing, ACL)"
url: "https://aclanthology.org/2025.banglalp-1.45"
confidence: medium
key_claims:
  - "DAPT on 315K+ Bangla social media comments improves hate speech detection over general-purpose models"
  - "Single-shot six-way classification outperforms two-stage hierarchical classification for hate speech categories"
  - "DAPT-enhanced BUET-BERT achieves 0.7265 micro-F1 on BLP-2025 Task 1"
tags: [source, paper, dapt, hate-speech, bangla, low-resource, social-media, domain-adaptation, nlp, 2025]
created: 2026-04-27
updated: 2026-04-27
---

# Domain-Adapted BERT for Bangla Hate Speech Detection (Fahim & Khan, BLP-2025)

Applies DAPT to Bangla social media NLP for multiclass hate speech detection. Demonstrates DAPT effectiveness in a low-resource, non-English, social-media domain.

## Methodology

1. **DAPT**: BUET-BERT continued pre-trained on 315,000+ Bangla social media comments
2. **Dataset construction**: novel Bangla sexism corpus (6,800+ comments) built via weak supervision + manual review
3. **Classification**: compared single-shot (direct 6-way) vs. hierarchical (hate/non-hate → fine-grained) classification

## Key Results

| Model | Micro-F1 |
|-------|---------|
| DAPT-enhanced BUET-BERT (single-shot) | **0.7265** |
| Hierarchical approach | lower |
| General-purpose LLMs | lower |

## Key Findings

- DAPT on social media text transfers effectively to hate speech detection — the domain shift from general Bangla text to social media Bangla is bridged by domain-specific continued pre-training
- Single-shot classification is better than hierarchical: introducing an intermediate binary step amplifies errors and loses signal
- Subtle hate speech (e.g., sarcasm, implicit sexism) remains challenging even with DAPT

## Significance

Shows DAPT is not just a high-resource English NLP technique. Effective for low-resource languages (Bangla) and highly specialized tasks (hate speech with informal/sarcastic language). Social media domain adaptation is one of the hardest DA scenarios due to code-switching, abbreviations, and slang.

## Related

[[Domain-Adaptive Pre-Training (DAPT)]], [[Pre-training for Domain Adaptation]]
