# UI Quality Model

## Definition

Good UI enables specified users to achieve specified goals effectively, efficiently, and with satisfaction in the real context of use. It makes information perceivable, interaction operable, behavior understandable, and implementation robust. It expresses a coherent product identity without allowing visual style to obstruct the task.

Quality is contextual. The same visual treatment can be excellent for one product and harmful for another.

## Quality Dimensions

### 1. Purpose Fit

- The interface serves a real user goal rather than displaying available features.
- The most important task receives the strongest hierarchy and shortest practical path.
- Density, language, controls, and navigation match user expertise, frequency, urgency, and risk.
- The first screen reveals the actual product, place, object, workflow, or gameplay when that is what the user came to use or inspect.

### 2. Effectiveness And Efficiency

- Users can complete the intended task accurately.
- Common actions are easy to find and repeat.
- The interface reduces memory load through visible choices, sensible defaults, and recognition.
- Expert users can work quickly without making first-time use incomprehensible.
- Destructive, costly, or irreversible actions receive proportional friction.

### 3. Clarity And Hierarchy

- Importance is communicated through position, scale, contrast, grouping, rhythm, and language.
- Every major region has an obvious role.
- Labels name the user's object or action rather than internal implementation concepts.
- The current state, available actions, and result of an action are visible.
- Visual simplicity comes from removing ambiguity and low-value elements, not from emptying the screen.

### 4. Interaction Quality

- Controls look and behave like their function.
- Navigation is predictable and preserves orientation.
- Feedback arrives quickly and at the location where it matters.
- Errors are prevented when practical and recoverable when they occur.
- Loading, empty, error, disabled, success, validation, and permission states are designed rather than left to framework defaults.

### 5. Accessibility And Inclusion

- Information is perceivable without depending on one color, sense, or input method.
- The interface can be operated by keyboard and relevant assistive technology.
- Focus, labels, structure, instructions, errors, and targets are understandable.
- Content reflows and remains usable when zoomed, localized, or viewed on a small screen.
- Automated checks support but do not replace manual judgement and task testing.

### 6. Contextual Coherence

- The interface follows the product's design system and the target platform's conventions unless there is a reason to diverge.
- Repeated patterns remain consistent across screens and states.
- Brand expression appears in meaningful choices such as typography, imagery, composition, language, and motion rather than decoration alone.
- New components have a clear relationship to existing components and tokens.

### 7. Visual Craft

- The composition has one intentional point of view.
- Typography is readable and establishes a disciplined hierarchy.
- Color roles are clear and contrast is sufficient.
- Spacing and alignment reveal relationships.
- Geometry, borders, shadows, icons, imagery, and motion use a consistent visual grammar.
- Decorative elements earn their space by adding meaning, atmosphere, orientation, or delight appropriate to the product.

Attractiveness matters because it affects perceived usability, trust, attention, and willingness to engage. It cannot compensate for broken behavior.

### 8. Content Integrity

- Copy, data, media, and labels resemble production content.
- Long names, large values, missing images, validation messages, and unusual records do not break the layout.
- Media shows the real subject when users need evidence or inspection.
- Placeholder content tests the design instead of making it look artificially balanced.

### 9. Adaptability

- The layout responds to available space, content, device, input, and orientation.
- Mobile and desktop compositions preserve the task rather than merely scaling.
- Text wrapping, zoom, localization, dynamic type, and reduced motion are considered where applicable.
- Persistent chrome does not consume space needed for the primary experience.

### 10. Performance And Stability

- The primary content appears promptly.
- Interaction feedback remains responsive.
- Layout does not shift unexpectedly.
- Assets are appropriately sized and loaded.
- Animation and visual complexity do not undermine responsiveness, battery, or clarity.

### 11. Trust And Agency

- Material prices, terms, consequences, and data uses are visible before commitment.
- Accept, reject, cancel, revoke, delete, and recover paths are honest and proportionate.
- The interface does not fabricate urgency, scarcity, authority, social proof, or certainty.
- Defaults protect users when decisions are costly, public, sensitive, or hard to reverse.
- High-impact recommendations expose source, freshness, confidence, limitations, and escalation where applicable.

### 12. Evidence Integrity

- Completion claims are supported by rendered screenshots and actual task outcomes.
- Accessibility combines automated checks with manual input, focus, zoom, and semantic verification.
- Performance claims name the budget, measurement mode, conditions, and result.
- User-validation claims name the participants, task, result, and limitations.
- Unknown or untested conditions remain explicit instead of being converted into confidence.

### 13. Distinctiveness Without Formula

- The visual language follows the product's content, audience, platform, and brand.
- Unrelated products differ in several structural or expressive dimensions when context supports it.
- Products in one family preserve useful shared patterns.
- Difference comes from a product-specific design thesis rather than arbitrary decoration or palette swapping.

## Hard Gates And Flexible Choices

Hard gates are observable failures:

- The task cannot be completed
- State or feedback is missing
- Text overlaps or becomes unreadable
- Controls cannot be reached or understood
- The layout fails at a target viewport
- Required content or media is absent
- The interface violates an established product contract
- A material choice is deceptive, obscured, or needlessly difficult to reverse
- A declared accessibility or performance budget fails
- The result was never rendered or exercised
- A completion or validation claim exceeds the recorded evidence

Flexible choices depend on context:

- Light or dark
- Dense or spacious
- Minimal or expressive
- Flat, bordered, elevated, glass, textured, or illustrative
- Neutral, monochrome, or colorful
- Geometric, soft, editorial, playful, technical, or cinematic

Do not turn flexible choices into universal bans. Judge whether the choice supports the user, product, content, and platform.

## Research Basis

- [ISO 9241-11 usability](https://www.iso.org/obp/ui/#iso:std:iso:9241:-11:ed-2:v1:en): effectiveness, efficiency, satisfaction, and context of use.
- [Nielsen Norman Group usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/): status visibility, real-world match, user control, consistency, error handling, recognition, efficiency, minimalist design, and help.
- [Nielsen Norman Group usability components](https://www.nngroup.com/articles/usability-101-introduction-to-usability/): learnability, efficiency, memorability, errors, and satisfaction.
- [W3C accessibility principles](https://www.w3.org/WAI/fundamentals/accessibility-principles/): perceivable, operable, understandable, and robust interfaces.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): reflow, focus, input, target size, and accessible interaction requirements.
- [GOV.UK design principles](https://www.gov.uk/guidance/government-design-principles): start with user needs, do less, design with data, make complexity simple, and iterate.
- [Apple design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles): hierarchy, consistency, and platform-appropriate experience.
- [Core Web Vitals](https://web.dev/articles/vitals): loading performance, responsiveness, and layout stability.
- [FTC report on dark patterns](https://www.ftc.gov/news-events/news/press-releases/2022/09/ftc-report-shows-rise-sophisticated-dark-patterns-designed-trick-trap-consumers): deceptive choice architecture, hidden terms, difficult cancellation, and manipulative privacy choices.
- [Windows App Design](https://learn.microsoft.com/windows/apps/design/): platform-appropriate navigation, commands, windowing, input, and accessibility.
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/): platform conventions, hierarchy, interaction, and adaptable experiences.
- [The aesthetic-usability effect](https://www.nngroup.com/articles/aesthetic-usability-effect/): attractive products are often perceived as easier to use, without aesthetics replacing usability.
- [AI-generated UI accessibility research](https://dl.acm.org/doi/10.1145/3715336.3735691): basic compliance can coexist with homogenized design patterns and weak specialization.

Verify current platform guidance and accessibility standards when exact requirements matter.
