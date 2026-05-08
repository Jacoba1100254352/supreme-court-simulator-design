package constitutionalreview;

import constitutionalreview.experiment.CampaignResult;
import constitutionalreview.experiment.CampaignRunner;
import constitutionalreview.model.LegislativeOutputProfile;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public final class CampaignRunnerTests {
    private CampaignRunnerTests() {
    }

    public static void run() throws IOException {
        Path outputDir = Files.createTempDirectory("constitutional-review-campaign");
        CampaignResult result = CampaignRunner.runV1(
                outputDir,
                2,
                8,
                20260501L,
                LegislativeOutputProfile.neutral().withSourceName("test imported profile"),
                null
        );
        TestSupport.check(Files.exists(result.csvPath()), "campaign should write csv");
        TestSupport.check(Files.exists(result.markdownPath()), "campaign should write markdown");
        TestSupport.check(Files.exists(result.manifestPath()), "campaign should write manifest");
        String markdown = Files.readString(result.markdownPath());
        TestSupport.check(markdown.contains("Scenario Averages Across Cases"), "markdown should include scenario table");
        TestSupport.check(markdown.contains("Top directional-score cluster"), "markdown should report score clusters");
        TestSupport.check(markdown.contains("close differences are not interpreted as rankings"), "markdown should discourage close-score rankings");
        TestSupport.check(markdown.contains("precedent durability, lower-court compliance"), "markdown should explain expanded directional-score components");
        TestSupport.check(markdown.contains("Cert admit"), "markdown should include certiorari admission diagnostics");
        TestSupport.check(markdown.contains("Emerg. downstream"), "markdown should include emergency downstream diagnostics");
        TestSupport.check(markdown.contains("governmentNoncomplianceRate"), "markdown should include noncompliance direction guidance");
        TestSupport.check(markdown.contains("Resistance"), "markdown should include lower-court resistance diagnostics");
        TestSupport.check(markdown.contains("Enforcement"), "markdown should include enforcement-capacity diagnostics");
        TestSupport.check(markdown.contains("Stress Case Leaders"), "markdown should include stress-case slices");

        CampaignResult v2 = CampaignRunner.runV2(
                outputDir,
                1,
                6,
                20260501L,
                LegislativeOutputProfile.neutral().withSourceName("test imported profile"),
                null
        );
        String csv = Files.readString(v2.csvPath());
        TestSupport.check(csv.contains("precedentStability"), "v2 csv should include split stability metrics");
        TestSupport.check(csv.contains("certiorariAdmissionRate"), "v2 csv should include certiorari admission metrics");
        TestSupport.check(csv.contains("lowerCourtSplitDepth"), "v2 csv should include lower-court split depth");
        TestSupport.check(csv.contains("lowerCourtResistanceRisk"), "v2 csv should include lower-court resistance");
        TestSupport.check(csv.contains("forumShoppingPressure"), "v2 csv should include forum-shopping pressure");
        TestSupport.check(csv.contains("settledBeforeReviewRate"), "v2 csv should include pre-review settlement");
        TestSupport.check(csv.contains("enforcementCapacity"), "v2 csv should include enforcement capacity");
        TestSupport.check(csv.contains("emergencyOpportunism"), "v2 csv should include emergency opportunism");
        TestSupport.check(csv.contains("strategicPlaintiffSelection"), "v2 csv should include strategic plaintiff selection");
        TestSupport.check(csv.contains("repeatPlayerAdvantage"), "v2 csv should include repeat-player advantage");
        TestSupport.check(csv.contains("governmentNoncomplianceRate"), "v2 csv should include government noncompliance");
        TestSupport.check(csv.contains("emergencyDownstreamEffect"), "v2 csv should include emergency downstream effects");
        TestSupport.check(csv.contains("appointment-timing-manipulation"), "v2 campaign should include manipulation cases");
        TestSupport.check(csv.contains("mandatory-written-emergency-reasoning"), "v2 campaign should include written emergency reasoning scenario");
        TestSupport.check(csv.contains("constitutional-remand"), "v2 campaign should include constitutional remand scenario");
        TestSupport.check(csv.contains("emergency-integrity-package"), "v2 campaign should include bundled emergency-integrity scenario");
    }
}
