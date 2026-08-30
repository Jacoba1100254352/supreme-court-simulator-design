# Certiorari Journal Docket Detail Summary v1

This report summarizes the official Supreme Court docket-page join for all OT2023 Journal certiorari disposition seed rows. It is bounded Journal-disposition docket-detail evidence only, not a closed filed-petition cohort and not denominator-wide specialist-counsel or split-quality validation.

- Failed docket fetches: 4

| Metric | Value | Manuscript use | Notes |
| --- | ---: | --- | --- |
| `certiorariJournalDocketSourceRows` | 3951 | keeps the Journal disposition denominator visible before any closed-cohort claim | Total OT2023 Journal certiorari disposition seed rows attempted. |
| `certiorariJournalDocketFailedFetchRows` | 4 | must remain a public-docket coverage limitation until official pages or another source covers these rows | Journal seed rows whose official static docket page was not reachable by the extractor. |
| `certiorariJournalDocketDetailRows` | 3947 | can support bounded reachable-public-docket detail evidence, not closed filed-petition validation | One official docket-page row for each Journal disposition seed row successfully fetched. |
| `certiorariJournalDocketPetitionFiledRows` | 3913 | can support bounded petition-filed-date coverage for Journal disposition rows only | Petition filing date parsed from official docket proceedings. |
| `certiorariJournalDocketResponseFiledRows` | 3924 | can support bounded response-stage coverage for Journal disposition rows only | Rows with filed respondent briefs, memoranda, other response filings, or waiver entries. |
| `certiorariJournalDocketCfrRows` | 244 | can support bounded CFR presence among Journal disposition rows only | Rows with a docket proceeding labeled Response Requested. |
| `certiorariJournalDocketCvsgRows` | 13 | can support bounded CVSG presence among Journal disposition rows only | Rows with a docket proceeding inviting the Solicitor General to file a brief. |
| `certiorariJournalDocketAmicusRows` | 274 | can support bounded cert-stage amicus visibility for Journal disposition rows only | Rows with at least one docket-visible cert-stage amicus brief before disposition. |
| `certiorariJournalDocketRelistedRows` | 562 | can support bounded relist visibility for Journal disposition rows only | Rows with more than one docket-visible distribution before disposition. |
| `certiorariJournalDocketGrantedRows` | 115 | must remain bounded to Journal disposition rows only until it reconciles to the Journal granted/GVR count | Rows marked granted by the Journal disposition seed. |
