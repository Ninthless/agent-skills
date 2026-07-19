# Rendered Verification

Source inspection, typechecking, and a successful build cannot prove visual quality. Verify the interface in the environment where users experience it.

## Contents

- Verification Matrix
- Render Loop
- Visual Inspection Checklist
- Interaction Proof
- Accessibility And Performance
- Evidence Artifact
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
- Complete the manual keyboard, focus, target-size, non-color, and zoom or scaling gates in [accessibility-hard-gates.md](./accessibility-hard-gates.md).
- Inspect console errors and failed network or asset requests.
- For web surfaces, measure LCP, INP, and CLS against the declared budgets. Use 2500 milliseconds, 200 milliseconds, and 0.1 as defaults when the project has no stricter public-web budgets.
- For native surfaces, declare and measure scenario-specific budgets rather than inventing universal thresholds.
- Avoid adding new dependencies solely for one verification unless the task risk justifies them.

## Evidence Artifact

For substantial work, record the acceptance result in a UI evidence manifest or an equivalent project-native artifact.

- Link screenshots to required viewports and meaningful states.
- Record a passing primary workflow and one passing empty, error, unavailable, permission, or recovery path.
- Record console and asset failures, accessibility gates, trust-sensitive conditions, performance measurements, and user-evidence limits.
- Run `python scripts/validate_ui_evidence.py <manifest>` when using the bundled schema.
- Use [evidence-performance.md](./evidence-performance.md) to keep performance and user-validation claims proportional to the collected evidence.

The manifest supplements project tests and direct visual inspection. It does not replace them.

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
- A declared performance budget fails without an accepted exception
- Trust-sensitive actions hide terms or obstruct rejection, cancellation, revocation, or recovery
- The result visibly contradicts the reference or design contract
- Completion, accessibility, performance, or user-validation claims exceed the evidence collected

If runtime verification is blocked, report the exact blocker and the remaining risk.

## Sources

- [Playwright Visual Comparisons](https://playwright.dev/docs/test-snapshots)
- [Testing Library Guiding Principles](https://testing-library.com/docs/guiding-principles/)
- [Storybook UI Testing](https://storybook.js.org/docs/writing-tests)
- [Core Web Vitals](https://web.dev/articles/vitals)
