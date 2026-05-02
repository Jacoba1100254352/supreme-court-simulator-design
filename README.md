# Constitutional Review Simulator

This is a separate Java simulation project for comparing supreme-court and constitutional-review institutional designs. It follows the campaign/scenario/report style of the adjacent congressional simulator while keeping the source tree independent.

The simulator evaluates court designs across generated constitutional cases and, optionally, imports legislative campaign outputs as docket inputs. Imported legislative metrics are summarized into a `LegislativeOutputProfile`, which affects case quality, rights risk, weak-mandate disputes, emergency pressure, and constitutional conflict.

## Requirements

- Java 21 or newer
- `make`

There are no external Java dependencies.

## Common Commands

Build:

```sh
make build
```

Run the default scenario comparison:

```sh
make run
```

Run tests:

```sh
make test
```

Build the paper:

```sh
make paper
```

Write the current v2 campaign artifacts:

```sh
make campaign
```

`make campaign` now writes the v2 campaign. The initial v0 and v1 campaigns remain available as `make campaign-v0` and `make campaign-v1`.

Run the diagnostic suite:

```sh
make diagnostics
```

The suite writes source-backed historical calibration guardrails, seed-robustness bands, parameter-sweep uncertainty bands, mechanism ablations, a focused adversarial-manipulation stress campaign, and a multi-family legislative-import comparison.

Run the parameter sweep only:

```sh
make parameter-sweep
```

Compare the import contract against multiple congressional-simulator report families:

```sh
make legislative-family-comparison
```

Set `LEGISLATIVE_FAMILY_DIR=/path/to/reports` to compare a different directory of legislative campaign CSVs.

Use a different normalized empirical calibration-data directory:

```sh
make calibrate CALIBRATION_DATA_DIR=/path/to/calibration
```

Import a legislative simulator report as input:

```sh
make campaign ARGS="--legislative-input '/Users/jacobanderson/Documents/simulators/Congress Institutional Simulator/reports/simulation-campaign-v21-paper.csv'"
```

## Current Design Surface

The catalog includes appointment method, court size, term limits, removal standards, recusal rules, emergency docket procedures, voting thresholds, concurrence/dissent behavior, panel versus en banc review, dual or cross-checking courts, constitutional councils, legislative override rules, and independence/accountability tradeoffs.

The v1 campaign added docket subtypes, justice replacement/vacancy dynamics, richer emergency procedure states, stronger override outcomes, stress-case slices, and sensitivity cases for appointment capture, emergency pressure, rights risk, and weak democratic mandate.

The v2 campaign adds adversarial manipulation cases for appointment timing, emergency-application flooding, override evasion, recusal pressure, and court-expansion retaliation. It also splits legal stability into precedent stability, statutory stability, and interbranch compliance while keeping the blended legal-stability metric for headline comparisons.

The current diagnostics add normalized empirical calibration source tables, source-range appendix reports, legal-domain profiles for rights, election, executive-power, administrative, structural, and economic-regulation cases, review-path/admissibility filtering before merits review, and explicit strategic actor choices for formal legal response and practical implementation. Generated worlds now carry the filed universe directly into petition/admission filtering; there is no preliminary fixed-size top-case certiorari selection before admission.

The review-path model distinguishes certiorari, IFP certiorari, constitutional complaints, amparo, QPC-style filtered referral, abstract ex ante and ex post review, concrete referral, emergency applications, electoral review, and interbranch disputes. Cert-style intake now tracks petition type, SG/CVSG signal, amicus intensity, split maturity, relists, specialist counsel, vehicle defects, and conditional reversal probability.

Emergency applications are first-class objects with applicant/respondent type, application class, requested relief, response request, full-court referral, status-quo effect, public disagreement risk, and merits follow-through. Reports now separate `shadowDocketAbuse` from `emergencyLegitimacyRisk`.

The headline metrics are legal stability, rights protection, partisan alignment, shadow-docket abuse, legitimacy, reversal rate, constitutional conflict, and democratic responsiveness. Direct outputs such as rights-claimant success, domain-specific claimant success, doctrinal depth, remedial breadth, fragmentation, lower-court compliance, elite acceptance, and public confidence are kept separate from derived directional indices.

## Current Reports

- `reports/constitutional-review-campaign-v2.csv` and `.md`: full v2 campaign.
- `reports/calibration-baseline.csv` and `.md`: empirical calibration guardrails computed from normalized source observations.
- `reports/calibration-source-ranges-v4.csv` and `.md`: generated appendix of source ranges by metric.
- `reports/seed-robustness-v2.csv` and `.md`: weighted v2 campaign sensitivity across deterministic seed offsets.
- `reports/mechanism-ablation-v2.csv` and `.md`: pairwise institutional mechanism comparisons.
- `reports/manipulation-stress-v2.csv` and `.md`: focused adversarial stress campaign.
- `reports/parameter-sweep-v4.csv` and `.md`: uncertainty bands from named prior profiles, not only random seeds.
- `reports/legislative-family-comparison-v3.csv` and `.md`: constitutional-review results across multiple congressional-simulator campaign families.

## Calibration Data

Normalized empirical source observations live in `data/calibration/`. Regenerate them from raw SCDB and shadow-docket archives with `tools/build_calibration_tables.py`; raw archives are intentionally not committed. Import the Deep Research synthesis CSV blocks with `tools/import_deep_research_synthesis.py`; those rows preserve `confidenceLevel`, `validationUse`, `denominatorSpec`, `coverageScope`, and `comparabilityClass` so strict validation, loose calibration, and paper context remain distinct.

## Paper

The LaTeX manuscript lives at `paper/main.tex`. It is intentionally framed as a model-and-design paper, not a claim that the current formulas are empirically validated.

The current venue target is Journal of Law and Courts, with CELS 2026 as the near-term conference target. The manuscript is anonymous by default, uses the Cambridge/JLC template path when the official `cup-journal` class is available, and otherwise builds locally as an author-date review copy. Submission-prep notes live in `docs/submission-readiness.md`; reproduction notes live in `REPLICATION.md`.
