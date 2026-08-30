# Independent AI Methods Review v1

Review date: `2026-07-26`

## Disclosure and recommendation

This was an independent AI methods review, not human peer review. The reviewer
recommended **major revision before submission** and would have recommended
rejection with encouragement to resubmit if the paper had continued to describe
the environmental cohort as behavioral validation.

## Strongest rejection argument

The paper's consequential compliance and implementation outputs remain
stipulated model mechanisms rather than empirically validated behavioral
relationships. The new evidence comprises published citation-bearing opinions
for five purposively selected statutory environmental cases, usable full text
for only 115 of 191 opinion documents, no relevant-case opportunity denominator,
and five agency case studies with no noncompliant outcome. It therefore cannot
validate `lowerCourtCompliance` or `governmentNoncomplianceRate`.

No fatal data-integrity defect was found if the paper remains strictly a
synthetic design-search exercise and preserves those boundaries.

## Major findings

1. **Published-only selection was underdisclosed.** CourtListener case-law
   searches return published opinions by default. All 191 rows were published,
   but the manuscript described them more broadly. Two equal-score provider
   clusters also lacked a stable final tie-breaker.
2. **Full-text missingness was structurally nonrandom.** Availability was
   39/76 for *Massachusetts*, 15/41 for *Rapanos*, 38/44 for *UARG*, 18/25 for
   *Michigan*, and 5/5 for *Sackett*. It was 115/169 for combined opinions and
   0/22 for lead, dissenting, or in-part documents. Seventy unavailable rows had
   no document URL in the public search result, while six downloads failed or
   were unextractable.
3. **One of seven directional codes was a false positive.** A criminal
   restitution opinion cited *UARG* for a general contextual-interpretation
   proposition, then applied those principles to the MVRA. A 220-character
   regex incorrectly treated this as application of *UARG*. The corrected
   automated counts are five applied candidates, one distinguished candidate,
   109 citation-only, and 76 unclear.
4. **The 65 circuit cells were not empirical exposure.** Crossing every source
   decision with every circuit represents nationwide precedential
   applicability; observed values describe published-citation presence only.
5. **The five practical classifications were not rates.** The four compliant
   and one narrowly compliant labels accurately transcribed a purposive
   case-study sample, but 0.8 and 0.2 are sample composition rather than
   estimable compliance probabilities.
6. **The package reproduced normalized analysis, not source acquisition.** Raw
   search pages and documents were excluded, the package checker did not rerun
   the network extractor, and a dirty checkout was represented only by its HEAD
   commit.

## Minor findings

- The event CSV repeated `docketNumber` in its header.
- `caseName` identified the tracked Supreme Court case but no separate citing
  caption or CourtListener docket identifier was retained.
- The source-audit checker was structural but its name could be read as
  substantive source verification.
- “Gate completed” overstated the environmental snapshot's methodological
  closure.

## Checks that passed

- Search, federal-court, deduplication, event, circuit-cell, full-text, and
  practical-row counts reconciled to the manifest.
- Event identifiers were unique and source-output hashes matched.
- Practical action delays and the four-compliant/one-narrowly-compliant
  transcription reconciled.
- The manuscript already disclaimed causal estimation, representative
  compliance, ignored-precedent inference, and government-noncompliance
  estimation.
- Environmental rows were not consumed as main simulator calibration targets.
- Existing package-member hashes and anonymity scans passed.

## Source documentation consulted

- CourtListener search API:
  <https://wiki.free.law/c/courtlistener/help/api/rest/v4/search>
- CourtListener opinion coverage:
  <https://www.courtlistener.com/help/coverage/opinions/>
- Gurganus article DOI: <https://doi.org/10.1111/lapo.70004>
