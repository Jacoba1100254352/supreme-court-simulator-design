package constitutionalreview;

import constitutionalreview.simulation.Scenario;
import constitutionalreview.simulation.ScenarioCatalog;

import java.util.List;

public final class ScenarioCatalogTests {
    private ScenarioCatalogTests() {
    }

    public static void run() {
        List<String> keys = ScenarioCatalog.scenarioKeys();
        TestSupport.check(keys.contains("current-us-like"), "catalog should include current-us-like");
        TestSupport.check(keys.contains("cross-checking-courts"), "catalog should include cross-checking-courts");
        TestSupport.check(keys.contains("constitutional-council"), "catalog should include constitutional-council");
        TestSupport.check(keys.contains("randomized-merits-panels"), "catalog should include randomized-merits-panels");
        TestSupport.check(keys.contains("mandatory-written-emergency-reasoning"), "catalog should include mandatory-written-emergency-reasoning");
        TestSupport.check(keys.contains("automatic-merits-follow-up"), "catalog should include automatic-merits-follow-up");
        TestSupport.check(keys.contains("strong-recusal-enforcement"), "catalog should include strong-recusal-enforcement");
        TestSupport.check(keys.contains("jurisdiction-stripping-constraints"), "catalog should include jurisdiction-stripping-constraints");
        TestSupport.check(keys.contains("legislative-override-window"), "catalog should include legislative-override-window");
        TestSupport.check(keys.contains("constitutional-remand"), "catalog should include constitutional-remand");
        TestSupport.check(keys.contains("public-interest-litigation-filter"), "catalog should include public-interest-litigation-filter");
        List<Scenario> scenarios = ScenarioCatalog.scenariosForKeys(keys);
        TestSupport.check(scenarios.size() == keys.size(), "every scenario key should resolve");
        TestSupport.check(ScenarioCatalog.defaultScenarios().size() >= 10, "default scenario set should be broad");
    }
}
