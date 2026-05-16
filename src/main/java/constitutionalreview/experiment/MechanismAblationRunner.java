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
import java.util.*;


public final class MechanismAblationRunner
{
	private MechanismAblationRunner() {
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
		List<AblationPair> pairs = pairs();
		List<CampaignCase> cases = selectedCases(casesPerRun, importedProfile);
		Map<String, Scenario> scenarios = scenarioMap();
		Simulator simulator = new Simulator();
		List<AblationRow> rows = new ArrayList<>();
		
		int stream = 0;
		for (AblationPair pair : pairs) {
			Scenario base = scenarios.get(pair.baseScenarioKey());
			Scenario variant = scenarios.get(pair.variantScenarioKey());
			for (CampaignCase campaignCase : cases) {
				List<ScenarioReport> reports = simulator.compare(
						List.of(base, variant),
						campaignCase.worldSpec(),
						runs,
						seed + stream * 10_003L
				);
				ScenarioReport baseReport = reports.get(0);
				ScenarioReport variantReport = reports.get(1);
				rows.add(AblationRow.from(pair, campaignCase, baseReport, variantReport));
				stream++;
			}
		}
		
		Path csvPath = outputDir.resolve("mechanism-ablation-v2.csv");
		Path markdownPath = outputDir.resolve("mechanism-ablation-v2.md");
		Path manifestPath = outputDir.resolve("mechanism-ablation-v2-manifest.json");
		Files.writeString(csvPath, csv(rows));
		Files.writeString(markdownPath, markdown(rows, pairs, cases, runs, casesPerRun, seed, importedProfile));
		ReportProvenance.write(
				manifestPath,
				"Mechanism Ablation v2",
				runs,
				casesPerRun,
				seed,
				cases.size(),
				pairs.size() * 2,
				legislativeInput,
				List.of(csvPath, markdownPath)
		);
		return new DiagnosticResult("Mechanism Ablation v2", csvPath, markdownPath, manifestPath);
	}
	
	private static List<AblationPair> pairs() {
		return List.of(
				new AblationPair("appointment-screening", "Appointment screening", "current-us-like", "nonpartisan-commission"),
				new AblationPair("judicial-electorate-selection", "Judicial electorate selection", "nonpartisan-commission", "judicial-electorate-selection"),
				new AblationPair("term-regularization", "Term regularization", "current-us-like", "term-limited-balanced"),
				new AblationPair("emergency-restraint", "Emergency restraint", "current-us-like", "emergency-restraint-court"),
				new AblationPair("written-emergency-reasoning", "Mandatory written emergency reasoning", "current-us-like", "mandatory-written-emergency-reasoning"),
				new AblationPair("automatic-merits-follow-up", "Automatic merits follow-up", "current-us-like", "automatic-merits-follow-up"),
				new AblationPair("invalidation-threshold", "Invalidation threshold", "current-us-like", "supermajority-review"),
				new AblationPair("recusal-emergency-process", "Recusal and emergency process", "current-us-like", "recusal-and-emergency-reform"),
				new AblationPair("strong-recusal-enforcement", "Strong recusal enforcement", "current-us-like", "strong-recusal-enforcement"),
				new AblationPair("panel-routing", "Panel routing", "term-limited-balanced", "panel-en-banc"),
				new AblationPair("randomized-merits-panels", "Randomized merits panels", "term-limited-balanced", "randomized-merits-panels"),
				new AblationPair("cross-checking-court", "Cross-checking court", "nonpartisan-commission", "cross-checking-courts"),
				new AblationPair("dual-court-filter", "Dual-court filter", "nonpartisan-commission", "dual-supreme-courts"),
				new AblationPair("constitutional-council", "Constitutional council", "nonpartisan-commission", "constitutional-council"),
				new AblationPair("constitutional-remand", "Constitutional remand", "nonpartisan-commission", "constitutional-remand"),
				new AblationPair("public-interest-filter", "Public-interest litigation filter", "nonpartisan-commission", "public-interest-litigation-filter"),
				new AblationPair("legislative-override", "Legislative override", "term-limited-balanced", "legislative-override"),
				new AblationPair("override-window", "Legislative override window", "term-limited-balanced", "legislative-override-window"),
				new AblationPair("jurisdiction-stripping-constraints", "Jurisdiction-stripping constraints", "term-limited-balanced", "jurisdiction-stripping-constraints"),
				new AblationPair("emergency-integrity-bundle", "Emergency integrity bundle", "current-us-like", "emergency-integrity-package"),
				new AblationPair("remand-override-window-bundle", "Remand and override-window bundle", "term-limited-balanced", "remand-override-window-package"),
				new AblationPair("panel-jurisdiction-safeguards", "Panel and jurisdiction safeguards", "term-limited-balanced", "panel-jurisdiction-safeguards"),
				new AblationPair("council-concrete-hybrid", "Council with concrete-review backstop", "nonpartisan-commission", "council-concrete-hybrid"),
				new AblationPair("accountability-election", "Accountability election", "nonpartisan-commission", "accountability-retention-court"),
				new AblationPair("court-expansion", "Court expansion", "term-limited-balanced", "expanded-court-fifteen")
		);
	}
	
	private static List<CampaignCase> selectedCases(int casesPerRun, LegislativeOutputProfile importedProfile) {
		Set<String> keys = Set.of(
				"baseline",
				"extreme-appointment-capture",
				"extreme-emergency-pressure",
				"extreme-rights-risk",
				"weak-mandate-legislation",
				"appointment-timing-manipulation",
				"emergency-application-flood",
				"override-evasion-loop"
		);
		return CampaignRunner.v2Cases(casesPerRun, importedProfile).stream()
		                     .filter(campaignCase -> keys.contains(campaignCase.key()))
		                     .toList();
	}
	
	private static Map<String, Scenario> scenarioMap() {
		Map<String, Scenario> map = new LinkedHashMap<>();
		for (String key : ScenarioCatalog.scenarioKeys()) {
			map.put(key, ScenarioCatalog.scenariosForKeys(List.of(key)).get(0));
		}
		return map;
	}
	
	private static String csv(List<AblationRow> rows) {
		StringBuilder builder = new StringBuilder();
		builder.append(String.join(",",
		                           "mechanismKey",
		                           "mechanism",
		                           "baseScenarioKey",
		                           "variantScenarioKey",
		                           "caseKey",
		                           "caseName",
		                           "caseWeight",
		                           "deltaDirectional",
		                           "deltaLegalStability",
		                           "deltaPrecedentStability",
		                           "deltaStatutoryStability",
		                           "deltaInterbranchCompliance",
		                           "deltaRightsProtection",
		                           "deltaPartisanAlignment",
		                           "deltaShadowDocketAbuse",
		                           "deltaLegitimacy",
		                           "deltaReversalRate",
		                           "deltaConstitutionalConflict",
		                           "deltaDemocraticResponsiveness",
		                           "deltaAdministrativeCost",
		                           "deltaLowerCourtCompliance",
		                           "deltaLowerCourtResistanceRisk",
		                           "deltaEnforcementCapacity",
		                           "deltaGovernmentNoncomplianceRate",
		                           "deltaEmergencyOpportunism",
		                           "deltaEmergencyDownstreamEffect",
		                           "deltaPrecedentDurability",
		                           "deltaJusticeReplacementRate",
		                           "deltaOverrideAttemptRate",
		                           "deltaOverrideRate"
		)).append('\n');
		for (AblationRow row : rows) {
			builder.append(Values.csv(row.mechanismKey())).append(',')
			       .append(Values.csv(row.mechanismName())).append(',')
			       .append(Values.csv(row.baseScenarioKey())).append(',')
			       .append(Values.csv(row.variantScenarioKey())).append(',')
			       .append(Values.csv(row.caseKey())).append(',')
			       .append(Values.csv(row.caseName())).append(',')
			       .append(format(row.caseWeight())).append(',')
			       .append(format(row.deltaDirectional())).append(',')
			       .append(format(row.deltaLegalStability())).append(',')
			       .append(format(row.deltaPrecedentStability())).append(',')
			       .append(format(row.deltaStatutoryStability())).append(',')
			       .append(format(row.deltaInterbranchCompliance())).append(',')
			       .append(format(row.deltaRightsProtection())).append(',')
			       .append(format(row.deltaPartisanAlignment())).append(',')
			       .append(format(row.deltaShadowDocketAbuse())).append(',')
			       .append(format(row.deltaLegitimacy())).append(',')
			       .append(format(row.deltaReversalRate())).append(',')
			       .append(format(row.deltaConstitutionalConflict())).append(',')
			       .append(format(row.deltaDemocraticResponsiveness())).append(',')
			       .append(format(row.deltaAdministrativeCost())).append(',')
			       .append(format(row.deltaLowerCourtCompliance())).append(',')
			       .append(format(row.deltaLowerCourtResistanceRisk())).append(',')
			       .append(format(row.deltaEnforcementCapacity())).append(',')
			       .append(format(row.deltaGovernmentNoncomplianceRate())).append(',')
			       .append(format(row.deltaEmergencyOpportunism())).append(',')
			       .append(format(row.deltaEmergencyDownstreamEffect())).append(',')
			       .append(format(row.deltaPrecedentDurability())).append(',')
			       .append(format(row.deltaJusticeReplacementRate())).append(',')
			       .append(format(row.deltaOverrideAttemptRate())).append(',')
			       .append(format(row.deltaOverrideRate()))
			       .append('\n');
		}
		return builder.toString();
	}
	
	private static String markdown(
			List<AblationRow> rows,
			List<AblationPair> pairs,
			List<CampaignCase> cases,
			int runs,
			int casesPerRun,
			long seed,
			LegislativeOutputProfile importedProfile
	) {
		List<AblationSummary> summaries = summaries(rows);
		StringBuilder builder = new StringBuilder();
		builder.append("# Mechanism Ablation v2\n\n");
		builder.append("Pairwise comparisons that change one institutional mechanism at a time where the catalog permits a close proxy.\n\n");
		builder.append("## Run Configuration\n\n");
		builder.append("- runs per pair/case: ").append(runs).append('\n');
		builder.append("- cases per run: ").append(casesPerRun).append('\n');
		builder.append("- base seed: ").append(seed).append('\n');
		builder.append("- mechanisms: ").append(pairs.size()).append('\n');
		builder.append("- stress cases: ").append(cases.size()).append('\n');
		builder.append("- legislative input: ")
		       .append(importedProfile == null ? "neutral synthetic profile" : importedProfile.sourceName())
		       .append("\n\n");
		builder.append("Positive deltas improve higher-better metrics. Negative deltas improve lower-better diagnostics such as partisan alignment, shadow abuse, conflict, and administrative cost.\n\n");
		builder.append("## Weighted Mechanism Summary\n\n");
		builder.append("| Mechanism | Base -> Variant | Directional | Legal | Rights | Shadow | Conflict | Lower-court compliance | LC resistance | Enforcement | Gov. noncomp. | Emerg. opp. | Emerg. downstream | Precedent durability | Admin cost |\n");
		builder.append("| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |\n");
		for (AblationSummary summary : summaries) {
			builder.append("| ")
			       .append(summary.mechanismName())
			       .append(" | `")
			       .append(summary.baseScenarioKey())
			       .append("` -> `")
			       .append(summary.variantScenarioKey())
			       .append("` | ")
			       .append(format(summary.deltaDirectional()))
			       .append(" | ")
			       .append(format(summary.deltaLegalStability()))
			       .append(" | ")
			       .append(format(summary.deltaRightsProtection()))
			       .append(" | ")
			       .append(format(summary.deltaShadowDocketAbuse()))
			       .append(" | ")
			       .append(format(summary.deltaConstitutionalConflict()))
			       .append(" | ")
			       .append(format(summary.deltaLowerCourtCompliance()))
			       .append(" | ")
			       .append(format(summary.deltaLowerCourtResistanceRisk()))
			       .append(" | ")
			       .append(format(summary.deltaEnforcementCapacity()))
			       .append(" | ")
			       .append(format(summary.deltaGovernmentNoncomplianceRate()))
			       .append(" | ")
			       .append(format(summary.deltaEmergencyOpportunism()))
			       .append(" | ")
			       .append(format(summary.deltaEmergencyDownstreamEffect()))
			       .append(" | ")
			       .append(format(summary.deltaPrecedentDurability()))
			       .append(" | ")
			       .append(format(summary.deltaAdministrativeCost()))
			       .append(" |\n");
		}
		return builder.toString();
	}
	
	private static List<AblationSummary> summaries(List<AblationRow> rows) {
		Map<String, SummaryTotals> totals = new LinkedHashMap<>();
		for (AblationRow row : rows) {
			totals.computeIfAbsent(row.mechanismKey(), ignored -> new SummaryTotals(row))
			      .add(row);
		}
		return totals.values().stream()
		             .map(SummaryTotals::toSummary)
		             .sorted(Comparator.comparingDouble(AblationSummary::deltaDirectional).reversed())
		             .toList();
	}
	
	private static String format(double value) {
		return String.format(Locale.ROOT, "%.3f", value);
	}
	
	private record AblationPair(String key, String name, String baseScenarioKey, String variantScenarioKey)
	{
	}
	
	
	private record AblationRow(
			String mechanismKey,
			String mechanismName,
			String baseScenarioKey,
			String variantScenarioKey,
			String caseKey,
			String caseName,
			double caseWeight,
			double deltaDirectional,
			double deltaLegalStability,
			double deltaPrecedentStability,
			double deltaStatutoryStability,
			double deltaInterbranchCompliance,
			double deltaRightsProtection,
			double deltaPartisanAlignment,
			double deltaShadowDocketAbuse,
			double deltaLegitimacy,
			double deltaReversalRate,
			double deltaConstitutionalConflict,
			double deltaDemocraticResponsiveness,
			double deltaAdministrativeCost,
			double deltaLowerCourtCompliance,
			double deltaLowerCourtResistanceRisk,
			double deltaEnforcementCapacity,
			double deltaGovernmentNoncomplianceRate,
			double deltaEmergencyOpportunism,
			double deltaEmergencyDownstreamEffect,
			double deltaPrecedentDurability,
			double deltaJusticeReplacementRate,
			double deltaOverrideAttemptRate,
			double deltaOverrideRate
	)
	{
		private static AblationRow from(
				AblationPair pair,
				CampaignCase campaignCase,
				ScenarioReport base,
				ScenarioReport variant
		) {
			return new AblationRow(
					pair.key(),
					pair.name(),
					pair.baseScenarioKey(),
					pair.variantScenarioKey(),
					campaignCase.key(),
					campaignCase.name(),
					campaignCase.weight(),
					variant.directionalScore() - base.directionalScore(),
					variant.legalStability() - base.legalStability(),
					variant.precedentStability() - base.precedentStability(),
					variant.statutoryStability() - base.statutoryStability(),
					variant.interbranchCompliance() - base.interbranchCompliance(),
					variant.rightsProtection() - base.rightsProtection(),
					variant.partisanAlignment() - base.partisanAlignment(),
					variant.shadowDocketAbuse() - base.shadowDocketAbuse(),
					variant.legitimacy() - base.legitimacy(),
					variant.reversalRate() - base.reversalRate(),
					variant.constitutionalConflict() - base.constitutionalConflict(),
					variant.democraticResponsiveness() - base.democraticResponsiveness(),
					variant.administrativeCost() - base.administrativeCost(),
					variant.lowerCourtCompliance() - base.lowerCourtCompliance(),
					variant.lowerCourtResistanceRisk() - base.lowerCourtResistanceRisk(),
					variant.enforcementCapacity() - base.enforcementCapacity(),
					variant.governmentNoncomplianceRate() - base.governmentNoncomplianceRate(),
					variant.emergencyOpportunism() - base.emergencyOpportunism(),
					variant.emergencyDownstreamEffect() - base.emergencyDownstreamEffect(),
					variant.precedentDurability() - base.precedentDurability(),
					variant.justiceReplacementRate() - base.justiceReplacementRate(),
					variant.overrideAttemptRate() - base.overrideAttemptRate(),
					variant.overrideRate() - base.overrideRate()
			);
		}
	}
	
	
	private static final class SummaryTotals
	{
		private final String mechanismKey;
		private final String mechanismName;
		private final String baseScenarioKey;
		private final String variantScenarioKey;
		private double weight;
		private double deltaDirectional;
		private double deltaLegalStability;
		private double deltaPrecedentStability;
		private double deltaStatutoryStability;
		private double deltaInterbranchCompliance;
		private double deltaRightsProtection;
		private double deltaPartisanAlignment;
		private double deltaShadowDocketAbuse;
		private double deltaLegitimacy;
		private double deltaReversalRate;
		private double deltaConstitutionalConflict;
		private double deltaDemocraticResponsiveness;
		private double deltaAdministrativeCost;
		private double deltaLowerCourtCompliance;
		private double deltaLowerCourtResistanceRisk;
		private double deltaEnforcementCapacity;
		private double deltaGovernmentNoncomplianceRate;
		private double deltaEmergencyOpportunism;
		private double deltaEmergencyDownstreamEffect;
		private double deltaPrecedentDurability;
		private double deltaJusticeReplacementRate;
		private double deltaOverrideAttemptRate;
		private double deltaOverrideRate;
		
		private SummaryTotals(AblationRow row) {
			mechanismKey = row.mechanismKey();
			mechanismName = row.mechanismName();
			baseScenarioKey = row.baseScenarioKey();
			variantScenarioKey = row.variantScenarioKey();
		}
		
		private void add(AblationRow row) {
			double rowWeight = row.caseWeight();
			weight += rowWeight;
			deltaDirectional += row.deltaDirectional() * rowWeight;
			deltaLegalStability += row.deltaLegalStability() * rowWeight;
			deltaPrecedentStability += row.deltaPrecedentStability() * rowWeight;
			deltaStatutoryStability += row.deltaStatutoryStability() * rowWeight;
			deltaInterbranchCompliance += row.deltaInterbranchCompliance() * rowWeight;
			deltaRightsProtection += row.deltaRightsProtection() * rowWeight;
			deltaPartisanAlignment += row.deltaPartisanAlignment() * rowWeight;
			deltaShadowDocketAbuse += row.deltaShadowDocketAbuse() * rowWeight;
			deltaLegitimacy += row.deltaLegitimacy() * rowWeight;
			deltaReversalRate += row.deltaReversalRate() * rowWeight;
			deltaConstitutionalConflict += row.deltaConstitutionalConflict() * rowWeight;
			deltaDemocraticResponsiveness += row.deltaDemocraticResponsiveness() * rowWeight;
			deltaAdministrativeCost += row.deltaAdministrativeCost() * rowWeight;
			deltaLowerCourtCompliance += row.deltaLowerCourtCompliance() * rowWeight;
			deltaLowerCourtResistanceRisk += row.deltaLowerCourtResistanceRisk() * rowWeight;
			deltaEnforcementCapacity += row.deltaEnforcementCapacity() * rowWeight;
			deltaGovernmentNoncomplianceRate += row.deltaGovernmentNoncomplianceRate() * rowWeight;
			deltaEmergencyOpportunism += row.deltaEmergencyOpportunism() * rowWeight;
			deltaEmergencyDownstreamEffect += row.deltaEmergencyDownstreamEffect() * rowWeight;
			deltaPrecedentDurability += row.deltaPrecedentDurability() * rowWeight;
			deltaJusticeReplacementRate += row.deltaJusticeReplacementRate() * rowWeight;
			deltaOverrideAttemptRate += row.deltaOverrideAttemptRate() * rowWeight;
			deltaOverrideRate += row.deltaOverrideRate() * rowWeight;
		}
		
		private AblationSummary toSummary() {
			double denominator = Math.max(1.0, weight);
			return new AblationSummary(
					mechanismKey,
					mechanismName,
					baseScenarioKey,
					variantScenarioKey,
					deltaDirectional / denominator,
					deltaLegalStability / denominator,
					deltaPrecedentStability / denominator,
					deltaStatutoryStability / denominator,
					deltaInterbranchCompliance / denominator,
					deltaRightsProtection / denominator,
					deltaPartisanAlignment / denominator,
					deltaShadowDocketAbuse / denominator,
					deltaLegitimacy / denominator,
					deltaReversalRate / denominator,
					deltaConstitutionalConflict / denominator,
					deltaDemocraticResponsiveness / denominator,
					deltaAdministrativeCost / denominator,
					deltaLowerCourtCompliance / denominator,
					deltaLowerCourtResistanceRisk / denominator,
					deltaEnforcementCapacity / denominator,
					deltaGovernmentNoncomplianceRate / denominator,
					deltaEmergencyOpportunism / denominator,
					deltaEmergencyDownstreamEffect / denominator,
					deltaPrecedentDurability / denominator,
					deltaJusticeReplacementRate / denominator,
					deltaOverrideAttemptRate / denominator,
					deltaOverrideRate / denominator
			);
		}
	}
	
	
	private record AblationSummary(
			String mechanismKey,
			String mechanismName,
			String baseScenarioKey,
			String variantScenarioKey,
			double deltaDirectional,
			double deltaLegalStability,
			double deltaPrecedentStability,
			double deltaStatutoryStability,
			double deltaInterbranchCompliance,
			double deltaRightsProtection,
			double deltaPartisanAlignment,
			double deltaShadowDocketAbuse,
			double deltaLegitimacy,
			double deltaReversalRate,
			double deltaConstitutionalConflict,
			double deltaDemocraticResponsiveness,
			double deltaAdministrativeCost,
			double deltaLowerCourtCompliance,
			double deltaLowerCourtResistanceRisk,
			double deltaEnforcementCapacity,
			double deltaGovernmentNoncomplianceRate,
			double deltaEmergencyOpportunism,
			double deltaEmergencyDownstreamEffect,
			double deltaPrecedentDurability,
			double deltaJusticeReplacementRate,
			double deltaOverrideAttemptRate,
			double deltaOverrideRate
	)
	{
	}
}
