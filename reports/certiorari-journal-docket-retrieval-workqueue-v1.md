# Certiorari Journal Docket Retrieval Workqueue v1

This workqueue expands the failed-fetch portion of the OT2023 Journal public-docket detail pass into row-level retrieval tasks. It is not validation evidence. It identifies official static docket pages that returned errors during the extraction run and must be retried, manually recovered from official docket search, or otherwise documented before any closed filed-petition cohort claim is upgraded.

- Rows needing retrieval: 4
- Source slice: failed official static docket fetches from `certiorari-journal-docket-detail-ot2023-manifest.json`
- Boundary: Journal disposition rows only; not all petitions filed during OT2023

Priority counts:

- `priority_3_ifp_petition_denominator`: 4

Disposition counts:

- `denied`: 4

Paid/IFP counts:

- `ifp`: 4

Representative first rows:

| Rank | Docket | Disposition | Paid/IFP | Priority | Retrieval action |
| ---: | --- | --- | --- | --- | --- |
| 1 | `23-5090` | denied | ifp | priority_3_ifp_petition_denominator | retry official static docket page with rate limiting, then use official docket search or manual Supreme Court docket lookup before treating the row as closed-cohort coded |
| 2 | `23-5209` | denied | ifp | priority_3_ifp_petition_denominator | retry official static docket page with rate limiting, then use official docket search or manual Supreme Court docket lookup before treating the row as closed-cohort coded |
| 3 | `23-5275` | denied | ifp | priority_3_ifp_petition_denominator | retry official static docket page with rate limiting, then use official docket search or manual Supreme Court docket lookup before treating the row as closed-cohort coded |
| 4 | `23-5310` | denied | ifp | priority_3_ifp_petition_denominator | retry official static docket page with rate limiting, then use official docket search or manual Supreme Court docket lookup before treating the row as closed-cohort coded |
