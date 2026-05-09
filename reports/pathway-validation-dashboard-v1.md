# Pathway Validation Dashboard v1

This dashboard keeps pathway denominators separate. It does not pool certiorari, emergency applications, individual complaints, QPC/concrete referrals, compliance, and override/remand behavior.

| Pathway | Construct | Sim metric | Current-like | Source metric | Source range | Tier | Validation use | Next action |
| --- | --- | --- | ---: | --- | ---: | --- | --- | --- |
| certiorari | paid/IFP split | `paidPetitionRate` | 0.400 | `paidPetitionShare` | 0.235--0.235 | primary_source_named_in_table | strict_validation | expand term coverage |
| certiorari | paid/IFP split | `ifpPetitionRate` | 0.156 | `ifpPetitionShare` | 0.765--0.765 | primary_source_named_in_table | strict_validation | expand term coverage |
| certiorari | court-requested response | `paidCfrRequestRate` | 0.059 | `cfrRate_paid` | 0.047--0.047 | research_synthesis | loose_calibration | expand term coverage |
| certiorari | court-requested response | `ifpCfrRequestRate` | 0.040 | `cfrRate_ifp` | 0.020--0.020 | research_synthesis | strict_validation | expand term coverage |
| certiorari | CVSG signal | `cvsgRequestRate` | 0.001 | `cvsgCount` |  | not_yet_source_backed |  | needs primary-source target |
| certiorari | grant/admission funnel | `certiorariAdmissionRate` | 0.236 | `us_scotus_plenaryReviewRate_allDocketed` | 0.016--0.018 | primary_source_named_in_table | strict_validation | attach extracted source row or raw file in supplement |
| certiorari | split quality | `genuineLowerCourtSplitRate` | 0.535 | `genuineConflictGrantRate` | 0.160--0.160 | research_synthesis | proxy_context | replace proxy with direct denominator if available |
| certiorari | elite counsel access | `specialistCounselRate` | 0.429 | `us_certGrant_formerClerk_predicted` | 0.150--0.150 | peer_reviewed_or_scholarly_summary | loose_calibration | expand term coverage |
| emergency | emergency application presence | `emergencyStayDocketRate` | 0.092 | `emergencyStayDocketRate` | 0.000--0.023 | raw_or_primary_summary | normalized_source | usable guardrail |
| emergency | emergency orders | `emergencyOrderRate` | 0.458 | `emergencyOrderRate` | 0.011--0.323 | raw_or_primary_summary | normalized_source | usable guardrail |
| emergency | emergency relief grants | `emergencyGrantRate` | 0.120 | `noncapitalGrantRate_overall` | 0.230--0.230 | research_synthesis | strict_validation | expand term coverage |
| emergency | reason/disagreement visibility | `reasonedEmergencyOrderRate` | 0.000 | `noncapitalDissentRate_any` | 0.250--0.250 | research_synthesis | strict_validation | expand term coverage |
| emergency | merits follow-through | `meritsAccelerationRate` | 0.000 | `noncapitalGrantRate_noLinkedMerits` | 0.250--0.250 | raw_or_primary_summary | loose_calibration | expand term coverage |
| emergency | downstream incentive effect | `emergencyDownstreamEffect` | 0.191 | `presidentialEmergencyApplications_peak` | 22.000--22.000 | research_synthesis | proxy_context | replace proxy with direct denominator if available |
| complaint_referral | individual complaint admission | `admissionRate` | 0.555 | `spain_amparo_admission_rate` | 0.016--0.016 | primary_source_named_in_table | strict_validation | expand term coverage |
| complaint_referral | public-interest filtering | `publicInterestFilteredRate` | 0.000 | `spain_amparo_admissionRate` | 0.023--0.023 | primary_source_named_in_table | strict_validation | expand term coverage |
| complaint_referral | constitutional remand/deferred remedy | `constitutionalRemandRate` | 0.000 | `fr_qpc_delayedEffectRate_decidedQPC` | 0.126--0.126 | primary_source_named_in_table | loose_calibration | expand term coverage |
| complaint_referral | filtered referral merits path | `meritsTransferRate` | 0.432 | `france_qpc_decisions` | 45.000--45.000 | model_prior | strict_validation | expand term coverage |
| lower_court_compliance | lower-court alignment | `lowerCourtCompliance` | 0.510 | `districtCourtAlignmentShockSameDirectionPP` | 0.330--0.330 | research_synthesis | strict_validation | expand term coverage |
| lower_court_compliance | implementation resistance | `lowerCourtResistanceRisk` | 0.332 | `echrEnforcementDomesticJudgmentsThemeShare` | 0.040--0.040 | primary_source_named_in_table | loose_calibration | expand term coverage |
| lower_court_compliance | government noncompliance | `governmentNoncomplianceRate` | 0.189 | `federalAgencyNarrowComplianceShare` | 0.068--0.068 | research_synthesis | loose_calibration | expand term coverage |
| lower_court_compliance | monitoring capacity | `interbranchCompliance` | 0.446 | `costaRicaOrdersTrackedShare` | 0.973--0.973 | raw_or_primary_summary | strict_validation | expand term coverage |
| override_remand | override pressure after invalidation | `overrideAttemptRate` | 0.000 | `invalidationRate` | 0.000--0.153 | raw_or_primary_summary | normalized_source | usable guardrail |
| override_remand | legislative override success | `overrideRate` | 0.000 | `canada_override_duration_years` | 5.000--5.000 | primary_source_named_in_table | strict_validation | expand term coverage |
| override_remand | rights carveout pressure | `rightsCarveoutBlockRate` | 0.000 | `fr_qpc_invalidityRate_decidedQPC` | 0.350--0.350 | primary_source_named_in_table | strict_validation | expand term coverage |
