package constitutionalreview.experiment;


import constitutionalreview.model.LegislativeOutputProfile;
import constitutionalreview.reporting.ReportProvenance;
import constitutionalreview.simulation.*;
import constitutionalreview.util.Values;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;


public final class PriorUncertaintyRunner
{
	private PriorUncertaintyRunner() {
	}
	
	public static DiagnosticResult run(
			Path outputDir,
			int runs,
			int casesPerRun,
			int priorSamples,
			long seed,
			LegislativeOutputProfile importedProfile,
			Path legislativeInput
	) throws IOException {
		Files.createDirectories(outputDir);
		List<Scenario> scenarios = ScenarioCatalog.defaultScenarios();
		Simulator simulator = new Simulator();
		Map<String, ScenarioPriorStats> stats = new LinkedHashMap<>();
		List<PriorDraw> draws = new ArrayList<>();
		Random priorRandom = new Random(seed ^ 0x6A09E667F3BCC909L);
		LegislativeOutputProfile baseProfile = importedProfile == null ? LegislativeOutputProfile.neutral() : importedProfile.normalized();
		
		for (int sample = 0; sample < priorSamples; sample++) {
			PriorDraw draw = drawPrior(sample + 1, casesPerRun, baseProfile, priorRandom);
			draws.add(draw);
			List<ScenarioReport> reports = simulator.compare(
					scenarios,
					draw.worldSpec(),
					runs,
					seed + sample * 20_011L
			);
			for (ScenarioReport report : reports) {
				stats.computeIfAbsent(report.scenarioKey(), ignored -> new ScenarioPriorStats(report.scenarioName()))
				     .add(report);
			}
		}
		
		List<PriorUncertaintyRow> rows = stats.entrySet().stream()
		                                      .map(entry -> entry.getValue().toRow(entry.getKey()))
		                                      .sorted(Comparator.comparingDouble(PriorUncertaintyRow::directionalP50).reversed())
		                                      .toList();
		rows = classify(rows);
		
		Path csvPath = outputDir.resolve("prior-uncertainty-v1.csv");
		Path markdownPath = outputDir.resolve("prior-uncertainty-v1.md");
		Path manifestPath = outputDir.resolve("prior-uncertainty-v1-manifest.json");
		Files.writeString(csvPath, csv(rows));
		Files.writeString(markdownPath, markdown(rows, draws, runs, casesPerRun, priorSamples, seed, importedProfile));
		ReportProvenance.write(
				manifestPath,
				"Sampled Prior Uncertainty v1",
				runs,
				casesPerRun,
				seed,
				priorSamples,
				scenarios.size(),
				legislativeInput,
				List.of(csvPath, markdownPath)
		);
		return new DiagnosticResult("Sampled Prior Uncertainty v1", csvPath, markdownPath, manifestPath);
	}
	
	private static PriorDraw drawPrior(int index, int casesPerRun, LegislativeOutputProfile baseProfile, Random random) {
		double polarization = triangular(random, 0.28, 0.54, 0.86);
		double appointmentCapture = triangular(random, 0.16, 0.42, 0.88);
		double publicPressure = triangular(random, 0.18, 0.46, 0.82);
		double emergencyShare = triangular(random, 0.03, 0.18, 0.76);
		LegislativeOutputProfile profile = sampledProfile(baseProfile, index, random);
		int justicePool = random.nextDouble() < 0.18 ? 45 : random.nextDouble() < 0.32 ? 37 : 31;
		WorldSpec worldSpec = new WorldSpec(casesPerRun, justicePool, polarization, appointmentCapture, publicPressure, emergencyShare, profile);
		return new PriorDraw(
				"prior-" + index,
				worldSpec,
				polarization,
				appointmentCapture,
				publicPressure,
				emergencyShare
		);
	}
	
	private static LegislativeOutputProfile sampledProfile(LegislativeOutputProfile baseProfile, int index, Random random) {
		LegislativeOutputProfile base = baseProfile.normalized();
		return new LegislativeOutputProfile(
				"sampled prior " + index + " / " + base.sourceName(),
				jitter(base.volatility(), 0.20, random),
				jitter(base.legalQuality(), 0.22, random),
				jitter(base.weakMandateRate(), 0.24, random),
				jitter(base.rightsRisk(), 0.24, random),
				jitter(base.partisanSkew(), 0.24, random),
				jitter(base.volatility(), 0.24, random),
				jitter(base.publicLegitimacy(), 0.22, random),
				jitter(base.overridePressure(), 0.24, random)
		).normalized();
	}
	
	private static double jitter(double center, double span, Random random) {
		return Values.clamp01(center + (random.nextDouble() - random.nextDouble()) * span);
	}
	
	private static double triangular(Random random, double low, double mode, double high) {
		double u = random.nextDouble();
		double c = (mode - low) / (high - low);
		if (u < c) {
			return low + Math.sqrt(u * (high - low) * (mode - low));
		}
		return high - Math.sqrt((1.0 - u) * (high - low) * (high - mode));
	}
	
	private static List<PriorUncertaintyRow> classify(List<PriorUncertaintyRow> rows) {
		if (rows.isEmpty()) {
			return rows;
		}
		PriorUncertaintyRow best = rows.get(0);
		List<PriorUncertaintyRow> classified = new ArrayList<>();
		for (PriorUncertaintyRow row : rows) {
			String interpretation;
			if (best.directionalP50() - row.directionalP50() <= 0.015) {
				interpretation = "front-line cluster";
			} else if (row.directionalP95() >= best.directionalP05()) {
				interpretation = "overlapping uncertainty band";
			} else {
				interpretation = "separated in sampled priors";
			}
			classified.add(row.withInterpretation(interpretation));
		}
		return classified;
	}
	
	private static String csv(List<PriorUncertaintyRow> rows) {
		StringBuilder builder = new StringBuilder();
		builder.append(String.join(",",
		                           "scenarioKey",
		                           "scenario",
		                           "priorSamples",
		                           "directionalP05",
		                           "directionalP50",
		                           "directionalP95",
		                           "rightsProtectionP05",
		                           "rightsProtectionP50",
		                           "rightsProtectionP95",
		                           "shadowDocketAbuseP05",
		                           "shadowDocketAbuseP50",
		                           "shadowDocketAbuseP95",
		                           "emergencyDownstreamP05",
		                           "emergencyDownstreamP50",
		                           "emergencyDownstreamP95",
		                           "lowerCourtComplianceP05",
		                           "lowerCourtComplianceP50",
		                           "lowerCourtComplianceP95",
		                           "governmentNoncomplianceP05",
		                           "governmentNoncomplianceP50",
		                           "governmentNoncomplianceP95",
		                           "constitutionalConflictP05",
		                           "constitutionalConflictP50",
		                           "constitutionalConflictP95",
		                           "interpretation"
		)).append('\n');
		for (PriorUncertaintyRow row : rows) {
			builder.append(Values.csv(row.scenarioKey())).append(',')
			       .append(Values.csv(row.scenarioName())).append(',')
			       .append(row.priorSamples()).append(',')
			       .append(format(row.directionalP05())).append(',')
			       .append(format(row.directionalP50())).append(',')
			       .append(format(row.directionalP95())).append(',')
			       .append(format(row.rightsProtectionP05())).append(',')
			       .append(format(row.rightsProtectionP50())).append(',')
			       .append(format(row.rightsProtectionP95())).append(',')
			       .append(format(row.shadowDocketAbuseP05())).append(',')
			       .append(format(row.shadowDocketAbuseP50())).append(',')
			       .append(format(row.shadowDocketAbuseP95())).append(',')
			       .append(format(row.emergencyDownstreamP05())).append(',')
			       .append(format(row.emergencyDownstreamP50())).append(',')
			       .append(format(row.emergencyDownstreamP95())).append(',')
			       .append(format(row.lowerCourtComplianceP05())).append(',')
			       .append(format(row.lowerCourtComplianceP50())).append(',')
			       .append(format(row.lowerCourtComplianceP95())).append(',')
			       .append(format(row.governmentNoncomplianceP05())).append(',')
			       .append(format(row.governmentNoncomplianceP50())).append(',')
			       .append(format(row.governmentNoncomplianceP95())).append(',')
			       .append(format(row.constitutionalConflictP05())).append(',')
			       .append(format(row.constitutionalConflictP50())).append(',')
			       .append(format(row.constitutionalConflictP95())).append(',')
			       .append(Values.csv(row.interpretation()))
			       .append('\n');
		}
		return builder.toString();
	}
	
	private static String markdown(
			List<PriorUncertaintyRow> rows,
			List<PriorDraw> draws,
			int runs,
			int casesPerRun,
			int priorSamples,
			long seed,
			LegislativeOutputProfile importedProfile
	) {
		StringBuilder builder = new StringBuilder();
		builder.append("# Sampled Prior Uncertainty v1\n\n");
		builder.append("This diagnostic replaces a purely named-scenario sensitivity story with sampled prior distributions over polarization, appointment capture, public pressure, emergency share, justice-pool size, and legislative-output profile components. It is still synthetic uncertainty, not empirical validation.\n\n");
		builder.append("## Run Configuration\n\n");
		builder.append("- runs per prior draw: ").append(runs).append('\n');
		builder.append("- cases per run: ").append(casesPerRun).append('\n');
		builder.append("- prior draws: ").append(priorSamples).append('\n');
		builder.append("- base seed: ").append(seed).append('\n');
		builder.append("- legislative input: ")
		       .append(importedProfile == null ? "neutral synthetic profile" : importedProfile.sourceName())
		       .append("\n\n");
		builder.append("## Prior Draw Ranges\n\n");
		builder.append("| Field | Min | Median | Max |\n");
		builder.append("| --- | ---: | ---: | ---: |\n");
		appendDrawRange(builder, "polarization", draws.stream().map(PriorDraw::polarization).toList());
		appendDrawRange(builder, "appointment capture", draws.stream().map(PriorDraw::appointmentCapture).toList());
		appendDrawRange(builder, "public pressure", draws.stream().map(PriorDraw::publicPressure).toList());
		appendDrawRange(builder, "emergency share", draws.stream().map(PriorDraw::emergencyShare).toList());
		builder.append("\n## Scenario Uncertainty Bands\n\n");
		builder.append("| Scenario | Score 5/50/95 | Rights 5/50/95 | Shadow 5/50/95 | Emerg. downstream 5/50/95 | Lower-court compliance 5/50/95 | Gov. noncomp. 5/50/95 | Conflict 5/50/95 | Interpretation |\n");
		builder.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |\n");
		for (PriorUncertaintyRow row : rows) {
			builder.append("| ")
			       .append(row.scenarioName())
			       .append(" | ")
			       .append(band(row.directionalP05(), row.directionalP50(), row.directionalP95()))
			       .append(" | ")
			       .append(band(row.rightsProtectionP05(), row.rightsProtectionP50(), row.rightsProtectionP95()))
			       .append(" | ")
			       .append(band(row.shadowDocketAbuseP05(), row.shadowDocketAbuseP50(), row.shadowDocketAbuseP95()))
			       .append(" | ")
			       .append(band(row.emergencyDownstreamP05(), row.emergencyDownstreamP50(), row.emergencyDownstreamP95()))
			       .append(" | ")
			       .append(band(row.lowerCourtComplianceP05(), row.lowerCourtComplianceP50(), row.lowerCourtComplianceP95()))
			       .append(" | ")
			       .append(band(row.governmentNoncomplianceP05(), row.governmentNoncomplianceP50(), row.governmentNoncomplianceP95()))
			       .append(" | ")
			       .append(band(row.constitutionalConflictP05(), row.constitutionalConflictP50(), row.constitutionalConflictP95()))
			       .append(" | ")
			       .append(row.interpretation())
			       .append(" |\n");
		}
		return builder.toString();
	}
	
	private static void appendDrawRange(StringBuilder builder, String label, List<Double> values) {
		List<Double> sorted = values.stream().sorted().toList();
		builder.append("| ")
		       .append(label)
		       .append(" | ")
		       .append(format(sorted.get(0)))
		       .append(" | ")
		       .append(format(percentile(sorted, 0.50)))
		       .append(" | ")
		       .append(format(sorted.get(sorted.size() - 1)))
		       .append(" |\n");
	}
	
	private static String band(double p05, double p50, double p95) {
		return format(p05) + "/" + format(p50) + "/" + format(p95);
	}
	
	private static double percentile(List<Double> sorted, double percentile) {
		if (sorted.isEmpty()) {
			return 0.0;
		}
		double position = percentile * (sorted.size() - 1);
		int lower = (int) Math.floor(position);
		int upper = (int) Math.ceil(position);
		if (lower == upper) {
			return sorted.get(lower);
		}
		double fraction = position - lower;
		return sorted.get(lower) * (1.0 - fraction) + sorted.get(upper) * fraction;
	}
	
	private static String format(double value) {
		return String.format(Locale.ROOT, "%.3f", value);
	}
	
	private record PriorDraw(
			String key,
			WorldSpec worldSpec,
			double polarization,
			double appointmentCapture,
			double publicPressure,
			double emergencyShare
	)
	{
	}
	
	
	private static final class ScenarioPriorStats
	{
		private final String scenarioName;
		private final List<Double> directional = new ArrayList<>();
		private final List<Double> rightsProtection = new ArrayList<>();
		private final List<Double> shadowDocketAbuse = new ArrayList<>();
		private final List<Double> emergencyDownstream = new ArrayList<>();
		private final List<Double> lowerCourtCompliance = new ArrayList<>();
		private final List<Double> governmentNoncompliance = new ArrayList<>();
		private final List<Double> constitutionalConflict = new ArrayList<>();
		
		private ScenarioPriorStats(String scenarioName) {
			this.scenarioName = scenarioName;
		}
		
		private static List<Double> sorted(List<Double> values) {
			return values.stream().sorted().toList();
		}
		
		private void add(ScenarioReport report) {
			directional.add(report.directionalScore());
			rightsProtection.add(report.rightsProtection());
			shadowDocketAbuse.add(report.shadowDocketAbuse());
			emergencyDownstream.add(report.emergencyDownstreamEffect());
			lowerCourtCompliance.add(report.lowerCourtCompliance());
			governmentNoncompliance.add(report.governmentNoncomplianceRate());
			constitutionalConflict.add(report.constitutionalConflict());
		}
		
		private PriorUncertaintyRow toRow(String scenarioKey) {
			return new PriorUncertaintyRow(
					scenarioKey,
					scenarioName,
					directional.size(),
					percentile(sorted(directional), 0.05),
					percentile(sorted(directional), 0.50),
					percentile(sorted(directional), 0.95),
					percentile(sorted(rightsProtection), 0.05),
					percentile(sorted(rightsProtection), 0.50),
					percentile(sorted(rightsProtection), 0.95),
					percentile(sorted(shadowDocketAbuse), 0.05),
					percentile(sorted(shadowDocketAbuse), 0.50),
					percentile(sorted(shadowDocketAbuse), 0.95),
					percentile(sorted(emergencyDownstream), 0.05),
					percentile(sorted(emergencyDownstream), 0.50),
					percentile(sorted(emergencyDownstream), 0.95),
					percentile(sorted(lowerCourtCompliance), 0.05),
					percentile(sorted(lowerCourtCompliance), 0.50),
					percentile(sorted(lowerCourtCompliance), 0.95),
					percentile(sorted(governmentNoncompliance), 0.05),
					percentile(sorted(governmentNoncompliance), 0.50),
					percentile(sorted(governmentNoncompliance), 0.95),
					percentile(sorted(constitutionalConflict), 0.05),
					percentile(sorted(constitutionalConflict), 0.50),
					percentile(sorted(constitutionalConflict), 0.95),
					"unclassified"
			);
		}
	}
	
	
	private record PriorUncertaintyRow(
			String scenarioKey,
			String scenarioName,
			int priorSamples,
			double directionalP05,
			double directionalP50,
			double directionalP95,
			double rightsProtectionP05,
			double rightsProtectionP50,
			double rightsProtectionP95,
			double shadowDocketAbuseP05,
			double shadowDocketAbuseP50,
			double shadowDocketAbuseP95,
			double emergencyDownstreamP05,
			double emergencyDownstreamP50,
			double emergencyDownstreamP95,
			double lowerCourtComplianceP05,
			double lowerCourtComplianceP50,
			double lowerCourtComplianceP95,
			double governmentNoncomplianceP05,
			double governmentNoncomplianceP50,
			double governmentNoncomplianceP95,
			double constitutionalConflictP05,
			double constitutionalConflictP50,
			double constitutionalConflictP95,
			String interpretation
	)
	{
		private PriorUncertaintyRow withInterpretation(String value) {
			return new PriorUncertaintyRow(
					scenarioKey,
					scenarioName,
					priorSamples,
					directionalP05,
					directionalP50,
					directionalP95,
					rightsProtectionP05,
					rightsProtectionP50,
					rightsProtectionP95,
					shadowDocketAbuseP05,
					shadowDocketAbuseP50,
					shadowDocketAbuseP95,
					emergencyDownstreamP05,
					emergencyDownstreamP50,
					emergencyDownstreamP95,
					lowerCourtComplianceP05,
					lowerCourtComplianceP50,
					lowerCourtComplianceP95,
					governmentNoncomplianceP05,
					governmentNoncomplianceP50,
					governmentNoncomplianceP95,
					constitutionalConflictP05,
					constitutionalConflictP50,
					constitutionalConflictP95,
					value
			);
		}
	}
}
