---
name: git-checkpoint-push
description: 'Perform only explicit Git actions such as stage, commit, checkpoint, push, PR handoff, or draft a message from the real current diff. Use when the user clearly requests one of those actions. Do not trigger for merely mentioning git, status, diff, branch, or repository, for read-only Git questions, implementation, or ordinary review; never infer an action.'
---
# Git Checkpoint Push

## Invocation contract

Trigger for an explicit request to inspect and perform any subset of stage, commit, checkpoint, push, PR handoff, or to draft a Conventional Commit message from the real current diff. A real-diff message request is `message-only`: inspect repository state and return a message without staging, committing, pushing, or otherwise changing Git state.

Do not trigger for fictional features, generic commit-message examples, read-only status/diff/log questions, ordinary code review, or implementation work with no checkpoint request.

## Authorization boundary

Derive an ordered action set from the user's exact request. Execute only that set.

- `message-only`: read-only inspection and message output.
- `stage-only`: stage only authorized paths.
- `commit-only`: inspect, verify, stage relevant files, and commit locally; never push.
- `push-only`: push only the explicitly identified existing commit/branch after safety checks.
- Combined requests run only the named actions in order.

Never infer push permission from commit, checkpoint, save progress, a configured remote, or a successful hook. Never create, switch, or push a branch without explicit authorization.

## Preflight

Before any mutation inspect `git status --short`, current branch, remotes, upstream and divergence when applicable, and the actual relevant diff. Exclude unrelated changes and secrets. For message-only, base the message on the actual unstaged/staged diff and report when no coherent current diff exists.

If the branch is behind, history is conflicting, or the requested target is a protected default/release branch, stop before mutation or push. Report the blocker and suggest a descriptive branch name, but do not create or push it without authorization.

## Verification and execution

Run proportionate verification before committing. If verification fails, stop unless the user explicitly authorized a failing local checkpoint. A failed stage, pre-commit hook, commit, or any prerequisite ends the sequence; never continue to push.

Stage targeted paths and recheck staged content. Never use destructive Git commands, bypass hooks or signing, amend, force push, change repository rules, or include credentials unless explicitly authorized and safe.

PowerShell 5 does not support `&&`. Do not replace it with an unconditional semicolon chain for `add`, `commit`, and `push`. Run each command separately, inspect its exit status and resulting Git state, then proceed only after success.

## Commit messages

Use Conventional Commits:

```text
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

Choose natural language in this order:

1. Use the language explicitly requested for the commit message.
2. Otherwise match the primary language of the checkpoint request.
3. For mixed requests, use the language describing the change and commit intent, then the conversation language if still unclear.

Keep `type`, scope syntax, `!`, and `BREAKING CHANGE` standard and untranslated. Preserve identifiers and issue references exactly. Use an imperative, accurate subject under 72 characters. Include body or footer only when evidence requires context, verification, issue references, or breaking-change details.

## Push safety

Push only when explicitly authorized, from the authorized existing branch to the intended remote. Never force push, bypass protections, or claim success without command evidence. If an upstream is absent, setting one or pushing a new branch requires explicit authorization.

## Report

Report actions actually performed, commit hash and exact message when created, branch, verification, push result when authorized, blockers, and remaining changes. In message-only mode, label the result read-only and report that no Git state changed.
