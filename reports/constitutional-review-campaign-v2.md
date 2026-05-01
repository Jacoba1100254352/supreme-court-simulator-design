# Constitutional Review Campaign v2

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 13
- experiment cases: 20

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
| Low Appointment Capture | 0.750 | neutral synthetic legislature | Appointment incentives are less partisan and the justice pool is less polarized. |
| Extreme Appointment Capture | 1.000 | neutral synthetic legislature | Appointment incentives are highly partisan and vacancies become ideological leverage points. |
| Low Emergency Pressure | 0.750 | neutral synthetic legislature | Few cases arrive through urgent stay requests or executive emergency disputes. |
| Extreme Emergency Pressure | 1.000 | extreme-emergency synthetic legislature | Emergency applications, executive-power disputes, and time-sensitive election conflicts are common. |
| Low Rights Risk | 0.750 | low-rights-risk synthetic legislature | Legislative output is legally careful, low-volatility, and rarely burdens protected interests. |
| Extreme Rights Risk | 1.000 | extreme-rights-risk synthetic legislature | Legislative output often creates concentrated rights burdens under contested public mandates. |
| Weak-Mandate Legislation | 1.000 | weak-mandate synthetic legislature | Many reviewed laws have low public legitimacy and high override pressure after invalidation. |
| Strong-Mandate Legislation | 0.750 | strong-mandate synthetic legislature | Popular legislation creates the hardest democratic-responsiveness pressure for review. |
| Appointment Timing Manipulation | 1.000 | adversarial/imported blend | Political actors time vacancies under high capture and public pressure. |
| Emergency Application Flood | 1.000 | emergency-flood synthetic legislature | Executives and litigants route controversial policies through urgent stay requests. |
| Override Evasion Loop | 1.000 | override-evasion synthetic legislature | Legislatures repeatedly revise invalidated laws to test rights carveouts and override thresholds. |
| Recusal Pressure Campaign | 0.850 | recusal-pressure synthetic legislature | High-salience litigants try to force or avoid recusals around ideologically charged cases. |
| Court Expansion Retaliation | 0.850 | expansion-retaliation synthetic legislature | A polarized political system reacts to judicial conflict with expansion threats and capture pressure. |

## Headline Findings

- Highest directional score: 60 percent invalidation threshold at 0.786.
- Highest rights protection: Dual supreme courts with disagreement filter at 0.703.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.001.
- Lowest partisan alignment: Dual supreme courts with disagreement filter at 0.029.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, and administrative feasibility.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Lower `partisanAlignment`, `shadowDocketAbuse`, `reversalRate`, `constitutionalConflict`, and `administrativeCost` are usually better.
- Invalidation, emergency, replacement, recusal, concurrence, dissent, panel, en banc, council, cross-check, and override rates are diagnostic.

## Scenario Averages Across Cases

| Scenario | Directional | Stability/rights | Legitimacy/control | Legal stability | Precedent | Statutory | Compliance | Rights protection | Partisan align. | Shadow abuse | Legitimacy | Reversal | Conflict | Responsiveness | Admin cost | Merits accel. | Replacement | Override att. | Override |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.786 | 0.784 | 0.842 | 0.751 | 0.955 | 0.698 | 0.600 | 0.696 | 0.071 | 0.049 | 0.795 | 0.018 | 0.294 | 0.712 | 0.266 | 0.196 | 0.024 | 0.000 | 0.000 |
| 18-year staggered terms + regular appointments | 0.784 | 0.783 | 0.840 | 0.748 | 0.939 | 0.704 | 0.599 | 0.702 | 0.072 | 0.066 | 0.800 | 0.023 | 0.295 | 0.718 | 0.272 | 0.297 | 0.104 | 0.000 | 0.000 |
| Stylized current U.S.-like supreme court | 0.777 | 0.782 | 0.772 | 0.744 | 0.928 | 0.705 | 0.599 | 0.702 | 0.071 | 0.238 | 0.678 | 0.021 | 0.296 | 0.716 | 0.222 | 0.000 | 0.025 | 0.000 | 0.000 |
| Nonpartisan commission appointments | 0.776 | 0.783 | 0.847 | 0.749 | 0.943 | 0.706 | 0.599 | 0.701 | 0.046 | 0.066 | 0.805 | 0.022 | 0.295 | 0.717 | 0.302 | 0.295 | 0.104 | 0.000 | 0.000 |
| No emergency relief without merits review | 0.776 | 0.785 | 0.869 | 0.756 | 0.958 | 0.711 | 0.600 | 0.695 | 0.047 | 0.001 | 0.844 | 0.017 | 0.294 | 0.712 | 0.326 | 0.446 | 0.103 | 0.000 | 0.000 |
| Retention-election accountability court | 0.776 | 0.782 | 0.847 | 0.752 | 0.949 | 0.708 | 0.597 | 0.696 | 0.050 | 0.066 | 0.807 | 0.020 | 0.298 | 0.718 | 0.302 | 0.300 | 0.107 | 0.038 | 0.012 |
| Three-judge panels with en banc correction | 0.775 | 0.783 | 0.857 | 0.749 | 0.943 | 0.705 | 0.599 | 0.700 | 0.082 | 0.066 | 0.901 | 0.023 | 0.295 | 0.717 | 0.314 | 0.295 | 0.447 | 0.000 | 0.000 |
| Judicial review with legislative supermajority override | 0.774 | 0.782 | 0.852 | 0.747 | 0.941 | 0.704 | 0.596 | 0.701 | 0.030 | 0.066 | 0.808 | 0.022 | 0.300 | 0.719 | 0.312 | 0.297 | 0.105 | 0.044 | 0.006 |
| Peer recusal + reasoned emergency docket | 0.771 | 0.783 | 0.840 | 0.749 | 0.943 | 0.705 | 0.599 | 0.701 | 0.073 | 0.066 | 0.804 | 0.023 | 0.295 | 0.717 | 0.312 | 0.297 | 0.104 | 0.000 | 0.000 |
| Expanded 15-seat court | 0.770 | 0.783 | 0.848 | 0.749 | 0.942 | 0.705 | 0.599 | 0.701 | 0.046 | 0.067 | 0.811 | 0.023 | 0.295 | 0.718 | 0.322 | 0.296 | 0.103 | 0.000 | 0.000 |
| Pre-enactment constitutional council | 0.761 | 0.784 | 0.867 | 0.755 | 0.953 | 0.709 | 0.604 | 0.696 | 0.056 | 0.066 | 0.912 | 0.018 | 0.298 | 0.721 | 0.368 | 0.297 | 0.169 | 0.035 | 0.007 |
| Supreme court with cross-checking constitutional court | 0.736 | 0.771 | 0.855 | 0.738 | 0.950 | 0.694 | 0.569 | 0.692 | 0.031 | 0.049 | 0.813 | 0.015 | 0.332 | 0.710 | 0.417 | 0.197 | 0.141 | 0.000 | 0.000 |
| Dual supreme courts with disagreement filter | 0.720 | 0.768 | 0.858 | 0.727 | 0.924 | 0.688 | 0.568 | 0.703 | 0.029 | 0.049 | 0.818 | 0.022 | 0.334 | 0.717 | 0.468 | 0.194 | 0.144 | 0.000 | 0.000 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Baseline | 60 percent invalidation threshold (0.806) | Stylized current U.S.-like supreme court (0.718) | No emergency relief without merits review (0.000) | Dual supreme courts with disagreement filter (0.020) |
| Partisan Appointment Pressure | 60 percent invalidation threshold (0.807) | Stylized current U.S.-like supreme court (0.720) | No emergency relief without merits review (0.000) | Dual supreme courts with disagreement filter (0.022) |
| Rights-Risk Legislation | 60 percent invalidation threshold (0.780) | 18-year staggered terms + regular appointments (0.676) | No emergency relief without merits review (0.000) | Dual supreme courts with disagreement filter (0.026) |
| Shadow-Docket Stress | 60 percent invalidation threshold (0.770) | Dual supreme courts with disagreement filter (0.697) | No emergency relief without merits review (0.002) | Judicial review with legislative supermajority override (0.028) |
| High Democratic Mandate | 60 percent invalidation threshold (0.817) | Dual supreme courts with disagreement filter (0.726) | No emergency relief without merits review (0.000) | Dual supreme courts with disagreement filter (0.012) |
| Constitutional Conflict | 60 percent invalidation threshold (0.765) | Stylized current U.S.-like supreme court (0.688) | No emergency relief without merits review (0.003) | Dual supreme courts with disagreement filter (0.045) |
| Imported Legislative Output | 60 percent invalidation threshold (0.809) | Stylized current U.S.-like supreme court (0.725) | No emergency relief without merits review (0.000) | Judicial review with legislative supermajority override (0.018) |
| Low Appointment Capture | 60 percent invalidation threshold (0.806) | Dual supreme courts with disagreement filter (0.718) | No emergency relief without merits review (0.000) | Dual supreme courts with disagreement filter (0.013) |
| Extreme Appointment Capture | 60 percent invalidation threshold (0.804) | Dual supreme courts with disagreement filter (0.720) | No emergency relief without merits review (0.000) | Dual supreme courts with disagreement filter (0.027) |
| Low Emergency Pressure | 60 percent invalidation threshold (0.811) | Dual supreme courts with disagreement filter (0.719) | No emergency relief without merits review (0.000) | Dual supreme courts with disagreement filter (0.018) |
| Extreme Emergency Pressure | 60 percent invalidation threshold (0.755) | Stylized current U.S.-like supreme court (0.687) | No emergency relief without merits review (0.004) | Dual supreme courts with disagreement filter (0.033) |
| Low Rights Risk | 60 percent invalidation threshold (0.824) | Dual supreme courts with disagreement filter (0.742) | No emergency relief without merits review (0.000) | Judicial review with legislative supermajority override (0.011) |
| Extreme Rights Risk | 60 percent invalidation threshold (0.756) | Dual supreme courts with disagreement filter (0.702) | No emergency relief without merits review (0.001) | Dual supreme courts with disagreement filter (0.035) |
| Weak-Mandate Legislation | 60 percent invalidation threshold (0.780) | Expanded 15-seat court (0.703) | No emergency relief without merits review (0.000) | Judicial review with legislative supermajority override (0.024) |
| Strong-Mandate Legislation | 60 percent invalidation threshold (0.821) | Dual supreme courts with disagreement filter (0.730) | No emergency relief without merits review (0.000) | Dual supreme courts with disagreement filter (0.012) |
| Appointment Timing Manipulation | 60 percent invalidation threshold (0.808) | Judicial review with legislative supermajority override (0.726) | No emergency relief without merits review (0.000) | Judicial review with legislative supermajority override (0.027) |
| Emergency Application Flood | No emergency relief without merits review (0.742) | Stylized current U.S.-like supreme court (0.676) | No emergency relief without merits review (0.009) | Dual supreme courts with disagreement filter (0.045) |
| Override Evasion Loop | 60 percent invalidation threshold (0.766) | Dual supreme courts with disagreement filter (0.649) | No emergency relief without merits review (0.001) | Judicial review with legislative supermajority override (0.038) |
| Recusal Pressure Campaign | 60 percent invalidation threshold (0.767) | Stylized current U.S.-like supreme court (0.682) | No emergency relief without merits review (0.003) | Judicial review with legislative supermajority override (0.057) |
| Court Expansion Retaliation | 60 percent invalidation threshold (0.760) | Peer recusal + reasoned emergency docket (0.688) | No emergency relief without merits review (0.004) | Dual supreme courts with disagreement filter (0.061) |
