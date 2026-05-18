#!/usr/bin/env python3
"""Build pathway-specific denominator and metric-semantics audits."""

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
METRIC_SEMANTICS_CSV = REPORTS / "metric-semantics-v1.csv"
METRIC_SEMANTICS_MD = REPORTS / "metric-semantics-v1.md"


PATHWAY_ROWS = [
    {
        "pathway": "certiorari",
        "simulatorMetric": "paidCertPetitionShare",
        "sourceMetric": "paidPetitionShare",
        "construct": "paid certiorari intake share",
        "simulatorDenominator": "paid plus IFP certiorari-path petitions in the generated filed universe",
        "sourceDenominator": "all docketed paid and IFP matters in official term flow",
        "dashboardUse": "loose_calibration",
        "denominatorCompatibility": "near_pathway_match",
        "comparabilityNote": "conditional paid/IFP split is closer than all-case paidPetitionRate, but the simulator still excludes many non-review docketed matters",
    },
    {
        "pathway": "certiorari",
        "simulatorMetric": "ifpCertPetitionShare",
        "sourceMetric": "ifpPetitionShare",
        "construct": "IFP certiorari intake share",
        "simulatorDenominator": "paid plus IFP certiorari-path petitions in the generated filed universe",
        "sourceDenominator": "all docketed paid and IFP matters in official term flow",
        "dashboardUse": "loose_calibration",
        "denominatorCompatibility": "near_pathway_match",
        "comparabilityNote": "conditional paid/IFP split is closer than all-case ifpPetitionRate, but the simulator still excludes many non-review docketed matters",
    },
    {
        "pathway": "certiorari",
        "simulatorMetric": "paidCfrRequestRate",
        "sourceMetric": "cfrRate_paid",
        "construct": "paid court-requested response",
        "simulatorDenominator": "paid certiorari-path petitions",
        "sourceDenominator": "paid petitions or paid cert-stage subset described by source",
        "dashboardUse": "loose_calibration",
        "denominatorCompatibility": "near_pathway_match",
        "comparabilityNote": "stage is modeled explicitly, but the source rows are term-flow summaries rather than closed petition cohorts",
    },
    {
        "pathway": "certiorari",
        "simulatorMetric": "ifpCfrRequestRate",
        "sourceMetric": "cfrRate_ifp",
        "construct": "IFP court-requested response",
        "simulatorDenominator": "IFP certiorari-path petitions",
        "sourceDenominator": "IFP petitions or IFP cert-stage subset described by source",
        "dashboardUse": "loose_calibration",
        "denominatorCompatibility": "near_pathway_match",
        "comparabilityNote": "stage is modeled explicitly, but the source rows are term-flow summaries rather than closed petition cohorts",
    },
    {
        "pathway": "certiorari",
        "simulatorMetric": "cvsgRequestRate",
        "sourceMetric": "cvsgFrequency",
        "construct": "CVSG signal",
        "simulatorDenominator": "all generated filed matters",
        "sourceDenominator": "petitions receiving CVSG per year in historical study period",
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "count_rate_mismatch",
        "comparabilityNote": "the source is a count-per-year anchor, so the simulator rate is only a low-frequency transition diagnostic",
    },
    {
        "pathway": "certiorari",
        "simulatorMetric": "certiorariAdmissionRate",
        "sourceMetric": "us_scotus_plenaryReviewRate_allDocketed",
        "construct": "grant/admission funnel",
        "simulatorDenominator": "generated certiorari-path filings",
        "sourceDenominator": "all Supreme Court docketed matters",
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "denominator_mismatch",
        "comparabilityNote": "the source includes all docketed matters; the simulator denominator is already a constitutional-review cert-path subset",
    },
    {
        "pathway": "certiorari",
        "simulatorMetric": "genuineLowerCourtSplitRate",
        "sourceMetric": "genuineConflictAmongAlleged_rate",
        "construct": "genuine split quality",
        "simulatorDenominator": "all generated filed matters",
        "sourceDenominator": "petitions alleging lower-court conflict in a historical coded sample",
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "denominator_mismatch",
        "comparabilityNote": "useful for alleged-versus-genuine split logic, not as a whole-docket split prevalence target",
    },
    {
        "pathway": "certiorari",
        "simulatorMetric": "specialistCounselRate",
        "sourceMetric": "us_certStageAmicus_formerClerk_predicted",
        "construct": "elite counsel access",
        "simulatorDenominator": "all generated filed matters",
        "sourceDenominator": "cert-stage amicus/counsel study subset",
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "mechanism_proxy",
        "comparabilityNote": "the source is an effect-size/access signal, not a direct rate of specialist counsel in all filings",
    },
    {
        "pathway": "emergency",
        "simulatorMetric": "emergencyStayDocketRate",
        "sourceMetric": "emergencyStayDocketRate",
        "construct": "emergency application presence",
        "simulatorDenominator": "all generated filed matters",
        "sourceDenominator": "parsed Journal orders or emergency application universe described by source",
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "denominator_mismatch",
        "comparabilityNote": "presence in a synthetic filed universe is not the same denominator as Journal-order emergency applications",
    },
    {
        "pathway": "emergency",
        "simulatorMetric": "emergencyOrderRate",
        "sourceMetric": "emergencyOrderRate",
        "construct": "emergency orders",
        "simulatorDenominator": "all generated filed matters",
        "sourceDenominator": "emergency relief applications/orders in source summaries",
        "dashboardUse": "loose_calibration",
        "denominatorCompatibility": "near_pathway_match",
        "comparabilityNote": "kept as a broad bounded-frequency check rather than a strict application denominator",
    },
    {
        "pathway": "emergency",
        "simulatorMetric": "emergencyGrantConditionalRate",
        "sourceMetric": "noncapitalGrantRate_overall",
        "construct": "emergency relief grants",
        "simulatorDenominator": "simulated emergency orders",
        "sourceDenominator": "all noncapital emergency applications, excluding specified related dismissals",
        "dashboardUse": "loose_calibration",
        "denominatorCompatibility": "conditional_near_match",
        "comparabilityNote": "conditional rate is closer than all-case emergencyGrantRate, but the simulated emergency universe is not limited to noncapital applications",
    },
    {
        "pathway": "emergency",
        "simulatorMetric": "reasonedEmergencyOrderRate",
        "sourceMetric": "noncapitalDissentRate_any",
        "construct": "reason/disagreement visibility",
        "simulatorDenominator": "all generated filed matters",
        "sourceDenominator": "noncapital emergency applications with any public dissent/disagreement",
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "mechanism_proxy",
        "comparabilityNote": "public disagreement is a visibility proxy, not the same as written reasoning",
    },
    {
        "pathway": "emergency",
        "simulatorMetric": "meritsAccelerationPerEmergencyStayDocket",
        "sourceMetric": "noncapitalGrantRate_noLinkedMerits",
        "construct": "merits follow-through",
        "simulatorDenominator": "simulated emergency stay dockets",
        "sourceDenominator": "noncapital emergency applications without linked merits review",
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "mechanism_proxy",
        "comparabilityNote": "the source helps flag weak merits follow-through, but it is not a direct acceleration rate",
    },
    {
        "pathway": "emergency",
        "simulatorMetric": "emergencyDownstreamEffect",
        "sourceMetric": "presidentialEmergencyApplications_peak",
        "construct": "downstream incentive effect",
        "simulatorDenominator": "mean synthetic downstream-effect score",
        "sourceDenominator": "peak historical count/trend context",
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "scale_mismatch",
        "comparabilityNote": "trend context supports mechanism direction, not a numeric rate target",
    },
    {
        "pathway": "complaint_referral",
        "simulatorMetric": "admissionRate",
        "sourceMetric": "spain_amparo_admission_rate",
        "construct": "individual complaint admission",
        "simulatorDenominator": "all generated filed matters across all access paths",
        "sourceDenominator": "Spain amparo admissibility decisions",
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "denominator_mismatch",
        "comparabilityNote": "this is a strong complaint-filter source but not a whole-universe admission target",
    },
    {
        "pathway": "complaint_referral",
        "simulatorMetric": "publicInterestFilteredRate",
        "sourceMetric": "spain_amparo_admissionRate",
        "construct": "public-interest filtering",
        "simulatorDenominator": "all generated filed matters across all access paths",
        "sourceDenominator": "Spain amparo admissibility decisions",
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "denominator_mismatch",
        "comparabilityNote": "comparative complaint filter supports the mechanism, but the simulator metric is not complaint-only",
    },
    {
        "pathway": "complaint_referral",
        "simulatorMetric": "constitutionalRemandRate",
        "sourceMetric": "fr_qpc_delayedEffectRate_decidedQPC",
        "construct": "constitutional remand/deferred remedy",
        "simulatorDenominator": "all generated filed matters",
        "sourceDenominator": "decided QPC cases with delayed effect",
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "mechanism_proxy",
        "comparabilityNote": "QPC delayed effect informs remand/remedy design, not a whole-docket remand prevalence",
    },
    {
        "pathway": "complaint_referral",
        "simulatorMetric": "meritsTransferRate",
        "sourceMetric": "france_qpc_decisions",
        "construct": "filtered referral merits path",
        "simulatorDenominator": "all generated filed matters",
        "sourceDenominator": "annual count of French QPC decisions",
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "count_rate_mismatch",
        "comparabilityNote": "count context cannot validate a simulated transfer rate without a filing denominator",
    },
    {
        "pathway": "lower_court_compliance",
        "simulatorMetric": "lowerCourtCompliance",
        "sourceMetric": "districtCourtAlignmentShockSameDirectionPP",
        "construct": "lower-court alignment",
        "simulatorDenominator": "mean synthetic lower-court compliance score",
        "sourceDenominator": "estimated same-direction percentage-point alignment shock",
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "mechanism_proxy",
        "comparabilityNote": "the source anchors direction and magnitude of alignment pressure, not a compliance-level target",
    },
    {
        "pathway": "lower_court_compliance",
        "simulatorMetric": "lowerCourtResistanceRisk",
        "sourceMetric": "echrEnforcementDomesticJudgmentsThemeShare",
        "construct": "implementation resistance",
        "simulatorDenominator": "mean synthetic resistance-risk score",
        "sourceDenominator": "theme share in enforcement/domestic-judgment material",
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "mechanism_proxy",
        "comparabilityNote": "theme shares justify a resistance channel but do not validate a numeric resistance score",
    },
    {
        "pathway": "lower_court_compliance",
        "simulatorMetric": "governmentNoncomplianceRate",
        "sourceMetric": "federalAgencyNarrowComplianceShare",
        "construct": "government noncompliance",
        "simulatorDenominator": "all generated filed matters",
        "sourceDenominator": "agency implementation cases with narrow compliance in study sample",
        "dashboardUse": "loose_calibration",
        "denominatorCompatibility": "mechanism_proxy",
        "comparabilityNote": "closest available implementation anchor, but still a study-sample proxy rather than a court-wide noncompliance rate",
    },
    {
        "pathway": "lower_court_compliance",
        "simulatorMetric": "interbranchCompliance",
        "sourceMetric": "costaRicaOrdersTrackedShare",
        "construct": "monitoring capacity",
        "simulatorDenominator": "mean synthetic interbranch-compliance score",
        "sourceDenominator": "share of Costa Rica orders tracked by monitoring system",
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "mechanism_proxy",
        "comparabilityNote": "monitoring coverage is institutional capacity context, not realized interbranch compliance",
    },
    {
        "pathway": "override_remand",
        "simulatorMetric": "overrideAttemptRate",
        "sourceMetric": "invalidationRate",
        "construct": "override pressure after invalidation",
        "simulatorDenominator": "all generated filed matters",
        "sourceDenominator": "decisions declaring law unconstitutional",
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "mechanism_proxy",
        "comparabilityNote": "invalidation creates override opportunity, but it is not an override-attempt rate",
    },
    {
        "pathway": "override_remand",
        "simulatorMetric": "overrideRate",
        "sourceMetric": "canada_override_duration_years",
        "construct": "legislative override success",
        "simulatorDenominator": "all generated filed matters",
        "sourceDenominator": "design duration of override effect in years",
        "dashboardUse": "design_prior",
        "denominatorCompatibility": "design_prior",
        "comparabilityNote": "duration informs institutional design, not observed behavioral override success",
    },
    {
        "pathway": "override_remand",
        "simulatorMetric": "rightsCarveoutBlockRate",
        "sourceMetric": "fr_qpc_invalidityRate_decidedQPC",
        "construct": "rights carveout pressure",
        "simulatorDenominator": "all generated filed matters",
        "sourceDenominator": "decided QPC cases with invalidity",
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "mechanism_proxy",
        "comparabilityNote": "comparative invalidity rates inform remedy pressure, not rights-carveout blocking prevalence",
    },
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
    for spec in PATHWAY_ROWS:
        pathway = spec["pathway"]
        simulator_metric = spec["simulatorMetric"]
        source_metric = spec["sourceMetric"]
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
        source_validation_use = joined(
                meta.get("validationUse", set()),
                target.get("guardrailClass", "") if target else ""
        )
        rows.append({
            "pathway": pathway,
            "construct": spec["construct"],
            "simulatorMetric": simulator_metric,
            "currentLikeValue": "" if simulated is None else f"{simulated:.3f}",
            "sourceMetric": source_metric,
            "sourceRange": source_range,
            "sourceObservations": source_observations,
            "sourceTerms": source_terms,
            "sourceKeys": source_keys or joined(meta.get("file", set())),
            "validationUse": spec["dashboardUse"],
            "sourceValidationUse": source_validation_use,
            "confidence": joined(meta.get("confidence", set())),
            "sourceTier": source_tier(source_metric, target, metadata),
            "denominatorCompatibility": spec["denominatorCompatibility"],
            "simulatorDenominator": spec["simulatorDenominator"],
            "sourceDenominator": spec["sourceDenominator"],
            "comparabilityNote": spec["comparabilityNote"],
            "denominatorNote": spec["comparabilityNote"],
            "nextValidationAction": next_action(spec, source_metric, source, target, meta),
        })
    return rows


def next_action(
        spec: dict[str, str],
        source_metric: str,
        source: dict[str, str] | None,
        target: dict[str, str] | None,
        meta: dict[str, set[str]]
) -> str:
    tier = source_tier(source_metric, target, {source_metric: meta})
    if tier == "not_yet_source_backed":
        return "needs primary-source target"
    dashboard_use = spec["dashboardUse"]
    compatibility = spec["denominatorCompatibility"]
    if dashboard_use in {"proxy_context", "design_prior"} or compatibility in {"denominator_mismatch", "mechanism_proxy", "count_rate_mismatch", "scale_mismatch"}:
        return "do not treat as validation; seek direct denominator before causal claims"
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
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Pathway Denominator Audit v1",
        "",
        "This dashboard keeps pathway denominators separate. It does not pool certiorari, emergency applications, individual complaints, QPC/concrete referrals, compliance, and override/remand behavior. The `Use` column is the manuscript-use label after denominator review; `Source use` preserves the source row's original validation-use label.",
        "",
        "| Pathway | Construct | Sim metric | Current-like | Source metric | Source range | Tier | Use | Compatibility | Next action |",
        "| --- | --- | --- | ---: | --- | ---: | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['pathway']} | {row['construct']} | `{row['simulatorMetric']}` | "
            f"{row['currentLikeValue']} | `{row['sourceMetric']}` | {row['sourceRange']} | "
            f"{row['sourceTier']} | {row['validationUse']} | {row['denominatorCompatibility']} | "
            f"{row['nextValidationAction']} |"
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
        writer = csv.DictWriter(handle, fieldnames=list(coverage[0]), lineterminator="\n")
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


def build_metric_semantics_rows(dashboard_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    rows = []
    for row in dashboard_rows:
        rows.append({
            "metricFamily": row["pathway"],
            "metric": row["simulatorMetric"],
            "sourceMetric": row["sourceMetric"],
            "simulatorDenominatorOrScale": row["simulatorDenominator"],
            "sourceDenominatorOrScale": row["sourceDenominator"],
            "empiricalUse": row["validationUse"],
            "denominatorCompatibility": row["denominatorCompatibility"],
            "manuscriptInterpretation": row["comparabilityNote"],
        })
    rows.extend([
        {
            "metricFamily": "headline",
            "metric": "directionalScore",
            "sourceMetric": "",
            "simulatorDenominatorOrScale": "normative average of selected direct and derived synthetic outputs",
            "sourceDenominatorOrScale": "none",
            "empiricalUse": "reading_aid",
            "denominatorCompatibility": "not_empirical_target",
            "manuscriptInterpretation": "used only for ordering and clustering; close score differences are not substantive rankings",
        },
        {
            "metricFamily": "headline",
            "metric": "rightsClaimantSuccess",
            "sourceMetric": "",
            "simulatorDenominatorOrScale": "rights-claimant cases in the generated filed universe, with domain-specific variants reported separately",
            "sourceDenominatorOrScale": "none",
            "empiricalUse": "synthetic_output",
            "denominatorCompatibility": "not_empirical_target",
            "manuscriptInterpretation": "case-average claimant-success output",
        },
        {
            "metricFamily": "headline",
            "metric": "publicConfidence",
            "sourceMetric": "",
            "simulatorDenominatorOrScale": "synthetic legitimacy/confidence index derived from process visibility, emergency legitimacy, partisan alignment, and strategic response",
            "sourceDenominatorOrScale": "none",
            "empiricalUse": "synthetic_output",
            "denominatorCompatibility": "not_empirical_target",
            "manuscriptInterpretation": "compatibility field for the process-legitimacy index",
        },
        {
            "metricFamily": "headline",
            "metric": "processLegitimacyProxy",
            "sourceMetric": "",
            "simulatorDenominatorOrScale": "process visibility, emergency legitimacy, partisan alignment, and strategic response",
            "sourceDenominatorOrScale": "none",
            "empiricalUse": "synthetic_output",
            "denominatorCompatibility": "not_empirical_target",
            "manuscriptInterpretation": "constructed process-legitimacy index",
        },
        {
            "metricFamily": "headline",
            "metric": "emergencyProcessIrregularity",
            "sourceMetric": "",
            "simulatorDenominatorOrScale": "emergency opacity, missing merits follow-through, emergency opportunism, and merits-like relief",
            "sourceDenominatorOrScale": "none",
            "empiricalUse": "synthetic_output",
            "denominatorCompatibility": "not_empirical_target",
            "manuscriptInterpretation": "constructed emergency irregularity index",
        },
        {
            "metricFamily": "headline",
            "metric": "constitutionalConflict",
            "sourceMetric": "",
            "simulatorDenominatorOrScale": "synthetic conflict index from interbranch, lower-court, emergency, override, and compliance channels",
            "sourceDenominatorOrScale": "none",
            "empiricalUse": "synthetic_output",
            "denominatorCompatibility": "not_empirical_target",
            "manuscriptInterpretation": "mechanism summary metric; individual channels remain reported separately",
        },
    ])
    return rows


def write_metric_semantics(rows: list[dict[str, str]]) -> None:
    semantics = build_metric_semantics_rows(rows)
    with METRIC_SEMANTICS_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(semantics[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(semantics)
    lines = [
        "# Metric Semantics v1",
        "",
        "This table records the denominator or scale for each audit metric and separates empirical source comparisons from synthetic outputs and reading aids.",
        "",
        "| Family | Metric | Source metric | Use | Compatibility | Simulator denominator/scale | Source denominator/scale | Interpretation |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in semantics:
        lines.append(
            f"| {row['metricFamily']} | `{row['metric']}` | `{row['sourceMetric']}` | "
            f"{row['empiricalUse']} | {row['denominatorCompatibility']} | "
            f"{row['simulatorDenominatorOrScale']} | {row['sourceDenominatorOrScale']} | "
            f"{row['manuscriptInterpretation']} |"
        )
    METRIC_SEMANTICS_MD.write_text("\n".join(lines) + "\n")


def main() -> None:
    rows = build_dashboard_rows()
    write_dashboard(rows)
    write_coverage(rows)
    write_metric_semantics(rows)
    print(f"Wrote {DASHBOARD_CSV.relative_to(ROOT)}")
    print(f"Wrote {DASHBOARD_MD.relative_to(ROOT)}")
    print(f"Wrote {PRIMARY_COVERAGE_CSV.relative_to(ROOT)}")
    print(f"Wrote {PRIMARY_COVERAGE_MD.relative_to(ROOT)}")
    print(f"Wrote {METRIC_SEMANTICS_CSV.relative_to(ROOT)}")
    print(f"Wrote {METRIC_SEMANTICS_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
