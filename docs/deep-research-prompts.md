# Deep Research Prompts

Use the shared opening instructions below at the top of each Deep Research request:

> I am building a Java simulator and Journal of Law and Courts-style paper on supreme-court and constitutional-review institutional design. Separate empirical claims, synthetic modeling assumptions, and speculative design recommendations. Use official court statistics, official codebooks, public datasets, peer-reviewed empirical work, and constitutional/legal texts before secondary commentary. Label each quantitative row as strict validation, loose calibration, proxy/context, or design prior. Preserve denominators and coverage scope. Do not blend U.S. certiorari, constitutional complaint, amparo, QPC, abstract review, concrete referral, emergency applications, and post-judgment execution as if they share one denominator. Include ingest-ready markdown tables with columns: variableName, jurisdiction, period, observedValueOrRange, numeratorSpec, denominatorSpec, confidenceLevel, validationUse, coverageScope, comparabilityClass, sourceName, sourceUrl, notes.

Recommended run order after the May 2026 validation hardening:

1. Certiorari cohort and screening data. This is the biggest remaining source-coverage gap because the pathway dashboard still has weak direct denominators for CVSG and genuine split prevalence.
2. Emergency orders and downstream effects. This is the next-highest payoff because emergency relief is central to the paper's main design claim and still needs better linked merits-follow-through evidence.
3. Lower-court behavior, compliance, and monitoring. This should improve the compliance-learning and lower-court-resistance channels.
4. Claimant type, repeat players, and access filters. This improves bar-capital, strategic-plaintiff, and repeat-player learning.
5. Comparative hybrid design packages. Run this last because the design surface is already broad; the first four prompts improve validation more directly.

## Prompt 1: Certiorari Cohort And Screening Data

Research public and academic evidence that can calibrate a multi-stage certiorari intake model. Focus on paid vs IFP petitions, voluntary responses, waivers, calls for response, CVSGs, relists, specialist counsel/former clerks, cert-stage amicus briefs, genuine vs alleged circuit splits, vehicle-quality objections, lower-court origin, and conditional reversal after grant. Prioritize cohort-consistent denominators over same-term docket flows. Identify which variables can support strict validation and which must remain proxy/context. Provide ingest-ready tables and a short explanation of how a simulator should separate petition filing, response/CFR, CVSG, grant, DIG/GVR/summary disposition, merits decision, and reversal.

## Prompt 2: Emergency Orders And Downstream Effects

Research evidence on emergency applications and shadow-docket orders that can calibrate applicant type, capital vs noncapital applications, initial referral, response requested/CFR, amicus participation, relief type, status-quo effect, explanation/reason-giving, public dissent, full-court referral, linked merits petitions, later merits follow-through, and downstream policy effects. Keep applications-docket evidence separate from broader shadow-docket actions. Identify what can be measured directly from public data and what requires hand-linking. Provide ingest-ready rows plus design recommendations for mandatory written emergency reasoning, automatic merits follow-up, automatic expiry, and status-quo metadata.

## Prompt 3: Lower-Court Behavior, Compliance, And Monitoring

Research evidence on how lower courts, agencies, executives, and legislatures respond after constitutional or supreme-court decisions. Separate doctrinal lower-court alignment from practical implementation, enforcement capacity, monitoring, delay, symbolic/narrow compliance, bureaucratic resistance, open defiance, and backlog persistence. Prioritize studies with direct effect sizes, official monitoring reports, and execution-duration data. Include U.S. lower-court precedent-response evidence, agency compliance, comparative constitutional-court monitoring systems, ECtHR execution data, and any public-law systems with compliance dashboards. Provide ingest-ready rows and recommendations for modeling monitoring intensity, compliance speed, fidelity, substantive uptake, and long-tail unresolved cases.

## Prompt 4: Claimant Type, Repeat Players, And Access Filters

Research how claimant type and legal-capacity asymmetries shape constitutional-review pipelines. Focus on individuals, organized rights groups, business repeat players, government SG/AG offices, expert clinics, public-interest litigators, former clerks, state SG offices, specialized bars, court-appointed amici, legal aid, and business/association use of QPC, amparo, constitutional complaint, or certiorari channels. Identify evidence on whether filters reduce weak claims, concentrate elite access, or preserve rights-protective claims. Provide modeling guidance for claimantType, barCapital, claimStrength, vehicleQuality, forumShoppingPressure, strategicPlaintiffSelection, and public-interest filters.

## Prompt 5: Comparative Hybrid Design Packages

Research comparative evidence for hybrid constitutional-review designs that combine concrete referral, filtered individual complaint, abstract ex ante review, emergency review, constitutional remand, legislative override windows, jurisdiction-stripping constraints, randomized panels, and en banc correction. Evaluate which combinations reduce arbitrary emergency power while preserving rights protection, lower-court compliance, democratic responsiveness, and legitimacy. Treat design recommendations as speculative unless supported by direct empirical evidence. Provide ingest-ready tables for access-path volume, admission rates, decision timing, remedy types, override rules, remand/deferred-remedy procedures, panel/en banc structures, and publication/reason-giving requirements.
