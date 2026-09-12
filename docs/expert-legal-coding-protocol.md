# Expert legal coding protocol v1

This is a prepared request for human judgment. No human coding, adjudication or methods approval has been completed by preparing these materials. The existing methods review was performed by AI. The coordinator must verify reviewer qualifications, independence and completion before attributing work to a human reviewer.

## Coordinator workflow

1. Recruit two legally trained readers familiar with judicial opinions and a distinct adjudicator. Assign pseudonymous IDs and retain contact details outside public files. Record any conflicts and the agreed scope privately.
2. Send only the reviewer A ZIP to reader A and the reviewer B ZIP to reader B. Each includes these instructions, identical case cards and an empty form. Keep the coordinator key, automated labels, review stratum and previous AI discussion from the readers until their initial judgments are returned. The published study may already disclose model labels; document any prior exposure rather than claiming perfect blinding.
3. Readers work independently. Keep all 16 rows and source identifiers. Leave every answer field blank for unfinished rows. Never fill human-completion fields on a reader's behalf. Make a working copy of the CSV; generated templates must not store returned work. Regeneration stops before writing if a template contains any completed answer fields, so misplaced returns can be preserved in private storage.
4. Store returns under ignored `data/raw/expert-reviews/` or equivalent private storage. Retain the original returns and their hashes. Run the return validator described below. A complete row needs a human declaration, pseudonymous identity, date, source locator and rationale.
5. After both returns, give the adjudicator the source cards, both judgments and the coordinator key. The adjudicator records a final treatment and reason on every row, including agreements. Do not silently overwrite disagreements. Keep the two independent returns unchanged.
6. Report paired-row raw agreement, the confusion matrix and nominal Cohen's kappa before adjudication. Null kappa means too few pairs or degenerate marginal categories, not perfect reliability. Report the number of unclear judgments. With this small selected packet, no reliability threshold establishes validity; ask the methods reviewer whether further coding is needed.
7. Freeze returned files separately from templates. Incorporating approved judgments into a future benchmark requires a versioned source update, provenance and regenerated analyses. The validator does not modify the empirical snapshot or approve the manuscript.

## Scope and reading task

The packet has 16 citing opinion documents drawn from five salient environmental statutory Supreme Court decisions. It includes every automated directional candidate and two deterministic citation-only documents per source decision. It is a pilot enriched for candidates, not a random sample for estimating population coding accuracy, judicial compliance or resistance. The broader snapshot has 191 published citation-linked documents, with usable public text for 115. Missing and unpublished opinions and legally relevant cases without a citation are outside this pilot.

For each row, read the source Supreme Court decision and the complete citing opinion. Case cards retain context excerpts for navigation; they may overlap, cross a footnote, quote a litigant, or omit a qualification. Record which opinion authored the relevant proposition, the proposition itself, its page/paragraph/footnote and why your treatment classification follows. A dissent's treatment is not necessarily the court's holding. If the source page contains several opinions, identify the relevant one.

## Treatment vocabulary for the pilot

These are operational coding proposals for the reviewers to test; the adjudicator may recommend a documented protocol revision. Retain the original code and explanation if a definition is ambiguous.

| Value | Coding rule |
|---|---|
| `followed` | The citing opinion expressly adopts the source decision's relevant rule or holding as governing the issue before it. |
| `applied` | The opinion uses an identified rule from the source decision to resolve a specific issue on the facts. If both followed and applied fit, use applied and explain the relationship. |
| `distinguished` | The opinion explains a factual or legal difference that limits the source decision's relevance to the present issue. Distinction alone does not establish resistance. |
| `narrowed` | The opinion construes the source decision's scope more narrowly on an identified proposition; record the text supporting that interpretation. |
| `questioned_or_resisted` | The opinion expressly questions or declines the relevant rule; identify the precise proposition, authority and opinion role. Do not infer this from losing litigants or outcomes alone. |
| `cited_context_only` | The decision is cited, quoted, mentioned in background or used for a general proposition without sufficient evidence for a directional treatment judgment under this protocol. |
| `unclear` | The full text is unavailable, opinion attribution is unresolved, or the treatment cannot be determined. Explain the uncertainty; absence of evidence cannot establish an ignored precedent. |

If several treatments occur in one document, record the treatment of the proposition material to the disposition and describe competing passages in `uncertaintyNotes`. If no defensible primary proposition can be identified, use unclear. Do not force every document into a directional category.

## Form fields

Source identity, context hash and URLs are fixed. `coderId` is a pseudonym; `humanCompleted` is `yes` only when that person performed the work. `codedDate` uses YYYY-MM-DD. `fullTextReviewed` is yes/no; no requires unclear treatment. `opinionRole` is majority, plurality, concurrence, dissent, order, combined or unclear. `confidence` is high, medium or low and is a coder assessment, not a probability.

`proposition`, `sourceLocator` and `rationale` are required for completed rows. For unavailable text, identify the attempted source and access limitation in those fields and explain it in `uncertaintyNotes`. Use a page, paragraph or footnote locator that another reader can find.

`remedyFidelity` is full, partial, narrow, symbolic, resistant, not_assessable or not_applicable. Most citation-only documents will not establish fidelity to an actual remedy. A substantive fidelity judgment requires the governing remedial obligation, the actor and a supported comparison to the action taken. Keep this separate from doctrinal treatment; do not infer implementation from a citation or from the Supreme Court's disposition.

## Return validation

From the repository root, after the human readers return their files:

```sh
python3 tools/review_coding_returns.py \
  --reviewer-a data/raw/expert-reviews/reviewer-a.csv \
  --reviewer-b data/raw/expert-reviews/reviewer-b.csv \
  --adjudication data/raw/expert-reviews/adjudication.csv
```

Omit the adjudication argument for a preliminary reliability report. Empty templates produce zero completed reviews and no agreement estimate. The tool checks declared identities and dates but cannot authenticate people or qualifications. Even a completed legal coding packet supplies no external methods signoff and cannot validate the simulator's general compliance parameters.

## Decisions to return to the author

- Are the treatment definitions distinguishable and supported by the cited propositions, especially followed/applied and distinguished/narrowed?
- Which rows quote a party, dissent or general interpretive maxim rather than apply the tracked holding?
- Is any remedy-fidelity judgment supportable from these records, and what additional orders or implementation evidence are needed?
- How should missing full text and the candidate-enriched selection affect reported reliability and publication language?
- What decision selection, legal-issue screening and independent coding would define a relevant-case opportunity denominator including non-citing cases?
- Which manuscript claims, if any, still suggest behavioral validation beyond this evidence?
