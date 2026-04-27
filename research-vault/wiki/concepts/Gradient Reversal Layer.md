---
type: concept
status: developing
created: 2026-04-27
updated: 2026-04-27
tags: [concept, domain-adaptation, adversarial, technique]
sources:
  - "[[DANN Original Paper (Ganin 2016)]]"
  - "[[Neural UDA in NLP Survey (Ramponi COLING2020)]]"
---

# Gradient Reversal Layer

A pseudo-layer used in [[DANN (Domain-Adversarial Neural Networks)]] that acts as an identity function during the forward pass but multiplies gradients by −λ during backpropagation.

## Purpose

Converts a standard classification loss (minimization) into an adversarial maximization signal for the feature extractor. Without GRL, an adversarial setup would require alternating optimization; GRL makes it a single-pass minimax via standard SGD.

## Formal Definition

$$
\text{Forward: } \mathcal{R}_\lambda(x) = x
$$
$$
\text{Backward: } \frac{d\mathcal{R}_\lambda}{dx} = -\lambda \cdot I
$$

λ is typically annealed from 0 to 1 during training (linear or sigmoid schedule).

## Known Issues

- **Vanishing gradient**: once the discriminator saturates (reaches high accuracy), $|G_d(\mathbf{z}) - 0.5| \to 0.5$, and the gradient signal from GRL becomes too small to drive meaningful feature updates
- **Instability at λ=1 early in training**: large gradient reversals before features are meaningful can destabilize the label classifier

## Alternatives

- GAN-style discriminator with separate optimizer ([[ADDA]])
- Wasserstein distance with gradient penalty
- Directly minimizing statistical distances (MMD, CORAL) — no adversarial dynamics needed

## Related

[[DANN (Domain-Adversarial Neural Networks)]], [[Unsupervised Domain Adaptation]]
