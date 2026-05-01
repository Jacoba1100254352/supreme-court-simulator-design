package constitutionalreview.experiment;

import constitutionalreview.importer.LegislativeOutputImporter;
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

public final class CampaignRunner {
    private CampaignRunner() {
    }

    public static CampaignResult runV0(
            Path outputDir,
            int runs,
            int casesPerRun,
            long seed,
            LegislativeOutputProfile importedProfile,
            Path legislativeInput
    ) throws IOException {
        return run(
                "Constitutional Review Campaign v0",
                "constitutional-review-campaign-v0",
                outputDir,
                v0Cases(casesPerRun, importedProfile),
                ScenarioCatalog.defaultScenarios(),
                runs,
                casesPerRun,
                seed,
                importedProfile,
                legislativeInput
        );
    }

    private static CampaignResult run(
            String reportName,
            String fileStem,
            Path outputDir,
            List<CampaignCase> cases,
            List<Scenario> scenarios,
            int runs,
            int casesPerRun,
            long seed,
            LegislativeOutputProfile importedProfile,
            Path legislativeInput
    ) throws IOException {
        Files.createDirectories(outputDir);
        Simulator simulator = new Simulator();
        List<CampaignRow> rows = new ArrayList<>();
        for (int i = 0; i < cases.size(); i++) {
            CampaignCase campaignCase = cases.get(i);
            List<ScenarioReport> reports = simulator.compare(
                    scenarios,
                    campaignCase.worldSpec(),
                    runs,
                    seed + i * 10_003L
            );
            for (ScenarioReport report : reports) {
                rows.add(new CampaignRow(campaignCase, report));
            }
        }

        Path csvPath = outputDir.resolve(fileStem + ".csv");
        Path markdownPath = outputDir.resolve(fileStem + ".md");
        Path manifestPath = outputDir.resolve(fileStem + "-manifest.json");
        CampaignResult result = new CampaignResult(csvPath, markdownPath, manifestPath, rows);
        Files.writeString(csvPath, csv(result));
        Files.writeString(markdownPath, markdown(reportName, result, runs, casesPerRun, seed, cases, scenarios, importedProfile));
        ReportProvenance.write(
                manifestPath,
                reportName,
                runs,
                casesPerRun,
                seed,
                cases.size(),
                scenarios.size(),
                legislativeInput,
                List.of(csvPath, markdownPath)
        );
        return result;
    }

    private static List<CampaignCase> v0Cases(int casesPerRun, LegislativeOutputProfile importedProfile) {
        LegislativeOutputProfile neutral = LegislativeOutputProfile.neutral();
        LegislativeOutputProfile importedBlend = importedProfile == null
                ? neutral
                : neutral.blend(importedProfile, 0.65).withSourceName("neutral/imported blend");
        List<CampaignCase> cases = new ArrayList<>();
        cases.add(new CampaignCase(
                "baseline",
                "Baseline",
                "Moderate polarization, ordinary emergency pressure, and neutral legislative output.",
                1.0,
                WorldSpec.baseline(casesPerRun, neutral)
        ));
        cases.add(new CampaignCase(
                "partisan-appointment-pressure",
                "Partisan Appointment Pressure",
                "High appointment capture and polarized justice pool.",
                1.0,
                new WorldSpec(casesPerRun, 31, 0.78, 0.76, 0.44, 0.18, neutral)
        ));
        cases.add(new CampaignCase(
                "rights-risk-legislation",
                "Rights-Risk Legislation",
                "Legislative output creates concentrated rights burdens and weak mandates.",
                1.0,
                new WorldSpec(casesPerRun, 31, 0.58, 0.48, 0.48, 0.18, new LegislativeOutputProfile(
                        "rights-risk synthetic legislature",
                        0.55,
                        0.42,
                        0.45,
                        0.62,
                        0.38,
                        0.36,
                        0.46,
                        0.52
                ))
        ));
        cases.add(new CampaignCase(
                "shadow-docket-stress",
                "Shadow-Docket Stress",
                "High emergency pressure and executive-defiance disputes.",
                1.0,
                new WorldSpec(casesPerRun, 31, 0.55, 0.50, 0.46, 0.56, new LegislativeOutputProfile(
                        "emergency-pressure synthetic legislature",
                        0.50,
                        0.52,
                        0.32,
                        0.30,
                        0.44,
                        0.58,
                        0.52,
                        0.45
                ))
        ));
        cases.add(new CampaignCase(
                "high-democratic-mandate",
                "High Democratic Mandate",
                "Popular, high-mandate laws create accountability pressure against invalidation.",
                1.0,
                new WorldSpec(casesPerRun, 31, 0.42, 0.36, 0.66, 0.14, new LegislativeOutputProfile(
                        "high-mandate synthetic legislature",
                        0.48,
                        0.68,
                        0.10,
                        0.18,
                        0.18,
                        0.18,
                        0.76,
                        0.16
                ))
        ));
        cases.add(new CampaignCase(
                "constitutional-conflict",
                "Constitutional Conflict",
                "Polarized laws, executive defiance, and public attention raise court-legislature conflict.",
                1.0,
                new WorldSpec(casesPerRun, 31, 0.72, 0.68, 0.58, 0.34, new LegislativeOutputProfile(
                        "conflict synthetic legislature",
                        0.62,
                        0.44,
                        0.42,
                        0.40,
                        0.68,
                        0.54,
                        0.44,
                        0.66
                ))
        ));
        if (importedProfile != null) {
            cases.add(new CampaignCase(
                    "imported-legislative-output",
                    "Imported Legislative Output",
                    "Docket assumptions derived from a legislative simulator campaign CSV.",
                    1.0,
                    new WorldSpec(casesPerRun, 31, 0.58, 0.50, 0.50, 0.24, importedBlend)
            ));
        }
        return cases;
    }

    private static String csv(CampaignResult result) {
        StringBuilder builder = new StringBuilder();
        builder.append(String.join(",",
                "caseKey",
                "caseName",
                "caseDescription",
                "caseWeight",
                "legislativeSource",
                "scenarioKey",
                "scenario",
                "totalCases",
                "directionalScore",
                "stabilityRightsScore",
                "legitimacyControlScore",
                "legalStability",
                "rightsProtection",
                "partisanAlignment",
                "shadowDocketAbuse",
                "legitimacy",
                "reversalRate",
                "constitutionalConflict",
                "democraticResponsiveness",
                "independenceAccountabilityBalance",
                "administrativeCost",
                "invalidationRate",
                "meritsReviewRate",
                "emergencyOrderRate",
                "shadowReliefRate",
                "recusalRate",
                "concurrenceRate",
                "dissentRate",
                "panelRate",
                "enBancRate",
                "crossCheckDisagreementRate",
                "councilWarningRate",
                "overrideRate"
        )).append('\n');
        for (CampaignRow row : result.rows()) {
            ScenarioReport report = row.report();
            CampaignCase campaignCase = row.campaignCase();
            builder.append(Values.csv(campaignCase.key())).append(',')
                    .append(Values.csv(campaignCase.name())).append(',')
                    .append(Values.csv(campaignCase.description())).append(',')
                    .append(format(campaignCase.weight())).append(',')
                    .append(Values.csv(campaignCase.worldSpec().legislativeProfile().sourceName())).append(',')
                    .append(Values.csv(report.scenarioKey())).append(',')
                    .append(Values.csv(report.scenarioName())).append(',')
                    .append(report.totalCases()).append(',')
                    .append(format(report.directionalScore())).append(',')
                    .append(format(report.stabilityRightsScore())).append(',')
                    .append(format(report.legitimacyControlScore())).append(',')
                    .append(format(report.legalStability())).append(',')
                    .append(format(report.rightsProtection())).append(',')
                    .append(format(report.partisanAlignment())).append(',')
                    .append(format(report.shadowDocketAbuse())).append(',')
                    .append(format(report.legitimacy())).append(',')
                    .append(format(report.reversalRate())).append(',')
                    .append(format(report.constitutionalConflict())).append(',')
                    .append(format(report.democraticResponsiveness())).append(',')
                    .append(format(report.independenceAccountabilityBalance())).append(',')
                    .append(format(report.administrativeCost())).append(',')
                    .append(format(report.invalidationRate())).append(',')
                    .append(format(report.meritsReviewRate())).append(',')
                    .append(format(report.emergencyOrderRate())).append(',')
                    .append(format(report.shadowReliefRate())).append(',')
                    .append(format(report.recusalRate())).append(',')
                    .append(format(report.concurrenceRate())).append(',')
                    .append(format(report.dissentRate())).append(',')
                    .append(format(report.panelRate())).append(',')
                    .append(format(report.enBancRate())).append(',')
                    .append(format(report.crossCheckDisagreementRate())).append(',')
                    .append(format(report.councilWarningRate())).append(',')
                    .append(format(report.overrideRate()))
                    .append('\n');
        }
        return builder.toString();
    }

    private static String markdown(
            String reportName,
            CampaignResult result,
            int runs,
            int casesPerRun,
            long seed,
            List<CampaignCase> cases,
            List<Scenario> scenarios,
            LegislativeOutputProfile importedProfile
    ) {
        StringBuilder builder = new StringBuilder();
        builder.append("# ").append(reportName).append("\n\n");
        builder.append("Deterministic batch campaign for comparing supreme-court and constitutional-review designs.\n\n");
        builder.append("## Run Configuration\n\n");
        builder.append("- runs per case: ").append(runs).append('\n');
        builder.append("- cases per run: ").append(casesPerRun).append('\n');
        builder.append("- base seed: ").append(seed).append('\n');
        builder.append("- scenarios per case: ").append(scenarios.size()).append('\n');
        builder.append("- experiment cases: ").append(cases.size()).append("\n\n");
        if (importedProfile == null) {
            builder.append("- legislative input: neutral synthetic profile\n\n");
        } else {
            builder.append("- legislative input: ")
                    .append(LegislativeOutputImporter.describe(importedProfile))
                    .append("\n\n");
        }

        builder.append("## Case Weights\n\n");
        builder.append("| Case | Weight | Legislative source | Description |\n");
        builder.append("| --- | ---: | --- | --- |\n");
        for (CampaignCase campaignCase : cases) {
            builder.append("| ")
                    .append(campaignCase.name())
                    .append(" | ")
                    .append(format(campaignCase.weight()))
                    .append(" | ")
                    .append(campaignCase.worldSpec().legislativeProfile().sourceName())
                    .append(" | ")
                    .append(campaignCase.description())
                    .append(" |\n");
        }

        List<WeightedScenarioReport> weightedReports = weightedReports(result.rows());
        builder.append("\n## Headline Findings\n\n");
        WeightedScenarioReport bestDirectional = weightedReports.stream()
                .max(Comparator.comparingDouble(WeightedScenarioReport::directionalScore))
                .orElseThrow();
        WeightedScenarioReport bestRights = weightedReports.stream()
                .max(Comparator.comparingDouble(WeightedScenarioReport::rightsProtection))
                .orElseThrow();
        WeightedScenarioReport lowestShadow = weightedReports.stream()
                .min(Comparator.comparingDouble(WeightedScenarioReport::shadowDocketAbuse))
                .orElseThrow();
        WeightedScenarioReport lowestPartisan = weightedReports.stream()
                .min(Comparator.comparingDouble(WeightedScenarioReport::partisanAlignment))
                .orElseThrow();
        builder.append("- Highest directional score: ")
                .append(bestDirectional.scenarioName())
                .append(" at ")
                .append(format(bestDirectional.directionalScore()))
                .append(".\n");
        builder.append("- Highest rights protection: ")
                .append(bestRights.scenarioName())
                .append(" at ")
                .append(format(bestRights.rightsProtection()))
                .append(".\n");
        builder.append("- Lowest shadow-docket abuse: ")
                .append(lowestShadow.scenarioName())
                .append(" at ")
                .append(format(lowestShadow.shadowDocketAbuse()))
                .append(".\n");
        builder.append("- Lowest partisan alignment: ")
                .append(lowestPartisan.scenarioName())
                .append(" at ")
                .append(format(lowestPartisan.partisanAlignment()))
                .append(".\n");
        builder.append("- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, and administrative feasibility.\n");

        builder.append("\n## Metric Direction Legend\n\n");
        builder.append("- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.\n");
        builder.append("- Lower `partisanAlignment`, `shadowDocketAbuse`, `reversalRate`, `constitutionalConflict`, and `administrativeCost` are usually better.\n");
        builder.append("- Invalidation, emergency, recusal, concurrence, dissent, panel, en banc, council, cross-check, and override rates are diagnostic.\n");

        builder.append("\n## Scenario Averages Across Cases\n\n");
        builder.append("| Scenario | Directional | Stability/rights | Legitimacy/control | Legal stability | Rights protection | Partisan align. | Shadow abuse | Legitimacy | Reversal | Conflict | Responsiveness | Admin cost | Invalidation | Override |\n");
        builder.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |\n");
        weightedReports.stream()
                .sorted(Comparator.comparingDouble(WeightedScenarioReport::directionalScore).reversed())
                .forEach(report -> builder.append("| ")
                        .append(report.scenarioName())
                        .append(" | ")
                        .append(format(report.directionalScore()))
                        .append(" | ")
                        .append(format(report.stabilityRightsScore()))
                        .append(" | ")
                        .append(format(report.legitimacyControlScore()))
                        .append(" | ")
                        .append(format(report.legalStability()))
                        .append(" | ")
                        .append(format(report.rightsProtection()))
                        .append(" | ")
                        .append(format(report.partisanAlignment()))
                        .append(" | ")
                        .append(format(report.shadowDocketAbuse()))
                        .append(" | ")
                        .append(format(report.legitimacy()))
                        .append(" | ")
                        .append(format(report.reversalRate()))
                        .append(" | ")
                        .append(format(report.constitutionalConflict()))
                        .append(" | ")
                        .append(format(report.democraticResponsiveness()))
                        .append(" | ")
                        .append(format(report.administrativeCost()))
                        .append(" | ")
                        .append(format(report.invalidationRate()))
                        .append(" | ")
                        .append(format(report.overrideRate()))
                        .append(" |\n"));
        return builder.toString();
    }

    private static List<WeightedScenarioReport> weightedReports(List<CampaignRow> rows) {
        Map<String, WeightedTotals> totals = new LinkedHashMap<>();
        for (CampaignRow row : rows) {
            WeightedTotals total = totals.computeIfAbsent(
                    row.report().scenarioKey(),
                    key -> new WeightedTotals(row.report().scenarioName())
            );
            total.add(row.campaignCase().weight(), row.report());
        }
        return totals.entrySet().stream()
                .map(entry -> entry.getValue().toReport(entry.getKey()))
                .toList();
    }

    private static String format(double value) {
        return String.format(Locale.ROOT, "%.3f", value);
    }

    private static final class WeightedTotals {
        private final String scenarioName;
        private double weight;
        private double directionalScore;
        private double stabilityRightsScore;
        private double legitimacyControlScore;
        private double legalStability;
        private double rightsProtection;
        private double partisanAlignment;
        private double shadowDocketAbuse;
        private double legitimacy;
        private double reversalRate;
        private double constitutionalConflict;
        private double democraticResponsiveness;
        private double administrativeCost;
        private double invalidationRate;
        private double overrideRate;

        private WeightedTotals(String scenarioName) {
            this.scenarioName = scenarioName;
        }

        private void add(double rowWeight, ScenarioReport report) {
            weight += rowWeight;
            directionalScore += report.directionalScore() * rowWeight;
            stabilityRightsScore += report.stabilityRightsScore() * rowWeight;
            legitimacyControlScore += report.legitimacyControlScore() * rowWeight;
            legalStability += report.legalStability() * rowWeight;
            rightsProtection += report.rightsProtection() * rowWeight;
            partisanAlignment += report.partisanAlignment() * rowWeight;
            shadowDocketAbuse += report.shadowDocketAbuse() * rowWeight;
            legitimacy += report.legitimacy() * rowWeight;
            reversalRate += report.reversalRate() * rowWeight;
            constitutionalConflict += report.constitutionalConflict() * rowWeight;
            democraticResponsiveness += report.democraticResponsiveness() * rowWeight;
            administrativeCost += report.administrativeCost() * rowWeight;
            invalidationRate += report.invalidationRate() * rowWeight;
            overrideRate += report.overrideRate() * rowWeight;
        }

        private WeightedScenarioReport toReport(String scenarioKey) {
            double denominator = Math.max(1.0, weight);
            return new WeightedScenarioReport(
                    scenarioKey,
                    scenarioName,
                    directionalScore / denominator,
                    stabilityRightsScore / denominator,
                    legitimacyControlScore / denominator,
                    legalStability / denominator,
                    rightsProtection / denominator,
                    partisanAlignment / denominator,
                    shadowDocketAbuse / denominator,
                    legitimacy / denominator,
                    reversalRate / denominator,
                    constitutionalConflict / denominator,
                    democraticResponsiveness / denominator,
                    administrativeCost / denominator,
                    invalidationRate / denominator,
                    overrideRate / denominator
            );
        }
    }

    private record WeightedScenarioReport(
            String scenarioKey,
            String scenarioName,
            double directionalScore,
            double stabilityRightsScore,
            double legitimacyControlScore,
            double legalStability,
            double rightsProtection,
            double partisanAlignment,
            double shadowDocketAbuse,
            double legitimacy,
            double reversalRate,
            double constitutionalConflict,
            double democraticResponsiveness,
            double administrativeCost,
            double invalidationRate,
            double overrideRate
    ) {
    }
}
