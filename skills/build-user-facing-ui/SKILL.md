---
name: build-user-facing-ui
description: 'Build, redesign, implement, review, or fix the visual and interaction quality of user-facing interfaces. Use when a task changes how a website, landing page, dashboard, admin or CRM tool, commerce flow, content product, mobile or desktop app, game, editor, or form looks or behaves. Trigger for responsive UI, accessibility, design systems, Figma or screenshot implementation, and requests for polished, distinctive, usable, or production-ready UI. Apply context fit, hierarchy, complete states, coherent visuals, real assets, and rendered verification rather than one fixed style. Do not use for backend/API/database/CLI work, standalone image or logo creation, copy-only translation, or headless frontend data logic with no UI impact.'
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
- Read [rendered-verification.md](./references/rendered-verification.md) before verifying any non-trivial rendered interface.

## Priority Order

Resolve tradeoffs in this order:

1. User goal and product correctness
2. Interaction clarity and state completeness
3. Accessibility and input compatibility
4. Context and design-system coherence
5. Responsive content integrity
6. Visual hierarchy and craft
7. Performance and implementation maintainability
8. Novelty and decorative expression

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

Do not use vague direction such as "modern" or "clean" as the design contract. Translate it into observable choices that fit the product.

For substantial greenfield interfaces or redesigns with no accepted visual reference, create a complete visual concept or screen plan before coding when suitable design or image tools are available. Cover the primary screen, downstream sections, and critical states rather than producing only a hero fragment. Skip this step for small changes and established design-system work where the visual contract is already clear.

### 3. Design The Complete Experience

Design the real usable surface, not an attractive fragment.

- Build the requested app, tool, store, editor, game, or workflow as the primary experience. Do not replace it with a marketing wrapper unless the user asked for a marketing page.
- Establish the full information architecture before polishing isolated components.
- Cover the happy path plus loading, empty, error, disabled, success, destructive, validation, permission, and unavailable states that the workflow can reach.
- Use realistic content lengths, numbers, labels, images, and records. Placeholder data must exercise the layout rather than flatter it.
- Do not invent brand names, product claims, prices, ratings, testimonials, opening hours, availability, policies, or business facts as if they were real. Use user-provided facts or clearly marked placeholders.
- Use visual assets when the product, place, object, game, or brand needs to be inspected or felt. Prefer authentic or purpose-created media over generic atmospheric stock imagery.
- Keep important actions and state changes visible. Hide secondary complexity through progressive disclosure instead of flattening every action into one screen.

### 4. Choose A Visual Language, Not A Default Style

Create a coherent system from the product context.

- Give the interface one clear visual point of view.
- Make typography, color, spacing, shape, imagery, iconography, and motion support the same hierarchy.
- Match density to work: operational tools favor scanning and repeated action; brand and editorial surfaces can use stronger composition and imagery; games must protect the playfield; native apps should respect platform conventions.
- Prefer a few strong decisions over many decorative effects.
- Use contrast, scale, alignment, grouping, and whitespace to communicate importance before adding ornament.
- Make repeated elements consistent and differences intentional.

Do not ban or require a color, radius, layout, or style category globally. A monochrome interface, bright palette, dense table, large hero, glass effect, or playful motion can all be correct when the context supports them.

### 5. Avoid Generic AI Design Failure

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

### 6. Implement Through The Existing System

- Follow the repository's framework, component, routing, styling, state, icon, and asset conventions.
- Reuse existing primitives and design tokens before creating alternatives.
- Keep component ownership clear. Repeated structures should share a component or style primitive; meaningful differences should be explicit variants.
- Use semantic controls that match their behavior: buttons for commands, links for navigation, checkboxes or toggles for binary settings, segmented controls or tabs for modes, and inputs appropriate to the data.
- Prefer familiar icons for common actions. Label unfamiliar icons with accessible names and visible tooltips where appropriate.
- Keep data, state transitions, validation, and user feedback explicit.
- Avoid one giant screen component, copied markup, magic visual values, and layout fixes that only work at one viewport.

### 7. Protect Content And Layout

- Define stable layout constraints for boards, tables, toolbars, media, charts, controls, and repeated items.
- Ensure text never overlaps, clips unexpectedly, or escapes its container.
- Test short, typical, and long content, including the longest unbroken word that can realistically occur.
- Preserve hierarchy when text wraps or localizes.
- Make touch targets, focus states, selected states, hover states, and disabled states visible without changing layout dimensions.
- Use responsive composition, not simple shrinking. Reorder, collapse, disclose, or change navigation when the smaller context requires it.

### 8. Verify The Rendered Result

Do not stop at a successful build.

For non-trivial UI work:

- Start the real application and inspect it in a browser, simulator, emulator, or target runtime.
- Verify at least one representative desktop and mobile viewport when the surface is responsive.
- Exercise the primary workflow and at least one failure or empty state.
- Inspect text wrapping, content density, assets, focus, keyboard flow, pointer or touch behavior, loading, layout shift, and console errors.
- Capture screenshots and judge the composition directly.
- Compare against supplied references or the stated design contract and keep fixing visible mismatches.
- Run automated accessibility, interaction, or visual checks when the repository supports them, then perform manual checks that automation cannot cover.

If rendered verification is unavailable, state exactly what remains unverified. Do not claim visual or responsive completion from source inspection alone.

## Review Mode

When reviewing an existing interface, lead with findings rather than taste commentary.

Order findings by user impact:

1. Broken task flow, misleading behavior, inaccessible interaction, or missing state
2. Responsive failure, overflow, overlap, unreadable content, or unstable layout
3. Weak hierarchy, discoverability, feedback, consistency, or platform fit
4. Generic visual treatment, decoration without purpose, or brand mismatch
5. Maintainability problems that make visual quality fragile

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
- The rendered result has been visually inspected
- Known limitations and unverified surfaces are reported honestly
