# Empirical Calibration Appendix v4

Normalized source observations used to compute calibration ranges. The simulator does not read raw SCDB or shadow-docket archives at runtime; those large files are reduced into term-level source rows under `data/calibration`.

## Source Range Summary

| Metric | Obs. | Terms | Sources | Raw min | P05 | Median | P95 | Raw max |
| --- | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| `administrativeLawRate` | 79 | 1946-2024 | scdb-modern-2025-01 | 0.068 | 0.086 | 0.234 | 0.397 | 0.416 |
| `canada_override_duration_years` | 1 | stable | cross-national-calibration-targets | 5.000 | 5.000 | 5.000 | 5.000 | 5.000 |
| `civil_disposition_days_eu_median_first_instance` | 1 | 2022 | institutional-cost-delay-complexity-benchmarks | 239.000 | 239.000 | 239.000 | 239.000 | 239.000 |
| `complaw_courts_covered` | 1 | 2024_release | cross-national-calibration-targets | 42.000 | 42.000 | 42.000 | 42.000 | 42.000 |
| `complexity_appointment_actor_count_germany` | 1 | stable | institutional-cost-delay-complexity-benchmarks | 2.000 | 2.000 | 2.000 | 2.000 | 2.000 |
| `complexity_appointment_actor_count_italy` | 1 | stable | institutional-cost-delay-complexity-benchmarks | 3.000 | 3.000 | 3.000 | 3.000 | 3.000 |
| `complexity_appointment_actor_count_spain` | 1 | stable | institutional-cost-delay-complexity-benchmarks | 4.000 | 4.000 | 4.000 | 4.000 | 4.000 |
| `complexity_panel_layers_germany` | 1 | stable | institutional-cost-delay-complexity-benchmarks | 2.000 | 2.000 | 2.000 | 2.000 | 2.000 |
| `complexity_panel_layers_korea` | 1 | stable | institutional-cost-delay-complexity-benchmarks | 2.000 | 2.000 | 2.000 | 2.000 | 2.000 |
| `economicRegulationRate` | 79 | 1946-2024 | scdb-modern-2025-01 | 0.092 | 0.117 | 0.194 | 0.323 | 0.379 |
| `emergencyOrderRate` | 22 | 2003-2024 | shadow-docket-v2-0 | 0.011 | 0.031 | 0.100 | 0.225 | 0.323 |
| `emergencyStayDocketRate` | 32 | 1993-2024 | shadow-docket-v2-0 | 0.000 | 0.000 | 0.006 | 0.013 | 0.023 |
| `ex_ante_vs_ex_post_strike_odds_ratio_nine_courts` | 1 | 2002-2003 law cohort | cross-national-calibration-targets | 2.060 | 2.060 | 2.060 | 2.060 | 2.060 |
| `ex_ante_vs_ex_post_strike_odds_ratio_seven_courts` | 1 | 2002-2003 law cohort | cross-national-calibration-targets | 2.310 | 2.310 | 2.310 | 2.310 | 2.310 |
| `france_ex_ante_strike_rate` | 1 | 2002-2015 | cross-national-calibration-targets | 0.480 | 0.480 | 0.480 | 0.480 | 0.480 |
| `france_qpc_decisions` | 1 | 2023 | lower-court-intake-calibration | 45.000 | 45.000 | 45.000 | 45.000 | 45.000 |
| `france_qpc_mean_per_year_since_2010` | 1 | 2010-2023 | lower-court-intake-calibration | 79.400 | 79.400 | 79.400 | 79.400 | 79.400 |
| `germany_chamber_escalation_if_no_agreement` | 1 | stable | emergency-docket-calibration | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| `germany_constitutional_complaint_share_new_cases` | 1 | 2024 | lower-court-intake-calibration | 0.960 | 0.960 | 0.960 | 0.960 | 0.960 |
| `germany_court_size` | 1 | stable | cross-national-calibration-targets | 16.000 | 16.000 | 16.000 | 16.000 | 16.000 |
| `germany_judicial_budget_per_capita` | 1 | 2022 | institutional-cost-delay-complexity-benchmarks | 136.100 | 136.100 | 136.100 | 136.100 | 136.100 |
| `germany_preliminary_injunction_available` | 1 | stable | emergency-docket-calibration | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| `germany_preliminary_injunction_balancing_test` | 1 | stable | emergency-docket-calibration | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| `germany_term_years` | 1 | stable | cross-national-calibration-targets | 12.000 | 12.000 | 12.000 | 12.000 | 12.000 |
| `invalidationRate` | 79 | 1946-2024 | scdb-modern-2025-01 | 0.000 | 0.023 | 0.066 | 0.121 | 0.153 |
| `italy_courts_budget_per_capita` | 1 | 2022 | institutional-cost-delay-complexity-benchmarks | 67.200 | 67.200 | 67.200 | 67.200 | 67.200 |
| `italy_incidental_review_share` | 1 | 2024 | lower-court-intake-calibration | 0.656 | 0.656 | 0.656 | 0.656 | 0.656 |
| `italy_judicial_budget_per_capita` | 1 | 2022 | institutional-cost-delay-complexity-benchmarks | 100.600 | 100.600 | 100.600 | 100.600 | 100.600 |
| `italy_total_civil_procedure_days_three_instances` | 1 | 2022 | institutional-cost-delay-complexity-benchmarks | 2356.000 | 2356.000 | 2356.000 | 2356.000 | 2356.000 |
| `italy_total_decisions` | 1 | 2024 | lower-court-intake-calibration | 212.000 | 212.000 | 212.000 | 212.000 | 212.000 |
| `judicial_budget_per_capita_coe_median` | 1 | 2020 | institutional-cost-delay-complexity-benchmarks | 79.000 | 79.000 | 79.000 | 79.000 | 79.000 |
| `korea_constitutional_complaint_share_cumulative` | 1 | 1988-Mar-2026 | lower-court-intake-calibration | 0.977 | 0.977 | 0.977 | 0.977 | 0.977 |
| `korea_court_size` | 1 | stable | cross-national-calibration-targets | 9.000 | 9.000 | 9.000 | 9.000 | 9.000 |
| `korea_panel_dismissal_share_of_complaints_cumulative` | 1 | 1988-Mar-2026 | lower-court-intake-calibration | 0.649 | 0.649 | 0.649 | 0.649 | 0.649 |
| `korea_panel_transfer_deadline_days` | 1 | stable | emergency-docket-calibration | 30.000 | 30.000 | 30.000 | 30.000 | 30.000 |
| `korea_recusal_available` | 1 | stable | emergency-docket-calibration | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| `korea_supermajority_votes_for_unconstitutionality` | 1 | stable | cross-national-calibration-targets | 6.000 | 6.000 | 6.000 | 6.000 | 6.000 |
| `meritsReviewRate` | 79 | 1946-2024 | scdb-modern-2025-01 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| `precedentStability` | 79 | 1946-2024 | scdb-modern-2025-01 | 0.933 | 0.956 | 0.983 | 1.000 | 1.000 |
| `recusalRate` | 1 | 1946-2003 | black-epstein-recusal | 0.009 | 0.009 | 0.009 | 0.009 | 0.009 |
| `rightsClaimRate` | 79 | 1946-2024 | scdb-modern-2025-01 | 0.133 | 0.159 | 0.299 | 0.383 | 0.410 |
| `shadowDocketAbuse` | 22 | 2003-2024 | shadow-docket-v2-0 | 0.065 | 0.069 | 0.222 | 0.361 | 0.538 |
| `spain_amparo_admission_rate` | 1 | 2024 | lower-court-intake-calibration | 0.016 | 0.016 | 0.016 | 0.016 | 0.016 |
| `spain_amparo_admitted` | 1 | 2024 | lower-court-intake-calibration | 153.000 | 153.000 | 153.000 | 153.000 | 153.000 |
| `spain_amparo_filings` | 1 | 2024 | lower-court-intake-calibration | 9796.000 | 9796.000 | 9796.000 | 9796.000 | 9796.000 |
| `spain_amparo_share_total_matters` | 1 | 2024 | lower-court-intake-calibration | 0.992 | 0.992 | 0.992 | 0.992 | 0.992 |
| `spain_court_size` | 1 | stable | cross-national-calibration-targets | 12.000 | 12.000 | 12.000 | 12.000 | 12.000 |
| `spain_first_instance_civil_disposition_days` | 1 | 2022 | institutional-cost-delay-complexity-benchmarks | 359.000 | 359.000 | 359.000 | 359.000 | 359.000 |
| `spain_pending_amparo_admissibility` | 1 | 2024 | lower-court-intake-calibration | 3264.000 | 3264.000 | 3264.000 | 3264.000 | 3264.000 |
| `spain_term_years` | 1 | stable | cross-national-calibration-targets | 9.000 | 9.000 | 9.000 | 9.000 | 9.000 |
| `spain_total_matters` | 1 | 2024 | lower-court-intake-calibration | 9871.000 | 9871.000 | 9871.000 | 9871.000 | 9871.000 |
| `statutoryStability` | 79 | 1946-2024 | scdb-modern-2025-01 | 0.847 | 0.879 | 0.934 | 0.977 | 1.000 |
| `structuralRate` | 79 | 1946-2024 | scdb-modern-2025-01 | 0.133 | 0.145 | 0.223 | 0.309 | 0.370 |
| `us_argued_cases` | 1 | 2023 Term | lower-court-intake-calibration | 69.000 | 69.000 | 69.000 | 69.000 | 69.000 |
| `us_argued_to_filing_share` | 1 | 2023 Term | lower-court-intake-calibration | 0.016 | 0.016 | 0.016 | 0.016 | 0.016 |
| `us_emergency_brief_reasoning_common` | 1 | 2024-2025 terms | emergency-docket-calibration | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| `us_emergency_limited_briefing` | 1 | 2024-2025 terms | emergency-docket-calibration | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| `us_emergency_oral_argument_typically_absent` | 1 | 2024-2025 terms | emergency-docket-calibration | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| `us_merits_dispositions` | 1 | 2023 Term | lower-court-intake-calibration | 64.000 | 64.000 | 64.000 | 64.000 | 64.000 |
| `us_shadow_docket_dataset_terms_covered` | 1 | 1993-2024 | emergency-docket-calibration | 32.000 | 32.000 | 32.000 | 32.000 | 32.000 |
| `us_total_filings` | 1 | 2023 Term | lower-court-intake-calibration | 4223.000 | 4223.000 | 4223.000 | 4223.000 | 4223.000 |

## Source Files

- `black-epstein-recusal-summary.csv`
- `scdb-modern-2025-release-01.csv`
- `shadow-docket-v2-0-summary.csv`
- `supreme-court-synthesis/comparative-court-design-presets.csv`
- `supreme-court-synthesis/cross-national-calibration-targets.csv`
- `supreme-court-synthesis/emergency-docket-calibration.csv`
- `supreme-court-synthesis/institutional-cost-delay-complexity-benchmarks.csv`
- `supreme-court-synthesis/lower-court-intake-calibration.csv`
- `supreme-court-synthesis/source-register.csv`
