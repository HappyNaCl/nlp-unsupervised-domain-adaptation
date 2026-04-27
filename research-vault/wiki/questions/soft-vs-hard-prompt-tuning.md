---
type: question
title: "Soft Prompt vs. Hard Prompt Tuning (AdSPT context)"
question: "What is soft prompt and hard prompt tuning? How does AdSPT use soft prompts?"
answer_quality: solid
created: 2026-04-27
updated: 2026-04-27
tags: [question, adapter, soft-prompt, peft, adversarial, adSPT, nlp]
related:
  - "[[AdSPT Adversarial Soft Prompt Tuning (ACL2022)]]"
  - "[[Adapters (NLP)]]"
  - "[[Adapter + Adversarial Combination for NLP DA]]"
  - "[[Gradient Reversal Layer]]"
sources:
  - "[[AdSPT Adversarial Soft Prompt Tuning (ACL2022)]]"
  - "[[Adapters (NLP)]]"
status: developing
---

# Soft Prompt vs. Hard Prompt Tuning

## Hard Prompt Tuning

Discrete, human-readable templates prepended to the input in natural language. Example:

> `"Review sentiment: [INPUT]"` → fed into BERT

The words are fixed and chosen by hand. "Tuning" means iterating manually (or via discrete search) to find better wording. Nothing is gradient-trained — the model is steered purely through text. Hard prompts are human-interpretable but brittle and **cannot be backpropagated through**.

## Soft Prompt Tuning

Replaces discrete words with **learnable continuous vectors** prepended to the input embedding sequence:

$$[v_1, v_2, \ldots, v_k,\ \text{token}_1,\ \text{token}_2,\ \ldots]$$

The vectors $v_1 \ldots v_k$ do not correspond to any real word — they live in continuous embedding space and are trained end-to-end via gradient descent. The base model (BERT, RoBERTa, etc.) stays frozen; only the $k$ vectors are updated. Soft prompts are uninterpretable but directly optimizable for any differentiable objective.

## How AdSPT Uses Soft Prompts

AdSPT trains **separate soft prompt sets per domain** (each source domain and the target domain get their own $v_1 \ldots v_k$). Each prompt is tiny but domain-specific enough to capture that domain's distributional character.

The [[Gradient Reversal Layer]] is then applied **on top of the soft prompt output**, not on BERT's internal layers. The adversarial signal updates only the prompt vectors:

- BERT's pretrained knowledge stays intact (frozen base)
- Domain alignment pressure is absorbed by the small prompt parameters
- Per-domain prompts give the adversarial signal a cleaner domain separation to work with

This is the "adapter-first, adversarial-second" design pattern documented in [[Adapter + Adversarial Combination for NLP DA]].

## Why Soft, Not Hard?

Gradient flow. Adversarial training requires backpropagation through the adapter. Discrete tokens have no gradient; continuous vectors do. Hard prompts are incompatible with GRL-based adversarial training.

## Gap

> [!gap] Hard prompt + adversarial DA
> The vault has no coverage of hard prompt engineering for DA. AdSPT's choice of soft over hard prompts is justified by gradient requirements, but whether hard prompt methods achieve competitive DA results is not documented here.
