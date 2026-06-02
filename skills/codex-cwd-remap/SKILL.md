---
name: codex-cwd-remap
description: 'Use when Codex App or Codex CLI cannot open a thread because the working directory was moved, renamed, deleted, replaced, or shows "working directory missing", "cwd missing", 工作目录不存在, 项目路径变了, Codex 打不开旧会话. Repairs old path to new path remap, Codex SQLite state, threads.cwd records, and Windows junction fallback.'
---

# Codex CWD Remap

## Compatibility

Requires Windows and PowerShell. The bundled script uses PowerShell cmdlets and Windows junction points.

## Workflow

Use this skill only for local Codex state repair. The main target is `~/.codex/state_*.sqlite`, especially the `threads.cwd` column.

1. Confirm the old project path and the new project path.
2. Verify the new path exists.
3. Run the bundled script in dry-run mode first.
4. Apply the remap only after the dry run shows the expected rows.
5. If Codex App still says the old working directory is missing, create a junction from the old path to the new path.
6. Re-check exact old/new counts after the update.

## Script

Use `scripts/remap-codex-cwd.ps1`.

Dry run:

```powershell
& "$env:USERPROFILE\.codex\skills\codex-cwd-remap\scripts\remap-codex-cwd.ps1" `
  -OldPath "E:\Development\Projects\old-folder" `
  -NewPath "E:\Development\Projects\NewFolder"
```

Apply and create a junction:

```powershell
& "$env:USERPROFILE\.codex\skills\codex-cwd-remap\scripts\remap-codex-cwd.ps1" `
  -OldPath "E:\Development\Projects\old-folder" `
  -NewPath "E:\Development\Projects\NewFolder" `
  -Apply `
  -CreateJunction
```

## Safety Rules

- Do not edit `logs_*.sqlite` for cwd repair. It is historical telemetry and not needed for the App's current working directory check.
- Back up the SQLite database before applying changes. The bundled script does this with SQLite's backup API.
- Update only exact `threads.cwd` matches, not broad substring matches.
- Do not create a junction if the old path already exists as a real directory. Stop and inspect it.
- If Codex App rewrites the old cwd while open, close or restart the App, rerun the script, then reopen.
- Use a junction only as compatibility fallback for active conversations that still validate the original filesystem path.

## Validation

After applying, confirm:

```powershell
& "$env:USERPROFILE\.codex\skills\codex-cwd-remap\scripts\remap-codex-cwd.ps1" `
  -OldPath "E:\Development\Projects\old-folder" `
  -NewPath "E:\Development\Projects\NewFolder"
```

Expected result: old exact count is `0`, new exact count includes the remapped rows, and the old path exists if `-CreateJunction` was used.
