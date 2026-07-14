# Agent Skills

Small agent skills I use to keep repeated workflows consistent.

## Skills

| Skill | Purpose |
| --- | --- |
| `build-user-facing-ui` | Build polished, usable, context-appropriate user interfaces with complete states and rendered verification. |
| `english-spec-first` | Normalize rough or multilingual requests into a compact English specification before execution. |
| `freelance-order-triage` | Judge freelance coding orders, scope risks, quote posture, revisions, and acceptance before implementation. |
| `git-checkpoint-push` | Create clean git checkpoint commits and push completed work to a remote. |
| `high-constraint-coding` | Keep coding tasks disciplined: small diffs, clear assumptions, and practical verification. |
| `no-code-comments` | Keep generated and edited code free of comments by default. |
| `powershell-safe-commands` | Avoid Windows PowerShell quoting, interpolation, and nested shell command failures. |
| `vibecoding-domain-scout` | Research unfamiliar domains, then map workflows, constraints, MVP scope, risks, and build-ready briefs. |
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

Only `SKILL.md` is required. Other folders are included when the skill needs extra references, helper scripts, evaluation files, or agent-specific configuration.

The `agents/` directory contains per-platform YAML files (`claude.yaml`, `openai.yaml`) with display names, short descriptions, default prompts, and invocation policy. These are non-standard extensions on top of the [Agent Skills open standard](https://agentskills.io).

## Install

Agent Skills is an open standard supported by Cursor, Claude Code, OpenAI Codex CLI, and other compatible agents. Skills are discovered from these directories:

| Path | Scope |
| --- | --- |
| `.agents/skills/` | Project-level |
| `.cursor/skills/` | Project-level (Cursor) |
| `.claude/skills/` | Project-level (Claude Code) |
| `.codex/skills/` | Project-level (Codex CLI) |
| `~/.agents/skills/` | User-level (global) |
| `~/.cursor/skills/` | User-level (Cursor) |
| `~/.claude/skills/` | User-level (Claude Code) |
| `~/.codex/skills/` | User-level (Codex CLI) |

Copy a skill folder into whichever directory matches your agent:

```powershell
# Codex CLI
Copy-Item -Recurse .\skills\high-constraint-coding $env:USERPROFILE\.codex\skills\

# Claude Code
Copy-Item -Recurse .\skills\high-constraint-coding $env:USERPROFILE\.claude\skills\

# Cursor (user-level)
Copy-Item -Recurse .\skills\high-constraint-coding $env:USERPROFILE\.cursor\skills\

# Any compatible agent (generic path)
Copy-Item -Recurse .\skills\high-constraint-coding $env:USERPROFILE\.agents\skills\
```

Copy all skills at once:

```powershell
Copy-Item -Recurse .\skills\* $env:USERPROFILE\.agents\skills\
```

On macOS / Linux, replace `$env:USERPROFILE` with `$HOME` and use `cp -r`.

## Notes

These skills are personal workflow helpers. They are intentionally plain and focused on repeatable behavior rather than presentation.

All current skills are platform-independent unless a skill states otherwise.

## License

Copyright (c) 2026 Ninthless. All rights reserved.

These skills are proprietary personal workflow materials. They may not be copied, modified, redistributed, republished, sublicensed, or used to create derivative works without prior written permission.
