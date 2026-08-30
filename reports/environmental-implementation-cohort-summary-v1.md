# Environmental post-decision implementation cohort

Snapshot date: `2026-07-26`.

## Answer first

The cohort contains **191** deduplicated, citation-linked published federal lower-court opinion documents across five fixed two-year windows. Public full text was available for **115** documents and a source-decision citation context was located in **115**. The separate practical cohort contains **5** agency episodes: **4** classified as compliant and **1** as narrowly compliant in Gurganus (2025).

These data supply a bounded event-level citation-treatment candidate and practical-implementation source slice. They do **not** supply an all-relevant-case opportunity denominator, an ignored-precedent rate, a representative constitutional-case sample, or a government-noncompliance rate.

## Decision-level reconciliation

| Decision | Federal opinion documents | Full text | Context found | Observed circuits / 13 | Practical class |
|---|---:|---:|---:|---:|---|
| Massachusetts v. EPA | 76 | 39 | 39 | 12 / 13 | compliant |
| Rapanos v. United States | 41 | 15 | 15 | 10 / 13 | narrowly compliant |
| Utility Air Regulatory Group v. EPA | 44 | 38 | 38 | 11 / 13 | compliant |
| Michigan v. EPA | 25 | 18 | 18 | 8 / 13 | compliant |
| Sackett v. EPA | 5 | 5 | 5 | 4 / 13 | compliant |

## Automated treatment-candidate coding

Each lower-court row is one citation-linked opinion document after provider-cluster deduplication. When a public document is retrievable, the extractor retains up to three local citation contexts and applies conservative, inspectable phrase rules. Explicit language can flag `followed`, `applied`, `distinguished`, `narrowed`, or `questioned/resisted`; a located citation without directional language is `cited_context_only`; missing public text or an unlocated anchor is `unclear`. Directional values are automated candidates pending expert legal review, not final doctrinal-treatment determinations or findings about policy implementation or remedy fidelity.

Pooled treatment counts:

- `followed`: 0
- `applied`: 5
- `distinguished`: 1
- `narrowed`: 0
- `questioned/resisted`: 0
- `cited_context_only`: 109
- `unclear`: 76

## Nationwide applicability and citation presence

`data/benchmarks/lower-court-environmental-circuit-exposure-v1.csv` contains 65 decision-circuit cells (five decisions × thirteen circuits). All cells share nationwide precedential applicability. Published district-court citation events are assigned to their appellate circuit. A zero means only that CourtListener did not link a published citing federal opinion document in the fixed window; thirteen circuits is not an empirical exposure or behavioral denominator.

## Practical implementation

The practical rows preserve the complete purposive five-case sample and three-part response classifications reported in Gurganus (2025), then join each case to an official agency or Federal Register action. `Rapanos` is narrowly compliant because the formal guidance adopted the controlling tests while the study identifies preliminary jurisdictional determinations as an administrative workaround. The other four cases are classified as compliant. No noncompliant outcome is observed, so the cohort cannot validate a general government-noncompliance rate.

## Data-quality boundary

- Intended use: descriptive case-study summaries and data-quality checks.
- Lower-court grain: one source-decision × citing opinion document.
- Practical grain: one source decision × agency implementation episode.
- Search scope: published CourtListener-linked U.S. federal circuit and district opinions filed during a decision-specific 730-day window.
- Completeness boundary: full-text availability is nonrandom across tracked decisions and opinion-document types (115/191 overall).
- Construct boundary: all five Supreme Court decisions are salient environmental statutory cases, not constitutional judgments.
- Comparability boundary: neither source layer is denominator-matched to the simulator's synthetic case-average compliance measures.
- Expert-review status: `data/benchmarks/environmental-directional-treatment-review-queue-v1.csv` contains all automated directional candidates plus a deterministic citation-only sample; every row remains pending expert review.

## Sources

- Gurganus, Kayla. 2025. "Supreme Court Power and Agency Implementation in Environmental Litigation." Law & Policy 47(4). DOI: https://doi.org/10.1111/lapo.70004
- CourtListener search API documentation: https://wiki.free.law/c/courtlistener/help/api/rest/v4/search
- CourtListener citation documentation: https://wiki.free.law/c/courtlistener/help/api/rest/v4/citations
- CourtListener opinion coverage: https://www.courtlistener.com/help/coverage/opinions/
- Full-text missingness audit: `reports/environmental-full-text-availability-audit-v1.csv`
- Structured Gurganus Table 1 transcription: `data/benchmarks/gurganus-2025-table-1-classifications-v1.csv`
- Official agency and Federal Register source URLs and verified hashes are recorded in `data/benchmarks/environmental-implementation-cohort-v1-manifest.json`.
