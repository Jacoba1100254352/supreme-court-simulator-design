# Model Notes

The model is intentionally institutional rather than biography-heavy. A generated world contains a pool of possible justices, a docket of constitutional cases, and a legislative-output profile. Each scenario supplies a court design that selects reviewers and applies rules for merits review, emergency relief, voting thresholds, recusal, panel routing, cross-checks, council review, and overrides.

Legislative outputs enter through a profile rather than through direct Java dependencies on the congressional simulator. This keeps the projects separate while preserving the ability to review laws generated under different legislative systems.

The v0 metrics should be read as comparative indicators:

- `legalStability`: precedent continuity and low conflict escalation.
- `rightsProtection`: protection of high-burden cases without ignoring democratic mandate.
- `partisanAlignment`: how much outcomes track partisan direction rather than legal risk.
- `shadowDocketAbuse`: emergency or unexplained relief outside merits review.
- `legitimacy`: public attention, recusal discipline, reason-giving, and low partisan odor.
- `reversalRate`: frequency of precedent/law reversals.
- `constitutionalConflict`: institutional conflict after decisions and overrides.
- `democraticResponsiveness`: respect for public mandate and clear override channels without swallowing rights constraints.
