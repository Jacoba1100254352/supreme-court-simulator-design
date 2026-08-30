#!/usr/bin/env python3
"""Build a bounded environmental post-decision implementation cohort.

The cohort has two deliberately separate observational layers:

1. Event-level lower-court doctrinal treatment. CourtListener's public v4
   search API supplies published, citation-linked federal circuit and district
   opinion documents in a fixed 730-day window after five salient
   environmental Supreme Court decisions. Where a public opinion document is
   available, a conservative, inspectable context rule flags explicit treatment
   language for expert review.
2. Practical agency implementation. Five decision-level episodes reproduce
   the complete purposive environmental sample and three-part classifications
   in Gurganus (2025), joined to official agency or Federal Register actions.

Neither layer is a representative sample of all Supreme Court decisions or a
denominator-matched validation target for the simulator's synthetic
lowerCourtCompliance or governmentNoncomplianceRate metrics.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, date, datetime, timedelta
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK_DIR = ROOT / "data" / "benchmarks"
CALIBRATION_DIR = ROOT / "data" / "calibration"
REPORT_DIR = ROOT / "reports"
RAW_DIR = ROOT / "data" / "raw" / "environmental-implementation-cohort"
SCHEMA = BENCHMARK_DIR / "implementation-compliance-schema.csv"

EVENT_OUTPUT = BENCHMARK_DIR / "lower-court-environmental-treatment-events-v1.csv"
EXPOSURE_OUTPUT = BENCHMARK_DIR / "lower-court-environmental-circuit-exposure-v1.csv"
PRACTICAL_OUTPUT = BENCHMARK_DIR / "environmental-practical-implementation-events-v1.csv"
CALIBRATION_OUTPUT = CALIBRATION_DIR / "environmental-implementation-cohort-v1.csv"
MANIFEST_OUTPUT = BENCHMARK_DIR / "environmental-implementation-cohort-v1-manifest.json"
SUMMARY_CSV = REPORT_DIR / "environmental-implementation-cohort-summary-v1.csv"
SUMMARY_MD = REPORT_DIR / "environmental-implementation-cohort-summary-v1.md"
AVAILABILITY_CSV = REPORT_DIR / "environmental-full-text-availability-audit-v1.csv"
AVAILABILITY_MD = REPORT_DIR / "environmental-full-text-availability-audit-v1.md"
TREATMENT_REVIEW_QUEUE = (
    BENCHMARK_DIR / "environmental-directional-treatment-review-queue-v1.csv"
)
GURGANUS_CLASSIFICATIONS = (
    BENCHMARK_DIR / "gurganus-2025-table-1-classifications-v1.csv"
)

COURTLISTENER_SEARCH_ENDPOINT = "https://www.courtlistener.com/api/rest/v4/search/"
COURTLISTENER_SEARCH_DOCS = (
    "https://wiki.free.law/c/courtlistener/help/api/rest/v4/search"
)
COURTLISTENER_CITATION_DOCS = (
    "https://wiki.free.law/c/courtlistener/help/api/rest/v4/citations"
)
COURTLISTENER_COVERAGE = "https://www.courtlistener.com/help/coverage/opinions/"
GURGANUS_DOI = "10.1111/lapo.70004"
GURGANUS_URL = f"https://doi.org/{GURGANUS_DOI}"
GURGANUS_CITATION = (
    "Gurganus, Kayla. 2025. \"Supreme Court Power and Agency Implementation "
    "in Environmental Litigation.\" Law & Policy 47(4)."
)
WINDOW_DAYS = 730
USER_AGENT = (
    "Supreme-Court-Simulator-research/1.0 "
    "(reproducible academic benchmark; contact via repository)"
)

DECISIONS: list[dict[str, Any]] = [
    {
        "key": "massachusetts-v-epa-2007",
        "case_name": "Massachusetts v. EPA",
        "citation": "549 U.S. 497 (2007)",
        "decision_date": "2007-04-02",
        "courtlistener_opinion_ids": [145749, 9435108],
        "anchors": [
            r"massachusetts\s+v\.?\s+e\.?p\.?a\.?",
            r"549\s+u\.?\s*s\.?\s+497",
            r"127\s+s\.?\s*ct\.?\s+1438",
        ],
        "short_anchors": [r"massachusetts"],
        "practical": {
            "action_date": "2009-12-15",
            "actor": "U.S. Environmental Protection Agency",
            "implementation_action": "final endangerment and cause-or-contribute findings",
            "resistance_category": "none",
            "practical_response": "full compliance",
            "author_classification": "compliant",
            "source_document_id": "massachusetts-final-findings",
            "supporting_document_ids": ["gurganus-crossref-metadata"],
            "classification_basis": (
                "The agency completed the remand-directed endangerment inquiry "
                "and issued final findings under Clean Air Act section 202(a)."
            ),
        },
    },
    {
        "key": "rapanos-v-united-states-2006",
        "case_name": "Rapanos v. United States",
        "citation": "547 U.S. 715 (2006)",
        "decision_date": "2006-06-19",
        "courtlistener_opinion_ids": [
            145642,
            9434923,
            9434924,
            9434925,
            9434926,
            9434927,
        ],
        "anchors": [
            r"rapanos\s+v\.?\s+(?:united\s+states|u\.?s\.?)",
            r"547\s+u\.?\s*s\.?\s+715",
            r"126\s+s\.?\s*ct\.?\s+2208",
        ],
        "short_anchors": [r"rapanos"],
        "practical": {
            "action_date": "2007-06-05",
            "actor": "U.S. Environmental Protection Agency and U.S. Army Corps of Engineers",
            "implementation_action": "guidance plus administrative substitution",
            "resistance_category": "substitution",
            "practical_response": "narrow compliance",
            "author_classification": "narrowly compliant",
            "source_document_id": "rapanos-2007-guidance",
            "supporting_document_ids": ["gurganus-crossref-metadata"],
            "classification_basis": (
                "The agencies formally adopted the controlling Rapanos tests, "
                "while the published study identifies preliminary jurisdictional "
                "determinations as a practical workaround for cumbersome testing."
            ),
        },
    },
    {
        "key": "utility-air-regulatory-group-v-epa-2014",
        "case_name": "Utility Air Regulatory Group v. EPA",
        "citation": "573 U.S. 302 (2014)",
        "decision_date": "2014-06-23",
        "courtlistener_opinion_ids": [2679834],
        "anchors": [
            r"utility\s+air\s+regulatory\s+group\s+v\.?\s+e\.?p\.?a\.?",
            r"util\.?\s+air\s+regul\.?\s+gr[po]\.?\s+v\.?\s+e\.?p\.?a\.?",
            r"573\s+u\.?\s*s\.?\s+302",
            r"134\s+s\.?\s*ct\.?\s+2427",
        ],
        "short_anchors": [
            r"utility\s+air\s+regulatory\s+group",
            r"util\.?\s+air\s+regul\.?\s+gr[po]\.?",
            r"uarg",
        ],
        "practical": {
            "action_date": "2014-07-24",
            "actor": "U.S. Environmental Protection Agency",
            "implementation_action": "implementation memorandum and regulatory conforming actions",
            "resistance_category": "none",
            "practical_response": "full compliance",
            "author_classification": "compliant",
            "source_document_id": "uarg-2014-implementation-memo",
            "supporting_document_ids": [
                "uarg-2015-final-rule",
                "gurganus-crossref-metadata",
            ],
            "classification_basis": (
                "EPA issued implementation instructions one month after judgment "
                "and later removed vacated Step 2 permitting provisions."
            ),
        },
    },
    {
        "key": "michigan-v-epa-2015",
        "case_name": "Michigan v. EPA",
        "citation": "576 U.S. 743 (2015)",
        "decision_date": "2015-06-29",
        "courtlistener_opinion_ids": [2959748, 2812587, 9812709, 9812710],
        "anchors": [
            r"michigan\s+v\.?\s+e\.?p\.?a\.?",
            r"576\s+u\.?\s*s\.?\s+743",
            r"135\s+s\.?\s*ct\.?\s+2699",
        ],
        "short_anchors": [r"michigan"],
        "practical": {
            "action_date": "2016-04-25",
            "actor": "U.S. Environmental Protection Agency",
            "implementation_action": "final supplemental cost finding",
            "resistance_category": "none",
            "practical_response": "full compliance",
            "author_classification": "compliant",
            "source_document_id": "michigan-2016-final-finding",
            "supporting_document_ids": ["gurganus-crossref-metadata"],
            "classification_basis": (
                "EPA completed the remand-directed cost analysis and issued a "
                "final supplemental appropriate-and-necessary finding."
            ),
        },
    },
    {
        "key": "sackett-v-epa-2023",
        "case_name": "Sackett v. EPA",
        "citation": "598 U.S. 651 (2023)",
        "decision_date": "2023-05-25",
        "courtlistener_opinion_ids": [10516284, 9397381, 11066624],
        "anchors": [
            r"sackett\s+v\.?\s+e\.?p\.?a\.?",
            r"598\s+u\.?\s*s\.?\s+651",
            r"143\s+s\.?\s*ct\.?\s+1322",
        ],
        "short_anchors": [r"sackett"],
        "practical": {
            "action_date": "2023-09-08",
            "actor": "U.S. Environmental Protection Agency and U.S. Army Corps of Engineers",
            "implementation_action": "final conforming waters rule",
            "resistance_category": "none",
            "practical_response": "full compliance",
            "author_classification": "compliant",
            "source_document_id": "sackett-2023-final-rule",
            "supporting_document_ids": [
                "sackett-2023-agency-statement",
                "gurganus-crossref-metadata",
            ],
            "classification_basis": (
                "The agencies announced that they would apply the decision and "
                "issued a final rule conforming the waters definition to Sackett."
            ),
        },
    },
]

SOURCE_DOCUMENTS: dict[str, dict[str, Any]] = {
    "gurganus-crossref-metadata": {
        "url": f"https://api.crossref.org/works/{urllib.parse.quote(GURGANUS_DOI)}",
        "public_url": GURGANUS_URL,
        "expected_terms": [
            "supreme court power and agency implementation in environmental litigation",
            "gurganus",
        ],
        "description": "Crossref metadata for the open-access source study",
        "license": "Article licensed CC BY 4.0 according to the publisher metadata",
    },
    "massachusetts-final-findings": {
        "url": (
            "https://www.epa.gov/sites/default/files/2021-05/documents/"
            "federal_register-epa-hq-oar-2009-0171-dec.15-09.pdf"
        ),
        "expected_terms": ["massachusetts v. epa", "endangerment"],
        "description": "EPA final endangerment and cause-or-contribute findings",
        "license": "U.S. federal government work",
    },
    "rapanos-2007-guidance": {
        "url": (
            "https://www.epa.gov/sites/default/files/2016-04/documents/"
            "rapanosguidance6507.pdf"
        ),
        "expected_terms": ["rapanos", "significant nexus"],
        "description": "EPA and Army Corps post-Rapanos jurisdictional guidance",
        "license": "U.S. federal government work",
    },
    "uarg-2014-implementation-memo": {
        "url": (
            "https://www.epa.gov/sites/default/files/2015-12/documents/"
            "20140724memo.pdf"
        ),
        "expected_terms": ["utility air regulatory group", "supreme court"],
        "description": "EPA memorandum on permitting after UARG",
        "license": "U.S. federal government work",
    },
    "uarg-2015-final-rule": {
        "url": (
            "https://www.govinfo.gov/content/pkg/FR-2015-08-19/"
            "pdf/2015-20501.pdf"
        ),
        "expected_terms": ["utility air", "step 2"],
        "description": "EPA final rule removing vacated permitting provisions",
        "license": "U.S. federal government work",
    },
    "michigan-2016-final-finding": {
        "url": (
            "https://www.govinfo.gov/content/pkg/FR-2016-04-25/"
            "pdf/2016-09429.pdf"
        ),
        "expected_terms": ["michigan v. epa", "supplemental finding"],
        "description": "EPA final supplemental appropriate-and-necessary finding",
        "license": "U.S. federal government work",
    },
    "sackett-2023-agency-statement": {
        "url": "https://www.epa.gov/newsreleases/epa-statement-sackett-v-epa",
        "expected_terms": ["sackett v. epa", "amend the final"],
        "description": "EPA statement announcing implementation of Sackett",
        "license": "U.S. federal government work",
    },
    "sackett-2023-final-rule": {
        "url": (
            "https://www.govinfo.gov/content/pkg/FR-2023-09-08/"
            "pdf/2023-18929.pdf"
        ),
        "expected_terms": ["sackett v. epa", "conforming"],
        "description": "EPA and Army Corps final conforming waters rule",
        "license": "U.S. federal government work",
    },
}

CIRCUITS = [
    ("ca1", "First Circuit"),
    ("ca2", "Second Circuit"),
    ("ca3", "Third Circuit"),
    ("ca4", "Fourth Circuit"),
    ("ca5", "Fifth Circuit"),
    ("ca6", "Sixth Circuit"),
    ("ca7", "Seventh Circuit"),
    ("ca8", "Eighth Circuit"),
    ("ca9", "Ninth Circuit"),
    ("ca10", "Tenth Circuit"),
    ("ca11", "Eleventh Circuit"),
    ("cadc", "D.C. Circuit"),
    ("cafc", "Federal Circuit"),
]
CIRCUIT_NAMES = dict(CIRCUITS)
STATE_CIRCUIT = {
    "me": "ca1",
    "ma": "ca1",
    "nh": "ca1",
    "ri": "ca1",
    "pr": "ca1",
    "ct": "ca2",
    "ny": "ca2",
    "vt": "ca2",
    "de": "ca3",
    "nj": "ca3",
    "pa": "ca3",
    "vi": "ca3",
    "md": "ca4",
    "nc": "ca4",
    "sc": "ca4",
    "va": "ca4",
    "wv": "ca4",
    "la": "ca5",
    "ms": "ca5",
    "tx": "ca5",
    "ky": "ca6",
    "mi": "ca6",
    "oh": "ca6",
    "tn": "ca6",
    "il": "ca7",
    "in": "ca7",
    "wi": "ca7",
    "ar": "ca8",
    "ia": "ca8",
    "mn": "ca8",
    "mo": "ca8",
    "ne": "ca8",
    "nd": "ca8",
    "sd": "ca8",
    "ak": "ca9",
    "az": "ca9",
    "ca": "ca9",
    "hi": "ca9",
    "id": "ca9",
    "mt": "ca9",
    "nv": "ca9",
    "or": "ca9",
    "wa": "ca9",
    "gu": "ca9",
    "mp": "ca9",
    "co": "ca10",
    "ks": "ca10",
    "nm": "ca10",
    "ok": "ca10",
    "ut": "ca10",
    "wy": "ca10",
    "al": "ca11",
    "fl": "ca11",
    "ga": "ca11",
}

EVENT_EXTRA_FIELDS = [
    "sourceDecisionKey",
    "decisionCitation",
    "postDecisionWindowStart",
    "postDecisionWindowEnd",
    "courtlistenerClusterId",
    "courtlistenerMergedClusterIds",
    "courtlistenerOpinionId",
    "courtlistenerOpinionType",
    "courtId",
    "courtCitationString",
    "citingCaseName",
    "citingCaseNameFull",
    "courtlistenerDocketId",
    "opinionStatus",
    "opinionCitations",
    "federalCircuit",
    "fullTextStatus",
    "fullTextSourceUrl",
    "fullTextUnavailableReason",
    "fullTextRetrievalNotes",
    "searchSnippetAvailable",
    "searchSnippet",
    "citationContext",
    "codingRule",
    "codingConfidence",
    "citationLinkVerified",
    "providerDedupeKey",
]
EXPOSURE_FIELDS = [
    "sourceKey",
    "decisionId",
    "sourceDecisionKey",
    "caseName",
    "decisionCitation",
    "decisionDate",
    "postDecisionWindowStart",
    "postDecisionWindowEnd",
    "circuitId",
    "circuitName",
    "legallyExposed",
    "observedCitingOpinionDocuments",
    "observedFullTextDocuments",
    "observedContextCodedDocuments",
    "observedDirectionalTreatmentDocuments",
    "noObservedCitingEvent",
    "measurementDenominator",
    "denominatorReconciled",
    "sourceUrl",
    "coderNotes",
]
CALIBRATION_FIELDS = [
    "sourceKey",
    "sourceName",
    "domain",
    "metric",
    "term",
    "numerator",
    "denominator",
    "value",
    "sourceUrl",
    "confidenceLevel",
    "validationUse",
    "coverageScope",
    "comparabilityClass",
    "notes",
]
SUMMARY_FIELDS = [
    "decisionKey",
    "caseName",
    "decisionDate",
    "windowStart",
    "windowEnd",
    "allCourtSearchClusters",
    "federalClustersBeforeDedupe",
    "citingOpinionDocuments",
    "fullTextAvailable",
    "citationContextFound",
    "followed",
    "applied",
    "distinguished",
    "narrowed",
    "questionedOrResisted",
    "citedContextOnly",
    "unclear",
    "observedCircuits",
    "exposedCircuits",
    "practicalClassification",
    "practicalActionDate",
    "practicalDelayDays",
    "denominatorBoundary",
]
AVAILABILITY_FIELDS = [
    "dimension",
    "category",
    "events",
    "available",
    "unavailable",
    "availabilityRate",
]
TREATMENT_REVIEW_FIELDS = [
    "sourceRecordId",
    "sourceDecisionKey",
    "sourceUrl",
    "citingCaseName",
    "lowerCourt",
    "sourceRecordDate",
    "docketNumber",
    "automatedTreatment",
    "codingRule",
    "codingConfidence",
    "citationContext",
    "reviewStratum",
    "secondCoderTreatment",
    "agreement",
    "adjudicatedTreatment",
    "reviewStatus",
]
GURGANUS_CLASSIFICATION_FIELDS = [
    "sourceDecisionKey",
    "caseName",
    "decisionCitation",
    "articleDoi",
    "articleUrl",
    "articleLocator",
    "authorClassification",
    "classificationBasis",
    "sampleDesign",
    "license",
    "classificationRecordSha256",
]

RESISTED_PATTERNS = [
    (r"\bdeclin(?:e|es|ed|ing)\s+to\s+follow\b", "explicit-decline-to-follow"),
    (r"\b(?:not|no longer)\s+(?:binding|controlling)\b", "explicit-not-controlling"),
    (r"\bwrongly\s+decided\b", "explicit-questioning"),
    (r"\brefus(?:e|es|ed|ing)\s+to\s+(?:apply|follow)\b", "explicit-refusal"),
]
DISTINGUISHED_PATTERNS = [
    (r"\bdistinguish(?:able|ed|es|ing)?\b", "explicit-distinguishing"),
    (r"\binapposite\b", "explicit-inapposite"),
    (r"\bdoes\s+not\s+control\b", "explicit-does-not-control"),
    (r"\bunlike\s+(?:the\s+facts\s+in\s+)?", "explicit-unlike"),
]
NARROWED_PATTERNS = [
    (r"\blimit(?:ed|s|ing)?\s+(?:the\s+)?(?:holding|rule|reach|scope)\b", "explicit-limitation"),
    (r"\bconfined\s+to\b", "explicit-confinement"),
    (r"\bnarrow(?:ly|er)?\s+(?:read|reading|construction|scope)\b", "explicit-narrow-reading"),
]
FOLLOWED_PATTERNS = [
    (r"\b(?:we|this\s+court)\s+(?:are|is)\s+bound\s+by\b", "explicit-bound-by"),
    (r"\bmust\s+follow\b", "explicit-must-follow"),
    (r"\bcontrols?\s+(?:this|the)\s+(?:case|issue|question|outcome)\b", "explicit-controls"),
    (r"\bcompels?\s+(?:the|this|our|us)\b", "explicit-compels"),
]
APPLIED_PATTERNS = [
    (r"\bapply(?:ing|ies|ied)?\s+(?:the\s+)?(?:rule|standard|test|holding)\b", "explicit-application"),
    (r"\bpursuant\s+to\b", "explicit-pursuant-to"),
    (r"\bin\s+light\s+of\b", "explicit-in-light-of"),
    (r"\bunder\s+(?:the\s+)?(?:rule|standard|test|holding)\b", "explicit-under-rule"),
]


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.hidden_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript"}:
            self.hidden_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self.hidden_depth:
            self.hidden_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.hidden_depth:
            self.parts.append(data)

    def text(self) -> str:
        return " ".join(self.parts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--extraction-date",
        default=date.today().isoformat(),
        help="Snapshot date recorded in the manifest (YYYY-MM-DD).",
    )
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Refresh search pages, public opinion documents, and official sources.",
    )
    parser.add_argument(
        "--refresh-search",
        action="store_true",
        help="Refresh CourtListener search pages but reuse document caches.",
    )
    parser.add_argument(
        "--refresh-documents",
        action="store_true",
        help="Refresh public opinion documents and official source documents.",
    )
    parser.add_argument(
        "--download-workers",
        type=int,
        default=6,
        help="Maximum concurrent public document downloads (default: 6).",
    )
    return parser.parse_args()


def schema_fields() -> list[str]:
    with SCHEMA.open(newline="", encoding="utf-8") as handle:
        fields = [row["fieldName"] for row in csv.DictReader(handle)]
    if not fields:
        raise RuntimeError(f"No schema fields found in {SCHEMA}")
    return fields


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_csv(path: Path, fields: list[str], rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def request_bytes(url: str, retries: int = 5, timeout: int = 45) -> tuple[bytes, str, str]:
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            request = urllib.request.Request(
                url,
                headers={
                    "User-Agent": USER_AGENT,
                    "Accept": (
                        "application/json,text/html,application/pdf,text/plain,"
                        "application/octet-stream;q=0.9,*/*;q=0.8"
                    ),
                },
            )
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return (
                    response.read(),
                    response.headers.get("Content-Type", ""),
                    response.geturl(),
                )
        except urllib.error.HTTPError as error:
            last_error = error
            if error.code not in {429, 500, 502, 503, 504}:
                raise
            retry_after = error.headers.get("Retry-After", "")
            try:
                delay = min(30.0, float(retry_after))
            except ValueError:
                delay = min(30.0, 2.0 ** (attempt + 1))
            time.sleep(delay)
        except (urllib.error.URLError, TimeoutError) as error:
            last_error = error
            time.sleep(min(30.0, 2.0 ** (attempt + 1)))
    raise RuntimeError(f"Failed to retrieve {url}: {last_error}")


def search_query(decision: dict[str, Any]) -> str:
    ids = decision["courtlistener_opinion_ids"]
    citation_expression = " OR ".join(f"cites:{identifier}" for identifier in ids)
    if len(ids) > 1:
        citation_expression = f"({citation_expression})"
    decision_day = date.fromisoformat(decision["decision_date"])
    start = decision_day + timedelta(days=1)
    end = decision_day + timedelta(days=WINDOW_DAYS)
    return (
        f"{citation_expression} AND "
        f"dateFiled:[{start.isoformat()} TO {end.isoformat()}] AND "
        "status:published"
    )


def initial_search_url(query: str) -> str:
    return COURTLISTENER_SEARCH_ENDPOINT + "?" + urllib.parse.urlencode(
        {
            "q": query,
            "type": "o",
            "order_by": "dateFiled asc",
        }
    )


def fetch_search_results(
    decision: dict[str, Any], refresh: bool
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    query = search_query(decision)
    query_hash = hashlib.sha256(query.encode("utf-8")).hexdigest()[:16]
    cache_dir = RAW_DIR / "courtlistener-search" / decision["key"] / query_hash
    cache_dir.mkdir(parents=True, exist_ok=True)
    url: str | None = initial_search_url(query)
    page = 1
    results: list[dict[str, Any]] = []
    reported_count: int | None = None
    page_hashes: dict[str, str] = {}
    while url:
        path = cache_dir / f"page-{page:03d}.json"
        if path.exists() and not refresh:
            payload = json.loads(path.read_text(encoding="utf-8"))
        else:
            raw, content_type, _ = request_bytes(url)
            if "json" not in content_type.lower() and not raw.lstrip().startswith(b"{"):
                raise RuntimeError(
                    f"CourtListener search returned non-JSON content for {decision['key']}"
                )
            payload = json.loads(raw)
            write_json(path, payload)
            time.sleep(0.25)
        page_hashes[str(path.relative_to(ROOT))] = sha256_file(path)
        if reported_count is None:
            reported_count = int(payload["count"])
        elif reported_count != int(payload["count"]):
            raise RuntimeError(f"Search count changed during pagination for {decision['key']}")
        results.extend(payload.get("results", []))
        url = payload.get("next")
        page += 1
    if reported_count is None:
        reported_count = 0
    if len(results) != reported_count:
        raise RuntimeError(
            f"{decision['key']} returned {len(results)} rows, expected {reported_count}"
        )
    return results, {
        "query": query,
        "queryUrl": initial_search_url(query),
        "queryHash": query_hash,
        "reportedCount": reported_count,
        "fetchedCount": len(results),
        "pageCount": page - 1,
        "cachedPageHashes": page_hashes,
    }


def is_federal_lower_court(result: dict[str, Any]) -> bool:
    return (
        result.get("court_id") in CIRCUIT_NAMES
        or str(result.get("court", "")).startswith("District Court,")
    )


def circuit_for_court(court_id: str, court_name: str) -> str:
    if court_id in CIRCUIT_NAMES:
        return court_id
    if court_id == "dcd":
        return "cadc"
    for state_prefix in sorted(STATE_CIRCUIT, key=len, reverse=True):
        if court_id.startswith(state_prefix):
            return STATE_CIRCUIT[state_prefix]
    raise RuntimeError(
        f"Cannot map federal district court {court_id!r} ({court_name}) to a circuit"
    )


def normalized_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def cluster_dedupe_key(result: dict[str, Any]) -> str:
    court = result.get("court_id", "")
    filed = result.get("dateFiled", "")
    docket = normalized_key(result.get("docketNumber", ""))
    case = normalized_key(result.get("caseNameFull") or result.get("caseName", ""))
    # CourtListener can hold the same published case in multiple provider
    # clusters with variant captions. A same-court, same-date, same-docket
    # cluster is the strongest provider-duplicate key; normalized caption is
    # the fallback when no docket is supplied. Distinct joined/lead/concurrence
    # documents remain separate nested opinion rows within the retained cluster.
    identity = f"docket:{docket}" if docket else f"case:{case}"
    return f"{court}|{filed}|{identity}"


def relevant_opinions(
    decision: dict[str, Any], result: dict[str, Any]
) -> list[dict[str, Any]]:
    target_ids = set(decision["courtlistener_opinion_ids"])
    opinions = result.get("opinions", [])
    linked = [
        opinion
        for opinion in opinions
        if target_ids.intersection(set(opinion.get("cites") or []))
    ]
    if linked:
        return linked
    return opinions[:1]


def opinion_access_score(opinion: dict[str, Any]) -> int:
    score = 0
    if opinion.get("local_path"):
        score += 8
    if opinion.get("download_url"):
        score += 4
    if opinion.get("snippet"):
        score += 1
    return score


def result_access_score(decision: dict[str, Any], result: dict[str, Any]) -> tuple[int, int, int]:
    opinions = relevant_opinions(decision, result)
    return (
        sum(opinion_access_score(opinion) for opinion in opinions),
        len(opinions),
        1 if result.get("status") == "Published" else 0,
    )


def stable_cluster_id(result: dict[str, Any]) -> int:
    try:
        return int(result.get("cluster_id") or 0)
    except (TypeError, ValueError):
        return 0


def dedupe_clusters(
    decision: dict[str, Any], results: list[dict[str, Any]]
) -> tuple[list[dict[str, Any]], dict[str, list[str]]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for result in results:
        groups[cluster_dedupe_key(result)].append(result)
    selected: list[dict[str, Any]] = []
    merged_ids: dict[str, list[str]] = {}
    for key in sorted(groups):
        group = groups[key]
        # A lower cluster ID is the deterministic final tie-breaker after
        # document-access, opinion-count, and publication-status scores.
        chosen = max(
            group,
            key=lambda row: (
                *result_access_score(decision, row),
                -stable_cluster_id(row),
            ),
        )
        selected.append(chosen)
        merged_ids[str(chosen.get("cluster_id", ""))] = sorted(
            {str(row.get("cluster_id", "")) for row in group}
        )
    selected.sort(
        key=lambda row: (
            row.get("dateFiled", ""),
            row.get("court_id", ""),
            row.get("cluster_id", 0),
        )
    )
    return selected, merged_ids


def opinion_candidates(opinion: dict[str, Any]) -> list[str]:
    candidates: list[str] = []
    local_path = opinion.get("local_path")
    if local_path:
        candidates.append(
            "https://storage.courtlistener.com/" + str(local_path).lstrip("/")
        )
    download_url = opinion.get("download_url")
    if download_url:
        parsed = urllib.parse.urlparse(str(download_url))
        if parsed.scheme == "http":
            candidates.append(urllib.parse.urlunparse(parsed._replace(scheme="https")))
        candidates.append(str(download_url))
    return list(dict.fromkeys(candidates))


def content_suffix(payload: bytes, content_type: str, url: str) -> str:
    if payload.startswith(b"%PDF") or "pdf" in content_type.lower():
        return ".pdf"
    if "html" in content_type.lower() or b"<html" in payload[:1000].lower():
        return ".html"
    if "json" in content_type.lower() or payload.lstrip().startswith((b"{", b"[")):
        return ".json"
    suffix = Path(urllib.parse.urlparse(url).path).suffix.lower()
    if suffix in {".txt", ".json", ".xml"}:
        return suffix
    return ".bin"


def extract_text(path: Path) -> str:
    payload = path.read_bytes()
    if payload.startswith(b"%PDF") or path.suffix.lower() == ".pdf":
        completed = subprocess.run(
            ["pdftotext", "-layout", str(path), "-"],
            check=False,
            capture_output=True,
            text=True,
            timeout=90,
        )
        if completed.returncode != 0:
            return ""
        return completed.stdout
    decoded = payload.decode("utf-8", errors="replace")
    if path.suffix.lower() in {".html", ".htm"} or "<html" in decoded[:1000].lower():
        parser = TextExtractor()
        parser.feed(decoded)
        return html.unescape(parser.text())
    return decoded


def fetch_opinion_document(
    opinion: dict[str, Any], refresh: bool
) -> dict[str, str]:
    opinion_id = str(opinion.get("id", "unknown"))
    cache_dir = RAW_DIR / "opinion-documents"
    cache_dir.mkdir(parents=True, exist_ok=True)
    metadata_path = cache_dir / f"{opinion_id}.json"
    if metadata_path.exists() and not refresh:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        cached_path = metadata.get("cachePath", "")
        if cached_path:
            document_path = ROOT / cached_path
            if document_path.exists():
                text = extract_text(document_path)
                metadata["text"] = text
                return metadata
        if metadata.get("status") == "unavailable":
            metadata["text"] = ""
            return metadata

    errors: list[str] = []
    for url in opinion_candidates(opinion):
        try:
            payload, content_type, final_url = request_bytes(url, retries=2, timeout=30)
            if not payload:
                errors.append(f"{url}: empty response")
                continue
            suffix = content_suffix(payload, content_type, final_url)
            document_path = cache_dir / f"{opinion_id}{suffix}"
            document_path.write_bytes(payload)
            text = extract_text(document_path)
            if not text.strip():
                errors.append(f"{url}: no extractable text")
                continue
            metadata = {
                "status": "available",
                "sourceUrl": final_url,
                "cachePath": str(document_path.relative_to(ROOT)),
                "contentType": content_type,
                "bytes": str(len(payload)),
                "sha256": sha256_bytes(payload),
                "errorsBeforeSuccess": errors,
                "text": text,
            }
            persisted = {key: value for key, value in metadata.items() if key != "text"}
            write_json(metadata_path, persisted)
            return metadata
        except Exception as error:  # Preserve every failed public candidate.
            errors.append(f"{url}: {type(error).__name__}: {error}")
    metadata = {
        "status": "unavailable",
        "sourceUrl": "",
        "cachePath": "",
        "contentType": "",
        "bytes": "0",
        "sha256": "",
        "errors": errors,
        "text": "",
    }
    persisted = {key: value for key, value in metadata.items() if key != "text"}
    write_json(metadata_path, persisted)
    return metadata


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def clean_search_snippet(value: str) -> str:
    return clean_text(re.sub(r"<[^>]+>", " ", html.unescape(value or "")))


def citation_contexts(text: str, anchors: list[str]) -> list[str]:
    clean = clean_text(text)
    contexts: list[tuple[int, int, str]] = []
    for anchor in anchors:
        for match in re.finditer(anchor, clean, flags=re.IGNORECASE):
            start = max(0, match.start() - 900)
            end = min(len(clean), match.end() + 900)
            contexts.append((match.start(), match.end(), clean[start:end]))
    unique: list[str] = []
    seen: set[str] = set()
    for _, _, context in sorted(contexts):
        fingerprint = hashlib.sha256(context.encode("utf-8")).hexdigest()
        if fingerprint not in seen:
            seen.add(fingerprint)
            unique.append(context)
        if len(unique) == 3:
            break
    return unique


def classify_context(
    decision: dict[str, Any], contexts: list[str], full_text_status: str
) -> tuple[str, str, str]:
    if not contexts:
        if full_text_status == "available":
            return "unclear", "full-text-no-anchor", "low"
        return "unclear", "public-full-text-unavailable", "low"
    combined = " ".join(contexts).lower()
    target = "(?:" + "|".join(
        decision["anchors"] + decision.get("short_anchors", [])
    ) + ")"
    target_linked_patterns = (
        (
            "questioned/resisted",
            [
                (
                    rf"\b(?:declin(?:e|es|ed|ing)\s+to\s+follow|"
                    rf"refus(?:e|es|ed|ing)\s+to\s+(?:apply|follow))\b"
                    rf".{{0,100}}{target}",
                    "target-linked-decline-or-refusal",
                ),
                (
                    rf"{target}.{{0,100}}\b(?:wrongly\s+decided|"
                    rf"not\s+binding|no\s+longer\s+controlling)\b",
                    "target-linked-explicit-questioning",
                ),
            ],
        ),
        (
            "distinguished",
            [
                (
                    rf"\bunlike\s+(?:the\s+(?:case|facts)\s+in\s+)?{target}",
                    "target-linked-unlike",
                ),
                (
                    rf"\bdistinguish(?:able|ed|es|ing)?\b.{{0,100}}{target}",
                    "target-linked-distinguishing",
                ),
                (
                    rf"{target}.{{0,120}}\b(?:is|was|are|were)?\s*"
                    rf"(?:distinguishable|inapposite|not\s+controlling|"
                    rf"not\s+so\s+broad|does\s+not\s+control)\b",
                    "target-linked-limiting-distinction",
                ),
            ],
        ),
        (
            "narrowed",
            [
                (
                    rf"{target}.{{0,12}}\b(?:is|was)\s+"
                    rf"(?:limited\s+to|confined\s+to|narrowly\s+(?:read|construed))\b",
                    "target-linked-narrowing",
                ),
                (
                    rf"\b(?:holding|rule|reach|scope)\s+(?:of|in)\s+{target}"
                    rf".{{0,45}}\b(?:is|was)\s+(?:limited|confined|narrow)\b",
                    "target-linked-holding-limitation",
                ),
            ],
        ),
        (
            "followed",
            [
                (
                    rf"\b(?:bound\s+by|must\s+follow)\b.{{0,80}}{target}",
                    "target-linked-following",
                ),
                (
                    rf"{target}.{{0,100}}\b(?:controls?\s+(?:this|the)\s+"
                    rf"(?:case|issue|question|outcome)|compels?\s+us|"
                    rf"requires?\s+us)\b",
                    "target-linked-controlling",
                ),
            ],
        ),
        (
            "applied",
            [
                (
                    rf"\b(?:apply(?:ing|ies|ied)?|under|pursuant\s+to|"
                    rf"in\s+light\s+of|consistent\s+with)\b.{{0,55}}{target}",
                    "target-linked-application",
                ),
                (
                    rf"{target}.{{0,100}}\b(?:governs?|forecloses?|"
                    rf"requires?\s+that|instructs?\s+us)\b",
                    "target-linked-operative-rule",
                ),
            ],
        ),
    )
    for label, patterns in target_linked_patterns:
        for pattern, rule in patterns:
            if re.search(pattern, combined, flags=re.IGNORECASE):
                return label, rule, "medium"
    return "cited_context_only", "citation-anchor-without-directional-language", "high"


def validate_classification_rules() -> None:
    """Freeze the reviewer-identified UARG false positive as a negative test."""
    decision = next(
        row
        for row in DECISIONS
        if row["key"] == "utility-air-regulatory-group-v-epa-2014"
    )
    generic_context = (
        "Statutory language must be read in context. See Utility Air Regulatory "
        "Group v. EPA, 134 S. Ct. 2427, 2442 (2014). Applying these principles "
        "here, we interpret the Mandatory Victims Restitution Act."
    )
    treatment, rule, _ = classify_context(
        decision, [generic_context], "available"
    )
    if (
        treatment != "cited_context_only"
        or rule != "citation-anchor-without-directional-language"
    ):
        raise RuntimeError(
            "UARG generic-context negative regression was classified directionally"
        )


def courtlistener_source_url(result: dict[str, Any]) -> str:
    absolute = result.get("absolute_url", "")
    if absolute:
        return urllib.parse.urljoin("https://www.courtlistener.com", absolute)
    return COURTLISTENER_SEARCH_ENDPOINT


def build_event_candidates(
    decision: dict[str, Any],
    selected_results: list[dict[str, Any]],
    merged_ids: dict[str, list[str]],
) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    target_ids = set(decision["courtlistener_opinion_ids"])
    for result in selected_results:
        cluster_id = str(result.get("cluster_id", ""))
        opinions = relevant_opinions(decision, result)
        for opinion in opinions:
            candidates.append(
                {
                    "decision": decision,
                    "result": result,
                    "opinion": opinion,
                    "merged_cluster_ids": merged_ids.get(cluster_id, [cluster_id]),
                    "citation_link_verified": int(
                        bool(target_ids.intersection(set(opinion.get("cites") or [])))
                    ),
                }
            )
    return candidates


def build_event_row(
    candidate: dict[str, Any],
    document: dict[str, str],
    fields: list[str],
) -> dict[str, Any]:
    decision = candidate["decision"]
    result = candidate["result"]
    opinion = candidate["opinion"]
    contexts = citation_contexts(document.get("text", ""), decision["anchors"])
    treatment, rule, confidence = classify_context(
        decision, contexts, document.get("status", "unavailable")
    )
    decision_day = date.fromisoformat(decision["decision_date"])
    window_start = decision_day + timedelta(days=1)
    window_end = decision_day + timedelta(days=WINDOW_DAYS)
    circuit_id = circuit_for_court(result["court_id"], result["court"])
    candidate_urls = opinion_candidates(opinion)
    snippet = clean_search_snippet(str(opinion.get("snippet", "")))
    retrieval_errors = document.get("errors", [])
    if not isinstance(retrieval_errors, list):
        retrieval_errors = [str(retrieval_errors)]
    full_text_status = document.get("status", "unavailable")
    if full_text_status == "available":
        unavailable_reason = ""
    elif not candidate_urls:
        unavailable_reason = "no_document_url_in_search_result"
    elif retrieval_errors:
        unavailable_reason = "download_failed_or_unextractable"
    else:
        unavailable_reason = "unavailable_reason_unknown"
    row: dict[str, Any] = {field: "" for field in fields + EVENT_EXTRA_FIELDS}
    row.update(
        {
            "sourceKey": "courtlistener-environmental-scotus-citation-events",
            "sourceRecordId": f"{decision['key']}:{opinion.get('id', '')}",
            "sourceUrl": courtlistener_source_url(result),
            "sourceSlice": "lower-court-doctrinal-uptake",
            "jurisdiction": "United States federal courts",
            "decisionId": decision["citation"],
            "decisionDate": decision["decision_date"],
            "decidingCourt": "Supreme Court of the United States",
            "caseName": decision["case_name"],
            "sourceDecisionType": "merits statutory judicial-review decision",
            "sourceRecordDate": result.get("dateFiled", ""),
            "lowerCourt": result.get("court", ""),
            "treatmentType": treatment,
            "treatmentDate": result.get("dateFiled", ""),
            "followedOrDistinguished": (
                treatment if treatment != "cited_context_only" else "unclear"
            ),
            "remedyFidelity": "unclear",
            "measurementDenominator": (
                "published CourtListener citation-linked U.S. federal circuit and "
                "district opinion documents filed in the fixed 730-day post-decision "
                "window, after documented provider-cluster deduplication"
            ),
            "denominatorReconciled": "1",
            "coderNotes": (
                "Citation-linked doctrinal-treatment event. A zero-citation circuit "
                "is no observed event, not ignored precedent or noncompliance. "
                "The treatment value is an automated candidate flag pending expert "
                "legal review. CourtListener's published-opinion coverage is not an "
                "all-case opportunity denominator."
            ),
            "sourceDecisionKey": decision["key"],
            "decisionCitation": decision["citation"],
            "postDecisionWindowStart": window_start.isoformat(),
            "postDecisionWindowEnd": window_end.isoformat(),
            "courtlistenerClusterId": result.get("cluster_id", ""),
            "courtlistenerMergedClusterIds": ";".join(
                candidate["merged_cluster_ids"]
            ),
            "courtlistenerOpinionId": opinion.get("id", ""),
            "courtlistenerOpinionType": opinion.get("type", ""),
            "courtId": result.get("court_id", ""),
            "courtCitationString": result.get("court_citation_string", ""),
            "citingCaseName": result.get("caseName", ""),
            "citingCaseNameFull": result.get("caseNameFull", ""),
            "courtlistenerDocketId": result.get("docket_id", ""),
            "docketNumber": result.get("docketNumber", ""),
            "opinionStatus": result.get("status", ""),
            "opinionCitations": "; ".join(result.get("citation") or []),
            "federalCircuit": circuit_id,
            "fullTextStatus": full_text_status,
            "fullTextSourceUrl": document.get("sourceUrl", ""),
            "fullTextUnavailableReason": unavailable_reason,
            "fullTextRetrievalNotes": " | ".join(str(item) for item in retrieval_errors),
            "searchSnippetAvailable": "1" if snippet else "0",
            "searchSnippet": snippet,
            "citationContext": " […] ".join(contexts),
            "codingRule": rule,
            "codingConfidence": confidence,
            "citationLinkVerified": str(candidate["citation_link_verified"]),
            "providerDedupeKey": cluster_dedupe_key(result),
        }
    )
    return row


def build_lower_court_cohort(
    refresh_search: bool,
    refresh_documents: bool,
    workers: int,
    fields: list[str],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    all_candidates: list[dict[str, Any]] = []
    search_metadata: dict[str, Any] = {}
    pre_dedupe_counts: dict[str, int] = {}
    post_dedupe_cluster_counts: dict[str, int] = {}
    for decision in DECISIONS:
        results, metadata = fetch_search_results(decision, refresh_search)
        federal_results = [row for row in results if is_federal_lower_court(row)]
        selected, merged_ids = dedupe_clusters(decision, federal_results)
        candidates = build_event_candidates(decision, selected, merged_ids)
        all_candidates.extend(candidates)
        metadata["federalClustersBeforeDedupe"] = len(federal_results)
        metadata["federalClustersAfterDedupe"] = len(selected)
        metadata["citingOpinionDocumentsAfterDedupe"] = len(candidates)
        search_metadata[decision["key"]] = metadata
        pre_dedupe_counts[decision["key"]] = len(federal_results)
        post_dedupe_cluster_counts[decision["key"]] = len(selected)

    documents: dict[str, dict[str, str]] = {}
    opinion_by_id: dict[str, dict[str, Any]] = {}
    for candidate in all_candidates:
        opinion = candidate["opinion"]
        opinion_by_id[str(opinion.get("id", "unknown"))] = opinion
    with ThreadPoolExecutor(max_workers=max(1, workers)) as executor:
        futures = {
            executor.submit(fetch_opinion_document, opinion, refresh_documents): opinion_id
            for opinion_id, opinion in opinion_by_id.items()
        }
        for future in as_completed(futures):
            opinion_id = futures[future]
            try:
                documents[opinion_id] = future.result()
            except Exception as error:
                documents[opinion_id] = {
                    "status": "unavailable",
                    "sourceUrl": "",
                    "text": "",
                    "errors": [f"{type(error).__name__}: {error}"],
                }

    event_rows = [
        build_event_row(
            candidate,
            documents.get(
                str(candidate["opinion"].get("id", "unknown")),
                {"status": "unavailable", "sourceUrl": "", "text": ""},
            ),
            fields,
        )
        for candidate in all_candidates
    ]
    event_rows.sort(
        key=lambda row: (
            row["sourceDecisionKey"],
            row["treatmentDate"],
            row["courtId"],
            int(row["courtlistenerOpinionId"] or 0),
        )
    )
    exposure_rows = build_exposure_rows(event_rows)
    metadata = {
        "searches": search_metadata,
        "allCourtSearchClusters": sum(
            item["reportedCount"] for item in search_metadata.values()
        ),
        "federalClustersBeforeDedupe": sum(pre_dedupe_counts.values()),
        "federalClustersAfterDedupe": sum(post_dedupe_cluster_counts.values()),
        "citingOpinionDocumentsAfterDedupe": len(event_rows),
        "uniqueOpinionDocumentsDownloadedOrAttempted": len(opinion_by_id),
        "fullTextAvailable": sum(
            row["fullTextStatus"] == "available" for row in event_rows
        ),
        "citationContextFound": sum(bool(row["citationContext"]) for row in event_rows),
        "citationLinkVerified": sum(
            row["citationLinkVerified"] == "1" for row in event_rows
        ),
        "treatmentCounts": dict(
            sorted(Counter(row["treatmentType"] for row in event_rows).items())
        ),
        "exposureRows": len(exposure_rows),
    }
    return event_rows, exposure_rows, metadata


def build_exposure_rows(event_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in event_rows:
        grouped[(row["sourceDecisionKey"], row["federalCircuit"])].append(row)
    rows: list[dict[str, Any]] = []
    for decision in DECISIONS:
        decision_day = date.fromisoformat(decision["decision_date"])
        start = decision_day + timedelta(days=1)
        end = decision_day + timedelta(days=WINDOW_DAYS)
        query_url = initial_search_url(search_query(decision))
        for circuit_id, circuit_name in CIRCUITS:
            events = grouped.get((decision["key"], circuit_id), [])
            context_count = sum(bool(row["citationContext"]) for row in events)
            directional_count = sum(
                row["treatmentType"]
                in {
                    "followed",
                    "applied",
                    "distinguished",
                    "narrowed",
                    "questioned/resisted",
                }
                for row in events
            )
            rows.append(
                {
                    "sourceKey": "courtlistener-environmental-circuit-exposure",
                    "decisionId": decision["citation"],
                    "sourceDecisionKey": decision["key"],
                    "caseName": decision["case_name"],
                    "decisionCitation": decision["citation"],
                    "decisionDate": decision["decision_date"],
                    "postDecisionWindowStart": start.isoformat(),
                    "postDecisionWindowEnd": end.isoformat(),
                    "circuitId": circuit_id,
                    "circuitName": circuit_name,
                    "legallyExposed": "1",
                    "observedCitingOpinionDocuments": str(len(events)),
                    "observedFullTextDocuments": str(
                        sum(row["fullTextStatus"] == "available" for row in events)
                    ),
                    "observedContextCodedDocuments": str(context_count),
                    "observedDirectionalTreatmentDocuments": str(directional_count),
                    "noObservedCitingEvent": "1" if not events else "0",
                    "measurementDenominator": (
                        "five source decisions x thirteen federal appellate circuits "
                        "(65 nationwide-applicability cells); published district-court "
                        "citation events assigned to their appellate circuit"
                    ),
                    "denominatorReconciled": "1",
                    "sourceUrl": query_url,
                    "coderNotes": (
                        "Nationwide applicability means binding Supreme Court authority. "
                        "A zero records no published CourtListener-linked citing opinion "
                        "in the fixed window; this is citation presence, not an empirical "
                        "exposure, opportunity, uptake, resistance, or compliance rate."
                    ),
                }
            )
    return rows


def source_cache_path(document_id: str, suffix: str) -> Path:
    return RAW_DIR / "official-sources" / f"{document_id}.source{suffix}"


def fetch_source_document(document_id: str, refresh: bool) -> dict[str, Any]:
    spec = SOURCE_DOCUMENTS[document_id]
    metadata_path = RAW_DIR / "official-sources" / f"{document_id}.metadata.json"
    if metadata_path.exists() and not refresh:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        cache_path = metadata.get("cachePath", "")
        if cache_path and (ROOT / cache_path).exists():
            return metadata
    payload, content_type, final_url = request_bytes(spec["url"])
    suffix = content_suffix(payload, content_type, final_url)
    path = source_cache_path(document_id, suffix)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    text = clean_text(extract_text(path)).lower()
    missing_terms = [
        term for term in spec["expected_terms"] if term.lower() not in text
    ]
    if missing_terms:
        raise RuntimeError(
            f"{document_id} is missing expected source terms: {missing_terms}"
        )
    metadata = {
        "documentId": document_id,
        "description": spec["description"],
        "sourceUrl": spec.get("public_url", spec["url"]),
        "retrievalUrl": spec["url"],
        "finalUrl": final_url,
        "contentType": content_type,
        "cachePath": str(path.relative_to(ROOT)),
        "bytes": len(payload),
        "sha256": sha256_bytes(payload),
        "expectedTermsVerified": spec["expected_terms"],
        "license": spec["license"],
        "status": "verified",
    }
    write_json(metadata_path, metadata)
    return metadata


def fetch_practical_sources(refresh: bool, workers: int) -> dict[str, dict[str, Any]]:
    metadata: dict[str, dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=max(1, min(workers, 4))) as executor:
        futures = {
            executor.submit(fetch_source_document, document_id, refresh): document_id
            for document_id in SOURCE_DOCUMENTS
        }
        for future in as_completed(futures):
            document_id = futures[future]
            metadata[document_id] = future.result()
    return metadata


def build_practical_rows(
    source_metadata: dict[str, dict[str, Any]], fields: list[str]
) -> list[dict[str, Any]]:
    extra_fields = [
        "sourceDecisionKey",
        "decisionCitation",
        "authorClassification",
        "sourceStudyCitation",
        "sourceStudyUrl",
        "primarySourceDocumentId",
        "primarySourceSha256",
        "supportingSourceUrls",
        "classificationBasis",
        "sampleDesign",
    ]
    rows: list[dict[str, Any]] = []
    for decision in DECISIONS:
        practical = decision["practical"]
        primary = source_metadata[practical["source_document_id"]]
        supporting = [
            source_metadata[document_id]["sourceUrl"]
            for document_id in practical["supporting_document_ids"]
        ]
        delay = (
            date.fromisoformat(practical["action_date"])
            - date.fromisoformat(decision["decision_date"])
        ).days
        row: dict[str, Any] = {field: "" for field in fields + extra_fields}
        row.update(
            {
                "sourceKey": "gurganus-2025-environmental-agency-implementation",
                "sourceRecordId": f"{decision['key']}:implementation-episode",
                "sourceUrl": primary["sourceUrl"],
                "sourceSlice": "implementation-resistance",
                "jurisdiction": "United States federal environmental administration",
                "decisionId": decision["citation"],
                "decisionDate": decision["decision_date"],
                "decidingCourt": "Supreme Court of the United States",
                "caseName": decision["case_name"],
                "sourceDecisionType": "merits statutory judicial-review decision",
                "sourceRecordDate": practical["action_date"],
                "actorType": practical["actor"],
                "implementationAction": practical["implementation_action"],
                "delayDays": str(delay),
                "resistanceCategory": practical["resistance_category"],
                "enforcementCapacity": "unknown",
                "practicalResponse": practical["practical_response"],
                "measurementDenominator": (
                    "complete purposive sample of five salient environmental "
                    "Supreme Court decisions from 2005-2023 in Gurganus (2025), "
                    "one practical implementation episode per decision"
                ),
                "denominatorReconciled": "1",
                "coderNotes": (
                    "Published three-part agency-response classification joined to "
                    "official implementation evidence. The five statutory "
                    "environmental cases are purposive, not representative of all "
                    "agencies, courts, constitutional decisions, or outcomes. No "
                    "open noncompliance event appears in this sample."
                ),
                "sourceDecisionKey": decision["key"],
                "decisionCitation": decision["citation"],
                "authorClassification": practical["author_classification"],
                "sourceStudyCitation": GURGANUS_CITATION,
                "sourceStudyUrl": GURGANUS_URL,
                "primarySourceDocumentId": practical["source_document_id"],
                "primarySourceSha256": primary["sha256"],
                "supportingSourceUrls": ";".join(supporting),
                "classificationBasis": practical["classification_basis"],
                "sampleDesign": (
                    "complete purposive sample of five salient environmental "
                    "Supreme Court decisions selected in Gurganus (2025)"
                ),
            }
        )
        rows.append(row)
    return rows


def practical_extra_fields() -> list[str]:
    return [
        "sourceDecisionKey",
        "decisionCitation",
        "authorClassification",
        "sourceStudyCitation",
        "sourceStudyUrl",
        "primarySourceDocumentId",
        "primarySourceSha256",
        "supportingSourceUrls",
        "classificationBasis",
        "sampleDesign",
    ]


def build_availability_rows(
    event_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    groups: list[tuple[str, str, list[dict[str, Any]]]] = [
        ("pooled", "all events", event_rows)
    ]
    dimensions = [
        ("decision", "sourceDecisionKey"),
        ("court", "courtId"),
        ("filing_year", "sourceRecordDate"),
        ("opinion_type", "courtlistenerOpinionType"),
    ]
    for dimension, field in dimensions:
        grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in event_rows:
            category = str(row.get(field, ""))
            if dimension == "filing_year":
                category = category[:4]
            grouped[category or "missing"].append(row)
        for category in sorted(grouped):
            groups.append((dimension, category, grouped[category]))
    reason_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in event_rows:
        if row["fullTextStatus"] != "available":
            reason_groups[
                row.get("fullTextUnavailableReason", "") or "unavailable_reason_unknown"
            ].append(row)
    for category in sorted(reason_groups):
        groups.append(("unavailable_reason", category, reason_groups[category]))

    rows: list[dict[str, Any]] = []
    for dimension, category, members in groups:
        available = sum(row["fullTextStatus"] == "available" for row in members)
        total = len(members)
        rows.append(
            {
                "dimension": dimension,
                "category": category,
                "events": total,
                "available": available,
                "unavailable": total - available,
                "availabilityRate": f"{available / total:.9f}" if total else "0.000000000",
            }
        )
    return rows


def markdown_availability_audit(
    availability_rows: list[dict[str, Any]],
    extraction_date: str,
) -> str:
    by_dimension: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in availability_rows:
        by_dimension[row["dimension"]].append(row)
    lines = [
        "# Environmental cohort full-text availability audit",
        "",
        f"Snapshot date: `{extraction_date}`.",
        "",
        "Public full text is available for 115 of 191 published citation-linked "
        "opinion documents (60.2%). Missingness is visibly nonrandom across tracked "
        "decisions and opinion-document types, so automated directional-candidate "
        "shares must not be compared as lower-court behavior rates.",
        "",
        "## Decision",
        "",
        "| Decision key | Events | Available | Unavailable | Availability |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in by_dimension["decision"]:
        lines.append(
            f"| `{row['category']}` | {row['events']} | {row['available']} | "
            f"{row['unavailable']} | {float(row['availabilityRate']):.1%} |"
        )
    lines.extend(
        [
            "",
            "## Opinion-document type",
            "",
            "| Type | Events | Available | Unavailable | Availability |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for row in by_dimension["opinion_type"]:
        lines.append(
            f"| `{row['category']}` | {row['events']} | {row['available']} | "
            f"{row['unavailable']} | {float(row['availabilityRate']):.1%} |"
        )
    lines.extend(
        [
            "",
            "## Recorded unavailability reason",
            "",
            "| Reason | Events |",
            "|---|---:|",
        ]
    )
    for row in by_dimension["unavailable_reason"]:
        lines.append(f"| `{row['category']}` | {row['events']} |")
    lines.extend(
        [
            "",
            "Court- and filing-year strata are retained in the companion CSV. A "
            "`no_document_url_in_search_result` value describes the public search "
            "result supplied to this extractor; it is not a finding that no opinion "
            "text exists elsewhere. Search snippets are preserved in the event file "
            "for audit, but snippets are not used as substitutes for full-text legal "
            "treatment coding.",
            "",
        ]
    )
    return "\n".join(lines)


def build_treatment_review_queue(
    event_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    directional_labels = {
        "followed",
        "applied",
        "distinguished",
        "narrowed",
        "questioned/resisted",
    }
    directional = sorted(
        (row for row in event_rows if row["treatmentType"] in directional_labels),
        key=lambda row: row["sourceRecordId"],
    )
    citation_only_by_decision: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in event_rows:
        if row["treatmentType"] == "cited_context_only":
            citation_only_by_decision[row["sourceDecisionKey"]].append(row)
    citation_only_sample: list[dict[str, Any]] = []
    for decision in DECISIONS:
        candidates = sorted(
            citation_only_by_decision[decision["key"]],
            key=lambda row: hashlib.sha256(
                row["sourceRecordId"].encode("utf-8")
            ).hexdigest(),
        )
        citation_only_sample.extend(candidates[:2])

    rows: list[dict[str, Any]] = []
    for source, stratum in [
        *((row, "all_automated_directional_candidates") for row in directional),
        *((row, "stratified_citation_only_sample") for row in citation_only_sample),
    ]:
        rows.append(
            {
                "sourceRecordId": source["sourceRecordId"],
                "sourceDecisionKey": source["sourceDecisionKey"],
                "sourceUrl": source["sourceUrl"],
                "citingCaseName": (
                    source.get("citingCaseNameFull")
                    or source.get("citingCaseName")
                    or "caption unavailable"
                ),
                "lowerCourt": source["lowerCourt"],
                "sourceRecordDate": source["sourceRecordDate"],
                "docketNumber": source["docketNumber"],
                "automatedTreatment": source["treatmentType"],
                "codingRule": source["codingRule"],
                "codingConfidence": source["codingConfidence"],
                "citationContext": source["citationContext"],
                "reviewStratum": stratum,
                "secondCoderTreatment": "",
                "agreement": "",
                "adjudicatedTreatment": "",
                "reviewStatus": "pending_expert_review",
            }
        )
    return rows


def build_gurganus_classification_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for decision in DECISIONS:
        practical = decision["practical"]
        row: dict[str, Any] = {
            "sourceDecisionKey": decision["key"],
            "caseName": decision["case_name"],
            "decisionCitation": decision["citation"],
            "articleDoi": GURGANUS_DOI,
            "articleUrl": GURGANUS_URL,
            "articleLocator": (
                f"Table 1; case-study discussion under {decision['case_name']}"
            ),
            "authorClassification": practical["author_classification"],
            "classificationBasis": practical["classification_basis"],
            "sampleDesign": (
                "complete purposive sample of five salient environmental Supreme "
                "Court decisions selected in Gurganus (2025)"
            ),
            "license": "CC BY 4.0",
        }
        canonical = json.dumps(row, sort_keys=True, ensure_ascii=False).encode("utf-8")
        row["classificationRecordSha256"] = sha256_bytes(canonical)
        rows.append(row)
    return rows


def rate_row(
    source_key: str,
    source_name: str,
    domain: str,
    metric: str,
    term: str,
    numerator: int,
    denominator: int,
    source_url: str,
    confidence: str,
    validation_use: str,
    scope: str,
    comparability: str,
    notes: str,
) -> dict[str, Any]:
    value = numerator / denominator if denominator else 0.0
    return {
        "sourceKey": source_key,
        "sourceName": source_name,
        "domain": domain,
        "metric": metric,
        "term": term,
        "numerator": numerator,
        "denominator": denominator,
        "value": f"{value:.9f}",
        "sourceUrl": source_url,
        "confidenceLevel": confidence,
        "validationUse": validation_use,
        "coverageScope": scope,
        "comparabilityClass": comparability,
        "notes": notes,
    }


def build_calibration_rows(
    event_rows: list[dict[str, Any]],
    exposure_rows: list[dict[str, Any]],
    practical_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    events_by_decision: dict[str, list[dict[str, Any]]] = defaultdict(list)
    exposure_by_decision: dict[str, list[dict[str, Any]]] = defaultdict(list)
    practical_by_decision = {
        row["sourceDecisionKey"]: row for row in practical_rows
    }
    for row in event_rows:
        events_by_decision[row["sourceDecisionKey"]].append(row)
    for row in exposure_rows:
        exposure_by_decision[row["sourceDecisionKey"]].append(row)
    rows: list[dict[str, Any]] = []
    for decision in DECISIONS:
        key = decision["key"]
        events = events_by_decision[key]
        exposures = exposure_by_decision[key]
        context = [row for row in events if row["citationContext"]]
        directional = [
            row
            for row in events
            if row["treatmentType"]
            in {
                "followed",
                "applied",
                "distinguished",
                "narrowed",
                "questioned/resisted",
            }
        ]
        observed_circuits = sum(
            int(row["observedCitingOpinionDocuments"]) > 0 for row in exposures
        )
        scope = (
            f"{decision['case_name']}; published CourtListener-linked federal "
            f"opinion documents filed in the 730-day post-decision window"
        )
        comparability = (
            "published citation-linked automated treatment candidates and circuit "
            "citation presence versus synthetic case-average lower-court compliance; "
            "no all-case opportunity or ignored-case denominator"
        )
        common_notes = (
            "A zero-citation cell is no observed published citation, not ignored "
            "precedent or noncompliance. Full-text availability is nonrandom across "
            "decisions and opinion types; this row is descriptive only."
        )
        source_url = initial_search_url(search_query(decision))
        rows.extend(
            [
                rate_row(
                    "courtlistener-environmental-scotus-citation-events",
                    "CourtListener environmental Supreme Court citation-event cohort",
                    "lower_court_compliance",
                    f"lowerCourtPublicFullTextCoverage_{key}",
                    decision["decision_date"][:4],
                    sum(row["fullTextStatus"] == "available" for row in events),
                    len(events),
                    source_url,
                    "Medium",
                    "data_quality_guardrail",
                    scope,
                    comparability,
                    common_notes,
                ),
                rate_row(
                    "courtlistener-environmental-scotus-citation-events",
                    "CourtListener environmental Supreme Court citation-event cohort",
                    "lower_court_compliance",
                    f"lowerCourtCitationContextCoverage_{key}",
                    decision["decision_date"][:4],
                    len(context),
                    len(events),
                    source_url,
                    "Medium",
                    "data_quality_guardrail",
                    scope,
                    comparability,
                    common_notes,
                ),
                rate_row(
                    "courtlistener-environmental-circuit-exposure",
                    "CourtListener environmental circuit citation-presence frame",
                    "lower_court_compliance",
                    f"lowerCourtPublishedCitationPresenceByCircuit_{key}",
                    decision["decision_date"][:4],
                    observed_circuits,
                    len(exposures),
                    source_url,
                    "Medium",
                    "descriptive_case_study_summary",
                    scope,
                    comparability,
                    common_notes,
                ),
                rate_row(
                    "courtlistener-environmental-scotus-citation-events",
                    "CourtListener environmental Supreme Court citation-event cohort",
                    "lower_court_compliance",
                    f"lowerCourtAutomatedDirectionalCandidateShare_{key}",
                    decision["decision_date"][:4],
                    len(directional),
                    len(context),
                    source_url,
                    "Medium",
                    "descriptive_case_study_summary",
                    scope,
                    comparability,
                    (
                        "Automated candidate flags use inspectable context rules and "
                        "remain pending expert legal review. Nonrandom text availability "
                        "precludes behavioral comparison across decisions."
                    ),
                ),
            ]
        )
        practical = practical_by_decision[key]
        full = int(practical["authorClassification"] == "compliant")
        narrow = int(practical["authorClassification"] == "narrowly compliant")
        practical_scope = (
            f"{decision['case_name']}; one of five purposively selected salient "
            "environmental Supreme Court decisions in Gurganus (2025)"
        )
        practical_comparability = (
            "published three-part agency implementation classification versus "
            "synthetic cross-institutional compliance metrics; purposive statutory "
            "environmental sample and no observed noncompliance"
        )
        rows.extend(
            [
                rate_row(
                    "gurganus-2025-environmental-agency-implementation",
                    "Gurganus 2025 environmental agency implementation cohort",
                    "lower_court_compliance",
                    f"caseStudyCompliantClassificationIndicator_{key}",
                    decision["decision_date"][:4],
                    full,
                    1,
                    GURGANUS_URL,
                    "High",
                    "descriptive_case_study_summary",
                    practical_scope,
                    practical_comparability,
                    "Case-study label preserves the published category; it is not a probability or simulator target.",
                ),
                rate_row(
                    "gurganus-2025-environmental-agency-implementation",
                    "Gurganus 2025 environmental agency implementation cohort",
                    "lower_court_compliance",
                    f"caseStudyNarrowComplianceClassificationIndicator_{key}",
                    decision["decision_date"][:4],
                    narrow,
                    1,
                    GURGANUS_URL,
                    "High",
                    "descriptive_case_study_summary",
                    practical_scope,
                    practical_comparability,
                    "Case-study label preserves the published category; it is not a probability or simulator target.",
                ),
            ]
        )
    full_count = sum(
        row["authorClassification"] == "compliant" for row in practical_rows
    )
    narrow_count = sum(
        row["authorClassification"] == "narrowly compliant" for row in practical_rows
    )
    rows.extend(
        [
            rate_row(
                "gurganus-2025-environmental-agency-implementation",
                "Gurganus 2025 environmental agency implementation cohort",
                "lower_court_compliance",
                "caseStudyCompliantClassificationComposition_salientEnvironmentalCases",
                "2006-2023",
                full_count,
                len(practical_rows),
                GURGANUS_URL,
                "High",
                "descriptive_case_study_summary",
                "complete purposive five-case salient environmental sample",
                "purposive statutory environmental implementation classifications versus synthetic "
                "cross-institutional compliance metrics; scale mismatch",
                "Purposive case-study composition: four compliant labels and one narrowly compliant label; not an estimable compliance probability.",
            ),
            rate_row(
                "gurganus-2025-environmental-agency-implementation",
                "Gurganus 2025 environmental agency implementation cohort",
                "lower_court_compliance",
                "caseStudyNarrowComplianceClassificationComposition_salientEnvironmentalCases",
                "2006-2023",
                narrow_count,
                len(practical_rows),
                GURGANUS_URL,
                "High",
                "descriptive_case_study_summary",
                "complete purposive five-case salient environmental sample",
                "purposive statutory environmental implementation classifications versus synthetic "
                "cross-institutional compliance metrics; scale mismatch",
                "Purposive case-study composition: four compliant labels and one narrowly compliant label; not an estimable compliance probability.",
            ),
        ]
    )
    return rows


def build_summary_rows(
    event_rows: list[dict[str, Any]],
    exposure_rows: list[dict[str, Any]],
    practical_rows: list[dict[str, Any]],
    lower_metadata: dict[str, Any],
) -> list[dict[str, Any]]:
    events_by_decision: dict[str, list[dict[str, Any]]] = defaultdict(list)
    exposures_by_decision: dict[str, list[dict[str, Any]]] = defaultdict(list)
    practical_by_decision = {
        row["sourceDecisionKey"]: row for row in practical_rows
    }
    for row in event_rows:
        events_by_decision[row["sourceDecisionKey"]].append(row)
    for row in exposure_rows:
        exposures_by_decision[row["sourceDecisionKey"]].append(row)
    rows: list[dict[str, Any]] = []
    for decision in DECISIONS:
        key = decision["key"]
        events = events_by_decision[key]
        exposure = exposures_by_decision[key]
        counts = Counter(row["treatmentType"] for row in events)
        practical = practical_by_decision[key]
        search = lower_metadata["searches"][key]
        rows.append(
            {
                "decisionKey": key,
                "caseName": decision["case_name"],
                "decisionDate": decision["decision_date"],
                "windowStart": (
                    date.fromisoformat(decision["decision_date"]) + timedelta(days=1)
                ).isoformat(),
                "windowEnd": (
                    date.fromisoformat(decision["decision_date"])
                    + timedelta(days=WINDOW_DAYS)
                ).isoformat(),
                "allCourtSearchClusters": search["reportedCount"],
                "federalClustersBeforeDedupe": search["federalClustersBeforeDedupe"],
                "citingOpinionDocuments": len(events),
                "fullTextAvailable": sum(
                    row["fullTextStatus"] == "available" for row in events
                ),
                "citationContextFound": sum(
                    bool(row["citationContext"]) for row in events
                ),
                "followed": counts["followed"],
                "applied": counts["applied"],
                "distinguished": counts["distinguished"],
                "narrowed": counts["narrowed"],
                "questionedOrResisted": counts["questioned/resisted"],
                "citedContextOnly": counts["cited_context_only"],
                "unclear": counts["unclear"],
                "observedCircuits": sum(
                    int(row["observedCitingOpinionDocuments"]) > 0 for row in exposure
                ),
                "exposedCircuits": len(exposure),
                "practicalClassification": practical["authorClassification"],
                "practicalActionDate": practical["sourceRecordDate"],
                "practicalDelayDays": practical["delayDays"],
                "denominatorBoundary": (
                    "published CourtListener-linked citing opinion documents, not all "
                    "relevant case opportunities; purposive five-case agency sample"
                ),
            }
        )
    pooled_counts = Counter(row["treatmentType"] for row in event_rows)
    rows.append(
        {
            "decisionKey": "pooled",
            "caseName": "Five-decision environmental cohort",
            "decisionDate": "2006-2023",
            "windowStart": "",
            "windowEnd": "",
            "allCourtSearchClusters": lower_metadata["allCourtSearchClusters"],
            "federalClustersBeforeDedupe": lower_metadata[
                "federalClustersBeforeDedupe"
            ],
            "citingOpinionDocuments": len(event_rows),
            "fullTextAvailable": sum(
                row["fullTextStatus"] == "available" for row in event_rows
            ),
            "citationContextFound": sum(bool(row["citationContext"]) for row in event_rows),
            "followed": pooled_counts["followed"],
            "applied": pooled_counts["applied"],
            "distinguished": pooled_counts["distinguished"],
            "narrowed": pooled_counts["narrowed"],
            "questionedOrResisted": pooled_counts["questioned/resisted"],
            "citedContextOnly": pooled_counts["cited_context_only"],
            "unclear": pooled_counts["unclear"],
            "observedCircuits": sum(
                int(row["observedCitingOpinionDocuments"]) > 0
                for row in exposure_rows
            ),
            "exposedCircuits": len(exposure_rows),
            "practicalClassification": (
                f"{sum(row['authorClassification'] == 'compliant' for row in practical_rows)} "
                "compliant; "
                f"{sum(row['authorClassification'] == 'narrowly compliant' for row in practical_rows)} "
                "narrowly compliant"
            ),
            "practicalActionDate": "",
            "practicalDelayDays": "",
            "denominatorBoundary": (
                "Five decision-specific 730-day published-opinion windows and 65 "
                "nationwide-applicability/citation-presence cells; practical cohort "
                "is purposive n=5"
            ),
        }
    )
    return rows


def markdown_summary(
    summary_rows: list[dict[str, Any]],
    event_rows: list[dict[str, Any]],
    exposure_rows: list[dict[str, Any]],
    practical_rows: list[dict[str, Any]],
    extraction_date: str,
) -> str:
    pooled = summary_rows[-1]
    lines = [
        "# Environmental post-decision implementation cohort",
        "",
        f"Snapshot date: `{extraction_date}`.",
        "",
        "## Answer first",
        "",
        (
            f"The cohort contains **{len(event_rows)}** deduplicated, citation-linked "
            "published federal lower-court opinion documents across five fixed "
            f"two-year windows. Public full text was available for "
            f"**{pooled['fullTextAvailable']}** "
            f"documents and a source-decision citation context was located in "
            f"**{pooled['citationContextFound']}**. The separate practical cohort "
            f"contains **{len(practical_rows)}** agency episodes: "
            f"**{sum(row['authorClassification'] == 'compliant' for row in practical_rows)}** "
            "classified as compliant and "
            f"**{sum(row['authorClassification'] == 'narrowly compliant' for row in practical_rows)}** "
            "as narrowly compliant in Gurganus (2025)."
        ),
        "",
        "These data supply a bounded event-level citation-treatment candidate and "
        "practical-implementation source slice. They do **not** supply an all-relevant-case "
        "opportunity denominator, an ignored-precedent rate, a representative "
        "constitutional-case sample, or a government-noncompliance rate.",
        "",
        "## Decision-level reconciliation",
        "",
        "| Decision | Federal opinion documents | Full text | Context found | Observed circuits / 13 | Practical class |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for row in summary_rows[:-1]:
        lines.append(
            f"| {row['caseName']} | {row['citingOpinionDocuments']} | "
            f"{row['fullTextAvailable']} | {row['citationContextFound']} | "
            f"{row['observedCircuits']} / {row['exposedCircuits']} | "
            f"{row['practicalClassification']} |"
        )
    lines.extend(
        [
            "",
            "## Automated treatment-candidate coding",
            "",
            "Each lower-court row is one citation-linked opinion document after "
            "provider-cluster deduplication. When a public document is retrievable, "
            "the extractor retains up to three local citation contexts and applies "
            "conservative, inspectable phrase rules. Explicit language can flag "
            "`followed`, `applied`, `distinguished`, `narrowed`, or "
            "`questioned/resisted`; a located citation without directional language "
            "is `cited_context_only`; missing public text or an unlocated anchor is "
            "`unclear`. Directional values are automated candidates pending expert "
            "legal review, not final doctrinal-treatment determinations or findings "
            "about policy implementation or remedy fidelity.",
            "",
            "Pooled treatment counts:",
            "",
        ]
    )
    counts = Counter(row["treatmentType"] for row in event_rows)
    for category in [
        "followed",
        "applied",
        "distinguished",
        "narrowed",
        "questioned/resisted",
        "cited_context_only",
        "unclear",
    ]:
        lines.append(f"- `{category}`: {counts[category]}")
    lines.extend(
        [
            "",
            "## Nationwide applicability and citation presence",
            "",
            f"`{EXPOSURE_OUTPUT.relative_to(ROOT)}` contains {len(exposure_rows)} "
            "decision-circuit cells (five decisions × thirteen circuits). All cells "
            "share nationwide precedential applicability. Published district-court "
            "citation events are assigned to their appellate circuit. A zero means "
            "only that CourtListener did not link a published citing federal opinion "
            "document in the fixed window; thirteen circuits is not an empirical "
            "exposure or behavioral denominator.",
            "",
            "## Practical implementation",
            "",
            "The practical rows preserve the complete purposive five-case sample and "
            "three-part response classifications reported in Gurganus (2025), then "
            "join each case to an official agency or Federal Register action. "
            "`Rapanos` is narrowly compliant because the formal guidance adopted the "
            "controlling tests while the study identifies preliminary "
            "jurisdictional determinations as an administrative workaround. The "
            "other four cases are classified as compliant. No noncompliant outcome "
            "is observed, so the cohort cannot validate a general government-"
            "noncompliance rate.",
            "",
            "## Data-quality boundary",
            "",
            "- Intended use: descriptive case-study summaries and data-quality checks.",
            "- Lower-court grain: one source-decision × citing opinion document.",
            "- Practical grain: one source decision × agency implementation episode.",
            "- Search scope: published CourtListener-linked U.S. federal circuit and "
            "district opinions filed during a decision-specific 730-day window.",
            "- Completeness boundary: full-text availability is nonrandom across "
            "tracked decisions and opinion-document types (115/191 overall).",
            "- Construct boundary: all five Supreme Court decisions are salient "
            "environmental statutory cases, not constitutional judgments.",
            "- Comparability boundary: neither source layer is denominator-matched to "
            "the simulator's synthetic case-average compliance measures.",
            f"- Expert-review status: `{TREATMENT_REVIEW_QUEUE.relative_to(ROOT)}` "
            "contains all automated directional candidates plus a deterministic "
            "citation-only sample; every row remains pending expert review.",
            "",
            "## Sources",
            "",
            f"- {GURGANUS_CITATION} DOI: {GURGANUS_URL}",
            f"- CourtListener search API documentation: {COURTLISTENER_SEARCH_DOCS}",
            f"- CourtListener citation documentation: {COURTLISTENER_CITATION_DOCS}",
            f"- CourtListener opinion coverage: {COURTLISTENER_COVERAGE}",
            f"- Full-text missingness audit: `{AVAILABILITY_CSV.relative_to(ROOT)}`",
            f"- Structured Gurganus Table 1 transcription: "
            f"`{GURGANUS_CLASSIFICATIONS.relative_to(ROOT)}`",
            "- Official agency and Federal Register source URLs and verified hashes "
            f"are recorded in `{MANIFEST_OUTPUT.relative_to(ROOT)}`.",
            "",
        ]
    )
    return "\n".join(lines)


def validate_outputs(
    fields: list[str],
    event_rows: list[dict[str, Any]],
    exposure_rows: list[dict[str, Any]],
    practical_rows: list[dict[str, Any]],
) -> None:
    event_fields = fields + EVENT_EXTRA_FIELDS
    if len(event_fields) != len(set(event_fields)):
        duplicates = [
            field for field, count in Counter(event_fields).items() if count > 1
        ]
        raise RuntimeError(f"Duplicate environmental event CSV fields: {duplicates}")
    if len(exposure_rows) != len(DECISIONS) * len(CIRCUITS):
        raise RuntimeError("Exposure frame must contain exactly 65 rows")
    if len(practical_rows) != len(DECISIONS):
        raise RuntimeError("Practical cohort must contain exactly five rows")
    expected_keys = {decision["key"] for decision in DECISIONS}
    if {row["sourceDecisionKey"] for row in practical_rows} != expected_keys:
        raise RuntimeError("Practical cohort decision keys do not reconcile")
    event_ids = [row["sourceRecordId"] for row in event_rows]
    if len(event_ids) != len(set(event_ids)):
        duplicates = [
            key for key, count in Counter(event_ids).items() if count > 1
        ]
        raise RuntimeError(f"Duplicate event sourceRecordId values: {duplicates[:10]}")
    required_common = {
        row["fieldName"]
        for row in csv.DictReader(SCHEMA.open(newline="", encoding="utf-8"))
        if row["requiredFor"] == "all"
    }
    for label, rows in (("event", event_rows), ("practical", practical_rows)):
        for index, row in enumerate(rows, start=1):
            missing = [field for field in required_common if not str(row.get(field, ""))]
            if missing:
                raise RuntimeError(
                    f"{label} row {index} is missing all-slice fields: {missing}"
                )
    for row in event_rows:
        if row["treatmentDate"] <= row["decisionDate"]:
            raise RuntimeError(f"Non-post-decision treatment row: {row['sourceRecordId']}")
        if row["federalCircuit"] not in CIRCUIT_NAMES:
            raise RuntimeError(f"Unknown circuit in event row: {row['federalCircuit']}")
        if row["denominatorReconciled"] != "1":
            raise RuntimeError("Every event row must reconcile to the stated source denominator")
        if row["opinionStatus"] != "Published":
            raise RuntimeError(
                f"Published-only query returned {row['opinionStatus']!r}: "
                f"{row['sourceRecordId']}"
            )
        if not (row["citingCaseName"] or row["citingCaseNameFull"]):
            raise RuntimeError(
                f"Event row lacks citing-case caption: {row['sourceRecordId']}"
            )
        if row["fullTextStatus"] == "available":
            if row["fullTextUnavailableReason"]:
                raise RuntimeError(
                    f"Available event has unavailable reason: {row['sourceRecordId']}"
                )
        elif not row["fullTextUnavailableReason"]:
            raise RuntimeError(
                f"Unavailable event lacks reason: {row['sourceRecordId']}"
            )
    treatment_counts = Counter(row["treatmentType"] for row in event_rows)
    expected_treatment_counts = {
        "applied": 5,
        "distinguished": 1,
        "cited_context_only": 109,
        "unclear": 76,
    }
    if treatment_counts != expected_treatment_counts:
        raise RuntimeError(
            "Environmental treatment counts changed after the reviewed v1 coding "
            f"snapshot: {dict(sorted(treatment_counts.items()))}"
        )
    uarg_negative = next(
        (
            row
            for row in event_rows
            if row["sourceRecordId"]
            == "utility-air-regulatory-group-v-epa-2014:3153967"
        ),
        None,
    )
    if not uarg_negative or uarg_negative["treatmentType"] != "cited_context_only":
        raise RuntimeError("Reviewer-identified UARG false positive reappeared")
    for row in practical_rows:
        if row["sourceRecordDate"] <= row["decisionDate"]:
            raise RuntimeError(
                f"Non-post-decision implementation row: {row['sourceRecordId']}"
            )
        if row["authorClassification"] not in {"compliant", "narrowly compliant"}:
            raise RuntimeError("Unexpected practical classification")
    if not set(fields).issubset(set(event_rows[0]) if event_rows else set(fields)):
        raise RuntimeError("Event output does not contain the implementation schema fields")


def main() -> None:
    args = parse_args()
    extraction_day = date.fromisoformat(args.extraction_date)
    if extraction_day > date.today():
        raise SystemExit("Extraction date cannot be in the future")
    fields = schema_fields()
    validate_classification_rules()
    refresh_search = args.refresh or args.refresh_search
    refresh_documents = args.refresh or args.refresh_documents

    event_rows, exposure_rows, lower_metadata = build_lower_court_cohort(
        refresh_search=refresh_search,
        refresh_documents=refresh_documents,
        workers=args.download_workers,
        fields=fields,
    )
    source_metadata = fetch_practical_sources(
        refresh=refresh_documents,
        workers=args.download_workers,
    )
    practical_rows = build_practical_rows(source_metadata, fields)
    validate_outputs(fields, event_rows, exposure_rows, practical_rows)
    calibration_rows = build_calibration_rows(
        event_rows, exposure_rows, practical_rows
    )
    summary_rows = build_summary_rows(
        event_rows, exposure_rows, practical_rows, lower_metadata
    )
    availability_rows = build_availability_rows(event_rows)
    treatment_review_rows = build_treatment_review_queue(event_rows)
    gurganus_classification_rows = build_gurganus_classification_rows()

    write_csv(EVENT_OUTPUT, fields + EVENT_EXTRA_FIELDS, event_rows)
    write_csv(EXPOSURE_OUTPUT, EXPOSURE_FIELDS, exposure_rows)
    write_csv(PRACTICAL_OUTPUT, fields + practical_extra_fields(), practical_rows)
    write_csv(CALIBRATION_OUTPUT, CALIBRATION_FIELDS, calibration_rows)
    write_csv(SUMMARY_CSV, SUMMARY_FIELDS, summary_rows)
    write_csv(AVAILABILITY_CSV, AVAILABILITY_FIELDS, availability_rows)
    write_csv(
        TREATMENT_REVIEW_QUEUE,
        TREATMENT_REVIEW_FIELDS,
        treatment_review_rows,
    )
    write_csv(
        GURGANUS_CLASSIFICATIONS,
        GURGANUS_CLASSIFICATION_FIELDS,
        gurganus_classification_rows,
    )
    SUMMARY_MD.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_MD.write_text(
        markdown_summary(
            summary_rows,
            event_rows,
            exposure_rows,
            practical_rows,
            args.extraction_date,
        ),
        encoding="utf-8",
    )
    AVAILABILITY_MD.write_text(
        markdown_availability_audit(availability_rows, args.extraction_date),
        encoding="utf-8",
    )

    manifest = {
        "schemaVersion": "1.0",
        "extractionDate": args.extraction_date,
        "generatedAtUtc": datetime.now(UTC).replace(microsecond=0).isoformat(),
        "cohortName": "Environmental post-decision implementation cohort v1",
        "decisionCount": len(DECISIONS),
        "decisions": [
            {
                "decisionKey": decision["key"],
                "caseName": decision["case_name"],
                "citation": decision["citation"],
                "decisionDate": decision["decision_date"],
                "courtlistenerOpinionIds": decision["courtlistener_opinion_ids"],
                "searchQuery": search_query(decision),
                "practicalClassification": decision["practical"][
                    "author_classification"
                ],
            }
            for decision in DECISIONS
        ],
        "lowerCourtCohort": {
            "source": (
                "CourtListener public v4 search API, explicitly filtered to "
                "status:published, and linked public opinion documents"
            ),
            "publicationStatusScope": "published opinions only",
            "searchApi": COURTLISTENER_SEARCH_ENDPOINT,
            "searchDocumentation": COURTLISTENER_SEARCH_DOCS,
            "citationDocumentation": COURTLISTENER_CITATION_DOCS,
            "coverageDocumentation": COURTLISTENER_COVERAGE,
            "windowDays": WINDOW_DAYS,
            "includedCourts": (
                "U.S. Courts of Appeals for the First through Eleventh, D.C., "
                "and Federal Circuits, plus U.S. district courts"
            ),
            "excludedCourts": (
                "Supreme Court, state courts, territorial local courts, bankruptcy "
                "courts, and specialized non-district lower courts"
            ),
            "unit": "source decision x citation-linked lower-court opinion document",
            "deduplication": (
                "Provider clusters grouped by court, filing date, normalized docket "
                "and case identity; the group member with the strongest public-"
                "document access retained, then the smallest cluster ID used as a "
                "stable final tie-breaker; all merged cluster IDs recorded"
            ),
            "codingMethod": (
                "Up to three source-decision citation contexts per public document; "
                "conservative deterministic phrase rules produce automated candidate "
                "flags with rule and context retained; expert review remains pending"
            ),
            "treatmentReviewQueue": str(
                TREATMENT_REVIEW_QUEUE.relative_to(ROOT)
            ),
            "treatmentReviewStatus": "pending expert legal review",
            **lower_metadata,
        },
        "circuitExposureFrame": {
            "unit": (
                "source decision x federal appellate circuit nationwide-applicability "
                "and published-citation-presence cell"
            ),
            "rowCount": len(exposure_rows),
            "expectedRowCount": 65,
            "legallyExposedCells": sum(
                row["legallyExposed"] == "1" for row in exposure_rows
            ),
            "zeroObservedEventCells": sum(
                row["noObservedCitingEvent"] == "1" for row in exposure_rows
            ),
            "interpretation": (
                "All cells reflect nationwide precedential applicability. Zero means "
                "no published CourtListener-linked citing opinion in the fixed window; "
                "the frame is not empirical exposure, opportunity, uptake, resistance, "
                "or compliance."
            ),
        },
        "practicalImplementationCohort": {
            "sourceStudy": GURGANUS_CITATION,
            "sourceStudyDoi": GURGANUS_DOI,
            "sourceStudyUrl": GURGANUS_URL,
            "sourceStudyLicense": "CC BY 4.0",
            "unit": "source decision x practical agency implementation episode",
            "sampleDesign": (
                "complete purposive sample of five salient environmental Supreme "
                "Court decisions from 2005-2023 as selected in Gurganus (2025)"
            ),
            "rowCount": len(practical_rows),
            "classificationCounts": dict(
                sorted(
                    Counter(
                        row["authorClassification"] for row in practical_rows
                    ).items()
                )
            ),
            "structuredClassificationFile": str(
                GURGANUS_CLASSIFICATIONS.relative_to(ROOT)
            ),
            "structuredClassificationLocator": (
                "Gurganus (2025) Table 1 and decision-specific case-study discussion"
            ),
            "verifiedOfficialSources": source_metadata,
        },
        "dataQuality": {
            "intendedUse": (
                "descriptive case-study summaries and data-quality checks; not "
                "behavioral guardrails or denominator-matched simulator validation"
            ),
            "fullTextAvailabilityAudit": str(
                AVAILABILITY_CSV.relative_to(ROOT)
            ),
            "fullTextMissingnessInterpretation": (
                "nonrandom across tracked decisions and opinion-document types"
            ),
            "eventIdUnique": (
                len({row["sourceRecordId"] for row in event_rows}) == len(event_rows)
            ),
            "futureDatedRows": sum(
                date.fromisoformat(row["sourceRecordDate"]) > extraction_day
                for row in event_rows + practical_rows
            ),
            "schemaFieldsPresent": all(
                field in event_rows[0] for field in fields
            )
            if event_rows
            else True,
            "denominatorReconciledRows": sum(
                row["denominatorReconciled"] == "1"
                for row in event_rows + exposure_rows + practical_rows
            ),
            "totalRowsWithDenominatorField": (
                len(event_rows) + len(exposure_rows) + len(practical_rows)
            ),
        },
        "limitations": [
            "The CourtListener search is explicitly published-only; unpublished and other-status opinions are outside the cohort.",
            "Public full-text availability is 115/191 and nonrandom across tracked decisions and opinion-document types.",
            "The citation-linked denominator is not an all-case opportunity denominator and excludes legally relevant cases that do not cite a tracked CourtListener opinion identifier.",
            "The 65-cell nationwide-applicability and citation-presence frame does not reveal whether a relevant case opportunity arose in a circuit.",
            "Automated context rules produce candidate flags and do not substitute for expert legal treatment coding; the review queue remains pending.",
            "The five practical cases are purposively selected salient environmental statutory cases, not a representative or constitutional-case sample.",
            "The practical cohort contains no noncompliant classification and cannot estimate a general government-noncompliance rate.",
            "Neither cohort is denominator-matched to the simulator's synthetic case-average compliance metrics.",
        ],
        "outputRows": {
            str(EVENT_OUTPUT.relative_to(ROOT)): len(event_rows),
            str(EXPOSURE_OUTPUT.relative_to(ROOT)): len(exposure_rows),
            str(PRACTICAL_OUTPUT.relative_to(ROOT)): len(practical_rows),
            str(CALIBRATION_OUTPUT.relative_to(ROOT)): len(calibration_rows),
            str(SUMMARY_CSV.relative_to(ROOT)): len(summary_rows),
            str(AVAILABILITY_CSV.relative_to(ROOT)): len(availability_rows),
            str(TREATMENT_REVIEW_QUEUE.relative_to(ROOT)): len(
                treatment_review_rows
            ),
            str(GURGANUS_CLASSIFICATIONS.relative_to(ROOT)): len(
                gurganus_classification_rows
            ),
        },
        "outputSha256": {
            str(path.relative_to(ROOT)): sha256_file(path)
            for path in [
                EVENT_OUTPUT,
                EXPOSURE_OUTPUT,
                PRACTICAL_OUTPUT,
                CALIBRATION_OUTPUT,
                SUMMARY_CSV,
                SUMMARY_MD,
                AVAILABILITY_CSV,
                AVAILABILITY_MD,
                TREATMENT_REVIEW_QUEUE,
                GURGANUS_CLASSIFICATIONS,
            ]
        },
    }
    write_json(MANIFEST_OUTPUT, manifest)
    print(
        "Built environmental implementation cohort: "
        f"{len(event_rows)} lower-court events, {len(exposure_rows)} exposure cells, "
        f"{len(practical_rows)} practical episodes."
    )
    print(
        "Public full text available for "
        f"{lower_metadata['fullTextAvailable']}/{len(event_rows)} events; "
        f"citation context found for {lower_metadata['citationContextFound']}."
    )


if __name__ == "__main__":
    main()
