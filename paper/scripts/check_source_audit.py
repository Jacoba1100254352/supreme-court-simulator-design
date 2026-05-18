#!/usr/bin/env python3
"""Check that manuscript claims have source-audit anchors."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MAIN = ROOT / "paper" / "main.tex"
BIB = ROOT / "paper" / "references.bib"
AUDIT = ROOT / "paper" / "source-audit.csv"
CALIBRATION_PROVENANCE = ROOT / "data" / "calibration" / "provenance-manifest.csv"
LEGISLATIVE_PROVENANCE = ROOT / "data" / "external" / "legislative" / "source-provenance.csv"

REQUIRED_SECTIONS = {
    "Claim Boundaries and Interpretation",
    "Theory and Design Space",
    "Expectations",
    "Model",
    "Calibration and Source-Range Checks",
    "Metrics",
    "Emergency-Review Results",
    "Sensitivity and Robustness",
    "Limitations",
}


def fail(message: str) -> None:
    print(f"Source audit check failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def bib_keys() -> set[str]:
    return set(re.findall(r"@\w+\{([^,]+),", BIB.read_text()))


def cited_keys(source: str) -> set[str]:
    keys: set[str] = set()
    for group in re.findall(r"\\jlcite\{([^}]+)\}", source):
        keys.update(key.strip() for key in group.split(",") if key.strip())
    return keys


def main() -> None:
    if not AUDIT.exists():
        fail("paper/source-audit.csv is missing")
    if not CALIBRATION_PROVENANCE.exists():
        fail("data/calibration/provenance-manifest.csv is missing")
    if not LEGISLATIVE_PROVENANCE.exists():
        fail("data/external/legislative/source-provenance.csv is missing")
    source = MAIN.read_text()
    existing_bib_keys = bib_keys()
    manuscript_citations = cited_keys(source)

    rows = list(csv.DictReader(AUDIT.open(newline="")))
    if len(rows) < 12:
        fail("source audit should cover at least twelve material manuscript claims")

    sections = set()
    claim_ids = set()
    for row in rows:
        claim_id = row.get("claimId", "").strip()
        if not claim_id:
            fail("source audit row is missing claimId")
        if claim_id in claim_ids:
            fail(f"duplicate claimId {claim_id}")
        claim_ids.add(claim_id)

        section = row.get("manuscriptSection", "").strip()
        sections.add(section)
        if section and f"\\section{{{section}}}" not in source and f"\\section*{{{section}}}" not in source:
            fail(f"source audit section is not present in manuscript: {section}")

        evidence_path = row.get("evidencePath", "").strip()
        if evidence_path:
            path = ROOT / evidence_path
            if not path.exists():
                fail(f"{claim_id} evidence path does not exist: {evidence_path}")

        citation_field = row.get("citationKeys", "").strip()
        for key in [item.strip() for item in citation_field.split(";") if item.strip()]:
            if key not in existing_bib_keys:
                fail(f"{claim_id} cites missing bibliography key: {key}")
            if key not in manuscript_citations:
                fail(f"{claim_id} cites key not used in manuscript text: {key}")

        status = row.get("status", "").strip()
        if status != "checked":
            fail(f"{claim_id} status must be checked, not {status!r}")

    missing_sections = REQUIRED_SECTIONS - sections
    if missing_sections:
        fail("source audit is missing sections: " + ", ".join(sorted(missing_sections)))

    provenance_rows = list(csv.DictReader(CALIBRATION_PROVENANCE.open(newline="")))
    provenance_keys = {row.get("datasetKey", "").strip() for row in provenance_rows}
    for key in {"scdb-modern-2025-01", "shadow-docket-v2-0", "black-epstein-recusal", "supreme-court-synthesis", "supreme-court-research-2026"}:
        if key not in provenance_keys:
            fail(f"calibration provenance is missing datasetKey {key}")

    legislative_rows = list(csv.DictReader(LEGISLATIVE_PROVENANCE.open(newline="")))
    if "paper-legislative-profile" not in {row.get("datasetKey", "").strip() for row in legislative_rows}:
        fail("legislative provenance is missing paper-legislative-profile")

    print(f"Source audit check passed ({len(rows)} audited claims).")


if __name__ == "__main__":
    main()
