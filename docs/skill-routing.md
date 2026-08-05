# Skill Routing

This repository adds a repository-local routing extension to the open Agent Skills format. `SKILL.md` remains the portable skill definition. `skills-manifest.json` records local routing metadata and does not replace platform discovery.

## Primary ownership

Route by the requested final artifact, not by incidental words. One primary skill owns the result. Requirement contracts belong to `requirement-analysis`; root-cause reports to `bug-diagnosis`; current technical evidence and solution decisions to `technical-solution-research`; industry workflow research to `vibecoding-domain-scout`; source changes and code reviews to `high-constraint-coding`; API contracts to `write-api-docs`; commercial engagement decisions to `freelance-order-triage`; explicit Git checkpoints to `git-checkpoint-push`.

A request may use zero skills when it is a simple fact, ordinary conversation, status check, or clear task outside every skill boundary. A keyword alone never forces routing. Mentioning Git, PowerShell, an API, a bug, English, or a framework is incidental unless the requested result matches that skill.

## Companions

`no-code-comments` may accompany work that writes code-like artifacts when the user or repository requires comment-free output. `powershell-safe-commands` may accompany an action containing real PowerShell parsing, quoting, interpolation, path, wrapper, or encoding risk. Companions never replace the primary skill and do not expand authorization.

## Sequences and authorization

Use an ordered sequence only when outputs depend on each other. Unknown-root-cause diagnose-and-fix work runs `bug-diagnosis` before `high-constraint-coding`. Materially unclear implementation work may run `requirement-analysis` before coding. Domain evidence may precede requirement analysis; technical evidence may precede a decision contract.

Read-only analysis does not authorize edits. Implementation does not authorize a commit or push. A commit does not authorize a push. `git-checkpoint-push` runs only the explicitly requested Git action set. Research and diagnosis may recommend a bounded experiment, but they do not silently implement or mutate the project.
