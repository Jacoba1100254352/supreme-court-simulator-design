# Certiorari Docketed Cohort Summary v1

This report summarizes an independently enumerated OT2024 cohort of all 1,327 paid and 2,527 IFP cases docketed during the official Journal statistics window. It closes the 3,854-case docketed-intake denominator and docket-visible CFR/CVSG/amicus/relist fields. It does not cover submissions never docketed, and it does not code specialist counsel or alleged/genuine split quality.

- Failed official docket fetches after retries: 0

| Metric | Value | Denominator | Manuscript use | Notes |
| --- | ---: | --- | --- | --- |
| `certiorariDocketedCohortExpectedRows` | 3854 | Official OT2024 paid plus IFP cases docketed during term | direct official denominator reconciliation | Journal total: 1,327 paid plus 2,527 IFP docketed cases. |
| `certiorariDocketedCohortRows` | 3854 | Independently enumerated OT2024 paid and IFP public docket-number ranges | closed docketed-intake cohort when this equals 3,854 with zero failures | One row per reachable official public docket page. |
| `certiorariDocketedCohortFailedFetchRows` | 0 | Official OT2024 paid plus IFP docket-number ranges | must be zero before closed-cohort language is used | Rows not coded after bounded retries. |
| `certiorariDocketedCohortPaidRows` | 1327 | Closed OT2024 paid/IFP docketed-intake cohort | direct official paid-intake count | Must reconcile to the Journal count of 1,327. |
| `certiorariDocketedCohortIfpRows` | 2527 | Closed OT2024 paid/IFP docketed-intake cohort | direct official IFP-intake count | Must reconcile to the Journal count of 2,527. |
| `certiorariDocketedCohortCertPetitionRows` | 3683 | Closed OT2024 paid/IFP docketed-intake cohort | direct docket-visible certiorari petition denominator | Rows whose primary filing is a petition for a writ of certiorari. |
| `certiorariDocketedCohortPetitionFiledDateRows` | 3683 | Docket-visible certiorari petition rows in the closed cohort | direct filing-date completeness check | Certiorari rows with a parsed petition filing date. |
| `certiorariDocketedCohortResponseFiledOrWaivedRows` | 3681 | Docket-visible certiorari petition rows in the closed cohort | direct response-stage descriptive evidence | Includes filed responses and docketed waivers. |
| `certiorariDocketedCohortPaidCfrRows` | 189 | Paid certiorari petition rows in the closed cohort | direct paid CFR numerator | Official docket rows with a Response Requested entry. |
| `certiorariDocketedCohortIfpCfrRows` | 75 | IFP certiorari petition rows in the closed cohort | direct IFP CFR numerator | Official docket rows with a Response Requested entry. |
| `certiorariDocketedCohortCvsgRows` | 20 | Docket-visible certiorari petition rows in the closed cohort | direct whole-cohort CVSG numerator | Official docket rows inviting the Solicitor General's views. |
| `certiorariDocketedCohortAmicusRows` | 313 | Docket-visible certiorari petition rows in the closed cohort | direct cert-stage amicus-presence numerator | Rows with at least one docket-visible amicus brief before disposition. |
| `certiorariDocketedCohortRelistedRows` | 409 | Docket-visible certiorari petition rows in the closed cohort | direct relist-presence numerator | Rows with more than one distribution before disposition. |
| `certiorariDocketedCohortGrantedRows` | 62 | Docket-visible certiorari petition rows in the closed cohort | direct docketed-cohort plenary-grant numerator | Excludes GVR/remand dispositions. |
| `certiorariDocketedCohortGvrRows` | 52 | Docket-visible certiorari petition rows in the closed cohort | direct docketed-cohort GVR/remand numerator | Docket grant rows that also vacate or remand at cert-stage disposition. |
| `certiorariDocketedCohortDeniedRows` | 3463 | Docket-visible certiorari petition rows in the closed cohort | direct docketed-cohort denial numerator | First docket-visible certiorari disposition is denial. |
| `certiorariDocketedCohortDismissedRows` | 71 | Docket-visible certiorari petition rows in the closed cohort | direct docketed-cohort dismissal numerator | Includes Rule 39.8 and other petition dismissals. |
| `certiorariDocketedCohortOtherClosedRows` | 32 | Docket-visible certiorari petition rows in the closed cohort | direct nonstandard final-outcome numerator | Separates fee-denied closures, docket removals, and statutory quorum affirmance from ordinary denial. |
| `certiorariDocketedCohortPendingOrUnresolvedRows` | 3 | Docket-visible certiorari petition rows in the closed cohort | must remain explicit as an outcome-completeness limitation | Certiorari rows without a classified current docket disposition. |
