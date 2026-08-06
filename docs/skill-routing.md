# Skill Routing

This repository adds a repository-local routing extension to the open Agent Skills format. `SKILL.md` remains the portable skill definition. `skills-manifest.json` records local routing metadata and does not replace platform discovery.

## Primary ownership

Route by the requested final artifact, not by incidental words. One primary skill owns the result. Requirement contracts belong to `requirement-analysis`; root-cause reports to `bug-diagnosis`; current technical evidence and solution decisions to `technical-solution-research`; industry workflow research to `vibecoding-domain-scout`; all actual source changes and code reviews in every programming language, including frontend, backend, web page, React/Vue component, CSS, layout, and interaction implementation, to `high-constraint-coding`, which enforces language- and ecosystem-native, maintainable, reviewable, verified engineering properties rather than an authorship claim; API contracts to `write-api-docs`; commercial engagement decisions to `freelance-order-triage`; explicit Git checkpoints to `git-checkpoint-push`.

Web implementation is complete only after the most relevant available checks pass. When browser tools and the page are available, `high-constraint-coding` checks or starts the dev server, navigates to the actual page, exercises affected interactions at relevant desktop and mobile viewports, inspects console and request behavior, and fixes then retests failures. When browser verification is blocked, it runs available build, test, type, lint, or static checks and reports the exact unverified browser behavior.

Routing evaluations use a closed-world contract. For each routed case, only the declared primary skill, every skill in `expected_sequence`, and declared `allowed_companions` are expected to trigger; every other final skill must return false. Later sequence owners remain required true but are not companions. `forbidden_skills` documents an explicit subset of the false set. Incidental keywords never let an undeclared skill claim the case.

A request may use zero skills when it is a simple fact, ordinary conversation, status check, or clear task outside every skill boundary. A keyword alone never forces routing. Mentioning Git, PowerShell, an API, a bug, English, or a framework is incidental unless the requested result matches that skill.

## Companions

`no-code-comments` may accompany work that writes code-like artifacts when the user or repository requires comment-free output. `powershell-safe-commands` may accompany an action containing real PowerShell parsing, quoting, interpolation, path, wrapper, or encoding risk. Companions never replace the primary skill and do not expand authorization.

## Sequences and authorization

Use an ordered sequence only when outputs depend on each other. Unknown-root-cause diagnose-and-fix work runs `bug-diagnosis` before `high-constraint-coding`. Materially unclear implementation work may run `requirement-analysis` before coding. Domain evidence may precede requirement analysis; technical evidence may precede a decision contract.

Read-only analysis does not authorize edits. Implementation does not authorize a commit or push. A commit does not authorize a push. `git-checkpoint-push` runs only the explicitly requested Git action set. Research and diagnosis may recommend a bounded experiment, but they do not silently implement or mutate the project.

Webpage requirements without implementation remain with `requirement-analysis`; framework or version decisions remain with `technical-solution-research`; unknown-root-cause UI defects begin with `bug-diagnosis`. Once actual web source changes are authorized, `high-constraint-coding` owns implementation and must close the loop with available dev-server and browser evidence, console and relevant network checks, responsive verification where affected, and fix/retest iterations. Browser or server unavailability must be reported as a blocker with alternative evidence, never treated as a pass.
