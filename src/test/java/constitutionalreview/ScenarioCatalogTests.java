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
        List<Scenario> scenarios = ScenarioCatalog.scenariosForKeys(keys);
        TestSupport.check(scenarios.size() == keys.size(), "every scenario key should resolve");
        TestSupport.check(ScenarioCatalog.defaultScenarios().size() >= 10, "default scenario set should be broad");
    }
}
