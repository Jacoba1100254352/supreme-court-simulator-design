# ECtHR Execution Monitoring Summary v1

This report summarizes the generated HUDOC-EXEC pending leading-case monitoring slice. It is direct row-level monitoring evidence for the implementation/compliance workqueue's monitoring-capacity slice, not validation evidence for lower-court compliance, implementation resistance, government noncompliance, or emergency downstream effects.

| Metric | Value | Manuscript use | Notes |
| --- | ---: | --- | --- |
| `ecthrHudocExecPendingLeadingRows` | 1450 | can support bounded monitoring-capacity evidence, not lower-court compliance validation | Rows reconcile to the live HUDOC-EXEC API result count for the documented query. |
| `ecthrHudocExecEnhancedSupervisionRows` | 613 | can support bounded enhanced-supervision monitoring-capacity evidence | Rows with execsupervision=ENHA. |
| `ecthrHudocExecStandardSupervisionRows` | 830 | can support bounded standard-supervision monitoring-capacity evidence | Rows with execsupervision=STAND. |
| `ecthrHudocExecNewClassificationRows` | 7 | can support bounded awaiting-classification monitoring-capacity evidence | Rows with execsupervision=NEW. |
| `ecthrHudocExecPendingOverFiveYearsRows` | 754 | can support bounded long-pending monitoring-capacity evidence | Computed from final-judgment or judgment date to the snapshot date. |
