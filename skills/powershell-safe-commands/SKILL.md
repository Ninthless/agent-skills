---
name: powershell-safe-commands
description: 'Author or repair commands as a companion only when PowerShell parsing, quoting, interpolation, wrappers, path literals, or encoding can change meaning. Use for requests involving dollar-variable interpolation, pipeline variables, environment variables, here-strings, regex replacements, nested powershell -Command, quoted Windows paths, -EncodedCommand, or failures caused by those constructs. Do not become the primary owner or expand authorization; do not trigger merely because the host is Windows/PowerShell, for simple direct commands, conceptual explanations, non-PowerShell shells, or source changes with no PowerShell-specific risk.'
---
# PowerShell Safe Commands

## Trigger boundary

Use only when a command contains or has failed because of PowerShell-specific parsing, wrapping, interpolation, quoting, path-literal, regex replacement, or encoding risk. Windows, PowerShell, Cursor, or Codex context alone is insufficient.

## Safety ladder

Stop at the first safe option:

1. Use the host's dedicated edit, patch, file, process, or structured-data tool.
2. Execute the target program directly with argument boundaries preserved.
3. Use an existing project runtime or checked-in script.
4. Use a temporary script only as a last resort; place it in the system temporary directory by default and remove it after successful use.

Avoid extra `powershell -Command`, `pwsh -Command`, `cmd /c`, or shell-string layers. Do not retry fragile one-liners by adding random escaping. In PowerShell 5, `&&` is unavailable; run dependent commands separately and inspect success instead of using an unconditional semicolon chain.

Quote revision syntax such as `'@{u}'`. Use literal-path APIs for paths containing wildcard metacharacters. Keep environment values as quoted values rather than injecting unquoted paths into expressions. Move non-trivial `$`, `$_`, captures, nested quotes, or multiline edits out of inline commands.

## Encoded commands

Before showing or creating `-EncodedCommand`, inspect the decoded script and redact secrets. Never echo, print, log, embed in examples, or expose tokens, passwords, API keys, private keys, cookies, authorization headers, or connection strings. If safe redaction would change behavior, stop and ask for a secret-safe execution path. Show only a sanitized decoded script before execution.

## Recovery

Identify the token or layer that changed meaning, select the next safer rung, execute once, and run a minimal verification that proves the intended value reached the target program. Keep explanations brief.
