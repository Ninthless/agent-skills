# Accessibility Hard Gates

Use this reference when accessibility requirements are material, when a public or regulated service is involved, or before declaring a substantial interface complete. Treat these as minimum observable gates, not the whole accessibility practice.

## Contents

- Required Baseline
- Keyboard And Focus
- Pointer And Touch
- Forms And Authentication
- Zoom, Reflow, And Text
- Contrast And Non-Color Meaning
- Semantics And Announcements
- Conditional Gates
- Evidence
- Sources

## Required Baseline

Target WCAG 2.2 Level AA unless the product has a stricter contract. Do not describe an interface as accessible from an automated scan alone.

For every substantial primary workflow:

- Complete it with keyboard-only input where a keyboard is applicable.
- Preserve a logical focus order and visible focus indicator.
- Keep focused controls at least partially visible and unobscured by sticky regions.
- Expose programmatic names, roles, values, states, errors, and status changes.
- Keep information and actions understandable without color alone.
- Verify zoom, text enlargement, and reflow in the target runtime.
- Record automated critical violations and resolve or explicitly report them.

## Keyboard And Focus

- Every interactive element must be reachable and operable without a pointer unless the task fundamentally requires path-based input.
- Focus order must follow the visual and task order.
- Opening a dialog moves focus into it; closing returns focus to the invoking control when that control still exists.
- Menus, tabs, listboxes, grids, and composite widgets must follow the expected platform interaction pattern.
- Focus must not be entirely hidden by sticky headers, footers, cookie banners, dialogs, or virtual keyboards.
- The visible focus indicator must remain distinguishable from the component and adjacent colors.

WCAG 2.2 Level AA requires Focus Not Obscured (Minimum). Focus Appearance is Level AAA, but use its measurable target when the project has no stronger design-system rule: an indicator area at least equivalent to a 2 CSS-pixel perimeter and a contrast change of at least 3:1.

## Pointer And Touch

- Provide a non-drag alternative for functionality that uses dragging, unless dragging is essential or supplied by the user agent.
- Make pointer targets at least 24 by 24 CSS pixels or provide sufficient spacing or an allowed exception under WCAG 2.2 Target Size (Minimum).
- Use the platform's larger recommended touch target when space permits; 24 CSS pixels is a compliance floor, not a comfort target.
- Do not require precise hover, multi-pointer gestures, or motion input for essential actions without an equivalent path.
- Prevent accidental activation of destructive or costly actions and provide recovery when practical.

## Forms And Authentication

- Give every input a persistent accessible name and visible label unless the control is conventionally self-labelled.
- Put instructions before they are needed and associate errors with the relevant fields.
- Preserve entered values after validation failure when retaining them is safe.
- Avoid asking users to enter the same information twice in one process unless repetition is essential, required for security, or the earlier value can be selected or auto-populated.
- Do not block password managers or paste.
- Avoid cognitive-function tests in authentication. If one is required, provide an accessible alternative or an allowed mechanism such as object recognition or personal-content recognition.
- Make verification, recovery, timeout, and lockout states explicit.

## Zoom, Reflow, And Text

For responsive web surfaces:

- Verify text enlargement to 200 percent without loss of content or functionality.
- Verify reflow at 320 CSS pixels wide or the equivalent of 400 percent zoom at a 1280-pixel viewport, except for content that inherently requires two-dimensional layout.
- Keep controls, labels, validation, and reading order usable after wrapping.
- Do not require horizontal and vertical scrolling for ordinary prose and form workflows.
- Allow text spacing overrides without clipping or overlap.

For native surfaces, use dynamic type or the platform text-scaling mechanism and verify the largest supported size appropriate to the product.

## Contrast And Non-Color Meaning

- Normal text needs at least 4.5:1 contrast.
- Large text needs at least 3:1 contrast.
- Interactive boundaries, meaningful icons, focus indicators, and graphical objects need at least 3:1 against adjacent colors when required for identification.
- Disabled controls are exempt from some WCAG contrast requirements, but they must remain understandable in context.
- Reinforce color-coded status with text, shape, iconography, pattern, position, or another persistent signal.
- Check every interactive state, not only the default state.

## Semantics And Announcements

- Use native elements before custom roles.
- Maintain valid heading, landmark, list, table, and form structure.
- Announce asynchronous results, validation summaries, loading completion, and important state changes without moving focus unnecessarily.
- Give images alternatives that match their purpose; decorative images should not create noise.
- Keep accessible names consistent with visible labels.
- Preserve reading and focus order when responsive layouts visually reorder content.

## Conditional Gates

Apply these when the feature exists:

| Condition | Required gate |
| --- | --- |
| Dragging | Equivalent single-pointer operation without dragging |
| Authentication | Password managers and paste work; no unsupported cognitive-function test |
| Repeated entry | Previously supplied information is selectable or auto-populated unless exempt |
| Persistent help | Help appears in a consistent relative order across the process |
| Time limit | Users can extend, adjust, or disable it unless an allowed exception applies |
| Motion | Reduced-motion preference is respected for non-essential motion |
| Audio or video | Required captions, transcript, controls, and alternatives exist |
| Data visualization | Meaning is available beyond color and visual geometry alone |

## Evidence

Record the following in the UI evidence manifest or equivalent test artifact:

- Keyboard completion result for the primary workflow
- Focus visibility and focus-obscuring result
- Minimum observed target size
- Drag alternative result when dragging exists
- Authentication result when authentication exists
- Zoom, text scaling, and reflow result
- Automated critical violation count and tool used
- Known assistive-technology or platform gaps

Never convert an unrun check into a pass. Mark it unverified and explain the limitation.

## Sources

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [W3C Accessibility Principles](https://www.w3.org/WAI/fundamentals/accessibility-principles/)
- [Fluent 2 Accessibility](https://fluent2.microsoft.design/accessibility)
- [Apple Accessibility](https://developer.apple.com/accessibility/)
