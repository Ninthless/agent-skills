# Visual Diversity

Read this reference when creating several products, generating alternatives, or reviewing whether unrelated interfaces have converged on the same model-default aesthetic.

## Contents

- Diversity Goal
- Fingerprint Fields
- Context Before Difference
- Comparison Rules
- Convergence Signals
- Acceptable Similarity
- Evaluation Procedure
- Limits

## Diversity Goal

The goal is not novelty for its own sake. The goal is for each interface to derive its composition and visual language from its product, users, content, platform, and brand rather than from a reusable AI template.

Two unrelated products should usually differ in several structural and expressive decisions. Products in one family should preserve shared system rules where consistency helps users.

## Fingerprint Fields

Record a compact visual fingerprint in the UI evidence manifest:

- `layout_model`: dominant composition, navigation, and region structure
- `density`: sparse, moderate, dense, or a more precise task-based description
- `typography_strategy`: type roles, contrast, voice, and hierarchy
- `palette_strategy`: semantic and brand color logic, not a list of hex values
- `geometry`: shape, edge, radius, proportion, and control silhouette
- `surface_strategy`: flat, divided, bordered, elevated, layered, textured, or another coherent treatment
- `imagery_strategy`: product evidence, documentary media, illustration, data, canvas, or intentionally none
- `motion_tone`: restrained, direct, playful, cinematic, physical, or another task-based description
- `platform_conventions`: the platform behaviors that shape the presentation

Use concrete phrases. `Modern`, `clean`, `beautiful`, and `premium` are not useful fingerprints.

## Context Before Difference

Derive the fingerprint after defining:

- Product and interface archetype
- Primary user and task
- Frequency, urgency, risk, and expertise
- Content and data shape
- Brand or subject matter
- Target platform and input
- Existing design system

Do not force difference that harms these constraints. A finance table and a support queue may both be dense because the task demands density, while still differing in navigation, typography, status language, geometry, and interaction rhythm.

## Comparison Rules

- Compare unrelated products or deliberately distinct concepts.
- Do not fail products in one design-system family for sharing tokens and components.
- Compare structure and strategy, not only colors.
- Require multiple differing dimensions before calling a concept distinct.
- Inspect screenshots after the heuristic; exact labels do not prove visible difference.
- Prefer product-relevant differentiation over arbitrary decorative variation.

The bundled comparison script normalizes field text, calculates token overlap and exact agreement, and reports pairwise similarity. Its default threshold is intentionally conservative and can be overridden.

## Convergence Signals

Review unrelated products when several of these recur without contextual justification:

- Centered oversized headline over a generic supporting paragraph
- Repeated three-card or feature-grid structure
- Floating rounded cards for every region
- Large radii, soft shadows, muted gradient, and one accent hue across domains
- Sparse dashboards with low information density
- Identical sidebar, topbar, metric-card, and chart composition
- Decorative pills and badges that carry little information
- The same geometric sans hierarchy and compact uppercase eyebrow
- Stock-like atmospheric imagery instead of subject evidence
- Uniform motion, icon treatment, and surface elevation

These are diagnostic signals, not universal bans.

## Acceptable Similarity

Similarity is appropriate when it comes from:

- Shared brand and design-system ownership
- Host-platform conventions
- Accessibility and semantic-control requirements
- A well-established task pattern users rely on
- Common product objects and workflows
- Explicit user-provided references

Keep shared interaction correctness while changing product-specific structure and expression where context calls for it.

## Evaluation Procedure

1. Produce the design contract and fingerprint before implementation.
2. Render the primary state and at least one meaningful secondary state.
3. Compare fingerprints for unrelated products.
4. Inspect pairwise results above the configured threshold.
5. Compare screenshots and identify which repeated choices lack product justification.
6. Change the design contract, not only the colors.
7. Re-render and compare again.

For a set of alternatives for one product, require each alternative to express a genuinely different composition or interaction thesis. Palette swaps do not count.

## Limits

The script cannot determine whether an interface is beautiful, usable, on-brand, or visibly distinct. It is sensitive to wording and can miss visual convergence expressed with different labels. Treat it as an early-warning mechanism and use direct screenshot inspection and task evidence for the final judgment.
