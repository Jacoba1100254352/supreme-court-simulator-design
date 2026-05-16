package constitutionalreview;


import constitutionalreview.experiment.*;
import constitutionalreview.model.LegislativeOutputProfile;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;


public final class DiagnosticRunnerTests
{
	private DiagnosticRunnerTests() {
	}
	
	public static void run() throws IOException {
		Path outputDir = Files.createTempDirectory("constitutional-review-diagnostics");
		LegislativeOutputProfile profile = LegislativeOutputProfile.neutral().withSourceName("test profile");
		checkResult(CalibrationRunner.run(outputDir, 2, 8, 20260501L, profile, null), "Calibration Baseline");
		checkResult(SeedRobustnessRunner.run(outputDir, 1, 6, 20260501L, profile, null), "Seed Robustness");
		checkResult(MechanismAblationRunner.run(outputDir, 1, 6, 20260501L, profile, null), "Mechanism Ablation");
		checkResult(ParameterSweepRunner.run(outputDir, 1, 6, 20260501L, profile, null), "Parameter Sweep");
		checkResult(PriorUncertaintyRunner.run(outputDir, 1, 6, 3, 20260501L, profile, null), "Sampled Prior Uncertainty");
		Path familyDir = Files.createTempDirectory("legislative-family");
		Files.writeString(familyDir.resolve("simulation-campaign-v0.csv"), """
				caseKey,caseWeight,productivity,welfare,weakPublicMandatePassage,minorityHarm,lobbyCapture,policyShift,legitimacy
				baseline,1.0,0.40,0.70,0.20,0.10,0.30,0.25,0.65
				""");
		Files.writeString(familyDir.resolve("simulation-campaign-v10.csv"), """
				caseKey,caseWeight,productivity,welfare,weakPublicMandatePassage,minorityHarm,lobbyCapture,policyShift,legitimacy
				pressure,1.0,0.70,0.42,0.50,0.48,0.60,0.55,0.38
				""");
		checkResult(LegislativeFamilyComparisonRunner.run(outputDir, familyDir, 1, 6, 20260501L), "Legislative Family");
	}
	
	private static void checkResult(DiagnosticResult result, String title) throws IOException {
		TestSupport.check(Files.exists(result.csvPath()), title + " should write csv");
		TestSupport.check(Files.exists(result.markdownPath()), title + " should write markdown");
		TestSupport.check(Files.exists(result.manifestPath()), title + " should write manifest");
		TestSupport.check(Files.readString(result.markdownPath()).contains(title), title + " markdown should contain title");
	}
}
