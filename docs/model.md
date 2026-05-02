# Model Notes

The model is intentionally institutional rather than biography-heavy. A generated world contains a pool of possible justices, a docket of constitutional cases, and a legislative-output profile. Each scenario supplies a court design that selects reviewers and applies rules for merits review, emergency relief, voting thresholds, recusal, panel routing, cross-checks, council review, and overrides.

The docket generator separates facial challenges, as-applied challenges, election disputes, emergency stay applications, executive-power disputes, administrative-law challenges, economic-regulation disputes, structural disputes, and rights claims. Legal-domain profiles adjust case attributes before review. A review-path/admissibility layer now models filed disputes becoming petitions, screened-out matters, or merits transfers rather than handing every generated dispute directly to the merits court. The generated world is the filed universe for that run; admission filtering, not a preliminary top-case selector, determines the merits docket size.

Review paths include paid certiorari, IFP certiorari, discretionary certiorari, direct constitutional complaint, amparo, filtered QPC-style referral, abstract ex ante review, abstract ex post review, concrete court referral, emergency application, interbranch dispute, and electoral review. The admission filter tracks petition type, SG/CVSG-style signal, amicus count, split maturity, relist count, specialist counsel, vehicle-quality defects, and conditional reversal probability.

Court rosters now change over simulated time. Life-tenure systems have low attrition, staggered-term systems have regular replacement, retention-election systems react more strongly to conflict, and rotating-panel systems replace reviewers more often. Replacement selection follows the scenario's appointment method.

Emergency review is modeled as a procedure stage rather than a bare boolean: application-only, response window, reasoned temporary stay, shadow stay, merits acceleration, or expiration without relief. Emergency applications also carry applicant/respondent type, application class, requested relief, response request, full-court referral, status-quo effect, public disagreement risk, and merits follow-through. Override outcomes distinguish failed attempts, rights-carveout blocks, ordinary supermajority overrides, delayed reenactments, referenda, and repeated overrides.

Strategic actor policy is explicit. Legislatures and executives can choose compliance, evasion, delayed reenactment, emergency flooding, override campaigns, and appointment-pressure campaigns based on state variables and case incentives. Their post-decision reaction is split into formal legal response, such as repeal, replacement statute, narrowed reenactment, weak-form override, amendment, court-curbing, or open defiance, and practical implementation response, such as prompt implementation, delay, administrative substitution, symbolic compliance, bureaucratic resistance, or open noncompliance. Those choices feed back into legislative defiance, executive emergency strategy, appointment manipulation pressure, and override adaptation.

Institutional designs now include appointment fragmentation, confirmation threshold, vacancy-deadlock risk, term renewability, retirement age, size-change difficulty, recusal consequence type, quorum-failure risk, and per-remedy voting thresholds. Court size is no longer forced to be odd, which allows comparative designs with even full courts, chambers, panels, or senate structures.

Legislative outputs enter through a profile rather than through direct Java dependencies on the congressional simulator. This keeps the projects separate while preserving the ability to review laws generated under different legislative systems.

Empirical calibration uses normalized source observations under `data/calibration/`. The original source tables preserve metric, term, numerator, denominator, source URL, and transformation notes; the Deep Research synthesis tables preserve metric key, jurisdiction, time period, confidence level, validation use, denominator specification, coverage scope, comparability class, source name, and source URL. The runtime calibration report computes source ranges from both schemas and writes a separate appendix.

The metrics should be read as comparative indicators:

- `legalStability`: precedent continuity and low conflict escalation.
- `rightsProtection`: protection of high-burden cases without ignoring democratic mandate.
- `partisanAlignment`: how much outcomes track partisan direction rather than legal risk.
- `shadowDocketAbuse`: emergency or unexplained relief outside merits review.
- `legitimacy`: public attention, recusal discipline, reason-giving, and low partisan odor.
- `reversalRate`: frequency of precedent/law reversals.
- `constitutionalConflict`: institutional conflict after decisions and overrides.
- `democraticResponsiveness`: respect for public mandate and clear override channels without swallowing rights constraints.

Direct outputs are kept separate from derived indices. These include `rightsClaimantSuccess`, domain-specific claimant-success rates by case type, `doctrinalDepth`, `remedialBreadth`, `fragmentationIndex`, `lowerCourtCompliance`, `eliteAcceptance`, and `publicConfidence`. Diagnostic rates include petition filing, admission, screen-out, merits transfer, emergency grants, quorum failure, merits acceleration, justice replacement, override attempts, rights-carveout blocks, repeated overrides, strategic actor choices, formal/practical response choices, and docket-type shares.
