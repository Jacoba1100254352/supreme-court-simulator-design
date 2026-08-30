#!/usr/bin/env python3
"""Build a closed paid/IFP docketed-intake cohort for a configured term.

The official Journal term-flow totals define each publication cohort. This
extractor enumerates the corresponding public docket-number ranges, codes
docket-visible petition stages, and, when a same-term Journal disposition slice
exists, reconciles current docket outcomes to that independent extract.

The source unit is a docketed case, not every submission received by the Clerk.
Counsel specialization and alleged/genuine split quality remain uncoded.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.error import HTTPError, URLError

import extract_certiorari_granted_docket_detail_benchmark as docket


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK_DIR = ROOT / "data" / "benchmarks"
CALIBRATION_DIR = ROOT / "data" / "calibration"
REPORTS = ROOT / "reports"
SCHEMA = BENCHMARK_DIR / "certiorari-cohort-schema.csv"
SOURCE_URL = "https://www.supremecourt.gov/docket/docket.aspx"


@dataclass(frozen=True)
class TermConfig:
    term: str
    docket_prefix: str
    journal_url: str
    source_name: str
    journal_disposition_extract: Path | None = None
    journal_docket_detail_extract: Path | None = None
    boundary_exclusions: tuple[dict[str, str], ...] = ()

    @property
    def slug(self) -> str:
        return self.term.lower()

    @property
    def source_key(self) -> str:
        return f"scotus-certiorari-docketed-cohort-{self.slug}"

    @property
    def term_flow_extract(self) -> Path:
        return (
            BENCHMARK_DIR
            / f"certiorari-term-flow-extract-journal-{self.slug}.csv"
        )

    @property
    def default_output(self) -> Path:
        return BENCHMARK_DIR / f"certiorari-docketed-cohort-{self.slug}.csv"

    @property
    def default_manifest(self) -> Path:
        return (
            BENCHMARK_DIR
            / f"certiorari-docketed-cohort-{self.slug}-manifest.json"
        )

    @property
    def report_term_suffix(self) -> str:
        return "" if self.term == "OT2023" else f"-{self.slug}"

    @property
    def default_summary_csv(self) -> Path:
        return (
            REPORTS
            / f"certiorari-docketed-cohort-summary{self.report_term_suffix}-v1.csv"
        )

    @property
    def default_summary_md(self) -> Path:
        return (
            REPORTS
            / f"certiorari-docketed-cohort-summary{self.report_term_suffix}-v1.md"
        )

    @property
    def default_reconciliation_csv(self) -> Path:
        return (
            REPORTS
            / (
                "certiorari-docketed-cohort-journal-reconciliation"
                f"{self.report_term_suffix}-v1.csv"
            )
        )

    @property
    def default_reconciliation_md(self) -> Path:
        return (
            REPORTS
            / (
                "certiorari-docketed-cohort-journal-reconciliation"
                f"{self.report_term_suffix}-v1.md"
            )
        )

    @property
    def default_calibration_csv(self) -> Path:
        return (
            CALIBRATION_DIR
            / f"scotus-certiorari-docketed-cohort-{self.slug}.csv"
        )

    @property
    def default_cache_dir(self) -> Path:
        return ROOT / "data" / "raw" / "supreme-court-dockets" / self.slug

    @property
    def boundary_note(self) -> str:
        return (
            f"Official Supreme Court public docket row in the closed {self.term} "
            "paid/IFP docketed-intake cohort. The cohort covers docketed cases, "
            "not submissions that were never docketed; specialist counsel and "
            "split quality remain uncoded."
        )


TERM_CONFIGS = {
    "OT2023": TermConfig(
        term="OT2023",
        docket_prefix="23",
        journal_url="https://www.supremecourt.gov/orders/journal/jnl23.pdf",
        source_name=(
            "Official Supreme Court OT2023 paid/IFP docketed-intake cohort"
        ),
        journal_disposition_extract=(
            BENCHMARK_DIR / "certiorari-journal-disposition-extract-ot2023.csv"
        ),
        journal_docket_detail_extract=(
            BENCHMARK_DIR / "certiorari-journal-docket-detail-ot2023.csv"
        ),
    ),
    "OT2024": TermConfig(
        term="OT2024",
        docket_prefix="24",
        journal_url="https://www.supremecourt.gov/orders/journal/Jnl24.pdf",
        source_name=(
            "Official Supreme Court OT2024 published-statistics "
            "paid/IFP docketed-intake cohort"
        ),
        boundary_exclusions=(
            {
                "docketNumber": "24-1328",
                "paidOrIfp": "paid",
                "docketedDate": "2025-06-30",
                "sourceUrl": docket.docket_url("24-1328"),
                "reason": (
                    "official page is dated on the Journal cutoff but the "
                    "docket number is above the published paid-count range; "
                    "excluded to preserve the published-statistics snapshot"
                ),
            },
            {
                "docketNumber": "24-1329",
                "paidOrIfp": "paid",
                "docketedDate": "2025-06-30",
                "sourceUrl": docket.docket_url("24-1329"),
                "reason": (
                    "official page is dated on the Journal cutoff but the "
                    "docket number is above the published paid-count range; "
                    "excluded to preserve the published-statistics snapshot"
                ),
            },
            {
                "docketNumber": "24-7528",
                "paidOrIfp": "ifp",
                "docketedDate": "2025-06-30",
                "sourceUrl": docket.docket_url("24-7528"),
                "reason": (
                    "official page is dated on the Journal cutoff but the "
                    "docket number is above the published IFP-count range; "
                    "excluded to preserve the published-statistics snapshot"
                ),
            },
            {
                "docketNumber": "24-7529",
                "paidOrIfp": "ifp",
                "docketedDate": "2025-06-30",
                "sourceUrl": docket.docket_url("24-7529"),
                "reason": (
                    "official page is dated on the Journal cutoff but the "
                    "docket number is above the published IFP-count range; "
                    "excluded to preserve the published-statistics snapshot"
                ),
            },
        ),
    ),
}
CONFIG = TERM_CONFIGS["OT2023"]
PAID_FIRST = 1
IFP_FIRST = 5001
SUMMARY_FIELDS = [
    "metricKey",
    "observedValue",
    "denominatorSpec",
    "sourceUrl",
    "validationUse",
    "manuscriptUse",
    "notes",
]
RECONCILIATION_FIELDS = [
    "docketNumber",
    "paidOrIfp",
    "docketDisposition",
    "docketDispositionDate",
    "journalDispositions",
    "journalDispositionDates",
    "reconciliationStatus",
    "officialDocketUrl",
    "reviewNote",
]
CALIBRATION_FIELDS = [
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
GRANT_DISPOSITIONS = {"granted", "gvr_or_remand"}
NON_GRANT_FINAL_DISPOSITIONS = {
    "denied",
    "dismissed",
    "ifp_fee_denied_closed",
    "removed_from_docket",
    "quorum_affirmance",
}
RESOLVED_CERT_DISPOSITIONS = GRANT_DISPOSITIONS | NON_GRANT_FINAL_DISPOSITIONS


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def schema_fields() -> list[str]:
    return [row["fieldName"] for row in read_csv(SCHEMA)]


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def safe_relative(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def source_hash(rows: list[dict[str, str]]) -> str:
    payload = json.dumps(rows, sort_keys=True, ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def term_flow_counts() -> dict[str, int]:
    counts = {
        row["statisticKey"]: int(row["officialCount"])
        for row in read_csv(CONFIG.term_flow_extract)
        if row.get("officialCount")
    }
    required = {"cases_docketed_paid", "cases_docketed_ifp"}
    missing = required - set(counts)
    if missing:
        raise SystemExit(
            "Term-flow extract is missing official docket counts: "
            + ", ".join(sorted(missing))
        )
    return counts


def expected_dockets() -> list[dict[str, str]]:
    counts = term_flow_counts()
    paid_count = counts["cases_docketed_paid"]
    ifp_count = counts["cases_docketed_ifp"]
    rows: list[dict[str, str]] = []
    for number in range(PAID_FIRST, PAID_FIRST + paid_count):
        rows.append(
            {
                "docketNumber": f"{CONFIG.docket_prefix}-{number}",
                "paidOrIfp": "paid",
            }
        )
    for number in range(IFP_FIRST, IFP_FIRST + ifp_count):
        rows.append(
            {
                "docketNumber": f"{CONFIG.docket_prefix}-{number}",
                "paidOrIfp": "ifp",
            }
        )
    if (
        paid_count <= 0
        or ifp_count <= 0
        or len(rows) != paid_count + ifp_count
        or len({row["docketNumber"] for row in rows}) != len(rows)
    ):
        raise SystemExit(
            f"{CONFIG.term} term-flow counts do not define a valid cohort "
            f"contract: paid={paid_count}, ifp={ifp_count}, total={len(rows)}"
        )
    expected_numbers = {row["docketNumber"] for row in rows}
    overlapping_exclusions = [
        row["docketNumber"]
        for row in CONFIG.boundary_exclusions
        if row["docketNumber"] in expected_numbers
    ]
    if overlapping_exclusions:
        raise SystemExit(
            "Configured boundary exclusions overlap the official-count cohort: "
            + ", ".join(overlapping_exclusions)
        )
    return rows


def meta_content(body: str, name: str) -> str:
    pattern = re.compile(
        rf"<meta\s+name=['\"]{re.escape(name)}['\"]\s+content=['\"](.*?)['\"]\s*/?>",
        re.IGNORECASE | re.DOTALL,
    )
    match = pattern.search(body)
    if not match:
        return ""
    return " ".join(html.unescape(match.group(1)).split())


def primary_filing_row(
    proceedings: list[dict[str, str]],
) -> dict[str, str] | None:
    return docket.first_row(
        proceedings,
        lambda row: "filed" in row["text"].lower()
        and (
            row["text"].lower().startswith("petition for a writ")
            or row["text"].lower().startswith("petition for writ")
            or row["text"].lower().startswith("jurisdictional statement")
            or row["text"].lower().startswith("statement as to jurisdiction")
        ),
    )


def petition_type(proceedings: list[dict[str, str]]) -> str:
    filing = primary_filing_row(proceedings)
    if filing is None:
        return "uncoded_or_no_primary_filing"
    text = filing["text"].lower()
    if "writ of certiorari" in text or "writ certiorari" in text:
        return "certiorari"
    if "jurisdictional statement" in text or "statement as to jurisdiction" in text:
        return "appeal_or_jurisdictional_statement"
    if any(
        phrase in text
        for phrase in (
            "writ of mandamus",
            "writ of prohibition",
            "writ of habeas corpus",
            "extraordinary writ",
        )
    ):
        return "extraordinary_writ"
    return "other_petition"


def conservative_party_type(name: str) -> str:
    normalized = " ".join(name.lower().split())
    if not normalized:
        return ""
    federal_markers = (
        "united states",
        "u.s. department",
        "department of justice",
        "secretary of homeland security",
        "secretary of state",
        "secretary of defense",
        "secretary of education",
        "secretary of commerce",
        "secretary of labor",
        "secretary of the treasury",
        "attorney general of the united states",
    )
    if any(marker in normalized for marker in federal_markers):
        return "federal_government"
    state_markers = (
        "state of ",
        "commonwealth of ",
        "attorney general of ",
        "governor of ",
    )
    if any(marker in normalized for marker in state_markers):
        return "state_government"
    return "other_or_uncoded"


def lower_court_origin(lower_court: str) -> str:
    normalized = lower_court.lower()
    if "united states court of appeals" in normalized:
        if "armed forces" in normalized:
            return "military_appellate"
        return "federal_court_of_appeals"
    if "united states district court" in normalized:
        return "federal_district_court"
    if "supreme court" in normalized:
        return "state_or_territorial_high_court"
    if "court of appeals" in normalized or "appellate court" in normalized:
        return "state_or_territorial_appellate"
    if "tax court" in normalized or "court of federal claims" in normalized:
        return "specialized_federal_court"
    if "agency" in normalized or "board" in normalized or "commission" in normalized:
        return "agency_or_board"
    return "other_or_uncoded" if lower_court else ""


def certiorari_disposition(
    proceedings: list[dict[str, str]],
    filing_type: str,
) -> tuple[str, str, dict[str, str] | None]:
    if filing_type != "certiorari":
        return "not_certiorari_intake", "", None
    for row in proceedings:
        text = " ".join(row["text"].lower().split())
        if "rehearing" in text:
            continue
        denied = (
            re.match(r"^petition denied\b", text)
            or re.search(
                r"petition for (?:a )?(?:writ of )?certiorari"
                r"(?: before judgment)? (?:is )?denied\b",
                text,
            )
        )
        dismissed = (
            re.match(r"^petition dismissed\b", text)
            or re.match(r"^the petition is dismissed\b", text)
            or re.search(
                r"petition for (?:a )?(?:writ of )?certiorari"
                r"(?: before judgment)? (?:is )?dismissed\b",
                text,
            )
        )
        granted = (
            re.match(r"^petition granted\b", text)
            or re.match(r"^the petition is granted\b", text)
            or re.search(
                r"petition for (?:a )?(?:writ of )?certiorari"
                r"(?: before judgment)? (?:is )?granted\b",
                text,
            )
        )
        if dismissed:
            return "dismissed", row["date"], row
        if denied:
            return "denied", row["date"], row
        if granted:
            if "judgment vacated" in text or "case remanded" in text:
                return "gvr_or_remand", row["date"], row
            return "granted", row["date"], row
        if text.startswith("case considered closed"):
            return "ifp_fee_denied_closed", row["date"], row
        if text.startswith("case removed from docket"):
            return "removed_from_docket", row["date"], row
        if "court lacks a quorum" in text and "judgment is affirmed" in text:
            return "quorum_affirmance", row["date"], row
    return "pending_or_unresolved", "", None


def response_requested_row(
    proceedings: list[dict[str, str]],
    disposition_date: str,
) -> dict[str, str] | None:
    return docket.first_row(
        docket.rows_before(proceedings, disposition_date),
        lambda row: "response requested" in row["text"].lower(),
    )


def cvsg_row(
    proceedings: list[dict[str, str]],
    disposition_date: str,
) -> dict[str, str] | None:
    return docket.first_row(
        docket.rows_before(proceedings, disposition_date),
        lambda row: (
            "solicitor general is invited to file a brief" in row["text"].lower()
            or "expressing the views of the united states" in row["text"].lower()
        ),
    )


def build_row(expected: dict[str, str], page_url: str, body: str) -> dict[str, str]:
    proceedings = docket.proceeding_rows(body)
    parts = docket.text_parts(body)
    filing = primary_filing_row(proceedings)
    filing_type = petition_type(proceedings)
    disposition, disposition_date, disposition_row = certiorari_disposition(
        proceedings, filing_type
    )
    pre_disposition = docket.rows_before(proceedings, disposition_date)
    response_requested = response_requested_row(proceedings, disposition_date)
    cvsg = cvsg_row(proceedings, disposition_date)
    response_filed, response_source = docket.response_info(
        proceedings, pre_disposition
    )
    if not response_filed:
        response_filed = "no"
    amicus_count = sum(
        1
        for row in pre_disposition
        if row["text"].lower().startswith("brief amicus curiae")
        or row["text"].lower().startswith("brief amici curiae")
    )
    distribution_count = sum(
        1
        for row in pre_disposition
        if row["text"].startswith("DISTRIBUTED for Conference")
    )
    argued = any(
        row["text"].lower().startswith("argued.")
        or "set for argument" in row["text"].lower()
        for row in proceedings
        if row["date"] and (not disposition_date or row["date"] >= disposition_date)
    )
    merits_date, merits_result, reversal_or_vacatur = docket.merits_outcome(
        proceedings, disposition_date
    )
    lower_court = docket.next_after(parts, "Lower Ct:")
    petitioner = meta_content(body, "Petitioner")
    respondent = meta_content(body, "Respondent")
    docketed_date = docket.parse_date(meta_content(body, "Docketed"))
    metadata_case_type = meta_content(body, "CaseType").lower()
    expected_type = expected["paidOrIfp"]
    if metadata_case_type and metadata_case_type != expected_type:
        raise ValueError(
            f"{expected['docketNumber']} metadata CaseType={metadata_case_type!r} "
            f"does not match expected {expected_type!r}"
        )

    output = {field: "" for field in schema_fields()}
    output.update(
        {
            "sourceKey": CONFIG.source_key,
            "sourceRecordId": (
                f"docket:{expected['docketNumber']}; "
                f"cohort:{CONFIG.term}-paid-ifp-docketed"
            ),
            "sourceUrl": page_url,
            "term": CONFIG.term,
            "docketNumber": expected["docketNumber"],
            "petitionFiledDate": filing["date"] if filing else "",
            "petitionType": filing_type,
            "paidOrIfp": expected_type,
            "petitionerType": conservative_party_type(petitioner),
            "respondentType": conservative_party_type(respondent),
            "lowerCourt": lower_court,
            "lowerCourtOrigin": lower_court_origin(lower_court),
            "responseFiled": response_filed,
            "responseSource": response_source,
            "responseRequestedByCourt": "yes" if response_requested else "no",
            "cfrDate": response_requested["date"] if response_requested else "",
            "cvsgRequested": "yes" if cvsg else "no",
            "cvsgDate": cvsg["date"] if cvsg else "",
            "sgRecommendation": (
                docket.sg_recommendation(
                    proceedings,
                    cvsg["date"],
                    disposition_date,
                )
                if cvsg
                else ""
            ),
            "certStageAmicusCount": str(amicus_count),
            "relistCount": (
                str(max(0, distribution_count - 1))
                if distribution_count
                else "0"
            ),
            "dispositionDate": disposition_date,
            "certDisposition": disposition,
            "granted": (
                "yes"
                if disposition in GRANT_DISPOSITIONS
                else "no"
                if disposition in NON_GRANT_FINAL_DISPOSITIONS
                else ""
            ),
            "grantSetForArgument": (
                "yes"
                if argued
                else "no"
                if disposition in RESOLVED_CERT_DISPOSITIONS
                else ""
            ),
            "gvrOrSummaryDisposition": (
                "yes"
                if disposition == "gvr_or_remand"
                else "no"
                if disposition in RESOLVED_CERT_DISPOSITIONS
                else ""
            ),
            "meritsDocket": (
                expected["docketNumber"]
                if disposition == "granted" and argued
                else ""
            ),
            "meritsDecisionDate": merits_date,
            "meritsOutcome": merits_result,
            "reversalOrVacatur": reversal_or_vacatur,
            "coderNotes": (
                f"{CONFIG.boundary_note} "
                f"Docketed date={docketed_date or 'unparsed'}; "
                f"disposition source={'docket proceeding' if disposition_row else 'none/not applicable'}."
            ),
        }
    )
    return output


def fetch_and_build(
    index: int,
    expected: dict[str, str],
    retries: int,
    cache_dir: Path | None,
    request_delay: float,
) -> tuple[
    int,
    dict[str, str] | None,
    dict[str, str] | None,
    str,
]:
    docket_number = expected["docketNumber"]
    cache_path = (
        cache_dir / f"{docket_number}.html"
        if cache_dir is not None
        else None
    )
    if cache_path is not None and cache_path.exists():
        try:
            body = cache_path.read_text(errors="replace")
            page_url = docket.docket_url(docket_number)
            return index, build_row(expected, page_url, body), None, "cache"
        except (OSError, ValueError):
            pass

    last_error: Exception | None = None
    for attempt in range(retries + 1):
        try:
            if request_delay:
                time.sleep(request_delay)
            page_url, body = docket.fetch_docket(docket_number)
            coded = build_row(expected, page_url, body)
            if cache_path is not None:
                cache_path.parent.mkdir(parents=True, exist_ok=True)
                cache_path.write_text(body)
            return index, coded, None, "network"
        except (HTTPError, URLError, TimeoutError, OSError, ValueError) as exc:
            last_error = exc
            if attempt < retries:
                backoff = 0.5 * (attempt + 1)
                if isinstance(exc, HTTPError) and exc.code in {403, 429}:
                    backoff = 5.0 * (attempt + 1)
                time.sleep(backoff)
    return (
        index,
        None,
        {
            "index": str(index),
            "docketNumber": docket_number,
            "paidOrIfp": expected["paidOrIfp"],
            "sourceUrl": docket.docket_url(docket_number),
            "error": repr(last_error),
        },
        "",
    )


def reusable_journal_docket_rows() -> dict[str, dict[str, str]]:
    """Return one prior official-docket row for each in-range docket.

    The Journal-detail extract was fetched from the same official static pages
    on the same publication snapshot date. Reusing those rows avoids thousands
    of redundant requests while preserving an explicit provenance trail. When
    the Journal parser emitted more than one row for a docket, prefer the
    earliest cert-stage disposition because later entries can concern IFP or
    rehearing motions rather than a new petition outcome.
    """
    if CONFIG.journal_docket_detail_extract is None:
        return {}
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    counts = term_flow_counts()
    for row in read_csv(CONFIG.journal_docket_detail_extract):
        if not re.fullmatch(
            rf"{re.escape(CONFIG.docket_prefix)}-\d+",
            row.get("docketNumber", ""),
        ):
            continue
        number = int(row["docketNumber"].split("-", 1)[1])
        if not (
            PAID_FIRST <= number < PAID_FIRST + counts["cases_docketed_paid"]
            or IFP_FIRST <= number < IFP_FIRST + counts["cases_docketed_ifp"]
        ):
            continue
        grouped[row["docketNumber"]].append(row)
    reusable: dict[str, dict[str, str]] = {}
    for docket_number, rows in grouped.items():
        reusable[docket_number] = sorted(
            rows,
            key=lambda row: (
                row.get("dispositionDate", "") == "",
                row.get("dispositionDate", ""),
                row.get("sourceRecordId", ""),
            ),
        )[0]
    return reusable


def reusable_existing_cohort_rows(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    return {
        row["docketNumber"]: row
        for row in read_csv(path)
        if row.get("sourceKey") == CONFIG.source_key
        and row.get("docketNumber")
    }


def reuse_row(expected: dict[str, str], prior: dict[str, str]) -> dict[str, str]:
    output = {field: prior.get(field, "") for field in schema_fields()}
    disposition = output.get("certDisposition", "")
    resolved = disposition in RESOLVED_CERT_DISPOSITIONS
    if output.get("lowerCourt") and not output.get("lowerCourtOrigin"):
        output["lowerCourtOrigin"] = lower_court_origin(output["lowerCourt"])
    if output.get("cvsgRequested") != "yes":
        output["sgRecommendation"] = ""
    if resolved:
        output["granted"] = (
            "yes" if disposition in GRANT_DISPOSITIONS else "no"
        )
        output["gvrOrSummaryDisposition"] = (
            "yes" if disposition == "gvr_or_remand" else "no"
        )
        if not output.get("grantSetForArgument"):
            output["grantSetForArgument"] = "no"
    output["meritsDocket"] = (
        expected["docketNumber"]
        if output.get("grantSetForArgument") == "yes"
        else ""
    )
    output.update(
        {
            "sourceKey": CONFIG.source_key,
            "sourceRecordId": (
                f"docket:{expected['docketNumber']}; "
                f"cohort:{CONFIG.term}-paid-ifp-docketed"
            ),
            "term": CONFIG.term,
            "docketNumber": expected["docketNumber"],
            "paidOrIfp": expected["paidOrIfp"],
            "coderNotes": (
                f"{CONFIG.boundary_note} Docket-visible fields were reused from the "
                "same-date official-docket extract; a full network refresh "
                "remains available by disabling reuse."
            ),
        }
    )
    return output


def build_rows(
    expected_rows: list[dict[str, str]],
    workers: int,
    retries: int,
    reuse_journal_detail: bool,
    existing_output: Path | None,
    refresh_statuses: set[str],
    cache_dir: Path | None,
    request_delay: float,
) -> tuple[
    list[dict[str, str]],
    list[dict[str, str]],
    int,
    int,
    int,
    int,
]:
    coded_by_index: dict[int, dict[str, str]] = {}
    failures: list[dict[str, str]] = []
    existing = (
        reusable_existing_cohort_rows(existing_output)
        if existing_output is not None
        else {}
    )
    reusable = reusable_journal_docket_rows() if reuse_journal_detail else {}
    fetch_rows: list[tuple[int, dict[str, str]]] = []
    existing_reuse_count = 0
    journal_reuse_count = 0
    cache_reuse_count = 0
    network_fetch_count = 0
    for index, row in enumerate(expected_rows):
        current = existing.get(row["docketNumber"])
        if current is not None and current.get("certDisposition", "") not in refresh_statuses:
            coded_by_index[index] = reuse_row(row, current)
            existing_reuse_count += 1
            continue
        if current is not None and current.get("certDisposition", "") in refresh_statuses:
            fetch_rows.append((index, row))
            continue
        prior = reusable.get(row["docketNumber"])
        if prior is not None:
            coded_by_index[index] = reuse_row(row, prior)
            journal_reuse_count += 1
        else:
            fetch_rows.append((index, row))
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [
            executor.submit(
                fetch_and_build,
                index,
                row,
                retries,
                cache_dir,
                request_delay,
            )
            for index, row in fetch_rows
        ]
        for completed, future in enumerate(as_completed(futures), start=1):
            index, coded_row, failure, retrieval = future.result()
            if coded_row is not None:
                coded_by_index[index] = coded_row
                if retrieval == "cache":
                    cache_reuse_count += 1
                elif retrieval == "network":
                    network_fetch_count += 1
            if failure is not None:
                failures.append(failure)
            if completed % 250 == 0 or completed == len(futures):
                print(
                    f"{CONFIG.term}: processed {completed:,}/"
                    f"{len(futures):,} requested docket pages "
                    f"({network_fetch_count:,} network, "
                    f"{cache_reuse_count:,} cache, "
                    f"{len(failures):,} failed)",
                    flush=True,
                )
    coded_rows = [coded_by_index[index] for index in sorted(coded_by_index)]
    failures.sort(key=lambda row: int(row["index"]))
    return (
        coded_rows,
        failures,
        existing_reuse_count,
        journal_reuse_count,
        cache_reuse_count,
        network_fetch_count,
    )


def validate_coded_rows(
    expected_rows: list[dict[str, str]],
    coded_rows: list[dict[str, str]],
    failures: list[dict[str, str]],
) -> None:
    """Fail closed when the cohort no longer matches its enumeration contract."""
    expected = {row["docketNumber"]: row for row in expected_rows}
    coded_numbers = [row["docketNumber"] for row in coded_rows]
    failure_numbers = [row["docketNumber"] for row in failures]
    coded = set(coded_numbers)
    failed = set(failure_numbers)
    problems: list[str] = []

    if len(expected) != len(expected_rows):
        problems.append("expected docket contract contains duplicate numbers")
    if len(coded) != len(coded_numbers):
        problems.append("coded cohort contains duplicate docket numbers")
    if len(failed) != len(failure_numbers):
        problems.append("failure list contains duplicate docket numbers")
    if coded & failed:
        problems.append(
            "dockets appear in both coded and failed sets: "
            + ", ".join(sorted(coded & failed)[:5])
        )
    missing_or_extra = (coded | failed) ^ set(expected)
    if missing_or_extra:
        problems.append(
            "coded plus failed dockets do not equal the expected cohort: "
            + ", ".join(sorted(missing_or_extra)[:5])
        )

    allowed_petition_types = {
        "certiorari",
        "appeal_or_jurisdictional_statement",
        "extraordinary_writ",
        "other_petition",
        "uncoded_or_no_primary_filing",
    }
    allowed_dispositions = (
        RESOLVED_CERT_DISPOSITIONS
        | {"pending_or_unresolved", "not_certiorari_intake"}
    )
    for row in coded_rows:
        docket_number = row["docketNumber"]
        contract = expected.get(docket_number)
        if contract is None:
            continue
        if row["sourceKey"] != CONFIG.source_key:
            problems.append(f"{docket_number}: unexpected sourceKey")
        if row["term"] != CONFIG.term:
            problems.append(f"{docket_number}: unexpected term")
        if row["paidOrIfp"] != contract["paidOrIfp"]:
            problems.append(f"{docket_number}: paid/IFP class differs from contract")
        if row["sourceUrl"] != docket.docket_url(docket_number):
            problems.append(f"{docket_number}: unexpected sourceUrl")
        if row["petitionType"] not in allowed_petition_types:
            problems.append(
                f"{docket_number}: invalid petitionType={row['petitionType']!r}"
            )
        disposition = row["certDisposition"]
        if disposition not in allowed_dispositions:
            problems.append(
                f"{docket_number}: invalid certDisposition={disposition!r}"
            )
        if row["petitionType"] == "certiorari":
            if disposition == "not_certiorari_intake":
                problems.append(
                    f"{docket_number}: certiorari row marked not-certiorari intake"
                )
        elif disposition != "not_certiorari_intake":
            problems.append(
                f"{docket_number}: non-certiorari row has cert disposition "
                f"{disposition!r}"
            )

        expected_granted = (
            "yes"
            if disposition in GRANT_DISPOSITIONS
            else "no"
            if disposition in NON_GRANT_FINAL_DISPOSITIONS
            else ""
        )
        if row["granted"] != expected_granted:
            problems.append(f"{docket_number}: granted flag is inconsistent")
        expected_gvr = (
            "yes"
            if disposition == "gvr_or_remand"
            else "no"
            if disposition in RESOLVED_CERT_DISPOSITIONS
            else ""
        )
        if row["gvrOrSummaryDisposition"] != expected_gvr:
            problems.append(f"{docket_number}: GVR flag is inconsistent")
        for field in ("responseRequestedByCourt", "cvsgRequested"):
            if row[field] not in {"yes", "no"}:
                problems.append(f"{docket_number}: invalid {field}={row[field]!r}")
        if row["responseRequestedByCourt"] == "yes" and not row["cfrDate"]:
            problems.append(f"{docket_number}: CFR flag lacks cfrDate")
        if row["cvsgRequested"] == "yes" and not row["cvsgDate"]:
            problems.append(f"{docket_number}: CVSG flag lacks cvsgDate")
        if row["cvsgRequested"] == "no" and row["sgRecommendation"]:
            problems.append(
                f"{docket_number}: SG recommendation appears without CVSG"
            )
        for field in ("certStageAmicusCount", "relistCount"):
            try:
                if int(row[field]) < 0:
                    raise ValueError
            except ValueError:
                problems.append(f"{docket_number}: invalid {field}={row[field]!r}")
        for field in (
            "petitionFiledDate",
            "cfrDate",
            "cvsgDate",
            "dispositionDate",
            "meritsDecisionDate",
        ):
            if row[field]:
                try:
                    date.fromisoformat(row[field])
                except ValueError:
                    problems.append(
                        f"{docket_number}: invalid {field}={row[field]!r}"
                    )

    if problems:
        raise SystemExit(
            f"{CONFIG.term} cohort validation failed with {len(problems)} "
            "problem(s); first: "
            + problems[0]
        )


def journal_index() -> dict[str, list[dict[str, str]]]:
    if CONFIG.journal_disposition_extract is None:
        return {}
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in read_csv(CONFIG.journal_disposition_extract):
        if re.fullmatch(
            rf"{re.escape(CONFIG.docket_prefix)}-\d+",
            row.get("docketNumber", ""),
        ):
            grouped[row["docketNumber"]].append(row)
    return grouped


def reconciliation_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    journal = journal_index()
    output: list[dict[str, str]] = []
    for row in rows:
        journal_rows = journal.get(row["docketNumber"], [])
        journal_dispositions = sorted(
            {item["certDisposition"] for item in journal_rows}
        )
        journal_dates = sorted(
            {item["dispositionDate"] for item in journal_rows if item["dispositionDate"]}
        )
        if not journal_rows:
            status = "not_in_journal_disposition_extract"
            note = (
                f"Docket is in the independently enumerated {CONFIG.term} intake "
                "cohort but not the parsed Journal disposition slice."
            )
        elif row["certDisposition"] in journal_dispositions:
            status = "outcome_matches_journal"
            note = "Current docket outcome matches at least one parsed Journal row."
        else:
            status = "outcome_differs_from_journal"
            note = (
                "Review parser scope or later disposition timing before using the "
                "Journal row as a petition-cohort outcome."
            )
        output.append(
            {
                "docketNumber": row["docketNumber"],
                "paidOrIfp": row["paidOrIfp"],
                "docketDisposition": row["certDisposition"],
                "docketDispositionDate": row["dispositionDate"],
                "journalDispositions": ";".join(journal_dispositions),
                "journalDispositionDates": ";".join(journal_dates),
                "reconciliationStatus": status,
                "officialDocketUrl": row["sourceUrl"],
                "reviewNote": note,
            }
        )
    return output


def summary_rows(
    rows: list[dict[str, str]],
    failures: list[dict[str, str]],
    reconciliation: list[dict[str, str]],
) -> list[dict[str, str]]:
    official_counts = term_flow_counts()
    paid_count = official_counts["cases_docketed_paid"]
    ifp_count = official_counts["cases_docketed_ifp"]
    expected_count = paid_count + ifp_count
    cert_rows = [row for row in rows if row["petitionType"] == "certiorari"]
    paid_cert = [row for row in cert_rows if row["paidOrIfp"] == "paid"]
    ifp_cert = [row for row in cert_rows if row["paidOrIfp"] == "ifp"]
    status_counts = Counter(row["reconciliationStatus"] for row in reconciliation)
    disposition_counts = Counter(row["certDisposition"] for row in rows)

    def metric(
        key: str,
        value: int,
        denominator: str,
        use: str,
        notes: str,
    ) -> dict[str, str]:
        return {
            "metricKey": key,
            "observedValue": str(value),
            "denominatorSpec": denominator,
            "sourceUrl": SOURCE_URL,
            "validationUse": "closed_docketed_intake_cohort",
            "manuscriptUse": use,
            "notes": notes,
        }

    summary = [
        metric(
            "certiorariDocketedCohortExpectedRows",
            expected_count,
            f"Official {CONFIG.term} paid plus IFP cases docketed during term",
            "direct official denominator reconciliation",
            (
                f"Journal total: {paid_count:,} paid plus {ifp_count:,} "
                "IFP docketed cases."
            ),
        ),
        metric(
            "certiorariDocketedCohortRows",
            len(rows),
            (
                f"Independently enumerated {CONFIG.term} paid and IFP "
                "public docket-number ranges"
            ),
            (
                "closed docketed-intake cohort when this equals "
                f"{expected_count:,} with zero failures"
            ),
            "One row per reachable official public docket page.",
        ),
        metric(
            "certiorariDocketedCohortFailedFetchRows",
            len(failures),
            f"Official {CONFIG.term} paid plus IFP docket-number ranges",
            "must be zero before closed-cohort language is used",
            "Rows not coded after bounded retries.",
        ),
        metric(
            "certiorariDocketedCohortPaidRows",
            sum(1 for row in rows if row["paidOrIfp"] == "paid"),
            f"Closed {CONFIG.term} paid/IFP docketed-intake cohort",
            "direct official paid-intake count",
            f"Must reconcile to the Journal count of {paid_count:,}.",
        ),
        metric(
            "certiorariDocketedCohortIfpRows",
            sum(1 for row in rows if row["paidOrIfp"] == "ifp"),
            f"Closed {CONFIG.term} paid/IFP docketed-intake cohort",
            "direct official IFP-intake count",
            f"Must reconcile to the Journal count of {ifp_count:,}.",
        ),
        metric(
            "certiorariDocketedCohortCertPetitionRows",
            len(cert_rows),
            f"Closed {CONFIG.term} paid/IFP docketed-intake cohort",
            "direct docket-visible certiorari petition denominator",
            "Rows whose primary filing is a petition for a writ of certiorari.",
        ),
        metric(
            "certiorariDocketedCohortPetitionFiledDateRows",
            sum(1 for row in cert_rows if row["petitionFiledDate"]),
            "Docket-visible certiorari petition rows in the closed cohort",
            "direct filing-date completeness check",
            "Certiorari rows with a parsed petition filing date.",
        ),
        metric(
            "certiorariDocketedCohortResponseFiledOrWaivedRows",
            sum(1 for row in cert_rows if row["responseFiled"] in {"yes", "waived"}),
            "Docket-visible certiorari petition rows in the closed cohort",
            "direct response-stage descriptive evidence",
            "Includes filed responses and docketed waivers.",
        ),
        metric(
            "certiorariDocketedCohortPaidCfrRows",
            sum(1 for row in paid_cert if row["responseRequestedByCourt"] == "yes"),
            "Paid certiorari petition rows in the closed cohort",
            "direct paid CFR numerator",
            "Official docket rows with a Response Requested entry.",
        ),
        metric(
            "certiorariDocketedCohortIfpCfrRows",
            sum(1 for row in ifp_cert if row["responseRequestedByCourt"] == "yes"),
            "IFP certiorari petition rows in the closed cohort",
            "direct IFP CFR numerator",
            "Official docket rows with a Response Requested entry.",
        ),
        metric(
            "certiorariDocketedCohortCvsgRows",
            sum(1 for row in cert_rows if row["cvsgRequested"] == "yes"),
            "Docket-visible certiorari petition rows in the closed cohort",
            "direct whole-cohort CVSG numerator",
            "Official docket rows inviting the Solicitor General's views.",
        ),
        metric(
            "certiorariDocketedCohortAmicusRows",
            sum(1 for row in cert_rows if int(row["certStageAmicusCount"] or "0") > 0),
            "Docket-visible certiorari petition rows in the closed cohort",
            "direct cert-stage amicus-presence numerator",
            "Rows with at least one docket-visible amicus brief before disposition.",
        ),
        metric(
            "certiorariDocketedCohortRelistedRows",
            sum(1 for row in cert_rows if int(row["relistCount"] or "0") > 0),
            "Docket-visible certiorari petition rows in the closed cohort",
            "direct relist-presence numerator",
            "Rows with more than one distribution before disposition.",
        ),
        metric(
            "certiorariDocketedCohortGrantedRows",
            disposition_counts["granted"],
            "Docket-visible certiorari petition rows in the closed cohort",
            "direct docketed-cohort plenary-grant numerator",
            "Excludes GVR/remand dispositions.",
        ),
        metric(
            "certiorariDocketedCohortGvrRows",
            disposition_counts["gvr_or_remand"],
            "Docket-visible certiorari petition rows in the closed cohort",
            "direct docketed-cohort GVR/remand numerator",
            "Docket grant rows that also vacate or remand at cert-stage disposition.",
        ),
        metric(
            "certiorariDocketedCohortDeniedRows",
            disposition_counts["denied"],
            "Docket-visible certiorari petition rows in the closed cohort",
            "direct docketed-cohort denial numerator",
            "First docket-visible certiorari disposition is denial.",
        ),
        metric(
            "certiorariDocketedCohortDismissedRows",
            disposition_counts["dismissed"],
            "Docket-visible certiorari petition rows in the closed cohort",
            "direct docketed-cohort dismissal numerator",
            "Includes Rule 39.8 and other petition dismissals.",
        ),
        metric(
            "certiorariDocketedCohortOtherClosedRows",
            sum(
                disposition_counts[key]
                for key in (
                    "ifp_fee_denied_closed",
                    "removed_from_docket",
                    "quorum_affirmance",
                )
            ),
            "Docket-visible certiorari petition rows in the closed cohort",
            "direct nonstandard final-outcome numerator",
            "Separates fee-denied closures, docket removals, and statutory quorum affirmance from ordinary denial.",
        ),
        metric(
            "certiorariDocketedCohortPendingOrUnresolvedRows",
            disposition_counts["pending_or_unresolved"],
            "Docket-visible certiorari petition rows in the closed cohort",
            "must remain explicit as an outcome-completeness limitation",
            "Certiorari rows without a classified current docket disposition.",
        ),
    ]
    if CONFIG.journal_disposition_extract is not None:
        summary.extend(
            [
                metric(
                    "certiorariDocketedCohortJournalOutcomeMatches",
                    status_counts["outcome_matches_journal"],
                    (
                        "Closed cohort dockets also present in the parsed "
                        "Journal disposition slice"
                    ),
                    "source-reconciliation evidence",
                    (
                        "Current docket outcome matches at least one parsed "
                        "Journal disposition."
                    ),
                ),
                metric(
                    "certiorariDocketedCohortJournalOutcomeDifferences",
                    status_counts["outcome_differs_from_journal"],
                    (
                        "Closed cohort dockets also present in the parsed "
                        "Journal disposition slice"
                    ),
                    "manual parser-reconciliation queue only",
                    (
                        "Differences can reflect parser errors or later docket "
                        "developments."
                    ),
                ),
                metric(
                    "certiorariDocketedCohortNotInJournalDispositionExtract",
                    status_counts["not_in_journal_disposition_extract"],
                    f"Closed {CONFIG.term} paid/IFP docketed-intake cohort",
                    (
                        "cohort-closure evidence, not a Journal parser error "
                        "by itself"
                    ),
                    "Dockets absent from the disposition-seeded Journal extract.",
                ),
            ]
        )
    return summary


def rate_row(
    metric: str,
    numerator: int,
    denominator: int,
    notes: str,
) -> dict[str, str]:
    return {
        "sourceKey": CONFIG.source_key,
        "domain": "U.S. Supreme Court certiorari",
        "metric": metric,
        "term": CONFIG.term,
        "numerator": str(numerator),
        "denominator": str(denominator),
        "value": f"{numerator / denominator:.9f}" if denominator else "",
        "sourceUrl": SOURCE_URL,
        "notes": notes,
    }


def calibration_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    paid_rows = [row for row in rows if row["paidOrIfp"] == "paid"]
    ifp_rows = [row for row in rows if row["paidOrIfp"] == "ifp"]
    cert_rows = [row for row in rows if row["petitionType"] == "certiorari"]
    paid_cert = [row for row in cert_rows if row["paidOrIfp"] == "paid"]
    ifp_cert = [row for row in cert_rows if row["paidOrIfp"] == "ifp"]
    resolved_cert = [
        row
        for row in cert_rows
        if row["certDisposition"] in RESOLVED_CERT_DISPOSITIONS
    ]
    return [
        rate_row(
            "paidPetitionShare",
            len(paid_rows),
            len(rows),
            "Strict official term-flow check over the closed paid/IFP docketed-intake cohort.",
        ),
        rate_row(
            "ifpPetitionShare",
            len(ifp_rows),
            len(rows),
            "Strict official term-flow check over the closed paid/IFP docketed-intake cohort.",
        ),
        rate_row(
            "cfrRate_paid",
            sum(1 for row in paid_cert if row["responseRequestedByCourt"] == "yes"),
            len(paid_cert),
            "Official docket Response Requested entries among paid certiorari petitions in the closed docketed cohort.",
        ),
        rate_row(
            "cfrRate_ifp",
            sum(1 for row in ifp_cert if row["responseRequestedByCourt"] == "yes"),
            len(ifp_cert),
            "Official docket Response Requested entries among IFP certiorari petitions in the closed docketed cohort.",
        ),
        rate_row(
            "cvsgRequestRate",
            sum(1 for row in cert_rows if row["cvsgRequested"] == "yes"),
            len(cert_rows),
            "Official docket CVSG entries among certiorari petitions in the closed docketed cohort.",
        ),
        rate_row(
            "certStageAmicusPresenceRate",
            sum(1 for row in cert_rows if int(row["certStageAmicusCount"] or "0") > 0),
            len(cert_rows),
            "At least one docket-visible cert-stage amicus brief before disposition.",
        ),
        rate_row(
            "relistRate",
            sum(1 for row in cert_rows if int(row["relistCount"] or "0") > 0),
            len(cert_rows),
            "More than one docket-visible distribution before disposition.",
        ),
        rate_row(
            "certiorariGrantRate_docketedCohort",
            sum(
                1
                for row in resolved_cert
                if row["certDisposition"] in GRANT_DISPOSITIONS
            ),
            len(resolved_cert),
            "Grant or GVR among resolved certiorari petitions in the closed docketed cohort; not constitutional-review-only.",
        ),
    ]


def validate_calibration_rows(rows: list[dict[str, str]]) -> None:
    metrics = [row["metric"] for row in rows]
    problems: list[str] = []
    if len(metrics) != len(set(metrics)):
        problems.append("duplicate calibration metric rows")
    for row in rows:
        metric = row["metric"]
        if row["sourceKey"] != CONFIG.source_key or row["term"] != CONFIG.term:
            problems.append(f"{metric}: source identity differs from term config")
            continue
        try:
            numerator = int(row["numerator"])
            denominator = int(row["denominator"])
        except ValueError:
            problems.append(f"{metric}: non-numeric calibration value")
            continue
        if denominator == 0:
            if numerator != 0 or row["value"]:
                problems.append(
                    f"{metric}: zero denominator must have zero numerator "
                    "and blank value"
                )
            continue
        try:
            value = float(row["value"])
        except ValueError:
            problems.append(f"{metric}: non-numeric calibration value")
            continue
        if denominator < 0 or numerator < 0 or numerator > denominator:
            problems.append(
                f"{metric}: invalid numerator/denominator "
                f"{numerator}/{denominator}"
            )
        elif abs(value - numerator / denominator) > 5e-10:
            problems.append(f"{metric}: value does not match its ratio")
    if problems:
        raise SystemExit(
            f"{CONFIG.term} calibration validation failed with {len(problems)} "
            "problem(s); first: "
            + problems[0]
        )


def write_summary_markdown(
    path: Path,
    rows: list[dict[str, str]],
    failures: list[dict[str, str]],
) -> None:
    counts = term_flow_counts()
    paid_count = counts["cases_docketed_paid"]
    ifp_count = counts["cases_docketed_ifp"]
    expected_count = paid_count + ifp_count
    lines = [
        "# Certiorari Docketed Cohort Summary v1",
        "",
        (
            f"This report summarizes an independently enumerated {CONFIG.term} "
            f"cohort of all {paid_count:,} paid and {ifp_count:,} IFP cases "
            "docketed during the official Journal statistics window. It closes "
            f"the {expected_count:,}-case docketed-intake denominator and "
            "docket-visible CFR/CVSG/amicus/relist fields. It does not cover "
            "submissions never docketed, and it does not code specialist counsel "
            "or alleged/genuine split quality."
        ),
        "",
        f"- Failed official docket fetches after retries: {len(failures)}",
        "",
        "| Metric | Value | Denominator | Manuscript use | Notes |",
        "| --- | ---: | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| `{row['metricKey']}` | {row['observedValue']} | "
            f"{row['denominatorSpec']} | {row['manuscriptUse']} | {row['notes']} |"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def write_reconciliation_markdown(
    path: Path,
    rows: list[dict[str, str]],
) -> None:
    counts = Counter(row["reconciliationStatus"] for row in rows)
    differences = [
        row for row in rows if row["reconciliationStatus"] == "outcome_differs_from_journal"
    ]
    lines = [
        "# Certiorari Docketed Cohort and Journal Reconciliation v1",
        "",
        (
            "This reconciliation compares current official docket outcomes in "
            f"the closed {CONFIG.term} paid/IFP docketed cohort with the "
            "separately parsed Journal disposition slice. Absence from the "
            "Journal slice is expected for matters outside that disposition "
            "parser's scope or timing. Outcome differences are a parser-review "
            "queue, not evidence that the official docket is wrong."
        ),
        "",
        "| Status | Rows |",
        "| --- | ---: |",
    ]
    for key in sorted(counts):
        lines.append(f"| `{key}` | {counts[key]} |")
    lines.extend(
        [
            "",
            "## Outcome-Difference Review Queue",
            "",
            "| Docket | Docket outcome | Journal outcome(s) | Docket date | Journal date(s) |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in differences:
        lines.append(
            f"| [{row['docketNumber']}]({row['officialDocketUrl']}) | "
            f"{row['docketDisposition']} | {row['journalDispositions']} | "
            f"{row['docketDispositionDate']} | {row['journalDispositionDates']} |"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def write_manifest(
    path: Path,
    expected_rows: list[dict[str, str]],
    coded_rows: list[dict[str, str]],
    failures: list[dict[str, str]],
    reconciliation: list[dict[str, str]],
    snapshot_date: date,
    output_path: Path,
    calibration_path: Path,
    workers: int,
    retries: int,
    existing_reuse_count: int,
    journal_reuse_count: int,
    cache_reuse_count: int,
    network_fetch_count: int,
    cache_dir: Path | None,
    request_delay: float,
) -> None:
    counts = term_flow_counts()
    paid_count = counts["cases_docketed_paid"]
    ifp_count = counts["cases_docketed_ifp"]
    paid_last = PAID_FIRST + paid_count - 1
    ifp_last = IFP_FIRST + ifp_count - 1
    notes = [
        (
            f"The official Journal reports {paid_count:,} paid and "
            f"{ifp_count:,} IFP cases docketed during {CONFIG.term}."
        ),
        (
            "Those counts map exactly to contiguous public docket ranges "
            f"{CONFIG.docket_prefix}-{PAID_FIRST} through "
            f"{CONFIG.docket_prefix}-{paid_last} and "
            f"{CONFIG.docket_prefix}-{IFP_FIRST} through "
            f"{CONFIG.docket_prefix}-{ifp_last}."
            if not CONFIG.boundary_exclusions
            else (
                "The official published counts define the benchmark ranges "
                f"{CONFIG.docket_prefix}-{PAID_FIRST} through "
                f"{CONFIG.docket_prefix}-{paid_last} and "
                f"{CONFIG.docket_prefix}-{IFP_FIRST} through "
                f"{CONFIG.docket_prefix}-{ifp_last}; same-day dockets above "
                "those count boundaries are recorded separately as exclusions."
            )
        ),
        (
            "The extract is a closed docketed-intake cohort, not a census of "
            "submissions that were never docketed."
        ),
        (
            "Docket-visible response, CFR, CVSG, amicus, relist, disposition, "
            "and merits-follow-through fields are coded where applicable."
        ),
        (
            "Rows already present in the same-date official-docket "
            "Journal-detail extract may be reused to avoid redundant Court-site "
            "requests; the manifest reports reused and freshly fetched counts."
        ),
        (
            "Specialist-counsel, former-clerk, alleged-split, genuine-split, "
            "split-depth, issue-area, and vehicle-quality fields remain outside "
            "this automated source slice."
        ),
    ]
    payload = {
        "sourceKey": CONFIG.source_key,
        "sourceName": CONFIG.source_name,
        "sourceUrl": SOURCE_URL,
        "sourceJournalUrl": CONFIG.journal_url,
        "snapshotDate": snapshot_date.isoformat(),
        "term": CONFIG.term,
        "enumerationRule": {
            "paid": {
                "firstDocket": f"{CONFIG.docket_prefix}-{PAID_FIRST}",
                "lastDocket": f"{CONFIG.docket_prefix}-{paid_last}",
                "officialCount": paid_count,
            },
            "ifp": {
                "firstDocket": f"{CONFIG.docket_prefix}-{IFP_FIRST}",
                "lastDocket": f"{CONFIG.docket_prefix}-{ifp_last}",
                "officialCount": ifp_count,
            },
        },
        "expectedRowCount": len(expected_rows),
        "rowCount": len(coded_rows),
        "uniqueDocketCount": len({row["docketNumber"] for row in coded_rows}),
        "failedFetchCount": len(failures),
        "failedFetches": failures,
        "reusedExistingCohortRows": existing_reuse_count,
        "reusedJournalDocketDetailRows": journal_reuse_count,
        "reusedCachedDocketPages": cache_reuse_count,
        "freshlyFetchedRows": network_fetch_count,
        "cacheDirectory": safe_relative(cache_dir) if cache_dir else "",
        "workers": workers,
        "retries": retries,
        "requestDelaySeconds": request_delay,
        "output": safe_relative(output_path),
        "calibrationOutput": safe_relative(calibration_path),
        "sourceRecordSha256": source_hash(coded_rows),
        "paidOrIfpCounts": dict(
            sorted(Counter(row["paidOrIfp"] for row in coded_rows).items())
        ),
        "petitionTypeCounts": dict(
            sorted(Counter(row["petitionType"] for row in coded_rows).items())
        ),
        "dispositionCounts": dict(
            sorted(Counter(row["certDisposition"] for row in coded_rows).items())
        ),
        "journalReconciliationCounts": dict(
            sorted(
                Counter(
                    row["reconciliationStatus"] for row in reconciliation
                ).items()
            )
        ),
        "notes": notes,
    }
    if CONFIG.boundary_exclusions:
        payload["boundaryPolicy"] = {
            "basis": (
                "The Journal's published paid and IFP counts define the "
                "snapshot-cohort ranges."
            ),
            "calendarDateCaveat": (
                "The official public docket contains same-cutoff-date records "
                "above those count-defined ranges, so this cohort is not every "
                "public docket carrying the cutoff calendar date."
            ),
            "excludedDocketCount": len(CONFIG.boundary_exclusions),
        }
        payload["boundaryExclusions"] = list(CONFIG.boundary_exclusions)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--term",
        choices=sorted(TERM_CONFIGS),
        default="OT2023",
    )
    parser.add_argument("--snapshot-date", default=date.today().isoformat())
    parser.add_argument("--output", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--summary-csv", type=Path)
    parser.add_argument("--summary-md", type=Path)
    parser.add_argument(
        "--reconciliation-csv",
        type=Path,
    )
    parser.add_argument(
        "--reconciliation-md",
        type=Path,
    )
    parser.add_argument(
        "--calibration-csv",
        type=Path,
    )
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument(
        "--request-delay",
        type=float,
        default=0.0,
        help="minimum delay before each official-page request in each worker",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        help=(
            "uncommitted official-page cache; defaults under "
            "data/raw/supreme-court-dockets/"
        ),
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="disable reading and writing the uncommitted official-page cache",
    )
    parser.add_argument(
        "--reuse-existing-cohort",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="reuse the current cohort output and fetch only requested refresh rows",
    )
    parser.add_argument(
        "--reuse-journal-detail",
        action=argparse.BooleanOptionalAction,
        default=True,
        help=(
            "reuse same-date official-docket rows from the Journal-detail "
            "extract before fetching missing cohort dockets"
        ),
    )
    parser.add_argument(
        "--refresh-status",
        action="append",
        default=[],
        help=(
            "when reusing the existing cohort, refetch rows with this "
            "certDisposition; may be repeated"
        ),
    )
    parser.add_argument(
        "--allow-failures",
        action="store_true",
        help="write reachable rows and record failures instead of aborting",
    )
    return parser.parse_args()


def main() -> None:
    global CONFIG
    args = parse_args()
    CONFIG = TERM_CONFIGS[args.term]
    output = args.output or CONFIG.default_output
    manifest = args.manifest or CONFIG.default_manifest
    summary_csv = args.summary_csv or CONFIG.default_summary_csv
    summary_md = args.summary_md or CONFIG.default_summary_md
    reconciliation_csv = (
        args.reconciliation_csv or CONFIG.default_reconciliation_csv
    )
    reconciliation_md = (
        args.reconciliation_md or CONFIG.default_reconciliation_md
    )
    calibration_csv = (
        args.calibration_csv or CONFIG.default_calibration_csv
    )
    snapshot_date = date.fromisoformat(args.snapshot_date)
    expected_rows = expected_dockets()
    if args.limit:
        expected_rows = expected_rows[: args.limit]
    workers = max(1, args.workers)
    retries = max(0, args.retries)
    request_delay = max(0.0, args.request_delay)
    cache_dir = (
        None
        if args.no_cache
        else args.cache_dir or CONFIG.default_cache_dir
    )
    (
        coded_rows,
        failures,
        existing_reuse_count,
        journal_reuse_count,
        cache_reuse_count,
        network_fetch_count,
    ) = build_rows(
        expected_rows,
        workers,
        retries,
        args.reuse_journal_detail,
        output if args.reuse_existing_cohort else None,
        set(args.refresh_status),
        cache_dir,
        request_delay,
    )
    if failures and not args.allow_failures:
        raise SystemExit(
            f"Failed to fetch/code {len(failures)} docket pages after retries; "
            f"first failure: {failures[0]}"
        )
    reconciliation = (
        reconciliation_rows(coded_rows)
        if CONFIG.journal_disposition_extract is not None
        else []
    )
    summary = summary_rows(coded_rows, failures, reconciliation)
    calibrations = calibration_rows(coded_rows)
    validate_coded_rows(expected_rows, coded_rows, failures)
    validate_calibration_rows(calibrations)
    write_csv(output, coded_rows, schema_fields())
    write_csv(summary_csv, summary, SUMMARY_FIELDS)
    write_summary_markdown(summary_md, summary, failures)
    if CONFIG.journal_disposition_extract is not None:
        write_csv(
            reconciliation_csv,
            reconciliation,
            RECONCILIATION_FIELDS,
        )
        write_reconciliation_markdown(reconciliation_md, reconciliation)
    write_csv(calibration_csv, calibrations, CALIBRATION_FIELDS)
    write_manifest(
        manifest,
        expected_rows,
        coded_rows,
        failures,
        reconciliation,
        snapshot_date,
        output,
        calibration_csv,
        workers,
        retries,
        existing_reuse_count,
        journal_reuse_count,
        cache_reuse_count,
        network_fetch_count,
        cache_dir,
        request_delay,
    )
    print(f"Wrote {safe_relative(output)} ({len(coded_rows)} rows)")
    print(f"Wrote {safe_relative(manifest)}")
    print(f"Wrote {safe_relative(summary_csv)}")
    print(f"Wrote {safe_relative(summary_md)}")
    if CONFIG.journal_disposition_extract is not None:
        print(f"Wrote {safe_relative(reconciliation_csv)}")
        print(f"Wrote {safe_relative(reconciliation_md)}")
    print(f"Wrote {safe_relative(calibration_csv)}")


if __name__ == "__main__":
    main()
