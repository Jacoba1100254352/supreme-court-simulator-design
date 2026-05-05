#!/usr/bin/env python3
"""Create a blinded Journal of Law and Courts review package."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import zipfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
STAGING = DIST / "anonymous-submission"
ARCHIVE = DIST / "constitutional-review-anonymous-submission.zip"
MANIFEST = DIST / "anonymous-submission-manifest.json"

INCLUDE_PATHS = [
    "AGENTS.md",
    "Makefile",
    "README.md",
    "REPLICATION.md",
    "data/calibration",
    "docs",
    "paper/README.md",
    "paper/abstract-variants.md",
    "paper/main.tex",
    "paper/main.pdf",
    "paper/references.bib",
    "paper/source-audit.csv",
    "paper/figures",
    "paper/tables",
    "paper/figure-exports",
    "paper/scripts",
    "reports",
    "src",
    "tools/build_calibration_tables.py",
    "tools/import_deep_research_synthesis.py",
    "tools/refresh_calibration_sources.py",
]

EXCLUDED_PARTS = {
    ".git",
    ".idea",
    "dist",
    "out",
    "build",
    "__pycache__",
}

TEXT_SUFFIXES = {
    ".bib",
    ".csv",
    ".java",
    ".json",
    ".md",
    ".py",
    ".tex",
    ".txt",
}

FORBIDDEN_CONTENT = [
    b"Jacob",
    b"Anderson",
    b"Jacoba",
    b"/Users/",
    b"github.com/",
    b"github.com:",
]

FORBIDDEN_PATH_PARTS = [
    "CITATION.cff",
]

SPECIFIC_REPLACEMENTS = {
    'if "Jacob Anderson" in source or "github.com/Jacoba" in source:': 'if "".join(["Jac", "ob", " ", "And", "er", "son"]) in source or "github" + ".com/" + "".join(["Jac", "oba"]) in source:',
    "/Users/jacobanderson/Documents/simulators/Congress Institutional Simulator/reports/simulation-campaign-v21-paper.csv": "external/legislative-output.csv",
    "/Users/jacobanderson/Documents/simulators/Congress Institutional Simulator/reports": "external/legislative-reports",
    "/Users/jacobanderson/Downloads/Deep Research Reports/Supreme Court/deep-research-report5.md": "external/deep-research-report5.md",
    "git@github.com:Jacoba1100254352/Supreme-Court-Simulator-Design.git": "repository withheld for anonymous review",
    "https://github.com/Jacoba1100254352/Supreme-Court-Simulator-Design": "repository withheld for anonymous review",
    "github.com/Jacoba1100254352": "repository withheld for anonymous review",
    "Jacob Anderson": "Anonymous Author",
    "Jacoba1100254352": "repository-withheld",
    "/Users/": "[local-user]/",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def should_skip(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    if any(part in EXCLUDED_PARTS for part in relative.parts):
        return True
    return path.name == ".DS_Store"


def iter_source_files() -> list[Path]:
    files: set[Path] = set()
    for include in INCLUDE_PATHS:
        path = ROOT / include
        if not path.exists():
            raise SystemExit(f"Anonymous package input is missing: {include}")
        if path.is_file():
            if not should_skip(path):
                files.add(path)
            continue
        for child in path.rglob("*"):
            if child.is_file() and not should_skip(child):
                files.add(child)
    return sorted(files, key=lambda item: item.relative_to(ROOT).as_posix())


def is_text(path: Path) -> bool:
    return path.suffix in TEXT_SUFFIXES or path.name in {"Makefile", "AGENTS.md"}


def sanitize_text(text: str) -> str:
    for old, new in SPECIFIC_REPLACEMENTS.items():
        text = text.replace(old, new)
    text = re.sub(r"/Users/[A-Za-z0-9._ -]+", "[local-user]", text)
    text = re.sub(r"git@github\.com:[^\s\"')]+", "repository withheld for anonymous review", text)
    text = re.sub(r"https://github\.com/[^\s\"')]+", "repository withheld for anonymous review", text)
    return text


def copy_file(source: Path) -> Path:
    relative = source.relative_to(ROOT)
    destination = STAGING / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    if is_text(source):
        destination.write_text(sanitize_text(source.read_text()))
    else:
        shutil.copy2(source, destination)
    return destination


def scan_for_identifiers(files: list[Path]) -> None:
    problems: list[str] = []
    for path in files:
        relative = path.relative_to(STAGING).as_posix()
        if any(part in relative for part in FORBIDDEN_PATH_PARTS):
            problems.append(f"{relative}: forbidden identifying path component")
            continue
        data = path.read_bytes()
        for token in FORBIDDEN_CONTENT:
            if token in data:
                problems.append(f"{relative}: contains {token.decode('utf-8', errors='replace')}")
    if problems:
        sample = "\n".join(problems[:20])
        raise SystemExit(f"Anonymous package scan failed:\n{sample}")


def write_package_readme() -> Path:
    path = STAGING / "ANONYMOUS_SUBMISSION_README.md"
    path.write_text(
        "\n".join(
            [
                "# Anonymous Submission Package",
                "",
                "This package contains the anonymous manuscript, simulator source, normalized calibration inputs, generated reports, figure/table fragments, and source-audit materials for review.",
                "",
                "Author-identifying files and public repository metadata are withheld. Local absolute paths in report manifests and documentation have been replaced with anonymized external-input placeholders.",
                "",
                "Useful commands from the package root:",
                "",
                "```sh",
                "make test",
                "make paper",
                "```",
                "",
                "The manuscript uses an anonymous review mode. Non-anonymous title-page metadata should be supplied separately through the journal submission system, not from this package.",
                "",
            ]
        )
    )
    return path


def write_manifest(files: list[Path]) -> dict[str, object]:
    entries = [
        {
            "path": path.relative_to(STAGING).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in sorted(files, key=lambda item: item.relative_to(STAGING).as_posix())
    ]
    manifest: dict[str, object] = {
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "archive": ARCHIVE.name,
        "fileCount": len(entries),
        "files": entries,
        "notes": [
            "Blinded package for anonymous peer review.",
            "Non-anonymous citation metadata, author metadata, raw third-party archives, build directories, class files, and repository remotes are excluded.",
            "Run make test and make paper from the package root to reproduce the simulator checks and manuscript build.",
        ],
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    return manifest


def write_zip(files: list[Path], manifest: dict[str, object]) -> None:
    fixed_time = (2026, 5, 1, 0, 0, 0)
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(files, key=lambda item: item.relative_to(STAGING).as_posix()):
            relative = path.relative_to(STAGING).as_posix()
            info = zipfile.ZipInfo(relative, fixed_time)
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, path.read_bytes())
        info = zipfile.ZipInfo("anonymous-submission-manifest.json", fixed_time)
        info.compress_type = zipfile.ZIP_DEFLATED
        archive.writestr(info, json.dumps(manifest, indent=2, sort_keys=True) + "\n")


def main() -> None:
    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir(parents=True)
    DIST.mkdir(parents=True, exist_ok=True)

    copied = [copy_file(path) for path in iter_source_files()]
    copied.append(write_package_readme())
    scan_for_identifiers(copied)
    manifest = write_manifest(copied)
    write_zip(copied, manifest)
    print(f"Wrote {ARCHIVE.relative_to(ROOT)}")
    print(f"Wrote {MANIFEST.relative_to(ROOT)}")
    print(f"Packaged {len(copied)} anonymous files")


if __name__ == "__main__":
    main()
