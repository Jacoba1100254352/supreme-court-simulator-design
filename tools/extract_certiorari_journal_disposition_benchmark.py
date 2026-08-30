#!/usr/bin/env python3
"""Extract a Journal-based certiorari disposition seed.

The official Journal PDF is intentionally not committed. This script accepts a
locally downloaded Journal PDF or text dump and writes a schema-shaped extract
of certiorari petition disposition entries. The output is row-level disposition
evidence, not a closed filing cohort: it captures Journal entries that reached a
published disposition during the term and leaves filing, CFR, CVSG, counsel,
amicus, and split-quality fields uncoded.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "data" / "benchmarks" / "certiorari-cohort-schema.csv"
DEFAULT_OUTPUT = ROOT / "data" / "benchmarks" / "certiorari-journal-disposition-extract-ot2023.csv"
DEFAULT_MANIFEST = ROOT / "data" / "benchmarks" / "certiorari-journal-disposition-extract-ot2023-manifest.json"
SOURCE_KEY = "journal-ot2023"
SOURCE_NAME = "Journal of the Supreme Court OT2023"
SOURCE_URL = "https://www.supremecourt.gov/orders/journal/jnl23.pdf"
SOURCE_FILE = "jnl23.pdf"
TERM = "OT2023"
EXPECTED_SOURCE_SHA256 = "f5d8eb56e7b0256fa583a3722037b7ef1b01b028f7dc985f2d5ceb39900e30f7"
DATE_RE = re.compile(
    r"^(MONDAY|TUESDAY|WEDNESDAY|THURSDAY|FRIDAY|SATURDAY|SUNDAY),\s+"
    r"([A-Z]+)\s+(\d{1,2}),\s+(\d{4})$"
)
ENTRY_START_RE = re.compile(r"^(No\.|Nos\.)\s+")
DOCKET_RE = re.compile(r"\d{2}[\-–]\d+|\d{2}A\d+|Orig\.\s*\d+")
MONTHS = {
    "JANUARY": 1,
    "FEBRUARY": 2,
    "MARCH": 3,
    "APRIL": 4,
    "MAY": 5,
    "JUNE": 6,
    "JULY": 7,
    "AUGUST": 8,
    "SEPTEMBER": 9,
    "OCTOBER": 10,
    "NOVEMBER": 11,
    "DECEMBER": 12,
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pdf_text(path: Path) -> str:
    if path.suffix.lower() == ".txt":
        return path.read_text(errors="replace")
    try:
        result = subprocess.run(
            ["pdftotext", str(path), "-"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
    except FileNotFoundError as exc:
        raise SystemExit("pdftotext is required to parse Journal PDFs") from exc
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"pdftotext failed for {path}: {exc.stderr}") from exc
    return result.stdout


def schema_fields() -> list[str]:
    with SCHEMA.open(newline="") as handle:
        return [row["fieldName"] for row in csv.DictReader(handle)]


def normalize_docket(docket: str) -> str:
    return docket.replace("–", "-").replace(" ", "")


def paid_or_ifp(docket: str) -> str:
    normalized = normalize_docket(docket)
    match = re.match(r"(\d{2})-(\d+)$", normalized)
    if match:
        return "ifp" if int(match.group(2)) >= 5000 else "paid"
    if re.match(r"\d{2}A\d+$", normalized):
        return "application_or_misc"
    if normalized.startswith("Orig."):
        return "original"
    return "uncoded"


def disposition(paragraph: str) -> tuple[str, str, str]:
    lower = paragraph.lower()
    if "petition for writ of certiorari" not in lower and "petitions for writs of certiorari" not in lower:
        return "not_certiorari_petition", "", ""
    if "motion to expedite consideration of the petition for writ of certiorari" in lower:
        return "not_certiorari_petition", "", ""
    if "granted" in lower and ("vacated" in lower or "remanded" in lower):
        return "gvr_or_remand", "1", "1"
    if re.search(r"(?:^|[.]\s+)petitions?\s+for\s+writs?\s+of\s+certiorari\b[^.]*\bgranted\b", lower):
        return "granted", "1", "0"
    if "dismissed" in lower:
        return "dismissed", "0", "0"
    if "denied" in lower:
        return "denied", "0", "0"
    return "other_disposition_review_required", "", ""


def lower_court(paragraph: str) -> str:
    match = re.search(
        r"(?:to|from)\s+the\s+(.+?)(?:\.\s|\s+(?:denied|granted|dismissed|vacated|remanded)\b)",
        paragraph,
        flags=re.IGNORECASE,
    )
    if not match:
        return ""
    value = match.group(1).strip(" .;")
    return re.sub(r"\s+", " ", value)


def issue_area(paragraph: str) -> str:
    lower = paragraph.lower()
    if "united states" in lower and ("criminal" in lower or "court of appeals" in lower):
        return "uncoded_federal"
    if any(token in lower for token in ("warden", "correction", "superintendent", "habeas")):
        return "uncoded_criminal_or_habeas"
    return "uncoded"


def case_caption(paragraph: str) -> str:
    match = re.match(r"^(?:No\.|Nos\.)\s+[^.]+\.\s+(.+?)\s+Petitions? for writs? of certiorari", paragraph)
    if match:
        return match.group(1).strip()
    match = re.match(r"^(?:No\.|Nos\.)\s+[^.]+\.\s+(.+?)\s+On petition", paragraph)
    if match:
        return match.group(1).strip()
    return ""


def entry_dockets(paragraph: str) -> list[str]:
    match = re.match(r"^(?:No\.|Nos\.)\s+([^.]*)\.", paragraph)
    if not match:
        return []
    return [normalize_docket(item) for item in DOCKET_RE.findall(match.group(1))]


def journal_entries(text: str) -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    current_date = ""
    buffer: list[str] = []
    buffer_date = ""
    buffer_page = 0
    buffer_line = 0

    def flush() -> None:
        nonlocal buffer
        if not buffer:
            return
        paragraph = " ".join(line.strip() for line in buffer if line.strip())
        paragraph = re.sub(r"\s+", " ", paragraph)
        if re.search(r"Petitions? for writs? of certiorari", paragraph, flags=re.IGNORECASE):
            entries.append({
                "dispositionDate": buffer_date,
                "textPage": buffer_page,
                "textLine": buffer_line,
                "paragraph": paragraph,
            })
        buffer = []

    for page_number, page in enumerate(text.split("\f"), start=1):
        for line_number, raw_line in enumerate(page.splitlines(), start=1):
            line = raw_line.strip()
            if not line:
                continue
            date_match = DATE_RE.match(line)
            if date_match:
                current_date = date(
                    int(date_match.group(4)),
                    MONTHS[date_match.group(2)],
                    int(date_match.group(3)),
                ).isoformat()
                continue
            if buffer and re.fullmatch(r"\d+", line):
                continue
            if ENTRY_START_RE.match(line):
                flush()
                buffer = [line]
                buffer_date = current_date
                buffer_page = page_number
                buffer_line = line_number
            elif buffer:
                buffer.append(line)
    flush()
    return entries


def build_rows(text: str, source_hash: str) -> list[dict[str, str]]:
    fieldnames = schema_fields()
    rows: list[dict[str, str]] = []
    for entry in journal_entries(text):
        paragraph = str(entry["paragraph"])
        dockets = entry_dockets(paragraph)
        if not dockets:
            continue
        cert_disposition, granted, gvr = disposition(paragraph)
        if cert_disposition == "not_certiorari_petition":
            continue
        caption = case_caption(paragraph)
        court = lower_court(paragraph)
        for docket in dockets:
            row = {field: "" for field in fieldnames}
            row.update({
                "sourceKey": SOURCE_KEY,
                "sourceRecordId": f"{SOURCE_FILE}:text-page-{entry['textPage']}:line-{entry['textLine']}:{docket}",
                "sourceUrl": SOURCE_URL,
                "term": TERM,
                "docketNumber": docket,
                "petitionType": "certiorari",
                "paidOrIfp": paid_or_ifp(docket),
                "lowerCourt": court,
                "issueArea": issue_area(paragraph),
                "dispositionDate": str(entry["dispositionDate"]),
                "certDisposition": cert_disposition,
                "granted": granted,
                "gvrOrSummaryDisposition": gvr,
                "coderNotes": (
                    "Extracted from official Journal text. "
                    "This is disposition-level Journal evidence, not a closed filing cohort. "
                    "Filing date, CFR, CVSG, response source, counsel, amicus, split-quality, "
                    "and merits follow-through fields remain uncoded. "
                    f"Source PDF sha256={source_hash}. Caption: {caption}"
                ),
            })
            rows.append(row)
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = schema_fields()
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_manifest(path: Path, input_path: Path, source_hash: str, rows: list[dict[str, str]]) -> None:
    dispositions = Counter(row["certDisposition"] for row in rows)
    paid_ifp = Counter(row["paidOrIfp"] for row in rows)
    docket_prefixes = Counter(
        match.group(1)
        for row in rows
        if (match := re.match(r"(\d{2})-\d+$", row["docketNumber"]))
    )
    manifest = {
        "sourceKey": SOURCE_KEY,
        "sourceName": SOURCE_NAME,
        "sourceUrl": SOURCE_URL,
        "sourceFile": SOURCE_FILE,
        "sourceFileSha256": source_hash,
        "expectedSourceFileSha256": EXPECTED_SOURCE_SHA256,
        "inputPath": str(input_path),
        "output": str(DEFAULT_OUTPUT.relative_to(ROOT)),
        "rowCount": len(rows),
        "uniqueDocketCount": len({row["docketNumber"] for row in rows}),
        "firstDispositionDate": min(row["dispositionDate"] for row in rows if row["dispositionDate"]),
        "lastDispositionDate": max(row["dispositionDate"] for row in rows if row["dispositionDate"]),
        "dispositionCounts": dict(sorted(dispositions.items())),
        "dispositionDateCounts": dict(sorted(Counter(row["dispositionDate"] for row in rows).items())),
        "paidOrIfpCounts": dict(sorted(paid_ifp.items())),
        "docketPrefixCounts": dict(sorted(docket_prefixes.items())),
        "notes": [
            "Raw Journal PDF is not committed.",
            "Rows are extracted from Journal disposition text and shaped like the certiorari cohort schema.",
            "This extract is not a closed petition filing cohort and should not be used as denominator-matched validation evidence.",
        ],
    }
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Local Journal PDF or pdftotext dump")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    args = parser.parse_args()

    source_hash = sha256(args.input) if args.input.suffix.lower() != ".txt" else ""
    if source_hash and source_hash != EXPECTED_SOURCE_SHA256:
        raise SystemExit(
            "Unexpected Journal PDF sha256. "
            f"Expected {EXPECTED_SOURCE_SHA256}; got {source_hash}"
        )
    text = pdf_text(args.input)
    rows = build_rows(text, source_hash)
    if not rows:
        raise SystemExit("No certiorari disposition rows were extracted")
    write_csv(args.output, rows)
    write_manifest(args.manifest, args.input, source_hash, rows)
    print(f"Wrote {args.output.relative_to(ROOT)} ({len(rows)} rows)")
    print(f"Wrote {args.manifest.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
