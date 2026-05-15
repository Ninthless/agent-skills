param(
	[Parameter(Mandatory = $true)]
	[string] $OldPath,
	[Parameter(Mandatory = $true)]
	[string] $NewPath,
	[string] $StateDb,
	[switch] $Apply,
	[switch] $CreateJunction
)

$ErrorActionPreference = "Stop"

function Normalize-ProjectPath([string] $PathValue) {
	return [System.IO.Path]::GetFullPath($PathValue).TrimEnd('\', '/')
}

$oldFullPath = Normalize-ProjectPath $OldPath
$newFullPath = Normalize-ProjectPath $NewPath

if (-not (Test-Path -LiteralPath $newFullPath -PathType Container)) {
	throw "NewPath does not exist or is not a directory: $newFullPath"
}

if (-not $StateDb) {
	$codexDir = Join-Path $env:USERPROFILE ".codex"
	$stateDbItem = Get-ChildItem -LiteralPath $codexDir -Filter "state_*.sqlite" -File |
		Sort-Object LastWriteTime -Descending |
		Select-Object -First 1
	if (-not $stateDbItem) {
		throw "No state_*.sqlite found in $codexDir"
	}
	$StateDb = $stateDbItem.FullName
}

if (-not (Test-Path -LiteralPath $StateDb -PathType Leaf)) {
	throw "StateDb does not exist: $StateDb"
}

$python = @'
import argparse
import json
import sqlite3
import time
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--db", required=True)
parser.add_argument("--old", required=True)
parser.add_argument("--new", required=True)
parser.add_argument("--apply", action="store_true")
args = parser.parse_args()

db = Path(args.db)
backup_path = None

con = sqlite3.connect(db)
con.row_factory = sqlite3.Row
try:
    old_rows = [dict(row) for row in con.execute(
        "select id,title,archived,updated_at,cwd from threads where cwd = ? order by updated_at desc",
        (args.old,),
    )]
    new_count_before = con.execute(
        "select count(*) from threads where cwd = ?",
        (args.new,),
    ).fetchone()[0]

    if args.apply and old_rows:
        backup_dir = db.parent / "backups_state" / "manual-cwd-remap"
        backup_dir.mkdir(parents=True, exist_ok=True)
        backup_path = backup_dir / f"{db.stem}_before_cwd_remap_{time.strftime('%Y%m%dT%H%M%S')}.sqlite"
        backup = sqlite3.connect(backup_path)
        try:
            con.backup(backup)
        finally:
            backup.close()
        con.execute("update threads set cwd = ? where cwd = ?", (args.new, args.old))
        con.commit()

    old_count_after = con.execute(
        "select count(*) from threads where cwd = ?",
        (args.old,),
    ).fetchone()[0]
    new_count_after = con.execute(
        "select count(*) from threads where cwd = ?",
        (args.new,),
    ).fetchone()[0]

    print(json.dumps({
        "database": str(db),
        "apply": args.apply,
        "backup": str(backup_path) if backup_path else None,
        "old_count_before": len(old_rows),
        "new_count_before": new_count_before,
        "old_count_after": old_count_after,
        "new_count_after": new_count_after,
        "old_rows": old_rows,
    }, ensure_ascii=False, indent=2))
finally:
    con.close()
'@

$tempScript = Join-Path ([System.IO.Path]::GetTempPath()) ("codex-cwd-remap-" + [System.Guid]::NewGuid().ToString("N") + ".py")
try {
	Set-Content -LiteralPath $tempScript -Value $python -Encoding UTF8
	$pythonArgs = @($tempScript, "--db", $StateDb, "--old", $oldFullPath, "--new", $newFullPath)
	if ($Apply) {
		$pythonArgs += "--apply"
	}
	python @pythonArgs
}
finally {
	if (Test-Path -LiteralPath $tempScript) {
		Remove-Item -LiteralPath $tempScript -Force
	}
}

if ($CreateJunction) {
	if (-not $Apply) {
		throw "-CreateJunction requires -Apply"
	}
	if (Test-Path -LiteralPath $oldFullPath) {
		$item = Get-Item -LiteralPath $oldFullPath -Force
		if (-not (($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -eq [System.IO.FileAttributes]::ReparsePoint)) {
			throw "OldPath already exists and is not a reparse point: $oldFullPath"
		}
		Write-Output "OldPath already exists as a reparse point: $oldFullPath"
	}
	else {
		New-Item -ItemType Junction -Path $oldFullPath -Target $newFullPath | Select-Object FullName,Target,LinkType
	}
}
