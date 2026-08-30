# Emergency Application Denied/NA Linkage Coded Summary v1

This generated summary describes the official Supreme Court docket-page join for denied and non-binary full-court emergency applications. It supports bounded all-application docket-linkage checks only; it is not external implementation validation.

- Snapshot date: 2026-07-02
- Source rows: 210
- Unique official docket pages fetched: 197
- Failed fetches: 0

| Metric | Observed value | Notes |
| --- | ---: | --- |
| `emergencyDeniedNaDocketDetailRows` | 210 | coded rows in denied/NA official-docket slice |
| `emergencyDeniedNaDocketApplicationDateRows` | 210 | rows with official docket application filing dates |
| `emergencyDeniedNaDocketResponseRequestedRows` | 60 | rows with court-requested response entries |
| `emergencyDeniedNaDocketReasoningRows` | 40 | rows with docket-visible statement, opinion, mootness, or comparable reason marker |
| `emergencyDeniedNaDocketRepeatFilingRows` | 55 | rows with docket-visible refiling |
| `emergencyDeniedNaDocketReviewNeededRows` | 0 | rows with possible merits follow-through requiring manual review before any merits claim |

Boundary note:

- These rows use official docket pages to code application date, response request, reason visibility, status-quo effect, docket-visible merits follow-through category, downstream docket status, and repeat filing for the denied/NA queue. They do not observe external lower-court, agency, or policy implementation after the emergency order.
- One mixed-disposition source row (24A164) is manually linked to later merits docket 25-1017, filed February 19, 2026 and granted June 29, 2026; the merits matter remained pending at the 2026-07-26 refresh.
