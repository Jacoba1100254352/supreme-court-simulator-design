package constitutionalreview;


import constitutionalreview.experiment.*;
import constitutionalreview.importer.LegislativeOutputImporter;
import constitutionalreview.model.LegislativeOutputProfile;
import constitutionalreview.simulation.*;
import constitutionalreview.util.Values;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Locale;


public final class Main
{
	private Main() {
	}
	
	static void main(String[] args) {
		Options options = Options.parse(args);
		if (options.help) {
			Options.printUsage();
			return;
		}
		
		LegislativeOutputProfile profile = loadLegislativeProfile(options.legislativeInput);
		if (options.campaignName != null) {
			runCampaign(options, profile);
			return;
		}
		if (runDiagnostics(options, profile)) {
			return;
		}
		
		List<Scenario> scenarios = scenarios(options);
		WorldSpec spec = new WorldSpec(
				options.cases,
				options.justicePoolSize,
				options.polarization,
				options.appointmentCapture,
				options.publicPressure,
				options.emergencyShare,
				profile
		);
		Simulator simulator = new Simulator();
		List<ScenarioReport> reports = simulator.compare(scenarios, spec, options.runs, options.seed);
		printReports(reports, profile);
	}
	
	private static LegislativeOutputProfile loadLegislativeProfile(Path input) {
		if (input == null) {
			return LegislativeOutputProfile.neutral();
		}
		try {
			return LegislativeOutputImporter.importCsv(input);
		} catch (IOException exception) {
			throw new IllegalStateException("Unable to import legislative output CSV: " + input, exception);
		}
	}
	
	private static void runCampaign(Options options, LegislativeOutputProfile profile) {
		try {
			LegislativeOutputProfile imported = options.legislativeInput == null ? null : profile;
			CampaignResult result = switch (options.campaignName) {
				case "v0" -> CampaignRunner.runV0(
						options.outputDir,
						options.runs,
						options.cases,
						options.seed,
						imported,
						options.legislativeInput
				);
				case "v1" -> CampaignRunner.runV1(
						options.outputDir,
						options.runs,
						options.cases,
						options.seed,
						imported,
						options.legislativeInput
				);
				case "v2" -> CampaignRunner.runV2(
						options.outputDir,
						options.runs,
						options.cases,
						options.seed,
						imported,
						options.legislativeInput
				);
				case "manipulation-stress" -> CampaignRunner.runManipulationStress(
						options.outputDir,
						options.runs,
						options.cases,
						options.seed,
						imported,
						options.legislativeInput
				);
				default -> throw new IllegalArgumentException("Unknown campaign: " + options.campaignName);
			};
			System.out.println("Constitutional review campaign complete.");
			System.out.println("CSV: " + result.csvPath());
			System.out.println("Markdown: " + result.markdownPath());
			System.out.println("Manifest: " + result.manifestPath());
		} catch (IOException exception) {
			throw new IllegalStateException("Unable to write campaign outputs.", exception);
		}
	}
	
	private static boolean runDiagnostics(Options options, LegislativeOutputProfile profile) {
		boolean any = options.calibrate
				|| options.seedRobustness
				|| options.mechanismAblation
				|| options.parameterSweep
				|| options.priorUncertainty
				|| options.legislativeFamilyComparison;
		if (!any) {
			return false;
		}
		try {
			LegislativeOutputProfile imported = options.legislativeInput == null ? null : profile;
			if (options.calibrate) {
				printDiagnostic(CalibrationRunner.run(
						options.outputDir,
						options.calibrationDataDir,
						options.runs,
						options.cases,
						options.seed,
						imported,
						options.legislativeInput
				));
			}
			if (options.seedRobustness) {
				printDiagnostic(SeedRobustnessRunner.run(
						options.outputDir,
						options.runs,
						options.cases,
						options.seed,
						imported,
						options.legislativeInput
				));
			}
			if (options.mechanismAblation) {
				printDiagnostic(MechanismAblationRunner.run(
						options.outputDir,
						options.runs,
						options.cases,
						options.seed,
						imported,
						options.legislativeInput
				));
			}
			if (options.parameterSweep) {
				printDiagnostic(ParameterSweepRunner.run(
						options.outputDir,
						options.runs,
						options.cases,
						options.seed,
						imported,
						options.legislativeInput
				));
			}
			if (options.priorUncertainty) {
				printDiagnostic(PriorUncertaintyRunner.run(
						options.outputDir,
						options.runs,
						options.cases,
						options.priorSamples,
						options.seed,
						imported,
						options.legislativeInput
				));
			}
			if (options.legislativeFamilyComparison) {
				printDiagnostic(LegislativeFamilyComparisonRunner.run(
						options.outputDir,
						options.legislativeFamilyDir,
						options.runs,
						options.cases,
						options.seed
				));
			}
			return true;
		} catch (IOException exception) {
			throw new IllegalStateException("Unable to write diagnostic outputs.", exception);
		}
	}
	
	private static void printDiagnostic(DiagnosticResult result) {
		System.out.println(result.name() + " complete.");
		System.out.println("CSV: " + result.csvPath());
		System.out.println("Markdown: " + result.markdownPath());
		System.out.println("Manifest: " + result.manifestPath());
	}
	
	private static List<Scenario> scenarios(Options options) {
		if (!options.scenarioKeys.isEmpty()) {
			return ScenarioCatalog.scenariosForKeys(options.scenarioKeys);
		}
		if (options.allScenarios) {
			return ScenarioCatalog.allScenarios();
		}
		return ScenarioCatalog.defaultScenarios();
	}
	
	private static void printReports(List<ScenarioReport> reports, LegislativeOutputProfile profile) {
		System.out.println("Legislative input: " + LegislativeOutputImporter.describe(profile));
		System.out.println();
		System.out.printf(
				Locale.ROOT,
				"%-40s %7s %7s %7s %7s %7s %7s %7s %7s %7s %7s %7s%n",
				"Scenario",
				"Score",
				"Admit",
				"Stable",
				"Rights",
				"Partisan",
				"Irreg.",
				"Emerg",
				"Legit",
				"Conflict",
				"Resp",
				"LegitPx"
		);
		for (ScenarioReport report : reports) {
			System.out.printf(
					Locale.ROOT,
					"%-40s %7s %7s %7s %7s %7s %7s %7s %7s %7s %7s %7s%n",
					truncate(report.scenarioName(), 40),
					Values.format3(report.directionalScore()),
					Values.format3(report.admissionRate()),
					Values.format3(report.legalStability()),
					Values.format3(report.rightsProtection()),
					Values.format3(report.partisanAlignment()),
					Values.format3(report.emergencyProcessIrregularity()),
					Values.format3(report.emergencyLegitimacyRisk()),
					Values.format3(report.legitimacy()),
					Values.format3(report.constitutionalConflict()),
					Values.format3(report.democraticResponsiveness()),
					Values.format3(report.processLegitimacyProxy())
			);
		}
	}
	
	private static String truncate(String value, int length) {
		if (value.length() <= length) {
			return value;
		}
		return value.substring(0, Math.max(0, length - 3)) + "...";
	}
	
	private static final class Options
	{
		private final List<String> scenarioKeys = new ArrayList<>();
		private boolean help;
		private int runs = 60;
		private int cases = 48;
		private int justicePoolSize = 31;
		private long seed = 20260501L;
		private double polarization = 0.52;
		private double appointmentCapture = 0.42;
		private double publicPressure = 0.45;
		private double emergencyShare = 0.18;
		private boolean allScenarios;
		private String campaignName;
		private boolean calibrate;
		private boolean seedRobustness;
		private boolean mechanismAblation;
		private boolean parameterSweep;
		private boolean priorUncertainty;
		private boolean legislativeFamilyComparison;
		private int priorSamples = 32;
		private Path outputDir = Path.of("reports");
		private Path calibrationDataDir = Path.of("data/calibration");
		private Path legislativeInput;
		private Path legislativeFamilyDir;
		
		private static Options parse(String[] args) {
			Options options = new Options();
			for (int i = 0; i < args.length; i++) {
				String arg = args[i];
				switch (arg) {
					case "--help", "-h" -> options.help = true;
					case "--runs" -> options.runs = parseInt(args, ++i, arg);
					case "--cases", "--case-count" -> options.cases = parseInt(args, ++i, arg);
					case "--justice-pool-size" -> options.justicePoolSize = parseInt(args, ++i, arg);
					case "--seed" -> options.seed = parseLong(args, ++i, arg);
					case "--polarization" -> options.polarization = parseDouble(args, ++i, arg);
					case "--appointment-capture" -> options.appointmentCapture = parseDouble(args, ++i, arg);
					case "--public-pressure" -> options.publicPressure = parseDouble(args, ++i, arg);
					case "--emergency-share" -> options.emergencyShare = parseDouble(args, ++i, arg);
					case "--all-scenarios" -> options.allScenarios = true;
					case "--campaign" -> options.campaignName = requireValue(args, ++i, arg);
					case "--calibrate" -> options.calibrate = true;
					case "--seed-robustness" -> options.seedRobustness = true;
					case "--mechanism-ablation" -> options.mechanismAblation = true;
					case "--parameter-sweep" -> options.parameterSweep = true;
					case "--prior-uncertainty" -> options.priorUncertainty = true;
					case "--prior-samples" -> options.priorSamples = parseInt(args, ++i, arg);
					case "--legislative-family-comparison" -> options.legislativeFamilyComparison = true;
					case "--output-dir" -> options.outputDir = Path.of(requireValue(args, ++i, arg));
					case "--legislative-input" -> options.legislativeInput = Path.of(requireValue(args, ++i, arg));
					case "--legislative-family-dir" -> options.legislativeFamilyDir = Path.of(requireValue(args, ++i, arg));
					case "--calibration-data-dir" -> options.calibrationDataDir = Path.of(requireValue(args, ++i, arg));
					case "--scenarios" -> options.scenarioKeys.addAll(parseList(requireValue(args, ++i, arg)));
					default -> throw new IllegalArgumentException("Unknown argument: " + arg);
				}
			}
			if (options.runs <= 0) {
				throw new IllegalArgumentException("--runs must be positive");
			}
			if (options.cases <= 0) {
				throw new IllegalArgumentException("--cases must be positive");
			}
			if (options.priorSamples <= 0) {
				throw new IllegalArgumentException("--prior-samples must be positive");
			}
			return options;
		}
		
		private static List<String> parseList(String value) {
			if (value.isBlank()) {
				return List.of();
			}
			return Arrays.stream(value.split(","))
			             .map(String::trim)
			             .filter(item -> !item.isEmpty())
			             .toList();
		}
		
		private static String requireValue(String[] args, int index, String flag) {
			if (index >= args.length) {
				throw new IllegalArgumentException(flag + " requires a value");
			}
			return args[index];
		}
		
		private static int parseInt(String[] args, int index, String flag) {
			return Integer.parseInt(requireValue(args, index, flag));
		}
		
		private static long parseLong(String[] args, int index, String flag) {
			return Long.parseLong(requireValue(args, index, flag));
		}
		
		private static double parseDouble(String[] args, int index, String flag) {
			return Double.parseDouble(requireValue(args, index, flag));
		}
		
		private static void printUsage() {
			System.out.println("""
					                   Constitutional Review Simulator
					                   
					                   Usage:
					                     make run ARGS="--runs 60 --cases 48"
					                     make campaign ARGS="--legislative-input /path/to/simulation-campaign.csv"
					                   
					                   Options:
					                     --runs N
					                     --cases N
					                     --seed N
					                     --scenarios key,key
					                     --all-scenarios
					                     --campaign v0|v1|v2|manipulation-stress
					                     --calibrate
					                     --seed-robustness
					                     --mechanism-ablation
					                     --parameter-sweep
					                     --prior-uncertainty
					                     --prior-samples N
					                     --legislative-family-comparison
					                     --output-dir DIR
					                     --calibration-data-dir DIR
					                     --legislative-input CSV
					                     --legislative-family-dir DIR
					                     --polarization VALUE
					                     --appointment-capture VALUE
					                     --public-pressure VALUE
					                     --emergency-share VALUE
					                   
					                   Scenario keys:
					                   """ + String.join(", ", ScenarioCatalog.scenarioKeys()));
		}
	}
}
