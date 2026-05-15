# Agent Skills

Small agent skills I use to keep repeated workflows consistent.

## Skills

| Skill | Purpose |
| --- | --- |
| `codex-cwd-remap` | Repair Codex App conversations after a project folder is moved, renamed, deleted, or replaced. |
| `english-spec-first` | Normalize rough or multilingual requests into a compact English specification before execution. |
| `git-checkpoint-push` | Create clean git checkpoint commits and push completed work to a remote. |
| `high-constraint-coding` | Keep coding tasks disciplined: small diffs, clear assumptions, and practical verification. |
| `no-code-comments` | Keep generated and edited code free of comments by default. |
| `xposed-module-dev` | Build, review, and debug Android Xposed / LSPosed modules. |

## Layout

```txt
skills/
  <skill-name>/
    SKILL.md
    references/
    scripts/
    evals/
    agents/
```

Only `SKILL.md` is required. Other folders are included when the skill needs extra references, helper scripts, or evaluation files.

## Install

Copy a skill folder into your Codex skills directory:

```powershell
Copy-Item -Recurse .\skills\high-constraint-coding $env:USERPROFILE\.codex\skills\
```

Or copy all of them:

```powershell
Copy-Item -Recurse .\skills\* $env:USERPROFILE\.codex\skills\
```

## Notes

These skills are personal workflow helpers. They are intentionally plain and focused on repeatable behavior rather than presentation.
