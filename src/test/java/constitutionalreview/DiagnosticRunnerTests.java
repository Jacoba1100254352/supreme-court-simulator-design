package constitutionalreview;

import constitutionalreview.experiment.CalibrationRunner;
import constitutionalreview.experiment.DiagnosticResult;
import constitutionalreview.experiment.MechanismAblationRunner;
import constitutionalreview.experiment.SeedRobustnessRunner;
import constitutionalreview.model.LegislativeOutputProfile;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public final class DiagnosticRunnerTests {
    private DiagnosticRunnerTests() {
    }

    public static void run() throws IOException {
        Path outputDir = Files.createTempDirectory("constitutional-review-diagnostics");
        LegislativeOutputProfile profile = LegislativeOutputProfile.neutral().withSourceName("test profile");
        checkResult(CalibrationRunner.run(outputDir, 2, 8, 20260501L, profile, null), "Calibration Baseline");
        checkResult(SeedRobustnessRunner.run(outputDir, 1, 6, 20260501L, profile, null), "Seed Robustness");
        checkResult(MechanismAblationRunner.run(outputDir, 1, 6, 20260501L, profile, null), "Mechanism Ablation");
    }

    private static void checkResult(DiagnosticResult result, String title) throws IOException {
        TestSupport.check(Files.exists(result.csvPath()), title + " should write csv");
        TestSupport.check(Files.exists(result.markdownPath()), title + " should write markdown");
        TestSupport.check(Files.exists(result.manifestPath()), title + " should write manifest");
        TestSupport.check(Files.readString(result.markdownPath()).contains(title), title + " markdown should contain title");
    }
}
