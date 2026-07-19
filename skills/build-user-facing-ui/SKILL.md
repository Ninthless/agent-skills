---
name: build-user-facing-ui
description: 'Build, redesign, implement, review, or fix the visual and interaction quality of user-facing interfaces. Use when a task changes how a website, landing page, dashboard, admin or CRM tool, commerce or subscription flow, content product, mobile or desktop app, game, editor, or form looks or behaves. Trigger for responsive UI, accessibility, design systems, platform adaptation, consent or cancellation UX, user-facing performance and layout stability, Figma or screenshot implementation, and requests for polished, distinctive, usable, or production-ready UI. Apply context fit, hierarchy, complete states, coherent visuals, trust, measurable evidence, real assets, and rendered verification rather than one fixed style. Do not use for backend/API/database/CLI work, standalone image or logo creation, copy-only translation, privacy-policy prose, backend performance, or headless frontend data logic with no UI impact.'
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
- Read [interaction-accessibility.md](./references/interaction-accessibility.md) for forms, navigation, controls, stateful workflows, responsive behavior, localization, or accessibility-sensitive work.
- Read [accessibility-hard-gates.md](./references/accessibility-hard-gates.md) when exact accessibility requirements matter or before declaring a substantial interface complete.
- Read [platform-guidelines.md](./references/platform-guidelines.md) for native mobile, desktop, Electron, Tauri, or platform-adapted application work.
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

Preserve an established design system unless the user explicitly requests a redesign or the existing system is the problem. If the business domain or workflow is unclear enough to change the product shape, use a domain-research skill before inventing UI.

### 2. State The Design Contract

Before implementation, write a compact internal design contract covering:

- Interface archetype and appropriate density
- Primary task and first-screen priority
- Information hierarchy and navigation model
- Visual direction in one sentence
- Typography roles, palette roles, spacing rhythm, geometry, imagery, and motion tone
- Existing components and tokens to reuse
- Required responsive variants and interaction states
- Verification viewports and workflows
- Trust-sensitive decisions, material terms, and reversibility
- Platform conventions and intentional deviations
- Performance budgets and evidence needed for completion claims

Do not use vague direction such as "modern" or "clean" as the design contract. Translate it into observable choices that fit the product.

For substantial greenfield interfaces or redesigns with no accepted visual reference, create a complete visual concept or screen plan before coding when suitable design or image tools are available. Cover the primary screen, downstream sections, and critical states rather than producing only a hero fragment. Skip this step for small changes and established design-system work where the visual contract is already clear.

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
- Match density to work: operational tools favor scanning and repeated action; brand and editorial surfaces can use stronger composition and imagery; games must protect the playfield; native apps should respect platform conventions.
- Prefer a few strong decisions over many decorative effects.
- Use contrast, scale, alignment, grouping, and whitespace to communicate importance before adding ornament.
- Make repeated elements consistent and differences intentional.
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

When producing several unrelated products, use `scripts/compare_visual_fingerprints.py` as an early convergence check, then inspect screenshots directly. Do not create arbitrary difference that weakens platform fit, accessibility, or task performance.

### 7. Implement Through The Existing System

- Follow the repository's framework, component, routing, styling, state, icon, and asset conventions.
- Reuse existing primitives and design tokens before creating alternatives.
- Keep component ownership clear. Repeated structures should share a component or style primitive; meaningful differences should be explicit variants.
- Use semantic controls that match their behavior: buttons for commands, links for navigation, checkboxes or toggles for binary settings, segmented controls or tabs for modes, and inputs appropriate to the data.
- Prefer familiar icons for common actions. Label unfamiliar icons with accessible names and visible tooltips where appropriate.
- Keep data, state transitions, validation, and user feedback explicit.
- Match windowing, menus, navigation, shortcuts, permissions, safe areas, scaling, and system services to each target platform. A cross-platform app may share product identity without forcing identical chrome and behavior.
- Avoid one giant screen component, copied markup, magic visual values, and layout fixes that only work at one viewport.

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

For a tiny change, apply the same principles locally without producing a full design exercise. For a new product surface or redesign, complete the full workflow and reference set.

Do not let process documentation become the deliverable. The final result should be a working, visually verified interface.

## Completion Standard

A user-facing interface is complete only when:

- The primary user can complete the primary task
- The hierarchy makes the next action and current state clear
- Required states and recovery paths exist
- The design fits the product, audience, platform, and content
- Repeated elements form a coherent system
- Realistic content remains readable across target sizes
- Keyboard, pointer, touch, and accessibility needs are handled as applicable
- Material choices are truthful, reversible, and proportionate to risk
- Target-platform behavior is respected and exercised
- User-facing performance meets declared, measured budgets
- The rendered result has been visually inspected
- Screenshots and actual interaction outcomes cover the required surface
- User-validation, accessibility, and performance claims match the evidence collected
- Known limitations and unverified surfaces are reported honestly
