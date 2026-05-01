# Constitutional Review Campaign v1

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 13
- experiment cases: 15

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

## Headline Findings

- Highest directional score: 60 percent invalidation threshold at 0.809.
- Highest rights protection: Dual supreme courts with disagreement filter at 0.710.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.001.
- Lowest partisan alignment: Dual supreme courts with disagreement filter at 0.024.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, and administrative feasibility.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Lower `partisanAlignment`, `shadowDocketAbuse`, `reversalRate`, `constitutionalConflict`, and `administrativeCost` are usually better.
- Invalidation, emergency, replacement, recusal, concurrence, dissent, panel, en banc, council, cross-check, and override rates are diagnostic.

## Scenario Averages Across Cases

| Scenario | Directional | Stability/rights | Legitimacy/control | Legal stability | Rights protection | Partisan align. | Shadow abuse | Legitimacy | Reversal | Conflict | Responsiveness | Admin cost | Merits accel. | Replacement | Override att. | Override |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.809 | 0.840 | 0.847 | 0.950 | 0.703 | 0.062 | 0.043 | 0.799 | 0.016 | 0.279 | 0.715 | 0.261 | 0.182 | 0.025 | 0.000 | 0.000 |
| 18-year staggered terms + regular appointments | 0.805 | 0.836 | 0.846 | 0.934 | 0.708 | 0.060 | 0.060 | 0.803 | 0.020 | 0.280 | 0.720 | 0.268 | 0.277 | 0.104 | 0.000 | 0.000 |
| Stylized current U.S.-like supreme court | 0.799 | 0.834 | 0.783 | 0.926 | 0.709 | 0.061 | 0.219 | 0.691 | 0.018 | 0.281 | 0.718 | 0.219 | 0.000 | 0.025 | 0.000 | 0.000 |
| Nonpartisan commission appointments | 0.797 | 0.837 | 0.852 | 0.938 | 0.707 | 0.039 | 0.059 | 0.807 | 0.018 | 0.280 | 0.719 | 0.297 | 0.275 | 0.105 | 0.000 | 0.000 |
| No emergency relief without merits review | 0.797 | 0.840 | 0.872 | 0.953 | 0.702 | 0.040 | 0.001 | 0.842 | 0.015 | 0.279 | 0.714 | 0.321 | 0.416 | 0.103 | 0.000 | 0.000 |
| Retention-election accountability court | 0.797 | 0.837 | 0.851 | 0.945 | 0.703 | 0.043 | 0.059 | 0.809 | 0.017 | 0.283 | 0.719 | 0.298 | 0.280 | 0.105 | 0.035 | 0.011 |
| Three-judge panels with en banc correction | 0.797 | 0.836 | 0.864 | 0.937 | 0.707 | 0.071 | 0.059 | 0.906 | 0.020 | 0.280 | 0.719 | 0.309 | 0.274 | 0.447 | 0.000 | 0.000 |
| Judicial review with legislative supermajority override | 0.795 | 0.835 | 0.857 | 0.935 | 0.709 | 0.025 | 0.059 | 0.810 | 0.019 | 0.285 | 0.721 | 0.307 | 0.275 | 0.105 | 0.042 | 0.005 |
| Peer recusal + reasoned emergency docket | 0.792 | 0.837 | 0.846 | 0.938 | 0.708 | 0.063 | 0.060 | 0.806 | 0.019 | 0.280 | 0.719 | 0.307 | 0.276 | 0.104 | 0.000 | 0.000 |
| Expanded 15-seat court | 0.791 | 0.837 | 0.853 | 0.937 | 0.708 | 0.039 | 0.060 | 0.812 | 0.019 | 0.280 | 0.719 | 0.317 | 0.274 | 0.103 | 0.000 | 0.000 |
| Pre-enactment constitutional council | 0.783 | 0.838 | 0.872 | 0.949 | 0.703 | 0.048 | 0.059 | 0.915 | 0.016 | 0.283 | 0.721 | 0.360 | 0.276 | 0.170 | 0.034 | 0.007 |
| Supreme court with cross-checking constitutional court | 0.759 | 0.829 | 0.859 | 0.947 | 0.700 | 0.025 | 0.043 | 0.815 | 0.013 | 0.316 | 0.713 | 0.412 | 0.184 | 0.142 | 0.000 | 0.000 |
| Dual supreme courts with disagreement filter | 0.741 | 0.822 | 0.862 | 0.916 | 0.710 | 0.024 | 0.043 | 0.819 | 0.020 | 0.318 | 0.720 | 0.462 | 0.181 | 0.144 | 0.000 | 0.000 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Baseline | 60 percent invalidation threshold (0.822) | Stylized current U.S.-like supreme court (0.718) | No emergency relief without merits review (0.000) | Dual supreme courts with disagreement filter (0.020) |
| Partisan Appointment Pressure | 60 percent invalidation threshold (0.823) | Stylized current U.S.-like supreme court (0.720) | No emergency relief without merits review (0.000) | Dual supreme courts with disagreement filter (0.022) |
| Rights-Risk Legislation | 60 percent invalidation threshold (0.798) | 18-year staggered terms + regular appointments (0.676) | No emergency relief without merits review (0.000) | Dual supreme courts with disagreement filter (0.026) |
| Shadow-Docket Stress | 60 percent invalidation threshold (0.789) | Dual supreme courts with disagreement filter (0.697) | No emergency relief without merits review (0.002) | Judicial review with legislative supermajority override (0.028) |
| High Democratic Mandate | 60 percent invalidation threshold (0.832) | Dual supreme courts with disagreement filter (0.726) | No emergency relief without merits review (0.000) | Dual supreme courts with disagreement filter (0.012) |
| Constitutional Conflict | 60 percent invalidation threshold (0.785) | Stylized current U.S.-like supreme court (0.688) | No emergency relief without merits review (0.003) | Dual supreme courts with disagreement filter (0.045) |
| Imported Legislative Output | 60 percent invalidation threshold (0.825) | Stylized current U.S.-like supreme court (0.725) | No emergency relief without merits review (0.000) | Judicial review with legislative supermajority override (0.018) |
| Low Appointment Capture | 60 percent invalidation threshold (0.822) | Dual supreme courts with disagreement filter (0.718) | No emergency relief without merits review (0.000) | Dual supreme courts with disagreement filter (0.013) |
| Extreme Appointment Capture | 60 percent invalidation threshold (0.820) | Dual supreme courts with disagreement filter (0.720) | No emergency relief without merits review (0.000) | Dual supreme courts with disagreement filter (0.027) |
| Low Emergency Pressure | 60 percent invalidation threshold (0.827) | Dual supreme courts with disagreement filter (0.719) | No emergency relief without merits review (0.000) | Dual supreme courts with disagreement filter (0.018) |
| Extreme Emergency Pressure | 60 percent invalidation threshold (0.775) | Stylized current U.S.-like supreme court (0.687) | No emergency relief without merits review (0.004) | Dual supreme courts with disagreement filter (0.033) |
| Low Rights Risk | 60 percent invalidation threshold (0.838) | Dual supreme courts with disagreement filter (0.742) | No emergency relief without merits review (0.000) | Judicial review with legislative supermajority override (0.011) |
| Extreme Rights Risk | 60 percent invalidation threshold (0.760) | Dual supreme courts with disagreement filter (0.702) | No emergency relief without merits review (0.001) | Dual supreme courts with disagreement filter (0.035) |
| Weak-Mandate Legislation | 60 percent invalidation threshold (0.799) | Expanded 15-seat court (0.703) | No emergency relief without merits review (0.000) | Judicial review with legislative supermajority override (0.024) |
| Strong-Mandate Legislation | 60 percent invalidation threshold (0.835) | Dual supreme courts with disagreement filter (0.730) | No emergency relief without merits review (0.000) | Dual supreme courts with disagreement filter (0.012) |
