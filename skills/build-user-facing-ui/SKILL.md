---
name: build-user-facing-ui
description: 'Build, redesign, fully refactor, implement, review, or fix user-facing UI for web, dashboards, commerce, mobile, desktop or Electron apps, games, editors, kiosks, TV, wearables, automotive, and spatial interfaces. Use for visual hierarchy, layout, responsive behavior, interaction states, accessibility, platform adaptation, design systems, consent or cancellation UX, user-facing performance, content design, Figma or screenshot implementation, and requests for polished, distinctive, usable UI. Also trigger for 重构界面, 重构前端, 重构所有 UI, 彻底重做 UI, rebuild the entire UI, and full visual overhaul. When a UI refactor is broad, rebuild the complete interface from a new product-specific art direction while preserving valid functionality; do not default to cosmetic changes or a fixed AI style. Do not use for backend, API, database, or CLI work, standalone image or logo creation, copy-only translation, privacy-policy prose, backend performance, or headless logic with no UI impact.'
---

# Build User-Facing UI

## Copyright

Copyright (c) 2026 Ninthless. All rights reserved. This skill may not be copied, modified, redistributed, or used to create derivative works without prior written permission.

## Purpose

Create interfaces that help real users complete real tasks and feel intentionally designed for their product, audience, platform, and content. Optimize for effective, efficient, understandable, accessible, coherent, and visually resolved UI rather than a reusable aesthetic formula.

Treat visual quality as a product outcome. A technically valid page that is generic, misleading, incomplete, visually unstable, or unverified is not finished.

## Read The Right References

- Always read [quality-model.md](./references/quality-model.md) before making material design decisions.
- Read [interface-archetypes.md](./references/interface-archetypes.md) when creating a new surface, redesigning a product, or deciding density and composition.
- Read [visual-art-direction.md](./references/visual-art-direction.md) for greenfield work, redesigns, brand-sensitive surfaces, or any request where visual quality and distinctiveness are central.
- Read [transformation-mode.md](./references/transformation-mode.md) whenever the user asks to refactor, rebuild, overhaul, replace, or completely redo an existing UI or frontend.
- Read [content-design.md](./references/content-design.md) when labels, instructions, forms, empty states, errors, localization, or information scent materially affect the interface.
- Read [interaction-accessibility.md](./references/interaction-accessibility.md) for forms, navigation, controls, stateful workflows, responsive behavior, localization, or accessibility-sensitive work.
- Read [accessibility-hard-gates.md](./references/accessibility-hard-gates.md) when exact accessibility requirements matter or before declaring a substantial interface complete.
- Read [platform-guidelines.md](./references/platform-guidelines.md) for native mobile, desktop, Electron, Tauri, or platform-adapted application work.
- Read [specialized-surfaces.md](./references/specialized-surfaces.md) for messaging, maps, kiosks, TV, wearables, automotive, spatial, voice, or shared-device interfaces.
- Read [trust-privacy-ethics.md](./references/trust-privacy-ethics.md) for purchases, subscriptions, consent, personal data, permissions, cancellation, deletion, or high-impact decisions.
- Read [rendered-verification.md](./references/rendered-verification.md) before verifying any non-trivial rendered interface.
- Read [evidence-performance.md](./references/evidence-performance.md) when performance, usability, accessibility, or user-validation claims require measurable support.
- Read [visual-diversity.md](./references/visual-diversity.md) when producing multiple products or alternatives or when unrelated outputs may be converging on one visual formula.

## Priority Order

Resolve tradeoffs in this order:

1. User goal and product correctness
2. Interaction clarity and state completeness
3. Accessibility and input compatibility
4. User agency, trust, and truthful representation
5. Context, platform, and design-system coherence
6. Responsive content integrity
7. Visual hierarchy and craft
8. Measured performance and implementation maintainability
9. Novelty and decorative expression

Visual originality never justifies making the primary task harder. Familiarity never justifies producing an anonymous template.

## Core Workflow

### 0. Choose The Process Mode

Use the lightest mode that still covers the risk:

- **Patch mode**: local visual or interaction correction inside an established design system. Preserve the current visual language and verify the affected states.
- **Product mode**: a new screen, workflow, or feature inside an existing product. Reuse the system, define the screen archetype, and complete the end-to-end states.
- **Concept mode**: a greenfield interface, major redesign, or brand-defining surface. Gather references, establish an art direction and screen plan, then implement the complete experience.
- **Transformation mode**: a broad refactor or rebuild of an existing UI. Treat the current product as functional input, inventory every user-facing surface, derive a new art direction and design system, and migrate the complete interface rather than polishing the old one.
- **High-risk overlay**: add exact accessibility, trust, privacy, performance, and evidence requirements for health, finance, public service, identity, purchases, subscriptions, or other consequential flows.

Do not make patch work carry concept-mode ceremony. Do not let concept work skip visual exploration because the first plausible layout compiles.

When UI language such as `重构`, `重做`, `重新设计`, `rebuild`, `overhaul`, or `refactor the UI` is broad and the user does not limit it to one component or ask to preserve the current design system, choose Transformation mode. This explicit transformation request overrides the normal preserve-and-reuse defaults. A scoped component refactor or an instruction to keep the current system remains Patch or Product mode.

### 1. Understand The Interface Before Designing

Inspect the repository and the actual product surface before changing code.

Identify:

- Primary user and the job they need to complete
- Usage frequency, urgency, risk, and expected expertise
- Product type and interface archetype
- Existing framework, components, tokens, patterns, and assets
- Required content, real data shapes, actions, navigation, and states
- Target devices, viewport classes, input methods, and localization needs
- Brand references, screenshots, Figma files, or explicit visual direction

Preserve an established design system unless the user explicitly requests a redesign, refactor, rebuild, or the existing system is the problem. In Transformation mode, preserve product capabilities and valid contracts, not the old UI system. If the business domain or workflow is unclear enough to change the product shape, use a domain-research skill before inventing UI.

### 2. State The Design Contract

Before implementation, write a compact internal design contract covering:

- Interface archetype and appropriate density
- Primary task and first-screen priority
- Information hierarchy and navigation model
- Visual direction in one sentence
- Typography roles, palette roles, spacing rhythm, geometry, imagery, and motion tone
- Three signature decisions that make the interface recognizably belong to this product
- Model-default choices that would make this product look interchangeable and must be rejected
- Existing components and tokens to reuse
- In Transformation mode, existing UI foundations to replace, contracts to preserve, and obsolete UI to remove after migration
- Required responsive variants and interaction states
- Verification viewports and workflows
- Trust-sensitive decisions, material terms, and reversibility
- Platform conventions and intentional deviations
- Performance budgets and evidence needed for completion claims

Do not use vague direction such as "modern" or "clean" as the design contract. Translate it into observable choices that fit the product.

In concept mode without an accepted visual reference, gather a small reference set before coding when browsing or image tools are available. Include direct product references, an adjacent-domain reference, and a non-UI reference such as editorial, architecture, industrial design, wayfinding, or physical materials when useful. Extract principles for composition, type, color, imagery, density, and motion; do not copy a complete interface or let trend popularity replace product fit.

Create a complete visual concept or screen plan before implementation. Cover the primary screen, downstream regions, and critical states rather than producing only a hero fragment.

### 3. Set The Acceptance And Evidence Contract

For substantial work, define observable acceptance before implementation:

- Primary workflow outcome and one realistic failure, empty, or recovery path
- Required runtime, platforms, viewports, input methods, and content stress cases
- Applicable WCAG 2.2 hard gates and platform accessibility checks
- Purchase, subscription, consent, cancellation, deletion, permission, or sensitive-data conditions
- Web Core Web Vitals budgets or declared native performance budgets
- Screenshots and actual interactions needed as evidence
- User-evidence status and limitations; never imply representative validation when none was run

Use `scripts/validate_ui_evidence.py --init <path>` to create an evidence manifest when the surface and task justify a durable acceptance artifact. Keep the contract proportionate for small changes.

### 4. Design The Complete Experience

Design the real usable surface, not an attractive fragment.

- Build the requested app, tool, store, editor, game, or workflow as the primary experience. Do not replace it with a marketing wrapper unless the user asked for a marketing page.
- Establish the full information architecture before polishing isolated components.
- Cover the happy path plus loading, empty, error, disabled, success, destructive, validation, permission, and unavailable states that the workflow can reach.
- Use realistic content lengths, numbers, labels, images, and records. Placeholder data must exercise the layout rather than flatter it.
- Do not invent brand names, product claims, prices, ratings, testimonials, opening hours, availability, policies, or business facts as if they were real. Use user-provided facts or clearly marked placeholders.
- Show material pricing, renewal, consent, permission, and consequence information before commitment. Keep rejection, cancellation, revocation, and deletion paths honest and usable when applicable.
- Use visual assets when the product, place, object, game, or brand needs to be inspected or felt. Prefer authentic or purpose-created media over generic atmospheric stock imagery.
- Keep important actions and state changes visible. Hide secondary complexity through progressive disclosure instead of flattening every action into one screen.

### 5. Choose A Visual Language, Not A Default Style

Create a coherent system from the product context.

- Give the interface one clear visual point of view.
- Make typography, color, spacing, shape, imagery, iconography, and motion support the same hierarchy.
- Establish the large-scale silhouette and region proportions before polishing components.
- Match density to work: operational tools favor scanning and repeated action; brand and editorial surfaces can use stronger composition and imagery; games must protect the playfield; native apps should respect platform conventions.
- Prefer a few strong decisions over many decorative effects.
- Use contrast, scale, alignment, grouping, and whitespace to communicate importance before adding ornament.
- Make repeated elements consistent and differences intentional.
- Make at least three visible choices traceable to the product's subject, content, workflow, brand, or platform rather than to a generic UI trend.
- Record the layout, density, typography, palette, geometry, surfaces, imagery, motion, and platform strategy when comparing alternatives or unrelated products.

Do not ban or require a color, radius, layout, or style category globally. A monochrome interface, bright palette, dense table, large hero, glass effect, or playful motion can all be correct when the context supports them.

### 6. Avoid Generic AI Design Failure

Reject defaults that appear because they are statistically common rather than product-appropriate.

- Do not turn every section into a floating card or every card into nested cards.
- Do not use oversized marketing typography inside compact tools, dashboards, sidebars, modals, or mobile panels.
- Do not add badges, pills, fake metrics, decorative charts, gradients, glows, blobs, icon rows, or feature grids without a communicative role.
- Do not use a generic landing-page hero when the user asked for an application or tool.
- Do not make every product spacious, sparse, centered, and low-density.
- Do not make operational products illustrative when users need comparison, scanning, and repeated action.
- Do not substitute dark, blurred, cropped, or decorative media when users need to inspect the real product, place, object, state, or gameplay.
- Do not add explanatory UI copy that exists only to describe the interface or advertise features already visible on screen.

Treat this list as a diagnostic, not a replacement style. User direction and a coherent product-specific concept override aesthetic defaults.

If the same layout, typography, surfaces, and decoration could be reused for an unrelated product by changing only the copy and accent color, the art direction is not specific enough. Rework the composition or visual system, not only the palette.

When producing several unrelated products, use `scripts/compare_visual_fingerprints.py` as an early convergence check, then inspect screenshots directly. Do not create arbitrary difference that weakens platform fit, accessibility, or task performance.

### 7. Implement Through The Existing System

- Follow the repository's framework, component, routing, styling, state, icon, and asset conventions.
- Reuse existing primitives and design tokens before creating alternatives outside Transformation mode. In Transformation mode, establish new foundations when the old system would constrain the requested result.
- Keep component ownership clear. Repeated structures should share a component or style primitive; meaningful differences should be explicit variants.
- Use semantic controls that match their behavior: buttons for commands, links for navigation, checkboxes or toggles for binary settings, segmented controls or tabs for modes, and inputs appropriate to the data.
- Prefer familiar icons for common actions. Label unfamiliar icons with accessible names and visible tooltips where appropriate.
- Keep data, state transitions, validation, and user feedback explicit.
- Match windowing, menus, navigation, shortcuts, permissions, safe areas, scaling, and system services to each target platform. A cross-platform app may share product identity without forcing identical chrome and behavior.
- Avoid one giant screen component, copied markup, magic visual values, and layout fixes that only work at one viewport.
- In Transformation mode, remove superseded UI components, styles, and tokens after their consumers have migrated. Do not keep a half-old, half-new interface for convenience.

### 8. Protect Content And Layout

- Define stable layout constraints for boards, tables, toolbars, media, charts, controls, and repeated items.
- Ensure text never overlaps, clips unexpectedly, or escapes its container.
- Test short, typical, and long content, including the longest unbroken word that can realistically occur.
- Preserve hierarchy when text wraps or localizes.
- Make touch targets, focus states, selected states, hover states, and disabled states visible without changing layout dimensions.
- Use responsive composition, not simple shrinking. Reorder, collapse, disclose, or change navigation when the smaller context requires it.

### 9. Verify The Rendered Result

Do not stop at a successful build.

For non-trivial UI work:

- Start the real application and inspect it in a browser, simulator, emulator, or target runtime.
- Verify at least one representative desktop and mobile viewport when the surface is responsive.
- Exercise the primary workflow and at least one failure or empty state.
- Inspect text wrapping, content density, assets, focus, keyboard flow, pointer or touch behavior, loading, layout shift, and console errors.
- Capture screenshots and judge the composition directly.
- Inspect the screen at normal size, thumbnail scale, and in grayscale when hierarchy is uncertain. Check the overall silhouette before polishing isolated controls.
- Compare against supplied references or the stated design contract and keep fixing visible mismatches.
- Run automated accessibility, interaction, or visual checks when the repository supports them, then perform manual checks that automation cannot cover.
- Measure performance against the declared budgets under named conditions; do not turn one lab run into a field-performance claim.
- Validate the UI evidence manifest when one is used and keep every claim bounded by the evidence actually collected.

If rendered verification is unavailable, state exactly what remains unverified. Do not claim visual or responsive completion from source inspection alone.

## Review Mode

When reviewing an existing interface, lead with findings rather than taste commentary.

Order findings by user impact:

1. Broken task flow, misleading behavior, inaccessible interaction, or missing state
2. Deceptive choice architecture, hidden terms, blocked cancellation, privacy harm, or unsupported claims
3. Responsive failure, overflow, overlap, unreadable content, unstable layout, or missed performance budget
4. Weak hierarchy, discoverability, feedback, consistency, or platform fit
5. Generic visual treatment, decoration without purpose, or brand mismatch
6. Maintainability problems that make visual quality fragile

Support findings with screenshots, viewport details, interaction steps, DOM or accessibility evidence, or concrete code references when available. Explain the user consequence and the narrowest correction.

## Scale The Process

Use patch mode for tiny changes, product mode for normal feature work, concept mode for greenfield work, and Transformation mode for broad refactors of an existing interface. Apply only the conditional references required by the surface and risk.

Do not let process documentation become the deliverable. The final result should be a working, visually verified interface.

## Completion Standard

A user-facing interface is complete only when:

- The primary user can complete the primary task
- The hierarchy makes the next action and current state clear
- Required states and recovery paths exist
- The design fits the product, audience, platform, and content
- Repeated elements form a coherent system
- In Transformation mode, the requested surface inventory has migrated to the new system without accidental legacy islands
- Realistic content remains readable across target sizes
- Keyboard, pointer, touch, and accessibility needs are handled as applicable
- Material choices are truthful, reversible, and proportionate to risk
- Target-platform behavior is respected and exercised
- User-facing performance meets declared, measured budgets
- The rendered result has been visually inspected
- Screenshots and actual interaction outcomes cover the required surface
- User-validation, accessibility, and performance claims match the evidence collected
- Known limitations and unverified surfaces are reported honestly
