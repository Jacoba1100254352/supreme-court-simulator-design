# Constitutional Review Campaign v0

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 13
- experiment cases: 7

- legislative input: simulation-campaign-v21-paper.csv: volume=0.324 quality=0.617 weakMandate=0.174 rightsRisk=0.106 partisanSkew=0.233 volatility=0.121 legitimacy=0.550

## Case Weights

| Case | Weight | Legislative source | Description |
| --- | ---: | --- | --- |
| Baseline | 1.000 | neutral synthetic legislature | Moderate polarization, ordinary emergency pressure, and neutral legislative output. |
| Partisan Appointment Pressure | 1.000 | neutral synthetic legislature | High appointment capture and polarized justice pool. |
| Rights-Risk Legislation | 1.000 | rights-risk synthetic legislature | Legislative output creates concentrated rights burdens and weak mandates. |
| Shadow-Docket Stress | 1.000 | emergency-pressure synthetic legislature | High emergency pressure and executive-defiance disputes. |
| High Democratic Mandate | 1.000 | high-mandate synthetic legislature | Popular, high-mandate laws create accountability pressure against invalidation. |
| Constitutional Conflict | 1.000 | conflict synthetic legislature | Polarized laws, executive defiance, and public attention raise court-legislature conflict. |
| Imported Legislative Output | 1.000 | neutral/imported blend | Docket assumptions derived from a legislative simulator campaign CSV. |

## Headline Findings

- Highest directional score: 60 percent invalidation threshold at 0.817.
- Highest rights protection: Dual supreme courts with disagreement filter at 0.712.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.047.
- Lowest partisan alignment: Dual supreme courts with disagreement filter at 0.023.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, and administrative feasibility.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Lower `partisanAlignment`, `shadowDocketAbuse`, `reversalRate`, `constitutionalConflict`, and `administrativeCost` are usually better.
- Invalidation, emergency, recusal, concurrence, dissent, panel, en banc, council, cross-check, and override rates are diagnostic.

## Scenario Averages Across Cases

| Scenario | Directional | Stability/rights | Legitimacy/control | Legal stability | Rights protection | Partisan align. | Shadow abuse | Legitimacy | Reversal | Conflict | Responsiveness | Admin cost | Invalidation | Override |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.817 | 0.852 | 0.834 | 0.974 | 0.708 | 0.056 | 0.077 | 0.772 | 0.009 | 0.266 | 0.712 | 0.234 | 0.043 | 0.000 |
| 18-year staggered terms + regular appointments | 0.810 | 0.850 | 0.825 | 0.967 | 0.712 | 0.057 | 0.107 | 0.755 | 0.012 | 0.267 | 0.715 | 0.244 | 0.058 | 0.000 |
| Stylized current U.S.-like supreme court | 0.809 | 0.848 | 0.795 | 0.958 | 0.711 | 0.056 | 0.190 | 0.712 | 0.012 | 0.267 | 0.715 | 0.214 | 0.058 | 0.000 |
| No emergency relief without merits review | 0.803 | 0.852 | 0.850 | 0.976 | 0.707 | 0.043 | 0.047 | 0.795 | 0.008 | 0.266 | 0.711 | 0.294 | 0.039 | 0.000 |
| Three-judge panels with en banc correction | 0.802 | 0.850 | 0.843 | 0.968 | 0.711 | 0.068 | 0.107 | 0.863 | 0.012 | 0.267 | 0.715 | 0.286 | 0.058 | 0.000 |
| Nonpartisan commission appointments | 0.801 | 0.850 | 0.828 | 0.969 | 0.711 | 0.043 | 0.107 | 0.757 | 0.011 | 0.267 | 0.715 | 0.274 | 0.055 | 0.000 |
| Retention-election accountability court | 0.801 | 0.850 | 0.828 | 0.971 | 0.708 | 0.043 | 0.108 | 0.760 | 0.011 | 0.267 | 0.715 | 0.275 | 0.049 | 0.006 |
| Judicial review with legislative supermajority override | 0.800 | 0.850 | 0.834 | 0.967 | 0.711 | 0.023 | 0.107 | 0.763 | 0.012 | 0.267 | 0.715 | 0.284 | 0.056 | 0.001 |
| Peer recusal + reasoned emergency docket | 0.797 | 0.850 | 0.825 | 0.968 | 0.711 | 0.057 | 0.107 | 0.759 | 0.012 | 0.267 | 0.715 | 0.284 | 0.057 | 0.000 |
| Expanded 15-seat court | 0.796 | 0.850 | 0.833 | 0.967 | 0.712 | 0.034 | 0.107 | 0.766 | 0.012 | 0.267 | 0.715 | 0.294 | 0.058 | 0.000 |
| Pre-enactment constitutional council | 0.788 | 0.851 | 0.847 | 0.971 | 0.707 | 0.056 | 0.108 | 0.867 | 0.009 | 0.267 | 0.716 | 0.333 | 0.043 | 0.005 |
| Supreme court with cross-checking constitutional court | 0.767 | 0.841 | 0.845 | 0.968 | 0.707 | 0.024 | 0.078 | 0.786 | 0.008 | 0.303 | 0.711 | 0.385 | 0.043 | 0.000 |
| Dual supreme courts with disagreement filter | 0.750 | 0.839 | 0.847 | 0.958 | 0.712 | 0.023 | 0.078 | 0.790 | 0.012 | 0.303 | 0.715 | 0.435 | 0.058 | 0.000 |
