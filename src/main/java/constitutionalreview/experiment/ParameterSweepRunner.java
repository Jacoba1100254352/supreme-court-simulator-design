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
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

public final class ParameterSweepRunner {
    private ParameterSweepRunner() {
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
        List<SweepWorld> worlds = worlds(casesPerRun, importedProfile);
        List<Scenario> scenarios = ScenarioCatalog.defaultScenarios();
        Simulator simulator = new Simulator();
        Map<String, ScenarioSweepStats> stats = new LinkedHashMap<>();

        for (int i = 0; i < worlds.size(); i++) {
            SweepWorld world = worlds.get(i);
            List<ScenarioReport> reports = simulator.compare(scenarios, world.worldSpec(), runs, seed + i * 10_003L);
            for (ScenarioReport report : reports) {
                stats.computeIfAbsent(report.scenarioKey(), ignored -> new ScenarioSweepStats(report.scenarioName()))
                        .add(report);
            }
        }

        List<SweepRow> rows = stats.entrySet().stream()
                .map(entry -> entry.getValue().toRow(entry.getKey()))
                .sorted(Comparator.comparingDouble(SweepRow::directionalMedian).reversed())
                .toList();
        Path csvPath = outputDir.resolve("parameter-sweep-v4.csv");
        Path markdownPath = outputDir.resolve("parameter-sweep-v4.md");
        Path manifestPath = outputDir.resolve("parameter-sweep-v4-manifest.json");
        Files.writeString(csvPath, csv(rows));
        Files.writeString(markdownPath, markdown(rows, worlds, runs, casesPerRun, seed, importedProfile));
        ReportProvenance.write(
                manifestPath,
                "Parameter Sweep Priors v4",
                runs,
                casesPerRun,
                seed,
                worlds.size(),
                scenarios.size(),
                legislativeInput,
                List.of(csvPath, markdownPath)
        );
        return new DiagnosticResult("Parameter Sweep Priors v4", csvPath, markdownPath, manifestPath);
    }

    private static List<SweepWorld> worlds(int casesPerRun, LegislativeOutputProfile importedProfile) {
        LegislativeOutputProfile neutral = LegislativeOutputProfile.neutral();
        List<SweepWorld> worlds = new ArrayList<>();
        worlds.add(new SweepWorld("baseline", "Baseline institutional prior", 1.00, "Central case for ordinary constitutional review.", WorldSpec.baseline(casesPerRun, neutral)));
        worlds.add(new SweepWorld("low-polarization", "Low-polarization prior", 0.60, "Political branches and candidate pool are less polarized.", new WorldSpec(casesPerRun, 31, 0.32, 0.32, 0.40, 0.16, neutral)));
        worlds.add(new SweepWorld("high-polarization", "High-polarization prior", 0.85, "Polarization and appointment capture both rise.", new WorldSpec(casesPerRun, 31, 0.82, 0.70, 0.58, 0.22, neutral)));
        worlds.add(new SweepWorld("low-appointment-capture", "Low appointment-capture prior", 0.55, "Appointment incentives are less partisan.", new WorldSpec(casesPerRun, 35, 0.42, 0.16, 0.42, 0.16, neutral)));
        worlds.add(new SweepWorld("high-appointment-capture", "High appointment-capture prior", 0.80, "Vacancies become unusually strategic.", new WorldSpec(casesPerRun, 35, 0.80, 0.88, 0.58, 0.22, neutral)));
        worlds.add(new SweepWorld("low-public-pressure", "Low public-pressure prior", 0.45, "Cases receive less public attention.", new WorldSpec(casesPerRun, 31, 0.52, 0.42, 0.18, 0.18, neutral)));
        worlds.add(new SweepWorld("high-public-pressure", "High public-pressure prior", 0.70, "Public attention and accountability pressures rise.", new WorldSpec(casesPerRun, 31, 0.58, 0.46, 0.78, 0.22, neutral)));
        worlds.add(new SweepWorld("low-emergency-share", "Low emergency-share prior", 0.50, "Few cases arrive as urgent applications.", new WorldSpec(casesPerRun, 31, 0.50, 0.40, 0.42, 0.04, neutral)));
        worlds.add(new SweepWorld("high-emergency-share", "High emergency-share prior", 0.85, "Emergency routing becomes institutionally important.", new WorldSpec(casesPerRun, 31, 0.62, 0.56, 0.54, 0.72, emergencyProfile())));
        worlds.add(new SweepWorld("low-rights-risk", "Low rights-risk prior", 0.45, "Legislative outputs rarely burden protected interests.", new WorldSpec(casesPerRun, 31, 0.46, 0.34, 0.50, 0.12, lowRightsProfile())));
        worlds.add(new SweepWorld("high-rights-risk", "High rights-risk prior", 0.85, "Rights burdens and legal defects are common.", new WorldSpec(casesPerRun, 31, 0.64, 0.54, 0.50, 0.26, highRightsProfile())));
        worlds.add(new SweepWorld("weak-mandate", "Weak democratic-mandate prior", 0.75, "Reviewed laws have low public legitimacy.", new WorldSpec(casesPerRun, 31, 0.58, 0.48, 0.42, 0.22, weakMandateProfile())));
        worlds.add(new SweepWorld("high-conflict", "High constitutional-conflict prior", 0.90, "Interbranch conflict and defiance risk rise together.", new WorldSpec(casesPerRun, 31, 0.74, 0.68, 0.62, 0.36, conflictProfile())));
        if (importedProfile != null) {
            worlds.add(new SweepWorld(
                    "imported-legislative-family",
                    "Imported legislative-family prior",
                    0.70,
                    "A congressional simulator output is blended into the docket assumptions.",
                    new WorldSpec(casesPerRun, 31, 0.56, 0.46, 0.48, 0.22, neutral.blend(importedProfile, 0.70).withSourceName("parameter/imported blend"))
            ));
        }
        return worlds;
    }

    private static LegislativeOutputProfile emergencyProfile() {
        return new LegislativeOutputProfile("parameter emergency profile", 0.56, 0.46, 0.36, 0.34, 0.50, 0.68, 0.48, 0.56);
    }

    private static LegislativeOutputProfile lowRightsProfile() {
        return new LegislativeOutputProfile("parameter low-rights profile", 0.42, 0.74, 0.08, 0.06, 0.14, 0.12, 0.74, 0.08);
    }

    private static LegislativeOutputProfile highRightsProfile() {
        return new LegislativeOutputProfile("parameter high-rights profile", 0.62, 0.34, 0.48, 0.78, 0.46, 0.46, 0.40, 0.70);
    }

    private static LegislativeOutputProfile weakMandateProfile() {
        return new LegislativeOutputProfile("parameter weak-mandate profile", 0.58, 0.46, 0.68, 0.34, 0.42, 0.38, 0.30, 0.74);
    }

    private static LegislativeOutputProfile conflictProfile() {
        return new LegislativeOutputProfile("parameter conflict profile", 0.62, 0.42, 0.44, 0.42, 0.70, 0.58, 0.42, 0.72);
    }

    private static String csv(List<SweepRow> rows) {
        StringBuilder builder = new StringBuilder();
        builder.append(String.join(",",
                "scenarioKey",
                "scenario",
                "observations",
                "directionalP05",
                "directionalMedian",
                "directionalP95",
                "legalStabilityP05",
                "legalStabilityMedian",
                "legalStabilityP95",
                "rightsProtectionP05",
                "rightsProtectionMedian",
                "rightsProtectionP95",
                "shadowDocketAbuseP05",
                "shadowDocketAbuseMedian",
                "shadowDocketAbuseP95",
                "constitutionalConflictP05",
                "constitutionalConflictMedian",
                "constitutionalConflictP95",
                "strategicPressureP05",
                "strategicPressureMedian",
                "strategicPressureP95"
        )).append('\n');
        for (SweepRow row : rows) {
            builder.append(Values.csv(row.scenarioKey())).append(',')
                    .append(Values.csv(row.scenarioName())).append(',')
                    .append(row.observations()).append(',')
                    .append(format(row.directionalP05())).append(',')
                    .append(format(row.directionalMedian())).append(',')
                    .append(format(row.directionalP95())).append(',')
                    .append(format(row.legalStabilityP05())).append(',')
                    .append(format(row.legalStabilityMedian())).append(',')
                    .append(format(row.legalStabilityP95())).append(',')
                    .append(format(row.rightsProtectionP05())).append(',')
                    .append(format(row.rightsProtectionMedian())).append(',')
                    .append(format(row.rightsProtectionP95())).append(',')
                    .append(format(row.shadowDocketAbuseP05())).append(',')
                    .append(format(row.shadowDocketAbuseMedian())).append(',')
                    .append(format(row.shadowDocketAbuseP95())).append(',')
                    .append(format(row.constitutionalConflictP05())).append(',')
                    .append(format(row.constitutionalConflictMedian())).append(',')
                    .append(format(row.constitutionalConflictP95())).append(',')
                    .append(format(row.strategicPressureP05())).append(',')
                    .append(format(row.strategicPressureMedian())).append(',')
                    .append(format(row.strategicPressureP95()))
                    .append('\n');
        }
        return builder.toString();
    }

    private static String markdown(
            List<SweepRow> rows,
            List<SweepWorld> worlds,
            int runs,
            int casesPerRun,
            long seed,
            LegislativeOutputProfile importedProfile
    ) {
        StringBuilder builder = new StringBuilder();
        builder.append("# Parameter Sweep Priors v4\n\n");
        builder.append("Scenario bands from named uncertainty priors, not only random seeds. Prior weights are descriptive modeling weights used to document relative plausibility; the percentile bands below still summarize one observation per prior profile.\n\n");
        builder.append("## Run Configuration\n\n");
        builder.append("- runs per sweep world: ").append(runs).append('\n');
        builder.append("- cases per run: ").append(casesPerRun).append('\n');
        builder.append("- base seed: ").append(seed).append('\n');
        builder.append("- named priors: ").append(worlds.size()).append('\n');
        builder.append("- legislative input: ")
                .append(importedProfile == null ? "neutral synthetic profile" : importedProfile.sourceName())
                .append("\n\n");
        builder.append("## Named Prior Profiles\n\n");
        builder.append("| Key | Name | Weight | Legislative source | Rationale |\n");
        builder.append("| --- | --- | ---: | --- | --- |\n");
        for (SweepWorld world : worlds) {
            builder.append("| `")
                    .append(world.key())
                    .append("` | ")
                    .append(world.name())
                    .append(" | ")
                    .append(format(world.priorWeight()))
                    .append(" | ")
                    .append(world.worldSpec().legislativeProfile().sourceName())
                    .append(" | ")
                    .append(world.rationale())
                    .append(" |\n");
        }
        builder.append("\n## Scenario Bands\n\n");
        builder.append("| Scenario | Directional 5/50/95 | Legal 5/50/95 | Rights 5/50/95 | Shadow 5/50/95 | Conflict 5/50/95 | Strategic 5/50/95 |\n");
        builder.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: |\n");
        for (SweepRow row : rows) {
            builder.append("| ")
                    .append(row.scenarioName())
                    .append(" | ")
                    .append(band(row.directionalP05(), row.directionalMedian(), row.directionalP95()))
                    .append(" | ")
                    .append(band(row.legalStabilityP05(), row.legalStabilityMedian(), row.legalStabilityP95()))
                    .append(" | ")
                    .append(band(row.rightsProtectionP05(), row.rightsProtectionMedian(), row.rightsProtectionP95()))
                    .append(" | ")
                    .append(band(row.shadowDocketAbuseP05(), row.shadowDocketAbuseMedian(), row.shadowDocketAbuseP95()))
                    .append(" | ")
                    .append(band(row.constitutionalConflictP05(), row.constitutionalConflictMedian(), row.constitutionalConflictP95()))
                    .append(" | ")
                    .append(band(row.strategicPressureP05(), row.strategicPressureMedian(), row.strategicPressureP95()))
                    .append(" |\n");
        }
        return builder.toString();
    }

    private static String band(double p05, double p50, double p95) {
        return format(p05) + " / " + format(p50) + " / " + format(p95);
    }

    private static String format(double value) {
        return String.format(Locale.ROOT, "%.3f", value);
    }

    private static final class ScenarioSweepStats {
        private final String scenarioName;
        private final List<Double> directional = new ArrayList<>();
        private final List<Double> legalStability = new ArrayList<>();
        private final List<Double> rightsProtection = new ArrayList<>();
        private final List<Double> shadowDocketAbuse = new ArrayList<>();
        private final List<Double> constitutionalConflict = new ArrayList<>();
        private final List<Double> strategicPressure = new ArrayList<>();

        private ScenarioSweepStats(String scenarioName) {
            this.scenarioName = scenarioName;
        }

        private void add(ScenarioReport report) {
            directional.add(report.directionalScore());
            legalStability.add(report.legalStability());
            rightsProtection.add(report.rightsProtection());
            shadowDocketAbuse.add(report.shadowDocketAbuse());
            constitutionalConflict.add(report.constitutionalConflict());
            strategicPressure.add(report.strategicPressure());
        }

        private SweepRow toRow(String scenarioKey) {
            return new SweepRow(
                    scenarioKey,
                    scenarioName,
                    directional.size(),
                    percentile(directional, 0.05),
                    percentile(directional, 0.50),
                    percentile(directional, 0.95),
                    percentile(legalStability, 0.05),
                    percentile(legalStability, 0.50),
                    percentile(legalStability, 0.95),
                    percentile(rightsProtection, 0.05),
                    percentile(rightsProtection, 0.50),
                    percentile(rightsProtection, 0.95),
                    percentile(shadowDocketAbuse, 0.05),
                    percentile(shadowDocketAbuse, 0.50),
                    percentile(shadowDocketAbuse, 0.95),
                    percentile(constitutionalConflict, 0.05),
                    percentile(constitutionalConflict, 0.50),
                    percentile(constitutionalConflict, 0.95),
                    percentile(strategicPressure, 0.05),
                    percentile(strategicPressure, 0.50),
                    percentile(strategicPressure, 0.95)
            );
        }

        private static double percentile(List<Double> values, double percentile) {
            if (values.isEmpty()) {
                return 0.0;
            }
            List<Double> sorted = values.stream().sorted().toList();
            double raw = percentile * (sorted.size() - 1);
            int lower = (int) Math.floor(raw);
            int upper = (int) Math.ceil(raw);
            if (lower == upper) {
                return sorted.get(lower);
            }
            double fraction = raw - lower;
            return sorted.get(lower) * (1.0 - fraction) + sorted.get(upper) * fraction;
        }
    }

    private record SweepWorld(String key, String name, double priorWeight, String rationale, WorldSpec worldSpec) {
    }

    private record SweepRow(
            String scenarioKey,
            String scenarioName,
            int observations,
            double directionalP05,
            double directionalMedian,
            double directionalP95,
            double legalStabilityP05,
            double legalStabilityMedian,
            double legalStabilityP95,
            double rightsProtectionP05,
            double rightsProtectionMedian,
            double rightsProtectionP95,
            double shadowDocketAbuseP05,
            double shadowDocketAbuseMedian,
            double shadowDocketAbuseP95,
            double constitutionalConflictP05,
            double constitutionalConflictMedian,
            double constitutionalConflictP95,
            double strategicPressureP05,
            double strategicPressureMedian,
            double strategicPressureP95
    ) {
    }
}
