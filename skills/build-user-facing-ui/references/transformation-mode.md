# Transformation Mode

Use Transformation mode when the user asks to refactor, rebuild, overhaul, replace, or completely redo an existing UI or frontend. Treat the work as greenfield reconstruction followed by migration. Extract valid product behavior from the old interface, but do not visually derive the destination from its layout, component tree, CSS, tokens, or design system unless the user explicitly asks to preserve something.

## Contents

- Entry Conditions
- Redesign Amplitude
- Instruction Priority
- Transformation Contract
- Inventory The Existing Surface
- Greenfield Reconstruction Protocol
- Visual Quarantine
- Blank-Canvas Destination Design
- Preserve Product Contracts
- Replace The UI System
- Layout Replacement Requirements
- Rebuild The Complete Experience
- Migration Strategy
- Prove The Transformation Magnitude
- Avoid False Transformations
- Completion Standard

## Entry Conditions

Choose Transformation mode when the UI request is broad and includes language such as:

- `重构界面`
- `重构前端`
- `重构所有 UI`
- `完全重构`
- `彻底重做界面`
- `从零重新设计`
- `不要保留旧视觉`
- `refactor the UI`
- `rebuild the entire frontend`
- `full visual overhaul`
- `replace the current design system`

When the build-user-facing-ui skill is active and the user says only `重构` about the UI, frontend, app, site, dashboard, or desktop interface without naming a narrow component, interpret it as a full UI rebuild rather than a polish pass.

Do not choose Transformation mode when:

- The request names one local component, bug, or visual defect
- The user explicitly asks to preserve the existing design system
- The refactor concerns internal component architecture with no visible UI change
- The user asks only for performance, accessibility, or responsive corrections inside the current presentation

Use Patch or Product mode for those narrower cases.

## Redesign Amplitude

Classify the requested magnitude:

| Level | Meaning | Default scope |
| --- | --- | --- |
| 1. Polish | Correct spacing, color, typography, alignment, and local hierarchy | Existing visual system |
| 2. System refresh | Replace tokens and component styling while keeping the main layout and navigation | Shared UI foundations |
| 3. Full UI rebuild | Rebuild screen shells, navigation presentation, layouts, components, visual system, states, and responsive behavior | All user-facing UI in scope |
| 4. Experience redesign | Reconsider information architecture, task flows, feature grouping, and interaction model as well as visual design | Product experience |

An unscoped request to refactor all UI defaults to Level 3. Use Level 4 only when the user explicitly asks to rethink workflows, information architecture, navigation logic, or the overall product experience.

## Instruction Priority

Transformation mode overrides these normal defaults:

- Preserve the existing visual language
- Reuse the existing design tokens
- Reuse existing UI primitives before creating alternatives
- Keep the current page shell, navigation presentation, or component composition
- Make the smallest visual change
- Mirror the local UI style or minimize the UI diff

Transformation mode does not override:

- User goals and product correctness
- Business rules and data integrity
- Accessibility and platform requirements
- Trust, privacy, and truthful representation
- Existing functionality that the user expects to keep
- Explicit user constraints, approved references, or brand requirements

Treat the old UI as evidence about features, data, states, and pain points. Do not treat it as a visual or structural reference unless the user asks to preserve part of it. For a broad rebuild, replacing the complete visible system is the narrowest correct implementation even when the code diff is large.

## Transformation Contract

Before implementation, state an internal transformation contract covering:

- Redesign level and the surfaces included
- Neutral product specification: capabilities, content, data, routes, states, permissions, workflows, and platform contracts
- UI foundations and legacy patterns to replace
- New art direction and three signature decisions
- New navigation, shell, layout, component, typography, color, geometry, imagery, and motion strategy
- Responsive and platform variants
- Migration order and legacy cleanup boundary
- Proof required to show that the result is structurally different and complete

Do not begin by tweaking the existing CSS, editing legacy components, or styling the existing DOM. Establish the replacement system and destination architecture first.

## Inventory The Existing Surface

Build a user-facing inventory before editing:

- Application shells and navigation
- Routes, screens, windows, tabs, and modes
- Repeated lists, tables, cards, canvases, maps, timelines, and editors
- Forms, filters, search, bulk actions, and settings
- Dialogs, drawers, menus, popovers, tooltips, toasts, and context menus
- Authentication, onboarding, permissions, account, and destructive flows
- Loading, empty, no-results, error, offline, unavailable, success, and recovery states
- Desktop, mobile, tablet, native, window-size, theme, and input variants
- Shared components, tokens, icons, assets, and layout primitives

For each item, record its capability, inputs, outputs, states, dependencies, and preservation requirement. Mark its visible implementation as `replace`, `redesign`, `remove`, `explicitly preserve`, or `out of scope`. Do not silently leave low-visibility screens on the old system.

Translate the inventory into product language before designing. Prefer statements such as "compare active accounts, filter by risk, and open account detail" over legacy layout language such as "three metric cards above a table inside the dashboard shell."

## Greenfield Reconstruction Protocol

Follow this sequence for Level 3 and Level 4 work:

1. Audit the old product for capabilities, data, workflows, states, permissions, routes, shortcuts, and platform behavior.
2. Convert that audit into a neutral product specification with no legacy layout or component prescriptions.
3. Quarantine the old visual system and stop using it as a design reference.
4. Gather product, domain, platform, adjacent-domain, and non-UI references as if the interface did not yet exist.
5. Design a blank-canvas destination architecture, art direction, navigation model, screen map, page templates, and UI foundations.
6. Implement the destination system independently, then map preserved product contracts into it.
7. Verify every workflow and state, remove superseded UI, and report any intentionally retained legacy surface.

Do not reverse steps 5 and 6. Starting from legacy components and gradually making them look different usually preserves the old composition and fails Transformation mode.

## Visual Quarantine

After the neutral product specification and migration inventory exist:

- Stop consulting old screenshots for composition, hierarchy, spacing, typography, geometry, color, or component ideas.
- Do not use legacy component names, DOM structure, CSS selectors, token names, or page-template names in the destination design plan.
- Keep the legacy inventory only as a functional coverage checklist and later migration map.
- Reopen legacy screens during migration only to verify a capability, state, contract, or cleanup target after the destination design is fixed.
- Preserve brand assets, platform conventions, or specific UI elements only when the user, law, contract, or product identity requires them; document each exception.

If the destination concept can only be explained by saying how the old layout will be restyled, quarantine has failed. Rewrite the concept from product goals and content.

## Blank-Canvas Destination Design

Design the replacement as if no user-facing components exist yet.

- Base the concept on the product's users, jobs, content, risk, frequency, platform, brand, and external references.
- Explore at least two materially different macro-structures for Level 3 or 4 work. Vary navigation model, information grouping, screen boundaries, workspace silhouette, density, and primary-region composition rather than only decoration.
- Choose the structure that best supports the primary workflows and platform, then define the complete screen map and responsive variants.
- Define new shell, navigation, page templates, region layout, hierarchy, density, typography, geometry, surfaces, imagery, iconography, motion, and state presentation before adapting old functionality.
- Name destination components by product role or interaction responsibility, not by the legacy component they replace.
- Do not begin implementation until the destination can be described without reference to the old UI's layout.

The destination may share familiar platform patterns when they are correct. Familiarity is not a reason to preserve this product's old composition.

## Preserve Product Contracts

Unless the user requests Level 4, preserve:

- Core user jobs and feature availability
- Business rules, validation, permissions, and destructive safeguards
- API and data contracts
- Authentication and authorization boundaries
- Persistence, save, undo, recovery, and offline behavior
- Public route or deep-link contracts when other systems may depend on them
- Important platform conventions and keyboard shortcuts

The implementation may reorganize frontend components and internal UI state when required by the new system. Avoid unrelated backend, database, or service refactors.

Level 3 may regroup navigation, change page or panel boundaries, combine or separate presentations, and alter information grouping while preserving feature meaning, reachability, permissions, outcomes, and important deep links. Level 4 additionally authorizes changes to user jobs, workflow semantics, feature grouping logic, and product behavior.

## Replace The UI System

Level 3 authorizes replacement of:

- Design tokens and semantic color roles
- Typography scale and text roles
- Spacing, grid, container, and breakpoint strategy
- Geometry, radius, borders, elevation, and surface treatment
- Page shells, navigation presentation, and region composition
- Component visual language and variants
- Iconography, imagery, illustration, and data-display treatment
- Motion, transitions, feedback, and loading presentation
- Responsive composition and desktop window layouts

Reuse an old primitive only after the destination design is fixed and only when its rendered behavior already matches that design without pulling legacy composition or styling into the new system. Do not reuse it solely to reduce the diff.

## Layout Replacement Requirements

For Level 3, explicitly redesign all of these unless the user names an exception:

- Global application shell or window workspace
- Navigation composition and wayfinding
- Page, screen, or workspace templates
- Primary and secondary region layout
- Information grouping and component composition
- Hierarchy, density, and responsive restructuring

The final result must materially diverge across several structural dimensions, not merely expressive ones. Normally change at least four of the six dimensions above, including either the shell or navigation and the primary-region layout. If a dimension remains similar because the product or platform strongly requires it, state the reason and make the other structural decisions independently.

The following fail Level 3:

- Keeping the same DOM or component tree and applying new CSS
- Keeping the same sidebar, topbar, card grid, table, and page-template arrangement with new tokens
- Adding a replacement shell while legacy pages remain structurally unchanged inside it
- Changing component-library imports without changing information grouping or region composition

## Rebuild The Complete Experience

- Reconstruct the primary workflow end to end in the new system.
- Apply the new visual grammar to every state, not only populated screenshots.
- Replace generic framework defaults for validation, loading, dialogs, menus, and notifications.
- Keep density and hierarchy appropriate to each screen rather than forcing one layout everywhere.
- Maintain coherent identity across operational, account, settings, and edge-case surfaces.
- Use realistic data and assets so the new system is tested under production-like pressure.

Do not create a new landing wrapper while leaving the actual application unchanged.

## Migration Strategy

1. Freeze the blank-canvas destination architecture and art direction.
2. Build the new shell, navigation, page templates, tokens, and shared primitives without importing legacy visual structure.
3. Map one complete primary workflow from the neutral product specification into the new system and verify it.
4. Migrate remaining surfaces by workflow or ownership boundary.
5. Exercise responsive, platform, empty, error, permission, and destructive states.
6. Remove obsolete styles, components, assets, wrappers, and tokens after no consumers remain.
7. Verify the complete inventory and search for legacy visual or structural islands.

Use an incremental implementation sequence when the repository requires it, but the delivered result must still satisfy the complete transformation scope.

## Prove The Transformation Magnitude

The transformation should be visible without inspecting CSS values.

Verify that:

- The page silhouette and region proportions reflect the new design contract
- Navigation, screen shells, page templates, region layouts, and information grouping use the new system
- Typography, color, geometry, surfaces, imagery, and motion form a different coherent grammar
- Shared components have been rebuilt or intentionally retained for documented reasons
- At least three product-specific signature decisions appear across the interface
- All requested surfaces use the new system
- Thumbnail comparison shows structural change, not only palette change
- Functional workflows and states still work

Record a compact old-versus-new structural comparison for shell, navigation, screen boundaries, region composition, grouping, hierarchy, density, and responsive behavior. Similarity needs a product or platform reason, not implementation convenience.

Do not impose arbitrary pixel-difference percentages. Judge whether the composition and system changed at a structural level.

## Avoid False Transformations

These do not count as a full UI rebuild by themselves:

- Changing only colors, fonts, radii, shadows, or spacing
- Keeping the same DOM, component hierarchy, or page templates and replacing only CSS
- Wrapping old pages in a new sidebar or marketing shell
- Replacing one component library while preserving the same generic composition
- Redesigning only the dashboard while leaving settings, forms, dialogs, and states unchanged
- Adding gradients, animation, illustration, or glass effects to the old structure
- Renaming components without changing the rendered experience
- Preserving old UI inconsistencies because existing components are convenient

If the old and new products would look substantially the same in grayscale or at thumbnail scale, revisit the transformation contract.

## Completion Standard

Transformation mode is complete only when:

- Every in-scope surface has a migration decision
- All migrated surfaces use the new design system
- The primary and recovery workflows pass
- No accidental legacy visual islands remain
- Obsolete UI code created redundant by the transformation is removed
- The rendered result is structurally and visually different
- The shell, navigation or workspace composition, primary-region layout, and several other structural dimensions differ from the legacy interface unless explicitly preserved
- Product capabilities and preserved contracts still work
- Remaining out-of-scope or intentionally retained UI is reported explicitly
