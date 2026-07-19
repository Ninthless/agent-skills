# Transformation Mode

Use Transformation mode when the user asks to refactor, rebuild, overhaul, replace, or completely redo an existing UI or frontend. The goal is to produce the interface that would be designed if the product were rebuilt today with this skill, while preserving valid product behavior unless the user also requests an experience redesign.

## Contents

- Entry Conditions
- Redesign Amplitude
- Instruction Priority
- Transformation Contract
- Inventory The Existing Surface
- Preserve Product Contracts
- Replace The UI System
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

Transformation mode does not override:

- User goals and product correctness
- Business rules and data integrity
- Accessibility and platform requirements
- Trust, privacy, and truthful representation
- Existing functionality that the user expects to keep
- Explicit user constraints, approved references, or brand requirements

Treat the old UI as evidence about features, data, states, and pain points. Do not treat it as the design reference unless the user asks to preserve part of it.

## Transformation Contract

Before implementation, state an internal transformation contract covering:

- Redesign level and the surfaces included
- Product capabilities and contracts to preserve
- UI foundations and legacy patterns to replace
- New art direction and three signature decisions
- New navigation, shell, layout, component, typography, color, geometry, imagery, and motion strategy
- Responsive and platform variants
- Migration order and legacy cleanup boundary
- Proof required to show that the result is structurally different and complete

Do not begin by tweaking the existing CSS. Establish the replacement system and destination architecture first.

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

Mark each item as `replace`, `redesign`, `preserve behavior`, `remove`, or `out of scope`. Do not silently leave low-visibility screens on the old system.

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

Reuse an old primitive only when it already supports the new art direction and interaction contract. Do not reuse it solely to reduce the diff.

## Rebuild The Complete Experience

- Reconstruct the primary workflow end to end in the new system.
- Apply the new visual grammar to every state, not only populated screenshots.
- Replace generic framework defaults for validation, loading, dialogs, menus, and notifications.
- Keep density and hierarchy appropriate to each screen rather than forcing one layout everywhere.
- Maintain coherent identity across operational, account, settings, and edge-case surfaces.
- Use realistic data and assets so the new system is tested under production-like pressure.

Do not create a new landing wrapper while leaving the actual application unchanged.

## Migration Strategy

1. Define the destination art direction and foundations.
2. Build the new shell, navigation, tokens, and shared primitives.
3. Migrate one complete primary workflow and verify the system.
4. Migrate remaining surfaces by workflow or ownership boundary.
5. Exercise responsive, platform, empty, error, permission, and destructive states.
6. Remove obsolete styles, components, and assets after no consumers remain.
7. Verify the complete inventory and search for legacy visual islands.

Use an incremental implementation sequence when the repository requires it, but the delivered result must still satisfy the complete transformation scope.

## Prove The Transformation Magnitude

The transformation should be visible without inspecting CSS values.

Verify that:

- The page silhouette and region proportions reflect the new design contract
- Navigation and screen shells use the new system
- Typography, color, geometry, surfaces, imagery, and motion form a different coherent grammar
- Shared components have been rebuilt or intentionally retained for documented reasons
- At least three product-specific signature decisions appear across the interface
- All requested surfaces use the new system
- Thumbnail comparison shows structural change, not only palette change
- Functional workflows and states still work

Do not impose arbitrary pixel-difference percentages. Judge whether the composition and system changed at a structural level.

## Avoid False Transformations

These do not count as a full UI rebuild by themselves:

- Changing only colors, fonts, radii, shadows, or spacing
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
- Product capabilities and preserved contracts still work
- Remaining out-of-scope or intentionally retained UI is reported explicitly
