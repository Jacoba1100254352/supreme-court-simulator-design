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
        Files.writeString(csvPath, csv(targets));
        Files.writeString(markdownPath, markdown(targets, runs, casesPerRun, seed, profile.sourceName()));
        ReportProvenance.write(
                manifestPath,
                "Calibration Baseline v2",
                runs,
                casesPerRun,
                seed,
                1,
                scenarios.size(),
                legislativeInput,
                List.of(csvPath, markdownPath)
        );
        return new DiagnosticResult("Calibration Baseline v2", csvPath, markdownPath, manifestPath);
    }

    private static List<CalibrationTarget> targets(Map<String, ScenarioReport> reports) {
        List<CalibrationTarget> targets = new ArrayList<>();
        ScenarioReport current = reports.get("current-us-like");
        ScenarioReport commission = reports.get("nonpartisan-commission");
        ScenarioReport emergency = reports.get("emergency-restraint-court");
        ScenarioReport override = reports.get("legislative-override");

        add(targets, current, "docket-facial", "Facial challenges remain a material share of the synthetic docket.", "facialChallengeRate", 0.08, 0.45);
        add(targets, current, "docket-as-applied", "As-applied challenges remain visible but not dominant.", "asAppliedChallengeRate", 0.02, 0.30);
        add(targets, current, "docket-election", "Election disputes are plausible as a stress category.", "electionDisputeRate", 0.06, 0.28);
        add(targets, current, "docket-emergency-stay", "Emergency stay applications are present but not the whole docket.", "emergencyStayDocketRate", 0.01, 0.22);
        add(targets, current, "docket-executive-power", "Executive-power disputes remain a recurring constitutional category.", "executivePowerDisputeRate", 0.06, 0.30);
        add(targets, current, "docket-admin-law", "Administrative-law challenges remain a recurring constitutional category.", "administrativeLawRate", 0.06, 0.30);
        add(targets, current, "docket-rights", "Rights claims remain a major constitutional review category.", "rightsClaimRate", 0.06, 0.35);
        add(targets, current, "current-invalidation", "Current-like invalidation does not dominate the whole docket.", "invalidationRate", 0.00, 0.45);
        add(targets, current, "current-recusal", "Current-like recusals are rare at the justice-case level.", "recusalRate", 0.00, 0.12);
        add(targets, current, "current-shadow-abuse", "Open emergency procedure creates measurable but bounded shadow-docket abuse.", "shadowDocketAbuse", 0.05, 0.45);
        add(targets, current, "current-precedent-stability", "Precedent stability stays in a plausible unit-interval band.", "precedentStability", 0.55, 1.00);
        add(targets, current, "current-statutory-stability", "Statutory stability stays in a plausible unit-interval band.", "statutoryStability", 0.45, 1.00);
        add(targets, current, "current-compliance", "Interbranch compliance stays in a plausible unit-interval band.", "interbranchCompliance", 0.35, 1.00);
        add(targets, commission, "commission-partisan-alignment", "Commission appointments should keep partisan alignment low.", "partisanAlignment", 0.00, 0.12);
        add(targets, emergency, "emergency-restraint-shadow", "No-relief-without-merits should sharply suppress shadow-docket abuse.", "shadowDocketAbuse", 0.00, 0.08);
        add(targets, override, "override-attempts", "Override designs should produce observable but not constant override attempts.", "overrideAttemptRate", 0.00, 0.30);
        return targets;
    }

    private static void add(
            List<CalibrationTarget> targets,
            ScenarioReport report,
            String key,
            String label,
            String metric,
            double min,
            double max
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
                    .append(target.pass())
                    .append('\n');
        }
        return builder.toString();
    }

    private static String markdown(List<CalibrationTarget> targets, int runs, int casesPerRun, long seed, String profileName) {
        long passed = targets.stream().filter(CalibrationTarget::pass).count();
        StringBuilder builder = new StringBuilder();
        builder.append("# Calibration Baseline v2\n\n");
        builder.append("Synthetic plausibility checks for the constitutional-review simulator. These are guardrails, not empirical validation.\n\n");
        builder.append("## Run Configuration\n\n");
        builder.append("- runs: ").append(runs).append('\n');
        builder.append("- cases per run: ").append(casesPerRun).append('\n');
        builder.append("- seed: ").append(seed).append('\n');
        builder.append("- legislative profile: ").append(profileName).append("\n\n");
        builder.append("## Summary\n\n");
        builder.append("- targets passing: ").append(passed).append(" / ").append(targets.size()).append("\n\n");
        builder.append("## Targets\n\n");
        builder.append("| Target | Scenario | Metric | Observed | Range | Pass |\n");
        builder.append("| --- | --- | --- | ---: | ---: | --- |\n");
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
            boolean pass
    ) {
    }
}
