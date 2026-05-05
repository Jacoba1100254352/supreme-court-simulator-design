#!/usr/bin/env python3
"""Create a clean replication archive for journal review or deposit."""

from __future__ import annotations

import hashlib
import json
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
ARCHIVE = DIST / "constitutional-review-replication.zip"
MANIFEST = DIST / "replication-package-manifest.json"

INCLUDE_PATHS = [
    "AGENTS.md",
    "CITATION.cff",
    "Makefile",
    "README.md",
    "REPLICATION.md",
    "data",
    "docs",
    "paper/README.md",
    "paper/abstract-variants.md",
    "paper/main.tex",
    "paper/main.pdf",
    "paper/title-page.tex",
    "paper/references.bib",
    "paper/source-audit.csv",
    "paper/figures",
    "paper/tables",
    "paper/figure-exports",
    "paper/scripts",
    "reports",
    "src",
    "tools",
]

EXCLUDED_PARTS = {
    ".git",
    ".idea",
    "dist",
    "out",
    "build",
    "__pycache__",
}


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def should_skip(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    return any(part in EXCLUDED_PARTS for part in relative.parts)


def iter_files() -> list[Path]:
    files: set[Path] = set()
    for include in INCLUDE_PATHS:
        path = ROOT / include
        if not path.exists():
            raise SystemExit(f"Replication package input is missing: {include}")
        if path.is_file():
            if not should_skip(path):
                files.add(path)
            continue
        for child in path.rglob("*"):
            if child.is_file() and not should_skip(child):
                files.add(child)
    return sorted(files, key=lambda item: item.relative_to(ROOT).as_posix())


def write_zip(files: list[Path], manifest: dict[str, object]) -> None:
    fixed_time = (2026, 5, 1, 0, 0, 0)
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            relative = path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(relative, fixed_time)
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, path.read_bytes())
        info = zipfile.ZipInfo("replication-package-manifest.json", fixed_time)
        info.compress_type = zipfile.ZIP_DEFLATED
        archive.writestr(info, json.dumps(manifest, indent=2, sort_keys=True) + "\n")


def main() -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    files = iter_files()
    entries = [
        {
            "path": path.relative_to(ROOT).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in files
    ]
    manifest: dict[str, object] = {
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "gitCommit": git_commit(),
        "archive": ARCHIVE.name,
        "fileCount": len(entries),
        "files": entries,
        "notes": [
            "Run make test and make paper before packaging.",
            "The archive includes normalized calibration inputs, generated reports, paper source, generated figure/table fragments, standalone figure exports, Java source, tests, and replication documentation.",
            "Raw third-party source archives are intentionally not included; normalized calibration rows and provenance notes are included under data/calibration.",
        ],
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    write_zip(files, manifest)
    print(f"Wrote {ARCHIVE.relative_to(ROOT)}")
    print(f"Wrote {MANIFEST.relative_to(ROOT)}")
    print(f"Packaged {len(entries)} files")


if __name__ == "__main__":
    main()
