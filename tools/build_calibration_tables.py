#!/usr/bin/env python3
"""Build normalized calibration source tables from raw public datasets.

The simulator consumes small normalized CSVs in data/calibration instead of
coupling runtime Java code to large raw files. This script is intentionally
stdlib-only so it can be rerun after refreshing SCDB or shadow-docket downloads.
"""

from __future__ import annotations

import argparse
import csv
import zipfile
from collections import defaultdict
from pathlib import Path


SCDB_SOURCE_URL = "https://scdb.la.psu.edu/data/2025-release-01/"
SHADOW_SOURCE_URL = "https://www.shadowdocketdata.com/data"
RECUSAL_SOURCE_URL = "https://epstein.wustl.edu/recusal"


HEADER = [
    "sourceKey",
    "domain",
    "metric",
    "term",
    "numerator",
    "denominator",
    "value",
    "sourceUrl",
    "notes",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scdb-case-zip", type=Path, required=True)
    parser.add_argument("--shadow-zip", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("data/calibration"))
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    scdb_term_counts = write_scdb_observations(args.scdb_case_zip, args.output_dir)
    write_recusal_observations(scdb_term_counts, args.output_dir)
    if args.shadow_zip:
        write_shadow_observations(args.shadow_zip, args.output_dir)


def write_scdb_observations(scdb_case_zip: Path, output_dir: Path) -> dict[int, int]:
    term_stats: dict[int, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    with zipfile.ZipFile(scdb_case_zip) as archive:
        [name] = [name for name in archive.namelist() if name.endswith(".csv")]
        with archive.open(name) as raw:
            reader = csv.DictReader(line.decode("utf-8-sig") for line in raw)
            for row in reader:
                term = int(value(row, "term"))
                issue_area = int(value(row, "issueArea", "0"))
                admin_action = int(value(row, "adminAction", "0"))
                declaration_uncon = int(value(row, "declarationUncon", "1"))
                precedent_alteration = int(value(row, "precedentAlteration", "0"))

                stats = term_stats[term]
                stats["total"] += 1
                if issue_area in {2, 3, 4, 5}:
                    stats["rights"] += 1
                if issue_area == 8:
                    stats["economic"] += 1
                if issue_area in {9, 10, 11, 12}:
                    stats["structural"] += 1
                if admin_action > 0:
                    stats["admin"] += 1
                if declaration_uncon in {2, 3, 4}:
                    stats["unconstitutional"] += 1
                if precedent_alteration == 1:
                    stats["precedent_altered"] += 1

    rows: list[list[str]] = []
    for term in sorted(term_stats):
        stats = term_stats[term]
        total = stats["total"]
        add(rows, "scdb-modern-2025-01", "rights", "rightsClaimRate", term, stats["rights"], total,
            "SCDB issueArea values 2 civil rights, 3 First Amendment, 4 due process, and 5 privacy.")
        add(rows, "scdb-modern-2025-01", "administrative", "administrativeLawRate", term, stats["admin"], total,
            "SCDB adminAction present and nonzero.")
        add(rows, "scdb-modern-2025-01", "economic", "economicRegulationRate", term, stats["economic"], total,
            "SCDB issueArea value 8 economic activity.")
        add(rows, "scdb-modern-2025-01", "structural", "structuralRate", term, stats["structural"], total,
            "SCDB issueArea values 9 judicial power, 10 federalism, 11 interstate relations, and 12 federal taxation.")
        add(rows, "scdb-modern-2025-01", "constitutional", "invalidationRate", term, stats["unconstitutional"], total,
            "SCDB declarationUncon values 2, 3, and 4.")
        stable = total - stats["precedent_altered"]
        add(rows, "scdb-modern-2025-01", "precedent", "precedentStability", term, stable, total,
            "One minus SCDB precedentAlteration share.")
        not_unconstitutional = total - stats["unconstitutional"]
        add(rows, "scdb-modern-2025-01", "statutory", "statutoryStability", term, not_unconstitutional, total,
            "One minus SCDB declarationUncon share.")
        add(rows, "scdb-modern-2025-01", "merits", "meritsReviewRate", term, total, total,
            "SCDB case-centered merits dataset term coverage.")

    write_csv(output_dir / "scdb-modern-2025-release-01.csv", rows)
    return {term: stats["total"] for term, stats in term_stats.items()}


def write_shadow_observations(shadow_zip: Path, output_dir: Path) -> None:
    term_stats: dict[int, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    with zipfile.ZipFile(shadow_zip) as archive:
        [name] = [name for name in archive.namelist() if name.endswith(".csv") and not name.startswith("__MACOSX")]
        with archive.open(name) as raw:
            reader = csv.DictReader(line.decode("utf-8-sig", errors="replace") for line in raw)
            for row in reader:
                term_text = value(row, "term", "")
                if not term_text:
                    continue
                term = int(float(term_text))
                stats = term_stats[term]
                stats["orders"] += 1
                emergency = truthy(value(row, "emergency_application", "0"))
                if emergency:
                    stats["emergency"] += 1
                    if truthy(value(row, "relief_granted", "0")):
                        stats["relief_granted"] += 1
                    if truthy(value(row, "dissent", "0")) or truthy(value(row, "disagreement", "0")):
                        stats["visible_disagreement"] += 1

    rows: list[list[str]] = []
    for term in sorted(term_stats):
        stats = term_stats[term]
        orders = stats["orders"]
        emergency = stats["emergency"]
        add(rows, "shadow-docket-v2-0", "emergency", "emergencyStayDocketRate", term, emergency, orders,
            "Emergency applications divided by all parsed Journal orders.", SHADOW_SOURCE_URL)
        if emergency:
            add(rows, "shadow-docket-v2-0", "emergency", "emergencyOrderRate", term, stats["relief_granted"], emergency,
                "Relief granted among emergency applications.", SHADOW_SOURCE_URL)
            add(rows, "shadow-docket-v2-0", "emergency", "shadowDocketAbuse", term, stats["visible_disagreement"], emergency,
                "Proxy: dissent or visible disagreement among emergency applications.", SHADOW_SOURCE_URL)
    write_csv(output_dir / "shadow-docket-v2-0-summary.csv", rows)


def write_recusal_observations(scdb_term_counts: dict[int, int], output_dir: Path) -> None:
    cases_1946_2003 = sum(count for term, count in scdb_term_counts.items() if 1946 <= term <= 2003)
    justice_case_opportunities = cases_1946_2003 * 9
    rows: list[list[str]] = []
    add(rows, "black-epstein-recusal", "recusal", "recusalRate", "1946-2003", 599, justice_case_opportunities,
        "Black and Epstein report 599 post-1946 recusal cases; denominator uses SCDB case-centered cases times nine justice seats.",
        RECUSAL_SOURCE_URL)
    write_csv(output_dir / "black-epstein-recusal-summary.csv", rows)


def add(
    rows: list[list[str]],
    source_key: str,
    domain: str,
    metric: str,
    term: int | str,
    numerator: int,
    denominator: int,
    notes: str,
    source_url: str = SCDB_SOURCE_URL,
) -> None:
    value_text = "0.000000" if denominator == 0 else f"{numerator / denominator:.6f}"
    rows.append([
        source_key,
        domain,
        metric,
        str(term),
        str(numerator),
        str(denominator),
        value_text,
        source_url,
        notes,
    ])


def write_csv(path: Path, rows: list[list[str]]) -> None:
    with path.open("w", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(HEADER)
        writer.writerows(rows)


def value(row: dict[str, str], key: str, default: str | None = None) -> str:
    text = row.get(key, "")
    if text is None or text == "":
        if default is None:
            raise ValueError(f"Missing required field: {key}")
        return default
    return text


def truthy(text: str) -> bool:
    return text.strip().lower() in {"1", "true", "yes", "y"}


if __name__ == "__main__":
    main()
