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
		checkDirectCertiorariObservationPrecedence();
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

	private static void checkDirectCertiorariObservationPrecedence() throws IOException {
		Path dataDir = Files.createTempDirectory("calibration-observation-precedence");
		Files.writeString(
				dataDir.resolve("direct.csv"),
				"""
				sourceKey,domain,metric,term,numerator,denominator,value,sourceUrl,notes
				scotus-certiorari-docketed-cohort-ot2023,U.S. Supreme Court certiorari,paidPetitionShare,OT2023,1375,4222,0.325675036,https://example.test/docket,direct cohort
				"""
		);
		Files.writeString(
				dataDir.resolve("supreme-court-simulator-calibration-targets.csv"),
				"""
				metricKey,observedValue,jurisdiction,timePeriod,lowerBound,upperBound,sourceUrl
				paidPetitionShare,0.3257,U.S. Supreme Court,OT2023,0.3257,0.3257,https://example.test/journal
				cfrRate_paid,0.047,U.S. Supreme Court,OT2001-OT2004,0.047,0.047,https://example.test/study
				"""
		);
		EmpiricalCalibrationDataset dataset = EmpiricalCalibrationDataset.load(dataDir);
		long paidRows = dataset.observations().stream()
		                       .filter(row -> row.metric().equals("paidPetitionShare"))
		                       .count();
		long independentRows = dataset.observations().stream()
		                              .filter(row -> row.metric().equals("cfrRate_paid"))
		                              .count();
		TestSupport.check(
				paidRows == 1,
				"direct certiorari cohort should supersede its near-identical summary row"
		);
		TestSupport.check(
				independentRows == 1,
				"independent different-term certiorari observations should remain"
		);
	}
	
	private static void checkResult(DiagnosticResult result, String title) throws IOException {
		TestSupport.check(Files.exists(result.csvPath()), title + " should write csv");
		TestSupport.check(Files.exists(result.markdownPath()), title + " should write markdown");
		TestSupport.check(Files.exists(result.manifestPath()), title + " should write manifest");
		TestSupport.check(Files.readString(result.markdownPath()).contains(title), title + " markdown should contain title");
	}
}
