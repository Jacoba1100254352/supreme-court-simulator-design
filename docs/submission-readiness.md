# Submission Readiness

## Primary Target

Primary journal target: Journal of Law and Courts.

Reason: its scope explicitly fits judicial institutions, judicial independence, court selection, and theoretical or empirical work on law and courts. The manuscript is now framed as computational institutional design for judicial politics rather than as a software-platform overview.

Current manuscript posture:

- `paper/main.tex` is anonymous by default.
- The source attempts to use the official Cambridge `cup-journal` template with `journal=jlc` when `cup-journal.cls` is available.
- The local build falls back to an article review copy with author-date citations because the local TeX Live Basic installation does not ship Cambridge's class or `biber`.
- Citations are author-date in the local build and are ready for the official template's Chicago author-date pipeline when compiled in the Cambridge/Overleaf environment.

## Immediate Conference Target

Conference on Empirical Legal Studies 2026 is the strongest near-term conference target. As of May 2, 2026, the official page lists October 2-3, 2026 at Northwestern Pritzker School of Law and a June 12, 2026 paper-submission deadline.

Before CELS submission, prioritize:

- Tighten the main calibration/validation section.
- Add at least one benchmark or back-test display.
- Keep the framing empirical: observed inputs, coded rules, assumptions, simulated outputs.

## Files Added for Submission Preparation

- `paper/title-page.tex`: separate non-anonymous title-page skeleton.
- `paper/abstract-variants.md`: CELS, ICON-S, and APSA abstract/proposal variants.
- `REPLICATION.md`: one-command reproduction plan and observed/coded/assumed/simulated memo.

## Remaining No-Regrets Work

- Add a stronger benchmark table to the paper once raw-source refresh is automated.
- Replace placeholder title-page author fields before any non-anonymous submission.
- Prepare a blinded repository or Dataverse placeholder if submitting before public release.
- Decide whether I-CON remains a possible future target before posting a public preprint.
