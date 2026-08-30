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
    "paper/emergency-review-constitutional-court-design.tex",
    "paper/emergency-review-constitutional-court-design.pdf",
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

REQUIRED_CONTENTS = {
    "data/benchmarks/certiorari-docketed-cohort-ot2023.csv",
    "data/benchmarks/certiorari-docketed-cohort-ot2023-manifest.json",
    "data/benchmarks/certiorari-docketed-cohort-ot2024.csv",
    "data/benchmarks/certiorari-docketed-cohort-ot2024-manifest.json",
    "data/benchmarks/certiorari-journal-disposition-extract-ot2023.csv",
    "data/benchmarks/certiorari-journal-disposition-extract-ot2023-manifest.json",
    "data/benchmarks/certiorari-journal-docket-detail-ot2023.csv",
    "data/benchmarks/certiorari-journal-docket-detail-ot2023-manifest.json",
    "data/benchmarks/certiorari-granted-docket-detail-ot2023.csv",
    "data/benchmarks/certiorari-granted-docket-detail-ot2023-manifest.json",
    "data/benchmarks/certiorari-term-flow-extract-journal-ot2023.csv",
    "data/benchmarks/certiorari-term-flow-extract-journal-ot2023-manifest.json",
    "data/benchmarks/certiorari-term-flow-extract-journal-ot2024.csv",
    "data/benchmarks/certiorari-term-flow-extract-journal-ot2024-manifest.json",
    "data/benchmarks/ecthr-execution-monitoring-pending-leading-cases-v1.csv",
    "data/benchmarks/ecthr-execution-monitoring-pending-leading-cases-v1-manifest.json",
    "data/benchmarks/emergency-application-denied-linkage-coded-v1.csv",
    "data/benchmarks/emergency-application-denied-linkage-coded-v1-manifest.json",
    "data/benchmarks/emergency-application-denied-linkage-workqueue-v1.csv",
    "data/benchmarks/emergency-application-linkage-coded-v1.csv",
    "data/benchmarks/emergency-application-grant-linkage-workqueue-v1.csv",
    "data/benchmarks/emergency-application-order-extract-shadow-docket-v3-0.csv",
    "data/benchmarks/implementation-compliance-schema.csv",
    "data/benchmarks/implementation-compliance-template.csv",
    "data/benchmarks/environmental-implementation-cohort-v1-manifest.json",
    "data/benchmarks/environmental-directional-treatment-review-queue-v1.csv",
    "data/benchmarks/environmental-practical-implementation-events-v1.csv",
    "data/benchmarks/gurganus-2025-table-1-classifications-v1.csv",
    "data/benchmarks/lower-court-environmental-circuit-exposure-v1.csv",
    "data/benchmarks/lower-court-environmental-treatment-events-v1.csv",
    "data/benchmarks/lower-court-precedent-treatment-aggregate-v1.csv",
    "data/benchmarks/lower-court-precedent-treatment-aggregate-v1-manifest.json",
    "data/calibration/environmental-implementation-cohort-v1.csv",
    "data/calibration/lower-court-precedent-treatment-v1.csv",
    "data/calibration/scotus-certiorari-docketed-cohort-ot2023.csv",
    "data/calibration/scotus-certiorari-docketed-cohort-ot2024.csv",
    "reports/certiorari-docketed-cohort-journal-reconciliation-v1.csv",
    "reports/certiorari-docketed-cohort-journal-reconciliation-v1.md",
    "reports/certiorari-docketed-cohort-summary-v1.csv",
    "reports/certiorari-docketed-cohort-summary-v1.md",
    "reports/certiorari-docketed-cohort-summary-ot2024-v1.csv",
    "reports/certiorari-docketed-cohort-summary-ot2024-v1.md",
    "reports/certiorari-multi-term-benchmark-v1.csv",
    "reports/certiorari-multi-term-benchmark-v1.md",
    "reports/certiorari-cohort-closure-plan-v1.csv",
    "reports/certiorari-cohort-closure-plan-v1.md",
    "reports/certiorari-cohort-field-readiness-v1.csv",
    "reports/certiorari-cohort-field-readiness-v1.md",
    "reports/certiorari-granted-docket-detail-summary-v1.csv",
    "reports/certiorari-granted-docket-detail-summary-v1.md",
    "reports/certiorari-journal-disposition-summary-v1.csv",
    "reports/certiorari-journal-disposition-summary-v1.md",
    "reports/certiorari-journal-docket-detail-summary-v1.csv",
    "reports/certiorari-journal-docket-detail-summary-v1.md",
    "reports/certiorari-journal-docket-retrieval-workqueue-v1.csv",
    "reports/certiorari-journal-docket-retrieval-workqueue-v1.md",
    "reports/certiorari-term-flow-reconciliation-v1.md",
    "reports/emergency-application-field-readiness-v1.csv",
    "reports/emergency-application-field-readiness-v1.md",
    "reports/emergency-application-denied-linkage-coded-summary-v1.csv",
    "reports/emergency-application-denied-linkage-coded-summary-v1.md",
    "reports/emergency-application-denied-linkage-workqueue-v1.md",
    "reports/ecthr-execution-monitoring-summary-v1.csv",
    "reports/ecthr-execution-monitoring-summary-v1.md",
    "reports/emergency-application-linkage-coded-v1.md",
    "reports/emergency-application-grant-linkage-workqueue-v1.md",
    "reports/emergency-application-order-reconciliation-v1.md",
    "reports/implementation-compliance-closure-plan-v1.csv",
    "reports/implementation-compliance-closure-plan-v1.md",
    "reports/implementation-compliance-workqueue-v1.csv",
    "reports/implementation-compliance-workqueue-v1.md",
    "reports/environmental-implementation-cohort-summary-v1.csv",
    "reports/environmental-implementation-cohort-summary-v1.md",
    "reports/environmental-full-text-availability-audit-v1.csv",
    "reports/environmental-full-text-availability-audit-v1.md",
    "reports/external-methods-review-ai-v1.md",
    "reports/external-methods-review-response-v1.md",
    "reports/lower-court-precedent-treatment-summary-v1.csv",
    "reports/lower-court-precedent-treatment-summary-v1.md",
    "paper/tables/certiorari_multi_term.tex",
    "tools/build_certiorari_journal_docket_retrieval_workqueue.py",
    "tools/extract_certiorari_docketed_cohort_benchmark.py",
    "tools/extract_certiorari_journal_disposition_benchmark.py",
    "tools/extract_certiorari_journal_docket_detail_benchmark.py",
    "tools/extract_certiorari_granted_docket_detail_benchmark.py",
    "tools/extract_certiorari_term_flow_benchmark.py",
    "tools/extract_emergency_denied_docket_detail_benchmark.py",
    "tools/extract_ecthr_execution_monitoring_benchmark.py",
    "tools/extract_environmental_implementation_cohort.py",
    "tools/create_environmental_source_snapshot.py",
    "tools/extract_lower_court_precedent_treatment_benchmark.py",
    "tools/extract_shadow_docket_benchmark.py",
}

EXCLUDED_PARTS = {
    ".git",
    ".idea",
    "dist",
    "out",
    "build",
    "__pycache__",
}


def git_state() -> dict[str, object]:
    try:
        commit_result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        status_result = subprocess.run(
            ["git", "status", "--porcelain=v1", "--untracked-files=all"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if commit_result.returncode != 0 or status_result.returncode != 0:
            return {
                "gitAvailable": False,
                "gitCommit": "unknown",
                "gitDirty": None,
                "gitStatusEntryCount": 0,
                "gitStatusSha256": "",
            }
        status = status_result.stdout
        entries = [line for line in status.splitlines() if line.strip()]
        return {
            "gitAvailable": True,
            "gitCommit": commit_result.stdout.strip(),
            "gitDirty": bool(entries),
            "gitStatusEntryCount": len(entries),
            "gitStatusSha256": hashlib.sha256(status.encode("utf-8")).hexdigest(),
        }
    except (subprocess.CalledProcessError, FileNotFoundError):
        return {
            "gitAvailable": False,
            "gitCommit": "unknown",
            "gitDirty": None,
            "gitStatusEntryCount": 0,
            "gitStatusSha256": "",
        }


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def package_tree_sha256(entries: list[dict[str, object]]) -> str:
    payload = "".join(
        f"{entry['path']}\t{entry['bytes']}\t{entry['sha256']}\n"
        for entry in entries
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def should_skip(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    return (
        path.name == ".DS_Store"
        or path.suffix == ".iml"
        or relative.parts[:2] == ("data", "raw")
        or any(part in EXCLUDED_PARTS for part in relative.parts)
    )


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


def check_required_contents(files: list[Path]) -> None:
    package_paths = {path.relative_to(ROOT).as_posix() for path in files}
    missing = sorted(REQUIRED_CONTENTS - package_paths)
    if missing:
        formatted = "\n".join(f"- {path}" for path in missing)
        raise SystemExit(f"Replication package is missing required benchmark files:\n{formatted}")


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
    check_required_contents(files)
    entries = [
        {
            "path": path.relative_to(ROOT).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in files
    ]
    state = git_state()
    manifest: dict[str, object] = {
        "createdAt": datetime.now(timezone.utc).isoformat(),
        **state,
        "archive": ARCHIVE.name,
        "fileCount": len(entries),
        "packageTreeSha256": package_tree_sha256(entries),
        "analyticReproductionScope": (
            "Reproduces tests, generated dashboards, manuscript tables/figures, and "
            "paper checks from frozen normalized inputs."
        ),
        "sourceAcquisitionScope": (
            "Live source acquisition requires public network access or the optional "
            "environmental-implementation-source-snapshot.zip created by "
            "make environmental-source-snapshot."
        ),
        "files": entries,
        "notes": [
            "Run make test and make paper before packaging.",
            "The archive includes normalized calibration inputs, generated reports, paper source, generated figure/table fragments, standalone figure exports, Java source, tests, and replication documentation.",
            "This archive supports analytic reproduction from frozen normalized outputs; it does not by itself reproduce network source acquisition.",
            "Raw third-party source archives are intentionally not included. The environmental source-snapshot builder is included, and its optional archive is deposited separately when redistribution review permits.",
            "gitCommit identifies HEAD only. gitDirty, gitStatusEntryCount, gitStatusSha256, and packageTreeSha256 disclose the packaged working-tree state.",
        ],
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    write_zip(files, manifest)
    print(f"Wrote {ARCHIVE.relative_to(ROOT)}")
    print(f"Wrote {MANIFEST.relative_to(ROOT)}")
    print(f"Packaged {len(entries)} files")


if __name__ == "__main__":
    main()
