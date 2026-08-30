#!/usr/bin/env python3
"""Verify that manuscript artifacts match the report manifests."""

from __future__ import annotations

import hashlib
import json
import re
import sys
import csv
from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PAPER_LEGISLATIVE_INPUT = "data/external/legislative/simulation-campaign-v21-paper.csv"
MANIFESTS = [
    ROOT / "reports" / "constitutional-review-campaign-v2-manifest.json",
    ROOT / "reports" / "calibration-baseline-manifest.json",
    ROOT / "reports" / "parameter-sweep-v4-manifest.json",
    ROOT / "reports" / "prior-uncertainty-v1-manifest.json",
]
CAMPAIGN_CSV = ROOT / "reports" / "constitutional-review-campaign-v2.csv"
PRIOR_UNCERTAINTY_CSV = ROOT / "reports" / "prior-uncertainty-v1.csv"
PATHWAY_DASHBOARD_CSV = ROOT / "reports" / "pathway-validation-dashboard-v1.csv"
METRIC_SEMANTICS_CSV = ROOT / "reports" / "metric-semantics-v1.csv"
BENCHMARK_READINESS_CSV = ROOT / "reports" / "benchmark-readiness-v1.csv"
BENCHMARK_PROTOCOL_CSV = ROOT / "reports" / "benchmark-extraction-protocol-v1.csv"
BENCHMARK_WORKQUEUE_CSV = ROOT / "reports" / "benchmark-extraction-workqueue-v1.csv"
CERTIORARI_WORKQUEUE_CSV = ROOT / "reports" / "certiorari-extraction-workqueue-v1.csv"
CERTIORARI_TERM_FLOW_RECONCILIATION_CSV = ROOT / "reports" / "certiorari-term-flow-reconciliation-v1.csv"
CERTIORARI_FIELD_READINESS_CSV = ROOT / "reports" / "certiorari-cohort-field-readiness-v1.csv"
CERTIORARI_COHORT_CLOSURE_PLAN_CSV = ROOT / "reports" / "certiorari-cohort-closure-plan-v1.csv"
IMPLEMENTATION_COMPLIANCE_CLOSURE_PLAN_CSV = (
    ROOT / "reports" / "implementation-compliance-closure-plan-v1.csv"
)
IMPLEMENTATION_COMPLIANCE_WORKQUEUE_CSV = (
    ROOT / "reports" / "implementation-compliance-workqueue-v1.csv"
)
CERTIORARI_TERM_FLOW_EXTRACT_CSV = ROOT / "data" / "benchmarks" / "certiorari-term-flow-extract-journal-ot2023.csv"
CERTIORARI_TERM_FLOW_MANIFEST = (
    ROOT / "data" / "benchmarks" / "certiorari-term-flow-extract-journal-ot2023-manifest.json"
)
CERTIORARI_TERM_FLOW_EXTRACT_OT2024_CSV = (
    ROOT / "data" / "benchmarks" / "certiorari-term-flow-extract-journal-ot2024.csv"
)
CERTIORARI_TERM_FLOW_OT2024_MANIFEST = (
    ROOT / "data" / "benchmarks" / "certiorari-term-flow-extract-journal-ot2024-manifest.json"
)
CERTIORARI_JOURNAL_DISPOSITION_EXTRACT_CSV = (
    ROOT / "data" / "benchmarks" / "certiorari-journal-disposition-extract-ot2023.csv"
)
CERTIORARI_JOURNAL_DISPOSITION_MANIFEST = (
    ROOT / "data" / "benchmarks" / "certiorari-journal-disposition-extract-ot2023-manifest.json"
)
CERTIORARI_JOURNAL_DISPOSITION_SUMMARY_CSV = (
    ROOT / "reports" / "certiorari-journal-disposition-summary-v1.csv"
)
CERTIORARI_JOURNAL_DOCKET_DETAIL_EXTRACT_CSV = (
    ROOT / "data" / "benchmarks" / "certiorari-journal-docket-detail-ot2023.csv"
)
CERTIORARI_JOURNAL_DOCKET_DETAIL_MANIFEST = (
    ROOT / "data" / "benchmarks" / "certiorari-journal-docket-detail-ot2023-manifest.json"
)
CERTIORARI_JOURNAL_DOCKET_DETAIL_SUMMARY_CSV = (
    ROOT / "reports" / "certiorari-journal-docket-detail-summary-v1.csv"
)
CERTIORARI_DOCKETED_COHORT_EXTRACT_CSV = (
    ROOT / "data" / "benchmarks" / "certiorari-docketed-cohort-ot2023.csv"
)
CERTIORARI_DOCKETED_COHORT_MANIFEST = (
    ROOT / "data" / "benchmarks" / "certiorari-docketed-cohort-ot2023-manifest.json"
)
CERTIORARI_DOCKETED_COHORT_SUMMARY_CSV = (
    ROOT / "reports" / "certiorari-docketed-cohort-summary-v1.csv"
)
CERTIORARI_DOCKETED_COHORT_RECONCILIATION_CSV = (
    ROOT / "reports" / "certiorari-docketed-cohort-journal-reconciliation-v1.csv"
)
CERTIORARI_DOCKETED_COHORT_RECONCILIATION_MD = (
    ROOT / "reports" / "certiorari-docketed-cohort-journal-reconciliation-v1.md"
)
CERTIORARI_DOCKETED_COHORT_CALIBRATION_CSV = (
    ROOT / "data" / "calibration" / "scotus-certiorari-docketed-cohort-ot2023.csv"
)
CERTIORARI_DOCKETED_COHORT_OT2024_EXTRACT_CSV = (
    ROOT / "data" / "benchmarks" / "certiorari-docketed-cohort-ot2024.csv"
)
CERTIORARI_DOCKETED_COHORT_OT2024_MANIFEST = (
    ROOT / "data" / "benchmarks" / "certiorari-docketed-cohort-ot2024-manifest.json"
)
CERTIORARI_DOCKETED_COHORT_OT2024_SUMMARY_CSV = (
    ROOT / "reports" / "certiorari-docketed-cohort-summary-ot2024-v1.csv"
)
CERTIORARI_DOCKETED_COHORT_OT2024_CALIBRATION_CSV = (
    ROOT / "data" / "calibration" / "scotus-certiorari-docketed-cohort-ot2024.csv"
)
CERTIORARI_MULTI_TERM_BENCHMARK_CSV = (
    ROOT / "reports" / "certiorari-multi-term-benchmark-v1.csv"
)
CERTIORARI_MULTI_TERM_BENCHMARK_MD = (
    ROOT / "reports" / "certiorari-multi-term-benchmark-v1.md"
)
CERTIORARI_MULTI_TERM_TABLE = ROOT / "paper" / "tables" / "certiorari_multi_term.tex"
CERTIORARI_JOURNAL_DOCKET_RETRIEVAL_WORKQUEUE_CSV = (
    ROOT / "reports" / "certiorari-journal-docket-retrieval-workqueue-v1.csv"
)
CERTIORARI_JOURNAL_DOCKET_RETRIEVAL_WORKQUEUE_MD = (
    ROOT / "reports" / "certiorari-journal-docket-retrieval-workqueue-v1.md"
)
CERTIORARI_GRANTED_DOCKET_DETAIL_EXTRACT_CSV = (
    ROOT / "data" / "benchmarks" / "certiorari-granted-docket-detail-ot2023.csv"
)
CERTIORARI_GRANTED_DOCKET_DETAIL_MANIFEST = (
    ROOT / "data" / "benchmarks" / "certiorari-granted-docket-detail-ot2023-manifest.json"
)
CERTIORARI_GRANTED_DOCKET_DETAIL_SUMMARY_CSV = (
    ROOT / "reports" / "certiorari-granted-docket-detail-summary-v1.csv"
)
EMERGENCY_APPLICATION_EXTRACT_CSV = ROOT / "data" / "benchmarks" / "emergency-application-order-extract-shadow-docket-v3-0.csv"
EMERGENCY_APPLICATION_RECONCILIATION_CSV = ROOT / "reports" / "emergency-application-order-reconciliation-v1.csv"
EMERGENCY_GRANT_LINKAGE_WORKQUEUE_CSV = ROOT / "data" / "benchmarks" / "emergency-application-grant-linkage-workqueue-v1.csv"
EMERGENCY_DENIED_LINKAGE_WORKQUEUE_CSV = ROOT / "data" / "benchmarks" / "emergency-application-denied-linkage-workqueue-v1.csv"
EMERGENCY_DENIED_LINKAGE_CODED_CSV = ROOT / "data" / "benchmarks" / "emergency-application-denied-linkage-coded-v1.csv"
EMERGENCY_DENIED_LINKAGE_CODED_MANIFEST = (
    ROOT / "data" / "benchmarks" / "emergency-application-denied-linkage-coded-v1-manifest.json"
)
EMERGENCY_DENIED_LINKAGE_CODED_SUMMARY_CSV = (
    ROOT / "reports" / "emergency-application-denied-linkage-coded-summary-v1.csv"
)
EMERGENCY_LINKAGE_CODED_CSV = ROOT / "data" / "benchmarks" / "emergency-application-linkage-coded-v1.csv"
EMERGENCY_LINKAGE_SCHEMA_CSV = ROOT / "data" / "benchmarks" / "emergency-application-linkage-schema.csv"
EMERGENCY_LINKAGE_TEMPLATE_CSV = ROOT / "data" / "benchmarks" / "emergency-application-linkage-template.csv"
EMERGENCY_FIELD_READINESS_CSV = ROOT / "reports" / "emergency-application-field-readiness-v1.csv"
CERTIORARI_COHORT_SCHEMA_CSV = ROOT / "data" / "benchmarks" / "certiorari-cohort-schema.csv"
CERTIORARI_COHORT_TEMPLATE_CSV = ROOT / "data" / "benchmarks" / "certiorari-cohort-template.csv"
IMPLEMENTATION_COMPLIANCE_SCHEMA_CSV = ROOT / "data" / "benchmarks" / "implementation-compliance-schema.csv"
IMPLEMENTATION_COMPLIANCE_TEMPLATE_CSV = ROOT / "data" / "benchmarks" / "implementation-compliance-template.csv"
ECTHR_EXECUTION_MONITORING_EXTRACT_CSV = (
    ROOT / "data" / "benchmarks" / "ecthr-execution-monitoring-pending-leading-cases-v1.csv"
)
ECTHR_EXECUTION_MONITORING_MANIFEST = (
    ROOT / "data" / "benchmarks" / "ecthr-execution-monitoring-pending-leading-cases-v1-manifest.json"
)
ECTHR_EXECUTION_MONITORING_SUMMARY_CSV = ROOT / "reports" / "ecthr-execution-monitoring-summary-v1.csv"
LOWER_COURT_PRECEDENT_TREATMENT_BENCHMARK_CSV = (
    ROOT / "data" / "benchmarks" / "lower-court-precedent-treatment-aggregate-v1.csv"
)
LOWER_COURT_PRECEDENT_TREATMENT_MANIFEST = (
    ROOT / "data" / "benchmarks" / "lower-court-precedent-treatment-aggregate-v1-manifest.json"
)
LOWER_COURT_PRECEDENT_TREATMENT_SUMMARY_CSV = (
    ROOT / "reports" / "lower-court-precedent-treatment-summary-v1.csv"
)
LOWER_COURT_PRECEDENT_TREATMENT_CALIBRATION_CSV = (
    ROOT / "data" / "calibration" / "lower-court-precedent-treatment-v1.csv"
)
ENVIRONMENTAL_LOWER_COURT_EVENTS_CSV = (
    ROOT / "data" / "benchmarks" / "lower-court-environmental-treatment-events-v1.csv"
)
ENVIRONMENTAL_CIRCUIT_EXPOSURE_CSV = (
    ROOT / "data" / "benchmarks" / "lower-court-environmental-circuit-exposure-v1.csv"
)
ENVIRONMENTAL_PRACTICAL_IMPLEMENTATION_CSV = (
    ROOT / "data" / "benchmarks" / "environmental-practical-implementation-events-v1.csv"
)
ENVIRONMENTAL_IMPLEMENTATION_CALIBRATION_CSV = (
    ROOT / "data" / "calibration" / "environmental-implementation-cohort-v1.csv"
)
ENVIRONMENTAL_IMPLEMENTATION_MANIFEST = (
    ROOT / "data" / "benchmarks" / "environmental-implementation-cohort-v1-manifest.json"
)
ENVIRONMENTAL_IMPLEMENTATION_SUMMARY_CSV = (
    ROOT / "reports" / "environmental-implementation-cohort-summary-v1.csv"
)
ENVIRONMENTAL_IMPLEMENTATION_SUMMARY_MD = (
    ROOT / "reports" / "environmental-implementation-cohort-summary-v1.md"
)
ENVIRONMENTAL_FULL_TEXT_AVAILABILITY_CSV = (
    ROOT / "reports" / "environmental-full-text-availability-audit-v1.csv"
)
ENVIRONMENTAL_FULL_TEXT_AVAILABILITY_MD = (
    ROOT / "reports" / "environmental-full-text-availability-audit-v1.md"
)
ENVIRONMENTAL_TREATMENT_REVIEW_QUEUE_CSV = (
    ROOT / "data" / "benchmarks" / "environmental-directional-treatment-review-queue-v1.csv"
)
GURGANUS_TABLE_1_CLASSIFICATIONS_CSV = (
    ROOT / "data" / "benchmarks" / "gurganus-2025-table-1-classifications-v1.csv"
)
REQUIRED_CAMPAIGN_COLUMNS = {
    "certiorariPathRate",
    "certiorariAdmissionRate",
    "paidCertPetitionShare",
    "ifpCertPetitionShare",
    "cvsgRequestRate",
    "paidCfrRequestRate",
    "ifpCfrRequestRate",
    "lowerCourtSplitDepth",
    "lowerCourtIdeologicalDrift",
    "lowerCourtResistanceRisk",
    "forumShoppingPressure",
    "preReviewSettlementPressure",
    "settledBeforeReviewRate",
    "strategicPlaintiffSelection",
    "repeatPlayerAdvantage",
    "repeatPlayerLearning",
    "emergencyIncentiveLearning",
    "complianceLearning",
    "governmentNoncomplianceRisk",
    "governmentNoncomplianceRate",
    "enforcementCapacity",
    "emergencyOpportunism",
    "emergencyProcessIrregularity",
    "processLegitimacyProxy",
    "rightsPriorityScore",
    "emergencyRestraintScore",
    "democraticResponsivenessPriorityScore",
    "legalStabilityPriorityScore",
    "lowConflictScore",
    "administrativeFeasibilityScore",
    "emergencyGrantConditionalRate",
    "emergencyGrantPerEmergencyStayDocket",
    "meritsAccelerationPerEmergencyStayDocket",
    "recusalIncentivePressure",
    "constitutionalRemandRate",
    "publicInterestFilteredRate",
    "precedentDurability",
    "emergencyDownstreamEffect",
    "emergencyRightsClaimantSuccess",
}
REQUIRED_PRIOR_COLUMNS = {
    "scenarioKey",
    "directionalP05",
    "directionalP50",
    "directionalP95",
    "interpretation",
}
REQUIRED_PATHWAY_COLUMNS = {
    "pathway",
    "simulatorMetric",
    "sourceMetric",
    "sourceTier",
    "sourceValidationUse",
    "validationUse",
    "denominatorCompatibility",
    "simulatorDenominator",
    "sourceDenominator",
    "comparabilityNote",
    "nextValidationAction",
}
REQUIRED_METRIC_SEMANTICS_COLUMNS = {
    "metricFamily",
    "metric",
    "simulatorDenominatorOrScale",
    "sourceDenominatorOrScale",
    "empiricalUse",
    "denominatorCompatibility",
    "manuscriptInterpretation",
}
REQUIRED_BENCHMARK_READINESS_COLUMNS = {
    "priorityRank",
    "priorityScore",
    "priorityBand",
    "pathway",
    "construct",
    "simulatorMetric",
    "sourceMetric",
    "sourceTier",
    "validationUse",
    "denominatorCompatibility",
    "sourceObservations",
    "benchmarkStatus",
    "benchmarkQuestion",
    "requiredEvidence",
    "manuscriptUseAfterCompletion",
}
REQUIRED_BENCHMARK_PROTOCOL_COLUMNS = {
    "protocolRank",
    "targetKey",
    "benchmarkTarget",
    "pathway",
    "simulatorMetrics",
    "blockingReadinessRows",
    "currentEvidenceLimit",
    "requiredSourceUnit",
    "requiredFields",
    "recommendedFields",
    "candidateSources",
    "completionRule",
    "validationUpgrade",
    "firstExtractionSlice",
}
REQUIRED_BENCHMARK_WORKQUEUE_COLUMNS = {
    "queueRank",
    "targetKey",
    "benchmarkTarget",
    "sourceKey",
    "sourceName",
    "sourceMetric",
    "sourceUrl",
    "termOrPeriod",
    "unitOfWork",
    "observedApplications",
    "observedGrantedApplications",
    "observedPublicDisagreement",
    "requiredFields",
    "recommendedFields",
    "coderAction",
    "completionEvidence",
    "manuscriptUse",
}
REQUIRED_CERTIORARI_WORKQUEUE_COLUMNS = {
    "queueRank",
    "targetKey",
    "benchmarkTarget",
    "sourceKey",
    "sourceName",
    "sourceMetric",
    "sourceUrl",
    "periodOrSample",
    "unitOfWork",
    "observedSourceSignal",
    "requiredFields",
    "recommendedFields",
    "coderAction",
    "completionEvidence",
    "manuscriptUse",
}
REQUIRED_CERTIORARI_FIELD_READINESS_COLUMNS = {
    "fieldName",
    "fieldGroup",
    "type",
    "requiredFor",
    "validationUse",
    "simulatorMetric",
    "currentStatus",
    "currentEvidence",
    "sourceSlice",
    "nextCodingAction",
    "completionGate",
    "manuscriptUse",
}
REQUIRED_CERTIORARI_CLOSURE_PLAN_COLUMNS = {
    "planRank",
    "sourceKey",
    "sourceName",
    "sourceUrl",
    "targetKeys",
    "benchmarkTargets",
    "blockingReadinessRows",
    "currentBoundary",
    "seededFieldsAvailable",
    "requiredFieldsStillBlocking",
    "recommendedFieldsStillBlocking",
    "minimumViableExtraction",
    "completionGate",
    "publicationGate",
    "manuscriptUse",
}
REQUIRED_IMPLEMENTATION_COMPLIANCE_CLOSURE_PLAN_COLUMNS = {
    "planRank",
    "sourceSlice",
    "targetPathway",
    "benchmarkTargets",
    "simulatorMetrics",
    "blockingReadinessRows",
    "currentBoundary",
    "requiredSourceUnit",
    "requiredFields",
    "candidateSources",
    "minimumViableExtraction",
    "completionGate",
    "publicationGate",
    "manuscriptUse",
}
REQUIRED_IMPLEMENTATION_COMPLIANCE_WORKQUEUE_COLUMNS = {
    "queueRank",
    "sourceSlice",
    "schemaTarget",
    "targetPathway",
    "benchmarkTargets",
    "simulatorMetrics",
    "requiredSourceUnit",
    "requiredFields",
    "recommendedFields",
    "candidateSources",
    "coderAction",
    "completionEvidence",
    "denominatorGate",
    "manuscriptUse",
}
REQUIRED_ECTHR_EXECUTION_MONITORING_SUMMARY_COLUMNS = {
    "metricKey",
    "observedValue",
    "denominatorSpec",
    "sourceUrl",
    "validationUse",
    "manuscriptUse",
    "notes",
}
REQUIRED_BENCHMARK_SCHEMA_COLUMNS = {
    "fieldName",
    "fieldGroup",
    "type",
    "requiredFor",
    "candidateSourceEvidence",
    "simulatorMetric",
    "validationUse",
    "notes",
}
REQUIRED_CERTIORARI_RECONCILIATION_COLUMNS = {
    "metricKey",
    "sourceKey",
    "sourceName",
    "sourceUrl",
    "term",
    "sourceRecordId",
    "officialNumerator",
    "officialDenominator",
    "officialTotalDocketed",
    "officialValue",
    "normalizedObservedValue",
    "normalizedRawObservedValue",
    "absoluteDifference",
    "reconciliationStatus",
    "denominatorNote",
    "manuscriptUse",
}
REQUIRED_CERTIORARI_TERM_FLOW_EXTRACT_COLUMNS = {
    "sourceKey",
    "sourceName",
    "sourceUrl",
    "sourceFile",
    "sourceFileSha256",
    "sourceRecordId",
    "term",
    "statisticsAsOf",
    "statisticsCoverageNote",
    "statisticKey",
    "statisticSection",
    "statisticLabel",
    "caseCategory",
    "officialCount",
    "denominatorKey",
    "denominatorCount",
    "normalizedObservedValue",
    "benchmarkUse",
    "coderNotes",
}
REQUIRED_CERTIORARI_JOURNAL_DISPOSITION_SUMMARY_COLUMNS = {
    "metricKey",
    "sourceKey",
    "term",
    "observedValue",
    "comparisonValue",
    "reconciliationStatus",
    "manuscriptUse",
    "notes",
}
REQUIRED_CERTIORARI_JOURNAL_DOCKET_RETRIEVAL_WORKQUEUE_COLUMNS = {
    "workQueueRank",
    "sourceRecordId",
    "docketNumber",
    "paidOrIfp",
    "certDisposition",
    "dispositionDate",
    "lowerCourt",
    "staticDocketUrl",
    "failedFetchError",
    "retrievalPriority",
    "retrievalAction",
    "denominatorRole",
    "completionEvidence",
    "manuscriptUse",
}
REQUIRED_CERTIORARI_DOCKETED_COHORT_RECONCILIATION_COLUMNS = {
    "docketNumber",
    "paidOrIfp",
    "docketDisposition",
    "docketDispositionDate",
    "journalDispositions",
    "journalDispositionDates",
    "reconciliationStatus",
    "officialDocketUrl",
    "reviewNote",
}
REQUIRED_NORMALIZED_CALIBRATION_COLUMNS = {
    "sourceKey",
    "domain",
    "metric",
    "term",
    "numerator",
    "denominator",
    "value",
    "sourceUrl",
    "notes",
}
REQUIRED_CERTIORARI_MULTI_TERM_COLUMNS = {
    "metric",
    "termCount",
    "terms",
    "termValues",
    "firstTerm",
    "firstNumerator",
    "firstDenominator",
    "firstValue",
    "latestTerm",
    "latestNumerator",
    "latestDenominator",
    "latestValue",
    "absoluteChange",
    "rangeAcrossTerms",
    "pooledNumerator",
    "pooledDenominator",
    "pooledValue",
    "sourceKeys",
    "sourceUrl",
    "manuscriptUse",
    "notes",
}
REQUIRED_EMERGENCY_APPLICATION_EXTRACT_COLUMNS = {
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
}
REQUIRED_EMERGENCY_APPLICATION_RECONCILIATION_COLUMNS = {
    "sourceKey",
    "sourceName",
    "sourceUrl",
    "term",
    "sourceFile",
    "sourceFileSha256",
    "extractFilter",
    "extractedApplications",
    "summaryApplications",
    "applicationsDifference",
    "extractedGrantedApplications",
    "summaryGrantedApplications",
    "grantsDifference",
    "extractedPublicDisagreement",
    "summaryPublicDisagreement",
    "publicDisagreementDifference",
    "reconciliationStatus",
    "manuscriptUse",
    "remainingGap",
}
REQUIRED_EMERGENCY_FIELD_READINESS_COLUMNS = {
    "fieldName",
    "fieldGroup",
    "type",
    "requiredFor",
    "validationUse",
    "simulatorMetric",
    "currentStatus",
    "allApplicationRowsPopulated",
    "grantCodedRowsPopulated",
    "deniedOrNaRowsRequiringCoding",
    "currentEvidence",
    "nextCodingAction",
    "manuscriptUse",
}
REQUIRED_LOWER_COURT_PRECEDENT_TREATMENT_COLUMNS = [
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
REQUIRED_LOWER_COURT_PRECEDENT_TREATMENT_SUMMARY_COLUMNS = {
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
}
REQUIRED_LOWER_COURT_PRECEDENT_TREATMENT_CALIBRATION_COLUMNS = {
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
}
EXPECTED_LOWER_COURT_PRECEDENT_TERM_COUNTS = {
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
REQUIRED_ENVIRONMENTAL_EXPOSURE_COLUMNS = {
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
}
REQUIRED_ENVIRONMENTAL_SUMMARY_COLUMNS = {
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
}
REQUIRED_ENVIRONMENTAL_EVENT_EXTRA_COLUMNS = {
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
}
REQUIRED_ENVIRONMENTAL_AVAILABILITY_COLUMNS = {
    "dimension",
    "category",
    "events",
    "available",
    "unavailable",
    "availabilityRate",
}
REQUIRED_ENVIRONMENTAL_TREATMENT_REVIEW_COLUMNS = {
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
}
REQUIRED_GURGANUS_CLASSIFICATION_COLUMNS = {
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
}
REQUIRED_ENVIRONMENTAL_PRACTICAL_EXTRA_COLUMNS = {
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
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message: str) -> None:
    print(f"Paper artifact verification failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_manifest(path: Path) -> None:
    if not path.exists():
        fail(f"missing manifest {path.relative_to(ROOT)}")
    data = json.loads(path.read_text())
    command = data.get("javaCommand", "")
    manifest_text = path.read_text()
    local_home_marker = "/" + "Users" + "/"
    if local_home_marker in manifest_text:
        fail(f"{path.name} contains a local absolute path")
    if path.name in {"constitutional-review-campaign-v2-manifest.json", "calibration-baseline-manifest.json"}:
        if "--legislative-input" not in command:
            fail(f"{path.name} was not generated with the paper legislative input contract")
        if PAPER_LEGISLATIVE_INPUT not in command:
            fail(f"{path.name} was not generated with the frozen paper legislative fixture")
    for artifact in data.get("artifacts", []):
        artifact_path = ROOT / artifact["path"]
        if not artifact_path.exists():
            fail(f"missing artifact {artifact['path']} listed by {path.name}")
        actual = sha256(artifact_path)
        expected = artifact["sha256"]
        if actual != expected:
            fail(f"{artifact['path']} hash {actual} does not match manifest {expected}")


def check_campaign_schema() -> None:
    if not CAMPAIGN_CSV.exists():
        fail(f"missing campaign CSV {CAMPAIGN_CSV.relative_to(ROOT)}")
    with CAMPAIGN_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        missing = REQUIRED_CAMPAIGN_COLUMNS - set(reader.fieldnames or [])
    if missing:
        fail("campaign CSV is missing pipeline/downstream columns: " + ", ".join(sorted(missing)))


def check_csv_schema(path: Path, required: set[str], label: str) -> None:
    if not path.exists():
        fail(f"missing {label} CSV {path.relative_to(ROOT)}")
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        missing = required - set(reader.fieldnames or [])
    if missing:
        fail(f"{label} CSV is missing columns: " + ", ".join(sorted(missing)))


def check_certiorari_benchmark_readiness() -> None:
    with BENCHMARK_READINESS_CSV.open(newline="") as handle:
        rows = {
            row["simulatorMetric"]: row
            for row in csv.DictReader(handle)
            if row.get("pathway") == "certiorari"
        }
    expected_evidence = {
        "specialistCounselRate": "same-row petition representation coding for specialist or former-clerk counsel, represented side, disposition, and denominator rule",
        "genuineLowerCourtSplitRate": "same-row alleged and genuine split, split depth, issue, vehicle quality, disposition, and denominator rule",
        "certiorariAdmissionRate": "constitutional-review or issue-coded subset within the closed docketed cohort, with disposition and grant or GVR",
        "cvsgRequestRate": "additional docketed terms using the same closed enumeration and CVSG coding rule",
        "paidCfrRequestRate": "additional docketed terms using the same closed enumeration and response or CFR coding rule",
        "ifpCfrRequestRate": "additional docketed terms using the same closed enumeration and response or CFR coding rule",
        "paidCertPetitionShare": "additional docketed terms using the same closed enumeration and paid or IFP intake coding rule",
        "ifpCertPetitionShare": "additional docketed terms using the same closed enumeration and paid or IFP intake coding rule",
    }
    for metric, evidence in expected_evidence.items():
        row = rows.get(metric)
        if row is None:
            fail(f"benchmark readiness is missing certiorari metric {metric}")
        if row.get("requiredEvidence") != evidence:
            fail(f"benchmark readiness has stale or incorrect required evidence for {metric}")


def check_schema_template(schema_path: Path, template_path: Path, label: str) -> None:
    if not template_path.exists():
        fail(f"missing {label} template {template_path.relative_to(ROOT)}")
    with schema_path.open(newline="") as handle:
        schema_fields = [row["fieldName"] for row in csv.DictReader(handle)]
    with template_path.open(newline="") as handle:
        template_fields = csv.DictReader(handle).fieldnames or []
    if schema_fields != template_fields:
        fail(f"{label} template columns do not match schema fieldName order")


def check_emergency_grant_linkage_workqueue() -> None:
    if not EMERGENCY_GRANT_LINKAGE_WORKQUEUE_CSV.exists():
        fail(f"missing emergency grant linkage work queue {EMERGENCY_GRANT_LINKAGE_WORKQUEUE_CSV.relative_to(ROOT)}")
    with EMERGENCY_LINKAGE_SCHEMA_CSV.open(newline="") as handle:
        schema_fields = [row["fieldName"] for row in csv.DictReader(handle)]
    with EMERGENCY_GRANT_LINKAGE_WORKQUEUE_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if (reader.fieldnames or []) != schema_fields:
            fail("emergency grant linkage work queue columns do not match emergency linkage schema")
        linkage_rows = list(reader)
    with EMERGENCY_APPLICATION_EXTRACT_CSV.open(newline="") as handle:
        extract_rows = [row for row in csv.DictReader(handle) if row.get("reliefGranted") == "1"]
    if len(linkage_rows) != len(extract_rows):
        fail(
            "emergency grant linkage work queue row count does not match granted emergency extract rows: "
            f"{len(linkage_rows)} != {len(extract_rows)}"
        )
    extract_ids = {row["sourceRecordId"] for row in extract_rows}
    missing_ids = [
        row.get("sourceRecordId", "")
        for row in linkage_rows
        if row.get("sourceRecordId") not in extract_ids
    ]
    if missing_ids:
        fail("emergency grant linkage work queue has unknown source rows: " + ", ".join(missing_ids[:10]))
    bad_rows = [
        row.get("sourceRecordId", "")
        for row in linkage_rows
        if (
            row.get("reliefGranted") != "1"
            or not row.get("docketNumber")
            or not row.get("dispositionDate")
            or row.get("statusQuoEffect") != "uncoded"
            or row.get("meritsFollowThroughCategory") != "uncoded"
            or row.get("downstreamPolicyStatus") != "uncoded"
        )
    ]
    if bad_rows:
        fail("emergency grant linkage work queue rows require review: " + ", ".join(bad_rows[:10]))


def check_emergency_denied_linkage_workqueue() -> None:
    if not EMERGENCY_DENIED_LINKAGE_WORKQUEUE_CSV.exists():
        fail(f"missing emergency denied linkage work queue {EMERGENCY_DENIED_LINKAGE_WORKQUEUE_CSV.relative_to(ROOT)}")
    with EMERGENCY_LINKAGE_SCHEMA_CSV.open(newline="") as handle:
        schema_fields = [row["fieldName"] for row in csv.DictReader(handle)]
    with EMERGENCY_DENIED_LINKAGE_WORKQUEUE_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if (reader.fieldnames or []) != schema_fields:
            fail("emergency denied linkage work queue columns do not match emergency linkage schema")
        linkage_rows = list(reader)
    with EMERGENCY_APPLICATION_EXTRACT_CSV.open(newline="") as handle:
        extract_rows = [row for row in csv.DictReader(handle) if row.get("reliefGranted") != "1"]
    if len(extract_rows) != 210:
        fail(f"emergency extract denied/NA source row count changed unexpectedly: {len(extract_rows)} != 210")
    if len(linkage_rows) != len(extract_rows):
        fail(
            "emergency denied linkage work queue row count does not match denied/NA emergency extract rows: "
            f"{len(linkage_rows)} != {len(extract_rows)}"
        )
    extract_ids = {row["sourceRecordId"] for row in extract_rows}
    queue_ids = {row.get("sourceRecordId", "") for row in linkage_rows}
    missing_ids = sorted(extract_ids - queue_ids)
    extra_ids = sorted(queue_ids - extract_ids)
    if missing_ids:
        fail("emergency denied linkage work queue is missing source rows: " + ", ".join(missing_ids[:10]))
    if extra_ids:
        fail("emergency denied linkage work queue has unknown source rows: " + ", ".join(extra_ids[:10]))
    denied_rows = sum(1 for row in linkage_rows if row.get("reliefGranted") == "0")
    nonbinary_rows = sum(1 for row in linkage_rows if row.get("reliefGranted") not in {"0", "1"})
    if denied_rows != 200 or nonbinary_rows != 10:
        fail(
            "emergency denied linkage work queue does not preserve denied/non-binary split: "
            f"{denied_rows} denied and {nonbinary_rows} non-binary rows"
        )
    bad_rows = [
        row.get("sourceRecordId", "")
        for row in linkage_rows
        if (
            row.get("reliefGranted") == "1"
            or not row.get("docketNumber")
            or not row.get("dispositionDate")
            or row.get("statusQuoEffect") != "uncoded"
            or row.get("meritsFollowThroughCategory") != "uncoded"
            or row.get("downstreamPolicyStatus") != "uncoded"
            or "not validation evidence" not in row.get("coderNotes", "")
        )
    ]
    if bad_rows:
        fail("emergency denied linkage work queue rows require review: " + ", ".join(bad_rows[:10]))


def check_emergency_linkage_coded_rows() -> None:
    if not EMERGENCY_LINKAGE_CODED_CSV.exists():
        fail(f"missing emergency linkage coded slice {EMERGENCY_LINKAGE_CODED_CSV.relative_to(ROOT)}")
    with EMERGENCY_LINKAGE_SCHEMA_CSV.open(newline="") as handle:
        schema_fields = [row["fieldName"] for row in csv.DictReader(handle)]
    with EMERGENCY_GRANT_LINKAGE_WORKQUEUE_CSV.open(newline="") as handle:
        queue_rows = {row["sourceRecordId"]: row for row in csv.DictReader(handle)}
    with EMERGENCY_LINKAGE_CODED_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if (reader.fieldnames or []) != schema_fields:
            fail("emergency linkage coded slice columns do not match emergency linkage schema")
        coded_rows = list(reader)
    if not coded_rows:
        fail("emergency linkage coded slice has no coded rows")
    binary_fields = {
        "responseRequested",
        "fullCourtReferral",
        "reliefGranted",
        "reasoningPresent",
        "publicDisagreement",
        "repeatFilingFlag",
    }
    required_fields = {
        "sourceKey",
        "sourceRecordId",
        "sourceUrl",
        "term",
        "docketNumber",
        "applicationDate",
        "applicationClass",
        "responseRequested",
        "fullCourtReferral",
        "dispositionDate",
        "reliefGranted",
        "dispositionType",
        "reasoningPresent",
        "publicDisagreement",
        "statusQuoEffect",
        "meritsFollowThroughCategory",
        "downstreamPolicyStatus",
        "repeatFilingFlag",
        "coderNotes",
    }
    bad_rows: list[str] = []
    for row in coded_rows:
        source_id = row.get("sourceRecordId", "")
        queue_row = queue_rows.get(source_id)
        if queue_row is None:
            bad_rows.append(f"{source_id}: missing from grant linkage queue")
            continue
        if row.get("term") != queue_row.get("term") or row.get("docketNumber") != queue_row.get("docketNumber"):
            bad_rows.append(f"{source_id}: term or docket changed from grant linkage queue")
        if not row.get("sourceUrl", "").startswith("https://www.supremecourt.gov/"):
            bad_rows.append(f"{source_id}: sourceUrl is not an official Supreme Court URL")
        for field in required_fields:
            if not row.get(field, "").strip():
                bad_rows.append(f"{source_id}: missing {field}")
        for field in binary_fields:
            if row.get(field) not in {"0", "1"}:
                bad_rows.append(f"{source_id}: {field} must be 0 or 1")
        for field in {"statusQuoEffect", "meritsFollowThroughCategory", "downstreamPolicyStatus"}:
            if row.get(field) == "uncoded":
                bad_rows.append(f"{source_id}: {field} is still uncoded")
        if row.get("linkedMeritsDocket") and not row.get("linkedMeritsDecisionDate"):
            bad_rows.append(f"{source_id}: linked merits docket lacks decision date")
    if bad_rows:
        fail("emergency linkage coded slice rows require review: " + "; ".join(bad_rows[:10]))


def check_emergency_denied_linkage_coded_rows() -> None:
    if not EMERGENCY_DENIED_LINKAGE_CODED_CSV.exists():
        fail(f"missing emergency denied/NA coded slice {EMERGENCY_DENIED_LINKAGE_CODED_CSV.relative_to(ROOT)}")
    if not EMERGENCY_DENIED_LINKAGE_CODED_MANIFEST.exists():
        fail(f"missing emergency denied/NA coded manifest {EMERGENCY_DENIED_LINKAGE_CODED_MANIFEST.relative_to(ROOT)}")
    with EMERGENCY_LINKAGE_SCHEMA_CSV.open(newline="") as handle:
        schema_fields = [row["fieldName"] for row in csv.DictReader(handle)]
    with EMERGENCY_DENIED_LINKAGE_WORKQUEUE_CSV.open(newline="") as handle:
        queue_rows = {row["sourceRecordId"]: row for row in csv.DictReader(handle)}
    with EMERGENCY_DENIED_LINKAGE_CODED_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if (reader.fieldnames or []) != schema_fields:
            fail("emergency denied/NA coded slice columns do not match emergency linkage schema")
        coded_rows = list(reader)
    if len(coded_rows) != 210:
        fail(f"emergency denied/NA coded slice row count changed unexpectedly: {len(coded_rows)} != 210")
    coded_ids = {row.get("sourceRecordId", "") for row in coded_rows}
    queue_ids = set(queue_rows)
    if coded_ids != queue_ids:
        missing = sorted(queue_ids - coded_ids)
        extra = sorted(coded_ids - queue_ids)
        fail(
            "emergency denied/NA coded slice does not match denied queue IDs: "
            f"missing={missing[:5]} extra={extra[:5]}"
        )
    manifest = json.loads(EMERGENCY_DENIED_LINKAGE_CODED_MANIFEST.read_text())
    if manifest.get("rowCount") != len(coded_rows):
        fail("emergency denied/NA coded manifest rowCount does not match extract")
    if manifest.get("sourceQueueRows") != len(queue_rows):
        fail("emergency denied/NA coded manifest sourceQueueRows does not match queue")
    if manifest.get("failedFetchCount") != 0:
        fail("emergency denied/NA coded manifest reports failed official docket fetches")
    if manifest.get("sha256") != sha256(EMERGENCY_DENIED_LINKAGE_CODED_CSV):
        fail("emergency denied/NA coded manifest hash does not match extract")
    if manifest.get("manualLinkedMeritsRows") != 1:
        fail("emergency denied/NA coded manifest does not record the linked 24A164 merits row")
    if manifest.get("linkedMeritsRefreshDate") != "2026-07-26":
        fail("emergency denied/NA coded manifest linked-merits refresh date changed unexpectedly")
    if "not external implementation validation" not in manifest.get("notes", ""):
        fail("emergency denied/NA coded manifest does not preserve implementation-validation boundary")
    binary_fields = {
        "responseRequested",
        "fullCourtReferral",
        "reasoningPresent",
        "publicDisagreement",
        "repeatFilingFlag",
    }
    required_fields = {
        "sourceKey",
        "sourceRecordId",
        "sourceUrl",
        "term",
        "docketNumber",
        "applicationDate",
        "applicationClass",
        "responseRequested",
        "fullCourtReferral",
        "dispositionDate",
        "reliefGranted",
        "dispositionType",
        "reasoningPresent",
        "publicDisagreement",
        "statusQuoEffect",
        "meritsFollowThroughCategory",
        "downstreamPolicyStatus",
        "repeatFilingFlag",
        "coderNotes",
    }
    bad_rows: list[str] = []
    for row in coded_rows:
        source_id = row.get("sourceRecordId", "")
        queue_row = queue_rows.get(source_id, {})
        if row.get("term") != queue_row.get("term") or row.get("docketNumber") != queue_row.get("docketNumber"):
            bad_rows.append(f"{source_id}: term or docket changed from denied queue")
        if row.get("sourceKey") != "scotus-docket-plus-shadow-docket-v3-0":
            bad_rows.append(f"{source_id}: unexpected sourceKey")
        if not row.get("sourceUrl", "").startswith("https://www.supremecourt.gov/docket/docketfiles/html/public/"):
            bad_rows.append(f"{source_id}: sourceUrl is not an official Supreme Court docket URL")
        if row.get("reliefGranted") == "1":
            bad_rows.append(f"{source_id}: denied/NA coded slice contains a granted row")
        for field in required_fields:
            if not row.get(field, "").strip():
                bad_rows.append(f"{source_id}: missing {field}")
        for field in binary_fields:
            if row.get(field) not in {"0", "1"}:
                bad_rows.append(f"{source_id}: {field} must be 0 or 1")
        for field in {"statusQuoEffect", "meritsFollowThroughCategory", "downstreamPolicyStatus"}:
            if row.get(field) == "uncoded":
                bad_rows.append(f"{source_id}: {field} is still uncoded")
        if "review_required" in row.get("meritsFollowThroughCategory", ""):
            bad_rows.append(f"{source_id}: merits follow-through still requires manual review")
        if "not external implementation validation" not in row.get("coderNotes", ""):
            bad_rows.append(f"{source_id}: coderNotes may overclaim implementation validation")
    if bad_rows:
        fail("emergency denied/NA coded slice rows require review: " + "; ".join(bad_rows[:10]))
    denied_rows = sum(1 for row in coded_rows if row.get("reliefGranted") == "0")
    nonbinary_rows = sum(1 for row in coded_rows if row.get("reliefGranted") not in {"0", "1"})
    if denied_rows != 200 or nonbinary_rows != 10:
        fail(
            "emergency denied/NA coded slice does not preserve denied/non-binary split: "
            f"{denied_rows} denied and {nonbinary_rows} non-binary rows"
        )
    if sum(1 for row in coded_rows if row.get("responseRequested") == "1") < 50:
        fail("emergency denied/NA coded slice is missing expected response-request signal")
    if sum(1 for row in coded_rows if row.get("reasoningPresent") == "1") < 20:
        fail("emergency denied/NA coded slice is missing expected reason-visibility signal")


def check_emergency_denied_linkage_coded_summary() -> None:
    if not EMERGENCY_DENIED_LINKAGE_CODED_SUMMARY_CSV.exists():
        fail(f"missing emergency denied/NA coded summary {EMERGENCY_DENIED_LINKAGE_CODED_SUMMARY_CSV.relative_to(ROOT)}")
    with EMERGENCY_DENIED_LINKAGE_CODED_CSV.open(newline="") as handle:
        extract_rows = list(csv.DictReader(handle))
    with EMERGENCY_DENIED_LINKAGE_CODED_SUMMARY_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        missing_columns = REQUIRED_ECTHR_EXECUTION_MONITORING_SUMMARY_COLUMNS - set(reader.fieldnames or [])
        if missing_columns:
            fail("emergency denied/NA coded summary is missing columns: " + ", ".join(sorted(missing_columns)))
        rows = list(reader)
    by_metric = {row["metricKey"]: row for row in rows}
    required_metrics = {
        "emergencyDeniedNaDocketDetailRows",
        "emergencyDeniedNaDocketApplicationDateRows",
        "emergencyDeniedNaDocketResponseRequestedRows",
        "emergencyDeniedNaDocketReasoningRows",
        "emergencyDeniedNaDocketRepeatFilingRows",
        "emergencyDeniedNaDocketReviewNeededRows",
    }
    missing_metrics = required_metrics - set(by_metric)
    if missing_metrics:
        fail("emergency denied/NA coded summary missing metrics: " + ", ".join(sorted(missing_metrics)))
    if int(by_metric["emergencyDeniedNaDocketDetailRows"]["observedValue"]) != len(extract_rows):
        fail("emergency denied/NA coded summary row count does not match extract")
    if int(by_metric["emergencyDeniedNaDocketApplicationDateRows"]["observedValue"]) != len(extract_rows):
        fail("emergency denied/NA coded summary does not report all application dates")
    review_needed = sum(
        1 for row in extract_rows
        if "review_required" in row.get("meritsFollowThroughCategory", "")
    )
    if int(by_metric["emergencyDeniedNaDocketReviewNeededRows"]["observedValue"]) != review_needed:
        fail("emergency denied/NA coded summary review-needed count does not match extract")
    if review_needed:
        fail("emergency denied/NA coded slice still has unresolved merits-follow-through rows")
    bad_use = [
        row["metricKey"]
        for row in rows
        if "not external implementation validation" not in row.get("manuscriptUse", "")
    ]
    if bad_use:
        fail("emergency denied/NA coded summary may overclaim: " + ", ".join(bad_use))


def check_emergency_field_readiness() -> None:
    if not EMERGENCY_FIELD_READINESS_CSV.exists():
        fail(f"missing emergency field-readiness CSV {EMERGENCY_FIELD_READINESS_CSV.relative_to(ROOT)}")
    with EMERGENCY_LINKAGE_SCHEMA_CSV.open(newline="") as handle:
        schema_fields = [row["fieldName"] for row in csv.DictReader(handle)]
    with EMERGENCY_FIELD_READINESS_CSV.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    readiness_fields = [row["fieldName"] for row in rows]
    if readiness_fields != schema_fields:
        fail("emergency field-readiness rows do not match linkage schema field order")

    statuses = {row.get("currentStatus", "") for row in rows}
    required_statuses = {
        "all_application_extract",
        "all_application_docket_linkage_coded",
        "all_application_docket_linkage_partial",
        "all_application_docket_linkage_conditionally_complete",
    }
    missing_statuses = required_statuses - statuses
    if missing_statuses:
        fail("emergency field-readiness matrix is missing statuses: " + ", ".join(sorted(missing_statuses)))

    by_field = {row["fieldName"]: row for row in rows}
    all_application_fields = {
        "sourceKey",
        "sourceRecordId",
        "sourceUrl",
        "term",
        "docketNumber",
        "applicationClass",
        "applicantType",
        "respondentType",
        "reliefRequested",
        "lowerCourt",
        "fullCourtReferral",
        "dispositionDate",
        "reliefGranted",
        "dispositionType",
        "publicDisagreement",
        "coderNotes",
    }
    bad_all_application = [
        field
        for field in sorted(all_application_fields)
        if by_field.get(field, {}).get("currentStatus") != "all_application_extract"
    ]
    if bad_all_application:
        fail("emergency field-readiness matrix does not mark all-application extract fields: " + ", ".join(bad_all_application))

    grant_only_fields = {
        "applicationDate",
        "responseRequested",
        "reasoningPresent",
        "statusQuoEffect",
        "meritsFollowThroughCategory",
        "downstreamPolicyStatus",
        "repeatFilingFlag",
    }
    bad_grant_only = [
        field
        for field in sorted(grant_only_fields)
        if by_field.get(field, {}).get("currentStatus") != "all_application_docket_linkage_coded"
    ]
    if bad_grant_only:
        fail("emergency field-readiness matrix does not mark all-application docket-coded fields: " + ", ".join(bad_grant_only))

    for field in grant_only_fields:
        row = by_field[field]
        if row.get("deniedOrNaRowsRequiringCoding") != "0":
            fail(f"emergency field-readiness {field} does not close the denied/NA docket-coding gap")
        if "not external implementation validation" not in row.get("manuscriptUse", ""):
            fail(f"emergency field-readiness {field} manuscript-use text may overclaim")

    conditional_linkage_fields = {
        "linkedMeritsDocket",
        "linkedMeritsFiledDate",
        "linkedMeritsDecisionDate",
        "linkedMeritsOutcome",
    }
    bad_conditional = [
        field
        for field in sorted(conditional_linkage_fields)
        if by_field.get(field, {}).get("currentStatus")
        != "all_application_docket_linkage_conditionally_complete"
    ]
    if bad_conditional:
        fail(
            "emergency field-readiness matrix does not mark conditionally complete merits fields: "
            + ", ".join(bad_conditional)
        )
    for field in conditional_linkage_fields:
        row = by_field[field]
        if row.get("deniedOrNaRowsRequiringCoding") != "0":
            fail(f"emergency field-readiness {field} retains a denied/NA coding gap")
        if "not external implementation validation" not in row.get("manuscriptUse", ""):
            fail(f"emergency field-readiness {field} manuscript-use text may overclaim")


def check_reconciliation_status(path: Path, label: str) -> None:
    with path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        fail(f"{label} CSV has no rows")
    bad = [
        row.get("metricKey", "")
        for row in rows
        if row.get("reconciliationStatus") != "matches_official_source"
    ]
    if bad:
        fail(f"{label} rows require review: " + ", ".join(bad))


def check_status_values(path: Path, label: str, expected_status: str) -> None:
    with path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        fail(f"{label} CSV has no rows")
    bad = [
        row.get("term") or row.get("sourceRecordId") or row.get("metricKey", "")
        for row in rows
        if row.get("reconciliationStatus") != expected_status
    ]
    if bad:
        fail(f"{label} rows require review: " + ", ".join(bad))


def check_certiorari_field_readiness() -> None:
    if not CERTIORARI_FIELD_READINESS_CSV.exists():
        fail(f"missing certiorari field-readiness CSV {CERTIORARI_FIELD_READINESS_CSV.relative_to(ROOT)}")
    with CERTIORARI_COHORT_SCHEMA_CSV.open(newline="") as handle:
        schema_fields = [row["fieldName"] for row in csv.DictReader(handle)]
    with CERTIORARI_FIELD_READINESS_CSV.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    readiness_fields = [row["fieldName"] for row in rows]
    if readiness_fields != schema_fields:
        fail("certiorari field-readiness rows do not match cohort schema field order")
    statuses = {row.get("currentStatus", "") for row in rows}
    required_statuses = {
        "closed_docketed_cohort_complete",
        "closed_docketed_cohort_partial",
        "required_not_row_coded",
        "recommended_not_row_coded",
    }
    missing_statuses = required_statuses - statuses
    if missing_statuses:
        fail("certiorari field-readiness matrix is missing statuses: " + ", ".join(sorted(missing_statuses)))
    unexpected_statuses = statuses - required_statuses
    if unexpected_statuses:
        fail(
            "certiorari field-readiness matrix retains superseded statuses: "
            + ", ".join(sorted(unexpected_statuses))
        )
    by_field = {row["fieldName"]: row for row in rows}
    complete_fields = {
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
    bad_complete_fields = [
        field
        for field in sorted(complete_fields)
        if by_field.get(field, {}).get("currentStatus") != "closed_docketed_cohort_complete"
    ]
    if bad_complete_fields:
        fail(
            "certiorari field-readiness matrix does not mark closed-cohort fields complete: "
            + ", ".join(bad_complete_fields)
        )
    for field in complete_fields:
        manuscript_use = by_field[field].get("manuscriptUse", "")
        if "direct closed docketed-intake evidence" not in manuscript_use:
            fail(f"certiorari field-readiness closed-cohort row lacks direct-evidence wording for {field}")
        if "undocketed submissions" not in manuscript_use:
            fail(f"certiorari field-readiness closed-cohort row omits undocketed boundary for {field}")

    partial_fields = {
        "petitionerType",
        "respondentType",
        "meritsDecisionDate",
        "meritsOutcome",
        "reversalOrVacatur",
    }
    bad_partial_fields = [
        field
        for field in sorted(partial_fields)
        if by_field.get(field, {}).get("currentStatus") != "closed_docketed_cohort_partial"
    ]
    if bad_partial_fields:
        fail(
            "certiorari field-readiness matrix does not preserve partial cohort fields: "
            + ", ".join(bad_partial_fields)
        )
    for field in partial_fields:
        if "not complete field-level validation" not in by_field[field].get("manuscriptUse", ""):
            fail(f"certiorari field-readiness partial row may overclaim for {field}")

    still_uncoded_fields = {
        "issueArea": "recommended_not_row_coded",
        "specialistCounselFlag": "required_not_row_coded",
        "formerClerkCounselFlag": "recommended_not_row_coded",
        "allegedSplitFlag": "required_not_row_coded",
        "genuineSplitFlag": "required_not_row_coded",
        "splitDepth": "recommended_not_row_coded",
        "vehicleQualityObjection": "recommended_not_row_coded",
    }
    wrongly_upgraded = [
        field
        for field, expected_status in sorted(still_uncoded_fields.items())
        if by_field.get(field, {}).get("currentStatus") != expected_status
    ]
    if wrongly_upgraded:
        fail(
            "certiorari field-readiness matrix upgrades still-uncoded issue/counsel/split fields: "
            + ", ".join(wrongly_upgraded)
        )
    if len(complete_fields | partial_fields | set(still_uncoded_fields)) != len(schema_fields):
        fail("certiorari field-readiness verifier does not account for every cohort schema field")

    overclaiming_rows = [
        row["fieldName"]
        for row in rows
        if (
            row.get("currentStatus") in {"required_not_row_coded", "recommended_not_row_coded"}
            and "no validation upgrade until" not in row.get("manuscriptUse", "").lower()
        )
    ]
    if overclaiming_rows:
        fail("certiorari field-readiness uncoded rows may overclaim: " + ", ".join(overclaiming_rows))


def check_certiorari_closure_plan() -> None:
    if not CERTIORARI_COHORT_CLOSURE_PLAN_CSV.exists():
        fail(f"missing certiorari closure plan CSV {CERTIORARI_COHORT_CLOSURE_PLAN_CSV.relative_to(ROOT)}")
    with CERTIORARI_COHORT_CLOSURE_PLAN_CSV.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        fail("certiorari closure plan has no rows")
    by_source = {row["sourceKey"]: row for row in rows}
    expected_sources = {
        "scotus-certiorari-docketed-cohorts-ot2023-ot2024",
        "thompson-wachtell-certiorari",
        "feldman-kappner-elite-counsel",
        "lazarus-ot2005-cert-stage-amicus",
        "beim-rader-conflicts",
    }
    missing_sources = expected_sources - set(by_source)
    if missing_sources:
        fail("certiorari closure plan is missing source slices: " + ", ".join(sorted(missing_sources)))

    paired = by_source["scotus-certiorari-docketed-cohorts-ot2023-ot2024"]
    for phrase in (
        "close 8,076 paid/IFP dockets",
        "7,716 certiorari petitions",
        "Three OT2024 petitions remain pending",
        "four same-cutoff-date dockets",
        "official docket detail for 115 granted/GVR rows",
        "reachable public docket detail for 3947 Journal disposition rows",
    ):
        if phrase not in paired.get("currentBoundary", ""):
            fail(f"certiorari closure plan paired-cohort row omits: {phrase}")
    if paired.get("requiredFieldsStillBlocking") != "none":
        fail("certiorari closure plan paired-cohort row retains required docket-visible blockers")
    if "paired OT2023-OT2024 docketed-intake denominators" not in paired.get("publicationGate", ""):
        fail("certiorari closure plan paired-cohort row does not mark the bounded gate met")
    for boundary in ("undocketed-submission", "counsel", "split-quality"):
        if boundary not in paired.get("manuscriptUse", ""):
            fail(f"certiorari closure plan paired-cohort manuscript use omits {boundary}")

    thompson = by_source["thompson-wachtell-certiorari"]
    for target in ("cert_cfr_response", "cert_cvsg_signal"):
        if target not in thompson.get("targetKeys", ""):
            fail(f"certiorari closure plan Thompson-Wachtell row is missing target {target}")
    if "respondentType" not in thompson.get("requiredFieldsStillBlocking", ""):
        fail("certiorari closure plan Thompson-Wachtell row is missing respondent-type blocker")
    for field in ("responseRequestedByCourt", "cvsgRequested"):
        if field in thompson.get("requiredFieldsStillBlocking", ""):
            fail(f"certiorari closure plan improperly keeps closed-cohort field blocking: {field}")

    for source_key, required_text in {
        "feldman-kappner-elite-counsel": "filtered-sample",
        "lazarus-ot2005-cert-stage-amicus": "non-SG denominator",
        "beim-rader-conflicts": "same petition or conflict sample",
    }.items():
        row = by_source[source_key]
        if required_text not in row.get("publicationGate", ""):
            fail(f"certiorari closure plan {source_key} publication gate does not preserve denominator limits")

    overclaiming_rows = [
        row["sourceKey"]
        for row in rows
        if (
            row["sourceKey"] != "scotus-certiorari-docketed-cohorts-ot2023-ot2024"
            and "No validation upgrade until" not in row.get("manuscriptUse", "")
        )
    ]
    if overclaiming_rows:
        fail("certiorari closure plan manuscript-use text may overclaim: " + ", ".join(overclaiming_rows))


def check_implementation_compliance_closure_plan() -> None:
    if not IMPLEMENTATION_COMPLIANCE_CLOSURE_PLAN_CSV.exists():
        fail(
            "missing implementation/compliance closure plan CSV "
            f"{IMPLEMENTATION_COMPLIANCE_CLOSURE_PLAN_CSV.relative_to(ROOT)}"
        )
    with IMPLEMENTATION_COMPLIANCE_CLOSURE_PLAN_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = set(reader.fieldnames or [])
        rows = list(reader)
    if fieldnames != REQUIRED_IMPLEMENTATION_COMPLIANCE_CLOSURE_PLAN_COLUMNS:
        missing = REQUIRED_IMPLEMENTATION_COMPLIANCE_CLOSURE_PLAN_COLUMNS - fieldnames
        extra = fieldnames - REQUIRED_IMPLEMENTATION_COMPLIANCE_CLOSURE_PLAN_COLUMNS
        problems = []
        if missing:
            problems.append("missing " + ", ".join(sorted(missing)))
        if extra:
            problems.append("extra " + ", ".join(sorted(extra)))
        fail("implementation/compliance closure plan column mismatch: " + "; ".join(problems))
    if len(rows) != 4:
        fail("implementation/compliance closure plan must contain exactly four source slices")

    by_slice = {row["sourceSlice"]: row for row in rows}
    expected_slices = {
        "lower-court-doctrinal-uptake",
        "implementation-resistance",
        "monitoring-capacity",
        "emergency-downstream-implementation",
    }
    missing_slices = expected_slices - set(by_slice)
    if missing_slices:
        fail("implementation/compliance closure plan is missing source slices: " + ", ".join(sorted(missing_slices)))

    all_metrics = "; ".join(row["simulatorMetrics"] for row in rows)
    for metric in (
        "lowerCourtCompliance",
        "lowerCourtResistanceRisk",
        "interbranchCompliance",
        "governmentNoncomplianceRate",
        "emergencyDownstreamEffect",
    ):
        if metric not in all_metrics:
            fail(f"implementation/compliance closure plan is missing metric {metric}")

    for row in rows:
        if row["sourceSlice"] == "monitoring-capacity":
            if "bounded monitoring-capacity evidence" not in row.get("manuscriptUse", ""):
                fail("implementation/compliance monitoring row must be bounded monitoring evidence")
            if "broader execution-throughput claims" not in row.get("publicationGate", ""):
                fail("implementation/compliance monitoring row must keep broader throughput claims gated")
        elif row["sourceSlice"] == "lower-court-doctrinal-uptake":
            if "bounded aggregate doctrinal-uptake" not in row.get("manuscriptUse", ""):
                fail("implementation/compliance uptake row must preserve its bounded aggregate use")
            if "No lowerCourtCompliance validation upgrade" not in row.get("publicationGate", ""):
                fail("implementation/compliance uptake row must keep general validation gated")
        elif row["sourceSlice"] == "implementation-resistance":
            if "bounded purposive environmental practical-implementation evidence" not in row.get("manuscriptUse", ""):
                fail("implementation/compliance resistance row must preserve bounded practical evidence")
            if "No governmentNoncomplianceRate" not in row.get("publicationGate", ""):
                fail("implementation/compliance resistance row must keep general noncompliance gated")
        else:
            if "No validation upgrade" not in row.get("publicationGate", ""):
                fail(
                    "implementation/compliance closure plan publication gate may overclaim: "
                    + row["sourceSlice"]
                )
            if "not validation evidence" not in row.get("manuscriptUse", ""):
                fail(
                    "implementation/compliance closure plan manuscript-use text may overclaim: "
                    + row["sourceSlice"]
                )
        for field in (
            "blockingReadinessRows",
            "currentBoundary",
            "requiredSourceUnit",
            "requiredFields",
            "candidateSources",
            "minimumViableExtraction",
            "completionGate",
        ):
            if not row.get(field, "").strip():
                fail(
                    "implementation/compliance closure plan has empty "
                    f"{field} for {row['sourceSlice']}"
                )

    uptake = by_slice["lower-court-doctrinal-uptake"]
    if "aggregate benchmark covers 876 Supreme Court precedents" not in uptake["currentBoundary"]:
        fail("implementation/compliance lower-court uptake row omits the completed aggregate benchmark")
    if (
        "191 deduplicated published citation-linked federal opinion documents" not in uptake["currentBoundary"]
        or "not an empirical exposure" not in uptake["currentBoundary"]
        or "pending expert review" not in uptake["currentBoundary"]
    ):
        fail("implementation/compliance lower-court uptake row does not preserve the bounded event-level evidence")
    if "bounded environmental acquisition snapshot completed" not in uptake["minimumViableExtraction"]:
        fail("implementation/compliance lower-court uptake row does not record the bounded snapshot")
    if "followedOrDistinguished" not in uptake["requiredFields"]:
        fail("implementation/compliance lower-court uptake row is missing treatment coding fields")

    resistance = by_slice["implementation-resistance"]
    if "resistanceCategory" not in resistance["requiredFields"] or "delayDays" not in resistance["requiredFields"]:
        fail("implementation/compliance resistance row is missing resistance and delay fields")
    if (
        "5 agency implementation episodes" not in resistance["currentBoundary"]
        or "no observed noncompliant episode" not in resistance["currentBoundary"]
    ):
        fail("implementation/compliance resistance row omits bounded practical cohort evidence")
    if "broader cohort includes noncompliant outcomes" not in resistance["publicationGate"]:
        fail("implementation/compliance resistance row does not require broader outcome evidence")

    monitoring = by_slice["monitoring-capacity"]
    if "monitoringBody" not in monitoring["requiredFields"]:
        fail("implementation/compliance monitoring row is missing monitoring-body fields")
    if (
            "API result count" not in monitoring["completionGate"]
            or "supervision track" not in monitoring["completionGate"]
    ):
        fail("implementation/compliance monitoring row does not require denominator reconciliation")

    emergency = by_slice["emergency-downstream-implementation"]
    if "external implementation observations are missing" not in emergency["currentBoundary"]:
        fail("implementation/compliance emergency row does not preserve the external-implementation gap")
    if "denied/NA" not in emergency["currentBoundary"]:
        fail("implementation/compliance emergency row does not preserve denied/NA application limits")
    if "externalSourceUrl" not in emergency["requiredFields"]:
        fail("implementation/compliance emergency row is missing external source fields")


def check_implementation_compliance_workqueue() -> None:
    if not IMPLEMENTATION_COMPLIANCE_WORKQUEUE_CSV.exists():
        fail(
            "missing implementation/compliance workqueue CSV "
            f"{IMPLEMENTATION_COMPLIANCE_WORKQUEUE_CSV.relative_to(ROOT)}"
        )
    with IMPLEMENTATION_COMPLIANCE_WORKQUEUE_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = set(reader.fieldnames or [])
        rows = list(reader)
    if fieldnames != REQUIRED_IMPLEMENTATION_COMPLIANCE_WORKQUEUE_COLUMNS:
        missing = REQUIRED_IMPLEMENTATION_COMPLIANCE_WORKQUEUE_COLUMNS - fieldnames
        extra = fieldnames - REQUIRED_IMPLEMENTATION_COMPLIANCE_WORKQUEUE_COLUMNS
        problems = []
        if missing:
            problems.append("missing " + ", ".join(sorted(missing)))
        if extra:
            problems.append("extra " + ", ".join(sorted(extra)))
        fail("implementation/compliance workqueue column mismatch: " + "; ".join(problems))
    if len(rows) != 4:
        fail("implementation/compliance workqueue must contain exactly four source slices")

    expected = {
        "lower-court-doctrinal-uptake": {
            "schemaTarget": "lower_court_doctrinal_uptake",
            "metric": "lowerCourtCompliance",
            "requiredField": "followedOrDistinguished",
        },
        "implementation-resistance": {
            "schemaTarget": "implementation_resistance",
            "metric": "governmentNoncomplianceRate",
            "requiredField": "resistanceCategory",
        },
        "monitoring-capacity": {
            "schemaTarget": "monitoring_capacity",
            "metric": "interbranchCompliance",
            "requiredField": "monitoringBody",
        },
        "emergency-downstream-implementation": {
            "schemaTarget": "emergency_downstream_implementation",
            "metric": "emergencyDownstreamEffect",
            "requiredField": "externalSourceUrl",
        },
    }
    by_slice = {row["sourceSlice"]: row for row in rows}
    missing_slices = set(expected) - set(by_slice)
    if missing_slices:
        fail("implementation/compliance workqueue is missing source slices: " + ", ".join(sorted(missing_slices)))
    for source_slice, checks in expected.items():
        row = by_slice[source_slice]
        if row["schemaTarget"] != checks["schemaTarget"]:
            fail(f"implementation/compliance workqueue has wrong schema target for {source_slice}")
        if checks["metric"] not in row["simulatorMetrics"]:
            fail(f"implementation/compliance workqueue is missing metric {checks['metric']} for {source_slice}")
        if checks["requiredField"] not in row["requiredFields"]:
            fail(f"implementation/compliance workqueue is missing required field {checks['requiredField']} for {source_slice}")
        if "implementation-compliance-template.csv" not in row["coderAction"]:
            fail(f"implementation/compliance workqueue does not point coders to the template for {source_slice}")
        if source_slice == "monitoring-capacity":
            if "bounded monitoring-capacity evidence" not in row["manuscriptUse"]:
                fail("implementation/compliance monitoring row must be bounded monitoring evidence")
            if "broader execution-throughput claims" not in row["denominatorGate"]:
                fail("implementation/compliance monitoring row must keep broader throughput claims gated")
        elif source_slice == "lower-court-doctrinal-uptake":
            if "descriptive environmental published-citation" not in row["manuscriptUse"]:
                fail("implementation/compliance uptake row must preserve bounded event evidence")
            if "No lowerCourtCompliance validation upgrade" not in row["denominatorGate"]:
                fail("implementation/compliance uptake row must keep general validation gated")
            if "relevant-case opportunity" not in row["denominatorGate"]:
                fail("implementation/compliance uptake row must require an opportunity denominator")
        elif source_slice == "implementation-resistance":
            if "bounded purposive environmental practical-implementation evidence" not in row["manuscriptUse"]:
                fail("implementation/compliance resistance row must preserve bounded practical evidence")
            if "No governmentNoncomplianceRate" not in row["denominatorGate"]:
                fail("implementation/compliance resistance row must keep general noncompliance gated")
            if "noncompliant outcomes" not in row["denominatorGate"]:
                fail("implementation/compliance resistance row must require broader outcomes")
        else:
            if "not validation" not in row["manuscriptUse"]:
                fail(f"implementation/compliance workqueue manuscript-use text may overclaim for {source_slice}")
            if "No validation upgrade" not in row["denominatorGate"]:
                fail(f"implementation/compliance workqueue denominator gate may overclaim for {source_slice}")


def check_implementation_compliance_schema() -> None:
    with IMPLEMENTATION_COMPLIANCE_SCHEMA_CSV.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        fail("implementation/compliance schema has no rows")
    by_field = {row["fieldName"]: row for row in rows}
    required_fields = {
        "sourceSlice",
        "decisionId",
        "treatmentType",
        "followedOrDistinguished",
        "actorType",
        "implementationAction",
        "resistanceCategory",
        "monitoringBody",
        "complianceStatus",
        "docketNumber",
        "policyStatus",
        "externalSourceUrl",
        "measurementDenominator",
        "denominatorReconciled",
    }
    missing = required_fields - set(by_field)
    if missing:
        fail("implementation/compliance schema is missing fields: " + ", ".join(sorted(missing)))
    for field in ("sourceKey", "sourceRecordId", "sourceUrl", "sourceSlice", "measurementDenominator", "denominatorReconciled"):
        if by_field[field]["validationUse"] != "required":
            fail(f"implementation/compliance schema must require {field}")
    target_text = " ".join(row["requiredFor"] for row in rows)
    for target in (
        "lower_court_doctrinal_uptake",
        "implementation_resistance",
        "monitoring_capacity",
        "emergency_downstream_implementation",
    ):
        if target not in target_text:
            fail(f"implementation/compliance schema is missing requiredFor target {target}")


def check_ecthr_execution_monitoring_extract() -> None:
    if not ECTHR_EXECUTION_MONITORING_EXTRACT_CSV.exists():
        fail(
            "missing ECtHR execution monitoring extract "
            f"{ECTHR_EXECUTION_MONITORING_EXTRACT_CSV.relative_to(ROOT)}"
        )
    if not ECTHR_EXECUTION_MONITORING_MANIFEST.exists():
        fail(
            "missing ECtHR execution monitoring manifest "
            f"{ECTHR_EXECUTION_MONITORING_MANIFEST.relative_to(ROOT)}"
        )
    with IMPLEMENTATION_COMPLIANCE_SCHEMA_CSV.open(newline="") as handle:
        schema_fields = [row["fieldName"] for row in csv.DictReader(handle)]
    with ECTHR_EXECUTION_MONITORING_EXTRACT_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if (reader.fieldnames or []) != schema_fields:
            fail("ECtHR execution monitoring extract columns do not match implementation/compliance schema")
        rows = list(reader)
    if len(rows) < 1000:
        fail("ECtHR execution monitoring extract has too few pending leading-case rows")

    manifest = json.loads(ECTHR_EXECUTION_MONITORING_MANIFEST.read_text())
    if int(manifest.get("rowCount", -1)) != len(rows):
        fail("ECtHR execution monitoring manifest rowCount does not match extract")
    if int(manifest.get("resultCount", -1)) != len(rows):
        fail("ECtHR execution monitoring extract does not reconcile to API resultCount")
    if "execgroup:MS" not in manifest.get("query", ""):
        fail("ECtHR execution monitoring query must be limited to master/leading case rows")

    capacities = {row["enforcementCapacity"] for row in rows}
    if "enhanced supervision" not in capacities or "standard supervision" not in capacities:
        fail("ECtHR execution monitoring extract must include enhanced and standard supervision rows")
    bad_rows: list[str] = []
    for row in rows:
        source_id = row.get("sourceRecordId", "")
        if row.get("sourceKey") != "ecthr-hudoc-exec-pending-leading-cases":
            bad_rows.append(f"{source_id}: unexpected sourceKey")
        if row.get("sourceSlice") != "monitoring-capacity":
            bad_rows.append(f"{source_id}: unexpected sourceSlice")
        if row.get("decidingCourt") != "European Court of Human Rights":
            bad_rows.append(f"{source_id}: unexpected decidingCourt")
        if row.get("monitoringBody") != "Committee of Ministers of the Council of Europe":
            bad_rows.append(f"{source_id}: unexpected monitoringBody")
        if row.get("complianceStatus") != "pending under supervision":
            bad_rows.append(f"{source_id}: unexpected complianceStatus")
        if not row.get("sourceUrl", "").startswith("https://hudoc.exec.coe.int/?i="):
            bad_rows.append(f"{source_id}: sourceUrl is not a HUDOC-EXEC item link")
        if "API resultcount" not in row.get("denominatorReconciled", ""):
            bad_rows.append(f"{source_id}: denominator is not reconciled to API resultcount")
        if "not a doctrinal uptake" not in row.get("coderNotes", ""):
            bad_rows.append(f"{source_id}: coderNotes do not preserve compliance boundary")
        duration = row.get("unresolvedDurationDays", "")
        if duration and not duration.isdigit():
            bad_rows.append(f"{source_id}: unresolvedDurationDays is not numeric")
    if bad_rows:
        fail("ECtHR execution monitoring extract rows require review: " + "; ".join(bad_rows[:10]))


def check_ecthr_execution_monitoring_summary() -> None:
    check_csv_schema(
        ECTHR_EXECUTION_MONITORING_SUMMARY_CSV,
        REQUIRED_ECTHR_EXECUTION_MONITORING_SUMMARY_COLUMNS,
        "ECtHR execution monitoring summary",
    )
    with ECTHR_EXECUTION_MONITORING_EXTRACT_CSV.open(newline="") as handle:
        extract_rows = list(csv.DictReader(handle))
    with ECTHR_EXECUTION_MONITORING_SUMMARY_CSV.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    by_metric = {row["metricKey"]: row for row in rows}
    required = {
        "ecthrHudocExecPendingLeadingRows",
        "ecthrHudocExecEnhancedSupervisionRows",
        "ecthrHudocExecStandardSupervisionRows",
        "ecthrHudocExecPendingOverFiveYearsRows",
    }
    missing = required - set(by_metric)
    if missing:
        fail("ECtHR execution monitoring summary is missing metrics: " + ", ".join(sorted(missing)))
    if int(by_metric["ecthrHudocExecPendingLeadingRows"]["observedValue"]) != len(extract_rows):
        fail("ECtHR execution monitoring summary total does not match extract")
    overclaiming = [
        row["metricKey"]
        for row in rows
        if "monitoring-capacity" not in row.get("manuscriptUse", "")
    ]
    if overclaiming:
        fail("ECtHR execution monitoring summary may overclaim: " + ", ".join(overclaiming[:10]))


def check_environmental_implementation_cohort() -> None:
    required_paths = (
        ENVIRONMENTAL_LOWER_COURT_EVENTS_CSV,
        ENVIRONMENTAL_CIRCUIT_EXPOSURE_CSV,
        ENVIRONMENTAL_PRACTICAL_IMPLEMENTATION_CSV,
        ENVIRONMENTAL_IMPLEMENTATION_CALIBRATION_CSV,
        ENVIRONMENTAL_IMPLEMENTATION_MANIFEST,
        ENVIRONMENTAL_IMPLEMENTATION_SUMMARY_CSV,
        ENVIRONMENTAL_IMPLEMENTATION_SUMMARY_MD,
        ENVIRONMENTAL_FULL_TEXT_AVAILABILITY_CSV,
        ENVIRONMENTAL_FULL_TEXT_AVAILABILITY_MD,
        ENVIRONMENTAL_TREATMENT_REVIEW_QUEUE_CSV,
        GURGANUS_TABLE_1_CLASSIFICATIONS_CSV,
    )
    for path in required_paths:
        if not path.exists():
            fail(f"missing environmental implementation artifact {path.relative_to(ROOT)}")

    with IMPLEMENTATION_COMPLIANCE_SCHEMA_CSV.open(newline="") as handle:
        schema_fields = [row["fieldName"] for row in csv.DictReader(handle)]
    with ENVIRONMENTAL_LOWER_COURT_EVENTS_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        event_fields = reader.fieldnames or []
        event_rows = list(reader)
    if len(event_fields) != len(set(event_fields)):
        fail("environmental lower-court event CSV has duplicate header fields")
    if event_fields[:len(schema_fields)] != schema_fields:
        fail("environmental lower-court event columns do not begin with the implementation schema")
    if set(event_fields[len(schema_fields):]) != REQUIRED_ENVIRONMENTAL_EVENT_EXTRA_COLUMNS:
        fail("environmental lower-court event provenance columns changed")
    if len(event_rows) != 191:
        fail("environmental lower-court cohort must contain 191 event rows")
    event_ids = [row["sourceRecordId"] for row in event_rows]
    if len(event_ids) != len(set(event_ids)):
        fail("environmental lower-court event sourceRecordId values are not unique")

    expected_decision_counts = {
        "massachusetts-v-epa-2007": 76,
        "rapanos-v-united-states-2006": 41,
        "utility-air-regulatory-group-v-epa-2014": 44,
        "michigan-v-epa-2015": 25,
        "sackett-v-epa-2023": 5,
    }
    decision_counts = Counter(row["sourceDecisionKey"] for row in event_rows)
    if decision_counts != Counter(expected_decision_counts):
        fail("environmental lower-court event decision counts changed")
    treatment_counts = Counter(row["treatmentType"] for row in event_rows)
    if treatment_counts != Counter({
        "applied": 5,
        "distinguished": 1,
        "cited_context_only": 109,
        "unclear": 76,
    }):
        fail("environmental lower-court treatment counts changed")
    if sum(row["fullTextStatus"] == "available" for row in event_rows) != 115:
        fail("environmental lower-court public full-text coverage changed")
    if sum(bool(row["citationContext"]) for row in event_rows) != 115:
        fail("environmental lower-court citation-context coverage changed")
    directional_labels = {
        "followed", "applied", "distinguished", "narrowed", "questioned/resisted"
    }
    if sum(row["treatmentType"] in directional_labels for row in event_rows) != 6:
        fail("environmental lower-court directional candidate count changed")
    allowed_treatments = {
        "followed",
        "applied",
        "distinguished",
        "narrowed",
        "questioned/resisted",
        "cited_context_only",
        "unclear",
    }
    allowed_circuits = {
        "ca1", "ca2", "ca3", "ca4", "ca5", "ca6", "ca7",
        "ca8", "ca9", "ca10", "ca11", "cadc", "cafc",
    }
    for row in event_rows:
        source_id = row["sourceRecordId"]
        if row["sourceSlice"] != "lower-court-doctrinal-uptake":
            fail(f"environmental lower-court event has wrong source slice: {source_id}")
        if row["treatmentType"] not in allowed_treatments:
            fail(f"environmental lower-court event has unknown treatment: {source_id}")
        if row["federalCircuit"] not in allowed_circuits:
            fail(f"environmental lower-court event has unknown circuit: {source_id}")
        if row["opinionStatus"] != "Published":
            fail(f"environmental lower-court event is outside published-only scope: {source_id}")
        if not (row["citingCaseName"] or row["citingCaseNameFull"]):
            fail(f"environmental lower-court event lacks a citing-case caption: {source_id}")
        if row["denominatorReconciled"] != "1":
            fail(f"environmental lower-court event denominator is not reconciled: {source_id}")
        if row["citationLinkVerified"] != "1":
            fail(f"environmental lower-court event citation link is not verified: {source_id}")
        if date.fromisoformat(row["treatmentDate"]) <= date.fromisoformat(row["decisionDate"]):
            fail(f"environmental lower-court event is not post-decision: {source_id}")
        if row["treatmentDate"] < row["postDecisionWindowStart"] or row["treatmentDate"] > row["postDecisionWindowEnd"]:
            fail(f"environmental lower-court event is outside its fixed window: {source_id}")
        if row["fullTextStatus"] == "available" and not row["citationContext"]:
            fail(f"environmental lower-court available text lacks citation context: {source_id}")
        if row["fullTextStatus"] == "available" and row["fullTextUnavailableReason"]:
            fail(f"environmental available text has an unavailable reason: {source_id}")
        if row["fullTextStatus"] != "available" and row["treatmentType"] != "unclear":
            fail(f"environmental lower-court unavailable text received a treatment code: {source_id}")
        if row["fullTextStatus"] != "available" and not row["fullTextUnavailableReason"]:
            fail(f"environmental lower-court unavailable text lacks a reason: {source_id}")
        if row["fullTextStatus"] != "available" and row["searchSnippetAvailable"] != "1":
            fail(f"environmental lower-court unavailable text lacks its search snippet: {source_id}")
        if row["treatmentType"] in directional_labels and not row["codingRule"].startswith("target-linked-"):
            fail(f"environmental lower-court directional code is not target-linked: {source_id}")
        if "pending expert legal review" not in row["coderNotes"]:
            fail(f"environmental lower-court event omits candidate-review status: {source_id}")
        if "not ignored precedent or noncompliance" not in row["coderNotes"]:
            fail(f"environmental lower-court event omits the no-citation boundary: {source_id}")
    uarg_negative = next(
        (
            row for row in event_rows
            if row["sourceRecordId"]
            == "utility-air-regulatory-group-v-epa-2014:3153967"
        ),
        None,
    )
    if not uarg_negative or uarg_negative["treatmentType"] != "cited_context_only":
        fail("environmental UARG criminal-restitution negative regression changed")

    with ENVIRONMENTAL_CIRCUIT_EXPOSURE_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if set(reader.fieldnames or []) != REQUIRED_ENVIRONMENTAL_EXPOSURE_COLUMNS:
            fail("environmental circuit-exposure columns changed")
        exposure_rows = list(reader)
    if len(exposure_rows) != 65:
        fail("environmental circuit-exposure frame must contain 65 rows")
    exposure_ids = [
        (row["sourceDecisionKey"], row["circuitId"]) for row in exposure_rows
    ]
    if len(exposure_ids) != len(set(exposure_ids)):
        fail("environmental circuit-exposure decision/circuit cells are not unique")
    if Counter(row["sourceDecisionKey"] for row in exposure_rows) != Counter({
        key: 13 for key in expected_decision_counts
    }):
        fail("environmental circuit-exposure rows do not provide thirteen circuits per decision")
    event_by_cell = Counter(
        (row["sourceDecisionKey"], row["federalCircuit"]) for row in event_rows
    )
    zero_cells = 0
    for row in exposure_rows:
        cell = (row["sourceDecisionKey"], row["circuitId"])
        observed = int(row["observedCitingOpinionDocuments"])
        if observed != event_by_cell[cell]:
            fail(f"environmental circuit-exposure count does not reconcile for {cell}")
        expected_zero = "1" if observed == 0 else "0"
        if row["noObservedCitingEvent"] != expected_zero:
            fail(f"environmental circuit-exposure zero flag does not reconcile for {cell}")
        zero_cells += observed == 0
        if row["legallyExposed"] != "1" or row["denominatorReconciled"] != "1":
            fail(f"environmental circuit-exposure legal denominator changed for {cell}")
        if "not an empirical exposure" not in row["coderNotes"]:
            fail(f"environmental circuit citation-presence row omits denominator caveat for {cell}")
    if zero_cells != 20:
        fail("environmental circuit-exposure zero-cell count changed")

    with ENVIRONMENTAL_PRACTICAL_IMPLEMENTATION_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        practical_fields = reader.fieldnames or []
        practical_rows = list(reader)
    if practical_fields[:len(schema_fields)] != schema_fields:
        fail("environmental practical columns do not begin with the implementation schema")
    if set(practical_fields[len(schema_fields):]) != REQUIRED_ENVIRONMENTAL_PRACTICAL_EXTRA_COLUMNS:
        fail("environmental practical provenance columns changed")
    if len(practical_rows) != 5:
        fail("environmental practical cohort must contain five rows")
    classifications = Counter(row["authorClassification"] for row in practical_rows)
    if classifications != Counter({"compliant": 4, "narrowly compliant": 1}):
        fail("environmental practical classifications changed")
    for row in practical_rows:
        source_id = row["sourceRecordId"]
        if row["sourceSlice"] != "implementation-resistance":
            fail(f"environmental practical row has wrong source slice: {source_id}")
        if row["denominatorReconciled"] != "1":
            fail(f"environmental practical denominator is not reconciled: {source_id}")
        if date.fromisoformat(row["sourceRecordDate"]) <= date.fromisoformat(row["decisionDate"]):
            fail(f"environmental practical row is not post-decision: {source_id}")
        if not re.fullmatch(r"[0-9a-f]{64}", row["primarySourceSha256"]):
            fail(f"environmental practical source hash is malformed: {source_id}")
        if row["authorClassification"] == "narrowly compliant":
            if row["resistanceCategory"] != "substitution":
                fail("environmental narrow-compliance row must preserve substitution")
        elif row["resistanceCategory"] != "none":
            fail(f"environmental compliant row has unexpected resistance: {source_id}")
        if "No open noncompliance event" not in row["coderNotes"]:
            fail(f"environmental practical row omits noncompliance boundary: {source_id}")

    with ENVIRONMENTAL_IMPLEMENTATION_CALIBRATION_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if set(reader.fieldnames or []) != REQUIRED_LOWER_COURT_PRECEDENT_TREATMENT_CALIBRATION_COLUMNS:
            fail("environmental implementation calibration columns changed")
        calibration_rows = list(reader)
    if len(calibration_rows) != 32:
        fail("environmental implementation calibration must contain 32 rows")
    for row in calibration_rows:
        denominator = float(row["denominator"])
        numerator = float(row["numerator"])
        value = float(row["value"])
        expected = numerator / denominator if denominator else 0.0
        if abs(value - expected) > 5e-10:
            fail(f"environmental calibration arithmetic changed for {row['metric']}")
        if row["validationUse"] not in {
            "data_quality_guardrail",
            "descriptive_case_study_summary",
        }:
            fail(f"environmental calibration use may overclaim for {row['metric']}")
        if row["validationUse"] == "direct_behavior_guardrail":
            fail(f"environmental calibration row is mislabeled behavioral: {row['metric']}")
        if "synthetic" not in row["comparabilityClass"]:
            fail(f"environmental calibration row omits scale boundary for {row['metric']}")
    if Counter(row["validationUse"] for row in calibration_rows) != Counter({
        "data_quality_guardrail": 10,
        "descriptive_case_study_summary": 22,
    }):
        fail("environmental calibration use labels changed")
    if any(
        "ObservedCircuitCoverage" in row["metric"]
        or row["metric"].startswith("practical")
        for row in calibration_rows
    ):
        fail("environmental calibration retains behavioral-rate terminology")
    if sum(
        "PublishedCitationPresenceByCircuit" in row["metric"]
        for row in calibration_rows
    ) != 5:
        fail("environmental circuit citation-presence metrics changed")

    with ENVIRONMENTAL_IMPLEMENTATION_SUMMARY_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if set(reader.fieldnames or []) != REQUIRED_ENVIRONMENTAL_SUMMARY_COLUMNS:
            fail("environmental implementation summary columns changed")
        summary_rows = list(reader)
    if len(summary_rows) != 6 or summary_rows[-1]["decisionKey"] != "pooled":
        fail("environmental implementation summary must contain five decisions plus pooled row")
    pooled = summary_rows[-1]
    expected_pooled = {
        "allCourtSearchClusters": "239",
        "federalClustersBeforeDedupe": "192",
        "citingOpinionDocuments": "191",
        "fullTextAvailable": "115",
        "citationContextFound": "115",
        "applied": "5",
        "distinguished": "1",
        "citedContextOnly": "109",
        "unclear": "76",
        "exposedCircuits": "65",
    }
    for field, expected in expected_pooled.items():
        if pooled[field] != expected:
            fail(f"environmental implementation pooled summary changed for {field}")
    summary_text = ENVIRONMENTAL_IMPLEMENTATION_SUMMARY_MD.read_text()
    for required_text in (
        "do **not** supply an all-relevant-case opportunity denominator",
        "thirteen circuits is not an empirical exposure or behavioral denominator",
        "No noncompliant outcome is observed",
        "pending expert legal review",
    ):
        if required_text not in summary_text:
            fail(f"environmental implementation summary omits boundary: {required_text}")

    with ENVIRONMENTAL_FULL_TEXT_AVAILABILITY_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if set(reader.fieldnames or []) != REQUIRED_ENVIRONMENTAL_AVAILABILITY_COLUMNS:
            fail("environmental full-text availability columns changed")
        availability_rows = list(reader)
    pooled_availability = [
        row
        for row in availability_rows
        if row["dimension"] == "pooled" and row["category"] == "all events"
    ]
    if len(pooled_availability) != 1:
        fail("environmental full-text availability audit lacks one pooled row")
    if {
        key: pooled_availability[0][key]
        for key in ("events", "available", "unavailable")
    } != {"events": "191", "available": "115", "unavailable": "76"}:
        fail("environmental full-text availability pooled counts changed")
    expected_decision_availability = {
        "massachusetts-v-epa-2007": ("76", "39"),
        "rapanos-v-united-states-2006": ("41", "15"),
        "utility-air-regulatory-group-v-epa-2014": ("44", "38"),
        "michigan-v-epa-2015": ("25", "18"),
        "sackett-v-epa-2023": ("5", "5"),
    }
    observed_decision_availability = {
        row["category"]: (row["events"], row["available"])
        for row in availability_rows
        if row["dimension"] == "decision"
    }
    if observed_decision_availability != expected_decision_availability:
        fail("environmental full-text decision missingness changed")
    opinion_availability = {
        row["category"]: (row["events"], row["available"])
        for row in availability_rows
        if row["dimension"] == "opinion_type"
    }
    if opinion_availability != {
        "combined-opinion": ("169", "115"),
        "lead-opinion": ("18", "0"),
        "dissent": ("3", "0"),
        "in-part-opinion": ("1", "0"),
    }:
        fail("environmental full-text opinion-type missingness changed")
    if sum(
        int(row["events"])
        for row in availability_rows
        if row["dimension"] == "unavailable_reason"
    ) != 76:
        fail("environmental full-text unavailability reasons do not reconcile")
    availability_text = ENVIRONMENTAL_FULL_TEXT_AVAILABILITY_MD.read_text()
    for required_text in ("Missingness is visibly nonrandom", "115 of 191"):
        if required_text not in availability_text:
            fail(f"environmental availability audit omits warning: {required_text}")

    with ENVIRONMENTAL_TREATMENT_REVIEW_QUEUE_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if set(reader.fieldnames or []) != REQUIRED_ENVIRONMENTAL_TREATMENT_REVIEW_COLUMNS:
            fail("environmental treatment review-queue columns changed")
        review_rows = list(reader)
    if len(review_rows) != 16:
        fail("environmental treatment review queue must contain sixteen rows")
    if Counter(row["reviewStratum"] for row in review_rows) != Counter({
        "all_automated_directional_candidates": 6,
        "stratified_citation_only_sample": 10,
    }):
        fail("environmental treatment review strata changed")
    if any(row["reviewStatus"] != "pending_expert_review" for row in review_rows):
        fail("environmental treatment review queue incorrectly claims completed review")
    if any(
        row[field]
        for row in review_rows
        for field in ("secondCoderTreatment", "agreement", "adjudicatedTreatment")
    ):
        fail("environmental treatment review queue contains unverified expert coding")
    event_by_id = {row["sourceRecordId"]: row for row in event_rows}
    for row in review_rows:
        source = event_by_id.get(row["sourceRecordId"])
        if source is None or source["treatmentType"] != row["automatedTreatment"]:
            fail(f"environmental treatment review row does not reconcile: {row['sourceRecordId']}")

    with GURGANUS_TABLE_1_CLASSIFICATIONS_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if set(reader.fieldnames or []) != REQUIRED_GURGANUS_CLASSIFICATION_COLUMNS:
            fail("Gurganus structured-classification columns changed")
        gurganus_rows = list(reader)
    if len(gurganus_rows) != 5:
        fail("Gurganus structured classification must contain five rows")
    if Counter(row["authorClassification"] for row in gurganus_rows) != classifications:
        fail("Gurganus structured classifications do not reconcile")
    for row in gurganus_rows:
        canonical = json.dumps(
            {
                key: value
                for key, value in row.items()
                if key != "classificationRecordSha256"
            },
            sort_keys=True,
            ensure_ascii=False,
        ).encode("utf-8")
        if hashlib.sha256(canonical).hexdigest() != row["classificationRecordSha256"]:
            fail(f"Gurganus structured-classification hash changed: {row['sourceDecisionKey']}")
        if row["articleDoi"] != "10.1111/lapo.70004" or "Table 1" not in row["articleLocator"]:
            fail(f"Gurganus structured classification lacks locator: {row['sourceDecisionKey']}")

    manifest = json.loads(ENVIRONMENTAL_IMPLEMENTATION_MANIFEST.read_text())
    if manifest.get("schemaVersion") != "1.0" or manifest.get("decisionCount") != 5:
        fail("environmental implementation manifest identity changed")
    if date.fromisoformat(manifest["extractionDate"]) > date.today():
        fail("environmental implementation manifest extraction date is in the future")
    lower = manifest.get("lowerCourtCohort", {})
    lower_expectations = {
        "windowDays": 730,
        "allCourtSearchClusters": 239,
        "federalClustersBeforeDedupe": 192,
        "federalClustersAfterDedupe": 177,
        "citingOpinionDocumentsAfterDedupe": 191,
        "fullTextAvailable": 115,
        "citationContextFound": 115,
        "citationLinkVerified": 191,
        "exposureRows": 65,
    }
    for field, expected in lower_expectations.items():
        if lower.get(field) != expected:
            fail(f"environmental implementation manifest changed for lowerCourtCohort.{field}")
    if lower.get("publicationStatusScope") != "published opinions only":
        fail("environmental implementation manifest omits published-only scope")
    if any(
        "status:published" not in search.get("query", "")
        for search in lower.get("searches", {}).values()
    ):
        fail("environmental implementation manifest search query is not explicitly published")
    if lower.get("treatmentReviewStatus") != "pending expert legal review":
        fail("environmental implementation manifest overstates treatment review")
    if lower.get("treatmentCounts") != dict(sorted(treatment_counts.items())):
        fail("environmental implementation manifest treatment counts do not reconcile")
    exposure = manifest.get("circuitExposureFrame", {})
    if exposure.get("rowCount") != 65 or exposure.get("zeroObservedEventCells") != 20:
        fail("environmental implementation manifest exposure frame changed")
    practical = manifest.get("practicalImplementationCohort", {})
    if practical.get("sourceStudyDoi") != "10.1111/lapo.70004":
        fail("environmental implementation manifest source-study DOI changed")
    if practical.get("sourceStudyLicense") != "CC BY 4.0":
        fail("environmental implementation manifest source-study license changed")
    if practical.get("classificationCounts") != dict(sorted(classifications.items())):
        fail("environmental implementation manifest practical counts do not reconcile")
    if practical.get("structuredClassificationFile") != (
        GURGANUS_TABLE_1_CLASSIFICATIONS_CSV.relative_to(ROOT).as_posix()
    ):
        fail("environmental implementation manifest omits structured Gurganus classifications")
    official_sources = practical.get("verifiedOfficialSources", {})
    if len(official_sources) != 8:
        fail("environmental implementation manifest official-source inventory changed")
    for document_id, metadata in official_sources.items():
        if metadata.get("status") != "verified":
            fail(f"environmental official source is not verified: {document_id}")
        if not re.fullmatch(r"[0-9a-f]{64}", metadata.get("sha256", "")):
            fail(f"environmental official-source hash is malformed: {document_id}")
    limitations = " ".join(manifest.get("limitations", [])).lower()
    for required_text in (
        "published-only",
        "nonrandom",
        "all-case opportunity denominator",
        "purposively selected",
        "no noncompliant classification",
        "denominator-matched",
    ):
        if required_text not in limitations:
            fail(f"environmental implementation manifest omits limitation: {required_text}")
    intended_use = manifest.get("dataQuality", {}).get("intendedUse", "")
    if "descriptive case-study" not in intended_use or "not behavioral guardrails" not in intended_use:
        fail("environmental implementation manifest intended use may overclaim")
    expected_output_paths = {
        path.relative_to(ROOT).as_posix(): path
        for path in (
            ENVIRONMENTAL_LOWER_COURT_EVENTS_CSV,
            ENVIRONMENTAL_CIRCUIT_EXPOSURE_CSV,
            ENVIRONMENTAL_PRACTICAL_IMPLEMENTATION_CSV,
            ENVIRONMENTAL_IMPLEMENTATION_CALIBRATION_CSV,
            ENVIRONMENTAL_IMPLEMENTATION_SUMMARY_CSV,
            ENVIRONMENTAL_IMPLEMENTATION_SUMMARY_MD,
            ENVIRONMENTAL_FULL_TEXT_AVAILABILITY_CSV,
            ENVIRONMENTAL_FULL_TEXT_AVAILABILITY_MD,
            ENVIRONMENTAL_TREATMENT_REVIEW_QUEUE_CSV,
            GURGANUS_TABLE_1_CLASSIFICATIONS_CSV,
        )
    }
    if set(manifest.get("outputSha256", {})) != set(expected_output_paths):
        fail("environmental implementation manifest output hash inventory changed")
    for relative, path in expected_output_paths.items():
        if manifest["outputSha256"].get(relative) != sha256(path):
            fail(f"environmental implementation manifest hash mismatch for {relative}")
    expected_rows = {
        ENVIRONMENTAL_LOWER_COURT_EVENTS_CSV.relative_to(ROOT).as_posix(): 191,
        ENVIRONMENTAL_CIRCUIT_EXPOSURE_CSV.relative_to(ROOT).as_posix(): 65,
        ENVIRONMENTAL_PRACTICAL_IMPLEMENTATION_CSV.relative_to(ROOT).as_posix(): 5,
        ENVIRONMENTAL_IMPLEMENTATION_CALIBRATION_CSV.relative_to(ROOT).as_posix(): 32,
        ENVIRONMENTAL_IMPLEMENTATION_SUMMARY_CSV.relative_to(ROOT).as_posix(): 6,
        ENVIRONMENTAL_FULL_TEXT_AVAILABILITY_CSV.relative_to(ROOT).as_posix(): len(
            availability_rows
        ),
        ENVIRONMENTAL_TREATMENT_REVIEW_QUEUE_CSV.relative_to(ROOT).as_posix(): 16,
        GURGANUS_TABLE_1_CLASSIFICATIONS_CSV.relative_to(ROOT).as_posix(): 5,
    }
    if manifest.get("outputRows") != expected_rows:
        fail("environmental implementation manifest row counts changed")


def check_lower_court_precedent_treatment_benchmark() -> None:
    required_paths = (
        LOWER_COURT_PRECEDENT_TREATMENT_BENCHMARK_CSV,
        LOWER_COURT_PRECEDENT_TREATMENT_MANIFEST,
        LOWER_COURT_PRECEDENT_TREATMENT_SUMMARY_CSV,
        LOWER_COURT_PRECEDENT_TREATMENT_CALIBRATION_CSV,
    )
    for path in required_paths:
        if not path.exists():
            fail(f"missing lower-court precedent-treatment artifact {path.relative_to(ROOT)}")

    with LOWER_COURT_PRECEDENT_TREATMENT_BENCHMARK_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if (reader.fieldnames or []) != REQUIRED_LOWER_COURT_PRECEDENT_TREATMENT_COLUMNS:
            fail("lower-court precedent-treatment benchmark columns or column order changed")
        rows = list(reader)
    if len(rows) != 876:
        fail("lower-court precedent-treatment benchmark must contain exactly 876 precedents")
    if len({row["sourceRecordId"] for row in rows}) != 876:
        fail("lower-court precedent-treatment benchmark sourceRecordId values are not unique")
    if len({row["usReportsCitation"] for row in rows}) != 876:
        fail("lower-court precedent-treatment benchmark U.S. Reports citations are not unique")
    if any(not row["sourceRecordId"] or not row["usReportsCitation"] for row in rows):
        fail("lower-court precedent-treatment benchmark contains a blank source identifier")
    term_counts = Counter(row["supremeCourtTerm"] for row in rows)
    if dict(sorted(term_counts.items())) != EXPECTED_LOWER_COURT_PRECEDENT_TERM_COUNTS:
        fail("lower-court precedent-treatment source-term counts do not match the audited release")
    if sum(row["articleMainModelEligible"] == "yes" for row in rows) != 861:
        fail("lower-court precedent-treatment benchmark must retain exactly 861 main-model rows")
    if sum(row["constitutionalIssue"] == "yes" for row in rows) != 223:
        fail("lower-court precedent-treatment benchmark must retain exactly 223 constitutional rows")

    source_key = "masood-kassow-songer-2019-precedent-treatment"
    source_url = "https://doi.org/10.7910/DVN/DZZY7G"
    row_problems: list[str] = []
    for row in rows:
        source_id = row["sourceRecordId"]
        if row["sourceKey"] != source_key:
            row_problems.append(f"{source_id}: unexpected sourceKey")
        if row["sourceUrl"] != source_url:
            row_problems.append(f"{source_id}: unexpected sourceUrl")
        if row["sourceDatasetDoi"] != "10.7910/DVN/DZZY7G":
            row_problems.append(f"{source_id}: unexpected dataset DOI")
        if row["articleDoi"] != "10.1086/703067":
            row_problems.append(f"{source_id}: unexpected article DOI")
        cited = int(row["citedCountThrough2016"])
        followed = int(row["followedCountThrough2016"])
        other_adverse = int(row["otherAdverseTreatmentCountThrough2016"])
        distinguished = int(row["distinguishedCountThrough2016"])
        adverse = int(row["adverseTreatmentCountThrough2016"])
        cited_or_followed = int(row["citedOrFollowedCountThrough2016"])
        cited_or_adverse = int(row["citedOrAdverseCountThrough2016"])
        directional = int(row["directionalTreatmentCountThrough2016"])
        if adverse != other_adverse + distinguished:
            row_problems.append(f"{source_id}: adverse treatments do not reconcile")
        if cited_or_followed != cited + followed:
            row_problems.append(f"{source_id}: cited-or-followed denominator does not reconcile")
        if cited_or_adverse != cited + adverse:
            row_problems.append(f"{source_id}: cited-or-adverse denominator does not reconcile")
        if directional != followed + adverse:
            row_problems.append(f"{source_id}: directional-treatment denominator does not reconcile")
        ratio_checks = (
            ("followedShareAmongCitedOrFollowed", followed, cited_or_followed),
            ("adverseShareAmongCitedOrAdverse", adverse, cited_or_adverse),
            ("followedShareAmongDirectionalTreatments", followed, directional),
        )
        for field, numerator, denominator in ratio_checks:
            value = row[field]
            if denominator == 0:
                if value:
                    row_problems.append(f"{source_id}: {field} must be blank for a zero denominator")
            elif not value or abs(float(value) - numerator / denominator) > 1e-9:
                row_problems.append(f"{source_id}: {field} does not reconcile")
        notes = row["coderNotes"].lower()
        if "not as a practical-compliance rate" not in notes:
            row_problems.append(f"{source_id}: coderNotes omit the practical-compliance boundary")
    if row_problems:
        fail(
            "lower-court precedent-treatment rows require review: "
            + "; ".join(row_problems[:10])
        )

    def aggregate(selected: list[dict[str, str]]) -> dict[str, int]:
        cited = sum(int(row["citedCountThrough2016"]) for row in selected)
        followed = sum(int(row["followedCountThrough2016"]) for row in selected)
        other_adverse = sum(
            int(row["otherAdverseTreatmentCountThrough2016"]) for row in selected
        )
        distinguished = sum(int(row["distinguishedCountThrough2016"]) for row in selected)
        adverse = other_adverse + distinguished
        return {
            "precedents": len(selected),
            "cited": cited,
            "followed": followed,
            "otherAdverse": other_adverse,
            "distinguished": distinguished,
            "adverse": adverse,
            "citedOrFollowed": cited + followed,
            "citedOrAdverse": cited + adverse,
            "directional": followed + adverse,
        }

    subsets = {
        "all_precedents": rows,
        "article_main_model": [
            row for row in rows if row["articleMainModelEligible"] == "yes"
        ],
        "constitutional_issues": [
            row for row in rows if row["constitutionalIssue"] == "yes"
        ],
    }
    aggregates = {key: aggregate(selected) for key, selected in subsets.items()}
    expected_core_totals = {
        "all_precedents": {
            "precedents": 876,
            "cited": 959329,
            "followed": 235256,
            "adverse": 38297,
        },
        "article_main_model": {
            "precedents": 861,
            "cited": 955702,
            "followed": 234076,
            "adverse": 38207,
        },
        "constitutional_issues": {
            "precedents": 223,
            "cited": 249777,
            "followed": 47370,
            "adverse": 17753,
        },
    }
    for subset, totals in expected_core_totals.items():
        for key, expected in totals.items():
            if aggregates[subset][key] != expected:
                fail(
                    "lower-court precedent-treatment "
                    f"{subset} {key} total does not match the audited source"
                )

    manifest = json.loads(LOWER_COURT_PRECEDENT_TREATMENT_MANIFEST.read_text())
    manifest_expectations = {
        "sourceKey": source_key,
        "sourceDatasetDoi": "10.7910/DVN/DZZY7G",
        "articleDoi": "10.1086/703067",
        "datasetVersion": "1.0",
        "sourceRowCount": 876,
        "sourceColumnCount": 302,
        "articleMainModelRowCount": 861,
        "constitutionalIssueRowCount": 223,
        "originalFileMd5": "69cb7a7ff2d75da1ac6db1f99e085ffc",
        "codeFileMd5": "235872cd35d804bbee94b308289b34d8",
        "tabExportSha256": "815dd4a628e8be96b7a49b400bad55c0942193adcc152d0b0b055247c582069a",
        "fileUnf": "UNF:6:L5oJ8wGINogURIEtpkzJpQ==",
    }
    for key, expected in manifest_expectations.items():
        if manifest.get(key) != expected:
            fail(f"lower-court precedent-treatment manifest has unexpected {key}")
    if manifest.get("license", {}).get("rightsIdentifier") != "CC0-1.0":
        fail("lower-court precedent-treatment manifest does not preserve the CC0-1.0 license")
    if manifest.get("sourceTermCounts") != EXPECTED_LOWER_COURT_PRECEDENT_TERM_COUNTS:
        fail("lower-court precedent-treatment manifest source-term counts changed")
    if manifest.get("aggregateCounts") != aggregates["all_precedents"]:
        fail("lower-court precedent-treatment manifest aggregate counts do not reconcile")
    if manifest.get("constitutionalIssueAggregateCounts") != aggregates["constitutional_issues"]:
        fail("lower-court precedent-treatment manifest constitutional counts do not reconcile")
    boundary = " ".join(manifest.get("evidenceBoundary", [])).lower()
    for required_text in ("not one row per lower-court opinion", "practical implementation"):
        if required_text not in boundary:
            fail(
                "lower-court precedent-treatment manifest omits evidence boundary: "
                + required_text
            )
    expected_output_paths = {
        path.relative_to(ROOT).as_posix(): path
        for path in (
            LOWER_COURT_PRECEDENT_TREATMENT_BENCHMARK_CSV,
            LOWER_COURT_PRECEDENT_TREATMENT_CALIBRATION_CSV,
            LOWER_COURT_PRECEDENT_TREATMENT_SUMMARY_CSV,
            ROOT / "reports" / "lower-court-precedent-treatment-summary-v1.md",
        )
    }
    if set(manifest.get("outputs", {})) != set(expected_output_paths):
        fail("lower-court precedent-treatment manifest output inventory changed")
    for relative, path in expected_output_paths.items():
        if manifest["outputs"].get(relative) != sha256(path):
            fail(f"lower-court precedent-treatment manifest hash mismatch for {relative}")

    with LOWER_COURT_PRECEDENT_TREATMENT_SUMMARY_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if set(reader.fieldnames or []) != REQUIRED_LOWER_COURT_PRECEDENT_TREATMENT_SUMMARY_COLUMNS:
            fail("lower-court precedent-treatment summary columns changed")
        summary_rows = list(reader)
    if len(summary_rows) != 21:
        fail("lower-court precedent-treatment summary must contain 21 subset/metric rows")
    summary_by_key = {
        (row["subset"], row["metricKey"]): row for row in summary_rows
    }
    if len(summary_by_key) != len(summary_rows):
        fail("lower-court precedent-treatment summary contains duplicate subset/metric rows")
    for subset, totals in aggregates.items():
        expected_metrics: dict[str, tuple[int, int | None, float]] = {
            "lowerCourtPrecedentRows": (
                totals["precedents"],
                None,
                float(totals["precedents"]),
            ),
            "lowerCourtCitedCount": (
                totals["cited"],
                None,
                float(totals["cited"]),
            ),
            "lowerCourtFollowedCount": (
                totals["followed"],
                None,
                float(totals["followed"]),
            ),
            "lowerCourtAdverseTreatmentCount": (
                totals["adverse"],
                None,
                float(totals["adverse"]),
            ),
            "lowerCourtFollowedShareAmongCitedOrFollowed": (
                totals["followed"],
                totals["citedOrFollowed"],
                totals["followed"] / totals["citedOrFollowed"],
            ),
            "lowerCourtAdverseShareAmongCitedOrAdverse": (
                totals["adverse"],
                totals["citedOrAdverse"],
                totals["adverse"] / totals["citedOrAdverse"],
            ),
            "lowerCourtFollowedShareAmongDirectionalTreatments": (
                totals["followed"],
                totals["directional"],
                totals["followed"] / totals["directional"],
            ),
        }
        for metric, (numerator, denominator, value) in expected_metrics.items():
            row = summary_by_key.get((subset, metric))
            if row is None:
                fail(
                    "lower-court precedent-treatment summary is missing "
                    f"{subset}/{metric}"
                )
            if int(row["numerator"]) != numerator:
                fail(f"lower-court precedent-treatment summary numerator mismatch for {subset}/{metric}")
            if denominator is None:
                if row["denominator"]:
                    fail(f"lower-court precedent-treatment summary denominator should be blank for {subset}/{metric}")
            elif int(row["denominator"]) != denominator:
                fail(f"lower-court precedent-treatment summary denominator mismatch for {subset}/{metric}")
            if abs(float(row["observedValue"]) - value) > 1e-9:
                fail(f"lower-court precedent-treatment summary value mismatch for {subset}/{metric}")
            if row["sourceUrl"] != source_url:
                fail(f"lower-court precedent-treatment summary source URL changed for {subset}/{metric}")
            if row["validationUse"] != "direct_aggregate_doctrinal_uptake":
                fail(f"lower-court precedent-treatment summary use changed for {subset}/{metric}")
            if "not practical compliance" not in row["manuscriptUse"]:
                fail(f"lower-court precedent-treatment summary may overclaim for {subset}/{metric}")

    with LOWER_COURT_PRECEDENT_TREATMENT_CALIBRATION_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if set(reader.fieldnames or []) != REQUIRED_LOWER_COURT_PRECEDENT_TREATMENT_CALIBRATION_COLUMNS:
            fail("lower-court precedent-treatment calibration columns changed")
        calibration_rows = list(reader)
    if len(calibration_rows) != 60:
        fail("lower-court precedent-treatment calibration must contain exactly 60 term rows")
    calibration_by_key = {
        (row["metric"], row["term"]): row for row in calibration_rows
    }
    if len(calibration_by_key) != 60:
        fail("lower-court precedent-treatment calibration contains duplicate metric/term rows")
    metric_definitions = {
        "lowerCourtFollowedShareAmongCitedOrFollowed": (
            "followed",
            "citedOrFollowed",
        ),
        "lowerCourtAdverseShareAmongCitedOrAdverse": (
            "adverse",
            "citedOrAdverse",
        ),
        "lowerCourtFollowedShareAmongDirectionalTreatments": (
            "followed",
            "directional",
        ),
    }
    calibration_metric_counts = Counter(row["metric"] for row in calibration_rows)
    for suffix, selector in {
        "allPrecedents": lambda row: True,
        "constitutionalIssues": lambda row: row["constitutionalIssue"] == "yes",
    }.items():
        for metric_base, (numerator_key, denominator_key) in metric_definitions.items():
            metric = f"{metric_base}_{suffix}"
            if calibration_metric_counts[metric] != 10:
                fail(f"lower-court precedent-treatment calibration must have ten terms for {metric}")
            for term in EXPECTED_LOWER_COURT_PRECEDENT_TERM_COUNTS:
                selected = [
                    row
                    for row in rows
                    if row["supremeCourtTerm"] == term and selector(row)
                ]
                totals = aggregate(selected)
                expected_numerator = totals[numerator_key]
                expected_denominator = totals[denominator_key]
                expected_value = expected_numerator / expected_denominator
                row = calibration_by_key.get((metric, term))
                if row is None:
                    fail(f"lower-court precedent-treatment calibration is missing {metric}/{term}")
                if int(row["numerator"]) != expected_numerator:
                    fail(f"lower-court precedent-treatment calibration numerator mismatch for {metric}/{term}")
                if int(row["denominator"]) != expected_denominator:
                    fail(f"lower-court precedent-treatment calibration denominator mismatch for {metric}/{term}")
                if abs(float(row["value"]) - expected_value) > 1e-9:
                    fail(f"lower-court precedent-treatment calibration value mismatch for {metric}/{term}")
                if row["sourceKey"] != source_key or row["sourceUrl"] != source_url:
                    fail(f"lower-court precedent-treatment calibration provenance changed for {metric}/{term}")
                if row["domain"] != "lower_court_compliance":
                    fail(f"lower-court precedent-treatment calibration domain changed for {metric}/{term}")
                if row["validationUse"] != "direct_behavior_guardrail":
                    fail(f"lower-court precedent-treatment calibration use changed for {metric}/{term}")
                if "synthetic case-average compliance score" not in row["comparabilityClass"]:
                    fail(f"lower-court precedent-treatment calibration omits scale boundary for {metric}/{term}")

    with PATHWAY_DASHBOARD_CSV.open(newline="") as handle:
        pathway_rows = [
            row
            for row in csv.DictReader(handle)
            if row.get("simulatorMetric") == "lowerCourtCompliance"
        ]
    if len(pathway_rows) != 1:
        fail("pathway dashboard must contain one lowerCourtCompliance row")
    pathway_row = pathway_rows[0]
    if (
        pathway_row["sourceMetric"]
        != "lowerCourtFollowedShareAmongDirectionalTreatments_constitutionalIssues"
    ):
        fail("pathway dashboard is not using the direct aggregate doctrinal-uptake source slice")
    if pathway_row["validationUse"] != "proxy_context":
        fail("pathway dashboard must keep lowerCourtCompliance as proxy context")
    if pathway_row["denominatorCompatibility"] != "scale_mismatch":
        fail("pathway dashboard must preserve the lowerCourtCompliance scale mismatch")
    if int(pathway_row.get("sourceObservations", "0") or 0) != 10:
        fail("pathway dashboard must expose all ten constitutional-issue source terms")
    if "direct_behavior_guardrail" not in pathway_row.get("sourceValidationUse", ""):
        fail("pathway dashboard lost the source row's direct-behavior guardrail label")


def check_certiorari_journal_disposition_extract() -> None:
    if not CERTIORARI_JOURNAL_DISPOSITION_EXTRACT_CSV.exists():
        fail(
            "missing certiorari Journal disposition extract "
            f"{CERTIORARI_JOURNAL_DISPOSITION_EXTRACT_CSV.relative_to(ROOT)}"
        )
    if not CERTIORARI_JOURNAL_DISPOSITION_MANIFEST.exists():
        fail(
            "missing certiorari Journal disposition manifest "
            f"{CERTIORARI_JOURNAL_DISPOSITION_MANIFEST.relative_to(ROOT)}"
        )
    with CERTIORARI_COHORT_SCHEMA_CSV.open(newline="") as handle:
        schema_fields = [row["fieldName"] for row in csv.DictReader(handle)]
    with CERTIORARI_JOURNAL_DISPOSITION_EXTRACT_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if (reader.fieldnames or []) != schema_fields:
            fail("certiorari Journal disposition extract columns do not match cohort schema fieldName order")
        rows = list(reader)
    if not rows:
        fail("certiorari Journal disposition extract has no rows")

    manifest = json.loads(CERTIORARI_JOURNAL_DISPOSITION_MANIFEST.read_text())
    if int(manifest.get("rowCount", -1)) != len(rows):
        fail("certiorari Journal disposition manifest rowCount does not match extract")
    if manifest.get("sourceFileSha256") != manifest.get("expectedSourceFileSha256"):
        fail("certiorari Journal disposition manifest source hash does not match expected official PDF hash")

    disposition_dates = sorted({row.get("dispositionDate", "") for row in rows if row.get("dispositionDate")})
    if len(disposition_dates) < 10:
        fail("certiorari Journal disposition extract has too few distinct disposition dates")
    if disposition_dates[0] != "2023-10-02" or not disposition_dates[-1].startswith("2024-"):
        fail("certiorari Journal disposition extract date range does not match OT2023 Journal coverage")
    if manifest.get("firstDispositionDate") != disposition_dates[0]:
        fail("certiorari Journal disposition manifest firstDispositionDate does not match extract")
    if manifest.get("lastDispositionDate") != disposition_dates[-1]:
        fail("certiorari Journal disposition manifest lastDispositionDate does not match extract")

    allowed_dispositions = {"denied", "granted", "gvr_or_remand", "dismissed", "other_disposition_review_required"}
    allowed_paid_or_ifp = {"paid", "ifp", "application_or_misc", "original", "uncoded"}
    bad_rows: list[str] = []
    review_required = 0
    for row in rows:
        source_id = row.get("sourceRecordId", "")
        if row.get("sourceKey") != "journal-ot2023":
            bad_rows.append(f"{source_id}: unexpected sourceKey")
        if row.get("term") != "OT2023":
            bad_rows.append(f"{source_id}: unexpected term")
        if row.get("sourceUrl") != "https://www.supremecourt.gov/orders/journal/jnl23.pdf":
            bad_rows.append(f"{source_id}: sourceUrl is not the official OT2023 Journal PDF")
        if not row.get("docketNumber"):
            bad_rows.append(f"{source_id}: missing docketNumber")
        if not row.get("dispositionDate"):
            bad_rows.append(f"{source_id}: missing dispositionDate")
        if "petition for writ" in row.get("lowerCourt", "").lower():
            bad_rows.append(f"{source_id}: lowerCourt includes petition prose")
        if row.get("certDisposition") not in allowed_dispositions:
            bad_rows.append(f"{source_id}: unexpected certDisposition {row.get('certDisposition')}")
        if row.get("paidOrIfp") not in allowed_paid_or_ifp:
            bad_rows.append(f"{source_id}: unexpected paidOrIfp {row.get('paidOrIfp')}")
        notes = row.get("coderNotes", "").lower()
        if "not a closed filing cohort" not in notes:
            bad_rows.append(f"{source_id}: coderNotes do not preserve cohort boundary")
        if row.get("certDisposition") == "other_disposition_review_required":
            review_required += 1
    if bad_rows:
        fail("certiorari Journal disposition extract rows require review: " + "; ".join(bad_rows[:10]))

def check_certiorari_journal_disposition_summary() -> None:
    check_csv_schema(
        CERTIORARI_JOURNAL_DISPOSITION_SUMMARY_CSV,
        REQUIRED_CERTIORARI_JOURNAL_DISPOSITION_SUMMARY_COLUMNS,
        "certiorari Journal disposition summary",
    )
    with CERTIORARI_JOURNAL_DISPOSITION_SUMMARY_CSV.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        fail("certiorari Journal disposition summary has no rows")
    allowed_statuses = {
        "candidate_extract",
        "not_expected_to_match_term_flow",
        "review_boundary",
        "manual_review_required",
        "none_remaining",
        "matches_extract_rows",
        "missing_dates",
        "partial_extract",
    }
    by_metric = {row["metricKey"]: row for row in rows}
    required_metrics = {
        "journalCertiorariDispositionRows",
        "journalCertiorariUniqueDockets",
        "journalCertiorariUniqueDispositionDates",
        "journalCertiorariFirstDispositionDate",
        "journalCertiorariLastDispositionDate",
        "journalCertiorariPaidDispositionRows",
        "journalCertiorariIfpDispositionRows",
        "journalCertiorariReviewRequiredRows",
        "journalCertiorariRowsWithDispositionDate",
        "journalCertiorariRowsWithLowerCourt",
    }
    missing_metrics = required_metrics - set(by_metric)
    if missing_metrics:
        fail("certiorari Journal disposition summary is missing metrics: " + ", ".join(sorted(missing_metrics)))
    with CERTIORARI_JOURNAL_DISPOSITION_EXTRACT_CSV.open(newline="") as handle:
        extract_rows = list(csv.DictReader(handle))
    total_row = by_metric["journalCertiorariDispositionRows"]
    if int(total_row["observedValue"]) != len(extract_rows):
        fail("certiorari Journal disposition summary total does not match extract row count")
    bad_statuses = [
        row["metricKey"]
        for row in rows
        if row.get("reconciliationStatus") not in allowed_statuses
    ]
    if bad_statuses:
        fail("certiorari Journal disposition summary has unexpected statuses: " + ", ".join(bad_statuses))
    overclaiming_rows = [
        row["metricKey"]
        for row in rows
        if "not closed filing-cohort validation" not in row.get("manuscriptUse", "")
    ]
    if overclaiming_rows:
        fail(
            "certiorari Journal disposition summary manuscript-use text may overclaim: "
            + ", ".join(overclaiming_rows[:10])
        )


def check_certiorari_journal_docket_detail_extract() -> None:
    if not CERTIORARI_JOURNAL_DOCKET_DETAIL_EXTRACT_CSV.exists():
        fail(
            "missing certiorari Journal docket-detail extract "
            f"{CERTIORARI_JOURNAL_DOCKET_DETAIL_EXTRACT_CSV.relative_to(ROOT)}"
        )
    if not CERTIORARI_JOURNAL_DOCKET_DETAIL_MANIFEST.exists():
        fail(
            "missing certiorari Journal docket-detail manifest "
            f"{CERTIORARI_JOURNAL_DOCKET_DETAIL_MANIFEST.relative_to(ROOT)}"
        )
    with CERTIORARI_COHORT_SCHEMA_CSV.open(newline="") as handle:
        schema_fields = [row["fieldName"] for row in csv.DictReader(handle)]
    with CERTIORARI_JOURNAL_DOCKET_DETAIL_EXTRACT_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if (reader.fieldnames or []) != schema_fields:
            fail("certiorari Journal docket-detail extract columns do not match cohort schema fieldName order")
        rows = list(reader)
    manifest = json.loads(CERTIORARI_JOURNAL_DOCKET_DETAIL_MANIFEST.read_text())
    journal_disposition_rows = int(manifest.get("journalDispositionRows", -1))
    failed_fetch_count = int(manifest.get("failedFetchCount", -1))
    failed_fetches = manifest.get("failedFetches", [])
    if journal_disposition_rows != 3951:
        fail("certiorari Journal docket-detail manifest does not preserve the 3,951-row Journal source denominator")
    if int(manifest.get("rowCount", -1)) != len(rows):
        fail("certiorari Journal docket-detail manifest rowCount does not match extract")
    if failed_fetch_count != len(failed_fetches):
        fail("certiorari Journal docket-detail manifest failedFetchCount does not match failedFetches")
    if len(rows) + failed_fetch_count != journal_disposition_rows:
        fail("certiorari Journal docket-detail manifest rows plus failures do not reconcile to Journal denominator")
    if len(rows) < 3900 or failed_fetch_count > 10:
        fail("certiorari Journal docket-detail extract no longer preserves near-complete static-docket coverage")
    if "not a closed filed-petition cohort" not in " ".join(manifest.get("notes", [])):
        fail("certiorari Journal docket-detail manifest does not preserve the cohort boundary")

    allowed_response = {"yes", "no", "waived"}
    allowed_binary = {"yes", "no"}
    bad_rows: list[str] = []
    petition_dates = 0
    cfr_yes = 0
    cvsg_yes = 0
    amicus_rows = 0
    relisted_rows = 0
    for row in rows:
        source_id = row.get("sourceRecordId", "")
        if row.get("sourceKey") != "scotus-docket-plus-journal-disposition-ot2023":
            bad_rows.append(f"{source_id}: unexpected sourceKey")
        if row.get("term") != "OT2023":
            bad_rows.append(f"{source_id}: unexpected term")
        if not row.get("sourceUrl", "").startswith("https://www.supremecourt.gov/docket/docketfiles/html/public/"):
            bad_rows.append(f"{source_id}: sourceUrl is not an official docket page")
        if not row.get("docketNumber"):
            bad_rows.append(f"{source_id}: missing docketNumber")
        if row.get("responseFiled") not in allowed_response:
            bad_rows.append(f"{source_id}: unexpected responseFiled {row.get('responseFiled')}")
        if row.get("responseRequestedByCourt") not in allowed_binary:
            bad_rows.append(f"{source_id}: unexpected responseRequestedByCourt {row.get('responseRequestedByCourt')}")
        if row.get("cvsgRequested") not in allowed_binary:
            bad_rows.append(f"{source_id}: unexpected cvsgRequested {row.get('cvsgRequested')}")
        if "not a closed filing cohort" not in row.get("coderNotes", ""):
            bad_rows.append(f"{source_id}: coderNotes do not preserve cohort boundary")
        if row.get("petitionFiledDate"):
            petition_dates += 1
        if row.get("responseRequestedByCourt") == "yes":
            cfr_yes += 1
        if row.get("cvsgRequested") == "yes":
            cvsg_yes += 1
        if int(row.get("certStageAmicusCount") or 0) > 0:
            amicus_rows += 1
        if int(row.get("relistCount") or 0) > 0:
            relisted_rows += 1
    if bad_rows:
        fail("certiorari Journal docket-detail extract rows require review: " + "; ".join(bad_rows[:10]))
    if petition_dates < 3900 or cfr_yes < 200 or cvsg_yes < 10 or amicus_rows < 250 or relisted_rows < 500:
        fail("certiorari Journal docket-detail extract is missing expected bounded docket-detail signals")


def check_certiorari_journal_docket_detail_summary() -> None:
    check_csv_schema(
        CERTIORARI_JOURNAL_DOCKET_DETAIL_SUMMARY_CSV,
        REQUIRED_ECTHR_EXECUTION_MONITORING_SUMMARY_COLUMNS,
        "certiorari Journal docket-detail summary",
    )
    with CERTIORARI_JOURNAL_DOCKET_DETAIL_EXTRACT_CSV.open(newline="") as handle:
        extract_rows = list(csv.DictReader(handle))
    with CERTIORARI_JOURNAL_DOCKET_DETAIL_SUMMARY_CSV.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    by_metric = {row["metricKey"]: row for row in rows}
    required_metrics = {
        "certiorariJournalDocketSourceRows",
        "certiorariJournalDocketFailedFetchRows",
        "certiorariJournalDocketDetailRows",
        "certiorariJournalDocketPetitionFiledRows",
        "certiorariJournalDocketResponseFiledRows",
        "certiorariJournalDocketCfrRows",
        "certiorariJournalDocketCvsgRows",
        "certiorariJournalDocketAmicusRows",
        "certiorariJournalDocketRelistedRows",
        "certiorariJournalDocketGrantedRows",
    }
    missing = required_metrics - set(by_metric)
    if missing:
        fail("certiorari Journal docket-detail summary is missing metrics: " + ", ".join(sorted(missing)))
    if int(by_metric["certiorariJournalDocketSourceRows"]["observedValue"]) != 3951:
        fail("certiorari Journal docket-detail summary does not preserve the 3,951-row source denominator")
    manifest = json.loads(CERTIORARI_JOURNAL_DOCKET_DETAIL_MANIFEST.read_text())
    failed_fetch_count = int(manifest.get("failedFetchCount", -1))
    if int(by_metric["certiorariJournalDocketFailedFetchRows"]["observedValue"]) != failed_fetch_count:
        fail("certiorari Journal docket-detail summary failed-fetch count does not match manifest")
    if int(by_metric["certiorariJournalDocketDetailRows"]["observedValue"]) != len(extract_rows):
        fail("certiorari Journal docket-detail summary total does not match extract")
    boundary_phrases = (
        "not closed filed-petition validation",
        "not closed filing-cohort validation",
        "closed-cohort claim",
        "coverage limitation",
        "Journal disposition rows only",
    )
    overclaiming_rows = [
        row["metricKey"]
        for row in rows
        if not any(phrase in row.get("manuscriptUse", "") for phrase in boundary_phrases)
    ]
    if overclaiming_rows:
        fail(
            "certiorari Journal docket-detail summary manuscript-use text may overclaim: "
            + ", ".join(overclaiming_rows[:10])
        )


def check_certiorari_journal_docket_retrieval_workqueue() -> None:
    check_csv_schema(
        CERTIORARI_JOURNAL_DOCKET_RETRIEVAL_WORKQUEUE_CSV,
        REQUIRED_CERTIORARI_JOURNAL_DOCKET_RETRIEVAL_WORKQUEUE_COLUMNS,
        "certiorari Journal docket retrieval workqueue",
    )
    if not CERTIORARI_JOURNAL_DOCKET_RETRIEVAL_WORKQUEUE_MD.exists():
        fail(
            "missing certiorari Journal docket retrieval workqueue markdown "
            f"{CERTIORARI_JOURNAL_DOCKET_RETRIEVAL_WORKQUEUE_MD.relative_to(ROOT)}"
        )
    with CERTIORARI_JOURNAL_DOCKET_RETRIEVAL_WORKQUEUE_CSV.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    manifest = json.loads(CERTIORARI_JOURNAL_DOCKET_DETAIL_MANIFEST.read_text())
    failed_fetches = manifest.get("failedFetches", [])
    if len(rows) != int(manifest.get("failedFetchCount", -1)):
        fail("certiorari Journal docket retrieval workqueue row count does not match failedFetchCount")
    if len(rows) != len(failed_fetches):
        fail("certiorari Journal docket retrieval workqueue row count does not match failedFetches")
    by_source = {
        row["sourceRecordId"]: row
        for row in rows
    }
    if len(by_source) != len(rows):
        fail("certiorari Journal docket retrieval workqueue has duplicate sourceRecordId rows")
    expected_priorities = {
        "priority_1_granted_gvr_crosscheck",
        "priority_2_paid_petition_denominator",
        "priority_3_ifp_petition_denominator",
        "priority_4_dismissed_or_misc_boundary",
    }
    bad_rows: list[str] = []
    for index, failure in enumerate(failed_fetches, start=1):
        row = by_source.get(failure["sourceRecordId"])
        if row is None:
            bad_rows.append(f"{failure['sourceRecordId']}: absent from retrieval workqueue")
            continue
        if row["workQueueRank"] != str(index):
            bad_rows.append(f"{failure['sourceRecordId']}: workQueueRank does not preserve manifest order")
        if row["docketNumber"] != failure["docketNumber"]:
            bad_rows.append(f"{failure['sourceRecordId']}: docketNumber does not match manifest failure")
        if row["staticDocketUrl"] != failure["sourceUrl"]:
            bad_rows.append(f"{failure['sourceRecordId']}: staticDocketUrl does not match manifest failure")
        if row["failedFetchError"] != failure["error"]:
            bad_rows.append(f"{failure['sourceRecordId']}: failedFetchError does not match manifest failure")
        if not row["staticDocketUrl"].startswith("https://www.supremecourt.gov/docket/docketfiles/html/public/"):
            bad_rows.append(f"{failure['sourceRecordId']}: not an official static docket URL")
        if row["retrievalPriority"] not in expected_priorities:
            bad_rows.append(f"{failure['sourceRecordId']}: unexpected retrievalPriority")
        if "official docket" not in row["retrievalAction"]:
            bad_rows.append(f"{failure['sourceRecordId']}: retrievalAction does not require official docket recovery")
        if "not validation evidence" not in row["manuscriptUse"]:
            bad_rows.append(f"{failure['sourceRecordId']}: manuscriptUse may overclaim")
        if "closed filed-petition validation" not in row["manuscriptUse"]:
            bad_rows.append(f"{failure['sourceRecordId']}: manuscriptUse does not preserve closed-cohort boundary")
    if bad_rows:
        fail("certiorari Journal docket retrieval workqueue rows require review: " + "; ".join(bad_rows[:10]))
    markdown = CERTIORARI_JOURNAL_DOCKET_RETRIEVAL_WORKQUEUE_MD.read_text()
    expected_queue_line = f"Rows needing retrieval: {len(failed_fetches)}"
    for required in (expected_queue_line, "not validation evidence", "Journal disposition rows only"):
        if required not in markdown:
            fail("certiorari Journal docket retrieval workqueue markdown is missing boundary text: " + required)


def check_certiorari_term_flow_term(
    extract_path: Path,
    manifest_path: Path,
    term: str,
    source_key: str,
    expected_source_hash: str,
    expected_counts: dict[str, int],
) -> None:
    check_csv_schema(
        extract_path,
        REQUIRED_CERTIORARI_TERM_FLOW_EXTRACT_COLUMNS,
        f"{term} certiorari term-flow extract",
    )
    if not manifest_path.exists():
        fail(f"missing {term} certiorari term-flow manifest")
    with extract_path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    manifest = json.loads(manifest_path.read_text())
    if len(rows) != 22 or int(manifest.get("rowCount", -1)) != len(rows):
        fail(f"{term} certiorari term-flow extract must contain 22 statistics rows")
    if manifest.get("term") != term or manifest.get("sourceKey") != source_key:
        fail(f"{term} certiorari term-flow manifest has unexpected source identity")
    if manifest.get("sourceFileSha256") != expected_source_hash:
        fail(f"{term} certiorari term-flow source hash changed without review")
    if not str(manifest.get("sourceUrl", "")).startswith(
        "https://www.supremecourt.gov/orders/journal/"
    ):
        fail(f"{term} certiorari term-flow manifest does not cite the official Journal")
    official_counts = manifest.get("officialCounts", {})
    for statistic_key, expected in expected_counts.items():
        if int(official_counts.get(statistic_key, -1)) != expected:
            fail(
                f"{term} certiorari term-flow official count changed for "
                f"{statistic_key}"
            )
    by_key: dict[str, dict[str, str]] = {}
    bad_rows: list[str] = []
    for row in rows:
        statistic_key = row.get("statisticKey", "")
        if not statistic_key or statistic_key in by_key:
            bad_rows.append(f"{statistic_key or '<blank>'}: duplicate or blank statisticKey")
            continue
        by_key[statistic_key] = row
        if row.get("term") != term or row.get("sourceKey") != source_key:
            bad_rows.append(f"{statistic_key}: unexpected term or sourceKey")
        if row.get("sourceFileSha256") != expected_source_hash:
            bad_rows.append(f"{statistic_key}: source hash does not match manifest")
        if not row.get("sourceRecordId"):
            bad_rows.append(f"{statistic_key}: missing sourceRecordId")
        try:
            official_count = int(row["officialCount"])
        except ValueError:
            bad_rows.append(f"{statistic_key}: invalid officialCount")
            continue
        if int(official_counts.get(statistic_key, -1)) != official_count:
            bad_rows.append(f"{statistic_key}: row count does not match manifest")
        denominator_text = row.get("denominatorCount", "")
        value_text = row.get("normalizedObservedValue", "")
        if denominator_text or value_text:
            try:
                denominator = int(denominator_text)
                value = float(value_text)
            except ValueError:
                bad_rows.append(f"{statistic_key}: invalid normalized ratio")
            else:
                if denominator <= 0 or abs(value - official_count / denominator) > 1e-6:
                    bad_rows.append(f"{statistic_key}: normalized ratio mismatch")
    if set(by_key) != set(official_counts):
        fail(f"{term} certiorari term-flow rows do not match manifest statistics")
    if bad_rows:
        fail(f"{term} certiorari term-flow rows require review: " + "; ".join(bad_rows[:10]))
    if "not a closed petition-cohort dataset" not in " ".join(manifest.get("notes", [])):
        fail(f"{term} certiorari term-flow manifest omits the cohort boundary")


def check_certiorari_docketed_cohort() -> None:
    if not CERTIORARI_DOCKETED_COHORT_EXTRACT_CSV.exists():
        fail(
            "missing certiorari docketed-cohort extract "
            f"{CERTIORARI_DOCKETED_COHORT_EXTRACT_CSV.relative_to(ROOT)}"
        )
    if not CERTIORARI_DOCKETED_COHORT_MANIFEST.exists():
        fail(
            "missing certiorari docketed-cohort manifest "
            f"{CERTIORARI_DOCKETED_COHORT_MANIFEST.relative_to(ROOT)}"
        )
    with CERTIORARI_COHORT_SCHEMA_CSV.open(newline="") as handle:
        schema_fields = [row["fieldName"] for row in csv.DictReader(handle)]
    with CERTIORARI_DOCKETED_COHORT_EXTRACT_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if (reader.fieldnames or []) != schema_fields:
            fail("certiorari docketed-cohort columns do not match cohort schema fieldName order")
        rows = list(reader)
    manifest = json.loads(CERTIORARI_DOCKETED_COHORT_MANIFEST.read_text())
    if len(rows) != 4222 or int(manifest.get("expectedRowCount", -1)) != 4222:
        fail("certiorari docketed cohort does not preserve the 4,222-row official denominator")
    if int(manifest.get("rowCount", -1)) != len(rows):
        fail("certiorari docketed-cohort manifest rowCount does not match extract")
    if int(manifest.get("uniqueDocketCount", -1)) != 4222:
        fail("certiorari docketed-cohort manifest uniqueDocketCount is not 4,222")
    if int(manifest.get("failedFetchCount", -1)) != 0 or manifest.get("failedFetches"):
        fail("certiorari docketed cohort reports failed official docket fetches")
    enumeration = manifest.get("enumerationRule", {})
    expected_enumeration = {
        "paid": {"firstDocket": "23-1", "lastDocket": "23-1375", "officialCount": 1375},
        "ifp": {"firstDocket": "23-5001", "lastDocket": "23-7847", "officialCount": 2847},
    }
    if enumeration != expected_enumeration:
        fail("certiorari docketed-cohort manifest enumeration rule does not match official OT2023 counts")
    expected_dockets = {
        *(f"23-{number}" for number in range(1, 1376)),
        *(f"23-{number}" for number in range(5001, 7848)),
    }
    docket_numbers = [row["docketNumber"] for row in rows]
    if len(set(docket_numbers)) != len(rows) or set(docket_numbers) != expected_dockets:
        fail("certiorari docketed cohort does not contain each expected paid/IFP docket exactly once")
    expected_hash = hashlib.sha256(
        json.dumps(rows, sort_keys=True, ensure_ascii=True).encode("utf-8")
    ).hexdigest()
    if manifest.get("sourceRecordSha256") != expected_hash:
        fail("certiorari docketed-cohort manifest sourceRecordSha256 does not match extract")
    if "not a census of submissions that were never docketed" not in " ".join(manifest.get("notes", [])):
        fail("certiorari docketed-cohort manifest does not preserve the undocketed-submission boundary")

    allowed_petition_types = {
        "certiorari",
        "appeal_or_jurisdictional_statement",
        "extraordinary_writ",
        "uncoded_or_no_primary_filing",
    }
    allowed_dispositions = {
        "denied",
        "dismissed",
        "granted",
        "gvr_or_remand",
        "ifp_fee_denied_closed",
        "removed_from_docket",
        "quorum_affirmance",
        "not_certiorari_intake",
    }
    final_cert_dispositions = allowed_dispositions - {"not_certiorari_intake"}
    cert_rows: list[dict[str, str]] = []
    bad_rows: list[str] = []
    for row in rows:
        docket_number = row["docketNumber"]
        number = int(docket_number.split("-", 1)[1])
        expected_class = "paid" if number <= 1375 else "ifp"
        if row.get("sourceKey") != "scotus-certiorari-docketed-cohort-ot2023":
            bad_rows.append(f"{docket_number}: unexpected sourceKey")
        if row.get("sourceRecordId") != f"docket:{docket_number}; cohort:OT2023-paid-ifp-docketed":
            bad_rows.append(f"{docket_number}: unstable sourceRecordId")
        if row.get("sourceUrl") != (
            "https://www.supremecourt.gov/docket/docketfiles/html/public/"
            f"{docket_number}.html"
        ):
            bad_rows.append(f"{docket_number}: sourceUrl does not match official docket")
        if row.get("term") != "OT2023":
            bad_rows.append(f"{docket_number}: unexpected term")
        if row.get("paidOrIfp") != expected_class:
            bad_rows.append(f"{docket_number}: paidOrIfp does not match docket range")
        if row.get("petitionType") not in allowed_petition_types:
            bad_rows.append(f"{docket_number}: unexpected petitionType")
        if row.get("certDisposition") not in allowed_dispositions:
            bad_rows.append(f"{docket_number}: unexpected certDisposition")
        if row.get("responseFiled") not in {"yes", "no", "waived"}:
            bad_rows.append(f"{docket_number}: unexpected responseFiled")
        if row.get("responseRequestedByCourt") not in {"yes", "no"}:
            bad_rows.append(f"{docket_number}: unexpected responseRequestedByCourt")
        if row.get("cvsgRequested") not in {"yes", "no"}:
            bad_rows.append(f"{docket_number}: unexpected cvsgRequested")
        if row.get("responseRequestedByCourt") == "yes" and not row.get("cfrDate"):
            bad_rows.append(f"{docket_number}: CFR row lacks cfrDate")
        if row.get("cvsgRequested") == "yes" and not row.get("cvsgDate"):
            bad_rows.append(f"{docket_number}: CVSG row lacks cvsgDate")
        if "docketed-intake cohort" not in row.get("coderNotes", ""):
            bad_rows.append(f"{docket_number}: coderNotes omit cohort boundary")
        if row["petitionType"] == "certiorari":
            cert_rows.append(row)
            if not row.get("petitionFiledDate"):
                bad_rows.append(f"{docket_number}: certiorari row lacks petitionFiledDate")
            if not row.get("lowerCourt"):
                bad_rows.append(f"{docket_number}: certiorari row lacks lowerCourt")
            if row["certDisposition"] not in final_cert_dispositions:
                bad_rows.append(f"{docket_number}: certiorari outcome is not mature")
            expected_granted = (
                "yes"
                if row["certDisposition"] in {"granted", "gvr_or_remand"}
                else "no"
            )
            if row.get("granted") != expected_granted:
                bad_rows.append(f"{docket_number}: granted flag disagrees with outcome")
            expected_gvr = "yes" if row["certDisposition"] == "gvr_or_remand" else "no"
            if row.get("gvrOrSummaryDisposition") != expected_gvr:
                bad_rows.append(f"{docket_number}: GVR flag disagrees with outcome")
    if bad_rows:
        fail("certiorari docketed-cohort rows require review: " + "; ".join(bad_rows[:10]))
    if len(cert_rows) != 4033:
        fail("certiorari docketed cohort does not preserve the 4,033-row certiorari subset")
    paid_cert = [row for row in cert_rows if row["paidOrIfp"] == "paid"]
    ifp_cert = [row for row in cert_rows if row["paidOrIfp"] == "ifp"]
    if len(paid_cert) != 1343 or len(ifp_cert) != 2690:
        fail("certiorari docketed cohort paid/IFP certiorari subsets changed without review")
    if sum(row["responseRequestedByCourt"] == "yes" for row in paid_cert) != 169:
        fail("certiorari docketed cohort paid CFR count changed without review")
    if sum(row["responseRequestedByCourt"] == "yes" for row in ifp_cert) != 69:
        fail("certiorari docketed cohort IFP CFR count changed without review")
    if sum(row["cvsgRequested"] == "yes" for row in cert_rows) != 10:
        fail("certiorari docketed cohort CVSG count changed without review")
    if sum(int(row["certStageAmicusCount"] or "0") > 0 for row in cert_rows) != 305:
        fail("certiorari docketed cohort amicus-presence count changed without review")
    if sum(int(row["relistCount"] or "0") > 0 for row in cert_rows) != 566:
        fail("certiorari docketed cohort relist count changed without review")
    if sum(row["granted"] == "yes" for row in cert_rows) != 135:
        fail("certiorari docketed cohort grant/GVR count changed without review")


def check_certiorari_docketed_cohort_summary_and_calibration() -> None:
    check_csv_schema(
        CERTIORARI_DOCKETED_COHORT_SUMMARY_CSV,
        REQUIRED_ECTHR_EXECUTION_MONITORING_SUMMARY_COLUMNS,
        "certiorari docketed-cohort summary",
    )
    with CERTIORARI_DOCKETED_COHORT_EXTRACT_CSV.open(newline="") as handle:
        extract_rows = list(csv.DictReader(handle))
    cert_rows = [row for row in extract_rows if row["petitionType"] == "certiorari"]
    paid_cert = [row for row in cert_rows if row["paidOrIfp"] == "paid"]
    ifp_cert = [row for row in cert_rows if row["paidOrIfp"] == "ifp"]
    with CERTIORARI_DOCKETED_COHORT_SUMMARY_CSV.open(newline="") as handle:
        summary_rows = list(csv.DictReader(handle))
    by_metric = {row["metricKey"]: row for row in summary_rows}
    expected_summary = {
        "certiorariDocketedCohortExpectedRows": 4222,
        "certiorariDocketedCohortRows": 4222,
        "certiorariDocketedCohortFailedFetchRows": 0,
        "certiorariDocketedCohortPaidRows": 1375,
        "certiorariDocketedCohortIfpRows": 2847,
        "certiorariDocketedCohortCertPetitionRows": 4033,
        "certiorariDocketedCohortPetitionFiledDateRows": 4033,
        "certiorariDocketedCohortResponseFiledOrWaivedRows": 4033,
        "certiorariDocketedCohortPaidCfrRows": 169,
        "certiorariDocketedCohortIfpCfrRows": 69,
        "certiorariDocketedCohortCvsgRows": 10,
        "certiorariDocketedCohortAmicusRows": 305,
        "certiorariDocketedCohortRelistedRows": 566,
        "certiorariDocketedCohortGrantedRows": 69,
        "certiorariDocketedCohortGvrRows": 66,
        "certiorariDocketedCohortDeniedRows": 3791,
        "certiorariDocketedCohortDismissedRows": 82,
        "certiorariDocketedCohortOtherClosedRows": 25,
        "certiorariDocketedCohortPendingOrUnresolvedRows": 0,
    }
    missing = set(expected_summary) - set(by_metric)
    if missing:
        fail("certiorari docketed-cohort summary is missing metrics: " + ", ".join(sorted(missing)))
    mismatches = [
        metric
        for metric, expected in expected_summary.items()
        if int(by_metric[metric]["observedValue"]) != expected
    ]
    if mismatches:
        fail("certiorari docketed-cohort summary values changed without review: " + ", ".join(mismatches))

    check_csv_schema(
        CERTIORARI_DOCKETED_COHORT_CALIBRATION_CSV,
        REQUIRED_NORMALIZED_CALIBRATION_COLUMNS,
        "certiorari docketed-cohort calibration",
    )
    with CERTIORARI_DOCKETED_COHORT_CALIBRATION_CSV.open(newline="") as handle:
        calibration_rows = list(csv.DictReader(handle))
    calibration = {row["metric"]: row for row in calibration_rows}
    expected_rates = {
        "paidPetitionShare": (1375, 4222),
        "ifpPetitionShare": (2847, 4222),
        "cfrRate_paid": (169, len(paid_cert)),
        "cfrRate_ifp": (69, len(ifp_cert)),
        "cvsgRequestRate": (10, len(cert_rows)),
        "certStageAmicusPresenceRate": (305, len(cert_rows)),
        "relistRate": (566, len(cert_rows)),
        "certiorariGrantRate_docketedCohort": (135, len(cert_rows)),
    }
    if set(calibration) != set(expected_rates):
        fail("certiorari docketed-cohort calibration metric set changed without review")
    for metric, (numerator, denominator) in expected_rates.items():
        row = calibration[metric]
        if row.get("sourceKey") != "scotus-certiorari-docketed-cohort-ot2023":
            fail(f"certiorari docketed-cohort calibration {metric} has unexpected sourceKey")
        if int(row["numerator"]) != numerator or int(row["denominator"]) != denominator:
            fail(f"certiorari docketed-cohort calibration {metric} numerator/denominator mismatch")
        if abs(float(row["value"]) - numerator / denominator) > 1e-8:
            fail(f"certiorari docketed-cohort calibration {metric} value mismatch")


def check_certiorari_docketed_cohort_ot2024() -> None:
    if not CERTIORARI_DOCKETED_COHORT_OT2024_EXTRACT_CSV.exists():
        fail("missing OT2024 certiorari docketed-cohort extract")
    if not CERTIORARI_DOCKETED_COHORT_OT2024_MANIFEST.exists():
        fail("missing OT2024 certiorari docketed-cohort manifest")
    with CERTIORARI_COHORT_SCHEMA_CSV.open(newline="") as handle:
        schema_fields = [row["fieldName"] for row in csv.DictReader(handle)]
    with CERTIORARI_DOCKETED_COHORT_OT2024_EXTRACT_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if (reader.fieldnames or []) != schema_fields:
            fail("OT2024 certiorari cohort columns do not match cohort schema")
        rows = list(reader)
    manifest = json.loads(CERTIORARI_DOCKETED_COHORT_OT2024_MANIFEST.read_text())
    if len(rows) != 3854 or int(manifest.get("expectedRowCount", -1)) != 3854:
        fail("OT2024 certiorari cohort does not preserve the 3,854-row denominator")
    if int(manifest.get("rowCount", -1)) != len(rows):
        fail("OT2024 certiorari cohort manifest rowCount does not match extract")
    if int(manifest.get("uniqueDocketCount", -1)) != 3854:
        fail("OT2024 certiorari cohort uniqueDocketCount is not 3,854")
    if int(manifest.get("failedFetchCount", -1)) != 0 or manifest.get("failedFetches"):
        fail("OT2024 certiorari cohort reports failed official docket fetches")
    expected_enumeration = {
        "paid": {"firstDocket": "24-1", "lastDocket": "24-1327", "officialCount": 1327},
        "ifp": {"firstDocket": "24-5001", "lastDocket": "24-7527", "officialCount": 2527},
    }
    if manifest.get("enumerationRule") != expected_enumeration:
        fail("OT2024 certiorari cohort enumeration does not match Journal counts")
    expected_dockets = {
        *(f"24-{number}" for number in range(1, 1328)),
        *(f"24-{number}" for number in range(5001, 7528)),
    }
    docket_numbers = [row["docketNumber"] for row in rows]
    if len(set(docket_numbers)) != len(rows) or set(docket_numbers) != expected_dockets:
        fail("OT2024 certiorari cohort does not contain each count-defined docket once")
    expected_hash = hashlib.sha256(
        json.dumps(rows, sort_keys=True, ensure_ascii=True).encode("utf-8")
    ).hexdigest()
    if manifest.get("sourceRecordSha256") != expected_hash:
        fail("OT2024 certiorari cohort sourceRecordSha256 does not match extract")

    boundary_policy = manifest.get("boundaryPolicy", {})
    if int(boundary_policy.get("excludedDocketCount", -1)) != 4:
        fail("OT2024 certiorari cohort boundary policy does not report four exclusions")
    if "published paid and IFP counts" not in boundary_policy.get("basis", ""):
        fail("OT2024 certiorari cohort boundary policy omits the count basis")
    if "not every public docket" not in boundary_policy.get("calendarDateCaveat", ""):
        fail("OT2024 certiorari cohort boundary policy omits the calendar-date caveat")
    expected_exclusions = {
        (
            docket,
            "2025-06-30",
            paid_or_ifp,
            f"https://www.supremecourt.gov/docket/docketfiles/html/public/{docket}.html",
        )
        for docket, paid_or_ifp in (
            ("24-1328", "paid"),
            ("24-1329", "paid"),
            ("24-7528", "ifp"),
            ("24-7529", "ifp"),
        )
    }
    exclusions = manifest.get("boundaryExclusions", [])
    actual_exclusions = {
        (
            item.get("docketNumber"),
            item.get("docketedDate"),
            item.get("paidOrIfp"),
            item.get("sourceUrl"),
        )
        for item in exclusions
    }
    if actual_exclusions != expected_exclusions:
        fail("OT2024 certiorari cohort boundary exclusions changed without review")
    if any("published-statistics snapshot" not in item.get("reason", "") for item in exclusions):
        fail("OT2024 certiorari cohort exclusions omit the snapshot rationale")
    notes = " ".join(manifest.get("notes", []))
    for phrase in (
        "same-day dockets above those count boundaries",
        "not a census of submissions that were never docketed",
    ):
        if phrase not in notes:
            fail(f"OT2024 certiorari cohort manifest omits boundary text: {phrase}")

    allowed_petition_types = {
        "certiorari",
        "appeal_or_jurisdictional_statement",
        "extraordinary_writ",
        "uncoded_or_no_primary_filing",
    }
    allowed_dispositions = {
        "denied",
        "dismissed",
        "granted",
        "gvr_or_remand",
        "ifp_fee_denied_closed",
        "removed_from_docket",
        "quorum_affirmance",
        "not_certiorari_intake",
        "pending_or_unresolved",
    }
    resolved_dispositions = allowed_dispositions - {
        "not_certiorari_intake",
        "pending_or_unresolved",
    }
    cert_rows: list[dict[str, str]] = []
    bad_rows: list[str] = []
    for row in rows:
        docket_number = row["docketNumber"]
        number = int(docket_number.split("-", 1)[1])
        expected_class = "paid" if number <= 1327 else "ifp"
        if row.get("sourceKey") != "scotus-certiorari-docketed-cohort-ot2024":
            bad_rows.append(f"{docket_number}: unexpected sourceKey")
        if row.get("sourceRecordId") != f"docket:{docket_number}; cohort:OT2024-paid-ifp-docketed":
            bad_rows.append(f"{docket_number}: unstable sourceRecordId")
        expected_url = (
            "https://www.supremecourt.gov/docket/docketfiles/html/public/"
            f"{docket_number}.html"
        )
        if row.get("sourceUrl") != expected_url:
            bad_rows.append(f"{docket_number}: sourceUrl does not match official docket")
        if row.get("term") != "OT2024" or row.get("paidOrIfp") != expected_class:
            bad_rows.append(f"{docket_number}: unexpected term or paid/IFP class")
        if row.get("petitionType") not in allowed_petition_types:
            bad_rows.append(f"{docket_number}: unexpected petitionType")
        if row.get("certDisposition") not in allowed_dispositions:
            bad_rows.append(f"{docket_number}: unexpected certDisposition")
        if row.get("responseFiled") not in {"yes", "no", "waived"}:
            bad_rows.append(f"{docket_number}: unexpected responseFiled")
        if row.get("responseRequestedByCourt") not in {"yes", "no"}:
            bad_rows.append(f"{docket_number}: unexpected responseRequestedByCourt")
        if row.get("cvsgRequested") not in {"yes", "no"}:
            bad_rows.append(f"{docket_number}: unexpected cvsgRequested")
        if row.get("responseRequestedByCourt") == "yes" and not row.get("cfrDate"):
            bad_rows.append(f"{docket_number}: CFR row lacks cfrDate")
        if row.get("cvsgRequested") == "yes" and not row.get("cvsgDate"):
            bad_rows.append(f"{docket_number}: CVSG row lacks cvsgDate")
        for field in (
            "petitionFiledDate",
            "cfrDate",
            "cvsgDate",
            "dispositionDate",
            "meritsDecisionDate",
        ):
            value = row.get(field, "")
            if value:
                try:
                    date.fromisoformat(value)
                except ValueError:
                    bad_rows.append(f"{docket_number}: invalid {field}")
        if "docketed-intake cohort" not in row.get("coderNotes", ""):
            bad_rows.append(f"{docket_number}: coderNotes omit cohort boundary")
        if row["petitionType"] != "certiorari":
            if row["certDisposition"] != "not_certiorari_intake":
                bad_rows.append(f"{docket_number}: non-certiorari row has cert disposition")
            continue
        cert_rows.append(row)
        if not row.get("petitionFiledDate") or not row.get("lowerCourt"):
            bad_rows.append(f"{docket_number}: certiorari row lacks filing or lower-court data")
        if row["certDisposition"] == "pending_or_unresolved":
            if row.get("dispositionDate") or row.get("granted") or row.get("gvrOrSummaryDisposition"):
                bad_rows.append(f"{docket_number}: pending row has final-outcome fields")
            continue
        if row["certDisposition"] not in resolved_dispositions:
            bad_rows.append(f"{docket_number}: certiorari row has non-final disposition")
            continue
        expected_granted = (
            "yes" if row["certDisposition"] in {"granted", "gvr_or_remand"} else "no"
        )
        expected_gvr = "yes" if row["certDisposition"] == "gvr_or_remand" else "no"
        if row.get("granted") != expected_granted:
            bad_rows.append(f"{docket_number}: granted flag disagrees with outcome")
        if row.get("gvrOrSummaryDisposition") != expected_gvr:
            bad_rows.append(f"{docket_number}: GVR flag disagrees with outcome")
        if not row.get("dispositionDate"):
            bad_rows.append(f"{docket_number}: resolved row lacks dispositionDate")
    if bad_rows:
        fail("OT2024 certiorari cohort rows require review: " + "; ".join(bad_rows[:10]))
    if len(cert_rows) != 3683:
        fail("OT2024 certiorari cohort does not preserve the 3,683-row petition subset")
    paid_cert = [row for row in cert_rows if row["paidOrIfp"] == "paid"]
    ifp_cert = [row for row in cert_rows if row["paidOrIfp"] == "ifp"]
    resolved_cert = [
        row for row in cert_rows if row["certDisposition"] != "pending_or_unresolved"
    ]
    pending_dockets = {
        row["docketNumber"]
        for row in cert_rows
        if row["certDisposition"] == "pending_or_unresolved"
    }
    if len(paid_cert) != 1292 or len(ifp_cert) != 2391:
        fail("OT2024 paid/IFP certiorari subset counts changed without review")
    if len(resolved_cert) != 3680 or pending_dockets != {"24-969", "24-999", "24-1030"}:
        fail("OT2024 pending/resolved certiorari boundary changed without review")
    expected_signals = {
        "paid CFR": sum(row["responseRequestedByCourt"] == "yes" for row in paid_cert),
        "IFP CFR": sum(row["responseRequestedByCourt"] == "yes" for row in ifp_cert),
        "CVSG": sum(row["cvsgRequested"] == "yes" for row in cert_rows),
        "amicus": sum(int(row["certStageAmicusCount"] or "0") > 0 for row in cert_rows),
        "relist": sum(int(row["relistCount"] or "0") > 0 for row in cert_rows),
        "grant/GVR": sum(row["granted"] == "yes" for row in resolved_cert),
    }
    expected_signal_values = {
        "paid CFR": 189,
        "IFP CFR": 75,
        "CVSG": 20,
        "amicus": 313,
        "relist": 409,
        "grant/GVR": 114,
    }
    if expected_signals != expected_signal_values:
        fail("OT2024 certiorari cohort signal counts changed: " + repr(expected_signals))
    disposition_counts = {
        disposition: sum(row["certDisposition"] == disposition for row in rows)
        for disposition in allowed_dispositions
    }
    disposition_counts = {key: value for key, value in disposition_counts.items() if value}
    if disposition_counts != manifest.get("dispositionCounts"):
        fail("OT2024 certiorari cohort disposition counts do not match manifest")


def check_certiorari_docketed_cohort_ot2024_summary_and_calibration() -> None:
    check_csv_schema(
        CERTIORARI_DOCKETED_COHORT_OT2024_SUMMARY_CSV,
        REQUIRED_ECTHR_EXECUTION_MONITORING_SUMMARY_COLUMNS,
        "OT2024 certiorari docketed-cohort summary",
    )
    with CERTIORARI_DOCKETED_COHORT_OT2024_EXTRACT_CSV.open(newline="") as handle:
        extract_rows = list(csv.DictReader(handle))
    cert_rows = [row for row in extract_rows if row["petitionType"] == "certiorari"]
    paid_cert = [row for row in cert_rows if row["paidOrIfp"] == "paid"]
    ifp_cert = [row for row in cert_rows if row["paidOrIfp"] == "ifp"]
    resolved_cert = [
        row for row in cert_rows if row["certDisposition"] != "pending_or_unresolved"
    ]
    with CERTIORARI_DOCKETED_COHORT_OT2024_SUMMARY_CSV.open(newline="") as handle:
        summary = {row["metricKey"]: row for row in csv.DictReader(handle)}
    expected_summary = {
        "certiorariDocketedCohortExpectedRows": 3854,
        "certiorariDocketedCohortRows": 3854,
        "certiorariDocketedCohortFailedFetchRows": 0,
        "certiorariDocketedCohortPaidRows": 1327,
        "certiorariDocketedCohortIfpRows": 2527,
        "certiorariDocketedCohortCertPetitionRows": 3683,
        "certiorariDocketedCohortPetitionFiledDateRows": 3683,
        "certiorariDocketedCohortResponseFiledOrWaivedRows": 3681,
        "certiorariDocketedCohortPaidCfrRows": 189,
        "certiorariDocketedCohortIfpCfrRows": 75,
        "certiorariDocketedCohortCvsgRows": 20,
        "certiorariDocketedCohortAmicusRows": 313,
        "certiorariDocketedCohortRelistedRows": 409,
        "certiorariDocketedCohortGrantedRows": 62,
        "certiorariDocketedCohortGvrRows": 52,
        "certiorariDocketedCohortDeniedRows": 3463,
        "certiorariDocketedCohortDismissedRows": 71,
        "certiorariDocketedCohortOtherClosedRows": 32,
        "certiorariDocketedCohortPendingOrUnresolvedRows": 3,
    }
    if set(expected_summary) - set(summary):
        fail("OT2024 certiorari summary is missing required metrics")
    mismatches = [
        metric
        for metric, expected in expected_summary.items()
        if int(summary[metric]["observedValue"]) != expected
    ]
    if mismatches:
        fail("OT2024 certiorari summary values changed: " + ", ".join(mismatches))

    check_csv_schema(
        CERTIORARI_DOCKETED_COHORT_OT2024_CALIBRATION_CSV,
        REQUIRED_NORMALIZED_CALIBRATION_COLUMNS,
        "OT2024 certiorari docketed-cohort calibration",
    )
    with CERTIORARI_DOCKETED_COHORT_OT2024_CALIBRATION_CSV.open(newline="") as handle:
        calibration = {row["metric"]: row for row in csv.DictReader(handle)}
    expected_rates = {
        "paidPetitionShare": (1327, 3854),
        "ifpPetitionShare": (2527, 3854),
        "cfrRate_paid": (189, len(paid_cert)),
        "cfrRate_ifp": (75, len(ifp_cert)),
        "cvsgRequestRate": (20, len(cert_rows)),
        "certStageAmicusPresenceRate": (313, len(cert_rows)),
        "relistRate": (409, len(cert_rows)),
        "certiorariGrantRate_docketedCohort": (114, len(resolved_cert)),
    }
    if set(calibration) != set(expected_rates):
        fail("OT2024 certiorari calibration metric set changed without review")
    for metric, (numerator, denominator) in expected_rates.items():
        row = calibration[metric]
        if row.get("sourceKey") != "scotus-certiorari-docketed-cohort-ot2024":
            fail(f"OT2024 certiorari calibration {metric} has unexpected sourceKey")
        if row.get("term") != "OT2024":
            fail(f"OT2024 certiorari calibration {metric} has unexpected term")
        if int(row["numerator"]) != numerator or int(row["denominator"]) != denominator:
            fail(f"OT2024 certiorari calibration {metric} ratio counts do not reconcile")
        if abs(float(row["value"]) - numerator / denominator) > 1e-8:
            fail(f"OT2024 certiorari calibration {metric} value does not reconcile")
    grant_notes = calibration["certiorariGrantRate_docketedCohort"].get("notes", "")
    if "resolved certiorari petitions" not in grant_notes:
        fail("OT2024 certiorari grant calibration omits the resolved-petition denominator")


def check_certiorari_multi_term_benchmark() -> None:
    check_csv_schema(
        CERTIORARI_MULTI_TERM_BENCHMARK_CSV,
        REQUIRED_CERTIORARI_MULTI_TERM_COLUMNS,
        "certiorari multi-term benchmark",
    )
    calibration_by_term: dict[str, dict[str, dict[str, str]]] = {}
    for path in (
        CERTIORARI_DOCKETED_COHORT_CALIBRATION_CSV,
        CERTIORARI_DOCKETED_COHORT_OT2024_CALIBRATION_CSV,
    ):
        with path.open(newline="") as handle:
            rows = list(csv.DictReader(handle))
        terms = {row["term"] for row in rows}
        if len(terms) != 1:
            fail(f"{path.relative_to(ROOT)} does not contain exactly one term")
        calibration_by_term[next(iter(terms))] = {row["metric"]: row for row in rows}
    if set(calibration_by_term) != {"OT2023", "OT2024"}:
        fail("certiorari multi-term source files do not preserve OT2023 and OT2024")
    metric_sets = {frozenset(rows) for rows in calibration_by_term.values()}
    if len(metric_sets) != 1:
        fail("certiorari multi-term source files do not share one metric set")
    with CERTIORARI_MULTI_TERM_BENCHMARK_CSV.open(newline="") as handle:
        report_rows = list(csv.DictReader(handle))
    report = {row["metric"]: row for row in report_rows}
    metrics = set(next(iter(metric_sets)))
    if len(report_rows) != len(report) or set(report) != metrics or len(report) != 8:
        fail("certiorari multi-term report metric set does not reconcile")
    for metric in sorted(metrics):
        first = calibration_by_term["OT2023"][metric]
        latest = calibration_by_term["OT2024"][metric]
        expected_first = float(first["value"])
        expected_latest = float(latest["value"])
        pooled_numerator = int(first["numerator"]) + int(latest["numerator"])
        pooled_denominator = int(first["denominator"]) + int(latest["denominator"])
        expected_pooled = pooled_numerator / pooled_denominator
        row = report[metric]
        integer_expectations = {
            "termCount": 2,
            "firstNumerator": int(first["numerator"]),
            "firstDenominator": int(first["denominator"]),
            "latestNumerator": int(latest["numerator"]),
            "latestDenominator": int(latest["denominator"]),
            "pooledNumerator": pooled_numerator,
            "pooledDenominator": pooled_denominator,
        }
        for field, expected in integer_expectations.items():
            if int(row[field]) != expected:
                fail(f"certiorari multi-term {metric} has unexpected {field}")
        float_expectations = {
            "firstValue": expected_first,
            "latestValue": expected_latest,
            "absoluteChange": expected_latest - expected_first,
            "rangeAcrossTerms": abs(expected_latest - expected_first),
            "pooledValue": expected_pooled,
        }
        for field, expected in float_expectations.items():
            if abs(float(row[field]) - expected) > 1e-8:
                fail(f"certiorari multi-term {metric} has unexpected {field}")
        if row.get("firstTerm") != "OT2023" or row.get("latestTerm") != "OT2024":
            fail(f"certiorari multi-term {metric} has unexpected term endpoints")
        if row.get("terms") != "OT2023;OT2024":
            fail(f"certiorari multi-term {metric} has unexpected term list")
        expected_keys = f"{first['sourceKey']};{latest['sourceKey']}"
        if row.get("sourceKeys") != expected_keys:
            fail(f"certiorari multi-term {metric} has unexpected source keys")
        for phrase in (
            "descriptive multi-term docketed-intake benchmark",
            "not constitutional-review-only",
            "census of undocketed submissions",
        ):
            if phrase not in row.get("manuscriptUse", ""):
                fail(f"certiorari multi-term {metric} omits boundary text: {phrase}")
    if not CERTIORARI_MULTI_TERM_BENCHMARK_MD.exists():
        fail("missing certiorari multi-term benchmark markdown")
    markdown = CERTIORARI_MULTI_TERM_BENCHMARK_MD.read_text()
    for phrase in (
        "OT2023 through OT2024",
        "published paid/IFP count snapshot",
        "not a constitutional-review-only cohort",
        "Three OT2024 petitions remain pending",
    ):
        if phrase not in markdown:
            fail(f"certiorari multi-term markdown omits boundary text: {phrase}")
    if not CERTIORARI_MULTI_TERM_TABLE.exists():
        fail("missing generated certiorari multi-term manuscript table")
    table = CERTIORARI_MULTI_TERM_TABLE.read_text()
    for phrase in (
        "\\label{tab:certiorari-multi-term}",
        "OT2023",
        "OT2024",
        "three OT2024 petitions still pending or held",
        "same-cutoff-date dockets",
    ):
        if phrase not in table:
            fail(f"certiorari multi-term manuscript table omits: {phrase}")


def check_certiorari_docketed_cohort_reconciliation() -> None:
    check_csv_schema(
        CERTIORARI_DOCKETED_COHORT_RECONCILIATION_CSV,
        REQUIRED_CERTIORARI_DOCKETED_COHORT_RECONCILIATION_COLUMNS,
        "certiorari docketed-cohort Journal reconciliation",
    )
    if not CERTIORARI_DOCKETED_COHORT_RECONCILIATION_MD.exists():
        fail("missing certiorari docketed-cohort Journal reconciliation markdown")
    with CERTIORARI_DOCKETED_COHORT_EXTRACT_CSV.open(newline="") as handle:
        extract = {row["docketNumber"]: row for row in csv.DictReader(handle)}
    with CERTIORARI_DOCKETED_COHORT_RECONCILIATION_CSV.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 4222 or len({row["docketNumber"] for row in rows}) != 4222:
        fail("certiorari docketed-cohort reconciliation does not contain 4,222 unique dockets")
    allowed_statuses = {
        "outcome_matches_journal",
        "not_in_journal_disposition_extract",
        "outcome_differs_from_journal",
    }
    bad_rows: list[str] = []
    for row in rows:
        docket_number = row["docketNumber"]
        source = extract.get(docket_number)
        if source is None:
            bad_rows.append(f"{docket_number}: absent from cohort extract")
            continue
        if row["reconciliationStatus"] not in allowed_statuses:
            bad_rows.append(f"{docket_number}: unexpected reconciliationStatus")
        if row["docketDisposition"] != source["certDisposition"]:
            bad_rows.append(f"{docket_number}: docket disposition mismatch")
        if row["docketDispositionDate"] != source["dispositionDate"]:
            bad_rows.append(f"{docket_number}: docket disposition date mismatch")
        if row["officialDocketUrl"] != source["sourceUrl"]:
            bad_rows.append(f"{docket_number}: official docket URL mismatch")
    if bad_rows:
        fail("certiorari docketed-cohort reconciliation rows require review: " + "; ".join(bad_rows[:10]))
    markdown = CERTIORARI_DOCKETED_COHORT_RECONCILIATION_MD.read_text()
    for phrase in ("closed OT2023 paid/IFP docketed cohort", "not evidence that the official docket is wrong"):
        if phrase not in markdown:
            fail("certiorari docketed-cohort reconciliation markdown is missing boundary text: " + phrase)


def check_certiorari_granted_docket_detail_extract() -> None:
    if not CERTIORARI_GRANTED_DOCKET_DETAIL_EXTRACT_CSV.exists():
        fail(
            "missing certiorari granted docket-detail extract "
            f"{CERTIORARI_GRANTED_DOCKET_DETAIL_EXTRACT_CSV.relative_to(ROOT)}"
        )
    if not CERTIORARI_GRANTED_DOCKET_DETAIL_MANIFEST.exists():
        fail(
            "missing certiorari granted docket-detail manifest "
            f"{CERTIORARI_GRANTED_DOCKET_DETAIL_MANIFEST.relative_to(ROOT)}"
        )
    with CERTIORARI_COHORT_SCHEMA_CSV.open(newline="") as handle:
        schema_fields = [row["fieldName"] for row in csv.DictReader(handle)]
    with CERTIORARI_GRANTED_DOCKET_DETAIL_EXTRACT_CSV.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if (reader.fieldnames or []) != schema_fields:
            fail("certiorari granted docket-detail extract columns do not match cohort schema fieldName order")
        rows = list(reader)
    if len(rows) != 115:
        fail("certiorari granted docket-detail extract must contain the 115 Journal granted/GVR rows")

    manifest = json.loads(CERTIORARI_GRANTED_DOCKET_DETAIL_MANIFEST.read_text())
    if int(manifest.get("rowCount", -1)) != len(rows):
        fail("certiorari granted docket-detail manifest rowCount does not match extract")
    if int(manifest.get("journalGrantedOrGvrRows", -1)) != len(rows):
        fail("certiorari granted docket-detail manifest does not reconcile to Journal granted/GVR rows")
    if int(manifest.get("failedFetchCount", -1)) != 0:
        fail("certiorari granted docket-detail manifest reports failed docket fetches")
    if "not a closed filed-petition cohort" not in " ".join(manifest.get("notes", [])):
        fail("certiorari granted docket-detail manifest does not preserve the cohort boundary")

    dispositions = {row.get("certDisposition", "") for row in rows}
    if dispositions != {"granted", "gvr_or_remand"}:
        fail("certiorari granted docket-detail extract has unexpected dispositions")
    bad_rows: list[str] = []
    cfr_yes = 0
    cvsg_yes = 0
    argument_yes = 0
    merits_outcomes = 0
    for row in rows:
        source_id = row.get("sourceRecordId", "")
        if row.get("sourceKey") != "scotus-docket-plus-journal-granted-ot2023":
            bad_rows.append(f"{source_id}: unexpected sourceKey")
        if row.get("term") != "OT2023":
            bad_rows.append(f"{source_id}: unexpected term")
        if not row.get("sourceUrl", "").startswith("https://www.supremecourt.gov/docket/docketfiles/html/public/"):
            bad_rows.append(f"{source_id}: sourceUrl is not an official docket page")
        if not row.get("docketNumber"):
            bad_rows.append(f"{source_id}: missing docketNumber")
        if not row.get("petitionFiledDate"):
            bad_rows.append(f"{source_id}: missing petitionFiledDate")
        if row.get("granted") != "yes":
            bad_rows.append(f"{source_id}: granted field is not yes")
        if row.get("certDisposition") == "gvr_or_remand" and row.get("gvrOrSummaryDisposition") != "yes":
            bad_rows.append(f"{source_id}: GVR row is not marked as summary/GVR")
        if "not a closed filing cohort" not in row.get("coderNotes", ""):
            bad_rows.append(f"{source_id}: coderNotes do not preserve cohort boundary")
        if row.get("responseRequestedByCourt") == "yes":
            cfr_yes += 1
        if row.get("cvsgRequested") == "yes":
            cvsg_yes += 1
        if row.get("grantSetForArgument") == "yes":
            argument_yes += 1
        if row.get("meritsOutcome"):
            merits_outcomes += 1
    if bad_rows:
        fail("certiorari granted docket-detail extract rows require review: " + "; ".join(bad_rows[:10]))
    if cfr_yes < 20 or cvsg_yes < 1 or argument_yes < 50 or merits_outcomes < 40:
        fail("certiorari granted docket-detail extract is missing expected bounded docket-detail signals")


def check_certiorari_granted_docket_detail_summary() -> None:
    check_csv_schema(
        CERTIORARI_GRANTED_DOCKET_DETAIL_SUMMARY_CSV,
        REQUIRED_ECTHR_EXECUTION_MONITORING_SUMMARY_COLUMNS,
        "certiorari granted docket-detail summary",
    )
    with CERTIORARI_GRANTED_DOCKET_DETAIL_EXTRACT_CSV.open(newline="") as handle:
        extract_rows = list(csv.DictReader(handle))
    with CERTIORARI_GRANTED_DOCKET_DETAIL_SUMMARY_CSV.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    by_metric = {row["metricKey"]: row for row in rows}
    required_metrics = {
        "certiorariGrantedDocketDetailRows",
        "certiorariGrantedDocketPetitionFiledRows",
        "certiorariGrantedDocketCfrRows",
        "certiorariGrantedDocketCvsgRows",
        "certiorariGrantedDocketArgumentRows",
        "certiorariGrantedDocketMeritsOutcomeRows",
    }
    missing = required_metrics - set(by_metric)
    if missing:
        fail("certiorari granted docket-detail summary is missing metrics: " + ", ".join(sorted(missing)))
    if int(by_metric["certiorariGrantedDocketDetailRows"]["observedValue"]) != len(extract_rows):
        fail("certiorari granted docket-detail summary total does not match extract")
    overclaiming_rows = [
        row["metricKey"]
        for row in rows
        if "not closed petition-cohort validation" not in row.get("manuscriptUse", "")
    ]
    if overclaiming_rows:
        fail(
            "certiorari granted docket-detail summary manuscript-use text may overclaim: "
            + ", ".join(overclaiming_rows[:10])
        )


def main() -> None:
    for manifest in MANIFESTS:
        check_manifest(manifest)
    check_campaign_schema()
    check_csv_schema(PRIOR_UNCERTAINTY_CSV, REQUIRED_PRIOR_COLUMNS, "prior uncertainty")
    check_csv_schema(PATHWAY_DASHBOARD_CSV, REQUIRED_PATHWAY_COLUMNS, "pathway dashboard")
    check_csv_schema(METRIC_SEMANTICS_CSV, REQUIRED_METRIC_SEMANTICS_COLUMNS, "metric semantics")
    check_csv_schema(BENCHMARK_READINESS_CSV, REQUIRED_BENCHMARK_READINESS_COLUMNS, "benchmark readiness")
    check_certiorari_benchmark_readiness()
    check_lower_court_precedent_treatment_benchmark()
    check_environmental_implementation_cohort()
    check_csv_schema(BENCHMARK_PROTOCOL_CSV, REQUIRED_BENCHMARK_PROTOCOL_COLUMNS, "benchmark extraction protocol")
    check_csv_schema(BENCHMARK_WORKQUEUE_CSV, REQUIRED_BENCHMARK_WORKQUEUE_COLUMNS, "benchmark extraction work queue")
    check_csv_schema(CERTIORARI_WORKQUEUE_CSV, REQUIRED_CERTIORARI_WORKQUEUE_COLUMNS, "certiorari extraction work queue")
    check_csv_schema(CERTIORARI_FIELD_READINESS_CSV, REQUIRED_CERTIORARI_FIELD_READINESS_COLUMNS, "certiorari field readiness")
    check_csv_schema(CERTIORARI_COHORT_CLOSURE_PLAN_CSV, REQUIRED_CERTIORARI_CLOSURE_PLAN_COLUMNS, "certiorari closure plan")
    check_certiorari_closure_plan()
    check_csv_schema(
        IMPLEMENTATION_COMPLIANCE_CLOSURE_PLAN_CSV,
        REQUIRED_IMPLEMENTATION_COMPLIANCE_CLOSURE_PLAN_COLUMNS,
        "implementation/compliance closure plan",
    )
    check_implementation_compliance_closure_plan()
    check_csv_schema(
        IMPLEMENTATION_COMPLIANCE_WORKQUEUE_CSV,
        REQUIRED_IMPLEMENTATION_COMPLIANCE_WORKQUEUE_COLUMNS,
        "implementation/compliance workqueue",
    )
    check_implementation_compliance_workqueue()
    check_certiorari_term_flow_term(
        CERTIORARI_TERM_FLOW_EXTRACT_CSV,
        CERTIORARI_TERM_FLOW_MANIFEST,
        "OT2023",
        "journal-ot2023",
        "f5d8eb56e7b0256fa583a3722037b7ef1b01b028f7dc985f2d5ceb39900e30f7",
        {
            "cases_docketed_paid": 1375,
            "cases_docketed_ifp": 2847,
            "cases_docketed_total": 4223,
            "total_cases_granted_plenary_review": 69,
        },
    )
    check_certiorari_term_flow_term(
        CERTIORARI_TERM_FLOW_EXTRACT_OT2024_CSV,
        CERTIORARI_TERM_FLOW_OT2024_MANIFEST,
        "OT2024",
        "journal-ot2024",
        "d89d73c1e442aaa78d8a5b879989a50d6c2dc58d5d0b181326eff86476acff1b",
        {
            "cases_docketed_paid": 1327,
            "cases_docketed_ifp": 2527,
            "cases_docketed_total": 3856,
            "total_cases_granted_plenary_review": 70,
        },
    )
    check_certiorari_journal_disposition_extract()
    check_certiorari_journal_disposition_summary()
    check_certiorari_journal_docket_detail_extract()
    check_certiorari_journal_docket_detail_summary()
    check_certiorari_journal_docket_retrieval_workqueue()
    check_certiorari_docketed_cohort()
    check_certiorari_docketed_cohort_summary_and_calibration()
    check_certiorari_docketed_cohort_ot2024()
    check_certiorari_docketed_cohort_ot2024_summary_and_calibration()
    check_certiorari_multi_term_benchmark()
    check_certiorari_docketed_cohort_reconciliation()
    check_certiorari_granted_docket_detail_extract()
    check_certiorari_granted_docket_detail_summary()
    check_csv_schema(EMERGENCY_APPLICATION_EXTRACT_CSV, REQUIRED_EMERGENCY_APPLICATION_EXTRACT_COLUMNS, "emergency application extract")
    check_emergency_grant_linkage_workqueue()
    check_emergency_denied_linkage_workqueue()
    check_emergency_linkage_coded_rows()
    check_emergency_denied_linkage_coded_rows()
    check_emergency_denied_linkage_coded_summary()
    check_csv_schema(EMERGENCY_APPLICATION_RECONCILIATION_CSV, REQUIRED_EMERGENCY_APPLICATION_RECONCILIATION_COLUMNS, "emergency application reconciliation")
    check_status_values(EMERGENCY_APPLICATION_RECONCILIATION_CSV, "emergency application reconciliation", "matches_calibration_summary")
    check_csv_schema(EMERGENCY_FIELD_READINESS_CSV, REQUIRED_EMERGENCY_FIELD_READINESS_COLUMNS, "emergency field readiness")
    check_emergency_field_readiness()
    check_csv_schema(CERTIORARI_TERM_FLOW_RECONCILIATION_CSV, REQUIRED_CERTIORARI_RECONCILIATION_COLUMNS, "certiorari term-flow reconciliation")
    check_reconciliation_status(CERTIORARI_TERM_FLOW_RECONCILIATION_CSV, "certiorari term-flow reconciliation")
    check_csv_schema(EMERGENCY_LINKAGE_SCHEMA_CSV, REQUIRED_BENCHMARK_SCHEMA_COLUMNS, "emergency linkage schema")
    check_csv_schema(CERTIORARI_COHORT_SCHEMA_CSV, REQUIRED_BENCHMARK_SCHEMA_COLUMNS, "certiorari cohort schema")
    check_csv_schema(IMPLEMENTATION_COMPLIANCE_SCHEMA_CSV, REQUIRED_BENCHMARK_SCHEMA_COLUMNS, "implementation/compliance schema")
    check_schema_template(EMERGENCY_LINKAGE_SCHEMA_CSV, EMERGENCY_LINKAGE_TEMPLATE_CSV, "emergency linkage")
    check_schema_template(CERTIORARI_COHORT_SCHEMA_CSV, CERTIORARI_COHORT_TEMPLATE_CSV, "certiorari cohort")
    check_schema_template(
        IMPLEMENTATION_COMPLIANCE_SCHEMA_CSV,
        IMPLEMENTATION_COMPLIANCE_TEMPLATE_CSV,
        "implementation/compliance",
    )
    check_implementation_compliance_schema()
    check_ecthr_execution_monitoring_extract()
    check_ecthr_execution_monitoring_summary()
    check_certiorari_field_readiness()
    print(f"Paper artifact verification passed ({len(MANIFESTS)} manifests).")


if __name__ == "__main__":
    main()
