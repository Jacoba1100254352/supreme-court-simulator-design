# Environmental cohort full-text availability audit

Snapshot date: `2026-07-26`.

Public full text is available for 115 of 191 published citation-linked opinion documents (60.2%). Missingness is visibly nonrandom across tracked decisions and opinion-document types, so automated directional-candidate shares must not be compared as lower-court behavior rates.

## Decision

| Decision key | Events | Available | Unavailable | Availability |
|---|---:|---:|---:|---:|
| `massachusetts-v-epa-2007` | 76 | 39 | 37 | 51.3% |
| `michigan-v-epa-2015` | 25 | 18 | 7 | 72.0% |
| `rapanos-v-united-states-2006` | 41 | 15 | 26 | 36.6% |
| `sackett-v-epa-2023` | 5 | 5 | 0 | 100.0% |
| `utility-air-regulatory-group-v-epa-2014` | 44 | 38 | 6 | 86.4% |

## Opinion-document type

| Type | Events | Available | Unavailable | Availability |
|---|---:|---:|---:|---:|
| `combined-opinion` | 169 | 115 | 54 | 68.0% |
| `dissent` | 3 | 0 | 3 | 0.0% |
| `in-part-opinion` | 1 | 0 | 1 | 0.0% |
| `lead-opinion` | 18 | 0 | 18 | 0.0% |

## Recorded unavailability reason

| Reason | Events |
|---|---:|
| `download_failed_or_unextractable` | 6 |
| `no_document_url_in_search_result` | 70 |

Court- and filing-year strata are retained in the companion CSV. A `no_document_url_in_search_result` value describes the public search result supplied to this extractor; it is not a finding that no opinion text exists elsewhere. Search snippets are preserved in the event file for audit, but snippets are not used as substitutes for full-text legal treatment coding.
