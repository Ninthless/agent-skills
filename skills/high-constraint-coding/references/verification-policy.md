# Verification Policy

Read this when selecting checks for risky or shared changes.

Match evidence to the changed contract. Every code change requires the most relevant available verification. Prefer a failing-before and passing-after targeted test when it can be produced without distorting the task. For a shared seam, add or run an adjacent consumer check. For migrations, verify forward behavior, compatibility assumptions, rollback or recovery expectations, and representative data. For concurrency, verify ordering, ownership, cancellation, retry, and duplicate behavior relevant to the change.

For web page, frontend, CSS, layout, component, and interaction changes, first check whether a relevant dev server is already running and reuse it when healthy. Start the project-native server when needed and permitted. When browser tools are available, navigate to the actual changed page, exercise each affected interaction, test relevant desktop and mobile viewports, and inspect the console. Inspect relevant network requests and responses for data loading, API calls, submissions, navigation, uploads, or other request-driven behavior. Use screenshots, DOM state, or accessibility evidence when they materially prove visual output, responsive layout, semantics, or state transitions.

Browser verification is a loop, not a one-time observation. Fix only defects introduced by the current change or defects whose repair is necessary to complete the user's explicit request, then rerun the affected browser flow and related checks until they pass or a concrete blocker prevents completion. Report pre-existing or adjacent defects without fixing them unless the user separately authorizes that work. If the server, browser, credentials, fixtures, or route is unavailable, run the strongest available build, test, type, lint, and static checks instead. Report the blocker and each browser-visible behavior that remains unverified.

Static checks prove structure, not runtime behavior. Manual reproduction is valid when automation is unavailable, but record exact inputs and observed results. Never convert an unavailable check into a claim that the behavior is safe.

Report commands or checks run, their outcome, and remaining uncertainty. A failed check is not a completed verification result when the defect is inside the authorized repair boundary: repair and rerun unless a concrete blocker or an unknown root cause requires a different primary skill. Report failures caused by pre-existing or adjacent defects without repairing them unless separately authorized.
