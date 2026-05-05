# Submission Readiness

## Primary Target

Primary journal target: Journal of Law and Courts.

Reason: its scope explicitly fits judicial institutions, judicial independence, court selection, and theoretical or empirical work on law and courts. The manuscript is now framed as computational institutional design for judicial politics rather than as a software-platform overview.

Current manuscript posture:

- `paper/main.tex` is anonymous by default.
- The source attempts to use the official Cambridge `cup-journal` template with `journal=jlc` when `cup-journal.cls` is available.
- The local build falls back to an article review copy with author-date citations because the local TeX Live Basic installation does not ship Cambridge's class or `biber`.
- Citations are author-date in the local build and are ready for the official template's Chicago author-date pipeline when compiled in the Cambridge/Overleaf environment.
- Figures are appropriate for this target. JLC's author instructions ask authors to place tables and figures in the manuscript near first reference rather than collecting them at the end. The current manuscript follows that practice with generated campaign figures.
- `make paper-check` now verifies the local manuscript against the JLC-facing requirements that can be checked automatically: anonymous review mode, JLC template options, author-date fallback, declaration sections, figure descriptions, data availability before references, and the 10,000-word article ceiling.
- The manuscript includes a non-identifying AI assistance statement because the project used ChatGPT/Codex and Deep Research synthesis during research, implementation, drafting, and formatting.

## Why JLC Instead of ACM

The adjacent Congress Institutional Simulator uses ACM format because that paper is framed as a computational framework for collective decision-making, compromise, productivity, agenda control, and voting-system design. That framing fits an ACM-style computational social systems / collective intelligence audience and the `acmart` template's computing metadata expectations.

This paper is different. Its central claims are about judicial institutions: constitutional-review access paths, emergency orders, appointment and tenure rules, recusal, voting thresholds, constitutional conflict, legal stability, rights protection, and public legitimacy. Those claims need reviewers who can evaluate law-and-courts theory, comparative constitutional design, judicial-politics framing, and empirical/legal replication expectations.

Practical differences:

- JLC is the stronger substantive home because it is specifically a law-and-courts journal and publishes interdisciplinary work for the law-and-courts community. See the [JLC author instructions](https://www.cambridge.org/core/journals/journal-of-law-and-courts/information/author-instructions/preparing-your-materials).
- JLC's instructions support Word, PDF, or LaTeX review files, anonymous submission, author-date citation, data-availability language, and replication materials through JLC Dataverse at acceptance.
- ACM would be plausible only if the paper were reframed around the simulator as a computing contribution: model architecture, human-centered decision support, collective intelligence, simulation methodology, or software/tooling. That would risk making the constitutional-review substance look like an application case rather than the paper's core contribution.
- ACM production is also stricter about `acmart`, CCS concepts, TAPS compatibility, figure descriptions, and approved LaTeX packages. See ACM's [LaTeX preparation instructions](https://authors.acm.org/proceedings/production-information/preparing-your-article-with-latex). That is manageable, as the Congress paper shows, but it adds constraints without improving venue fit for a judicial-politics manuscript.

Bottom line: keep JLC as the primary journal target and CELS as the near-term feedback venue. Revisit ACM only if the paper is rewritten into a general computational institutional-design methods paper rather than a court-design paper.

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
