# Emergency Application Order Reconciliation v1

This report checks the compact Shadow Docket Database v3.0 full-court emergency-application extract against the normalized term-summary counts already used for calibration guardrails. It is application-level denominator evidence for the selected terms, not merits-follow-through or downstream-effect validation.

| Term | Applications | Summary applications | Grants | Summary grants | Public disagreement | Summary disagreement | Status | Manuscript use |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| OT2023 | 116 | 116 | 11 | 11 | 27 | 27 | matches_calibration_summary | application-level denominator guardrail only; no merits-follow-through or downstream-effect validation |
| OT2024 | 125 | 125 | 20 | 20 | 36 | 36 | matches_calibration_summary | application-level denominator guardrail only; no merits-follow-through or downstream-effect validation |

Boundary note:

- The extract uses `emergency_application=1` and `full_court=1`, matching the normalized shadow-docket summary denominator. The row dates are order dates, not filing dates. The extract does not code merits follow-through, status-quo effect, or downstream policy implementation.
