#!/usr/bin/env python3
"""Extract a bounded lower-court doctrinal-uptake benchmark.

The source is the replication release for Masood, Kassow, and Songer (2019),
"The Aggregate Dynamics of Lower Court Responses to the U.S. Supreme Court."
Its unit is one formally argued Supreme Court precedent, with aggregate
Shepard's lower-court response counts through 2016. It does not contain one row
per lower-court opinion, an exposed-case denominator, ignored decisions, or
practical implementation events. The generated benchmark is therefore direct
aggregate doctrinal-uptake evidence and proxy context for the simulator's
synthetic lowerCourtCompliance score, not denominator-matched validation.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK_DIR = ROOT / "data" / "benchmarks"
CALIBRATION_DIR = ROOT / "data" / "calibration"
REPORT_DIR = ROOT / "reports"
RAW_DIR = ROOT / "data" / "raw" / "lower-court-precedent-treatment"

DEFAULT_OUTPUT = BENCHMARK_DIR / "lower-court-precedent-treatment-aggregate-v1.csv"
DEFAULT_MANIFEST = (
    BENCHMARK_DIR / "lower-court-precedent-treatment-aggregate-v1-manifest.json"
)
DEFAULT_SUMMARY_CSV = REPORT_DIR / "lower-court-precedent-treatment-summary-v1.csv"
DEFAULT_SUMMARY_MD = REPORT_DIR / "lower-court-precedent-treatment-summary-v1.md"
DEFAULT_CALIBRATION = CALIBRATION_DIR / "lower-court-precedent-treatment-v1.csv"

SOURCE_KEY = "masood-kassow-songer-2019-precedent-treatment"
SOURCE_NAME = (
    "Replication Data for: The Aggregate Dynamics of Lower Court Responses "
    "to the U.S. Supreme Court"
)
DATASET_DOI = "10.7910/DVN/DZZY7G"
DATASET_URL = f"https://doi.org/{DATASET_DOI}"
DATASET_API = (
    "https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId="
    + urllib.parse.quote(f"doi:{DATASET_DOI}", safe="")
)
ARTICLE_DOI = "10.1086/703067"
ARTICLE_URL = f"https://doi.org/{ARTICLE_DOI}"
ARTICLE_CITATION = (
    "Masood, Ali S., Benjamin J. Kassow, and Donald R. Songer. 2019. "
    "\"The Aggregate Dynamics of Lower Court Responses to the U.S. Supreme Court.\" "
    "Journal of Law and Courts 7(2): 159-186."
)
DATA_LABEL = "MKS_ReplicationData_JLC.tab"
CODE_LABEL = "MKS_ReplicationCode_JLC.do"
EXPECTED_DATA_MD5 = "69cb7a7ff2d75da1ac6db1f99e085ffc"
EXPECTED_CODE_MD5 = "235872cd35d804bbee94b308289b34d8"
EXPECTED_TAB_SHA256 = "815dd4a628e8be96b7a49b400bad55c0942193adcc152d0b0b055247c582069a"
EXPECTED_FILE_UNF = "UNF:6:L5oJ8wGINogURIEtpkzJpQ=="
EXPECTED_ROWS = 876
EXPECTED_COLUMNS = 302
EXPECTED_MODEL_ROWS = 861
EXPECTED_CONSTITUTIONAL_ROWS = 223
EXPECTED_TERMS = {
    "1995": 90,
    "1996": 95,
    "1997": 100,
    "1998": 92,
    "1999": 85,
    "2000": 87,
    "2001": 84,
    "2002": 84,
    "2003": 79,
    "2004": 80,
}

RAW_METADATA = RAW_DIR / "dataset-metadata.json"
RAW_TAB = RAW_DIR / DATA_LABEL
RAW_ORIGINAL = RAW_DIR / "MKS_ReplicationData_JLC.dta"
RAW_CODE = RAW_DIR / CODE_LABEL
RAW_DDI = RAW_DIR / "MKS_ReplicationData_JLC-ddi.xml"

ARTICLE_MODEL_FIELDS = (
    "num_citationsto2016",
    "num_positiveto2016",
    "lnsummary2",
    "median_vitality16",
    "margin",
    "altprec",
    "nytsalience",
    "decisiondirection",
    "numberoflegalprovisionsincase",
    "criminal",
    "opp2016",
    "opp2_2016",
    "majopinwriterterm",
)

OUTPUT_FIELDS = [
    "sourceKey",
    "sourceRecordId",
    "sourceUrl",
    "sourceDatasetDoi",
    "articleDoi",
    "usReportsCitation",
    "caseName",
    "supremeCourtTerm",
    "decisionDate",
    "scdbDocketId",
    "scotusCitation",
    "lexisCitation",
    "issueAreaCode",
    "constitutionalIssue",
    "criminalCase",
    "articleMainModelEligible",
    "summaryDecisionCount",
    "citedCountThrough2016",
    "followedCountThrough2016",
    "otherAdverseTreatmentCountThrough2016",
    "distinguishedCountThrough2016",
    "adverseTreatmentCountThrough2016",
    "citedOrFollowedCountThrough2016",
    "citedOrAdverseCountThrough2016",
    "directionalTreatmentCountThrough2016",
    "followedShareAmongCitedOrFollowed",
    "adverseShareAmongCitedOrAdverse",
    "followedShareAmongDirectionalTreatments",
    "responseWindow",
    "measurementDenominator",
    "coderNotes",
]

SUMMARY_FIELDS = [
    "metricKey",
    "subset",
    "term",
    "numerator",
    "denominator",
    "observedValue",
    "denominatorSpec",
    "sourceUrl",
    "validationUse",
    "manuscriptUse",
    "notes",
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

DDI_NAMESPACE = {"d": "http://www.icpsr.umich.edu/DDI"}


def digest(path: Path, algorithm: str) -> str:
    hasher = hashlib.new(algorithm)
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def download(url: str, path: Path, refresh: bool) -> None:
    if path.exists() and not refresh:
        return
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "constitutional-review-publication-research/1.0",
            "Accept-Encoding": "identity",
        },
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        payload = response.read()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text())


def dataset_file(
    metadata: dict[str, object],
    label: str,
) -> dict[str, object]:
    latest = metadata["data"]["latestVersion"]  # type: ignore[index]
    files = latest["files"]  # type: ignore[index]
    for entry in files:  # type: ignore[assignment]
        if entry.get("label") == label:
            return entry
    raise SystemExit(f"Dataset metadata does not contain {label}")


def access_url(file_id: int, format_name: str | None = None) -> str:
    url = f"https://dataverse.harvard.edu/api/access/datafile/{file_id}"
    if format_name:
        url += "?" + urllib.parse.urlencode({"format": format_name})
    return url


def fetch_sources(refresh: bool) -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    download(DATASET_API, RAW_METADATA, refresh)
    metadata = read_json(RAW_METADATA)
    if metadata.get("status") != "OK":
        raise SystemExit("Harvard Dataverse metadata request did not return status=OK")
    latest = metadata["data"]["latestVersion"]  # type: ignore[index]
    if (
        int(latest.get("versionNumber", -1)) != 1
        or int(latest.get("versionMinorNumber", -1)) != 0
        or latest.get("versionState") != "RELEASED"
    ):
        raise SystemExit("Expected released Harvard Dataverse version 1.0")
    license_data = latest.get("license", {})
    if license_data.get("rightsIdentifier") != "CC0-1.0":
        raise SystemExit("Expected the replication dataset to retain its CC0-1.0 license")

    data_entry = dataset_file(metadata, DATA_LABEL)
    code_entry = dataset_file(metadata, CODE_LABEL)
    data_file = data_entry["dataFile"]  # type: ignore[index]
    code_file = code_entry["dataFile"]  # type: ignore[index]
    data_id = int(data_file["id"])  # type: ignore[index]
    code_id = int(code_file["id"])  # type: ignore[index]

    download(access_url(data_id, "tab"), RAW_TAB, refresh)
    download(access_url(data_id, "original"), RAW_ORIGINAL, refresh)
    download(access_url(code_id), RAW_CODE, refresh)
    download(access_url(data_id) + "/metadata", RAW_DDI, refresh)

    if digest(RAW_ORIGINAL, "md5") != EXPECTED_DATA_MD5:
        raise SystemExit("Original Stata file MD5 does not match the released Dataverse checksum")
    if digest(RAW_CODE, "md5") != EXPECTED_CODE_MD5:
        raise SystemExit("Replication code MD5 does not match the released Dataverse checksum")
    if digest(RAW_TAB, "sha256") != EXPECTED_TAB_SHA256:
        raise SystemExit("Dataverse tab export SHA-256 differs from the audited version")
    if data_file.get("checksum", {}).get("value") != EXPECTED_DATA_MD5:  # type: ignore[union-attr]
        raise SystemExit("Dataset metadata carries an unexpected data-file checksum")
    if code_file.get("checksum", {}).get("value") != EXPECTED_CODE_MD5:  # type: ignore[union-attr]
        raise SystemExit("Dataset metadata carries an unexpected code-file checksum")
    return metadata, data_file, code_file


def ddi_dimensions() -> tuple[int, int, str]:
    root = ET.parse(RAW_DDI).getroot()
    cases = root.findtext(".//d:caseQnty", namespaces=DDI_NAMESPACE)
    variables = root.findtext(".//d:varQnty", namespaces=DDI_NAMESPACE)
    unf = root.findtext(
        ".//d:fileDscr/d:notes[@subject='Universal Numeric Fingerprint']",
        namespaces=DDI_NAMESPACE,
    )
    if not cases or not variables or not unf:
        raise SystemExit("Dataverse DDI metadata is missing dimensions or file UNF")
    return int(cases), int(variables), unf


def read_source_rows() -> tuple[list[str], list[dict[str, str]]]:
    with RAW_TAB.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    required = {
        "uscite",
        "caseName",
        "term",
        "dateDecision",
        "docketId",
        "sctCite",
        "lexisCite",
        "issueArea",
        "constiss",
        "criminal",
        "num_summary2",
        "num_citationsto2016",
        "num_positiveto2016",
        "num_negativeto2016",
        "num_distinguishedto2016",
        "nnegativedist2016",
        *ARTICLE_MODEL_FIELDS,
    }
    missing = required - set(fields)
    if missing:
        raise SystemExit("Tab export is missing required fields: " + ", ".join(sorted(missing)))
    return fields, rows


def integer(value: str) -> int:
    clean = (value or "").strip()
    if not clean:
        return 0
    numeric = float(clean)
    if not numeric.is_integer():
        raise ValueError(f"Expected integer-valued source count, found {value!r}")
    return int(numeric)


def yes_no(value: str) -> str:
    parsed = integer(value)
    if parsed not in {0, 1}:
        raise ValueError(f"Expected binary source field, found {value!r}")
    return "yes" if parsed else "no"


def iso_date(value: str) -> str:
    return datetime.strptime(value, "%m/%d/%Y").date().isoformat()


def ratio(numerator: int, denominator: int) -> str:
    if denominator <= 0:
        return ""
    return f"{numerator / denominator:.9f}"


def article_model_eligible(row: dict[str, str]) -> bool:
    return all(row.get(field, "").strip() for field in ARTICLE_MODEL_FIELDS)


def build_rows(source_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    denominator = (
        "Aggregate Shepard's lower-court response categories attached to one formally "
        "argued U.S. Supreme Court precedent, covering the 12 regular federal circuits, "
        "their district courts, and state courts through 2016; Federal Circuit excluded"
    )
    output: list[dict[str, str]] = []
    for source in source_rows:
        cited = integer(source["num_citationsto2016"])
        followed = integer(source["num_positiveto2016"])
        other_adverse = integer(source["num_negativeto2016"])
        distinguished = integer(source["num_distinguishedto2016"])
        adverse = integer(source["nnegativedist2016"])
        if adverse != other_adverse + distinguished:
            raise SystemExit(
                f"{source['uscite']}: nnegativedist2016 does not equal "
                "num_negativeto2016 + num_distinguishedto2016"
            )
        cited_or_followed = cited + followed
        cited_or_adverse = cited + adverse
        directional = followed + adverse
        output.append({
            "sourceKey": SOURCE_KEY,
            "sourceRecordId": source["uscite"],
            "sourceUrl": DATASET_URL,
            "sourceDatasetDoi": DATASET_DOI,
            "articleDoi": ARTICLE_DOI,
            "usReportsCitation": source["uscite"],
            "caseName": source["caseName"],
            "supremeCourtTerm": source["term"],
            "decisionDate": iso_date(source["dateDecision"]),
            "scdbDocketId": source["docketId"],
            "scotusCitation": source["sctCite"],
            "lexisCitation": source["lexisCite"],
            "issueAreaCode": source["issueArea"],
            "constitutionalIssue": yes_no(source["constiss"]),
            "criminalCase": yes_no(source["criminal"]),
            "articleMainModelEligible": "yes" if article_model_eligible(source) else "no",
            "summaryDecisionCount": str(integer(source["num_summary2"])),
            "citedCountThrough2016": str(cited),
            "followedCountThrough2016": str(followed),
            "otherAdverseTreatmentCountThrough2016": str(other_adverse),
            "distinguishedCountThrough2016": str(distinguished),
            "adverseTreatmentCountThrough2016": str(adverse),
            "citedOrFollowedCountThrough2016": str(cited_or_followed),
            "citedOrAdverseCountThrough2016": str(cited_or_adverse),
            "directionalTreatmentCountThrough2016": str(directional),
            "followedShareAmongCitedOrFollowed": ratio(followed, cited_or_followed),
            "adverseShareAmongCitedOrAdverse": ratio(adverse, cited_or_adverse),
            "followedShareAmongDirectionalTreatments": ratio(followed, directional),
            "responseWindow": "post-decision through 2016",
            "measurementDenominator": denominator,
            "coderNotes": (
                "Automated reduction of the authors' public precedent-level replication file. "
                "The source aggregates Shepard's categories and does not expose individual "
                "lower-court opinions, non-citing or ignored exposed cases, treatment dates, "
                "remedy fidelity, or practical implementation. Use as bounded doctrinal-uptake "
                "context only, not as a practical-compliance rate or denominator-matched "
                "lowerCourtCompliance validation target."
            ),
        })
    return sorted(
        output,
        key=lambda row: (
            row["supremeCourtTerm"],
            row["decisionDate"],
            row["usReportsCitation"],
        ),
    )


def validate_rows(fields: list[str], source_rows: list[dict[str, str]], rows: list[dict[str, str]]) -> None:
    if len(fields) != EXPECTED_COLUMNS:
        raise SystemExit(f"Expected {EXPECTED_COLUMNS} source columns, found {len(fields)}")
    if len(source_rows) != EXPECTED_ROWS or len(rows) != EXPECTED_ROWS:
        raise SystemExit(f"Expected {EXPECTED_ROWS} source rows")
    citations = [row["usReportsCitation"] for row in rows]
    if len(set(citations)) != len(citations):
        raise SystemExit("U.S. Reports citations are not unique across source rows")
    term_counts = Counter(row["supremeCourtTerm"] for row in rows)
    if dict(sorted(term_counts.items())) != EXPECTED_TERMS:
        raise SystemExit("Source term counts differ from the audited 1995-2004 distribution")
    model_rows = sum(row["articleMainModelEligible"] == "yes" for row in rows)
    if model_rows != EXPECTED_MODEL_ROWS:
        raise SystemExit(
            f"Expected {EXPECTED_MODEL_ROWS} published-model-eligible rows, found {model_rows}"
        )
    constitutional_rows = sum(row["constitutionalIssue"] == "yes" for row in rows)
    if constitutional_rows != EXPECTED_CONSTITUTIONAL_ROWS:
        raise SystemExit(
            f"Expected {EXPECTED_CONSTITUTIONAL_ROWS} constitutional-issue rows, "
            f"found {constitutional_rows}"
        )


def subset_counts(rows: list[dict[str, str]]) -> dict[str, int]:
    cited = sum(int(row["citedCountThrough2016"]) for row in rows)
    followed = sum(int(row["followedCountThrough2016"]) for row in rows)
    other_adverse = sum(
        int(row["otherAdverseTreatmentCountThrough2016"]) for row in rows
    )
    distinguished = sum(int(row["distinguishedCountThrough2016"]) for row in rows)
    adverse = sum(int(row["adverseTreatmentCountThrough2016"]) for row in rows)
    return {
        "precedents": len(rows),
        "cited": cited,
        "followed": followed,
        "otherAdverse": other_adverse,
        "distinguished": distinguished,
        "adverse": adverse,
        "citedOrFollowed": cited + followed,
        "citedOrAdverse": cited + adverse,
        "directional": followed + adverse,
    }


def summary_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    subsets = {
        "all_precedents": rows,
        "article_main_model": [
            row for row in rows if row["articleMainModelEligible"] == "yes"
        ],
        "constitutional_issues": [
            row for row in rows if row["constitutionalIssue"] == "yes"
        ],
    }
    output: list[dict[str, str]] = []

    def add(
        metric: str,
        subset: str,
        numerator: int,
        denominator: int | None,
        denominator_spec: str,
        notes: str,
    ) -> None:
        observed = str(numerator) if denominator is None else f"{numerator / denominator:.9f}"
        output.append({
            "metricKey": metric,
            "subset": subset,
            "term": "1995-2004 precedents; responses through 2016",
            "numerator": str(numerator),
            "denominator": "" if denominator is None else str(denominator),
            "observedValue": observed,
            "denominatorSpec": denominator_spec,
            "sourceUrl": DATASET_URL,
            "validationUse": "direct_aggregate_doctrinal_uptake",
            "manuscriptUse": (
                "bounded doctrinal-uptake context only; not practical compliance "
                "or denominator-matched lowerCourtCompliance validation"
            ),
            "notes": notes,
        })

    for subset, subset_rows in subsets.items():
        counts = subset_counts(subset_rows)
        add(
            "lowerCourtPrecedentRows",
            subset,
            counts["precedents"],
            None,
            "unique U.S. Reports citations in the selected replication-file subset",
            "The full file has one row per formally argued Supreme Court precedent.",
        )
        add(
            "lowerCourtCitedCount",
            subset,
            counts["cited"],
            None,
            "aggregate Shepard's cited-only responses in the selected subset",
            "Cited-only is separate from followed and adverse treatment categories.",
        )
        add(
            "lowerCourtFollowedCount",
            subset,
            counts["followed"],
            None,
            "aggregate Shepard's followed responses in the selected subset",
            "The article treats followed responses as positive treatments.",
        )
        add(
            "lowerCourtAdverseTreatmentCount",
            subset,
            counts["adverse"],
            None,
            "aggregate adverse plus distinguished responses in the selected subset",
            (
                "Adverse equals the source's other negative-treatment count plus "
                "distinguished count."
            ),
        )
        if counts["citedOrFollowed"]:
            add(
                "lowerCourtFollowedShareAmongCitedOrFollowed",
                subset,
                counts["followed"],
                counts["citedOrFollowed"],
                "followed / (cited-only + followed) aggregate response counts",
                "This is the proportional outcome used in the article's positive-treatment model.",
            )
        if counts["citedOrAdverse"]:
            add(
                "lowerCourtAdverseShareAmongCitedOrAdverse",
                subset,
                counts["adverse"],
                counts["citedOrAdverse"],
                "adverse / (cited-only + adverse) aggregate response counts",
                (
                    "This combines the source's other negative-treatment and "
                    "distinguished categories."
                ),
            )
        if counts["directional"]:
            add(
                "lowerCourtFollowedShareAmongDirectionalTreatments",
                subset,
                counts["followed"],
                counts["directional"],
                "followed / (followed + adverse) aggregate directional treatment counts",
                (
                    "This excludes cited-only responses and is not an exposed-case "
                    "or practical-implementation compliance rate."
                ),
            )
    return output


def calibration_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    subsets: list[tuple[str, Callable[[dict[str, str]], bool], str]] = [
        (
            "allPrecedents",
            lambda row: True,
            "all 876 formally argued Supreme Court precedents in the replication file",
        ),
        (
            "constitutionalIssues",
            lambda row: row["constitutionalIssue"] == "yes",
            "223 precedents flagged as constitutional issues in the replication file",
        ),
    ]
    metrics = [
        (
            "FollowedShareAmongCitedOrFollowed",
            "followed",
            "citedOrFollowed",
            "followed / (cited-only + followed)",
        ),
        (
            "AdverseShareAmongCitedOrAdverse",
            "adverse",
            "citedOrAdverse",
            "adverse / (cited-only + adverse)",
        ),
        (
            "FollowedShareAmongDirectionalTreatments",
            "followed",
            "directional",
            "followed / (followed + adverse)",
        ),
    ]
    output: list[dict[str, str]] = []
    terms = sorted({row["supremeCourtTerm"] for row in rows})
    for subset_key, predicate, coverage in subsets:
        for term in terms:
            term_rows = [
                row
                for row in rows
                if row["supremeCourtTerm"] == term and predicate(row)
            ]
            counts = subset_counts(term_rows)
            for metric_suffix, numerator_key, denominator_key, formula in metrics:
                numerator = counts[numerator_key]
                denominator = counts[denominator_key]
                if denominator <= 0:
                    continue
                output.append({
                    "sourceKey": SOURCE_KEY,
                    "sourceName": SOURCE_NAME,
                    "domain": "lower_court_compliance",
                    "metric": f"lowerCourt{metric_suffix}_{subset_key}",
                    "term": term,
                    "numerator": str(numerator),
                    "denominator": str(denominator),
                    "value": f"{numerator / denominator:.9f}",
                    "sourceUrl": DATASET_URL,
                    "confidenceLevel": "High",
                    "validationUse": "direct_behavior_guardrail",
                    "coverageScope": coverage + "; lower-court responses through 2016",
                    "comparabilityClass": (
                        "aggregate precedent-treatment counts versus synthetic "
                        "case-average compliance score"
                    ),
                    "notes": (
                        f"Term-pooled {formula}. The source aggregates Shepard's "
                        "treatment categories across lower federal and state courts, "
                        "excludes the Federal Circuit, and lacks an exposed-case, "
                        "ignored-decision, treatment-date, remedy, or practical-"
                        "implementation denominator."
                    ),
                })
    return output


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_summary_markdown(path: Path, rows: list[dict[str, str]]) -> None:
    by_key = {(row["subset"], row["metricKey"]): row for row in rows}
    lines = [
        "# Lower-Court Precedent Treatment Summary v1",
        "",
        (
            "This report summarizes the public replication file for Masood, Kassow, "
            "and Songer (2019). The file contains one row per formally argued U.S. "
            "Supreme Court precedent and aggregate Shepard's lower-court response "
            "counts through 2016. It is direct doctrinal-uptake evidence, but it is "
            "not an individual-opinion extract or a practical-implementation "
            "compliance rate."
        ),
        "",
        "| Subset | Precedents | Cited only | Followed | Adverse | Followed / directional | Followed / cited-or-followed | Adverse / cited-or-adverse |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for subset, label in (
        ("all_precedents", "All source precedents"),
        ("article_main_model", "Published main-model rows"),
        ("constitutional_issues", "Constitutional-issue precedents"),
    ):
        def value(metric: str) -> str:
            return by_key[(subset, metric)]["observedValue"]

        lines.append(
            f"| {label} | {value('lowerCourtPrecedentRows')} | "
            f"{value('lowerCourtCitedCount')} | {value('lowerCourtFollowedCount')} | "
            f"{value('lowerCourtAdverseTreatmentCount')} | "
            f"{float(value('lowerCourtFollowedShareAmongDirectionalTreatments')):.3%} | "
            f"{float(value('lowerCourtFollowedShareAmongCitedOrFollowed')):.3%} | "
            f"{float(value('lowerCourtAdverseShareAmongCitedOrAdverse')):.3%} |"
        )
    lines.extend([
        "",
        "Evidence boundary:",
        "",
        "- The source-decision universe covers the 1995-2004 Supreme Court terms; lower-court responses are accumulated through 2016.",
        "- The article defines `followed` as a positive treatment. The generated adverse count equals the source's other negative-treatment count plus its separate distinguished count.",
        "- The 876-row file reconciles to the article's descriptive statistics. Exactly 861 rows have every field used by the main published models.",
        "- The 223-row constitutional-issue subset is source-flagged; it is not a new hand-coded constitutional-case classification.",
        "- Aggregate counts weight heavily treated precedents more heavily than lightly treated precedents and omit non-citing or ignored exposed cases.",
        "- The public Dataverse release is CC0-1.0, but the underlying treatment categories were compiled by the study authors from Shepard's Citations. Individual treatment-event records are not present in the released file.",
        "- Use these values as bounded doctrinal-uptake context only. They do not validate practical implementation, government compliance, remedy fidelity, or the simulator's synthetic case-average `lowerCourtCompliance` score.",
        "",
        f"Source: [{SOURCE_NAME}]({DATASET_URL}); article DOI: [{ARTICLE_DOI}]({ARTICLE_URL}).",
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def write_manifest(
    path: Path,
    metadata: dict[str, object],
    data_file: dict[str, object],
    code_file: dict[str, object],
    fields: list[str],
    rows: list[dict[str, str]],
    output_path: Path,
    summary_csv: Path,
    summary_md: Path,
    calibration_path: Path,
    extraction_date: date,
) -> None:
    latest = metadata["data"]["latestVersion"]  # type: ignore[index]
    ddi_rows, ddi_columns, file_unf = ddi_dimensions()
    if (ddi_rows, ddi_columns, file_unf) != (
        EXPECTED_ROWS,
        EXPECTED_COLUMNS,
        EXPECTED_FILE_UNF,
    ):
        raise SystemExit("Dataverse DDI dimensions or UNF differ from the audited release")
    counts_all = subset_counts(rows)
    constitutional = [row for row in rows if row["constitutionalIssue"] == "yes"]
    counts_constitutional = subset_counts(constitutional)
    payload = {
        "sourceKey": SOURCE_KEY,
        "sourceName": SOURCE_NAME,
        "sourceDatasetDoi": DATASET_DOI,
        "sourceUrl": DATASET_URL,
        "datasetApi": DATASET_API,
        "articleDoi": ARTICLE_DOI,
        "articleUrl": ARTICLE_URL,
        "articleCitation": ARTICLE_CITATION,
        "datasetVersion": (
            f"{latest.get('versionNumber')}.{latest.get('versionMinorNumber')}"
        ),
        "datasetReleaseTime": latest.get("releaseTime"),
        "license": latest.get("license"),
        "extractionDate": extraction_date.isoformat(),
        "dataFileId": data_file.get("id"),
        "dataFileLabel": DATA_LABEL,
        "originalFileFormat": data_file.get("originalFileFormat"),
        "expectedOriginalFileMd5": EXPECTED_DATA_MD5,
        "originalFileMd5": digest(RAW_ORIGINAL, "md5"),
        "originalFileSha256": digest(RAW_ORIGINAL, "sha256"),
        "tabExportSha256": digest(RAW_TAB, "sha256"),
        "tabExportBytes": RAW_TAB.stat().st_size,
        "codeFileId": code_file.get("id"),
        "codeFileLabel": CODE_LABEL,
        "expectedCodeFileMd5": EXPECTED_CODE_MD5,
        "codeFileMd5": digest(RAW_CODE, "md5"),
        "codeFileSha256": digest(RAW_CODE, "sha256"),
        "fileUnf": file_unf,
        "sourceRowCount": len(rows),
        "sourceColumnCount": len(fields),
        "sourceTermCounts": dict(sorted(Counter(
            row["supremeCourtTerm"] for row in rows
        ).items())),
        "articleMainModelRowCount": sum(
            row["articleMainModelEligible"] == "yes" for row in rows
        ),
        "constitutionalIssueRowCount": len(constitutional),
        "aggregateCounts": counts_all,
        "constitutionalIssueAggregateCounts": counts_constitutional,
        "outputs": {
            output_path.relative_to(ROOT).as_posix(): digest(output_path, "sha256"),
            summary_csv.relative_to(ROOT).as_posix(): digest(summary_csv, "sha256"),
            summary_md.relative_to(ROOT).as_posix(): digest(summary_md, "sha256"),
            calibration_path.relative_to(ROOT).as_posix(): digest(
                calibration_path, "sha256"
            ),
        },
        "normalizationMethod": (
            "One normalized row per source precedent; source aggregate treatment "
            "counts are retained and simple denominator-specific shares are derived. "
            "Calibration rows pool counts within source-decision term and separately "
            "retain all-precedent and source-flagged constitutional-issue subsets."
        ),
        "denominatorSpec": (
            "Aggregate Shepard's lower-court cited, followed, and adverse treatment "
            "categories attached to formally argued 1995-2004 Supreme Court "
            "precedents, with lower-court responses accumulated through 2016."
        ),
        "evidenceBoundary": [
            "The benchmark is direct aggregate doctrinal-uptake evidence, not one row per lower-court opinion.",
            "The release does not expose treatment dates, lower-court identifiers, remedies, ignored or non-citing exposed cases, or practical implementation events.",
            "The constitutional-issue subset uses the source file's constiss flag.",
            "The generated directional-treatment share is not a practical-compliance rate and is not denominator-matched to the simulator's synthetic lowerCourtCompliance score.",
            "The public release is CC0-1.0; the source study compiled the underlying treatment categories from Shepard's Citations.",
        ],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--extraction-date", default=date.today().isoformat())
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--summary-csv", type=Path, default=DEFAULT_SUMMARY_CSV)
    parser.add_argument("--summary-md", type=Path, default=DEFAULT_SUMMARY_MD)
    parser.add_argument("--calibration-output", type=Path, default=DEFAULT_CALIBRATION)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    extraction_date = date.fromisoformat(args.extraction_date)
    metadata, data_file, code_file = fetch_sources(args.refresh)
    fields, source_rows = read_source_rows()
    rows = build_rows(source_rows)
    validate_rows(fields, source_rows, rows)
    summaries = summary_rows(rows)
    calibrations = calibration_rows(rows)
    write_csv(args.output, rows, OUTPUT_FIELDS)
    write_csv(args.summary_csv, summaries, SUMMARY_FIELDS)
    write_summary_markdown(args.summary_md, summaries)
    write_csv(args.calibration_output, calibrations, CALIBRATION_FIELDS)
    write_manifest(
        args.manifest,
        metadata,
        data_file,
        code_file,
        fields,
        rows,
        args.output,
        args.summary_csv,
        args.summary_md,
        args.calibration_output,
        extraction_date,
    )
    print(f"Wrote {args.output.relative_to(ROOT)} ({len(rows)} rows)")
    print(f"Wrote {args.manifest.relative_to(ROOT)}")
    print(f"Wrote {args.summary_csv.relative_to(ROOT)}")
    print(f"Wrote {args.summary_md.relative_to(ROOT)}")
    print(f"Wrote {args.calibration_output.relative_to(ROOT)} ({len(calibrations)} rows)")


if __name__ == "__main__":
    main()
