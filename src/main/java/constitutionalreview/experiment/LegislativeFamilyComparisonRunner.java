package constitutionalreview.experiment;


import constitutionalreview.importer.LegislativeOutputImporter;
import constitutionalreview.model.LegislativeOutputProfile;
import constitutionalreview.reporting.ReportProvenance;
import constitutionalreview.simulation.*;
import constitutionalreview.util.Values;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Locale;


public final class LegislativeFamilyComparisonRunner
{
	private LegislativeFamilyComparisonRunner() {
	}
	
	public static DiagnosticResult run(
			Path outputDir,
			Path familyDir,
			int runs,
			int casesPerRun,
			long seed
	) throws IOException {
		Files.createDirectories(outputDir);
		List<Path> inputs = inputs(familyDir);
		List<Scenario> scenarios = ScenarioCatalog.defaultScenarios();
		Simulator simulator = new Simulator();
		List<FamilyScenarioRow> rows = new ArrayList<>();
		List<FamilySummary> summaries = new ArrayList<>();
		
		for (int i = 0; i < inputs.size(); i++) {
			Path input = inputs.get(i);
			LegislativeOutputProfile profile = LegislativeOutputImporter.importCsv(input);
			List<ScenarioReport> reports = simulator.compare(
					scenarios,
					WorldSpec.baseline(casesPerRun, profile),
					runs,
					seed + i * 10_003L
			);
			ScenarioReport best = reports.stream()
			                             .max(Comparator.comparingDouble(ScenarioReport::directionalScore))
			                             .orElseThrow();
			summaries.add(new FamilySummary(input.getFileName().toString(), profile, best));
			for (ScenarioReport report : reports) {
				rows.add(new FamilyScenarioRow(input.getFileName().toString(), profile, report));
			}
		}
		
		Path csvPath = outputDir.resolve("legislative-family-comparison-v3.csv");
		Path markdownPath = outputDir.resolve("legislative-family-comparison-v3.md");
		Path manifestPath = outputDir.resolve("legislative-family-comparison-v3-manifest.json");
		Files.writeString(csvPath, csv(rows));
		Files.writeString(markdownPath, markdown(summaries, rows, familyDir, runs, casesPerRun, seed));
		ReportProvenance.write(
				manifestPath,
				"Legislative Family Import Comparison v3",
				runs,
				casesPerRun,
				seed,
				inputs.size(),
				scenarios.size(),
				familyDir,
				List.of(csvPath, markdownPath)
		);
		return new DiagnosticResult("Legislative Family Import Comparison v3", csvPath, markdownPath, manifestPath);
	}
	
	private static List<Path> inputs(Path familyDir) throws IOException {
		if (familyDir == null || !Files.isDirectory(familyDir)) {
			throw new IllegalArgumentException("--legislative-family-dir must point to a directory of legislative campaign CSV reports");
		}
		List<String> preferred = List.of(
				"simulation-campaign-v0.csv",
				"simulation-campaign-v5.csv",
				"simulation-campaign-v10.csv",
				"simulation-campaign-v15.csv",
				"simulation-campaign-v20.csv",
				"simulation-campaign-v21-paper.csv",
				"simulation-manipulation-stress.csv"
		);
		List<Path> inputs = new ArrayList<>();
		for (String name : preferred) {
			Path candidate = familyDir.resolve(name);
			if (Files.isRegularFile(candidate)) {
				inputs.add(candidate);
			}
		}
		if (!inputs.isEmpty()) {
			return inputs;
		}
		try (var stream = Files.list(familyDir)) {
			return stream
					.filter(path -> path.getFileName().toString().endsWith(".csv"))
					.filter(path -> path.getFileName().toString().startsWith("simulation-"))
					.sorted()
					.limit(8)
					.toList();
		}
	}
	
	private static String csv(List<FamilyScenarioRow> rows) {
		StringBuilder builder = new StringBuilder();
		builder.append(String.join(",",
		                           "family",
		                           "scenarioKey",
		                           "scenario",
		                           "enactedVolume",
		                           "legalQuality",
		                           "weakMandateRate",
		                           "rightsRisk",
		                           "partisanSkew",
		                           "volatility",
		                           "publicLegitimacy",
		                           "overridePressure",
		                           "directionalScore",
		                           "legalStability",
		                           "rightsProtection",
		                           "partisanAlignment",
		                           "shadowDocketAbuse",
		                           "constitutionalConflict",
		                           "democraticResponsiveness",
		                           "strategicPressure",
		                           "overrideAttemptRate"
		)).append('\n');
		for (FamilyScenarioRow row : rows) {
			LegislativeOutputProfile profile = row.profile();
			ScenarioReport report = row.report();
			builder.append(Values.csv(row.family())).append(',')
			       .append(Values.csv(report.scenarioKey())).append(',')
			       .append(Values.csv(report.scenarioName())).append(',')
			       .append(format(profile.enactedVolume())).append(',')
			       .append(format(profile.legalQuality())).append(',')
			       .append(format(profile.weakMandateRate())).append(',')
			       .append(format(profile.rightsRisk())).append(',')
			       .append(format(profile.partisanSkew())).append(',')
			       .append(format(profile.volatility())).append(',')
			       .append(format(profile.publicLegitimacy())).append(',')
			       .append(format(profile.overridePressure())).append(',')
			       .append(format(report.directionalScore())).append(',')
			       .append(format(report.legalStability())).append(',')
			       .append(format(report.rightsProtection())).append(',')
			       .append(format(report.partisanAlignment())).append(',')
			       .append(format(report.shadowDocketAbuse())).append(',')
			       .append(format(report.constitutionalConflict())).append(',')
			       .append(format(report.democraticResponsiveness())).append(',')
			       .append(format(report.strategicPressure())).append(',')
			       .append(format(report.overrideAttemptRate()))
			       .append('\n');
		}
		return builder.toString();
	}
	
	private static String markdown(
			List<FamilySummary> summaries,
			List<FamilyScenarioRow> rows,
			Path familyDir,
			int runs,
			int casesPerRun,
			long seed
	) {
		StringBuilder builder = new StringBuilder();
		builder.append("# Legislative Family Import Comparison v3\n\n");
		builder.append("Compares the constitutional-review import contract across multiple congressional-simulator report families.\n\n");
		builder.append("## Run Configuration\n\n");
		builder.append("- legislative family directory: ").append(familyDir).append('\n');
		builder.append("- imported families: ").append(summaries.size()).append('\n');
		builder.append("- runs per family: ").append(runs).append('\n');
		builder.append("- cases per run: ").append(casesPerRun).append('\n');
		builder.append("- base seed: ").append(seed).append("\n\n");
		builder.append("## Imported Profiles\n\n");
		builder.append("| Family | Volume | Quality | Weak mandate | Rights risk | Partisan skew | Volatility | Legitimacy | Override pressure | Best scenario |\n");
		builder.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |\n");
		for (FamilySummary summary : summaries) {
			LegislativeOutputProfile profile = summary.profile();
			ScenarioReport best = summary.bestReport();
			builder.append("| ")
			       .append(summary.family())
			       .append(" | ")
			       .append(format(profile.enactedVolume()))
			       .append(" | ")
			       .append(format(profile.legalQuality()))
			       .append(" | ")
			       .append(format(profile.weakMandateRate()))
			       .append(" | ")
			       .append(format(profile.rightsRisk()))
			       .append(" | ")
			       .append(format(profile.partisanSkew()))
			       .append(" | ")
			       .append(format(profile.volatility()))
			       .append(" | ")
			       .append(format(profile.publicLegitimacy()))
			       .append(" | ")
			       .append(format(profile.overridePressure()))
			       .append(" | ")
			       .append(best.scenarioName())
			       .append(" (")
			       .append(format(best.directionalScore()))
			       .append(") |\n");
		}
		builder.append("\n## Scenario Sensitivity By Family\n\n");
		builder.append("| Family | Scenario | Directional | Legal | Rights | Shadow | Conflict | Strategic | Override att. |\n");
		builder.append("| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |\n");
		rows.stream()
		    .sorted(Comparator
				            .comparing(FamilyScenarioRow::family)
				            .thenComparing((FamilyScenarioRow row) -> -row.report().directionalScore()))
		    .forEach(row -> {
			    ScenarioReport report = row.report();
			    builder.append("| ")
			           .append(row.family())
			           .append(" | ")
			           .append(report.scenarioName())
			           .append(" | ")
			           .append(format(report.directionalScore()))
			           .append(" | ")
			           .append(format(report.legalStability()))
			           .append(" | ")
			           .append(format(report.rightsProtection()))
			           .append(" | ")
			           .append(format(report.shadowDocketAbuse()))
			           .append(" | ")
			           .append(format(report.constitutionalConflict()))
			           .append(" | ")
			           .append(format(report.strategicPressure()))
			           .append(" | ")
			           .append(format(report.overrideAttemptRate()))
			           .append(" |\n");
		    });
		return builder.toString();
	}
	
	private static String format(double value) {
		return String.format(Locale.ROOT, "%.3f", value);
	}
	
	private record FamilySummary(String family, LegislativeOutputProfile profile, ScenarioReport bestReport)
	{
	}
	
	
	private record FamilyScenarioRow(String family, LegislativeOutputProfile profile, ScenarioReport report)
	{
	}
}
