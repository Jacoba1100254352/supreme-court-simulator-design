#!/usr/bin/env python3
"""Build pathway-specific validation dashboards from generated reports."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
CALIBRATION_DIR = ROOT / "data" / "calibration"
CAMPAIGN_CSV = REPORTS / "constitutional-review-campaign-v2.csv"
SOURCE_RANGES_CSV = REPORTS / "calibration-source-ranges-v4.csv"
CALIBRATION_BASELINE_CSV = REPORTS / "calibration-baseline.csv"
DASHBOARD_CSV = REPORTS / "pathway-validation-dashboard-v1.csv"
DASHBOARD_MD = REPORTS / "pathway-validation-dashboard-v1.md"
PRIMARY_COVERAGE_CSV = REPORTS / "primary-source-coverage-v1.csv"
PRIMARY_COVERAGE_MD = REPORTS / "primary-source-coverage-v1.md"


PATHWAY_ROWS = [
    ("certiorari", "paidPetitionRate", "paidPetitionShare", "paid/IFP split", "same-court intake denominator"),
    ("certiorari", "ifpPetitionRate", "ifpPetitionShare", "paid/IFP split", "same-court intake denominator"),
    ("certiorari", "paidCfrRequestRate", "cfrRate_paid", "court-requested response", "petition-stage subset"),
    ("certiorari", "ifpCfrRequestRate", "cfrRate_ifp", "court-requested response", "petition-stage subset"),
    ("certiorari", "cvsgRequestRate", "cvsgCount", "CVSG signal", "count/flow context, not rate validated"),
    ("certiorari", "certiorariAdmissionRate", "us_scotus_plenaryReviewRate_allDocketed", "grant/admission funnel", "proxy: docketed-flow denominator"),
    ("certiorari", "genuineLowerCourtSplitRate", "genuineConflictGrantRate", "split quality", "proxy: grant-rate effect, not split prevalence"),
    ("certiorari", "specialistCounselRate", "us_certGrant_formerClerk_predicted", "elite counsel access", "proxy: predicted grant effect"),
    ("emergency", "emergencyStayDocketRate", "emergencyStayDocketRate", "emergency application presence", "raw shadow-docket denominator"),
    ("emergency", "emergencyOrderRate", "emergencyOrderRate", "emergency orders", "HLR/source-summary denominator"),
    ("emergency", "emergencyGrantRate", "noncapitalGrantRate_overall", "emergency relief grants", "noncapital applications denominator"),
    ("emergency", "reasonedEmergencyOrderRate", "noncapitalDissentRate_any", "reason/disagreement visibility", "related public-disagreement proxy"),
    ("emergency", "meritsAccelerationRate", "noncapitalGrantRate_noLinkedMerits", "merits follow-through", "proxy: no-linked-merits grant subset"),
    ("emergency", "emergencyDownstreamEffect", "presidentialEmergencyApplications_peak", "downstream incentive effect", "proxy trend context"),
    ("complaint_referral", "admissionRate", "spain_amparo_admission_rate", "individual complaint admission", "comparative complaint-filter denominator"),
    ("complaint_referral", "publicInterestFilteredRate", "spain_amparo_admissionRate", "public-interest filtering", "comparative complaint-filter denominator"),
    ("complaint_referral", "constitutionalRemandRate", "fr_qpc_delayedEffectRate_decidedQPC", "constitutional remand/deferred remedy", "QPC delayed-effect proxy"),
    ("complaint_referral", "meritsTransferRate", "france_qpc_decisions", "filtered referral merits path", "count context, not direct rate"),
    ("lower_court_compliance", "lowerCourtCompliance", "districtCourtAlignmentShockSameDirectionPP", "lower-court alignment", "direct mechanism estimate"),
    ("lower_court_compliance", "lowerCourtResistanceRisk", "echrEnforcementDomesticJudgmentsThemeShare", "implementation resistance", "theme-share proxy"),
    ("lower_court_compliance", "governmentNoncomplianceRate", "federalAgencyNarrowComplianceShare", "government noncompliance", "agency implementation proxy"),
    ("lower_court_compliance", "interbranchCompliance", "costaRicaOrdersTrackedShare", "monitoring capacity", "monitoring coverage proxy"),
    ("override_remand", "overrideAttemptRate", "invalidationRate", "override pressure after invalidation", "proxy: invalidation creates opportunity"),
    ("override_remand", "overrideRate", "canada_override_duration_years", "legislative override success", "design prior, not behavioral rate"),
    ("override_remand", "rightsCarveoutBlockRate", "fr_qpc_invalidityRate_decidedQPC", "rights carveout pressure", "comparative invalidity proxy"),
]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def weighted_current_like() -> dict[str, float]:
    totals: dict[str, float] = defaultdict(float)
    weight_total = 0.0
    for row in read_csv(CAMPAIGN_CSV):
        if row.get("scenarioKey") != "current-us-like":
            continue
        weight = float(row.get("caseWeight") or 1.0)
        weight_total += weight
        for key, value in row.items():
            if not value:
                continue
            try:
                totals[key] += float(value) * weight
            except ValueError:
                pass
    denominator = max(1.0, weight_total)
    return {key: value / denominator for key, value in totals.items()}


def source_ranges() -> dict[str, dict[str, str]]:
    return {row["metric"]: row for row in read_csv(SOURCE_RANGES_CSV)}


def calibration_targets() -> dict[str, dict[str, str]]:
    targets = {}
    for row in read_csv(CALIBRATION_BASELINE_CSV):
        targets[row["metric"]] = row
        targets[row["sourceMetric"]] = row
    return targets


def observation_metadata() -> dict[str, dict[str, set[str]]]:
    metadata: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    for path in CALIBRATION_DIR.rglob("*.csv"):
        with path.open(newline="") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                metric = row.get("metricKey") or row.get("metric")
                if not metric:
                    continue
                validation = row.get("validationUse") or "normalized_source"
                confidence = row.get("confidenceLevel") or ""
                source = row.get("sourceName") or row.get("sourceKey") or path.stem
                url = row.get("sourceUrl") or ""
                metadata[metric]["validationUse"].add(validation)
                metadata[metric]["confidence"].add(confidence)
                metadata[metric]["source"].add(source)
                metadata[metric]["sourceUrl"].add(url)
                metadata[metric]["file"].add(path.relative_to(ROOT).as_posix())
    return metadata


def source_tier(metric: str, target: dict[str, str] | None, metadata: dict[str, dict[str, set[str]]]) -> str:
    if target and target.get("sourceTier"):
        return target["sourceTier"]
    meta = metadata.get(metric, {})
    files = " ".join(meta.get("file", set())).lower()
    sources = " ".join(meta.get("source", set())).lower()
    urls = " ".join(meta.get("sourceUrl", set())).lower()
    joined = " ".join([files, sources, urls])
    if not joined.strip():
        return "not_yet_source_backed"
    primary_markers = (
        "supremecourt.gov",
        "scdb.la.psu.edu",
        "shadowdocketdata.com",
        "tribunalconstitucional",
        "qpc360",
        "conseil-constitutionnel",
        "cortecostituzionale",
        "ccourt.go.kr",
        "justice.gc.ca",
        "supreme court of canada",
        "journal of the supreme court",
        "supreme court journal",
        "year in review",
        "annual report",
        "memoria",
        "statistical annex",
    )
    if any(marker in joined for marker in primary_markers):
        return "primary_source_named_in_table" if "supreme-court-research" in files or "supreme-court-synthesis" in files else "raw_or_primary_summary"
    if "journal" in sources or "law review" in sources or "article" in sources or "study" in sources:
        return "peer_reviewed_or_scholarly_summary"
    if "supreme-court-research" in joined or "supreme-court-synthesis" in joined:
        return "research_synthesis"
    return "raw_or_primary_summary"


def joined(values: set[str], fallback: str = "") -> str:
    clean = sorted(value for value in values if value)
    return "; ".join(clean) if clean else fallback


def build_dashboard_rows() -> list[dict[str, str]]:
    current = weighted_current_like()
    ranges = source_ranges()
    targets = calibration_targets()
    metadata = observation_metadata()
    rows = []
    for pathway, simulator_metric, source_metric, construct, denominator_note in PATHWAY_ROWS:
        source = ranges.get(source_metric)
        target = targets.get(source_metric) or targets.get(simulator_metric)
        meta = metadata.get(source_metric, {})
        simulated = current.get(simulator_metric)
        if source:
            source_range = f"{float(source['rawMin']):.3f}--{float(source['rawMax']):.3f}"
            source_observations = source["observations"]
            source_terms = source["termRange"]
            source_keys = source["sourceKeys"]
        elif target:
            source_range = f"{float(target['min']):.3f}--{float(target['max']):.3f}"
            source_observations = target.get("sourceObservations", "")
            source_terms = target.get("sourceTerms", "")
            source_keys = target.get("sourceKey", "")
        else:
            source_range = ""
            source_observations = "0"
            source_terms = ""
            source_keys = ""
        rows.append({
            "pathway": pathway,
            "construct": construct,
            "simulatorMetric": simulator_metric,
            "currentLikeValue": "" if simulated is None else f"{simulated:.3f}",
            "sourceMetric": source_metric,
            "sourceRange": source_range,
            "sourceObservations": source_observations,
            "sourceTerms": source_terms,
            "sourceKeys": source_keys or joined(meta.get("file", set())),
            "validationUse": joined(meta.get("validationUse", set()), target.get("guardrailClass", "") if target else ""),
            "confidence": joined(meta.get("confidence", set())),
            "sourceTier": source_tier(source_metric, target, metadata),
            "denominatorNote": denominator_note,
            "nextValidationAction": next_action(source_metric, source, target, meta),
        })
    return rows


def next_action(source_metric: str, source: dict[str, str] | None, target: dict[str, str] | None, meta: dict[str, set[str]]) -> str:
    tier = source_tier(source_metric, target, {source_metric: meta})
    validation_use = " ".join(meta.get("validationUse", set())).lower()
    if tier == "not_yet_source_backed":
        return "needs primary-source target"
    if "proxy" in validation_use or "design_prior" in validation_use:
        return "replace proxy with direct denominator if available"
    if source and int(source.get("observations", "0") or 0) <= 1:
        return "expand term coverage"
    if tier == "primary_source_named_in_table":
        return "attach extracted source row or raw file in supplement"
    if tier in {"research_synthesis", "peer_reviewed_or_scholarly_summary"}:
        return "attach original source extraction in supplement"
    return "usable guardrail"


def write_dashboard(rows: list[dict[str, str]]) -> None:
    DASHBOARD_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0])
    with DASHBOARD_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Pathway Validation Dashboard v1",
        "",
        "This dashboard keeps pathway denominators separate. It does not pool certiorari, emergency applications, individual complaints, QPC/concrete referrals, compliance, and override/remand behavior.",
        "",
        "| Pathway | Construct | Sim metric | Current-like | Source metric | Source range | Tier | Validation use | Next action |",
        "| --- | --- | --- | ---: | --- | ---: | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['pathway']} | {row['construct']} | `{row['simulatorMetric']}` | "
            f"{row['currentLikeValue']} | `{row['sourceMetric']}` | {row['sourceRange']} | "
            f"{row['sourceTier']} | {row['validationUse']} | {row['nextValidationAction']} |"
        )
    DASHBOARD_MD.write_text("\n".join(lines) + "\n")


def build_coverage_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["pathway"]].append(row)
    coverage = []
    for pathway, pathway_rows in sorted(grouped.items()):
        total = len(pathway_rows)
        raw = sum(1 for row in pathway_rows if row["sourceTier"] in {"raw_or_primary_summary", "primary_source_named_in_table"})
        synthesis = sum(1 for row in pathway_rows if row["sourceTier"] in {"research_synthesis", "peer_reviewed_or_scholarly_summary"})
        missing = sum(1 for row in pathway_rows if row["sourceTier"] == "not_yet_source_backed")
        proxy = sum(1 for row in pathway_rows if "proxy" in row["validationUse"].lower() or "design_prior" in row["validationUse"].lower())
        coverage.append({
            "pathway": pathway,
            "rows": str(total),
            "rawOrPrimaryRows": str(raw),
            "researchSynthesisRows": str(synthesis),
            "missingRows": str(missing),
            "proxyOrDesignPriorRows": str(proxy),
            "primaryCoverageShare": f"{raw / max(1, total):.3f}",
        })
    return coverage


def write_coverage(rows: list[dict[str, str]]) -> None:
    coverage = build_coverage_rows(rows)
    with PRIMARY_COVERAGE_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(coverage[0]))
        writer.writeheader()
        writer.writerows(coverage)
    lines = [
        "# Primary Source Coverage v1",
        "",
        "Coverage counts are pathway-local. A low primary-coverage share means the simulator can still use the pathway as a synthetic diagnostic, but the paper should not frame that pathway as validated.",
        "",
        "| Pathway | Rows | Raw/primary | Research synthesis | Missing | Proxy/design prior | Primary share |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in coverage:
        lines.append(
            f"| {row['pathway']} | {row['rows']} | {row['rawOrPrimaryRows']} | "
            f"{row['researchSynthesisRows']} | {row['missingRows']} | "
            f"{row['proxyOrDesignPriorRows']} | {row['primaryCoverageShare']} |"
        )
    PRIMARY_COVERAGE_MD.write_text("\n".join(lines) + "\n")


def main() -> None:
    rows = build_dashboard_rows()
    write_dashboard(rows)
    write_coverage(rows)
    print(f"Wrote {DASHBOARD_CSV.relative_to(ROOT)}")
    print(f"Wrote {DASHBOARD_MD.relative_to(ROOT)}")
    print(f"Wrote {PRIMARY_COVERAGE_CSV.relative_to(ROOT)}")
    print(f"Wrote {PRIMARY_COVERAGE_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
