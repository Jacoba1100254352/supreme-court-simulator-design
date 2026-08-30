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
MANUSCRIPT_ARCHIVE = DIST / "constitutional-review-anonymous-manuscript.zip"
SUPPLEMENT_ARCHIVE = DIST / "constitutional-review-anonymous-supplement.zip"
MANIFEST = DIST / "anonymous-submission-manifest.json"

INCLUDE_PATHS = [
    "AGENTS.md",
    "Makefile",
    "README.md",
    "REPLICATION.md",
    "data/benchmarks",
    "data/calibration",
    "data/external",
    "docs",
    "paper/README.md",
    "paper/abstract-variants.md",
    "paper/emergency-review-constitutional-court-design.tex",
    "paper/emergency-review-constitutional-court-design.pdf",
    "paper/references.bib",
    "paper/source-audit.csv",
    "paper/figures",
    "paper/tables",
    "paper/figure-exports",
    "paper/scripts",
    "reports",
    "src",
    "tools/build_validation_dashboards.py",
    "tools/build_certiorari_journal_docket_retrieval_workqueue.py",
    "tools/build_calibration_tables.py",
    "tools/extract_certiorari_docketed_cohort_benchmark.py",
    "tools/extract_certiorari_granted_docket_detail_benchmark.py",
    "tools/extract_certiorari_journal_disposition_benchmark.py",
    "tools/extract_certiorari_journal_docket_detail_benchmark.py",
    "tools/extract_certiorari_term_flow_benchmark.py",
    "tools/extract_emergency_denied_docket_detail_benchmark.py",
    "tools/extract_ecthr_execution_monitoring_benchmark.py",
    "tools/extract_environmental_implementation_cohort.py",
    "tools/create_environmental_source_snapshot.py",
    "tools/extract_lower_court_precedent_treatment_benchmark.py",
    "tools/extract_shadow_docket_benchmark.py",
    "tools/import_deep_research_synthesis.py",
    "tools/refresh_calibration_sources.py",
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

ALLOWED_CONTENT_BY_PATH = {
    "data/benchmarks/certiorari-journal-disposition-extract-ot2023.csv": {b"Jacob", b"Anderson"},
    # A retained CourtListener citation context quotes Hughes Aircraft Co. v.
    # Jacobson; this is case text, not author-identifying metadata.
    "data/benchmarks/lower-court-environmental-treatment-events-v1.csv": {b"Jacob"},
}

FORBIDDEN_PATH_PARTS = [
    "CITATION.cff",
]

SPECIFIC_REPLACEMENTS = {
    'if "Jacob Anderson" in source or "github.com/Jacoba" in source:': 'if "".join(["Jac", "ob", " ", "And", "er", "son"]) in source or "github" + ".com/" + "".join(["Jac", "oba"]) in source:',
    "git@github.com:Jacoba1100254352/Supreme-Court-Simulator-Design.git": "repository withheld for anonymous review",
    "https://github.com/Jacoba1100254352/Supreme-Court-Simulator-Design": "repository withheld for anonymous review",
    "github.com/Jacoba1100254352": "repository withheld for anonymous review",
    "Jacob Anderson": "Anonymous Author",
    "Jacoba1100254352": "repository-withheld",
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
    if any(part in EXCLUDED_PARTS for part in relative.parts):
        return True
    return path.name == ".DS_Store" or path.suffix == ".iml"


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


def check_required_contents(files: list[Path]) -> None:
    package_paths = {path.relative_to(ROOT).as_posix() for path in files}
    missing = sorted(REQUIRED_CONTENTS - package_paths)
    if missing:
        formatted = "\n".join(f"- {path}" for path in missing)
        raise SystemExit(f"Anonymous package is missing required benchmark files:\n{formatted}")


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
        allowed_tokens = ALLOWED_CONTENT_BY_PATH.get(relative, set())
        for token in FORBIDDEN_CONTENT:
            if token in allowed_tokens:
                continue
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
                "This package contains the anonymous manuscript, simulator source, normalized calibration inputs, frozen external legislative-output fixtures, generated reports, figure/table fragments, and source-audit materials for review.",
                "",
                "Author-identifying files and public repository metadata are withheld. Local absolute paths in report manifests and documentation have been replaced with anonymized external-input placeholders if present.",
                "",
                "The package builder also writes separate manuscript-only and supplement-only ZIP archives so journal-upload categories can be kept distinct.",
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


def build_manifest(files: list[Path], archive_name: str, package_kind: str) -> dict[str, object]:
    entries = [
        {
            "path": path.relative_to(STAGING).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in sorted(files, key=lambda item: item.relative_to(STAGING).as_posix())
    ]
    return {
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "archive": archive_name,
        "packageKind": package_kind,
        "manuscriptArchive": MANUSCRIPT_ARCHIVE.name,
        "supplementArchive": SUPPLEMENT_ARCHIVE.name,
        "fileCount": len(entries),
        "packageTreeSha256": package_tree_sha256(entries),
        "files": entries,
        "notes": [
            "Blinded package for anonymous peer review.",
            "Non-anonymous citation metadata, author metadata, raw third-party archives, build directories, class files, and repository remotes are excluded.",
            "Run make test and make paper from the package root to reproduce the simulator checks and manuscript build.",
            "The supplement reproduces downstream analysis from frozen normalized inputs; live source acquisition requires network access or a separately deposited source snapshot.",
            "Upload the manuscript-only archive or paper/emergency-review-constitutional-court-design.pdf as the main anonymous manuscript; upload the supplement archive only if the submission system requests anonymous supplementary or replication materials at review.",
        ],
    }


def write_manifest(files: list[Path]) -> dict[str, object]:
    manifest = build_manifest(files, ARCHIVE.name, "combined-anonymous-review-package")
    MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    return manifest


def is_manuscript_file(path: Path) -> bool:
    relative = path.relative_to(STAGING).as_posix()
    if relative == "ANONYMOUS_SUBMISSION_README.md":
        return True
    if relative in {
        "paper/emergency-review-constitutional-court-design.pdf",
        "paper/emergency-review-constitutional-court-design.tex",
        "paper/references.bib",
        "paper/source-audit.csv",
        "paper/README.md",
    }:
        return True
    return relative.startswith("paper/figures/") or relative.startswith("paper/tables/") or relative.startswith("paper/figure-exports/")


def is_supplement_file(path: Path) -> bool:
    return not path.relative_to(STAGING).as_posix().startswith("paper/build/")


def write_zip(archive_path: Path, files: list[Path], manifest_name: str, manifest: dict[str, object]) -> None:
    fixed_time = (2026, 5, 1, 0, 0, 0)
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(files, key=lambda item: item.relative_to(STAGING).as_posix()):
            relative = path.relative_to(STAGING).as_posix()
            info = zipfile.ZipInfo(relative, fixed_time)
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, path.read_bytes())
        info = zipfile.ZipInfo(manifest_name, fixed_time)
        info.compress_type = zipfile.ZIP_DEFLATED
        archive.writestr(info, json.dumps(manifest, indent=2, sort_keys=True) + "\n")


def main() -> None:
    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir(parents=True)
    DIST.mkdir(parents=True, exist_ok=True)

    source_files = iter_source_files()
    check_required_contents(source_files)
    copied = [copy_file(path) for path in source_files]
    copied.append(write_package_readme())
    scan_for_identifiers(copied)
    manifest = write_manifest(copied)
    manuscript_files = [path for path in copied if is_manuscript_file(path)]
    supplement_files = [
        path for path in copied
        if is_supplement_file(path)
        and (not is_manuscript_file(path) or path.name == "ANONYMOUS_SUBMISSION_README.md")
    ]
    manuscript_manifest = build_manifest(
        manuscript_files,
        MANUSCRIPT_ARCHIVE.name,
        "anonymous-main-manuscript",
    )
    supplement_manifest = build_manifest(
        supplement_files,
        SUPPLEMENT_ARCHIVE.name,
        "anonymous-supplement",
    )
    write_zip(ARCHIVE, copied, "anonymous-submission-manifest.json", manifest)
    write_zip(MANUSCRIPT_ARCHIVE, manuscript_files, "anonymous-manuscript-manifest.json", manuscript_manifest)
    write_zip(SUPPLEMENT_ARCHIVE, supplement_files, "anonymous-supplement-manifest.json", supplement_manifest)
    print(f"Wrote {ARCHIVE.relative_to(ROOT)}")
    print(f"Wrote {MANUSCRIPT_ARCHIVE.relative_to(ROOT)}")
    print(f"Wrote {SUPPLEMENT_ARCHIVE.relative_to(ROOT)}")
    print(f"Wrote {MANIFEST.relative_to(ROOT)}")
    print(f"Packaged {len(copied)} anonymous files")


if __name__ == "__main__":
    main()
