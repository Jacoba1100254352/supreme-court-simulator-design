# Model Notes

The model is intentionally institutional rather than biography-heavy. A generated world contains a pool of possible justices, a docket of constitutional cases, and a legislative-output profile. Each scenario supplies a court design that selects reviewers and applies rules for merits review, emergency relief, voting thresholds, recusal, panel routing, cross-checks, council review, and overrides.

The docket generator separates facial challenges, as-applied challenges, election disputes, emergency stay applications, executive-power disputes, administrative-law challenges, economic-regulation disputes, structural disputes, and rights claims. Legal-domain profiles adjust case attributes before review, and a lower-court/certiorari intake layer now selects from a larger candidate pool rather than handing every generated dispute directly to the merits court.

Court rosters now change over simulated time. Life-tenure systems have low attrition, staggered-term systems have regular replacement, retention-election systems react more strongly to conflict, and rotating-panel systems replace reviewers more often. Replacement selection follows the scenario's appointment method.

Emergency review is modeled as a procedure stage rather than a bare boolean: application-only, response window, reasoned temporary stay, shadow stay, merits acceleration, or expiration without relief. Override outcomes distinguish failed attempts, rights-carveout blocks, ordinary supermajority overrides, delayed reenactments, referenda, and repeated overrides.

Strategic actor policy is explicit. Legislatures and executives can choose compliance, evasion, delayed reenactment, emergency flooding, override campaigns, and appointment-pressure campaigns based on state variables and case incentives. Those choices feed back into legislative defiance, executive emergency strategy, appointment manipulation pressure, and override adaptation.

Legislative outputs enter through a profile rather than through direct Java dependencies on the congressional simulator. This keeps the projects separate while preserving the ability to review laws generated under different legislative systems.

Empirical calibration uses normalized source observations under `data/calibration/`. The source tables preserve metric, term, numerator, denominator, source URL, and transformation notes; the runtime calibration report computes source ranges from those rows and writes a separate appendix.

The metrics should be read as comparative indicators:

- `legalStability`: precedent continuity and low conflict escalation.
- `rightsProtection`: protection of high-burden cases without ignoring democratic mandate.
- `partisanAlignment`: how much outcomes track partisan direction rather than legal risk.
- `shadowDocketAbuse`: emergency or unexplained relief outside merits review.
- `legitimacy`: public attention, recusal discipline, reason-giving, and low partisan odor.
- `reversalRate`: frequency of precedent/law reversals.
- `constitutionalConflict`: institutional conflict after decisions and overrides.
- `democraticResponsiveness`: respect for public mandate and clear override channels without swallowing rights constraints.

Diagnostic rates include merits acceleration, justice replacement, override attempts, rights-carveout blocks, repeated overrides, strategic actor choices, and docket-type shares.
