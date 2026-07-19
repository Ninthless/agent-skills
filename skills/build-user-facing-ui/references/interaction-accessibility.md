# Interaction And Accessibility

## Contents

- State Inventory
- Feedback
- Forms
- Navigation And Orientation
- Controls And Affordance
- Keyboard And Focus
- Semantics
- Responsive Composition
- Text And Localization
- Motion
- Accessibility Verification
- Sources

## State Inventory

For every asynchronous, editable, permissioned, destructive, or data-dependent surface, consider:

- Initial
- Loading and delayed loading
- Partial or streaming
- Populated
- Empty
- No matching results
- Validation error
- Request or system error
- Offline or stale
- Disabled or unavailable
- Read-only or insufficient permission
- Success and confirmation
- Destructive confirmation and recovery

Do not create every state mechanically. Include states the real workflow can reach and make their visual treatment coherent.

## Feedback

- Show the result of user actions near the affected object.
- Keep progress visible for operations that take noticeable time.
- Preserve user input when retrying after a recoverable failure.
- Distinguish saving, saved, failed, and unsaved states.
- Avoid success messages for actions whose result is already obvious unless persistence or risk makes confirmation valuable.
- Never use color as the only status signal.

## Forms

- Use labels that remain available after input.
- Choose controls that match the data and expected choice count.
- Provide formats, constraints, and examples before users fail when the requirement is not obvious.
- Validate at a time that helps correction without interrupting entry unnecessarily.
- Place error messages near the field and provide a useful summary for long forms when appropriate.
- Preserve values after validation or server errors.
- Make required and optional status explicit.
- Support keyboard submission only when it is predictable and safe.
- Prevent duplicate submission and expose pending state.

## Navigation And Orientation

- Make the current location, selected object, or active mode visible.
- Use links for navigation and buttons for commands.
- Preserve expected browser, platform, and system back behavior.
- Do not hide primary navigation behind an unfamiliar control without a strong space or product reason.
- Keep labels stable; do not rename the same destination across contexts.
- Use breadcrumbs, tabs, sidebars, history, or contextual back navigation according to information depth and platform.

## Controls And Affordance

- Match control appearance to behavior and state.
- Use familiar icons for common actions and accessible labels for all icon controls.
- Add visible tooltips for unfamiliar icons on pointer-based interfaces.
- Keep control dimensions stable across hover, active, selected, loading, and disabled states.
- Do not use a toggle for an action or a button for persistent binary state.
- Make destructive actions visually distinct without allowing them to dominate normal work.
- Keep touch and pointer targets large enough for the intended platform and spacing.

## Keyboard And Focus

- Make all interactive functionality reachable without a pointer when the platform expects keyboard access.
- Preserve a logical focus order that follows the visual and task order.
- Make focus clearly visible against every background.
- Move focus intentionally when opening and closing dialogs, drawers, menus, and dynamic workflows.
- Return focus to the invoking control when a temporary surface closes.
- Avoid keyboard traps, except where a modal interaction deliberately contains focus and provides an exit.
- Support escape and arrow-key behavior where platform patterns expect them.

## Semantics

- Use native semantic elements and controls before recreating them.
- Preserve heading hierarchy and landmark structure.
- Associate labels, instructions, errors, descriptions, and status messages with the relevant control.
- Give images useful alternatives when they convey information; use empty alternatives for decoration.
- Do not add ARIA that contradicts native behavior.
- Expose dynamic status changes without creating excessive announcements.

## Responsive Composition

- Start from task priority, not a fixed breakpoint list.
- Define which regions remain, move, collapse, scroll, disclose, or become modal at smaller sizes.
- Preserve the primary action and critical state.
- Avoid horizontal page scrolling unless the artifact itself requires a pan or canvas.
- Let data tables scroll or transform deliberately; do not silently remove important columns.
- Keep media in stable aspect ratios and define crop behavior.
- Test mobile navigation, virtual keyboard, sticky controls, drawers, dialogs, and long content.
- Ensure hover-only information has a touch and keyboard path.

## Text And Localization

- Test realistic long labels, names, values, validation messages, and unbroken strings.
- Do not place critical text in containers with fixed heights unless overflow behavior is deliberate.
- Allow text to wrap without covering adjacent controls.
- Avoid relying on exact English string length for alignment.
- Keep text legible under browser zoom or platform dynamic type.
- Use tabular numerals when changing numeric values must remain aligned.
- Use locale-aware number, date, currency, and plural formatting when production data requires it.

## Motion

- Use motion to explain hierarchy, continuity, state change, causality, or reward.
- Avoid motion that delays common work or competes with reading and input.
- Keep durations and easing consistent with the product tone.
- Respect reduced-motion preferences for non-essential animation.
- Pause or reduce background motion behind dialogs and text-heavy overlays when needed for clarity.

## Accessibility Verification

Perform both automated and manual checks when practical.

Automated checks can detect common contrast, naming, structure, role, and attribute failures. They cannot determine whether language is clear, focus movement is sensible, alternative text is useful, the reading order matches intent, or the complete task works with assistive technology.

Minimum manual pass for a web interface:

1. Complete the primary workflow with keyboard only.
2. Verify visible focus and logical order.
3. Inspect headings, landmarks, labels, names, and status messages.
4. Zoom and check reflow.
5. Check that color is not the only information channel.
6. Test one error and one empty or unavailable state.

Apply the exact conditional requirements in [accessibility-hard-gates.md](./accessibility-hard-gates.md) before declaring a substantial interface complete. Use current platform accessibility guidance when building native or specialized interfaces.

## Sources

- [W3C Accessibility Principles](https://www.w3.org/WAI/fundamentals/accessibility-principles/)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [W3C Selecting Accessibility Evaluation Tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/)
- [Nielsen Norman Group Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
