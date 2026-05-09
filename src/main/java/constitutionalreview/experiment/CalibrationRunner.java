package constitutionalreview.experiment;

import constitutionalreview.model.LegislativeOutputProfile;
import constitutionalreview.reporting.ReportProvenance;
import constitutionalreview.simulation.Scenario;
import constitutionalreview.simulation.ScenarioCatalog;
import constitutionalreview.simulation.ScenarioReport;
import constitutionalreview.simulation.Simulator;
import constitutionalreview.simulation.WorldSpec;
import constitutionalreview.util.Values;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

public final class CalibrationRunner {
    private CalibrationRunner() {
    }

    public static DiagnosticResult run(
            Path outputDir,
            int runs,
            int casesPerRun,
            long seed,
            LegislativeOutputProfile importedProfile,
            Path legislativeInput
    ) throws IOException {
        return run(outputDir, Path.of("data/calibration"), runs, casesPerRun, seed, importedProfile, legislativeInput);
    }

    public static DiagnosticResult run(
            Path outputDir,
            Path calibrationDataDir,
            int runs,
            int casesPerRun,
            long seed,
            LegislativeOutputProfile importedProfile,
            Path legislativeInput
    ) throws IOException {
        Files.createDirectories(outputDir);
        List<Scenario> scenarios = ScenarioCatalog.scenariosForKeys(List.of(
                "current-us-like",
                "nonpartisan-commission",
                "emergency-restraint-court",
                "legislative-override"
        ));
        LegislativeOutputProfile profile = importedProfile == null ? LegislativeOutputProfile.neutral() : importedProfile;
        List<ScenarioReport> reports = new Simulator().compare(
                scenarios,
                WorldSpec.baseline(casesPerRun, profile),
                runs,
                seed
        );
        Map<String, ScenarioReport> byScenario = new LinkedHashMap<>();
        for (ScenarioReport report : reports) {
            byScenario.put(report.scenarioKey(), report);
        }

        EmpiricalCalibrationDataset dataset = EmpiricalCalibrationDataset.load(calibrationDataDir);
        List<CalibrationTarget> targets = targets(byScenario, dataset);
        Path csvPath = outputDir.resolve("calibration-baseline.csv");
        Path markdownPath = outputDir.resolve("calibration-baseline.md");
        Path manifestPath = outputDir.resolve("calibration-baseline-manifest.json");
        Path appendixCsvPath = outputDir.resolve("calibration-source-ranges-v4.csv");
        Path appendixMarkdownPath = outputDir.resolve("calibration-source-ranges-v4.md");
        List<CalibrationSource> sources = sources();
        Files.writeString(csvPath, csv(targets));
        Files.writeString(markdownPath, markdown(targets, sources, runs, casesPerRun, seed, profile.sourceName(), calibrationDataDir, dataset.observations().size()));
        Files.writeString(appendixCsvPath, dataset.sourceRangesCsv());
        Files.writeString(appendixMarkdownPath, dataset.appendixMarkdown());
        ReportProvenance.write(
                manifestPath,
                "Historical Calibration Baseline v4",
                runs,
                casesPerRun,
                seed,
                1,
                scenarios.size(),
                legislativeInput,
                List.of(csvPath, markdownPath, appendixCsvPath, appendixMarkdownPath)
        );
        return new DiagnosticResult("Historical Calibration Baseline v4", csvPath, markdownPath, manifestPath);
    }

    private static List<CalibrationTarget> targets(Map<String, ScenarioReport> reports, EmpiricalCalibrationDataset dataset) {
        List<CalibrationTarget> targets = new ArrayList<>();
        ScenarioReport current = reports.get("current-us-like");
        ScenarioReport commission = reports.get("nonpartisan-commission");
        ScenarioReport emergency = reports.get("emergency-restraint-court");
        ScenarioReport override = reports.get("legislative-override");

        add(targets, current, "docket-rights", "Rights-related merits domains track SCDB rights issue areas.", "rightsClaimRate", "rightsClaimRate", "strict_validation", 0.10, 0.48, 0.02, "scdb-issue-area", dataset);
        add(targets, current, "docket-admin-law", "Administrative-law challenges track SCDB administrative-action observations.", "administrativeLawRate", "administrativeLawRate", "strict_validation", 0.05, 0.42, 0.02, "scdb-issue-area", dataset);
        add(targets, current, "docket-election", "Election disputes remain a stress domain rather than the whole docket.", "electionDisputeRate", "electionDocketShare", "model_prior_check", 0.02, 0.24, 0.00, "model-docket-mix-prior", dataset);
        add(targets, current, "docket-executive-power", "Executive-power disputes remain visible but bounded within structural public-law disputes.", "executivePowerDisputeRate", "structuralRate", "loose_calibration", 0.03, 0.30, 0.04, "scdb-issue-area", dataset);
        add(targets, current, "current-invalidation", "Declarations of unconstitutionality should be uncommon in the full merits docket.", "invalidationRate", "invalidationRate", "strict_validation", 0.00, 0.22, 0.07, "scdb-unconstitutionality", dataset);
        add(targets, current, "current-merits-transfer", "Admissibility-aware current-like designs should transfer a substantial but not universal share of filed matters to merits.", "meritsTransferRate", "admissibilityModelShare", "model_prior_check", 0.25, 0.85, 0.00, "deep-research-intake-synthesis", dataset);
        add(targets, current, "current-paid-cfr-stage", "Paid cert-style petitions should expose a separate court-requested-response stage rather than a one-step grant draw.", "paidCfrRequestRate", "cfrRate_paid", "loose_calibration", 0.01, 0.12, 0.02, "deep-research-tables-2026", dataset);
        add(targets, current, "current-ifp-cfr-stage", "IFP cert-style petitions should expose a lower-frequency court-requested-response stage.", "ifpCfrRequestRate", "cfrRate_ifp", "loose_calibration", 0.00, 0.08, 0.02, "deep-research-tables-2026", dataset);
        add(targets, current, "current-emergency-applications", "Emergency applications should be present but bounded in the current-like docket.", "emergencyStayDocketRate", "emergencyStayDocketRate", "strict_validation", 0.00, 0.22, 0.20, "shadow-docket-database", dataset);
        add(targets, current, "current-emergency-orders", "Emergency orders should be observable but not universal.", "emergencyOrderRate", "emergencyOrderRate", "loose_calibration", 0.03, 0.60, 0.45, "hlr-emergency", dataset);
        add(targets, current, "current-recusal", "Justice-case recusals should be rare.", "recusalRate", "recusalRate", "strict_validation", 0.00, 0.06, 0.02, "epstein-recusal", dataset);
        add(targets, current, "current-shadow-abuse", "Open emergency procedure creates measurable but bounded shadow-docket abuse.", "shadowDocketAbuse", "shadowDocketAbuse", "loose_calibration", 0.05, 0.60, 0.05, "shadow-docket-database", dataset);
        add(targets, current, "current-precedent-stability", "Precedent stability remains high enough for a stress-inclusive docket with screened and emergency matters.", "precedentStability", "precedentStability", "loose_calibration", 0.55, 1.00, 0.18, "scdb-formal-precedent", dataset);
        add(targets, current, "current-statutory-stability", "Statutory stability remains in a source-derived post-review band.", "statutoryStability", "statutoryStability", "loose_calibration", 0.40, 1.00, 0.22, "scdb-unconstitutionality", dataset);
        add(targets, current, "current-compliance", "Interbranch compliance stays above a low-conflict floor.", "interbranchCompliance", "statutoryStability", "proxy_sanity_check", 0.30, 1.00, 0.42, "hlr-emergency", dataset);
        add(targets, commission, "commission-partisan-alignment", "Commission appointments should keep partisan alignment low.", "partisanAlignment", "shadowDocketAbuse", "proxy_sanity_check", 0.00, 0.18, 0.08, "hlr-voting-alignments", dataset);
        add(targets, emergency, "emergency-restraint-shadow", "No-relief-without-merits should sharply suppress shadow-docket abuse.", "shadowDocketAbuse", "shadowDocketAbuse", "mechanism_sanity_check", 0.00, 0.10, 0.00, "shadow-docket-database", dataset);
        add(targets, emergency, "emergency-restraint-merits-timing", "Emergency-restraint designs should convert urgent matters into merits acceleration.", "meritsAccelerationRate", "emergencyOrderRate", "mechanism_sanity_check", 0.10, 0.75, 0.36, "hlr-emergency", dataset);
        add(targets, override, "override-attempts", "Override designs should produce observable but not constant override attempts.", "overrideAttemptRate", "invalidationRate", "proxy_sanity_check", 0.00, 0.35, 0.18, "scdb-unconstitutionality", dataset);
        return targets;
    }

    private static List<CalibrationSource> sources() {
        return List.of(
                new CalibrationSource(
                        "scdb-issue-area",
                        "Supreme Court Database issue-area codebook",
                        "https://scdb.la.psu.edu/online-codebook/issue-area/",
                        "Maps merits cases into broad legal issue areas such as civil rights, First Amendment, due process, privacy, economic activity, judicial power, and federalism."
                ),
                new CalibrationSource(
                        "scdb-unconstitutionality",
                        "Supreme Court Database declaration-of-unconstitutionality codebook",
                        "https://scdb.la.psu.edu/online-codebook/declaration-of-unconstitutionality/",
                        "Identifies decisions declaring federal, state, territorial, municipal, or local law unconstitutional."
                ),
                new CalibrationSource(
                        "hlr-subject-matter",
                        "Harvard Law Review Supreme Court Statistics, Table III",
                        "https://harvardlawreview.org/supreme-court-statistics/",
                        "Tracks subject matter of full opinions and constitutional holdings in recent terms."
                ),
                new CalibrationSource(
                        "hlr-merits",
                        "Harvard Law Review Supreme Court Statistics, full opinions / merits cases",
                        "https://harvardlawreview.org/supreme-court-statistics/",
                        "Distinguishes full-opinion merits cases from emergency-relief application orders."
                ),
                new CalibrationSource(
                        "hlr-emergency",
                        "Harvard Law Review Supreme Court Statistics, applications for emergency relief",
                        "https://harvardlawreview.org/supreme-court-statistics/",
                        "Tracks dispositions, writings, dissenting votes, and justice agreement in applications for emergency relief."
                ),
                new CalibrationSource(
                        "hlr-voting-alignments",
                        "Harvard Law Review Supreme Court Statistics, voting alignments",
                        "https://harvardlawreview.org/supreme-court-statistics/",
                        "Tracks justice alignment patterns in merits opinions and emergency-relief orders."
                ),
                new CalibrationSource(
                        "shadow-docket-database",
                        "Kastellec and Taboni, Supreme Court Shadow Docket Database, 1993-2025",
                        "https://www.cambridge.org/core/journals/journal-of-law-and-courts/article/database-of-the-united-states-supreme-courts-shadow-docket-19932025/266C0FA883BE4120FB4F37D387EFC61E",
                        "Parses Journal orders and separately tracks emergency applications, including stays, injunctions, and vacatur requests."
                ),
                new CalibrationSource(
                        "epstein-recusal",
                        "Black and Epstein, Recusals and the Problem of an Equally Divided Supreme Court",
                        "https://epstein.wustl.edu/recusal",
                        "Reports 599 post-1946 recusal cases and treats recusals as rare case-level events."
                ),
                new CalibrationSource(
                        "scdb-formal-precedent",
                        "Supreme Court Database formal alteration of precedent variable",
                        "https://scdb.la.psu.edu/online-codebook/formal-alteration-of-precedent/",
                        "Provides a historical anchor for rare formal precedent alteration."
                ),
                new CalibrationSource(
                        "deep-research-intake-synthesis",
                        "Normalized comparative intake source-register rows",
                        "data/calibration/supreme-court-synthesis/source-register.csv",
                        "Preserves named-source intake-denominator rows with validation-use and coverage metadata; used here as a structural guardrail rather than a one-to-one empirical target."
                ),
                new CalibrationSource(
                        "deep-research-tables-2026",
                        "Normalized Supreme Court simulator research-table source register",
                        "data/calibration/supreme-court-research-2026/source-register.csv",
                        "Preserves named-source rows from the 2026 markdown-table reports, including certiorari CFR/CVSG, emergency applications, comparative access paths, lower-court compliance, and repeat-player evidence."
                ),
                new CalibrationSource(
                        "model-docket-mix-prior",
                        "Simulator docket-mix prior",
                        "src/main/java/constitutionalreview/simulation/WorldGenerator.java",
                        "Defines stress-domain bounds for generated docket categories that do not map cleanly to a single empirical source denominator."
                )
        );
    }

    private static void add(
            List<CalibrationTarget> targets,
            ScenarioReport report,
            String key,
            String label,
            String metric,
            String sourceMetric,
            String guardrailClass,
            double min,
            double max,
            double tolerance,
            String sourceKey,
            EmpiricalCalibrationDataset dataset
    ) {
        double observed = metric(report, metric);
        EmpiricalCalibrationDataset.CalibrationRange range = dataset.range(sourceMetric, min, max, tolerance);
        targets.add(new CalibrationTarget(
                key,
                label,
                report.scenarioKey(),
                report.scenarioName(),
                metric,
                sourceMetric,
                guardrailClass,
                observed,
                range.min(),
                range.max(),
                range.median(),
                range.observations(),
                range.termRange(),
                range.sourceKeys().isBlank() ? sourceKey : range.sourceKeys(),
                range.basis(),
                sourceKey,
                sourceTier(sourceKey, range.sourceKeys(), range.basis()),
                observed >= range.min() && observed <= range.max()
        ));
    }

    private static String sourceTier(String sourceKey, String sourceKeys, String rangeBasis) {
        String combined = (sourceKey + " " + sourceKeys + " " + rangeBasis).toLowerCase(Locale.ROOT);
        if (combined.contains("fallback") || combined.contains("model-docket-mix-prior")) {
            return "model_prior";
        }
        if (combined.contains("deep-research")
                || combined.contains("supreme-court-synthesis")
                || combined.contains("supreme-court-research")) {
            return "research_synthesis";
        }
        if (combined.contains("scdb")
                || combined.contains("shadow-docket")
                || combined.contains("epstein")
                || combined.contains("harvard")) {
            return "raw_or_primary_summary";
        }
        return "source_register";
    }

    private static double metric(ScenarioReport report, String metric) {
        return switch (metric) {
            case "facialChallengeRate" -> report.facialChallengeRate();
            case "asAppliedChallengeRate" -> report.asAppliedChallengeRate();
            case "electionDisputeRate" -> report.electionDisputeRate();
            case "emergencyStayDocketRate" -> report.emergencyStayDocketRate();
            case "executivePowerDisputeRate" -> report.executivePowerDisputeRate();
            case "administrativeLawRate" -> report.administrativeLawRate();
            case "rightsClaimRate" -> report.rightsClaimRate();
            case "invalidationRate" -> report.invalidationRate();
            case "meritsReviewRate" -> report.meritsReviewRate();
            case "meritsTransferRate" -> report.meritsTransferRate();
            case "paidCfrRequestRate" -> report.paidCfrRequestRate();
            case "ifpCfrRequestRate" -> report.ifpCfrRequestRate();
            case "courtRequestedResponseRate" -> report.courtRequestedResponseRate();
            case "cvsgRequestRate" -> report.cvsgRequestRate();
            case "emergencyOrderRate" -> report.emergencyOrderRate();
            case "meritsAccelerationRate" -> report.meritsAccelerationRate();
            case "recusalRate" -> report.recusalRate();
            case "shadowDocketAbuse" -> report.shadowDocketAbuse();
            case "precedentStability" -> report.precedentStability();
            case "statutoryStability" -> report.statutoryStability();
            case "interbranchCompliance" -> report.interbranchCompliance();
            case "partisanAlignment" -> report.partisanAlignment();
            case "overrideAttemptRate" -> report.overrideAttemptRate();
            default -> throw new IllegalArgumentException("Unknown calibration metric: " + metric);
        };
    }

    private static String csv(List<CalibrationTarget> targets) {
        StringBuilder builder = new StringBuilder();
        builder.append(String.join(",",
                "targetKey",
                "target",
                "scenarioKey",
                "scenario",
                "metric",
                "sourceMetric",
                "guardrailClass",
                "observed",
                "min",
                "max",
                "sourceMedian",
                "sourceObservations",
                "sourceTerms",
                "rangeBasis",
                "sourceKey",
                "sourceTier",
                "pass"
        )).append('\n');
        for (CalibrationTarget target : targets) {
            builder.append(Values.csv(target.key())).append(',')
                    .append(Values.csv(target.label())).append(',')
                    .append(Values.csv(target.scenarioKey())).append(',')
                    .append(Values.csv(target.scenarioName())).append(',')
                    .append(Values.csv(target.metric())).append(',')
                    .append(Values.csv(target.sourceMetric())).append(',')
                    .append(Values.csv(target.guardrailClass())).append(',')
                    .append(format(target.observed())).append(',')
                    .append(format(target.min())).append(',')
                    .append(format(target.max())).append(',')
                    .append(format(target.sourceMedian())).append(',')
                    .append(target.sourceObservations()).append(',')
                    .append(Values.csv(target.sourceTermRange())).append(',')
                    .append(Values.csv(target.rangeBasis())).append(',')
                    .append(Values.csv(target.sourceKeys())).append(',')
                    .append(Values.csv(target.sourceTier())).append(',')
                    .append(target.pass())
                    .append('\n');
        }
        return builder.toString();
    }

    private static String markdown(
            List<CalibrationTarget> targets,
            List<CalibrationSource> sources,
            int runs,
            int casesPerRun,
            long seed,
            String profileName,
            Path calibrationDataDir,
            int sourceObservationCount
    ) {
        long passed = targets.stream().filter(CalibrationTarget::pass).count();
        StringBuilder builder = new StringBuilder();
        builder.append("# Historical Calibration Baseline v4\n\n");
        builder.append("Empirical plausibility checks for the constitutional-review simulator. Target ranges are computed from normalized source observations and widened by metric-specific model tolerances; they remain calibration guardrails, not validation.\n\n");
        builder.append("## Run Configuration\n\n");
        builder.append("- runs: ").append(runs).append('\n');
        builder.append("- cases per run: ").append(casesPerRun).append('\n');
        builder.append("- seed: ").append(seed).append('\n');
        builder.append("- legislative profile: ").append(profileName).append("\n\n");
        builder.append("- calibration data directory: `").append(calibrationDataDir).append("`\n");
        builder.append("- source observations: ").append(sourceObservationCount).append("\n\n");
        builder.append("## Summary\n\n");
        builder.append("- targets within assigned ranges: ").append(passed).append(" / ").append(targets.size()).append("\n");
        builder.append("- guardrail-use counts: ").append(guardrailClassSummary(targets)).append("\n\n");
        builder.append("## Sources\n\n");
        builder.append("| Key | Source | Basis |\n");
        builder.append("| --- | --- | --- |\n");
        for (CalibrationSource source : sources) {
            builder.append("| `")
                    .append(source.key())
                    .append("` | [")
                    .append(source.name())
                    .append("](")
                    .append(source.url())
                    .append(") | ")
                    .append(source.basis())
                    .append(" |\n");
        }
        builder.append("## Targets\n\n");
        builder.append("| Target | Scenario | Use | Evidence tier | Metric | Source metric | Observed | Range | Source median | Source obs. | Source terms | Status |\n");
        builder.append("| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- |\n");
        for (CalibrationTarget target : targets) {
            builder.append("| ")
                    .append(target.label())
                    .append(" | ")
                    .append(target.scenarioName())
                    .append(" | `")
                    .append(target.guardrailClass())
                    .append("` | `")
                    .append(target.sourceTier())
                    .append("` | `")
                    .append(target.metric())
                    .append("` | ")
                    .append("`")
                    .append(target.sourceMetric())
                    .append("` | ")
                    .append(format(target.observed()))
                    .append(" | ")
                    .append(format(target.min()))
                    .append("-")
                    .append(format(target.max()))
                    .append(" | ")
                    .append(format(target.sourceMedian()))
                    .append(" | ")
                    .append(target.sourceObservations())
                    .append(" | ")
                    .append(target.sourceTermRange())
                    .append(" | ")
                    .append(target.pass() ? "within range" : "review")
                    .append(" |\n");
        }
        builder.append("\nSee `calibration-source-ranges-v4.md` for the generated source-range appendix.\n");
        return builder.toString();
    }

    private static String format(double value) {
        return String.format(Locale.ROOT, "%.3f", value);
    }

    private static String guardrailClassSummary(List<CalibrationTarget> targets) {
        Map<String, Integer> counts = new LinkedHashMap<>();
        for (CalibrationTarget target : targets) {
            counts.merge(target.guardrailClass(), 1, Integer::sum);
        }
        StringBuilder builder = new StringBuilder();
        for (Map.Entry<String, Integer> entry : counts.entrySet()) {
            if (!builder.isEmpty()) {
                builder.append(", ");
            }
            builder.append(entry.getKey()).append("=").append(entry.getValue());
        }
        return builder.toString();
    }

    private record CalibrationTarget(
            String key,
            String label,
            String scenarioKey,
            String scenarioName,
            String metric,
            String sourceMetric,
            String guardrailClass,
            double observed,
            double min,
            double max,
            double sourceMedian,
            int sourceObservations,
            String sourceTermRange,
            String sourceKeys,
            String rangeBasis,
            String sourceKey,
            String sourceTier,
            boolean pass
    ) {
    }

    private record CalibrationSource(
            String key,
            String name,
            String url,
            String basis
    ) {
    }
}
