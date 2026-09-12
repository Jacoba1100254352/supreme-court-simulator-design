#!/usr/bin/env python3
"""Verify the delivered archive by rebuilding its extracted contents."""

from __future__ import annotations

import hashlib
import json
import stat
import subprocess
import tempfile
import zipfile
from pathlib import Path

from package_policy import validate_member_name


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_ARCHIVE_CONTENTS = {
    "paper/technical-supplement.tex",
    "paper/technical-supplement.pdf",
    "paper/tables/model_weights.tex",
    ".gitattributes",
    ".gitignore",
    "data/review/expert-legal-coding-v1/manifest.json",
    "data/review/expert-legal-coding-v1/reviewer-a-template.csv",
    "data/review/expert-legal-coding-v1/reviewer-b-template.csv",
    "docs/expert-legal-coding-protocol.md",
    "docs/evidence-acquisition-priorities.md",
    "reports/review-data-quality-v1.md",
    "tools/prepare_expert_review.py",
    "tools/review_coding_returns.py",
    "tools/package_policy.py",
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
    "data/benchmarks/emergency-application-grant-linkage-workqueue-v1.csv",
    "data/benchmarks/emergency-application-linkage-coded-v1.csv",
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
    "reports/emergency-application-denied-linkage-workqueue-v1.md",
    "reports/ecthr-execution-monitoring-summary-v1.csv",
    "reports/ecthr-execution-monitoring-summary-v1.md",
    "reports/emergency-application-field-readiness-v1.csv",
    "reports/emergency-application-field-readiness-v1.md",
    "reports/emergency-application-denied-linkage-coded-summary-v1.csv",
    "reports/emergency-application-denied-linkage-coded-summary-v1.md",
    "reports/emergency-application-grant-linkage-workqueue-v1.md",
    "reports/emergency-application-linkage-coded-v1.md",
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


def run(command: list[str], cwd: Path) -> None:
    print("Running " + " ".join(command))
    subprocess.run(command, cwd=cwd, check=True)


def package_tree_sha256(entries: list[dict[str, object]]) -> str:
    payload = "".join(
        f"{entry['path']}\t{entry['bytes']}\t{entry['sha256']}\n"
        for entry in entries
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def check_archive_contents(archive: Path, manifest_name: str = "replication-package-manifest.json", required_contents: set[str] | None = None) -> None:
    with zipfile.ZipFile(archive) as package:
        member_names = package.namelist()
        names = set(member_names)
        if len(names) != len(member_names):
            raise SystemExit("Replication archive contains duplicate member names")
        for info in package.infolist():
            validate_member_name(info.filename)
            if stat.S_ISLNK(info.external_attr >> 16):
                raise SystemExit(f"Replication archive contains a symbolic link: {info.filename}")
        if manifest_name not in names:
            raise SystemExit("Replication archive lacks its internal manifest")
        manifest = json.loads(package.read(manifest_name))
        entries = manifest.get("files", [])
        if not isinstance(entries, list):
            raise SystemExit("Replication manifest files field is malformed")
        if not all(isinstance(entry, dict) and isinstance(entry.get("path"), str) for entry in entries):
            raise SystemExit("Replication manifest entry is malformed")
        declared = [entry["path"] for entry in entries]
        if len(declared) != len(set(declared)):
            raise SystemExit("Replication manifest repeats a member")
        if set(declared) != names - {manifest_name}:
            raise SystemExit("Replication manifest does not cover exactly the archive members")
        if manifest.get("fileCount") != len(entries):
            raise SystemExit("Replication manifest file count does not reconcile")
        if manifest.get("packageTreeSha256") != package_tree_sha256(entries):
            raise SystemExit("Replication manifest package-tree hash does not reconcile")
        if manifest_name == "replication-package-manifest.json":
            if manifest.get("gitDirty") not in {True, False, None}:
                raise SystemExit("Replication manifest lacks a valid dirty-tree disclosure")
            if not isinstance(manifest.get("gitStatusEntryCount"), int):
                raise SystemExit("Replication manifest lacks git status entry count")
            if "frozen normalized inputs" not in manifest.get("analyticReproductionScope", ""):
                raise SystemExit("Replication manifest overstates analytic reproduction scope")
            if "network access" not in manifest.get("sourceAcquisitionScope", ""):
                raise SystemExit("Replication manifest omits source-acquisition boundary")
        for entry in entries:
            name = entry.get("path", "")
            if name not in names:
                raise SystemExit(f"Replication manifest member is missing: {name}")
            payload = package.read(name)
            if len(payload) != entry.get("bytes"):
                raise SystemExit(f"Replication manifest byte count changed: {name}")
            if hashlib.sha256(payload).hexdigest() != entry.get("sha256"):
                raise SystemExit(f"Replication manifest hash changed: {name}")
    required = REQUIRED_ARCHIVE_CONTENTS if required_contents is None else required_contents
    missing = sorted(required - names)
    if missing:
        formatted = "\n".join(f"- {path}" for path in missing)
        raise SystemExit(f"Replication archive is missing required benchmark files:\n{formatted}")
    forbidden = sorted(
        name
        for name in names
        if name.startswith("data/raw/")
        or Path(name).suffix in {".iml", ".pyc"}
        or Path(name).name == ".DS_Store"
        or "__pycache__" in Path(name).parts
    )
    if forbidden:
        formatted = "\n".join(f"- {path}" for path in forbidden)
        raise SystemExit(f"Replication archive contains local or generated metadata:\n{formatted}")


def check_split_archives(combined: Path, manuscript: Path, supplement: Path) -> None:
    """Prove the two upload ZIPs reconstruct the already tested combined tree."""
    merged = {}
    for archive, manifest_name in (
        (manuscript, "anonymous-manuscript-manifest.json"),
        (supplement, "anonymous-supplement-manifest.json"),
    ):
        check_archive_contents(archive, manifest_name, set())
        with zipfile.ZipFile(archive) as package:
            for name in package.namelist():
                if name == manifest_name:
                    continue
                payload = package.read(name)
                if name in merged and merged[name] != payload:
                    raise SystemExit(f"Split anonymous packages disagree: {name}")
                merged[name] = payload
    with zipfile.ZipFile(combined) as package:
        expected = {name: package.read(name) for name in package.namelist() if name != "anonymous-submission-manifest.json"}
    if merged != expected:
        raise SystemExit("Split anonymous packages do not reconstruct the combined archive")
    print("Split anonymous upload packages reconstruct the tested combined tree.")


def main() -> None:
    workspace_archive = ROOT / "dist" / "constitutional-review-replication.zip"
    if not workspace_archive.exists():
        raise SystemExit("Workspace replication archive is missing")
    check_archive_contents(workspace_archive)
    with tempfile.TemporaryDirectory(prefix="constitutional-review-replication-") as temp:
        checkout = Path(temp) / "repo"
        checkout.mkdir()
        with zipfile.ZipFile(workspace_archive) as package:
            package.extractall(checkout)
        # Compare deterministic analytic outputs, not PDF timestamps or run-time metadata.
        targets = sorted((checkout / "reports").glob("*.csv"))
        targets += sorted((checkout / "paper" / "tables").glob("*.tex"))
        targets += sorted((checkout / "paper" / "figures").glob("*.tex"))
        before = {path.relative_to(checkout): hashlib.sha256(path.read_bytes()).hexdigest() for path in targets}
        run(["make", "test", "campaign-v0", "campaign-v1", "campaign-v2", "diagnostics", "paper-strict-check", "replication-package"], checkout)
        changed = [str(path) for path, digest in before.items() if not (checkout / path).exists() or hashlib.sha256((checkout / path).read_bytes()).hexdigest() != digest]
        if changed:
            raise SystemExit("Extracted archive does not reproduce frozen analytic outputs: " + ", ".join(changed))
        archive = checkout / "dist" / "constitutional-review-replication.zip"
        manifest = checkout / "dist" / "replication-package-manifest.json"
        if not archive.exists() or not manifest.exists():
            raise SystemExit("Replication package outputs were not created from extracted archive")
        check_archive_contents(archive)
        print(f"Extracted-archive replication check passed ({len(before)} deterministic outputs matched).")
    anonymous = ROOT / "dist" / "constitutional-review-anonymous-submission.zip"
    if not anonymous.exists():
        raise SystemExit("Combined anonymous archive is missing")
    check_archive_contents(anonymous, "anonymous-submission-manifest.json")
    with tempfile.TemporaryDirectory(prefix="constitutional-review-anonymous-") as temp:
        checkout = Path(temp)
        with zipfile.ZipFile(anonymous) as package:
            package.extractall(checkout)
        targets = sorted((checkout / "reports").glob("*.csv"))
        targets += sorted((checkout / "paper" / "tables").glob("*.tex"))
        targets += sorted((checkout / "paper" / "figures").glob("*.tex"))
        before = {path.relative_to(checkout): hashlib.sha256(path.read_bytes()).hexdigest() for path in targets}
        run(["make", "test", "paper"], checkout)
        changed = [str(path) for path, digest in before.items() if not (checkout / path).exists() or hashlib.sha256((checkout / path).read_bytes()).hexdigest() != digest]
        if changed:
            raise SystemExit("Anonymous rebuild changed frozen analytic outputs: " + ", ".join(changed))
        print("Extracted anonymous archive test and manuscript rebuild passed.")
    check_split_archives(
        anonymous,
        ROOT / "dist" / "constitutional-review-anonymous-manuscript.zip",
        ROOT / "dist" / "constitutional-review-anonymous-supplement.zip",
    )


if __name__ == "__main__":
    main()
