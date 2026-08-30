#!/usr/bin/env python3
"""Build pathway-specific denominator and metric-semantics audits."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
CALIBRATION_DIR = ROOT / "data" / "calibration"
BENCHMARK_DIR = ROOT / "data" / "benchmarks"
CAMPAIGN_CSV = REPORTS / "constitutional-review-campaign-v2.csv"
SOURCE_RANGES_CSV = REPORTS / "calibration-source-ranges-v4.csv"
CALIBRATION_BASELINE_CSV = REPORTS / "calibration-baseline.csv"
SHADOW_DOCKET_SUMMARY_CSV = CALIBRATION_DIR / "shadow-docket-v2-0-summary.csv"
EMERGENCY_LINKAGE_SCHEMA_CSV = BENCHMARK_DIR / "emergency-application-linkage-schema.csv"
EMERGENCY_LINKAGE_TEMPLATE_CSV = BENCHMARK_DIR / "emergency-application-linkage-template.csv"
CERTIORARI_COHORT_SCHEMA_CSV = BENCHMARK_DIR / "certiorari-cohort-schema.csv"
CERTIORARI_COHORT_TEMPLATE_CSV = BENCHMARK_DIR / "certiorari-cohort-template.csv"
IMPLEMENTATION_COMPLIANCE_SCHEMA_CSV = BENCHMARK_DIR / "implementation-compliance-schema.csv"
IMPLEMENTATION_COMPLIANCE_TEMPLATE_CSV = BENCHMARK_DIR / "implementation-compliance-template.csv"
ENVIRONMENTAL_LOWER_COURT_EVENTS_CSV = (
    BENCHMARK_DIR / "lower-court-environmental-treatment-events-v1.csv"
)
ENVIRONMENTAL_CIRCUIT_EXPOSURE_CSV = (
    BENCHMARK_DIR / "lower-court-environmental-circuit-exposure-v1.csv"
)
ENVIRONMENTAL_PRACTICAL_IMPLEMENTATION_CSV = (
    BENCHMARK_DIR / "environmental-practical-implementation-events-v1.csv"
)
BENCHMARK_SOURCE_REGISTRY_CSV = BENCHMARK_DIR / "source-registry.csv"
EMERGENCY_APPLICATION_ORDER_EXTRACT_CSV = (
    BENCHMARK_DIR / "emergency-application-order-extract-shadow-docket-v3-0.csv"
)
EMERGENCY_GRANT_LINKAGE_WORKQUEUE_CSV = (
    BENCHMARK_DIR / "emergency-application-grant-linkage-workqueue-v1.csv"
)
EMERGENCY_DENIED_LINKAGE_WORKQUEUE_CSV = (
    BENCHMARK_DIR / "emergency-application-denied-linkage-workqueue-v1.csv"
)
EMERGENCY_LINKAGE_CODED_CSV = (
    BENCHMARK_DIR / "emergency-application-linkage-coded-v1.csv"
)
EMERGENCY_DENIED_LINKAGE_CODED_CSV = (
    BENCHMARK_DIR / "emergency-application-denied-linkage-coded-v1.csv"
)
CERTIORARI_TERM_FLOW_EXTRACT_CSV = (
    BENCHMARK_DIR / "certiorari-term-flow-extract-journal-ot2023.csv"
)
CERTIORARI_JOURNAL_DISPOSITION_EXTRACT_CSV = (
    BENCHMARK_DIR / "certiorari-journal-disposition-extract-ot2023.csv"
)
CERTIORARI_JOURNAL_DOCKET_DETAIL_CSV = (
    BENCHMARK_DIR / "certiorari-journal-docket-detail-ot2023.csv"
)
CERTIORARI_DOCKETED_COHORT_CSV = (
    BENCHMARK_DIR / "certiorari-docketed-cohort-ot2023.csv"
)
CERTIORARI_GRANTED_DOCKET_DETAIL_CSV = (
    BENCHMARK_DIR / "certiorari-granted-docket-detail-ot2023.csv"
)
DASHBOARD_CSV = REPORTS / "pathway-validation-dashboard-v1.csv"
DASHBOARD_MD = REPORTS / "pathway-validation-dashboard-v1.md"
PRIMARY_COVERAGE_CSV = REPORTS / "primary-source-coverage-v1.csv"
PRIMARY_COVERAGE_MD = REPORTS / "primary-source-coverage-v1.md"
METRIC_SEMANTICS_CSV = REPORTS / "metric-semantics-v1.csv"
METRIC_SEMANTICS_MD = REPORTS / "metric-semantics-v1.md"
BENCHMARK_READINESS_CSV = REPORTS / "benchmark-readiness-v1.csv"
BENCHMARK_READINESS_MD = REPORTS / "benchmark-readiness-v1.md"
BENCHMARK_PROTOCOL_CSV = REPORTS / "benchmark-extraction-protocol-v1.csv"
BENCHMARK_PROTOCOL_MD = REPORTS / "benchmark-extraction-protocol-v1.md"
BENCHMARK_WORKQUEUE_CSV = REPORTS / "benchmark-extraction-workqueue-v1.csv"
BENCHMARK_WORKQUEUE_MD = REPORTS / "benchmark-extraction-workqueue-v1.md"
CERTIORARI_WORKQUEUE_CSV = REPORTS / "certiorari-extraction-workqueue-v1.csv"
CERTIORARI_WORKQUEUE_MD = REPORTS / "certiorari-extraction-workqueue-v1.md"
EMERGENCY_APPLICATION_RECONCILIATION_CSV = REPORTS / "emergency-application-order-reconciliation-v1.csv"
EMERGENCY_APPLICATION_RECONCILIATION_MD = REPORTS / "emergency-application-order-reconciliation-v1.md"
EMERGENCY_GRANT_LINKAGE_WORKQUEUE_MD = REPORTS / "emergency-application-grant-linkage-workqueue-v1.md"
EMERGENCY_DENIED_LINKAGE_WORKQUEUE_MD = REPORTS / "emergency-application-denied-linkage-workqueue-v1.md"
EMERGENCY_FIELD_READINESS_CSV = REPORTS / "emergency-application-field-readiness-v1.csv"
EMERGENCY_FIELD_READINESS_MD = REPORTS / "emergency-application-field-readiness-v1.md"
CERTIORARI_TERM_FLOW_RECONCILIATION_CSV = REPORTS / "certiorari-term-flow-reconciliation-v1.csv"
CERTIORARI_TERM_FLOW_RECONCILIATION_MD = REPORTS / "certiorari-term-flow-reconciliation-v1.md"
CERTIORARI_FIELD_READINESS_CSV = REPORTS / "certiorari-cohort-field-readiness-v1.csv"
CERTIORARI_FIELD_READINESS_MD = REPORTS / "certiorari-cohort-field-readiness-v1.md"
CERTIORARI_COHORT_CLOSURE_PLAN_CSV = REPORTS / "certiorari-cohort-closure-plan-v1.csv"
CERTIORARI_COHORT_CLOSURE_PLAN_MD = REPORTS / "certiorari-cohort-closure-plan-v1.md"
CERTIORARI_MULTI_TERM_BENCHMARK_CSV = (
    REPORTS / "certiorari-multi-term-benchmark-v1.csv"
)
CERTIORARI_MULTI_TERM_BENCHMARK_MD = (
    REPORTS / "certiorari-multi-term-benchmark-v1.md"
)
IMPLEMENTATION_COMPLIANCE_CLOSURE_PLAN_CSV = (
    REPORTS / "implementation-compliance-closure-plan-v1.csv"
)
IMPLEMENTATION_COMPLIANCE_CLOSURE_PLAN_MD = (
    REPORTS / "implementation-compliance-closure-plan-v1.md"
)
IMPLEMENTATION_COMPLIANCE_WORKQUEUE_CSV = (
    REPORTS / "implementation-compliance-workqueue-v1.csv"
)
IMPLEMENTATION_COMPLIANCE_WORKQUEUE_MD = (
    REPORTS / "implementation-compliance-workqueue-v1.md"
)
CERTIORARI_JOURNAL_DISPOSITION_SUMMARY_CSV = REPORTS / "certiorari-journal-disposition-summary-v1.csv"
CERTIORARI_JOURNAL_DISPOSITION_SUMMARY_MD = REPORTS / "certiorari-journal-disposition-summary-v1.md"


CERTIORARI_TERM_FLOW_METRICS = [
    {
        "metricKey": "paidPetitionShare",
        "numeratorKey": "cases_docketed_paid",
        "denominatorKey": "paid_plus_ifp_cases_docketed_during_term",
        "denominatorNote": "Paid share uses paid plus IFP cases docketed during term; the Journal table also reports one original case, so total cases docketed during term is 4,223.",
        "manuscriptUse": "term-flow intake guardrail only; not a closed petition-cohort validation row",
    },
    {
        "metricKey": "ifpPetitionShare",
        "numeratorKey": "cases_docketed_ifp",
        "denominatorKey": "paid_plus_ifp_cases_docketed_during_term",
        "denominatorNote": "IFP share uses paid plus IFP cases docketed during term; the one original case is excluded from the paid/IFP split denominator.",
        "manuscriptUse": "term-flow intake guardrail only; not a closed petition-cohort validation row",
    },
    {
        "metricKey": "grantSetForArgumentRate_raw",
        "numeratorKey": "total_cases_granted_plenary_review",
        "denominatorKey": "total_cases_docketed_during_term",
        "denominatorNote": "Grant-rate context uses total cases granted plenary review over total cases docketed during term; this is same-term flow, not a closed certiorari petition cohort.",
        "manuscriptUse": "proxy context only until linked petition-cohort grants are coded",
    },
]


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
        "sourceDenominator": "2,635 paid certiorari petitions across the closed OT2023 and OT2024 docketed cohorts",
        "dashboardUse": "loose_calibration",
        "denominatorCompatibility": "near_pathway_match",
        "comparabilityNote": "the source denominator is closed and stage-matched, but the simulator represents a constitutional-review subset rather than the full certiorari docket",
    },
    {
        "pathway": "certiorari",
        "simulatorMetric": "ifpCfrRequestRate",
        "sourceMetric": "cfrRate_ifp",
        "construct": "IFP court-requested response",
        "simulatorDenominator": "IFP certiorari-path petitions",
        "sourceDenominator": "5,081 IFP certiorari petitions across the closed OT2023 and OT2024 docketed cohorts",
        "dashboardUse": "loose_calibration",
        "denominatorCompatibility": "near_pathway_match",
        "comparabilityNote": "the source denominator is closed and stage-matched, but the simulator represents a constitutional-review subset rather than the full certiorari docket",
    },
    {
        "pathway": "certiorari",
        "simulatorMetric": "cvsgRequestRate",
        "sourceMetric": "cvsgRequestRate",
        "construct": "CVSG signal",
        "simulatorDenominator": "generated certiorari-path petitions",
        "sourceDenominator": "7,716 certiorari petitions across the closed OT2023 and OT2024 docketed cohorts",
        "dashboardUse": "loose_calibration",
        "denominatorCompatibility": "near_pathway_match",
        "comparabilityNote": "the source supplies term-specific direct petition-level rates for two terms, but the simulator's constitutional-review subset and short time window limit generalization",
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
        "sourceMetric": "lowerCourtFollowedShareAmongDirectionalTreatments_constitutionalIssues",
        "construct": "lower-court doctrinal uptake",
        "simulatorDenominator": "mean synthetic lower-court compliance score",
        "sourceDenominator": (
            "term-pooled followed / (followed + adverse) aggregate Shepard's treatment "
            "counts for 223 constitutional-issue precedents, with responses through 2016"
        ),
        "dashboardUse": "proxy_context",
        "denominatorCompatibility": "scale_mismatch",
        "comparabilityNote": (
            "direct observed aggregate doctrinal treatment is citation/treatment-selected and "
            "citation-weighted, lacks an exposed or ignored-case denominator, and is not the "
            "simulator's synthetic case-average score"
        ),
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


def emergency_grant_linkage_complete() -> bool:
    queue_rows = read_csv(EMERGENCY_GRANT_LINKAGE_WORKQUEUE_CSV)
    coded_rows = read_csv(EMERGENCY_LINKAGE_CODED_CSV)
    if not queue_rows or not coded_rows:
        return False
    queue_ids = {row.get("sourceRecordId", "") for row in queue_rows}
    coded_ids = {row.get("sourceRecordId", "") for row in coded_rows}
    if queue_ids != coded_ids:
        return False
    for row in coded_rows:
        for field in ("statusQuoEffect", "meritsFollowThroughCategory", "downstreamPolicyStatus"):
            if row.get(field) in {"", "uncoded"}:
                return False
        if row.get("linkedMeritsDocket") and not row.get("linkedMeritsDecisionDate"):
            return False
    return True


def emergency_denied_linkage_complete() -> bool:
    queue_rows = read_csv(EMERGENCY_DENIED_LINKAGE_WORKQUEUE_CSV)
    coded_rows = read_csv(EMERGENCY_DENIED_LINKAGE_CODED_CSV)
    if not queue_rows or not coded_rows:
        return False
    queue_ids = {row.get("sourceRecordId", "") for row in queue_rows}
    coded_ids = {row.get("sourceRecordId", "") for row in coded_rows}
    if queue_ids != coded_ids:
        return False
    for row in coded_rows:
        for field in (
            "applicationDate",
            "responseRequested",
            "reasoningPresent",
            "statusQuoEffect",
            "meritsFollowThroughCategory",
            "downstreamPolicyStatus",
            "repeatFilingFlag",
        ):
            if row.get(field) in {"", "uncoded"}:
                return False
    return True


def emergency_linkage_adjustments(row: dict[str, str]) -> dict[str, str]:
    if row["pathway"] != "emergency" or not emergency_grant_linkage_complete():
        return {}
    denied_linkage_complete = emergency_denied_linkage_complete()
    construct = row["construct"].lower()
    metric = row["simulatorMetric"]
    if "follow" in construct or "acceleration" in metric.lower():
        if denied_linkage_complete:
            return {
                "priorityScore": "5",
                "priorityBand": priority_band(5),
                "benchmarkStatus": "all-application docket linkage complete; external implementation still missing",
                "requiredEvidence": "external lower-court or agency implementation observations before claims beyond docket-visible merits linkage",
                "manuscriptUseAfterCompletion": "can support bounded all-application docket-visible merits-linkage diagnostics",
            }
        return {
            "priorityScore": "6",
            "priorityBand": priority_band(6),
            "benchmarkStatus": "granted queue benchmark complete; extend beyond grants",
            "requiredEvidence": "all-application and denied-application rows if the manuscript claims beyond granted emergency applications",
            "manuscriptUseAfterCompletion": "can support bounded granted-emergency merits-follow-through diagnostics",
        }
    if "reason" in construct or "disagreement" in construct:
        if denied_linkage_complete:
            return {
                "priorityScore": "5",
                "priorityBand": priority_band(5),
                "benchmarkStatus": "all-application docket linkage complete for reason visibility",
                "requiredEvidence": "order-text or opinion-text audit if the manuscript claims more than docket-visible reason markers",
                "manuscriptUseAfterCompletion": "can support bounded all-application docket-visible reason-visibility diagnostics",
            }
        return {
            "priorityScore": "6",
            "priorityBand": priority_band(6),
            "benchmarkStatus": "granted queue benchmark complete; extend beyond grants",
            "requiredEvidence": "all-application and denied-application rows if the manuscript claims beyond granted emergency applications",
            "manuscriptUseAfterCompletion": "can support bounded granted-emergency reason-visibility diagnostics",
        }
    if "downstream" in construct:
        if denied_linkage_complete:
            return {
                "priorityScore": "9",
                "priorityBand": priority_band(9),
                "benchmarkStatus": "all-application docket linkage complete; needs external implementation measure",
                "requiredEvidence": "external lower-court or agency implementation observations joined to coded emergency rows",
                "manuscriptUseAfterCompletion": "can support docket-derived all-application downstream status only",
            }
        return {
            "priorityScore": "9",
            "priorityBand": priority_band(9),
            "benchmarkStatus": "grant linkage coded; needs external implementation measure",
            "requiredEvidence": "external lower-court or agency implementation observations joined to the coded granted-emergency rows",
            "manuscriptUseAfterCompletion": "can support docket-derived grant-queue downstream status only",
        }
    return {}


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
            "metricFamily": "rights",
            "metric": "emergencyRightsClaimantSuccess",
            "sourceMetric": "",
            "simulatorDenominatorOrScale": "rights-claimant cases with an emergency route or emergency order in the generated filed universe",
            "sourceDenominatorOrScale": "none",
            "empiricalUse": "synthetic_output",
            "denominatorCompatibility": "not_empirical_target",
            "manuscriptInterpretation": "conditional emergency-route claimant-success output",
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


PATHWAY_PRIORITY = {
    "emergency": 5,
    "certiorari": 4,
    "lower_court_compliance": 3,
    "complaint_referral": 2,
    "override_remand": 2,
}


def int_or_zero(value: str) -> int:
    try:
        return int(float(value or "0"))
    except ValueError:
        return 0


def readiness_status(row: dict[str, str]) -> str:
    compatibility = row["denominatorCompatibility"]
    use = row["validationUse"]
    observations = int_or_zero(row["sourceObservations"])
    if row["pathway"] == "lower_court_compliance":
        cohort_complete = (
            len(read_csv(ENVIRONMENTAL_LOWER_COURT_EVENTS_CSV)) == 191
            and len(read_csv(ENVIRONMENTAL_CIRCUIT_EXPOSURE_CSV)) == 65
            and len(read_csv(ENVIRONMENTAL_PRACTICAL_IMPLEMENTATION_CSV)) == 5
        )
        if cohort_complete:
            metric = row["simulatorMetric"]
            construct = row["construct"].lower()
            if metric == "lowerCourtCompliance":
                return "needs relevant-case opportunity denominator"
            if metric in {"governmentNoncomplianceRate", "lowerCourtResistanceRisk"}:
                return "needs broader outcome and noncompliance coverage"
            if "monitoring" in construct:
                return "bounded monitoring slice; needs broader coverage"
    if use == "design_prior" or compatibility == "design_prior":
        return "design prior only"
    if compatibility == "count_rate_mismatch":
        return "needs count-to-rate denominator"
    if compatibility == "scale_mismatch":
        return "needs linked event measure"
    if compatibility == "denominator_mismatch":
        return "needs pathway-specific denominator"
    if compatibility == "mechanism_proxy":
        return "needs direct behavior benchmark"
    if observations <= 1:
        return "needs term or cohort expansion"
    if row["sourceTier"] in {"research_synthesis", "peer_reviewed_or_scholarly_summary"}:
        return "needs original-source extraction"
    if "near" in compatibility or compatibility == "conditional_near_match":
        return "usable benchmark guardrail"
    return "review evidence boundary"


def benchmark_question(row: dict[str, str]) -> str:
    pathway = row["pathway"]
    construct = row["construct"].lower()
    metric = row["simulatorMetric"]
    if pathway == "certiorari":
        if "cfr" in metric.lower() or "court-requested" in construct:
            return "Are paid and IFP petition-stage CFR rates stable across additional fully enumerated docketed terms?"
        if "cvsg" in metric.lower():
            return "Is the petition-stage CVSG rate stable across additional fully enumerated docketed terms?"
        if "counsel" in construct or "bar" in construct:
            return "Can elite counsel and specialist bar access be benchmarked against petition-stage representation data?"
        if "admission" in metric.lower() or "grant" in construct:
            return "Can certiorari admission be benchmarked within an issue-coded constitutional-review petition subset?"
        if "split" in construct:
            return "Can alleged and genuine split coding be checked on the same rows as petition outcomes?"
        return "Can the intake generator reproduce paid and IFP certiorari composition by term or cohort?"
    if pathway == "emergency":
        if "follow" in construct or "acceleration" in metric.lower():
            return "Can emergency grants be linked to later merits petitions or merits follow-through outcomes?"
        if "downstream" in construct:
            return "Can emergency applications be linked to subsequent policy, compliance, or repeat-filing behavior?"
        if "reason" in construct or "disagreement" in construct:
            return "Can reason-giving, dissents, and full-court referral be coded on the application denominator?"
        return "Can emergency application, order, and grant rates be benchmarked on an application-level denominator?"
    if pathway == "complaint_referral":
        return "Can complaint, amparo, QPC, abstract-review, and concrete-referral pathways be benchmarked on their own filing and decision denominators?"
    if pathway == "lower_court_compliance":
        return (
            "Can the bounded five-decision event/exposure and practical-implementation cohort be "
            "expanded to a broader constitutional-case sample with relevant-case opportunity, "
            "remedy-fidelity, resistance, and noncompliance outcomes?"
        )
    if pathway == "override_remand":
        return "Can invalidation, remand, override attempt, and override success be observed as separate post-decision events?"
    return "Can this metric be benchmarked without pooling unlike legal pathways?"


def required_evidence(row: dict[str, str]) -> str:
    pathway = row["pathway"]
    status = readiness_status(row)
    if pathway == "certiorari":
        construct = row["construct"].lower()
        metric = row["simulatorMetric"].lower()
        if "counsel" in construct or "bar" in construct:
            return "same-row petition representation coding for specialist or former-clerk counsel, represented side, disposition, and denominator rule"
        if "split" in construct:
            return "same-row alleged and genuine split, split depth, issue, vehicle quality, disposition, and denominator rule"
        if "admission" in metric or "grant" in construct:
            return "constitutional-review or issue-coded subset within the closed docketed cohort, with disposition and grant or GVR"
        if "cvsg" in metric:
            return "additional docketed terms using the same closed enumeration and CVSG coding rule"
        if "cfr" in metric or "court-requested" in construct:
            return "additional docketed terms using the same closed enumeration and response or CFR coding rule"
        return "additional docketed terms using the same closed enumeration and paid or IFP intake coding rule"
    if pathway == "emergency":
        return "application-level emergency dataset linking applicant, relief request, reason-giving, grant, merits follow-through, and downstream status"
    if pathway == "complaint_referral":
        return "pathway-specific filing, admission, decision, and remedy time series from official constitutional-court statistics"
    if pathway == "lower_court_compliance":
        return (
            "broader decision and agency coverage with a relevant-case opportunity denominator, "
            "remedy fidelity, and observed resistance or noncompliance outcomes while preserving "
            "the existing event, practical-implementation, and monitoring source boundaries"
        )
    if pathway == "override_remand":
        return "event catalog distinguishing invalidation, delayed remedy, legislative response, override attempt, and override success"
    if status == "needs original-source extraction":
        return "original-source extraction attached to the replication supplement"
    return "direct source extraction with a denominator matching the simulator metric"


def manuscript_use(row: dict[str, str]) -> str:
    status = readiness_status(row)
    if status == "usable benchmark guardrail":
        return "can support a bounded plausibility or benchmark guardrail"
    if status == "needs term or cohort expansion":
        return "keep as loose calibration until term coverage expands"
    if status == "needs original-source extraction":
        return "use only after source rows are attached or independently reproduced"
    if status == "design prior only":
        return "keep as design-context coding, not validation"
    if status in {
        "needs relevant-case opportunity denominator",
        "needs broader outcome and noncompliance coverage",
        "bounded monitoring slice; needs broader coverage",
    }:
        return "use the completed bounded source slice only; do not generalize to denominator-matched validation"
    return "do not frame as validation before the benchmark gap is closed"


def benchmark_priority_score(row: dict[str, str]) -> int:
    score = PATHWAY_PRIORITY.get(row["pathway"], 1)
    compatibility = row["denominatorCompatibility"]
    use = row["validationUse"]
    tier = row["sourceTier"]
    observations = int_or_zero(row["sourceObservations"])
    if use in {"proxy_context", "design_prior"}:
        score += 3
    if compatibility in {"denominator_mismatch", "mechanism_proxy", "count_rate_mismatch", "scale_mismatch"}:
        score += 3
    elif compatibility == "conditional_near_match":
        score += 1
    if tier == "not_yet_source_backed":
        score += 4
    elif tier in {"research_synthesis", "peer_reviewed_or_scholarly_summary"}:
        score += 2
    if observations <= 1:
        score += 1
    return score


def priority_band(score: int) -> str:
    if score >= 10:
        return "A: benchmark blocker"
    if score >= 7:
        return "B: source extraction"
    return "C: guardrail maintenance"


def build_benchmark_readiness_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    ranked = sorted(
        rows,
        key=lambda row: (
            -benchmark_priority_score(row),
            row["pathway"],
            row["construct"],
            row["simulatorMetric"],
        ),
    )
    output = []
    for index, row in enumerate(ranked, start=1):
        score = benchmark_priority_score(row)
        output_row = {
            "priorityRank": str(index),
            "priorityScore": str(score),
            "priorityBand": priority_band(score),
            "pathway": row["pathway"],
            "construct": row["construct"],
            "simulatorMetric": row["simulatorMetric"],
            "currentLikeValue": row["currentLikeValue"],
            "sourceMetric": row["sourceMetric"],
            "sourceTier": row["sourceTier"],
            "validationUse": row["validationUse"],
            "denominatorCompatibility": row["denominatorCompatibility"],
            "sourceObservations": row["sourceObservations"],
            "benchmarkStatus": readiness_status(row),
            "benchmarkQuestion": benchmark_question(row),
            "requiredEvidence": required_evidence(row),
            "manuscriptUseAfterCompletion": manuscript_use(row),
        }
        output_row.update(emergency_linkage_adjustments(row))
        output.append(output_row)
    output.sort(
        key=lambda row: (
            -int(row["priorityScore"]),
            row["pathway"],
            row["construct"],
            row["simulatorMetric"],
        )
    )
    for index, row in enumerate(output, start=1):
        row["priorityRank"] = str(index)
    return output


def markdown_cell(value: str) -> str:
    return value.replace("|", "\\|")


def term_sort_key(term: str) -> tuple[int, str]:
    digits = "".join(character for character in term if character.isdigit())
    return (int(digits) if digits else -1, term)


def build_certiorari_multi_term_benchmark_rows() -> list[dict[str, str]]:
    paths = sorted(
        CALIBRATION_DIR.glob("scotus-certiorari-docketed-cohort-ot*.csv")
    )
    if len(paths) < 2:
        raise SystemExit(
            "Multi-term certiorari benchmark requires at least two closed "
            "term calibration files."
        )

    by_term: dict[str, dict[str, dict[str, str]]] = {}
    for path in paths:
        rows = read_csv(path)
        terms = {row.get("term", "") for row in rows if row.get("term")}
        if len(terms) != 1:
            raise SystemExit(
                f"{path.relative_to(ROOT)} must contain exactly one term."
            )
        term = next(iter(terms))
        metrics: dict[str, dict[str, str]] = {}
        for row in rows:
            metric = row.get("metric", "")
            if not metric or metric in metrics:
                raise SystemExit(
                    f"{path.relative_to(ROOT)} has a blank or duplicate metric."
                )
            try:
                numerator = int(row["numerator"])
                denominator = int(row["denominator"])
                value = float(row["value"])
            except (KeyError, ValueError) as error:
                raise SystemExit(
                    f"{path.relative_to(ROOT)} has invalid ratio data for "
                    f"{metric!r}."
                ) from error
            if (
                denominator <= 0
                or numerator < 0
                or numerator > denominator
                or abs(value - numerator / denominator) > 1e-8
            ):
                raise SystemExit(
                    f"{path.relative_to(ROOT)} has an inconsistent ratio for "
                    f"{metric!r}."
                )
            metrics[metric] = row
        by_term[term] = metrics

    terms = sorted(by_term, key=term_sort_key)
    metric_sets = {frozenset(metrics) for metrics in by_term.values()}
    if len(metric_sets) != 1:
        raise SystemExit(
            "Closed certiorari term files do not expose the same metric set."
        )

    first_term = terms[0]
    latest_term = terms[-1]
    output: list[dict[str, str]] = []
    for metric in sorted(next(iter(metric_sets))):
        term_rows = [by_term[term][metric] for term in terms]
        values = [float(row["value"]) for row in term_rows]
        pooled_numerator = sum(int(row["numerator"]) for row in term_rows)
        pooled_denominator = sum(int(row["denominator"]) for row in term_rows)
        first = by_term[first_term][metric]
        latest = by_term[latest_term][metric]
        output.append(
            {
                "metric": metric,
                "termCount": str(len(terms)),
                "terms": ";".join(terms),
                "termValues": ";".join(
                    f"{term}={float(by_term[term][metric]['value']):.9f}"
                    for term in terms
                ),
                "firstTerm": first_term,
                "firstNumerator": first["numerator"],
                "firstDenominator": first["denominator"],
                "firstValue": f"{float(first['value']):.9f}",
                "latestTerm": latest_term,
                "latestNumerator": latest["numerator"],
                "latestDenominator": latest["denominator"],
                "latestValue": f"{float(latest['value']):.9f}",
                "absoluteChange": (
                    f"{float(latest['value']) - float(first['value']):.9f}"
                ),
                "rangeAcrossTerms": f"{max(values) - min(values):.9f}",
                "pooledNumerator": str(pooled_numerator),
                "pooledDenominator": str(pooled_denominator),
                "pooledValue": f"{pooled_numerator / pooled_denominator:.9f}",
                "sourceKeys": ";".join(
                    by_term[term][metric]["sourceKey"] for term in terms
                ),
                "sourceUrl": latest["sourceUrl"],
                "manuscriptUse": (
                    "descriptive multi-term docketed-intake benchmark; not "
                    "constitutional-review-only, causal, or a census of "
                    "undocketed submissions"
                ),
                "notes": (
                    "Pooled value is the ratio of summed term numerators to "
                    "summed term denominators; absolute change is latest minus "
                    f"first term. Source definition: {latest['notes']}"
                ),
            }
        )
    return output


def write_certiorari_multi_term_benchmark() -> None:
    rows = build_certiorari_multi_term_benchmark_rows()
    with CERTIORARI_MULTI_TERM_BENCHMARK_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0]),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)

    first_term = rows[0]["firstTerm"]
    latest_term = rows[0]["latestTerm"]
    lines = [
        "# Certiorari Multi-Term Benchmark v1",
        "",
        (
            "This generated report compares independently enumerated official "
            f"docketed-intake cohorts from {first_term} through {latest_term}. "
            "Each source term preserves its own paid/IFP and petition-stage "
            "denominators."
        ),
        "",
        (
            "The comparison is descriptive. It is not a constitutional-review-"
            "only cohort, a causal estimate, or a census of submissions that "
            "were never docketed. The OT2024 cohort follows the Journal's "
            "published paid/IFP count snapshot; its manifest separately records "
            "same-cutoff-date public dockets above those count-defined ranges. "
            "Three OT2024 petitions remain pending or held at the snapshot, so "
            "the grant/GVR row uses the 3,680 resolved petitions."
        ),
        "",
        "| Metric | First term | Latest term | Change (pp) | Pooled | Term range (pp) |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        first = 100 * float(row["firstValue"])
        latest = 100 * float(row["latestValue"])
        change = 100 * float(row["absoluteChange"])
        pooled = 100 * float(row["pooledValue"])
        spread = 100 * float(row["rangeAcrossTerms"])
        lines.append(
            f"| `{markdown_cell(row['metric'])}` | "
            f"{first:.2f}% ({row['firstNumerator']}/{row['firstDenominator']}) | "
            f"{latest:.2f}% ({row['latestNumerator']}/{row['latestDenominator']}) | "
            f"{change:+.2f} | {pooled:.2f}% "
            f"({row['pooledNumerator']}/{row['pooledDenominator']}) | "
            f"{spread:.2f} |"
        )
    CERTIORARI_MULTI_TERM_BENCHMARK_MD.write_text(
        "\n".join(lines) + "\n"
    )


def write_benchmark_readiness(rows: list[dict[str, str]]) -> None:
    benchmark_rows = build_benchmark_readiness_rows(rows)
    with BENCHMARK_READINESS_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(benchmark_rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(benchmark_rows)

    lines = [
        "# Benchmark Readiness v1",
        "",
        "This report turns the pathway denominator audit into a benchmark and back-test work queue. It does not add empirical validation by itself; it identifies which source extractions would be needed before stronger validation language would be justified.",
        "",
        "| Rank | Band | Pathway | Construct | Sim metric | Evidence state | Benchmark gap | Required evidence | Manuscript use |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in benchmark_rows:
        evidence = (
            f"{row['sourceTier']}; {row['validationUse']}; "
            f"{row['denominatorCompatibility']}; n={row['sourceObservations'] or '0'}"
        )
        lines.append(
            f"| {row['priorityRank']} | {markdown_cell(row['priorityBand'])} | "
            f"{markdown_cell(row['pathway'])} | {markdown_cell(row['construct'])} | "
            f"`{markdown_cell(row['simulatorMetric'])}` | {markdown_cell(evidence)} | "
            f"{markdown_cell(row['benchmarkStatus'])} | {markdown_cell(row['requiredEvidence'])} | "
            f"{markdown_cell(row['manuscriptUseAfterCompletion'])} |"
        )
    BENCHMARK_READINESS_MD.write_text("\n".join(lines) + "\n")


PROTOCOL_TARGETS = [
    {
        "targetKey": "merits_followthrough",
        "benchmarkTarget": "emergency merits follow-through",
        "pathway": "emergency",
        "schemaPath": EMERGENCY_LINKAGE_SCHEMA_CSV,
        "metrics": ["meritsAccelerationPerEmergencyStayDocket", "emergencyGrantConditionalRate"],
        "requiredSourceUnit": "one row per emergency application or interim-relief request",
        "completionRule": "each granted or otherwise resolved emergency application has a disposition and linked-merits category",
        "validationUpgrade": "can convert merits-follow-through rows from mechanism proxy to direct benchmark or loose calibration",
        "firstExtractionSlice": "noncapital emergency applications with grants in the existing OT2003-OT2021 source window",
    },
    {
        "targetKey": "reason_visibility",
        "benchmarkTarget": "emergency reason and public-disagreement visibility",
        "pathway": "emergency",
        "schemaPath": EMERGENCY_LINKAGE_SCHEMA_CSV,
        "metrics": ["reasonedEmergencyOrderRate"],
        "requiredSourceUnit": "one row per emergency disposition",
        "completionRule": "each disposition records response request, reasoning, public disagreement, and full-court referral when visible",
        "validationUpgrade": "can separate written-reasoning benchmarks from dissent or disagreement proxies",
        "firstExtractionSlice": "applications with public writings or noted dissents in the existing noncapital emergency source window",
    },
    {
        "targetKey": "downstream_effect",
        "benchmarkTarget": "emergency downstream implementation effect",
        "pathway": "emergency",
        "schemaPath": EMERGENCY_LINKAGE_SCHEMA_CSV,
        "metrics": ["emergencyDownstreamEffect"],
        "requiredSourceUnit": "one row per granted emergency application plus linked implementation observation",
        "completionRule": "each row classifies status-quo effect, linked merits result, and downstream policy status",
        "validationUpgrade": "can replace peak-count context with a direct event-linkage benchmark",
        "firstExtractionSlice": "presidential or government emergency applications in the currently cited peak-period source row",
    },
    {
        "targetKey": "application_presence",
        "benchmarkTarget": "emergency application denominator",
        "pathway": "emergency",
        "schemaPath": EMERGENCY_LINKAGE_SCHEMA_CSV,
        "metrics": ["emergencyStayDocketRate", "emergencyOrderRate"],
        "requiredSourceUnit": "one row per application with term and source-record identifier",
        "completionRule": "application counts and order counts are separated from all Journal-order denominators",
        "validationUpgrade": "can turn the emergency-application presence row from denominator mismatch into a pathway-specific rate",
        "firstExtractionSlice": "2003-2024 shadow-docket rows already summarized in the normalized calibration file",
    },
    {
        "targetKey": "cert_petition_denominator",
        "benchmarkTarget": "certiorari petition denominator",
        "pathway": "certiorari",
        "schemaPath": CERTIORARI_COHORT_SCHEMA_CSV,
        "metrics": ["paidCertPetitionShare", "ifpCertPetitionShare", "certiorariAdmissionRate"],
        "requiredSourceUnit": "one row per docketed certiorari petition or term-flow petition record",
        "completionRule": "closed petition cohort separates paid and IFP filing, disposition, grant, and set-for-argument status",
        "validationUpgrade": "can move paid/IFP intake and certiorari admission from term-flow guardrails toward petition-cohort benchmarks",
        "firstExtractionSlice": "OT2023-OT2024 official docketed cohorts complete; next add another mature term or an issue-coded constitutional-review subset",
    },
    {
        "targetKey": "cert_cfr_response",
        "benchmarkTarget": "certiorari response and CFR stage",
        "pathway": "certiorari",
        "schemaPath": CERTIORARI_COHORT_SCHEMA_CSV,
        "metrics": ["paidCfrRequestRate", "ifpCfrRequestRate"],
        "requiredSourceUnit": "one row per paid or IFP petition with response and CFR status",
        "completionRule": "each petition has paid/IFP status, response status, CFR flag or date, respondent category, and disposition",
        "validationUpgrade": "can benchmark CFR and response-stage sorting without pooling paid and IFP petitions",
        "firstExtractionSlice": "OT2023-OT2024 direct CFR incidence complete; next add respondent and SG-response coding or another mature term",
    },
    {
        "targetKey": "cert_cvsg_signal",
        "benchmarkTarget": "certiorari CVSG signal",
        "pathway": "certiorari",
        "schemaPath": CERTIORARI_COHORT_SCHEMA_CSV,
        "metrics": ["cvsgRequestRate"],
        "requiredSourceUnit": "one row per petition eligible for or receiving a CVSG",
        "completionRule": "CVSG request, SG recommendation, Court follow-through, and disposition are coded on a known petition denominator",
        "validationUpgrade": "can replace count-per-year CVSG context with a petition-stage CVSG rate and recommendation benchmark",
        "firstExtractionSlice": "OT2023-OT2024 direct CVSG-request incidence complete; next add SG recommendation and Court-follow-through coding",
    },
    {
        "targetKey": "cert_elite_counsel",
        "benchmarkTarget": "certiorari elite counsel and amicus access",
        "pathway": "certiorari",
        "schemaPath": CERTIORARI_COHORT_SCHEMA_CSV,
        "metrics": ["specialistCounselRate"],
        "requiredSourceUnit": "one row per petition with counsel, former-clerk, and cert-stage amicus indicators when source permits",
        "completionRule": "counsel and amicus signals are coded without reducing the denominator to only high-success attorney subsets",
        "validationUpgrade": "can separate access/salience proxy evidence from direct specialist-counsel prevalence benchmarks",
        "firstExtractionSlice": "Feldman-Kappner filtered elite-counsel rows and Lazarus OT2005 non-SG amicus rows as bounded proxy slices",
    },
    {
        "targetKey": "cert_split_quality",
        "benchmarkTarget": "certiorari split-quality coding",
        "pathway": "certiorari",
        "schemaPath": CERTIORARI_COHORT_SCHEMA_CSV,
        "metrics": ["genuineLowerCourtSplitRate"],
        "requiredSourceUnit": "one row per petition or conflict observation with alleged and genuine split coding",
        "completionRule": "alleged split, genuine split, split depth, maturity, and disposition are coded in the same petition or conflict sample",
        "validationUpgrade": "can test alleged-versus-genuine split logic before treating split quality as a direct petition benchmark",
        "firstExtractionSlice": "Beim-Rader conflict rows as a secondary split-quality proxy before locating underlying petition records",
    },
]


def schema_field_names(schema_path: Path) -> list[str]:
    return [row["fieldName"] for row in read_csv(schema_path)]


def schema_fields_for_targets(
        target_keys: list[str],
        required_label: str,
        schema_path: Path = EMERGENCY_LINKAGE_SCHEMA_CSV
) -> str:
    fields = []
    for row in read_csv(schema_path):
        targets = {item.strip() for item in row["requiredFor"].split(";")}
        if "all" not in targets and not any(target_key in targets for target_key in target_keys):
            continue
        if row["validationUse"] != required_label:
            continue
        fields.append(row["fieldName"])
    return "; ".join(dict.fromkeys(fields))


def schema_fields(
        target_key: str,
        required_label: str,
        schema_path: Path = EMERGENCY_LINKAGE_SCHEMA_CSV
) -> str:
    return schema_fields_for_targets([target_key], required_label, schema_path)


def source_registry_summary(pathway: str) -> str:
    rows = [row for row in read_csv(BENCHMARK_SOURCE_REGISTRY_CSV) if row["pathway"] == pathway]
    parts = []
    for row in rows:
        parts.append(f"{row['sourceKey']} ({row['benchmarkStatus']})")
    return "; ".join(parts)


def readiness_links(rows: list[dict[str, str]], metrics: list[str]) -> str:
    matched = [
        f"#{row['priorityRank']} {row['simulatorMetric']}: {row['benchmarkStatus']}"
        for row in build_benchmark_readiness_rows(rows)
        if row["simulatorMetric"] in metrics
    ]
    return "; ".join(matched)


def current_evidence_limits(rows: list[dict[str, str]], metrics: list[str]) -> str:
    matched = []
    for row in build_benchmark_readiness_rows(rows):
        if row["simulatorMetric"] not in metrics:
            continue
        matched.append(
            f"{row['sourceTier']}/{row['denominatorCompatibility']}/n={row['sourceObservations'] or '0'}"
        )
    return "; ".join(matched)


def build_benchmark_protocol_rows(dashboard_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    output = []
    for index, target in enumerate(PROTOCOL_TARGETS, start=1):
        schema_path = target.get("schemaPath", EMERGENCY_LINKAGE_SCHEMA_CSV)
        output.append({
            "protocolRank": str(index),
            "targetKey": target["targetKey"],
            "benchmarkTarget": target["benchmarkTarget"],
            "pathway": target["pathway"],
            "simulatorMetrics": "; ".join(target["metrics"]),
            "blockingReadinessRows": readiness_links(dashboard_rows, target["metrics"]),
            "currentEvidenceLimit": current_evidence_limits(dashboard_rows, target["metrics"]),
            "requiredSourceUnit": target["requiredSourceUnit"],
            "requiredFields": schema_fields(target["targetKey"], "required", schema_path),
            "recommendedFields": schema_fields(target["targetKey"], "recommended", schema_path),
            "candidateSources": source_registry_summary(target["pathway"]),
            "completionRule": target["completionRule"],
            "validationUpgrade": target["validationUpgrade"],
            "firstExtractionSlice": target["firstExtractionSlice"],
        })
    return output


def write_benchmark_protocol(rows: list[dict[str, str]]) -> None:
    protocol_rows = build_benchmark_protocol_rows(rows)
    with BENCHMARK_PROTOCOL_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(protocol_rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(protocol_rows)

    lines = [
        "# Benchmark Extraction Protocol v1",
        "",
        "This protocol defines the source extraction needed to close the highest-priority emergency and certiorari benchmark gaps. It is generated from `data/benchmarks/`, `data/benchmarks/source-registry.csv`, and the pathway denominator audit.",
        "",
        "| Rank | Target | Metrics | Current evidence limit | Required source unit | Required fields | Completion rule | Validation upgrade | First extraction slice |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in protocol_rows:
        lines.append(
            f"| {row['protocolRank']} | {markdown_cell(row['benchmarkTarget'])} | "
            f"`{markdown_cell(row['simulatorMetrics'])}` | {markdown_cell(row['currentEvidenceLimit'])} | "
            f"{markdown_cell(row['requiredSourceUnit'])} | {markdown_cell(row['requiredFields'])} | "
            f"{markdown_cell(row['completionRule'])} | {markdown_cell(row['validationUpgrade'])} | "
            f"{markdown_cell(row['firstExtractionSlice'])} |"
        )
    BENCHMARK_PROTOCOL_MD.write_text("\n".join(lines) + "\n")


def write_schema_template(schema_csv: Path, template_csv: Path) -> None:
    fieldnames = schema_field_names(schema_csv)
    with template_csv.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()


def calibration_metric_index() -> dict[str, dict[str, str]]:
    output: dict[str, dict[str, str]] = {}
    for path in CALIBRATION_DIR.rglob("*.csv"):
        for row in read_csv(path):
            metric = row.get("metricKey") or row.get("metric")
            if not metric:
                continue
            enriched = dict(row)
            enriched["_relativePath"] = path.relative_to(ROOT).as_posix()
            output.setdefault(metric, enriched)
    return output


def metric_row_text(metric_rows: dict[str, dict[str, str]], metric: str) -> str:
    row = metric_rows.get(metric, {})
    return (
        row.get("rawObservedValue")
        or row.get("observedValue")
        or row.get("value")
        or row.get("numerator")
        or ""
    )


def metric_source_names(metric_rows: dict[str, dict[str, str]], metrics: list[str]) -> str:
    names = [
        metric_rows[metric].get("sourceName", "")
        for metric in metrics
        if metric in metric_rows and metric_rows[metric].get("sourceName")
    ]
    return "; ".join(dict.fromkeys(names))


def metric_source_urls(metric_rows: dict[str, dict[str, str]], metrics: list[str]) -> str:
    urls = [
        metric_rows[metric].get("sourceUrl", "")
        for metric in metrics
        if metric in metric_rows and metric_rows[metric].get("sourceUrl")
    ]
    return "; ".join(dict.fromkeys(urls))


def metric_period(metric_rows: dict[str, dict[str, str]], metric: str, fallback: str) -> str:
    return metric_rows.get(metric, {}).get("timePeriod") or fallback


def protocol_lookup(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {row["targetKey"]: row for row in build_benchmark_protocol_rows(rows)}


def build_benchmark_workqueue_rows(dashboard_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    metric_rows = calibration_metric_index()
    protocols = protocol_lookup(dashboard_rows)
    output: list[dict[str, str]] = []

    def add_row(row: dict[str, str]) -> None:
        row["queueRank"] = str(len(output) + 1)
        output.append(row)

    def aggregate_row(
        target_key: str,
        source_metrics: list[str],
        unit_of_work: str,
        observed_applications_metric: str,
        observed_grants_metric: str,
        observed_disagreement_metric: str,
        coder_action: str,
        completion_evidence: str,
        term_or_period: str = "",
    ) -> None:
        protocol = protocols[target_key]
        add_row({
            "queueRank": "",
            "targetKey": target_key,
            "benchmarkTarget": protocol["benchmarkTarget"],
            "sourceKey": "supreme-court-simulator-calibration-targets",
            "sourceName": metric_source_names(metric_rows, source_metrics),
            "sourceMetric": "; ".join(source_metrics),
            "sourceUrl": metric_source_urls(metric_rows, source_metrics),
            "termOrPeriod": term_or_period or metric_period(metric_rows, observed_applications_metric, ""),
            "unitOfWork": unit_of_work,
            "observedApplications": metric_row_text(metric_rows, observed_applications_metric),
            "observedGrantedApplications": metric_row_text(metric_rows, observed_grants_metric),
            "observedPublicDisagreement": metric_row_text(metric_rows, observed_disagreement_metric),
            "requiredFields": protocol["requiredFields"],
            "recommendedFields": protocol["recommendedFields"],
            "coderAction": coder_action,
            "completionEvidence": completion_evidence,
            "manuscriptUse": "not validation until row-level extraction satisfies the completion rule",
        })

    aggregate_row(
        "merits_followthrough",
        ["noncapitalApplications_total", "noncapitalGrantRate_overall", "noncapitalGrantRate_noLinkedMerits"],
        "all granted noncapital emergency applications in the existing Goelzhauser source window",
        "noncapitalApplications_total",
        "noncapitalGrantRate_overall",
        "",
        "extract one row per granted noncapital application and code linked merits docket plus merits-follow-through category",
        "granted application rows reconcile to the source application count and every granted row has linkedMeritsDocket or meritsFollowThroughCategory=none",
        "OT2003-OT2021",
    )
    aggregate_row(
        "reason_visibility",
        ["noncapitalApplications_total", "noncapitalExplanationRate_any", "noncapitalDissentRate_any"],
        "noncapital emergency dispositions with public explanation or disagreement fields",
        "noncapitalApplications_total",
        "",
        "noncapitalDissentRate_any",
        "extract one row per noncapital disposition and code reasoningPresent publicDisagreement responseRequested and fullCourtReferral when visible",
        "coded rows reproduce the source explanation and dissent/disagreement rates before being used as transparency benchmarks",
        "OT2003-OT2021",
    )
    aggregate_row(
        "downstream_effect",
        ["presidentialEmergencyApplications_peak"],
        "presidential or government emergency applications in the cited peak-period trend source",
        "presidentialEmergencyApplications_peak",
        "",
        "",
        "link each government emergency application to status-quo effect and later implementation or policy status",
        "each row has statusQuoEffect plus either downstreamPolicyStatus or a documented unavailable-source note",
        metric_period(metric_rows, "presidentialEmergencyApplications_peak", "peak period in cited source"),
    )

    term_metrics: dict[str, dict[str, dict[str, str]]] = defaultdict(dict)
    for row in read_csv(SHADOW_DOCKET_SUMMARY_CSV):
        if row.get("domain") != "emergency":
            continue
        term_metrics[row["term"]][row["metric"]] = row
    extracted_terms = {
        row["term"]
        for row in read_csv(EMERGENCY_APPLICATION_ORDER_EXTRACT_CSV)
        if row.get("sourceKey") == "shadow-docket-v3-0"
    }
    coded_grant_terms = {
        row.get("term", "").removeprefix("OT")
        for row in read_csv(EMERGENCY_LINKAGE_CODED_CSV)
        if row.get("term", "").startswith("OT")
    }
    coded_denied_terms = {
        row.get("term", "").removeprefix("OT")
        for row in read_csv(EMERGENCY_DENIED_LINKAGE_CODED_CSV)
        if row.get("term", "").startswith("OT")
    }
    grant_linkage_complete = emergency_grant_linkage_complete()
    denied_linkage_complete = emergency_denied_linkage_complete()

    protocol = protocols["application_presence"]
    for term in sorted(term_metrics, key=lambda item: int(item)):
        if int(term) < 2003:
            continue
        metrics = term_metrics[term]
        presence = metrics.get("emergencyStayDocketRate")
        if not presence:
            continue
        grants = metrics.get("emergencyOrderRate", {})
        disagreement = metrics.get("shadowDocketAbuse", {})
        has_extract = term in extracted_terms
        has_coded_grants = has_extract and grant_linkage_complete and term in coded_grant_terms
        has_coded_all_app = (
            has_coded_grants
            and denied_linkage_complete
            and term in coded_denied_terms
        )
        add_row({
            "queueRank": "",
            "targetKey": "application_presence",
            "benchmarkTarget": protocol["benchmarkTarget"],
            "sourceKey": "shadow-docket-v3-0" if has_extract else presence.get("sourceKey", "shadow-docket-v2-0"),
            "sourceName": "Supreme Court Shadow Docket Database term summary",
            "sourceMetric": "emergencyStayDocketRate; emergencyOrderRate; shadowDocketAbuse",
            "sourceUrl": presence.get("sourceUrl", ""),
            "termOrPeriod": f"OT{term}",
            "unitOfWork": (
                f"OT{term} compact application-level extract and all-application official-docket linkage are coded"
                if has_coded_all_app
                else (
                    f"OT{term} compact application-level extract exists and granted-row linkage benchmark is coded"
                    if has_coded_grants
                    else (
                        f"OT{term} compact application-level extract exists; next code merits follow-through and downstream fields"
                        if has_extract
                        else f"replace OT{term} term summary with application-level rows and source-record identifiers"
                    )
                )
            ),
            "observedApplications": presence.get("numerator", ""),
            "observedGrantedApplications": grants.get("numerator", ""),
            "observedPublicDisagreement": disagreement.get("numerator", ""),
            "requiredFields": schema_fields_for_targets(["application_presence", "grant_rate", "reason_visibility"], "required"),
            "recommendedFields": schema_fields_for_targets(["application_presence", "grant_rate", "reason_visibility"], "recommended"),
            "coderAction": (
                "preserve the all-application docket linkage; add external implementation observations or order/opinion text before claims beyond docket-visible markers"
                if has_coded_all_app
                else (
                    "extend beyond granted rows only if all-application denied-emergency or external implementation claims are made"
                    if has_coded_grants
                    else (
                        "extend the compact row-level extract with application filing date merits linkage status-quo effect and downstream policy status"
                        if has_extract
                        else "extract one row per emergency application for this term and reconcile application grant and public-disagreement counts to the summary"
                    )
                )
            ),
            "completionEvidence": (
                "compact application-level row counts reconcile to observedApplications, grants, and public-disagreement subtotals; granted and denied/NA rows have official-docket linkage coding"
                if has_coded_all_app
                else (
                    "compact application-level row counts reconcile to observedApplications grants and public-disagreement subtotals; granted rows have official-docket linkage coding"
                    if has_coded_grants
                    else (
                        "compact application-level row counts reconcile to observedApplications grants and public-disagreement subtotals; linkage fields remain uncoded"
                        if has_extract
                        else "application-level row counts equal observedApplications and grant/disagreement subtotals reconcile to the term summary or are explicitly explained"
                    )
                )
            ),
            "manuscriptUse": (
                "application-level denominator guardrail plus bounded all-application docket-visible linkage diagnostics"
                if has_coded_all_app
                else (
                    "application-level denominator guardrail plus bounded granted-emergency linkage diagnostics"
                    if has_coded_grants
                    else (
                        "application-level denominator guardrail only; not merits-follow-through or downstream-effect validation"
                        if has_extract
                        else "not validation until the term has application-level rows with sourceRecordId and docketNumber"
                    )
                )
            ),
        })

    return output


def write_benchmark_workqueue(rows: list[dict[str, str]]) -> None:
    workqueue_rows = build_benchmark_workqueue_rows(rows)
    with BENCHMARK_WORKQUEUE_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(workqueue_rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(workqueue_rows)

    lines = [
        "# Benchmark Extraction Work Queue v1",
        "",
        "This generated work queue turns the emergency-application extraction protocol into concrete source-coding tasks. It is not validation evidence; it records the first source units that must be replaced by application-level rows before the manuscript can claim stronger emergency benchmarks.",
        "",
        "| Rank | Target | Source | Period | Applications | Grants | Public disagreement | Unit of work | Completion evidence |",
        "| ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |",
    ]
    for row in workqueue_rows:
        lines.append(
            f"| {row['queueRank']} | {markdown_cell(row['benchmarkTarget'])} | "
            f"{markdown_cell(row['sourceKey'])} | {markdown_cell(row['termOrPeriod'])} | "
            f"{markdown_cell(row['observedApplications'])} | {markdown_cell(row['observedGrantedApplications'])} | "
            f"{markdown_cell(row['observedPublicDisagreement'])} | {markdown_cell(row['unitOfWork'])} | "
            f"{markdown_cell(row['completionEvidence'])} |"
        )
    BENCHMARK_WORKQUEUE_MD.write_text("\n".join(lines) + "\n")


def metric_periods(metric_rows: dict[str, dict[str, str]], metrics: list[str], fallback: str = "") -> str:
    periods = [
        metric_rows[metric].get("timePeriod", "")
        for metric in metrics
        if metric in metric_rows and metric_rows[metric].get("timePeriod")
    ]
    return "; ".join(dict.fromkeys(periods)) or fallback


def metric_observed_signal(metric_rows: dict[str, dict[str, str]], metrics: list[str]) -> str:
    parts = []
    for metric in metrics:
        value = metric_row_text(metric_rows, metric)
        if value:
            parts.append(f"{metric}: {value}")
    return "; ".join(parts)


def build_certiorari_workqueue_rows(dashboard_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    metric_rows = calibration_metric_index()
    protocols = protocol_lookup(dashboard_rows)
    registry = {
        row["sourceKey"]: row
        for row in read_csv(BENCHMARK_SOURCE_REGISTRY_CSV)
    }
    output: list[dict[str, str]] = []

    def add_row(
        target_key: str,
        source_key: str,
        source_metrics: list[str],
        period_or_sample: str,
        unit_of_work: str,
        coder_action: str,
        completion_evidence: str,
        manuscript_use: str = "not validation until row-level extraction satisfies the completion rule",
    ) -> None:
        protocol = protocols[target_key]
        output.append({
            "queueRank": str(len(output) + 1),
            "targetKey": target_key,
            "benchmarkTarget": protocol["benchmarkTarget"],
            "sourceKey": source_key,
            "sourceName": (
                registry.get(source_key, {}).get("sourceName")
                or metric_source_names(metric_rows, source_metrics)
            ),
            "sourceMetric": "; ".join(source_metrics),
            "sourceUrl": (
                registry.get(source_key, {}).get("sourceUrl")
                or metric_source_urls(metric_rows, source_metrics)
            ),
            "periodOrSample": period_or_sample or metric_periods(metric_rows, source_metrics),
            "unitOfWork": unit_of_work,
            "observedSourceSignal": metric_observed_signal(metric_rows, source_metrics),
            "requiredFields": protocol["requiredFields"],
            "recommendedFields": protocol["recommendedFields"],
            "coderAction": coder_action,
            "completionEvidence": completion_evidence,
            "manuscriptUse": manuscript_use,
        })

    add_row(
        "cert_petition_denominator",
        "scotus-certiorari-docketed-cohorts-ot2023-ot2024",
        ["paidPetitionShare", "ifpPetitionShare", "grantSetForArgumentRate_raw"],
        "OT2023-OT2024",
        "maintain the paired official-docket cohorts and extend the same count-defined enumeration to the next mature term",
        "preserve paid, IFP, petition type, docket-visible procedure, disposition, snapshot boundary, and source-page provenance for every enumerated docket",
        "OT2023 and OT2024 separately reconcile to 4,222 and 3,854 paid/IFP dockets; the paired files contain 7,716 certiorari petitions, with the three OT2024 pending outcomes retained explicitly",
        "completed two-term docketed-intake guardrail; descriptive only and not a census of undocketed submissions or a constitutional-review-only cohort",
    )
    add_row(
        "cert_cfr_response",
        "thompson-wachtell-certiorari",
        [
            "cfrRate_paid",
            "cfrRate_ifp",
            "certGrantRateAfterCFR_paid",
            "certGrantRateAfterCFR_ifp",
            "sgVoluntaryResponseRate_USRespondent_paid",
            "sgVoluntaryResponseRate_USRespondent_ifp",
            "sgResponsePredictiveValue_allFederalRespondents",
        ],
        "OT2001-OT2004",
        "extract paid and IFP petition-stage CFR and SG-response buckets from the Thompson-Wachtell petition universe",
        "code paidOrIfp, respondentType, responseFiled, responseSource, responseRequestedByCourt, cfrDate or CFR flag, and disposition",
        "paid and IFP CFR counts reconcile separately; U.S.-respondent SG-response buckets remain separate from all-petition CFR buckets",
    )
    add_row(
        "cert_cvsg_signal",
        "thompson-wachtell-certiorari",
        ["cvsgFrequency", "cvsgGrantRate_recent", "courtFollowsSGRecommendation"],
        "1994-2004; OT2001-OT2004 subperiod",
        "extract CVSG request, SG recommendation, and Court follow-through rows before converting count-per-year context into petition-stage rates",
        "code cvsgRequested, cvsgDate where available, sgRecommendation, certDisposition, granted, and whether the Court followed the SG recommendation",
        "CVSG rows reconcile to the reported subperiod denominator before any rate is attached to the simulator CVSG transition",
    )
    add_row(
        "cert_elite_counsel",
        "feldman-kappner-elite-counsel",
        [
            "specialistCounselGrantRate_JeffreyFisher_filtered",
            "specialistCounselDenyRate_ChristopherLandau_filtered",
        ],
        "2001-2015 filtered attorney subset",
        "extract filtered elite-attorney success rows as a bounded access proxy without treating them as whole-docket counsel prevalence",
        "code counsel identity, specialistCounselFlag, petition side, response side, disposition, and filtered-sample rule",
        "filtered attorney rows keep their denominator flags and are not merged into a whole-cohort specialist-counsel rate",
        "proxy context only until a whole-cohort counsel field is coded",
    )
    add_row(
        "cert_elite_counsel",
        "lazarus-ot2005-cert-stage-amicus",
        [
            "grantRate_noCertStageAmicus_paidNonOSG",
            "grantRate_anyCertStageAmicus_paidNonOSG",
            "grantRate_fourPlusCertStageAmici_paidNonOSG",
        ],
        "OT2005 non-SG paid petitions",
        "extract cert-stage amicus buckets as a salience proxy and keep the single-term non-SG denominator explicit",
        "code paidOrIfp, respondentType, certStageAmicusCount, grant status, and non-SG inclusion rule",
        "zero, one-plus, and four-plus amicus buckets reconcile to the reported OT2005 paid non-SG denominators",
        "proxy context only until multi-term petition rows are coded",
    )
    add_row(
        "cert_split_quality",
        "beim-rader-conflicts",
        [
            "genuineConflictAmongAlleged_rate",
            "genuineConflictGrantRate",
            "conflictUnresolvedShare_sample",
            "conflictResolutionMeanYears_coaSample",
            "conflictResolutionMeanYears_scotusSample",
            "conflictResolvedAtThreeCircuitsOrFewer_share",
        ],
        "1986-1993 petition sample; 2005-2013 conflict lifecycle sample",
        "extract split-quality and conflict-lifecycle rows as proxy checks before locating petition-level alleged/genuine split records",
        "code allegedSplitFlag, genuineSplitFlag, splitDepth, split maturity, disposition, grant status, and conflict resolution timing where available",
        "alleged-versus-genuine split coding stays in the same sample and lifecycle rows remain separate from petition-denominator rows",
        "proxy context only until alleged and genuine split flags are coded on petition rows",
    )
    return output


def write_certiorari_workqueue(rows: list[dict[str, str]]) -> None:
    workqueue_rows = build_certiorari_workqueue_rows(rows)
    with CERTIORARI_WORKQUEUE_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(workqueue_rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(workqueue_rows)

    lines = [
        "# Certiorari Extraction Work Queue v1",
        "",
        "This generated work queue turns the certiorari cohort extraction protocol into concrete source-coding tasks. It is not validation evidence; it identifies the first petition-denominator, response/CFR, CVSG, counsel/amicus, and split-quality source slices that must be row-coded before stronger certiorari benchmark language is justified.",
        "",
        "| Rank | Target | Source | Period/sample | Observed source signal | Unit of work | Completion evidence | Manuscript use |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in workqueue_rows:
        lines.append(
            f"| {row['queueRank']} | {markdown_cell(row['benchmarkTarget'])} | "
            f"{markdown_cell(row['sourceKey'])} | {markdown_cell(row['periodOrSample'])} | "
            f"{markdown_cell(row['observedSourceSignal'])} | {markdown_cell(row['unitOfWork'])} | "
            f"{markdown_cell(row['completionEvidence'])} | {markdown_cell(row['manuscriptUse'])} |"
        )
    CERTIORARI_WORKQUEUE_MD.write_text("\n".join(lines) + "\n")


def shadow_docket_summary_index() -> dict[tuple[str, str], dict[str, str]]:
    output: dict[tuple[str, str], dict[str, str]] = {}
    for row in read_csv(SHADOW_DOCKET_SUMMARY_CSV):
        output[(row["term"], row["metric"])] = row
    return output


def count_extract_rows(rows: list[dict[str, str]], term: str) -> dict[str, int]:
    term_rows = [row for row in rows if row["term"] == term]
    return {
        "applications": len(term_rows),
        "grants": sum(1 for row in term_rows if row["reliefGranted"] == "1"),
        "publicDisagreement": sum(1 for row in term_rows if row["publicDisagreement"] == "1"),
    }


def summary_count(
        summary: dict[tuple[str, str], dict[str, str]],
        term: str,
        metric: str
) -> int:
    row = summary.get((term, metric), {})
    try:
        return int(float(row.get("numerator", "0") or "0"))
    except ValueError:
        return 0


def build_emergency_application_reconciliation_rows() -> list[dict[str, str]]:
    extract_rows = read_csv(EMERGENCY_APPLICATION_ORDER_EXTRACT_CSV)
    summary = shadow_docket_summary_index()
    terms = sorted({row["term"] for row in extract_rows})
    output: list[dict[str, str]] = []
    for term in terms:
        extracted = count_extract_rows(extract_rows, term)
        expected_applications = summary_count(summary, term, "emergencyStayDocketRate")
        expected_grants = summary_count(summary, term, "emergencyOrderRate")
        expected_disagreement = summary_count(summary, term, "shadowDocketAbuse")
        status = (
            "matches_calibration_summary"
            if (
                extracted["applications"] == expected_applications
                and extracted["grants"] == expected_grants
                and extracted["publicDisagreement"] == expected_disagreement
            )
            else "mismatch_review_required"
        )
        output.append({
            "sourceKey": "shadow-docket-v3-0",
            "sourceName": "Supreme Court Shadow Docket Database v3.0",
            "sourceUrl": "https://www.shadowdocketdata.com/data",
            "term": term,
            "sourceFile": extract_rows[0].get("sourceFile", "") if extract_rows else "",
            "sourceFileSha256": extract_rows[0].get("sourceFileSha256", "") if extract_rows else "",
            "extractFilter": "emergency_application=1; full_court=1",
            "extractedApplications": str(extracted["applications"]),
            "summaryApplications": str(expected_applications),
            "applicationsDifference": str(extracted["applications"] - expected_applications),
            "extractedGrantedApplications": str(extracted["grants"]),
            "summaryGrantedApplications": str(expected_grants),
            "grantsDifference": str(extracted["grants"] - expected_grants),
            "extractedPublicDisagreement": str(extracted["publicDisagreement"]),
            "summaryPublicDisagreement": str(expected_disagreement),
            "publicDisagreementDifference": str(extracted["publicDisagreement"] - expected_disagreement),
            "reconciliationStatus": status,
            "manuscriptUse": "application-level denominator guardrail only; no merits-follow-through or downstream-effect validation",
            "remainingGap": "link granted applications to merits follow-through, status-quo effect, and downstream implementation before stronger emergency benchmark claims",
        })
    return output


def party_type(flag: str) -> str:
    if flag == "1":
        return "government"
    if flag == "0":
        return "private_or_individual"
    return "uncoded"


def build_emergency_grant_linkage_rows() -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    fieldnames = schema_field_names(EMERGENCY_LINKAGE_SCHEMA_CSV)
    extract_rows = [
        row
        for row in read_csv(EMERGENCY_APPLICATION_ORDER_EXTRACT_CSV)
        if row.get("reliefGranted") == "1"
    ]
    extract_rows.sort(key=lambda row: (int(row["term"]), row["orderDate"], row["docketNumber"], row["sourceRecordId"]))
    for row in extract_rows:
        payload = {
            "sourceKey": row["sourceKey"],
            "sourceRecordId": row["sourceRecordId"],
            "sourceUrl": row["sourceUrl"],
            "term": f"OT{row['term']}",
            "docketNumber": row["docketNumber"],
            "applicationDate": "",
            "applicationClass": row["actionClass"],
            "applicantType": party_type(row.get("governmentPetitioner", "")),
            "respondentType": party_type(row.get("governmentRespondent", "")),
            "reliefRequested": row["actionClass"],
            "lowerCourt": row["lowerCourt"],
            "responseRequested": "",
            "briefingWindowDays": "",
            "fullCourtReferral": row["fullCourt"],
            "dispositionDate": row["orderDate"],
            "reliefGranted": row["reliefGranted"],
            "dispositionType": row["relief"],
            "reasoningPresent": "",
            "publicDisagreement": row["publicDisagreement"],
            "statusQuoEffect": "uncoded",
            "linkedMeritsDocket": "",
            "linkedMeritsFiledDate": "",
            "linkedMeritsDecisionDate": "",
            "meritsFollowThroughCategory": "uncoded",
            "linkedMeritsOutcome": "",
            "downstreamPolicyStatus": "uncoded",
            "repeatFilingFlag": "",
            "coderNotes": (
                "Prefilled from compact Shadow Docket Database v3.0 extract. "
                "Application filing date, response request, reasoning, status-quo effect, "
                "merits linkage, merits outcome, downstream policy status, and repeat filing "
                "must be coded from docket/order/implementation sources before use as validation evidence. "
                f"Petitioner: {row['petitioner']}; respondent: {row['respondent']}."
            ),
        }
        output.append({field: payload.get(field, "") for field in fieldnames})
    return output


def write_emergency_grant_linkage_workqueue() -> None:
    rows = build_emergency_grant_linkage_rows()
    fieldnames = schema_field_names(EMERGENCY_LINKAGE_SCHEMA_CSV)
    with EMERGENCY_GRANT_LINKAGE_WORKQUEUE_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    term_counts = defaultdict(int)
    term_public_disagreement = defaultdict(int)
    term_government_applicant = defaultdict(int)
    for row in rows:
        term_counts[row["term"]] += 1
        if row["publicDisagreement"] == "1":
            term_public_disagreement[row["term"]] += 1
        if row["applicantType"] == "government":
            term_government_applicant[row["term"]] += 1

    lines = [
        "# Emergency Application Grant Linkage Work Queue v1",
        "",
        "This generated coding sheet preloads all granted full-court emergency-application rows from the compact Shadow Docket Database v3.0 OT2023-OT2024 extract. It is not validation evidence. It is the next row-level coding queue for merits follow-through, status-quo effect, and downstream implementation.",
        "",
        "| Term | Granted rows | Public-disagreement grants | Government-applicant grants |",
        "| --- | ---: | ---: | ---: |",
    ]
    for term in sorted(term_counts):
        lines.append(
            f"| {term} | {term_counts[term]} | {term_public_disagreement[term]} | "
            f"{term_government_applicant[term]} |"
        )
    lines.extend([
        "",
        "Completion rule:",
        "",
        "- Every row must be coded for `statusQuoEffect` and `meritsFollowThroughCategory`; rows with a linked merits proceeding should also code `linkedMeritsDocket`, merits dates/outcome when available, and `downstreamPolicyStatus` before any emergency merits-follow-through or downstream-effect validation claim is upgraded.",
        "",
        "| Term | Docket | Disposition date | Class | Lower court | Public disagreement | Required next coding |",
        "| --- | --- | --- | --- | --- | ---: | --- |",
    ])
    for row in rows:
        lines.append(
            f"| {markdown_cell(row['term'])} | {markdown_cell(row['docketNumber'])} | "
            f"{markdown_cell(row['dispositionDate'])} | {markdown_cell(row['applicationClass'])} | "
            f"{markdown_cell(row['lowerCourt'])} | {markdown_cell(row['publicDisagreement'])} | "
            "status-quo effect; merits linkage; merits follow-through; downstream policy status |"
        )
    EMERGENCY_GRANT_LINKAGE_WORKQUEUE_MD.write_text("\n".join(lines) + "\n")


def build_emergency_denied_linkage_rows() -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    fieldnames = schema_field_names(EMERGENCY_LINKAGE_SCHEMA_CSV)
    extract_rows = [
        row
        for row in read_csv(EMERGENCY_APPLICATION_ORDER_EXTRACT_CSV)
        if row.get("reliefGranted") != "1"
    ]
    extract_rows.sort(key=lambda row: (int(row["term"]), row["orderDate"], row["docketNumber"], row["sourceRecordId"]))
    for row in extract_rows:
        payload = {
            "sourceKey": row["sourceKey"],
            "sourceRecordId": row["sourceRecordId"],
            "sourceUrl": row["sourceUrl"],
            "term": f"OT{row['term']}",
            "docketNumber": row["docketNumber"],
            "applicationDate": "",
            "applicationClass": row["actionClass"],
            "applicantType": party_type(row.get("governmentPetitioner", "")),
            "respondentType": party_type(row.get("governmentRespondent", "")),
            "reliefRequested": row["actionClass"],
            "lowerCourt": row["lowerCourt"],
            "responseRequested": "",
            "briefingWindowDays": "",
            "fullCourtReferral": row["fullCourt"],
            "dispositionDate": row["orderDate"],
            "reliefGranted": row["reliefGranted"],
            "dispositionType": row["relief"],
            "reasoningPresent": "",
            "publicDisagreement": row["publicDisagreement"],
            "statusQuoEffect": "uncoded",
            "linkedMeritsDocket": "",
            "linkedMeritsFiledDate": "",
            "linkedMeritsDecisionDate": "",
            "meritsFollowThroughCategory": "uncoded",
            "linkedMeritsOutcome": "",
            "downstreamPolicyStatus": "uncoded",
            "repeatFilingFlag": "",
            "coderNotes": (
                "Prefilled from compact Shadow Docket Database v3.0 extract. "
                "This denied/non-binary queue is not validation evidence. "
                "Application filing date, response request, reasoning, status-quo effect, "
                "merits follow-through category, downstream policy status, and repeat filing "
                "must be coded or explicitly scoped out before all-application emergency claims. "
                f"Petitioner: {row['petitioner']}; respondent: {row['respondent']}."
            ),
        }
        output.append({field: payload.get(field, "") for field in fieldnames})
    return output


def write_emergency_denied_linkage_workqueue() -> None:
    rows = build_emergency_denied_linkage_rows()
    fieldnames = schema_field_names(EMERGENCY_LINKAGE_SCHEMA_CSV)
    with EMERGENCY_DENIED_LINKAGE_WORKQUEUE_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    term_denied = defaultdict(int)
    term_nonbinary = defaultdict(int)
    term_public_disagreement = defaultdict(int)
    term_government_applicant = defaultdict(int)
    for row in rows:
        if row["reliefGranted"] == "0":
            term_denied[row["term"]] += 1
        else:
            term_nonbinary[row["term"]] += 1
        if row["publicDisagreement"] == "1":
            term_public_disagreement[row["term"]] += 1
        if row["applicantType"] == "government":
            term_government_applicant[row["term"]] += 1

    terms = sorted(set(term_denied) | set(term_nonbinary))
    lines = [
        "# Emergency Application Denied/NA Linkage Work Queue v1",
        "",
        "This generated coding sheet preloads all denied and non-binary full-court emergency-application rows from the compact Shadow Docket Database v3.0 OT2023-OT2024 extract. It is a provenance queue, not validation evidence. Its 210 source rows are now reconciled in the companion official-docket coded benchmark; the queue remains available to make that coding target auditable.",
        "",
        "| Term | Denied rows | Non-binary/NA rows | Public-disagreement rows | Government-applicant rows |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for term in terms:
        lines.append(
            f"| {term} | {term_denied[term]} | {term_nonbinary[term]} | "
            f"{term_public_disagreement[term]} | {term_government_applicant[term]} |"
        )
    lines.extend([
        "",
        "Completion rule:",
        "",
        "- The companion coded benchmark must reconcile to the compact extract's 200 denied rows plus 10 non-binary/NA rows before bounded all-application docket-linkage language is used; that gate is met.",
        "- Every companion row must either be coded for application date, response request, reasoning visibility, status-quo effect, merits follow-through category, downstream docket status, and repeat filing, or marked as not applicable with source-backed coder notes; no external implementation claim follows from this completion.",
        "",
        "| Term | Docket | Disposition date | Class | Disposition | Lower court | Public disagreement | Companion benchmark coding fields |",
        "| --- | --- | --- | --- | --- | --- | ---: | --- |",
    ])
    for row in rows:
        lines.append(
            f"| {markdown_cell(row['term'])} | {markdown_cell(row['docketNumber'])} | "
            f"{markdown_cell(row['dispositionDate'])} | {markdown_cell(row['applicationClass'])} | "
            f"{markdown_cell(row['dispositionType'])} | {markdown_cell(row['lowerCourt'])} | "
            f"{markdown_cell(row['publicDisagreement'])} | "
            "application date; response request; reasoning; status-quo effect; merits follow-through; downstream policy status |"
        )
    EMERGENCY_DENIED_LINKAGE_WORKQUEUE_MD.write_text("\n".join(lines) + "\n")


def certiorari_term_flow_index() -> dict[str, dict[str, str]]:
    rows = read_csv(CERTIORARI_TERM_FLOW_EXTRACT_CSV)
    if not rows:
        raise SystemExit(f"Missing certiorari term-flow extract: {CERTIORARI_TERM_FLOW_EXTRACT_CSV}")
    return {row["statisticKey"]: row for row in rows}


def certiorari_official_count(row: dict[str, str]) -> int:
    return int(row.get("officialCount", "0") or "0")


def certiorari_denominator_count(
        extract_rows: dict[str, dict[str, str]],
        numerator_row: dict[str, str],
        denominator_key: str
) -> int:
    if numerator_row.get("denominatorKey") == denominator_key and numerator_row.get("denominatorCount"):
        return int(numerator_row["denominatorCount"])
    if denominator_key == "paid_plus_ifp_cases_docketed_during_term":
        return (
            certiorari_official_count(extract_rows["cases_docketed_paid"])
            + certiorari_official_count(extract_rows["cases_docketed_ifp"])
        )
    if denominator_key == "total_cases_docketed_during_term":
        return certiorari_official_count(extract_rows["cases_docketed_total"])
    if denominator_key in extract_rows:
        return certiorari_official_count(extract_rows[denominator_key])
    raise SystemExit(f"Unknown certiorari denominator key: {denominator_key}")


def write_emergency_application_reconciliation() -> None:
    rows = build_emergency_application_reconciliation_rows()
    with EMERGENCY_APPLICATION_RECONCILIATION_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Emergency Application Order Reconciliation v1",
        "",
        "This report checks the compact Shadow Docket Database v3.0 full-court emergency-application extract against the normalized term-summary counts already used for calibration guardrails. It is application-level denominator evidence for the selected terms, not merits-follow-through or downstream-effect validation.",
        "",
        "| Term | Applications | Summary applications | Grants | Summary grants | Public disagreement | Summary disagreement | Status | Manuscript use |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| OT{row['term']} | {row['extractedApplications']} | {row['summaryApplications']} | "
            f"{row['extractedGrantedApplications']} | {row['summaryGrantedApplications']} | "
            f"{row['extractedPublicDisagreement']} | {row['summaryPublicDisagreement']} | "
            f"{markdown_cell(row['reconciliationStatus'])} | {markdown_cell(row['manuscriptUse'])} |"
        )
    lines.extend([
        "",
        "Boundary note:",
        "",
        "- The extract uses `emergency_application=1` and `full_court=1`, matching the normalized shadow-docket summary denominator. The row dates are order dates, not filing dates. The extract does not code merits follow-through, status-quo effect, or downstream policy implementation.",
    ])
    EMERGENCY_APPLICATION_RECONCILIATION_MD.write_text("\n".join(lines) + "\n")


EMERGENCY_EXTRACT_FIELD_MAP = {
    "sourceKey": "sourceKey",
    "sourceRecordId": "sourceRecordId",
    "sourceUrl": "sourceUrl",
    "term": "term",
    "docketNumber": "docketNumber",
    "applicationClass": "actionClass",
    "applicantType": "governmentPetitioner",
    "respondentType": "governmentRespondent",
    "reliefRequested": "actionClass",
    "lowerCourt": "lowerCourt",
    "fullCourtReferral": "fullCourt",
    "dispositionDate": "orderDate",
    "reliefGranted": "reliefGranted",
    "dispositionType": "relief",
    "publicDisagreement": "publicDisagreement",
    "coderNotes": "coderNotes",
}

GRANT_LINKAGE_ONLY_FIELDS = {
    "applicationDate",
    "responseRequested",
    "briefingWindowDays",
    "reasoningPresent",
    "statusQuoEffect",
    "linkedMeritsDocket",
    "linkedMeritsFiledDate",
    "linkedMeritsDecisionDate",
    "meritsFollowThroughCategory",
    "linkedMeritsOutcome",
    "downstreamPolicyStatus",
    "repeatFilingFlag",
}

FULL_GRANT_LINKAGE_FIELDS = {
    "applicationDate",
    "responseRequested",
    "reasoningPresent",
    "statusQuoEffect",
    "meritsFollowThroughCategory",
    "downstreamPolicyStatus",
    "repeatFilingFlag",
}

CONDITIONAL_LINKED_MERITS_FIELDS = {
    "linkedMeritsDocket",
    "linkedMeritsFiledDate",
    "linkedMeritsDecisionDate",
    "linkedMeritsOutcome",
}

EXPLICIT_NO_LINK_CATEGORIES = {
    "cert_or_merits_petition_denied_no_scotus_merits_followthrough",
    "no_scotus_merits_link_on_application_docket",
    "official_docket_no_application_merits_link_visible",
}


def emergency_merits_field_resolved(field_name: str, row: dict[str, str]) -> bool:
    if row.get(field_name, "").strip():
        return True
    category = row.get("meritsFollowThroughCategory", "").strip()
    if category in EXPLICIT_NO_LINK_CATEGORIES:
        return True
    if category == "cert_extension_granted_petition_deadline_pending":
        return True
    if field_name == "linkedMeritsDecisionDate" and category.endswith("_pending"):
        return True
    return False


def emergency_extract_count(field_name: str, extract_rows: list[dict[str, str]]) -> int:
    extract_field = EMERGENCY_EXTRACT_FIELD_MAP.get(field_name)
    if extract_field is None:
        return 0
    return sum(1 for row in extract_rows if row.get(extract_field, "").strip())


def emergency_grant_coded_count(field_name: str, coded_rows: list[dict[str, str]]) -> int:
    return sum(1 for row in coded_rows if row.get(field_name, "").strip())


def emergency_denied_coded_count(field_name: str, coded_rows: list[dict[str, str]]) -> int:
    return sum(1 for row in coded_rows if row.get(field_name, "").strip())


def emergency_field_status(
        field_name: str,
        extract_total: int,
        extract_count: int,
        grant_count: int,
        grant_total: int,
        denied_count: int,
        denied_total: int,
        grant_resolved_count: int,
        denied_resolved_count: int,
) -> str:
    combined_count = grant_count + denied_count
    combined_total = grant_total + denied_total
    combined_resolved_count = grant_resolved_count + denied_resolved_count
    if extract_total and extract_count == extract_total:
        return "all_application_extract"
    if (
            field_name in FULL_GRANT_LINKAGE_FIELDS
            and combined_total
            and grant_total
            and denied_total
            and combined_count == combined_total
    ):
        return "all_application_docket_linkage_coded"
    if (
            field_name in CONDITIONAL_LINKED_MERITS_FIELDS
            and combined_total
            and grant_total
            and denied_total
            and combined_resolved_count == combined_total
    ):
        return "all_application_docket_linkage_conditionally_complete"
    if field_name in GRANT_LINKAGE_ONLY_FIELDS and denied_total and combined_count > grant_count:
        return "all_application_docket_linkage_partial"
    if field_name in FULL_GRANT_LINKAGE_FIELDS and grant_total and grant_count == grant_total:
        return "grant_linkage_coded"
    if field_name in GRANT_LINKAGE_ONLY_FIELDS and grant_count > 0:
        return "grant_linkage_partial"
    return "not_row_coded"


def emergency_current_evidence(
        field_name: str,
        status: str,
        extract_total: int,
        extract_count: int,
        grant_total: int,
        grant_count: int,
        denied_total: int,
        denied_count: int,
        grant_resolved_count: int,
        denied_resolved_count: int,
        unresolved_count: int
) -> str:
    if status == "all_application_extract":
        if field_name == "reliefGranted":
            return (
                f"Compact Shadow Docket v3.0 extract populates `{field_name}` for "
                f"{extract_count}/{extract_total} full-court emergency-application rows; "
                "values include granted, denied, and non-binary/NA dispositions"
            )
        return (
            f"Compact Shadow Docket v3.0 extract populates `{field_name}` for "
            f"{extract_count}/{extract_total} full-court emergency-application rows; "
            "this supports denominator and disposition guardrails, not merits-follow-through validation"
        )
    if status == "grant_linkage_coded":
        return (
            f"Official-docket coded grant benchmark populates `{field_name}` for "
            f"{grant_count}/{grant_total} granted source-record rows; {unresolved_count} denied or non-binary "
            "application rows remain uncoded for this field"
        )
    if status == "all_application_docket_linkage_coded":
        return (
            f"Official-docket linkage benchmarks populate `{field_name}` for "
            f"{grant_count}/{grant_total} granted rows and {denied_count}/{denied_total} denied or non-binary "
            "rows; this closes the docket-visible all-application coding gap for this field"
        )
    if status == "all_application_docket_linkage_partial":
        return (
            f"Official-docket linkage benchmarks populate `{field_name}` where docket-visible for "
            f"{grant_count}/{grant_total} granted rows and {denied_count}/{denied_total} denied or non-binary rows; "
            "blanks may represent no linked merits proceeding or no briefing window"
        )
    if status == "all_application_docket_linkage_conditionally_complete":
        return (
            f"Official-docket linkage benchmarks populate `{field_name}` where applicable for "
            f"{grant_count}/{grant_total} granted rows and {denied_count}/{denied_total} denied or non-binary rows; "
            f"all {grant_resolved_count + denied_resolved_count}/{grant_total + denied_total} rows are resolved "
            "by a linked value or an explicit no-link or pending category"
        )
    if status == "grant_linkage_partial":
        return (
            f"Official-docket coded grant benchmark populates `{field_name}` where applicable for "
            f"{grant_count}/{grant_total} granted source-record rows; {unresolved_count} denied or non-binary "
            "application rows remain uncoded and blanks may represent no linked merits proceeding or no briefing window"
        )
    return (
        f"No row-level emergency benchmark currently populates `{field_name}` beyond schema scaffolding; "
        f"{extract_total} application rows require source coding before use"
    )


def emergency_next_action(field_name: str, status: str) -> str:
    if status == "all_application_extract":
        return (
            f"preserve the extract-populated `{field_name}` value while adding official-docket coding "
            "only if all-application or denied-application claims are made"
        )
    if status == "all_application_docket_linkage_coded":
        return (
            f"preserve all-application official-docket `{field_name}` coding and avoid upgrading beyond "
            "docket-visible linkage without external implementation observations"
        )
    if status == "all_application_docket_linkage_partial":
        return (
            f"treat `{field_name}` as docket-visible where present; use manual order/merits review before "
            "claiming a complete all-application merits or briefing denominator"
        )
    if status == "all_application_docket_linkage_conditionally_complete":
        return (
            f"preserve `{field_name}` where applicable, retain explicit no-link and pending categories, "
            "and refresh pending linked merits dockets before publication or deposit"
        )
    if status in {"grant_linkage_coded", "grant_linkage_partial"}:
        return (
            f"extend `{field_name}` coding from granted rows to denied and non-binary application rows "
            "using `data/benchmarks/emergency-application-denied-linkage-workqueue-v1.csv` before claiming "
            "all-application emergency benchmarks"
        )
    return f"code `{field_name}` from official application dockets, order text, merits dockets, or implementation sources"


def emergency_manuscript_use(status: str) -> str:
    if status == "all_application_extract":
        return "application-level denominator or disposition guardrail only"
    if status == "all_application_docket_linkage_coded":
        return "bounded all-application emergency docket-linkage evidence only; not external implementation validation"
    if status == "all_application_docket_linkage_partial":
        return "bounded docket-visible emergency linkage where present; not complete merits or external implementation validation"
    if status == "all_application_docket_linkage_conditionally_complete":
        return "bounded all-application docket-visible merits-linkage evidence; not external implementation validation"
    if status in {"grant_linkage_coded", "grant_linkage_partial"}:
        return "bounded granted-emergency linkage evidence only; not all-application validation"
    return "no validation upgrade until row-level coding reconciles to the application denominator"


def build_emergency_field_readiness_rows() -> list[dict[str, str]]:
    extract_rows = read_csv(EMERGENCY_APPLICATION_ORDER_EXTRACT_CSV)
    coded_rows = read_csv(EMERGENCY_LINKAGE_CODED_CSV)
    denied_coded_rows = read_csv(EMERGENCY_DENIED_LINKAGE_CODED_CSV)
    extract_total = len(extract_rows)
    grant_total = len(coded_rows)
    denied_total = len(denied_coded_rows)
    unresolved_count = sum(1 for row in extract_rows if row.get("reliefGranted") != "1")
    output: list[dict[str, str]] = []
    for field in read_csv(EMERGENCY_LINKAGE_SCHEMA_CSV):
        field_name = field["fieldName"]
        extract_count = emergency_extract_count(field_name, extract_rows)
        grant_count = emergency_grant_coded_count(field_name, coded_rows)
        denied_count = emergency_denied_coded_count(field_name, denied_coded_rows)
        grant_resolved_count = (
            sum(1 for row in coded_rows if emergency_merits_field_resolved(field_name, row))
            if field_name in CONDITIONAL_LINKED_MERITS_FIELDS
            else grant_count
        )
        denied_resolved_count = (
            sum(1 for row in denied_coded_rows if emergency_merits_field_resolved(field_name, row))
            if field_name in CONDITIONAL_LINKED_MERITS_FIELDS
            else denied_count
        )
        status = emergency_field_status(
            field_name,
            extract_total,
            extract_count,
            grant_count,
            grant_total,
            denied_count,
            denied_total,
            grant_resolved_count,
            denied_resolved_count,
        )
        all_application_count = extract_count
        if status in {
            "all_application_docket_linkage_coded",
            "all_application_docket_linkage_partial",
            "all_application_docket_linkage_conditionally_complete",
        }:
            all_application_count = grant_count + denied_count
        output.append({
            "fieldName": field_name,
            "fieldGroup": field["fieldGroup"],
            "type": field["type"],
            "requiredFor": field["requiredFor"],
            "validationUse": field["validationUse"],
            "simulatorMetric": field["simulatorMetric"],
            "currentStatus": status,
            "allApplicationRowsPopulated": str(all_application_count),
            "grantCodedRowsPopulated": str(grant_count),
            "deniedOrNaRowsRequiringCoding": (
                "0"
                if status in {
                    "all_application_extract",
                    "all_application_docket_linkage_coded",
                    "all_application_docket_linkage_partial",
                    "all_application_docket_linkage_conditionally_complete",
                }
                else str(unresolved_count)
            ),
            "currentEvidence": emergency_current_evidence(
                field_name,
                status,
                extract_total,
                extract_count,
                grant_total,
                grant_count,
                denied_total,
                denied_count,
                grant_resolved_count,
                denied_resolved_count,
                unresolved_count,
            ),
            "nextCodingAction": emergency_next_action(field_name, status),
            "manuscriptUse": emergency_manuscript_use(status),
        })
    return output


def write_emergency_field_readiness() -> None:
    readiness_rows = build_emergency_field_readiness_rows()
    with EMERGENCY_FIELD_READINESS_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(readiness_rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(readiness_rows)

    by_status: dict[str, int] = defaultdict(int)
    for row in readiness_rows:
        by_status[row["currentStatus"]] += 1

    extract_rows = read_csv(EMERGENCY_APPLICATION_ORDER_EXTRACT_CSV)
    denied_coded_rows = read_csv(EMERGENCY_DENIED_LINKAGE_CODED_CSV)
    grant_rows = [row for row in extract_rows if row.get("reliefGranted") == "1"]
    denied_rows = [row for row in extract_rows if row.get("reliefGranted") == "0"]
    nonbinary_rows = [row for row in extract_rows if row.get("reliefGranted") not in {"0", "1"}]

    lines = [
        "# Emergency Application Field Readiness v1",
        "",
        "This report audits the emergency-application linkage schema field by field. It is a coding-readiness matrix, not validation evidence. It separates fields populated by the compact all-application Shadow Docket extract, fields coded through official Supreme Court docket linkage, and fields still limited to docket-visible or external-implementation evidence.",
        "",
        "Application denominator:",
        "",
        f"- Extracted full-court emergency-application rows: {len(extract_rows)}",
        f"- Granted source-record rows with official-docket linkage coding: {len(grant_rows)}",
        f"- Denied source-record rows with official-docket linkage coding: {sum(1 for row in denied_coded_rows if row.get('reliefGranted') == '0')}",
        f"- Non-binary or NA disposition rows with official-docket linkage coding: {sum(1 for row in denied_coded_rows if row.get('reliefGranted') not in {'0', '1'})}",
        f"- Denied/NA source-record rows in generated linkage queue: {len(denied_rows) + len(nonbinary_rows)}",
        "",
        "Status counts:",
        "",
    ]
    for status, count in sorted(by_status.items()):
        lines.append(f"- `{status}`: {count}")
    lines.extend([
        "",
        "| Field | Group | Use | Status | All-app rows | Grant-coded rows | Denied/NA gap | Current evidence | Manuscript use |",
        "| --- | --- | --- | --- | ---: | ---: | ---: | --- | --- |",
    ])
    for row in readiness_rows:
        lines.append(
            f"| `{markdown_cell(row['fieldName'])}` | {markdown_cell(row['fieldGroup'])} | "
            f"{markdown_cell(row['validationUse'])} | {markdown_cell(row['currentStatus'])} | "
            f"{row['allApplicationRowsPopulated']} | {row['grantCodedRowsPopulated']} | "
            f"{row['deniedOrNaRowsRequiringCoding']} | {markdown_cell(row['currentEvidence'])} | "
            f"{markdown_cell(row['manuscriptUse'])} |"
        )
    EMERGENCY_FIELD_READINESS_MD.write_text("\n".join(lines) + "\n")


def build_certiorari_term_flow_reconciliation_rows() -> list[dict[str, str]]:
    metric_rows = calibration_metric_index()
    ot2023_calibration = (
        CALIBRATION_DIR / "scotus-certiorari-docketed-cohort-ot2023.csv"
    )
    for row in read_csv(ot2023_calibration):
        metric = row.get("metric", "")
        if metric:
            metric_rows[metric] = row
    extract_rows = certiorari_term_flow_index()
    total_docketed = certiorari_official_count(extract_rows["cases_docketed_total"])
    output: list[dict[str, str]] = []
    for metric in CERTIORARI_TERM_FLOW_METRICS:
        numerator_row = extract_rows[metric["numeratorKey"]]
        official_numerator = certiorari_official_count(numerator_row)
        official_denominator = certiorari_denominator_count(
            extract_rows,
            numerator_row,
            metric["denominatorKey"],
        )
        official_value = official_numerator / official_denominator
        metric_row = metric_rows.get(metric["metricKey"], {})
        normalized_observed = (
            metric_row.get("observedValue")
            or metric_row.get("value")
            or ""
        )
        try:
            normalized_value = float(normalized_observed)
            absolute_difference = abs(normalized_value - official_value)
        except ValueError:
            normalized_value = None
            absolute_difference = None
        status = (
            "matches_official_source"
            if absolute_difference is not None and absolute_difference <= 0.0005
            else "mismatch_review_required"
        )
        output.append({
            "metricKey": metric["metricKey"],
            "sourceKey": numerator_row["sourceKey"],
            "sourceName": numerator_row["sourceName"],
            "sourceUrl": numerator_row["sourceUrl"],
            "term": numerator_row["term"],
            "sourceRecordId": numerator_row["sourceRecordId"],
            "officialNumerator": str(official_numerator),
            "officialDenominator": str(official_denominator),
            "officialTotalDocketed": str(total_docketed),
            "officialValue": f"{official_value:.4f}",
            "normalizedObservedValue": "" if normalized_value is None else f"{normalized_value:.4f}",
            "normalizedRawObservedValue": (
                metric_row.get("rawObservedValue")
                or metric_row_text(metric_rows, metric["metricKey"])
            ),
            "absoluteDifference": "" if absolute_difference is None else f"{absolute_difference:.6f}",
            "reconciliationStatus": status,
            "denominatorNote": metric["denominatorNote"],
            "manuscriptUse": metric["manuscriptUse"],
        })
    return output


def write_certiorari_term_flow_reconciliation() -> None:
    rows = build_certiorari_term_flow_reconciliation_rows()
    with CERTIORARI_TERM_FLOW_RECONCILIATION_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Certiorari Term-Flow Reconciliation v1",
        "",
        "This report checks the first certiorari petition-denominator source slice against the official OT2023 Journal statistics table. It is a source-quality reconciliation, not a closed petition-cohort validation result.",
        "",
        "| Metric | Official count | Official denominator | Official value | Normalized value | Status | Manuscript use |",
        "| --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| `{markdown_cell(row['metricKey'])}` | {row['officialNumerator']} | "
            f"{row['officialDenominator']} | {row['officialValue']} | "
            f"{row['normalizedObservedValue']} | {markdown_cell(row['reconciliationStatus'])} | "
            f"{markdown_cell(row['manuscriptUse'])} |"
        )
    lines.extend([
        "",
        "Denominator notes:",
        "",
    ])
    for row in rows:
        lines.append(f"- `{row['metricKey']}`: {row['denominatorNote']}")
    CERTIORARI_TERM_FLOW_RECONCILIATION_MD.write_text("\n".join(lines) + "\n")


PETITION_DENOMINATOR_AGGREGATE_FIELDS = {
    "sourceKey",
    "sourceRecordId",
    "sourceUrl",
    "term",
    "petitionType",
    "paidOrIfp",
    "certDisposition",
    "granted",
    "grantSetForArgument",
    "dispositionDate",
}

JOURNAL_DISPOSITION_SEED_FIELDS = {
    "docketNumber",
    "petitionType",
    "paidOrIfp",
    "lowerCourt",
    "dispositionDate",
    "certDisposition",
    "granted",
    "gvrOrSummaryDisposition",
}

GRANTED_DOCKET_DETAIL_FIELDS = {
    "petitionFiledDate",
    "responseFiled",
    "responseSource",
    "responseRequestedByCourt",
    "cfrDate",
    "cvsgRequested",
    "cvsgDate",
    "sgRecommendation",
    "certStageAmicusCount",
    "relistCount",
    "grantSetForArgument",
    "meritsDocket",
    "meritsDecisionDate",
    "meritsOutcome",
    "reversalOrVacatur",
}

JOURNAL_DOCKET_DETAIL_FIELDS = {
    "petitionFiledDate",
    "responseFiled",
    "responseSource",
    "responseRequestedByCourt",
    "cfrDate",
    "cvsgRequested",
    "cvsgDate",
    "sgRecommendation",
    "certStageAmicusCount",
    "relistCount",
}

DOCKETED_COHORT_COMPLETE_FIELDS = {
    "sourceKey",
    "sourceRecordId",
    "sourceUrl",
    "term",
    "docketNumber",
    "petitionFiledDate",
    "petitionType",
    "paidOrIfp",
    "lowerCourt",
    "lowerCourtOrigin",
    "responseFiled",
    "responseSource",
    "responseRequestedByCourt",
    "cfrDate",
    "cvsgRequested",
    "cvsgDate",
    "sgRecommendation",
    "certStageAmicusCount",
    "relistCount",
    "dispositionDate",
    "certDisposition",
    "granted",
    "grantSetForArgument",
    "gvrOrSummaryDisposition",
    "meritsDocket",
    "coderNotes",
}

DOCKETED_COHORT_PARTIAL_FIELDS = {
    "petitionerType",
    "respondentType",
    "meritsDecisionDate",
    "meritsOutcome",
    "reversalOrVacatur",
}


def certiorari_source_slice(target_keys: list[str], protocols: dict[str, dict[str, str]]) -> str:
    slices = [
        protocols[target_key]["firstExtractionSlice"]
        for target_key in target_keys
        if target_key in protocols
    ]
    return "; ".join(dict.fromkeys(slices))


def certiorari_completion_gate(
        field: dict[str, str],
        target_keys: list[str],
        protocols: dict[str, dict[str, str]]
) -> str:
    if field["fieldName"] in {"sourceKey", "sourceRecordId", "sourceUrl", "term"}:
        return "preserve source provenance on every row before any cohort claim is made"
    gates = [
        protocols[target_key]["completionRule"]
        for target_key in target_keys
        if target_key in protocols
    ]
    if gates:
        return "; ".join(dict.fromkeys(gates))
    return "populate field on the same row-level petition unit as the target metric before using it as benchmark evidence"


def certiorari_journal_disposition_counts() -> tuple[int, dict[str, int]]:
    if not CERTIORARI_JOURNAL_DISPOSITION_EXTRACT_CSV.exists():
        return 0, {}
    rows = read_csv(CERTIORARI_JOURNAL_DISPOSITION_EXTRACT_CSV)
    counts: dict[str, int] = {}
    for field_name in JOURNAL_DISPOSITION_SEED_FIELDS:
        counts[field_name] = sum(1 for row in rows if row.get(field_name, "").strip())
    return len(rows), counts


def certiorari_granted_docket_detail_counts() -> tuple[int, dict[str, int]]:
    if not CERTIORARI_GRANTED_DOCKET_DETAIL_CSV.exists():
        return 0, {}
    rows = read_csv(CERTIORARI_GRANTED_DOCKET_DETAIL_CSV)
    counts: dict[str, int] = {}
    for field_name in GRANTED_DOCKET_DETAIL_FIELDS:
        counts[field_name] = sum(1 for row in rows if row.get(field_name, "").strip())
    return len(rows), counts


def certiorari_journal_docket_detail_counts() -> tuple[int, dict[str, int]]:
    if not CERTIORARI_JOURNAL_DOCKET_DETAIL_CSV.exists():
        return 0, {}
    rows = read_csv(CERTIORARI_JOURNAL_DOCKET_DETAIL_CSV)
    counts: dict[str, int] = {}
    for field_name in JOURNAL_DOCKET_DETAIL_FIELDS:
        counts[field_name] = sum(1 for row in rows if row.get(field_name, "").strip())
    return len(rows), counts


def certiorari_docketed_cohort_counts() -> tuple[int, dict[str, int], int, dict[str, int]]:
    if not CERTIORARI_DOCKETED_COHORT_CSV.exists():
        return 0, {}, 0, {}
    rows = read_csv(CERTIORARI_DOCKETED_COHORT_CSV)
    cert_rows = [row for row in rows if row.get("petitionType") == "certiorari"]
    fields = [row["fieldName"] for row in read_csv(CERTIORARI_COHORT_SCHEMA_CSV)]
    counts = {
        field_name: sum(1 for row in rows if row.get(field_name, "").strip())
        for field_name in fields
    }
    cert_counts = {
        field_name: sum(1 for row in cert_rows if row.get(field_name, "").strip())
        for field_name in fields
    }
    return len(rows), counts, len(cert_rows), cert_counts


def certiorari_field_status(
        field: dict[str, str],
        target_keys: list[str],
        cohort_counts: dict[str, int],
        journal_counts: dict[str, int],
        journal_docket_counts: dict[str, int],
        granted_docket_counts: dict[str, int],
) -> str:
    field_name = field["fieldName"]
    if field_name in DOCKETED_COHORT_COMPLETE_FIELDS and cohort_counts.get(field_name, 0) > 0:
        return "closed_docketed_cohort_complete"
    if field_name in DOCKETED_COHORT_PARTIAL_FIELDS and cohort_counts.get(field_name, 0) > 0:
        return "closed_docketed_cohort_partial"
    if field_name in {"sourceKey", "sourceRecordId", "sourceUrl", "term"}:
        return "scaffold_available"
    if field_name in JOURNAL_DISPOSITION_SEED_FIELDS and journal_counts.get(field_name, 0) > 0:
        return "journal_disposition_seed"
    if field_name in JOURNAL_DOCKET_DETAIL_FIELDS and journal_docket_counts.get(field_name, 0) > 0:
        return "journal_public_docket_detail_partial"
    if field_name in GRANTED_DOCKET_DETAIL_FIELDS and granted_docket_counts.get(field_name, 0) > 0:
        return "granted_gvr_docket_detail"
    if "cert_petition_denominator" in target_keys and field_name in PETITION_DENOMINATOR_AGGREGATE_FIELDS:
        return "aggregate_guardrail_only"
    if field["validationUse"] == "required":
        return "required_not_row_coded"
    return "recommended_not_row_coded"


def certiorari_current_evidence(
        status: str,
        field: dict[str, str],
        cohort_total: int,
        cohort_counts: dict[str, int],
        cert_total: int,
        cert_counts: dict[str, int],
        journal_total: int,
        journal_counts: dict[str, int],
        journal_docket_total: int,
        journal_docket_counts: dict[str, int],
        granted_docket_total: int,
        granted_docket_counts: dict[str, int],
) -> str:
    if status == "closed_docketed_cohort_complete":
        field_name = field["fieldName"]
        return (
            f"The independently enumerated OT2023 cohort contains {cohort_total} paid/IFP dockets "
            f"and {cert_total} certiorari petitions; `{field_name}` is populated for "
            f"{cohort_counts.get(field_name, 0)}/{cohort_total} all-docket rows and "
            f"{cert_counts.get(field_name, 0)}/{cert_total} certiorari rows, with blanks retained "
            "only where the field is structurally conditional or not applicable"
        )
    if status == "closed_docketed_cohort_partial":
        field_name = field["fieldName"]
        return (
            f"The closed OT2023 docketed cohort populates `{field_name}` for "
            f"{cohort_counts.get(field_name, 0)}/{cohort_total} all-docket rows and "
            f"{cert_counts.get(field_name, 0)}/{cert_total} certiorari rows; this field remains "
            "partial even though the paid/IFP and certiorari denominators are closed"
        )
    if status == "scaffold_available":
        return "schema and source registry already require stable provenance fields"
    if status == "journal_disposition_seed":
        field_name = field["fieldName"]
        count = journal_counts.get(field_name, 0)
        if field_name == "lowerCourt":
            return (
                f"OT2023 official Journal disposition seed parses lower-court text where visible "
                f"for {count}/{journal_total} source-addressed disposition rows; closed filed-petition, "
                "whole-docket CFR/CVSG, counsel, split-quality, and merits follow-through fields remain incomplete"
            )
        return (
            f"OT2023 official Journal disposition seed populates `{field_name}` for "
            f"{count}/{journal_total} source-addressed disposition rows; closed filed-petition, whole-docket "
            "CFR/CVSG, counsel, split-quality, and merits follow-through fields remain incomplete"
        )
    if status == "journal_public_docket_detail_partial":
        field_name = field["fieldName"]
        count = journal_docket_counts.get(field_name, 0)
        missing = max(0, journal_total - journal_docket_total)
        return (
            f"Official Supreme Court static docket pages are reachable for {journal_docket_total}/{journal_total} "
            f"OT2023 Journal disposition rows and populate `{field_name}` for {count} reachable rows; "
            f"{missing} Journal rows still lack static-page docket detail in this extract, so this remains "
            "bounded reachable-public-docket evidence rather than closed filed-petition validation"
        )
    if status == "granted_gvr_docket_detail":
        field_name = field["fieldName"]
        count = granted_docket_counts.get(field_name, 0)
        return (
            f"Official Supreme Court docket pages populate `{field_name}` for "
            f"{count}/{granted_docket_total} OT2023 Journal granted/GVR rows; this is bounded "
            "granted/GVR detail, not a closed filed-petition cohort"
        )
    if status == "aggregate_guardrail_only":
        return "OT2023 Journal term-flow extract reconciles aggregate paid/IFP and plenary-review counts but does not supply petition rows"
    if field["validationUse"] == "required":
        return "candidate source family is identified, but no row-level petition cohort currently populates this field"
    return "recommended field for later row-level coding; absent from the current benchmark evidence boundary"


def certiorari_next_action(status: str, field: dict[str, str], source_slice: str) -> str:
    field_name = field["fieldName"]
    if status == "closed_docketed_cohort_complete":
        return (
            f"retain `{field_name}` in the closed cohort and re-run the official-docket "
            "extractor when refreshing the publication snapshot"
        )
    if status == "closed_docketed_cohort_partial":
        return (
            f"complete or validate the remaining `{field_name}` rows without changing the "
            "closed 4,222-docket denominator"
        )
    if status == "scaffold_available":
        return "carry this provenance field into every extracted certiorari row"
    if status == "journal_disposition_seed":
        return (
            f"preserve the Journal-populated `{field_name}` value while joining docket or petition "
            "sources needed to close the filed-petition cohort"
        )
    if status == "journal_public_docket_detail_partial":
        return (
            f"preserve reachable official-docket `{field_name}` values and add an alternate official "
            "docket-search/manual retrieval source for failed static pages before any closed-cohort upgrade"
        )
    if status == "granted_gvr_docket_detail":
        return (
            f"preserve the official-docket `{field_name}` value for granted/GVR rows while coding "
            "denied, dismissed, pending, and response-stage petition rows before any closed-cohort upgrade"
        )
    if status == "aggregate_guardrail_only":
        return (
            "replace aggregate Journal counts with closed petition rows before upgrading "
            f"`{field_name}` from guardrail context"
        )
    if source_slice:
        return f"code `{field_name}` from {source_slice}"
    return f"code `{field_name}` when a compatible petition-level source is selected"


def certiorari_manuscript_use(status: str) -> str:
    if status == "closed_docketed_cohort_complete":
        return (
            "direct closed docketed-intake evidence for this docket-visible field; "
            "not a census of undocketed submissions or specialist-counsel/split-quality validation"
        )
    if status == "closed_docketed_cohort_partial":
        return (
            "bounded field coverage inside a closed docketed-intake cohort; "
            "not complete field-level validation"
        )
    if status == "scaffold_available":
        return "source provenance requirement only"
    if status == "journal_disposition_seed":
        return "source-addressed disposition evidence only; not closed petition-cohort validation"
    if status == "journal_public_docket_detail_partial":
        return "bounded reachable-public-docket detail evidence only; not closed petition-cohort validation"
    if status == "granted_gvr_docket_detail":
        return "bounded granted/GVR docket-detail evidence only; not closed petition-cohort validation"
    if status == "aggregate_guardrail_only":
        return "term-flow intake guardrail only; not closed petition-cohort validation"
    return "no validation upgrade until populated on row-level petition or source-sample rows that reconcile to their denominator"


def build_certiorari_field_readiness_rows(dashboard_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    protocols = protocol_lookup(dashboard_rows)
    cohort_total, cohort_counts, cert_total, cert_counts = certiorari_docketed_cohort_counts()
    journal_total, journal_counts = certiorari_journal_disposition_counts()
    journal_docket_total, journal_docket_counts = certiorari_journal_docket_detail_counts()
    granted_docket_total, granted_docket_counts = certiorari_granted_docket_detail_counts()
    output = []
    for field in read_csv(CERTIORARI_COHORT_SCHEMA_CSV):
        target_keys = [
            target_key
            for target_key in field["requiredFor"].split(";")
            if target_key and target_key != "all"
        ]
        status = certiorari_field_status(
            field,
            target_keys,
            cohort_counts,
            journal_counts,
            journal_docket_counts,
            granted_docket_counts,
        )
        source_slice = certiorari_source_slice(target_keys, protocols)
        output.append({
            "fieldName": field["fieldName"],
            "fieldGroup": field["fieldGroup"],
            "type": field["type"],
            "requiredFor": field["requiredFor"],
            "validationUse": field["validationUse"],
            "simulatorMetric": field["simulatorMetric"],
            "currentStatus": status,
            "currentEvidence": certiorari_current_evidence(
                status,
                field,
                cohort_total,
                cohort_counts,
                cert_total,
                cert_counts,
                journal_total,
                journal_counts,
                journal_docket_total,
                journal_docket_counts,
                granted_docket_total,
                granted_docket_counts,
            ),
            "sourceSlice": source_slice,
            "nextCodingAction": certiorari_next_action(status, field, source_slice),
            "completionGate": (
                "met for the closed OT2023 docketed-intake cohort; preserve source and denominator provenance"
                if status == "closed_docketed_cohort_complete"
                else certiorari_completion_gate(field, target_keys, protocols)
            ),
            "manuscriptUse": certiorari_manuscript_use(status),
        })
    return output


def write_certiorari_field_readiness(rows: list[dict[str, str]]) -> None:
    readiness_rows = build_certiorari_field_readiness_rows(rows)
    with CERTIORARI_FIELD_READINESS_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(readiness_rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(readiness_rows)

    by_status: dict[str, int] = defaultdict(int)
    for row in readiness_rows:
        by_status[row["currentStatus"]] += 1

    lines = [
        "# Certiorari Cohort Field Readiness v1",
        "",
        "This report audits the certiorari cohort schema field by field. The 4,222-row OT2023 paid/IFP docketed-intake denominator is now closed and contains 4,033 certiorari petitions with mature docket outcomes. The matrix separates complete docket-visible cohort fields, partial metadata or merits fields, older Journal slices, and counsel/split/issue fields that still require external or manual coding.",
        "",
        "Status counts:",
        "",
    ]
    for status, count in sorted(by_status.items()):
        lines.append(f"- `{status}`: {count}")
    lines.extend([
        "",
        "| Field | Group | Use | Status | Current evidence | Next coding action | Manuscript use |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ])
    for row in readiness_rows:
        lines.append(
            f"| `{markdown_cell(row['fieldName'])}` | {markdown_cell(row['fieldGroup'])} | "
            f"{markdown_cell(row['validationUse'])} | {markdown_cell(row['currentStatus'])} | "
            f"{markdown_cell(row['currentEvidence'])} | {markdown_cell(row['nextCodingAction'])} | "
            f"{markdown_cell(row['manuscriptUse'])} |"
        )
    CERTIORARI_FIELD_READINESS_MD.write_text("\n".join(lines) + "\n")


def unique_join(values: list[str]) -> str:
    return "; ".join(dict.fromkeys(value for value in values if value))


def targets_for_field(field: dict[str, str]) -> set[str]:
    return {item.strip() for item in field["requiredFor"].split(";") if item.strip()}


def certiorari_fields_for_targets(
        readiness_rows: list[dict[str, str]],
        target_keys: list[str],
        statuses: set[str],
        validation_use: str | None = None
) -> str:
    output: list[str] = []
    target_set = set(target_keys)
    for row in readiness_rows:
        field_targets = targets_for_field(row)
        if "all" not in field_targets and not field_targets.intersection(target_set):
            continue
        if row["currentStatus"] not in statuses:
            continue
        if validation_use and row["validationUse"] != validation_use:
            continue
        output.append(row["fieldName"])
    return unique_join(output)


def certiorari_source_boundary(source_key: str, registry_row: dict[str, str], journal_total: int) -> str:
    if source_key == "scotus-certiorari-docketed-cohorts-ot2023-ot2024":
        cohort_total, _cohort_counts, cert_total, _cert_counts = certiorari_docketed_cohort_counts()
        granted_total, _granted_counts = certiorari_granted_docket_detail_counts()
        journal_docket_total, _journal_docket_counts = certiorari_journal_docket_detail_counts()
        granted_note = (
            f" plus official docket detail for {granted_total} granted/GVR rows"
            if granted_total
            else ""
        )
        journal_docket_note = (
            f" plus reachable public docket detail for {journal_docket_total} Journal disposition rows"
            if journal_docket_total
            else ""
        )
        return (
            f"The independently enumerated official-docket cohorts close 8,076 paid/IFP "
            f"dockets and identify 7,716 certiorari petitions across OT2023 and OT2024. "
            f"The OT2023 field-audit anchor contains {cohort_total} dockets and {cert_total} "
            f"certiorari petitions; its older Journal reconciliation has {journal_total} "
            f"source-addressed disposition rows{granted_note}{journal_docket_note}. Three "
            "OT2024 petitions remain pending, four same-cutoff-date dockets above the "
            "Journal count-defined ranges are explicit exclusions, and undocketed "
            "submissions plus specialist-counsel/split-quality coding remain outside scope"
        )
    status = registry_row.get("benchmarkStatus", "source slice not yet extracted")
    notes = registry_row.get("notes", "")
    if notes:
        return f"{status}; {notes}"
    return status


def certiorari_publication_gate(source_key: str, target_keys: list[str]) -> str:
    if source_key == "scotus-certiorari-docketed-cohorts-ot2023-ot2024":
        return (
            "met for the paired OT2023-OT2024 docketed-intake denominators and docket-visible filing, "
            "paid/IFP, response/CFR, CVSG, amicus, relist, and cert-stage outcome fields; "
            "retain the three-pending-outcome and OT2024 count-snapshot boundaries, the "
            "undocketed-submission boundary, and separate partial metadata/merits fields"
        )
    if "cert_cfr_response" in target_keys or "cert_cvsg_signal" in target_keys:
        return (
            "row-level CFR/CVSG extraction must reconcile paid, IFP, U.S.-respondent, SG-response, "
            "and CVSG denominators before CFR or CVSG validation language is upgraded"
        )
    if "cert_elite_counsel" in target_keys:
        return (
            "counsel and amicus rows must preserve their filtered-sample or non-SG denominator "
            "and cannot be merged into whole-cohort specialist-counsel prevalence"
        )
    if "cert_split_quality" in target_keys:
        return (
            "alleged and genuine split coding must remain in the same petition or conflict sample "
            "before split-quality logic is treated as a benchmark"
        )
    return "source rows must reconcile to their own denominator before any manuscript upgrade"


def build_certiorari_closure_plan_rows(dashboard_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    workqueue_rows = build_certiorari_workqueue_rows(dashboard_rows)
    readiness_rows = build_certiorari_field_readiness_rows(dashboard_rows)
    protocols = protocol_lookup(dashboard_rows)
    registry = {row["sourceKey"]: row for row in read_csv(BENCHMARK_SOURCE_REGISTRY_CSV)}
    journal_total, _journal_counts = certiorari_journal_disposition_counts()

    source_order: list[str] = []
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in workqueue_rows:
        source_key = row["sourceKey"]
        if source_key not in grouped:
            source_order.append(source_key)
        grouped[source_key].append(row)

    output: list[dict[str, str]] = []
    for source_key in source_order:
        rows = grouped[source_key]
        target_keys = unique_join([row["targetKey"] for row in rows]).split("; ")
        metrics = [
            metric
            for target_key in target_keys
            for metric in protocols.get(target_key, {}).get("metrics", [])
        ]
        source_name = unique_join([row["sourceName"] for row in rows]) or registry.get(source_key, {}).get("sourceName", "")
        benchmark_targets = unique_join([row["benchmarkTarget"] for row in rows])
        source_url = unique_join([row["sourceUrl"] for row in rows]) or registry.get(source_key, {}).get("sourceUrl", "")
        seeded_fields = certiorari_fields_for_targets(
            readiness_rows,
            target_keys,
            {
                "closed_docketed_cohort_complete",
                "closed_docketed_cohort_partial",
                "journal_disposition_seed",
                "journal_public_docket_detail_partial",
                "aggregate_guardrail_only",
                "granted_gvr_docket_detail",
            },
        )
        required_blocking = certiorari_fields_for_targets(
            readiness_rows,
            target_keys,
            {"required_not_row_coded", "closed_docketed_cohort_partial"},
            "required",
        )
        recommended_blocking = certiorari_fields_for_targets(
            readiness_rows,
            target_keys,
            {"recommended_not_row_coded", "closed_docketed_cohort_partial"},
            "recommended",
        )
        manuscript_use = (
            "Paired OT2023-OT2024 docketed-intake and docket-visible screening descriptions may be used "
            "within their stated denominator; no counsel, split-quality, undocketed-submission, "
            "or incomplete merits-field validation upgrade."
            if source_key == "scotus-certiorari-docketed-cohorts-ot2023-ot2024"
            else "No validation upgrade until the source-slice completion gate is met and rows reconcile to their stated denominator."
        )
        output.append({
            "planRank": str(len(output) + 1),
            "sourceKey": source_key,
            "sourceName": source_name,
            "sourceUrl": source_url,
            "targetKeys": unique_join(target_keys),
            "benchmarkTargets": benchmark_targets,
            "blockingReadinessRows": readiness_links(dashboard_rows, metrics),
            "currentBoundary": certiorari_source_boundary(source_key, registry.get(source_key, {}), journal_total),
            "seededFieldsAvailable": seeded_fields or "none",
            "requiredFieldsStillBlocking": required_blocking or "none",
            "recommendedFieldsStillBlocking": recommended_blocking or "none",
            "minimumViableExtraction": unique_join([row["unitOfWork"] for row in rows]),
            "completionGate": unique_join([row["completionEvidence"] for row in rows]),
            "publicationGate": certiorari_publication_gate(source_key, target_keys),
            "manuscriptUse": manuscript_use,
        })
    return output


def write_certiorari_closure_plan(rows: list[dict[str, str]]) -> None:
    plan_rows = build_certiorari_closure_plan_rows(rows)
    with CERTIORARI_COHORT_CLOSURE_PLAN_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(plan_rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(plan_rows)

    lines = [
        "# Certiorari Cohort Closure Plan v1",
        "",
        "This generated plan distinguishes the completed paired OT2023-OT2024 paid/IFP docketed-intake and docket-visible screening benchmark from the remaining respondent-type, specialist-counsel, issue-area, split-quality, and merits-follow-through source slices. The OT2023 cohort remains the detailed field-completeness audit anchor. Closed-cohort status does not extend to submissions never docketed, and the OT2024 outcome rate excludes three petitions still pending or held at the snapshot.",
        "",
        "| Rank | Source | Targets | Current boundary | Required fields still blocking | Minimum viable extraction | Publication gate |",
        "| ---: | --- | --- | --- | --- | --- | --- |",
    ]
    for row in plan_rows:
        lines.append(
            f"| {row['planRank']} | {markdown_cell(row['sourceKey'])} | "
            f"{markdown_cell(row['benchmarkTargets'])} | {markdown_cell(row['currentBoundary'])} | "
            f"{markdown_cell(row['requiredFieldsStillBlocking'])} | "
            f"{markdown_cell(row['minimumViableExtraction'])} | {markdown_cell(row['publicationGate'])} |"
        )
    CERTIORARI_COHORT_CLOSURE_PLAN_MD.write_text("\n".join(lines) + "\n")


def implementation_compliance_closure_targets() -> list[dict[str, object]]:
    environmental_events = read_csv(ENVIRONMENTAL_LOWER_COURT_EVENTS_CSV)
    environmental_exposure = read_csv(ENVIRONMENTAL_CIRCUIT_EXPOSURE_CSV)
    environmental_practical = read_csv(ENVIRONMENTAL_PRACTICAL_IMPLEMENTATION_CSV)
    environmental_decisions = {
        row.get("sourceDecisionKey", "") for row in environmental_events
        if row.get("sourceDecisionKey", "")
    }
    full_text_events = sum(
        row.get("fullTextStatus") == "available" for row in environmental_events
    )
    context_events = sum(
        bool(row.get("citationContext")) for row in environmental_events
    )
    practical_counts: dict[str, int] = defaultdict(int)
    for row in environmental_practical:
        practical_counts[row.get("authorClassification", "")] += 1
    return [
        {
            "sourceSlice": "lower-court-doctrinal-uptake",
            "targetPathway": "lower_court_compliance",
            "benchmarkTargets": "lower-court doctrinal uptake",
            "metrics": ["lowerCourtCompliance"],
            "currentBoundary": (
                "The aggregate benchmark covers 876 Supreme Court precedents and 223 source-flagged "
                "constitutional-issue precedents. A separate environmental cohort now adds "
                f"{len(environmental_events)} deduplicated published citation-linked federal opinion documents "
                f"for {len(environmental_decisions)} Supreme Court decisions, with public full text "
                f"for {full_text_events} rows and source-decision context for {context_events}, plus "
                f"{len(environmental_exposure)} nationwide-applicability/published-citation-presence "
                "cells. Full-text missingness is nonrandom, and automated directional candidates remain "
                "pending expert review. The cells are descriptive, not an empirical exposure, all-"
                "relevant-case opportunity, ignored-precedent, remedy-fidelity, or representative "
                "constitutional-case denominator."
            ),
            "requiredSourceUnit": (
                "post-decision lower-court citation or treatment row joined to a source decision"
            ),
            "requiredFields": (
                "decisionId; decidingCourt; lowerCourt; treatmentType; treatmentDate; "
                "followedOrDistinguished; remedyFidelity; monitoringSource; sourceUrl; coderNotes"
            ),
            "candidateSources": (
                "U.S. lower-court precedent-response datasets; official court opinions; "
                "citator treatment exports with reproducible filters"
            ),
            "minimumViableExtraction": (
                "aggregate doctrinal-uptake and bounded environmental acquisition snapshot completed; "
                "next expand beyond five purposively selected statutory cases and acquire a relevant-"
                "case opportunity or remedy-fidelity denominator"
            ),
            "completionGate": (
                "the environmental snapshot reconciles to five explicitly published-only CourtListener searches, "
                "document provider-cluster deduplication, retain treatment date and source URL, and "
                "separate citation-only or unclear rows from automated directional candidates; expert "
                "legal review remains a separate open step"
            ),
            "publicationGate": (
                "Use the environmental rows only as a descriptive published-citation case study and "
                "data-quality audit. No lowerCourtCompliance validation upgrade until expert coding, a relevant-case "
                "opportunity or ignored-case denominator, remedy fidelity, broader decision coverage, "
                "and construct alignment close the remaining gaps."
            ),
            "manuscriptUse": (
                "bounded aggregate doctrinal-uptake plus descriptive environmental published-citation "
                "presence and automated-candidate evidence; not a denominator-matched lowerCourtCompliance target"
            ),
        },
        {
            "sourceSlice": "implementation-resistance",
            "targetPathway": "lower_court_compliance",
            "benchmarkTargets": "implementation resistance; government noncompliance",
            "metrics": ["lowerCourtResistanceRisk", "governmentNoncomplianceRate"],
            "currentBoundary": (
                f"A five-decision practical environmental cohort now contains "
                f"{len(environmental_practical)} agency implementation episodes: "
                f"{practical_counts.get('compliant', 0)} compliant and "
                f"{practical_counts.get('narrowly compliant', 0)} narrowly compliant under the "
                "published three-part classification. It is a purposive salient statutory sample "
                "with no observed noncompliant episode, not a representative agency, constitutional-"
                "case, resistance, or government-noncompliance denominator."
            ),
            "requiredSourceUnit": (
                "post-judgment implementation, enforcement, delay, or resistance episode"
            ),
            "requiredFields": (
                "decisionId; actorType; implementationAction; delayDays; resistanceCategory; "
                "enforcementCapacity; practicalResponse; sourceUrl; coderNotes"
            ),
            "candidateSources": (
                "agency implementation records; executive directives; compliance litigation dockets; "
                "official monitoring reports; scholarly event datasets"
            ),
            "minimumViableExtraction": (
                "bounded five-decision practical-implementation acquisition snapshot completed; next add broader "
                "decision and agency coverage with observed delay, symbolic compliance, resistance, "
                "and noncompliance outcomes"
            ),
            "completionGate": (
                "the five episode rows reconcile to the published purposive sample and expose actor, "
                "official action, delay, resistance category, practical response, source URL, and "
                "verified primary-source document hash"
            ),
            "publicationGate": (
                "Use only as bounded practical-implementation evidence. No governmentNoncomplianceRate "
                "or general resistance validation upgrade until a broader cohort includes noncompliant "
                "outcomes and supports a denominator-specific rate."
            ),
            "manuscriptUse": (
                "bounded purposive environmental practical-implementation evidence; not a general "
                "agency-compliance, resistance, or government-noncompliance rate"
            ),
        },
        {
            "sourceSlice": "monitoring-capacity",
            "targetPathway": "lower_court_compliance",
            "benchmarkTargets": "monitoring capacity",
            "metrics": ["interbranchCompliance"],
            "currentBoundary": (
                "A direct HUDOC-EXEC pending-leading-case monitoring extract is now coded for a "
                "bounded ECtHR execution-supervision slice; it supports monitoring-capacity context "
                "only and does not validate doctrinal lower-court uptake, practical compliance, or "
                "government noncompliance."
            ),
            "requiredSourceUnit": (
                "monitoring report, compliance dashboard row, execution status update, or enforcement step"
            ),
            "requiredFields": (
                "decisionId; monitoringBody; reportingInterval; complianceStatus; "
                "unresolvedDurationDays; enforcementStep; sourceUrl; coderNotes"
            ),
            "candidateSources": (
                "constitutional-court monitoring offices; ECtHR execution data; public compliance "
                "dashboards; official annual or status reports"
            ),
            "minimumViableExtraction": (
                "completed for the live HUDOC-EXEC English pending-leading-case query; extend with "
                "country-specific execution documents, annual-report aggregate reconciliation, or "
                "closed-case rows before making broader monitoring-throughput claims"
            ),
            "completionGate": (
                "HUDOC-EXEC rows reconcile to the documented API result count and distinguish "
                "pending leading cases by supervision track and unresolved duration"
            ),
            "publicationGate": (
                "Use only as bounded monitoring-capacity evidence until closed-case, country, or "
                "annual-report aggregate reconciliation supports broader execution-throughput claims."
            ),
            "manuscriptUse": (
                "bounded monitoring-capacity evidence; not lower-court compliance, implementation "
                "resistance, or government-noncompliance validation"
            ),
        },
        {
            "sourceSlice": "emergency-downstream-implementation",
            "targetPathway": "emergency",
            "benchmarkTargets": "emergency downstream effect",
            "metrics": ["emergencyDownstreamEffect"],
            "currentBoundary": (
                "Granted and denied/NA emergency rows now have official-docket linkage and "
                "docket-derived downstream status, but external implementation observations are missing."
            ),
            "requiredSourceUnit": (
                "granted emergency application joined to downstream policy, lower-court, agency, "
                "or implementation observation"
            ),
            "requiredFields": (
                "sourceRecordId; docketNumber; linkedMeritsDocket; actorType; policyStatus; "
                "implementationDate; repeatFilingFlag; externalSourceUrl; coderNotes"
            ),
            "candidateSources": (
                "official Supreme Court dockets and orders; lower-court follow-on orders; agency "
                "policy pages; government implementation notices; source-backed public policy trackers"
            ),
            "minimumViableExtraction": (
                "coded emergency rows joined to external implementation observations, with the "
                "denied/NA official-docket slice retained as the all-application docket-linkage boundary"
            ),
            "completionGate": (
                "each granted emergency matter has source-backed implementation status, actor, date, "
                "and repeat-filing flag or a documented unavailable-source reason"
            ),
            "publicationGate": (
                "No validation upgrade until external implementation observations join to coded "
                "emergency rows and docket-derived versus external-implementation limits stay explicit."
            ),
            "manuscriptUse": (
                "not validation evidence; use only as a work plan until the completion gate is met"
            ),
        },
    ]


def build_implementation_compliance_closure_plan_rows(
        dashboard_rows: list[dict[str, str]]
) -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    for index, target in enumerate(implementation_compliance_closure_targets(), start=1):
        metrics = list(target["metrics"])
        output.append({
            "planRank": str(index),
            "sourceSlice": str(target["sourceSlice"]),
            "targetPathway": str(target["targetPathway"]),
            "benchmarkTargets": str(target["benchmarkTargets"]),
            "simulatorMetrics": "; ".join(metrics),
            "blockingReadinessRows": readiness_links(dashboard_rows, metrics),
            "currentBoundary": (
                f"{target['currentBoundary']} Current evidence limits: "
                f"{current_evidence_limits(dashboard_rows, metrics)}."
            ),
            "requiredSourceUnit": str(target["requiredSourceUnit"]),
            "requiredFields": str(target["requiredFields"]),
            "candidateSources": str(target["candidateSources"]),
            "minimumViableExtraction": str(target["minimumViableExtraction"]),
            "completionGate": str(target["completionGate"]),
            "publicationGate": str(target["publicationGate"]),
            "manuscriptUse": str(target["manuscriptUse"]),
        })
    return output


def write_implementation_compliance_closure_plan(rows: list[dict[str, str]]) -> None:
    plan_rows = build_implementation_compliance_closure_plan_rows(rows)
    with IMPLEMENTATION_COMPLIANCE_CLOSURE_PLAN_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(plan_rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(plan_rows)

    lines = [
        "# Implementation and Compliance Closure Plan v1",
        "",
        "This generated plan distinguishes four bounded acquisition snapshots---aggregate lower-court doctrinal uptake, descriptive environmental published-citation presence and automated treatment candidates, purposive environmental practical implementation, and HUDOC-EXEC monitoring capacity---from the remaining expert-coding, relevant-case opportunity, remedy-fidelity, broader implementation/noncompliance, and emergency-downstream source-acquisition work. Each slice keeps its own manuscript-use boundary; none supplies denominator-matched general compliance validation.",
        "",
        "| Rank | Source slice | Targets | Current boundary | Required source unit | Minimum viable extraction | Publication gate |",
        "| ---: | --- | --- | --- | --- | --- | --- |",
    ]
    for row in plan_rows:
        lines.append(
            f"| {row['planRank']} | {markdown_cell(row['sourceSlice'])} | "
            f"{markdown_cell(row['benchmarkTargets'])} | {markdown_cell(row['currentBoundary'])} | "
            f"{markdown_cell(row['requiredSourceUnit'])} | "
            f"{markdown_cell(row['minimumViableExtraction'])} | {markdown_cell(row['publicationGate'])} |"
        )
    IMPLEMENTATION_COMPLIANCE_CLOSURE_PLAN_MD.write_text("\n".join(lines) + "\n")


def implementation_schema_target(source_slice: str) -> str:
    return source_slice.replace("-", "_")


def build_implementation_compliance_workqueue_rows(
        dashboard_rows: list[dict[str, str]]
) -> list[dict[str, str]]:
    closure_rows = build_implementation_compliance_closure_plan_rows(dashboard_rows)
    output: list[dict[str, str]] = []
    for row in closure_rows:
        schema_target = implementation_schema_target(row["sourceSlice"])
        output.append({
            "queueRank": str(len(output) + 1),
            "sourceSlice": row["sourceSlice"],
            "schemaTarget": schema_target,
            "targetPathway": row["targetPathway"],
            "benchmarkTargets": row["benchmarkTargets"],
            "simulatorMetrics": row["simulatorMetrics"],
            "requiredSourceUnit": row["requiredSourceUnit"],
            "requiredFields": schema_fields(schema_target, "required", IMPLEMENTATION_COMPLIANCE_SCHEMA_CSV),
            "recommendedFields": schema_fields(schema_target, "recommended", IMPLEMENTATION_COMPLIANCE_SCHEMA_CSV),
            "candidateSources": row["candidateSources"],
            "coderAction": (
                "copy data/benchmarks/implementation-compliance-template.csv and code one row per "
                f"{row['requiredSourceUnit']}; keep sourceSlice={row['sourceSlice']}"
            ),
            "completionEvidence": row["completionGate"],
            "denominatorGate": row["publicationGate"],
            "manuscriptUse": (
                row["manuscriptUse"]
                if row["sourceSlice"] in {
                    "lower-court-doctrinal-uptake",
                    "implementation-resistance",
                    "monitoring-capacity",
                }
                else (
                    "not validation until coded rows reconcile to the stated denominator and satisfy "
                    "the completion evidence"
                )
            ),
        })
    return output


def write_implementation_compliance_workqueue(rows: list[dict[str, str]]) -> None:
    workqueue_rows = build_implementation_compliance_workqueue_rows(rows)
    with IMPLEMENTATION_COMPLIANCE_WORKQUEUE_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(workqueue_rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(workqueue_rows)

    lines = [
        "# Implementation and Compliance Work Queue v1",
        "",
        "This generated work queue converts the implementation/compliance closure plan and schema into source-specific coding tasks. It preserves the bounded descriptive uses supported by the aggregate doctrinal-uptake, environmental published-citation snapshot, environmental practical-implementation, and HUDOC-EXEC monitoring slices while identifying the expert-coding, relevant-case opportunity, remedy-fidelity, noncompliance-outcome, and emergency downstream fields still required for stronger claims.",
        "",
        "| Rank | Source slice | Metrics | Required source unit | Required fields | Candidate sources | Completion evidence | Manuscript use |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in workqueue_rows:
        lines.append(
            f"| {row['queueRank']} | {markdown_cell(row['sourceSlice'])} | "
            f"`{markdown_cell(row['simulatorMetrics'])}` | {markdown_cell(row['requiredSourceUnit'])} | "
            f"{markdown_cell(row['requiredFields'])} | {markdown_cell(row['candidateSources'])} | "
            f"{markdown_cell(row['completionEvidence'])} | {markdown_cell(row['manuscriptUse'])} |"
        )
    IMPLEMENTATION_COMPLIANCE_WORKQUEUE_MD.write_text("\n".join(lines) + "\n")


def build_certiorari_journal_disposition_summary_rows() -> list[dict[str, str]]:
    rows = read_csv(CERTIORARI_JOURNAL_DISPOSITION_EXTRACT_CSV)
    if not rows:
        return []
    term = rows[0]["term"]
    source_key = rows[0]["sourceKey"]
    dispositions: dict[str, int] = defaultdict(int)
    paid_ifp: dict[str, int] = defaultdict(int)
    for row in rows:
        dispositions[row["certDisposition"]] += 1
        paid_ifp[row["paidOrIfp"]] += 1
    unique_dockets = len({row["docketNumber"] for row in rows})
    unique_dates = len({row["dispositionDate"] for row in rows if row["dispositionDate"]})
    dates = sorted({row["dispositionDate"] for row in rows if row["dispositionDate"]})
    dated = sum(1 for row in rows if row["dispositionDate"])
    lower_court = sum(1 for row in rows if row["lowerCourt"])

    def summary_row(
            metric: str,
            value: int,
            comparison: str,
            status: str,
            notes: str,
    ) -> dict[str, str]:
        return {
            "metricKey": metric,
            "sourceKey": source_key,
            "term": term,
            "observedValue": str(value),
            "comparisonValue": comparison,
            "reconciliationStatus": status,
            "manuscriptUse": "row-level disposition seed only; not closed filing-cohort validation",
            "notes": notes,
        }

    return [
        summary_row(
            "journalCertiorariDispositionRows",
            len(rows),
            "",
            "candidate_extract",
            "One row per docket number parsed from official Journal certiorari disposition entries.",
        ),
        summary_row(
            "journalCertiorariUniqueDockets",
            unique_dockets,
            "",
            "candidate_extract",
            "Unique docket count can differ from row count when consolidated entries list multiple docket numbers.",
        ),
        summary_row(
            "journalCertiorariUniqueDispositionDates",
            unique_dates,
            "",
            "candidate_extract",
            "Distinct Journal date headings assigned to disposition entries.",
        ),
        summary_row(
            "journalCertiorariFirstDispositionDate",
            int(dates[0].replace("-", "")) if dates else 0,
            "",
            "candidate_extract",
            "Earliest Journal date heading assigned to a disposition entry, formatted as YYYYMMDD for CSV consistency.",
        ),
        summary_row(
            "journalCertiorariLastDispositionDate",
            int(dates[-1].replace("-", "")) if dates else 0,
            "",
            "candidate_extract",
            "Latest Journal date heading assigned to a disposition entry, formatted as YYYYMMDD for CSV consistency.",
        ),
        summary_row(
            "journalCertiorariPaidDispositionRows",
            paid_ifp.get("paid", 0),
            "official OT2023 paid docketed during term = 1375",
            "not_expected_to_match_term_flow",
            "Disposition rows include prior-term carryover dockets and omit still-pending docketed matters.",
        ),
        summary_row(
            "journalCertiorariIfpDispositionRows",
            paid_ifp.get("ifp", 0),
            "official OT2023 IFP docketed during term = 2847",
            "not_expected_to_match_term_flow",
            "Disposition rows include prior-term carryover dockets and omit still-pending docketed matters.",
        ),
        summary_row(
            "journalCertiorariApplicationOrMiscRows",
            paid_ifp.get("application_or_misc", 0),
            "",
            "review_boundary",
            "Application or miscellaneous dockets are included only when the Journal text treats them as certiorari before judgment or certiorari-related entries.",
        ),
        summary_row(
            "journalCertiorariDeniedRows",
            dispositions.get("denied", 0),
            "",
            "candidate_extract",
            "Routine denied-petition dispositions parsed from Journal text.",
        ),
        summary_row(
            "journalCertiorariGrantedRows",
            dispositions.get("granted", 0),
            "",
            "candidate_extract",
            "Rows where the parser found a grant without GVR/remand wording.",
        ),
        summary_row(
            "journalCertiorariGvrOrRemandRows",
            dispositions.get("gvr_or_remand", 0),
            "",
            "candidate_extract",
            "Rows where the parser found certiorari granted plus vacated or remanded wording.",
        ),
        summary_row(
            "journalCertiorariDismissedRows",
            dispositions.get("dismissed", 0),
            "",
            "candidate_extract",
            "Dismissal rows parsed from Journal certiorari entries.",
        ),
        summary_row(
            "journalCertiorariReviewRequiredRows",
            dispositions.get("other_disposition_review_required", 0),
            "",
            "manual_review_required" if dispositions.get("other_disposition_review_required", 0) else "none_remaining",
            "Rows whose certiorari entry was captured but whose disposition text needs manual review after parser classification.",
        ),
        summary_row(
            "journalCertiorariRowsWithDispositionDate",
            dated,
            str(len(rows)),
            "matches_extract_rows" if dated == len(rows) else "missing_dates",
            "Disposition date comes from the Journal date heading nearest the entry.",
        ),
        summary_row(
            "journalCertiorariRowsWithLowerCourt",
            lower_court,
            str(len(rows)),
            "partial_extract",
            "Lower-court text is parsed from the Journal entry where visible.",
        ),
    ]


def write_certiorari_journal_disposition_summary() -> None:
    rows = build_certiorari_journal_disposition_summary_rows()
    if not rows:
        return
    with CERTIORARI_JOURNAL_DISPOSITION_SUMMARY_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Certiorari Journal Disposition Summary v1",
        "",
        "This report summarizes the first row-level certiorari disposition seed extracted from the official OT2023 Journal. It is source-addressable disposition evidence, not a closed petition filing cohort and not denominator-matched validation.",
        "",
        "| Metric | Observed | Comparison | Status | Notes |",
        "| --- | ---: | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| `{markdown_cell(row['metricKey'])}` | {row['observedValue']} | "
            f"{markdown_cell(row['comparisonValue'])} | {markdown_cell(row['reconciliationStatus'])} | "
            f"{markdown_cell(row['notes'])} |"
        )
    CERTIORARI_JOURNAL_DISPOSITION_SUMMARY_MD.write_text("\n".join(lines) + "\n")


def main() -> None:
    rows = build_dashboard_rows()
    write_dashboard(rows)
    write_coverage(rows)
    write_metric_semantics(rows)
    write_benchmark_readiness(rows)
    write_benchmark_protocol(rows)
    write_schema_template(EMERGENCY_LINKAGE_SCHEMA_CSV, EMERGENCY_LINKAGE_TEMPLATE_CSV)
    write_schema_template(CERTIORARI_COHORT_SCHEMA_CSV, CERTIORARI_COHORT_TEMPLATE_CSV)
    write_schema_template(IMPLEMENTATION_COMPLIANCE_SCHEMA_CSV, IMPLEMENTATION_COMPLIANCE_TEMPLATE_CSV)
    write_benchmark_workqueue(rows)
    write_certiorari_workqueue(rows)
    write_emergency_application_reconciliation()
    write_emergency_grant_linkage_workqueue()
    write_emergency_denied_linkage_workqueue()
    write_emergency_field_readiness()
    write_certiorari_term_flow_reconciliation()
    write_certiorari_multi_term_benchmark()
    write_certiorari_field_readiness(rows)
    write_certiorari_closure_plan(rows)
    write_implementation_compliance_closure_plan(rows)
    write_implementation_compliance_workqueue(rows)
    write_certiorari_journal_disposition_summary()
    print(f"Wrote {DASHBOARD_CSV.relative_to(ROOT)}")
    print(f"Wrote {DASHBOARD_MD.relative_to(ROOT)}")
    print(f"Wrote {PRIMARY_COVERAGE_CSV.relative_to(ROOT)}")
    print(f"Wrote {PRIMARY_COVERAGE_MD.relative_to(ROOT)}")
    print(f"Wrote {METRIC_SEMANTICS_CSV.relative_to(ROOT)}")
    print(f"Wrote {METRIC_SEMANTICS_MD.relative_to(ROOT)}")
    print(f"Wrote {BENCHMARK_READINESS_CSV.relative_to(ROOT)}")
    print(f"Wrote {BENCHMARK_READINESS_MD.relative_to(ROOT)}")
    print(f"Wrote {BENCHMARK_PROTOCOL_CSV.relative_to(ROOT)}")
    print(f"Wrote {BENCHMARK_PROTOCOL_MD.relative_to(ROOT)}")
    print(f"Wrote {EMERGENCY_LINKAGE_TEMPLATE_CSV.relative_to(ROOT)}")
    print(f"Wrote {CERTIORARI_COHORT_TEMPLATE_CSV.relative_to(ROOT)}")
    print(f"Wrote {IMPLEMENTATION_COMPLIANCE_TEMPLATE_CSV.relative_to(ROOT)}")
    print(f"Wrote {BENCHMARK_WORKQUEUE_CSV.relative_to(ROOT)}")
    print(f"Wrote {BENCHMARK_WORKQUEUE_MD.relative_to(ROOT)}")
    print(f"Wrote {CERTIORARI_WORKQUEUE_CSV.relative_to(ROOT)}")
    print(f"Wrote {CERTIORARI_WORKQUEUE_MD.relative_to(ROOT)}")
    print(f"Wrote {EMERGENCY_APPLICATION_RECONCILIATION_CSV.relative_to(ROOT)}")
    print(f"Wrote {EMERGENCY_APPLICATION_RECONCILIATION_MD.relative_to(ROOT)}")
    print(f"Wrote {EMERGENCY_GRANT_LINKAGE_WORKQUEUE_CSV.relative_to(ROOT)}")
    print(f"Wrote {EMERGENCY_GRANT_LINKAGE_WORKQUEUE_MD.relative_to(ROOT)}")
    print(f"Wrote {EMERGENCY_DENIED_LINKAGE_WORKQUEUE_CSV.relative_to(ROOT)}")
    print(f"Wrote {EMERGENCY_DENIED_LINKAGE_WORKQUEUE_MD.relative_to(ROOT)}")
    print(f"Wrote {EMERGENCY_FIELD_READINESS_CSV.relative_to(ROOT)}")
    print(f"Wrote {EMERGENCY_FIELD_READINESS_MD.relative_to(ROOT)}")
    print(f"Wrote {CERTIORARI_TERM_FLOW_RECONCILIATION_CSV.relative_to(ROOT)}")
    print(f"Wrote {CERTIORARI_TERM_FLOW_RECONCILIATION_MD.relative_to(ROOT)}")
    print(f"Wrote {CERTIORARI_MULTI_TERM_BENCHMARK_CSV.relative_to(ROOT)}")
    print(f"Wrote {CERTIORARI_MULTI_TERM_BENCHMARK_MD.relative_to(ROOT)}")
    print(f"Wrote {CERTIORARI_FIELD_READINESS_CSV.relative_to(ROOT)}")
    print(f"Wrote {CERTIORARI_FIELD_READINESS_MD.relative_to(ROOT)}")
    print(f"Wrote {CERTIORARI_COHORT_CLOSURE_PLAN_CSV.relative_to(ROOT)}")
    print(f"Wrote {CERTIORARI_COHORT_CLOSURE_PLAN_MD.relative_to(ROOT)}")
    print(f"Wrote {IMPLEMENTATION_COMPLIANCE_CLOSURE_PLAN_CSV.relative_to(ROOT)}")
    print(f"Wrote {IMPLEMENTATION_COMPLIANCE_CLOSURE_PLAN_MD.relative_to(ROOT)}")
    print(f"Wrote {IMPLEMENTATION_COMPLIANCE_WORKQUEUE_CSV.relative_to(ROOT)}")
    print(f"Wrote {IMPLEMENTATION_COMPLIANCE_WORKQUEUE_MD.relative_to(ROOT)}")
    if CERTIORARI_JOURNAL_DISPOSITION_SUMMARY_CSV.exists():
        print(f"Wrote {CERTIORARI_JOURNAL_DISPOSITION_SUMMARY_CSV.relative_to(ROOT)}")
        print(f"Wrote {CERTIORARI_JOURNAL_DISPOSITION_SUMMARY_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
