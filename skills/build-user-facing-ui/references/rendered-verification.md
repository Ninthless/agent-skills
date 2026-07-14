# Rendered Verification

Source inspection, typechecking, and a successful build cannot prove visual quality. Verify the interface in the environment where users experience it.

## Contents

- Verification Matrix
- Render Loop
- Visual Inspection Checklist
- Interaction Proof
- Accessibility And Performance
- Reference And Screenshot Fidelity
- Failure Conditions
- Sources

## Verification Matrix

Choose the smallest matrix that covers the risk.

For responsive web UI, normally include:

- One representative desktop viewport
- One representative mobile viewport
- One narrow or content-stress viewport when layout risk is high

Add cases for:

- Tablet or split-screen layouts
- Landscape mobile
- High zoom or dynamic text
- Dark and light themes
- Reduced motion
- Authenticated and unauthenticated states
- Empty, error, loading, permission, and long-content states
- Touch, keyboard, pointer lock, gamepad, or stylus input

Use actual product requirements when they define a specific device or browser matrix.

## Render Loop

1. Start the real app or target runtime.
2. Navigate to the exact changed surface.
3. Confirm page identity before judging appearance.
4. Exercise the primary interaction path.
5. Capture a screenshot of the meaningful state.
6. Inspect hierarchy, composition, spacing, typography, color, imagery, controls, and content.
7. Record concrete mismatches or defects.
8. Fix the implementation.
9. Repeat the same viewport and interaction until the defect is gone.

Do not rely on memory between screenshots. Compare the latest render against the reference, design contract, or previous screenshot directly.

## Visual Inspection Checklist

### Composition

- Is the primary task or subject the dominant signal?
- Does the first viewport fit the product type?
- Are regions aligned to a coherent container and grid?
- Is density appropriate rather than uniformly sparse or crowded?
- Are repeated sections visually repetitive without a reason?

### Typography

- Does the type hierarchy match information importance?
- Are line length, line height, size, and weight readable?
- Does text wrap without hiding controls or changing intended alignment?
- Is compact UI text sized for the container rather than treated like hero copy?
- Are labels, values, and metadata distinguishable?

### Color And Surfaces

- Do color roles remain consistent?
- Is contrast sufficient in default, hover, focus, selected, disabled, and error states?
- Are borders, fills, and shadows doing useful grouping work?
- Does the palette fit the brand and subject rather than a generic model default?
- Is any effect reducing legibility or hiding media?

### Components And Controls

- Are the same component types visually consistent?
- Are variants meaningful and limited?
- Do controls communicate action, navigation, selection, or state correctly?
- Are icons recognizable, aligned, and from a coherent family?
- Do interaction states preserve stable dimensions?

### Content And Assets

- Are images, products, places, charts, records, and game assets visible and correctly framed?
- Are image crops intentional at every viewport?
- Are there missing, stretched, blurry, placeholder, or unrelated assets?
- Does realistic content reveal overflow or balance problems?

### Responsive Behavior

- Does the composition change intentionally rather than merely shrink?
- Is primary navigation usable?
- Are sticky elements and dialogs usable with a virtual keyboard?
- Are tables, toolbars, charts, and media constrained predictably?
- Is any content clipped, overlapping, inaccessible, or off-screen?

## Interaction Proof

Verify outcomes, not only clicks.

- A filter changes the visible result set and selected state.
- A form validates, submits, exposes pending state, and handles failure.
- A dialog receives focus, closes correctly, and returns focus.
- A navigation action reaches the expected destination and preserves orientation.
- A game menu pauses or gates gameplay input.
- An editor action updates the artifact and exposes save or undo state.

Use tests that resemble real user behavior. Prefer roles, names, and visible outcomes over implementation selectors when the repository supports interaction tests.

## Accessibility And Performance

- Run the repository's accessibility tooling when available.
- Complete a manual keyboard and focus pass.
- Inspect console errors and failed network or asset requests.
- Check loading performance, responsiveness, and layout stability when the public experience or task requires it.
- Avoid adding new dependencies solely for one verification unless the task risk justifies them.

## Reference And Screenshot Fidelity

When a screenshot, Figma frame, or approved concept exists:

- Preserve its information architecture and visible content unless the user requests a change.
- Extract the layout, type, spacing, color, imagery, geometry, and component rules before coding.
- Compare screenshots at matching viewport dimensions.
- Keep a short mismatch ledger with observable differences.
- Do not declare fidelity while major differences remain visible.

When no reference exists, compare the render against the written design contract and quality model.

## Failure Conditions

Do not call the UI complete when:

- Only the build or typecheck ran
- The page was never opened
- Only one convenient viewport was inspected despite responsive requirements
- The primary interaction was not exercised
- Placeholder content concealed a layout problem
- Console, asset, overlap, focus, or accessibility failures remain unexplained
- The result visibly contradicts the reference or design contract

If runtime verification is blocked, report the exact blocker and the remaining risk.

## Sources

- [Playwright Visual Comparisons](https://playwright.dev/docs/test-snapshots)
- [Testing Library Guiding Principles](https://testing-library.com/docs/guiding-principles/)
- [Storybook UI Testing](https://storybook.js.org/docs/writing-tests)
- [Core Web Vitals](https://web.dev/articles/vitals)
