# Response to Independent AI Methods Review v1

This response addresses an independent AI review, not human peer review.

| Finding | Response | Evidence | Status |
|---|---|---|---|
| Published-only selection and unstable tie | Added `status:published` to every query, labeled the cohort published-only, retained citing captions and docket identifiers, and added the smallest cluster ID as the stable final tie-breaker. | `tools/extract_environmental_implementation_cohort.py`; cohort manifest | Addressed |
| Nonrandom 115/191 full-text availability | Added row-level unavailable reasons and snippets plus a 60-row audit by decision, court, filing year, opinion type, and reason. Manuscript and calibration rows now prohibit behavioral comparison. | `reports/environmental-full-text-availability-audit-v1.csv`; companion Markdown report | Addressed for disclosure; additional text recovery remains future work |
| UARG false positive | Removed the overbroad 220-character rule, recoded the event as citation-only, and added an executable negative regression. Corrected counts are 5 applied candidates, 1 distinguished candidate, 109 citation-only, and 76 unclear. | Event CSV; extractor; strict artifact verifier | Addressed |
| No second coder | Generated a 16-row queue containing all six directional candidates and a deterministic two-per-decision citation-only sample. Expert, agreement, and adjudication fields remain blank and explicitly pending. | `data/benchmarks/environmental-directional-treatment-review-queue-v1.csv` | Open external human/expert task; no completed review is claimed |
| “Exposure” overclaim | Reframed the 65 cells as nationwide applicability and published-citation presence. All environmental behavioral-guardrail labels were removed. | Exposure CSV notes; calibration CSV; manuscript | Addressed |
| Practical fractions presented as rates | Relabeled all rows as descriptive case-study summaries and added a structured five-row Table 1/case-study transcription with locators and record hashes. | `data/benchmarks/gurganus-2025-table-1-classifications-v1.csv`; calibration CSV | Addressed |
| Analytic reproduction versus source acquisition | The replication manifest now records dirty-tree state, status hash/count, and a complete package-tree hash. It states that the archive reproduces downstream analysis from frozen normalized outputs. A separate deterministic source-snapshot builder packages the cached acquisition evidence when redistribution review permits. | `tools/create_replication_package.py`; `tools/check_replication_package.py`; `tools/create_environmental_source_snapshot.py` | Addressed |
| Duplicate header and missing citing fields | Removed the duplicate header, added citing caption/full caption and CourtListener docket ID, and made both the extractor and verifier reject duplicate headers. | Event CSV; extractor; strict artifact verifier | Addressed |
| Structural source-audit naming | Renamed checker output and documentation to “source traceability”; added environmental boundary assertions and clarified that substantive counts, hashes, and semantics are checked separately. | `paper/scripts/check_source_audit.py`; `paper/scripts/verify_paper_artifacts.py` | Addressed |
| “Gate completed” wording | Replaced it with “bounded acquisition snapshot completed” and preserved expert-coding and opportunity-denominator work as open. | Generated closure plan and work queue | Addressed |

## Remaining publication boundary

The revision does not convert the environmental evidence into validation of
synthetic compliance behavior. Independent human legal coding, adjudication,
broader decision coverage, an issue-relevant opportunity denominator, remedy
fidelity, and observed noncompliance remain future external-validation work.
