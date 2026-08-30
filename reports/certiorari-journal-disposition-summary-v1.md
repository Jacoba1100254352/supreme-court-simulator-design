# Certiorari Journal Disposition Summary v1

This report summarizes the first row-level certiorari disposition seed extracted from the official OT2023 Journal. It is source-addressable disposition evidence, not a closed petition filing cohort and not denominator-matched validation.

| Metric | Observed | Comparison | Status | Notes |
| --- | ---: | --- | --- | --- |
| `journalCertiorariDispositionRows` | 3951 |  | candidate_extract | One row per docket number parsed from official Journal certiorari disposition entries. |
| `journalCertiorariUniqueDockets` | 3950 |  | candidate_extract | Unique docket count can differ from row count when consolidated entries list multiple docket numbers. |
| `journalCertiorariUniqueDispositionDates` | 52 |  | candidate_extract | Distinct Journal date headings assigned to disposition entries. |
| `journalCertiorariFirstDispositionDate` | 20231002 |  | candidate_extract | Earliest Journal date heading assigned to a disposition entry, formatted as YYYYMMDD for CSV consistency. |
| `journalCertiorariLastDispositionDate` | 20241004 |  | candidate_extract | Latest Journal date heading assigned to a disposition entry, formatted as YYYYMMDD for CSV consistency. |
| `journalCertiorariPaidDispositionRows` | 1270 | official OT2023 paid docketed during term = 1375 | not_expected_to_match_term_flow | Disposition rows include prior-term carryover dockets and omit still-pending docketed matters. |
| `journalCertiorariIfpDispositionRows` | 2647 | official OT2023 IFP docketed during term = 2847 | not_expected_to_match_term_flow | Disposition rows include prior-term carryover dockets and omit still-pending docketed matters. |
| `journalCertiorariApplicationOrMiscRows` | 34 |  | review_boundary | Application or miscellaneous dockets are included only when the Journal text treats them as certiorari before judgment or certiorari-related entries. |
| `journalCertiorariDeniedRows` | 3773 |  | candidate_extract | Routine denied-petition dispositions parsed from Journal text. |
| `journalCertiorariGrantedRows` | 58 |  | candidate_extract | Rows where the parser found a grant without GVR/remand wording. |
| `journalCertiorariGvrOrRemandRows` | 57 |  | candidate_extract | Rows where the parser found certiorari granted plus vacated or remanded wording. |
| `journalCertiorariDismissedRows` | 63 |  | candidate_extract | Dismissal rows parsed from Journal certiorari entries. |
| `journalCertiorariReviewRequiredRows` | 0 |  | none_remaining | Rows whose certiorari entry was captured but whose disposition text needs manual review after parser classification. |
| `journalCertiorariRowsWithDispositionDate` | 3951 | 3951 | matches_extract_rows | Disposition date comes from the Journal date heading nearest the entry. |
| `journalCertiorariRowsWithLowerCourt` | 3948 | 3951 | partial_extract | Lower-court text is parsed from the Journal entry where visible. |
