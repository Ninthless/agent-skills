# Evidence And Performance

Read this reference before making completion, usability, accessibility, performance, or user-validation claims. Use the bundled evidence validator for substantial interfaces when practical.

## Contents

- Evidence Levels
- Evidence Manifest
- Workflow Evidence
- Screenshot Evidence
- Accessibility Evidence
- Web Performance
- Native Performance
- User Evidence
- Honest Completion Claims
- Commands
- Sources

## Evidence Levels

Use the strongest practical evidence and name its limits.

1. Source evidence: code, types, tests, and static analysis
2. Runtime evidence: the real surface opened in the target runtime
3. Interaction evidence: a workflow completed with observable outcomes
4. Accessibility evidence: automated checks plus manual input, focus, zoom, and semantic checks
5. Performance evidence: measured values under declared conditions
6. User evidence: representative participants attempting defined tasks
7. Field evidence: production behavior at a declared percentile and population

Higher levels do not erase failures at lower levels. A favorable screenshot cannot compensate for a broken task, and a lab score cannot replace field behavior.

## Evidence Manifest

For a substantial surface, create a JSON evidence manifest. Start from the bundled template:

```powershell
python scripts/validate_ui_evidence.py --init ui-evidence.json
```

The manifest records:

- Surface, archetype, audience, task, scope, platforms, and required viewports
- Screenshots, states, console errors, and asset failures
- Workflow outcomes and recovery paths
- Accessibility gates and conditional features
- Trust-sensitive conditions
- Performance budgets, measurements, and measurement mode
- User-evidence status, results, and limitations
- A visual fingerprint used only for cross-project convergence checks

Store evidence with the product artifact when useful. Do not fabricate measurements to satisfy the schema.

## Workflow Evidence

- Record the primary task as a workflow with `kind` set to `primary` and a passed outcome.
- Record at least one empty, error, unavailable, permission, or recovery workflow for a substantial surface.
- Describe the visible outcome rather than only the input action.
- Keep destructive, purchase, subscription, consent, and cancellation workflows separate when they exist.
- Record the runtime, device, and platform elsewhere in the product's test artifact when the manifest alone is insufficient.

## Screenshot Evidence

- Capture each required viewport in a meaningful state.
- Include the primary state and one failure, empty, or recovery state for substantial work.
- Use paths that resolve from the manifest location.
- Keep screenshots free of private or secret data.
- Pair screenshots with interaction evidence; a static image does not prove behavior.
- Treat missing assets, console errors, clipped text, overlap, and unstable geometry as failures unless explicitly accepted.

## Accessibility Evidence

Record manual results for keyboard completion, visible and unobscured focus, non-color meaning, target size, and zoom or reflow. Record conditional results for dragging and authentication. Include the named automated tool and its critical-violation count in the surrounding test record if the schema does not capture the tool name.

An automated zero does not justify an unqualified accessibility claim.

## Web Performance

For public web experiences, use Core Web Vitals as default user-facing budgets unless the project defines stricter budgets:

- Largest Contentful Paint: at most 2500 milliseconds
- Interaction to Next Paint: at most 200 milliseconds
- Cumulative Layout Shift: at most 0.1

Judge field data at the 75th percentile separately for mobile and desktop. Lab measurement is useful during implementation but does not replace field measurement.

Record:

- Measurement mode such as `lab`, `field`, or `both`
- A contextual measurement for every declared mode, including environment, device or connection profile, browser or runtime, route or scenario, build, sample count, and the 75th percentile for field Core Web Vitals
- Observed LCP, INP, and CLS values when applicable
- Project budgets and any justified exceptions

Do not claim field performance from Lighthouse or a single local run.

## Native Performance

Do not invent one universal threshold for every native product. Declare product-specific budgets based on platform guidance and task requirements.

Consider:

- Cold and warm launch
- Time to first useful content
- Input response and frame pacing
- Scrolling, canvas, timeline, or viewport smoothness
- Memory, CPU, GPU, battery, package size, and network use
- Window resize and display scaling
- Offline, resume, background, and recovery behavior

Record the measurement name, mode, environment, tool, device, build type, dataset, scenario, sample count, unit, budget, and observed value. A development build on one machine is implementation evidence, not a population claim.

## User Evidence

User research is not required for every small change, but the absence of it must not be disguised.

When available, record:

- Participant count and relationship to the target population
- Task scenario and success criteria
- Primary-task success rate
- Median task time when efficiency matters
- Critical-error rate
- Observed failure patterns
- Accessibility needs represented
- Recruitment, sample, prototype, and environment limitations

Set user-evidence status to `not_run`, `internal`, `representative`, or `field`. When status is `not_run`, state limitations. When claiming representative validation, provide participants and results.

## Honest Completion Claims

Use evidence-bounded language:

- `Rendered at the required desktop and mobile viewports`
- `Primary workflow and one recovery path passed in Chromium`
- `No automated critical violations were reported by axe; screen-reader testing was not run`
- `Lab LCP was 1.8 seconds on the declared profile; field performance is unknown`
- `No representative-user study was run`

Avoid:

- `Fully accessible`
- `Users will find this intuitive`
- `Performance is excellent`
- `Pixel perfect`
- `Production ready`

unless the product has an explicit acceptance contract and matching evidence.

## Commands

Validate one manifest:

```powershell
python scripts/validate_ui_evidence.py ui-evidence.json
```

Compare unrelated product fingerprints:

```powershell
python scripts/compare_visual_fingerprints.py product-a.json product-b.json product-c.json
```

The fingerprint comparison is a convergence heuristic. It cannot judge beauty or replace screenshot inspection.

## Sources

- [Core Web Vitals](https://web.dev/articles/vitals)
- [ISO 9241-11 usability](https://www.iso.org/standard/63500.html)
- [W3C Selecting Accessibility Evaluation Tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/)
- [GOV.UK Design Principles](https://www.gov.uk/guidance/government-design-principles)
