package constitutionalreview.experiment;

import constitutionalreview.model.LegislativeOutputProfile;
import constitutionalreview.reporting.ReportProvenance;
import constitutionalreview.simulation.Scenario;
import constitutionalreview.simulation.ScenarioCatalog;
import constitutionalreview.simulation.ScenarioReport;
import constitutionalreview.simulation.Simulator;
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

public final class SeedRobustnessRunner {
    private SeedRobustnessRunner() {
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
        List<Long> seeds = seeds(seed);
        List<CampaignCase> cases = CampaignRunner.v2Cases(casesPerRun, importedProfile);
        List<Scenario> scenarios = ScenarioCatalog.defaultScenarios();
        Map<String, RunningScenarioStats> stats = new LinkedHashMap<>();
        Simulator simulator = new Simulator();

        for (long seedValue : seeds) {
            Map<String, WeightedTotals> weighted = new LinkedHashMap<>();
            for (int i = 0; i < cases.size(); i++) {
                CampaignCase campaignCase = cases.get(i);
                List<ScenarioReport> reports = simulator.compare(
                        scenarios,
                        campaignCase.worldSpec(),
                        runs,
                        seedValue + i * 10_003L
                );
                for (ScenarioReport report : reports) {
                    WeightedTotals totals = weighted.computeIfAbsent(
                            report.scenarioKey(),
                            key -> new WeightedTotals(report.scenarioName())
                    );
                    totals.add(campaignCase.weight(), report);
                }
            }
            for (Map.Entry<String, WeightedTotals> entry : weighted.entrySet()) {
                ScenarioSnapshot snapshot = entry.getValue().toSnapshot(entry.getKey());
                stats.computeIfAbsent(entry.getKey(), key -> new RunningScenarioStats(snapshot.scenarioName()))
                        .add(snapshot);
            }
        }

        List<RobustnessRow> rows = stats.entrySet().stream()
                .map(entry -> entry.getValue().toRow(entry.getKey()))
                .sorted(Comparator.comparingDouble(RobustnessRow::directionalMean).reversed())
                .toList();
        Path csvPath = outputDir.resolve("seed-robustness-v2.csv");
        Path markdownPath = outputDir.resolve("seed-robustness-v2.md");
        Path manifestPath = outputDir.resolve("seed-robustness-v2-manifest.json");
        Files.writeString(csvPath, csv(rows));
        Files.writeString(markdownPath, markdown(rows, runs, casesPerRun, seeds, cases.size(), importedProfile));
        ReportProvenance.write(
                manifestPath,
                "Seed Robustness v2",
                runs,
                casesPerRun,
                seed,
                cases.size(),
                scenarios.size(),
                legislativeInput,
                List.of(csvPath, markdownPath)
        );
        return new DiagnosticResult("Seed Robustness v2", csvPath, markdownPath, manifestPath);
    }

    private static List<Long> seeds(long seed) {
        return List.of(seed, seed + 1L, seed + 2L, seed + 3L, seed + 4L);
    }

    private static String csv(List<RobustnessRow> rows) {
        StringBuilder builder = new StringBuilder();
        builder.append(String.join(",",
                "scenarioKey",
                "scenario",
                "seedCount",
                "directionalMean",
                "directionalMin",
                "directionalMax",
                "directionalStddev",
                "legalStabilityMean",
                "legalStabilityStddev",
                "precedentStabilityMean",
                "statutoryStabilityMean",
                "interbranchComplianceMean",
                "rightsProtectionMean",
                "rightsProtectionStddev",
                "shadowDocketAbuseMean",
                "shadowDocketAbuseStddev",
                "constitutionalConflictMean",
                "constitutionalConflictStddev",
                "democraticResponsivenessMean",
                "administrativeCostMean"
        )).append('\n');
        for (RobustnessRow row : rows) {
            builder.append(Values.csv(row.scenarioKey())).append(',')
                    .append(Values.csv(row.scenarioName())).append(',')
                    .append(row.seedCount()).append(',')
                    .append(format(row.directionalMean())).append(',')
                    .append(format(row.directionalMin())).append(',')
                    .append(format(row.directionalMax())).append(',')
                    .append(format(row.directionalStddev())).append(',')
                    .append(format(row.legalStabilityMean())).append(',')
                    .append(format(row.legalStabilityStddev())).append(',')
                    .append(format(row.precedentStabilityMean())).append(',')
                    .append(format(row.statutoryStabilityMean())).append(',')
                    .append(format(row.interbranchComplianceMean())).append(',')
                    .append(format(row.rightsProtectionMean())).append(',')
                    .append(format(row.rightsProtectionStddev())).append(',')
                    .append(format(row.shadowDocketAbuseMean())).append(',')
                    .append(format(row.shadowDocketAbuseStddev())).append(',')
                    .append(format(row.constitutionalConflictMean())).append(',')
                    .append(format(row.constitutionalConflictStddev())).append(',')
                    .append(format(row.democraticResponsivenessMean())).append(',')
                    .append(format(row.administrativeCostMean()))
                    .append('\n');
        }
        return builder.toString();
    }

    private static String markdown(
            List<RobustnessRow> rows,
            int runs,
            int casesPerRun,
            List<Long> seeds,
            int caseCount,
            LegislativeOutputProfile importedProfile
    ) {
        StringBuilder builder = new StringBuilder();
        builder.append("# Seed Robustness v2\n\n");
        builder.append("Weighted v2 campaign averages rerun across deterministic seed offsets.\n\n");
        builder.append("## Run Configuration\n\n");
        builder.append("- runs per case per seed: ").append(runs).append('\n');
        builder.append("- cases per run: ").append(casesPerRun).append('\n');
        builder.append("- experiment cases: ").append(caseCount).append('\n');
        builder.append("- seeds: ").append(seeds).append('\n');
        builder.append("- legislative input: ")
                .append(importedProfile == null ? "neutral synthetic profile" : importedProfile.sourceName())
                .append("\n\n");
        builder.append("## Scenario Robustness\n\n");
        builder.append("| Scenario | Directional mean | Directional range | Std. dev. | Legal stability | Rights | Shadow abuse | Conflict | Compliance | Admin cost |\n");
        builder.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |\n");
        for (RobustnessRow row : rows) {
            builder.append("| ")
                    .append(row.scenarioName())
                    .append(" | ")
                    .append(format(row.directionalMean()))
                    .append(" | ")
                    .append(format(row.directionalMin()))
                    .append("-")
                    .append(format(row.directionalMax()))
                    .append(" | ")
                    .append(format(row.directionalStddev()))
                    .append(" | ")
                    .append(format(row.legalStabilityMean()))
                    .append(" | ")
                    .append(format(row.rightsProtectionMean()))
                    .append(" | ")
                    .append(format(row.shadowDocketAbuseMean()))
                    .append(" | ")
                    .append(format(row.constitutionalConflictMean()))
                    .append(" | ")
                    .append(format(row.interbranchComplianceMean()))
                    .append(" | ")
                    .append(format(row.administrativeCostMean()))
                    .append(" |\n");
        }
        return builder.toString();
    }

    private static String format(double value) {
        return String.format(Locale.ROOT, "%.3f", value);
    }

    private static final class WeightedTotals {
        private final String scenarioName;
        private double weight;
        private double directional;
        private double legalStability;
        private double precedentStability;
        private double statutoryStability;
        private double interbranchCompliance;
        private double rightsProtection;
        private double shadowDocketAbuse;
        private double constitutionalConflict;
        private double democraticResponsiveness;
        private double administrativeCost;

        private WeightedTotals(String scenarioName) {
            this.scenarioName = scenarioName;
        }

        private void add(double rowWeight, ScenarioReport report) {
            weight += rowWeight;
            directional += report.directionalScore() * rowWeight;
            legalStability += report.legalStability() * rowWeight;
            precedentStability += report.precedentStability() * rowWeight;
            statutoryStability += report.statutoryStability() * rowWeight;
            interbranchCompliance += report.interbranchCompliance() * rowWeight;
            rightsProtection += report.rightsProtection() * rowWeight;
            shadowDocketAbuse += report.shadowDocketAbuse() * rowWeight;
            constitutionalConflict += report.constitutionalConflict() * rowWeight;
            democraticResponsiveness += report.democraticResponsiveness() * rowWeight;
            administrativeCost += report.administrativeCost() * rowWeight;
        }

        private ScenarioSnapshot toSnapshot(String scenarioKey) {
            double denominator = Math.max(1.0, weight);
            return new ScenarioSnapshot(
                    scenarioKey,
                    scenarioName,
                    directional / denominator,
                    legalStability / denominator,
                    precedentStability / denominator,
                    statutoryStability / denominator,
                    interbranchCompliance / denominator,
                    rightsProtection / denominator,
                    shadowDocketAbuse / denominator,
                    constitutionalConflict / denominator,
                    democraticResponsiveness / denominator,
                    administrativeCost / denominator
            );
        }
    }

    private static final class RunningScenarioStats {
        private final String scenarioName;
        private final RunningStat directional = new RunningStat();
        private final RunningStat legalStability = new RunningStat();
        private final RunningStat precedentStability = new RunningStat();
        private final RunningStat statutoryStability = new RunningStat();
        private final RunningStat interbranchCompliance = new RunningStat();
        private final RunningStat rightsProtection = new RunningStat();
        private final RunningStat shadowDocketAbuse = new RunningStat();
        private final RunningStat constitutionalConflict = new RunningStat();
        private final RunningStat democraticResponsiveness = new RunningStat();
        private final RunningStat administrativeCost = new RunningStat();

        private RunningScenarioStats(String scenarioName) {
            this.scenarioName = scenarioName;
        }

        private void add(ScenarioSnapshot snapshot) {
            directional.add(snapshot.directional());
            legalStability.add(snapshot.legalStability());
            precedentStability.add(snapshot.precedentStability());
            statutoryStability.add(snapshot.statutoryStability());
            interbranchCompliance.add(snapshot.interbranchCompliance());
            rightsProtection.add(snapshot.rightsProtection());
            shadowDocketAbuse.add(snapshot.shadowDocketAbuse());
            constitutionalConflict.add(snapshot.constitutionalConflict());
            democraticResponsiveness.add(snapshot.democraticResponsiveness());
            administrativeCost.add(snapshot.administrativeCost());
        }

        private RobustnessRow toRow(String scenarioKey) {
            return new RobustnessRow(
                    scenarioKey,
                    scenarioName,
                    directional.count(),
                    directional.mean(),
                    directional.min(),
                    directional.max(),
                    directional.stddev(),
                    legalStability.mean(),
                    legalStability.stddev(),
                    precedentStability.mean(),
                    statutoryStability.mean(),
                    interbranchCompliance.mean(),
                    rightsProtection.mean(),
                    rightsProtection.stddev(),
                    shadowDocketAbuse.mean(),
                    shadowDocketAbuse.stddev(),
                    constitutionalConflict.mean(),
                    constitutionalConflict.stddev(),
                    democraticResponsiveness.mean(),
                    administrativeCost.mean()
            );
        }
    }

    private static final class RunningStat {
        private final List<Double> values = new ArrayList<>();

        private void add(double value) {
            values.add(value);
        }

        private int count() {
            return values.size();
        }

        private double mean() {
            if (values.isEmpty()) {
                return 0.0;
            }
            double total = 0.0;
            for (double value : values) {
                total += value;
            }
            return total / values.size();
        }

        private double min() {
            return values.stream().min(Double::compareTo).orElse(0.0);
        }

        private double max() {
            return values.stream().max(Double::compareTo).orElse(0.0);
        }

        private double stddev() {
            if (values.size() < 2) {
                return 0.0;
            }
            double mean = mean();
            double total = 0.0;
            for (double value : values) {
                double delta = value - mean;
                total += delta * delta;
            }
            return Math.sqrt(total / values.size());
        }
    }

    private record ScenarioSnapshot(
            String scenarioKey,
            String scenarioName,
            double directional,
            double legalStability,
            double precedentStability,
            double statutoryStability,
            double interbranchCompliance,
            double rightsProtection,
            double shadowDocketAbuse,
            double constitutionalConflict,
            double democraticResponsiveness,
            double administrativeCost
    ) {
    }

    private record RobustnessRow(
            String scenarioKey,
            String scenarioName,
            int seedCount,
            double directionalMean,
            double directionalMin,
            double directionalMax,
            double directionalStddev,
            double legalStabilityMean,
            double legalStabilityStddev,
            double precedentStabilityMean,
            double statutoryStabilityMean,
            double interbranchComplianceMean,
            double rightsProtectionMean,
            double rightsProtectionStddev,
            double shadowDocketAbuseMean,
            double shadowDocketAbuseStddev,
            double constitutionalConflictMean,
            double constitutionalConflictStddev,
            double democraticResponsivenessMean,
            double administrativeCostMean
    ) {
    }
}
