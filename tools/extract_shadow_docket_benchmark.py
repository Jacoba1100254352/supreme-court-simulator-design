#!/usr/bin/env python3
"""Extract a compact emergency-application benchmark slice.

The raw Shadow Docket Database archive is intentionally not committed. This
script accepts a locally downloaded CSV or zip archive and writes a compact,
source-record-addressable slice under data/benchmarks/.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import zipfile
from collections import Counter
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "data" / "benchmarks" / "emergency-application-order-extract-shadow-docket-v3-0.csv"
DEFAULT_MANIFEST = ROOT / "data" / "benchmarks" / "emergency-application-order-extract-shadow-docket-v3-0-manifest.json"
SOURCE_KEY = "shadow-docket-v3-0"
SOURCE_NAME = "Supreme Court Shadow Docket Database v3.0"
SOURCE_URL = "https://www.shadowdocketdata.com/data"
SOURCE_DOWNLOAD_URL = (
    "https://www.dropbox.com/scl/fi/m4gr0ay66x8o7gqdy0mrd/"
    "shadow_docket_database_files.zip?rlkey=ofsyuzlon0modt9poc767qsd2&dl=1"
)
SOURCE_FILE = "shadow_docket_database_v3-0.csv"


FIELDNAMES = [
    "sourceKey",
    "sourceName",
    "sourceUrl",
    "sourceDownloadUrl",
    "sourceFile",
    "sourceFileSha256",
    "sourceRecordId",
    "term",
    "docketNumber",
    "orderDate",
    "actionClass",
    "relief",
    "reliefGranted",
    "emergencyApplication",
    "deathPenalty",
    "publicDisagreement",
    "writtenDissent",
    "fullCourt",
    "rulingJustice",
    "petitioner",
    "respondent",
    "lowerCourt",
    "governmentPetitioner",
    "governmentRespondent",
    "benchmarkUse",
    "coderNotes",
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_csv_bytes(path: Path) -> tuple[str, bytes]:
    if path.suffix.lower() == ".zip":
        with zipfile.ZipFile(path) as archive:
            candidates = [
                name
                for name in archive.namelist()
                if name.endswith(".csv") and not name.startswith("__MACOSX/")
            ]
            if SOURCE_FILE in candidates:
                name = SOURCE_FILE
            elif len(candidates) == 1:
                name = candidates[0]
            else:
                raise SystemExit(f"Could not choose source CSV from zip candidates: {candidates}")
            return name, archive.read(name)
    return path.name, path.read_bytes()


def normalize_binary(value: str) -> str:
    clean = (value or "").strip()
    if clean in {"1", "0"}:
        return clean
    if clean.lower() == "true":
        return "1"
    if clean.lower() == "false":
        return "0"
    if clean.upper() == "NA" or clean == "":
        return "NA"
    return clean


def source_rows(source_name: str, source_data: bytes) -> Iterable[tuple[int, dict[str, str]]]:
    text = source_data.decode("utf-8-sig").splitlines()
    reader = csv.DictReader(text)
    for index, row in enumerate(reader, start=2):
        yield index, row


def extract_rows(source_name: str, source_data: bytes, terms: set[str]) -> list[dict[str, str]]:
    source_hash = sha256_bytes(source_data)
    output: list[dict[str, str]] = []
    for line_number, row in source_rows(source_name, source_data):
        if row.get("term") not in terms:
            continue
        if row.get("emergency_application") != "1":
            continue
        if row.get("full_court") != "1":
            continue
        output.append({
            "sourceKey": SOURCE_KEY,
            "sourceName": SOURCE_NAME,
            "sourceUrl": SOURCE_URL,
            "sourceDownloadUrl": SOURCE_DOWNLOAD_URL,
            "sourceFile": source_name,
            "sourceFileSha256": source_hash,
            "sourceRecordId": f"{source_name}:line {line_number}",
            "term": row.get("term", ""),
            "docketNumber": row.get("docket_number", ""),
            "orderDate": row.get("date", ""),
            "actionClass": row.get("action_class", ""),
            "relief": row.get("relief", ""),
            "reliefGranted": normalize_binary(row.get("relief_granted", "")),
            "emergencyApplication": normalize_binary(row.get("emergency_application", "")),
            "deathPenalty": normalize_binary(row.get("death_penalty", "")),
            "publicDisagreement": normalize_binary(row.get("disagreement", "")),
            "writtenDissent": normalize_binary(row.get("dissent", "")),
            "fullCourt": normalize_binary(row.get("full_court", "")),
            "rulingJustice": row.get("ruling_justice", ""),
            "petitioner": row.get("petitioner", ""),
            "respondent": row.get("respondent", ""),
            "lowerCourt": row.get("lower_ct", ""),
            "governmentPetitioner": normalize_binary(row.get("gov_petitioner", "")),
            "governmentRespondent": normalize_binary(row.get("gov_respondent", "")),
            "benchmarkUse": "application-level denominator, grant, and public-disagreement reconciliation",
            "coderNotes": (
                "Source row is filtered to emergency_application=1 and full_court=1; "
                "order date is not a petition/application filing date; merits follow-through "
                "and downstream policy status are not coded in this extract."
            ),
        })
    return output


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_manifest(
    path: Path,
    source_name: str,
    source_data: bytes,
    terms: list[str],
    rows: list[dict[str, str]],
    output_path: Path,
) -> None:
    by_term = Counter(row["term"] for row in rows)
    granted_by_term = Counter(row["term"] for row in rows if row["reliefGranted"] == "1")
    disagreement_by_term = Counter(row["term"] for row in rows if row["publicDisagreement"] == "1")
    payload = {
        "sourceKey": SOURCE_KEY,
        "sourceName": SOURCE_NAME,
        "sourceUrl": SOURCE_URL,
        "sourceDownloadUrl": SOURCE_DOWNLOAD_URL,
        "sourceFile": source_name,
        "sourceFileSha256": sha256_bytes(source_data),
        "filters": {
            "terms": terms,
            "emergency_application": "1",
            "full_court": "1",
        },
        "output": output_path.relative_to(ROOT).as_posix(),
        "rowCount": len(rows),
        "termApplicationCounts": dict(sorted(by_term.items())),
        "termGrantedCounts": dict(sorted(granted_by_term.items())),
        "termPublicDisagreementCounts": dict(sorted(disagreement_by_term.items())),
        "notes": [
            "Raw third-party archive is not committed.",
            "Extract is an application/order denominator slice, not merits-follow-through or downstream-effect coding.",
            "The source page text may lag the downloadable file name; this extract follows the v3.0 CSV and v3.0 codebook naming.",
        ],
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Path to shadow_docket_database_v3-0.csv or containing zip")
    parser.add_argument("--terms", nargs="+", default=["2023", "2024"])
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source_name, data = source_csv_bytes(args.source)
    terms = [str(term) for term in args.terms]
    rows = extract_rows(source_name, data, set(terms))
    if not rows:
        raise SystemExit("No rows matched the requested filters.")
    write_csv(args.output, rows)
    write_manifest(args.manifest, source_name, data, terms, rows, args.output)
    print(f"Wrote {args.output.relative_to(ROOT)} ({len(rows)} rows)")
    print(f"Wrote {args.manifest.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
