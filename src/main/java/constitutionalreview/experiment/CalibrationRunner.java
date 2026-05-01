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

        List<CalibrationTarget> targets = targets(byScenario);
        Path csvPath = outputDir.resolve("calibration-baseline.csv");
        Path markdownPath = outputDir.resolve("calibration-baseline.md");
        Path manifestPath = outputDir.resolve("calibration-baseline-manifest.json");
        List<CalibrationSource> sources = sources();
        Files.writeString(csvPath, csv(targets));
        Files.writeString(markdownPath, markdown(targets, sources, runs, casesPerRun, seed, profile.sourceName()));
        ReportProvenance.write(
                manifestPath,
                "Historical Calibration Baseline v3",
                runs,
                casesPerRun,
                seed,
                1,
                scenarios.size(),
                legislativeInput,
                List.of(csvPath, markdownPath)
        );
        return new DiagnosticResult("Historical Calibration Baseline v3", csvPath, markdownPath, manifestPath);
    }

    private static List<CalibrationTarget> targets(Map<String, ScenarioReport> reports) {
        List<CalibrationTarget> targets = new ArrayList<>();
        ScenarioReport current = reports.get("current-us-like");
        ScenarioReport commission = reports.get("nonpartisan-commission");
        ScenarioReport emergency = reports.get("emergency-restraint-court");
        ScenarioReport override = reports.get("legislative-override");

        add(targets, current, "docket-rights", "Rights-related merits domains stay within a broad SCDB/HLR subject-matter band.", "rightsClaimRate", 0.10, 0.48, "scdb-issue-area");
        add(targets, current, "docket-admin-law", "Administrative-law challenges remain a recurring but not dominant merits domain.", "administrativeLawRate", 0.05, 0.32, "scdb-issue-area");
        add(targets, current, "docket-election", "Election disputes remain a stress domain rather than the whole docket.", "electionDisputeRate", 0.02, 0.24, "hlr-subject-matter");
        add(targets, current, "docket-executive-power", "Executive-power disputes are visible but bounded.", "executivePowerDisputeRate", 0.03, 0.30, "hlr-subject-matter");
        add(targets, current, "docket-facial", "Facial challenges remain a material constitutional-review slice.", "facialChallengeRate", 0.08, 0.45, "scdb-unconstitutionality");
        add(targets, current, "docket-as-applied", "As-applied challenges remain visible but not dominant.", "asAppliedChallengeRate", 0.02, 0.30, "scdb-unconstitutionality");
        add(targets, current, "current-invalidation", "Declarations of unconstitutionality should be uncommon in the full merits docket.", "invalidationRate", 0.00, 0.22, "scdb-unconstitutionality");
        add(targets, current, "current-merits-review", "Current-like cases should usually receive merits review outside pure emergency processing.", "meritsReviewRate", 0.60, 1.00, "hlr-merits");
        add(targets, current, "current-emergency-applications", "Emergency applications should be present but bounded in the current-like docket.", "emergencyStayDocketRate", 0.01, 0.22, "shadow-docket-database");
        add(targets, current, "current-emergency-orders", "Emergency orders should be observable but not universal.", "emergencyOrderRate", 0.05, 0.60, "hlr-emergency");
        add(targets, current, "current-recusal", "Justice-case recusals should be rare.", "recusalRate", 0.00, 0.06, "epstein-recusal");
        add(targets, current, "current-shadow-abuse", "Open emergency procedure creates measurable but bounded shadow-docket abuse.", "shadowDocketAbuse", 0.05, 0.55, "shadow-docket-database");
        add(targets, current, "current-precedent-stability", "Precedent stability remains high enough for a stable merits court.", "precedentStability", 0.55, 1.00, "scdb-formal-precedent");
        add(targets, current, "current-statutory-stability", "Statutory stability remains in the middle-to-high band after review.", "statutoryStability", 0.40, 1.00, "scdb-unconstitutionality");
        add(targets, current, "current-compliance", "Interbranch compliance stays above a low-conflict floor.", "interbranchCompliance", 0.30, 1.00, "hlr-emergency");
        add(targets, commission, "commission-partisan-alignment", "Commission appointments should keep partisan alignment low.", "partisanAlignment", 0.00, 0.14, "hlr-voting-alignments");
        add(targets, emergency, "emergency-restraint-shadow", "No-relief-without-merits should sharply suppress shadow-docket abuse.", "shadowDocketAbuse", 0.00, 0.08, "shadow-docket-database");
        add(targets, emergency, "emergency-restraint-merits-timing", "Emergency-restraint designs should convert urgent matters into merits acceleration.", "meritsAccelerationRate", 0.10, 0.75, "hlr-emergency");
        add(targets, override, "override-attempts", "Override designs should produce observable but not constant override attempts.", "overrideAttemptRate", 0.00, 0.35, "scdb-unconstitutionality");
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
                )
        );
    }

    private static void add(
            List<CalibrationTarget> targets,
            ScenarioReport report,
            String key,
            String label,
            String metric,
            double min,
            double max,
            String sourceKey
    ) {
        double observed = metric(report, metric);
        targets.add(new CalibrationTarget(
                key,
                label,
                report.scenarioKey(),
                report.scenarioName(),
                metric,
                observed,
                min,
                max,
                sourceKey,
                observed >= min && observed <= max
        ));
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
                "observed",
                "min",
                "max",
                "sourceKey",
                "pass"
        )).append('\n');
        for (CalibrationTarget target : targets) {
            builder.append(Values.csv(target.key())).append(',')
                    .append(Values.csv(target.label())).append(',')
                    .append(Values.csv(target.scenarioKey())).append(',')
                    .append(Values.csv(target.scenarioName())).append(',')
                    .append(Values.csv(target.metric())).append(',')
                    .append(format(target.observed())).append(',')
                    .append(format(target.min())).append(',')
                    .append(format(target.max())).append(',')
                    .append(Values.csv(target.sourceKey())).append(',')
                    .append(target.pass())
                    .append('\n');
        }
        return builder.toString();
    }

    private static String markdown(List<CalibrationTarget> targets, List<CalibrationSource> sources, int runs, int casesPerRun, long seed, String profileName) {
        long passed = targets.stream().filter(CalibrationTarget::pass).count();
        StringBuilder builder = new StringBuilder();
        builder.append("# Historical Calibration Baseline v3\n\n");
        builder.append("Source-backed plausibility checks for the constitutional-review simulator. These ranges are broad guardrails, not empirical validation.\n\n");
        builder.append("## Run Configuration\n\n");
        builder.append("- runs: ").append(runs).append('\n');
        builder.append("- cases per run: ").append(casesPerRun).append('\n');
        builder.append("- seed: ").append(seed).append('\n');
        builder.append("- legislative profile: ").append(profileName).append("\n\n");
        builder.append("## Summary\n\n");
        builder.append("- targets passing: ").append(passed).append(" / ").append(targets.size()).append("\n\n");
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
        builder.append("| Target | Scenario | Metric | Observed | Range | Source | Pass |\n");
        builder.append("| --- | --- | --- | ---: | ---: | --- | --- |\n");
        for (CalibrationTarget target : targets) {
            builder.append("| ")
                    .append(target.label())
                    .append(" | ")
                    .append(target.scenarioName())
                    .append(" | `")
                    .append(target.metric())
                    .append("` | ")
                    .append(format(target.observed()))
                    .append(" | ")
                    .append(format(target.min()))
                    .append("-")
                    .append(format(target.max()))
                    .append(" | ")
                    .append("`")
                    .append(target.sourceKey())
                    .append("` | ")
                    .append(target.pass() ? "pass" : "review")
                    .append(" |\n");
        }
        return builder.toString();
    }

    private static String format(double value) {
        return String.format(Locale.ROOT, "%.3f", value);
    }

    private record CalibrationTarget(
            String key,
            String label,
            String scenarioKey,
            String scenarioName,
            String metric,
            double observed,
            double min,
            double max,
            String sourceKey,
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
