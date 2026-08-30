# Certiorari Term-Flow Reconciliation v1

This report checks the first certiorari petition-denominator source slice against the official OT2023 Journal statistics table. It is a source-quality reconciliation, not a closed petition-cohort validation result.

| Metric | Official count | Official denominator | Official value | Normalized value | Status | Manuscript use |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| `paidPetitionShare` | 1375 | 4222 | 0.3257 | 0.3257 | matches_official_source | term-flow intake guardrail only; not a closed petition-cohort validation row |
| `ifpPetitionShare` | 2847 | 4222 | 0.6743 | 0.6743 | matches_official_source | term-flow intake guardrail only; not a closed petition-cohort validation row |
| `grantSetForArgumentRate_raw` | 69 | 4223 | 0.0163 | 0.0163 | matches_official_source | proxy context only until linked petition-cohort grants are coded |

Denominator notes:

- `paidPetitionShare`: Paid share uses paid plus IFP cases docketed during term; the Journal table also reports one original case, so total cases docketed during term is 4,223.
- `ifpPetitionShare`: IFP share uses paid plus IFP cases docketed during term; the one original case is excluded from the paid/IFP split denominator.
- `grantSetForArgumentRate_raw`: Grant-rate context uses total cases granted plenary review over total cases docketed during term; this is same-term flow, not a closed certiorari petition cohort.
