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
        TestSupport.check(csv.contains("appointment-timing-manipulation"), "v2 campaign should include manipulation cases");
    }
}
