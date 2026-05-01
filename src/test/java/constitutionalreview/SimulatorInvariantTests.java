package constitutionalreview;

import constitutionalreview.model.LegislativeOutputProfile;
import constitutionalreview.simulation.ScenarioCatalog;
import constitutionalreview.simulation.ScenarioReport;
import constitutionalreview.simulation.Simulator;
import constitutionalreview.simulation.WorldSpec;

import java.util.List;

public final class SimulatorInvariantTests {
    private SimulatorInvariantTests() {
    }

    public static void run() {
        Simulator simulator = new Simulator();
        List<ScenarioReport> first = simulator.compare(
                ScenarioCatalog.defaultScenarios(),
                WorldSpec.baseline(20, LegislativeOutputProfile.neutral()),
                8,
                1234L
        );
        List<ScenarioReport> second = simulator.compare(
                ScenarioCatalog.defaultScenarios(),
                WorldSpec.baseline(20, LegislativeOutputProfile.neutral()),
                8,
                1234L
        );
        TestSupport.check(first.size() == second.size(), "deterministic runs should produce same report count");
        for (int i = 0; i < first.size(); i++) {
            ScenarioReport a = first.get(i);
            ScenarioReport b = second.get(i);
            TestSupport.check(a.scenarioKey().equals(b.scenarioKey()), "scenario order should be deterministic");
            TestSupport.check(Math.abs(a.directionalScore() - b.directionalScore()) < 0.000_000_1, "directional score should be deterministic");
            checkReport(a);
        }
    }

    private static void checkReport(ScenarioReport report) {
        TestSupport.check(report.totalCases() == 160, "total cases should equal runs * cases");
        TestSupport.checkUnitInterval(report.directionalScore(), "directionalScore");
        TestSupport.checkUnitInterval(report.legalStability(), "legalStability");
        TestSupport.checkUnitInterval(report.rightsProtection(), "rightsProtection");
        TestSupport.checkUnitInterval(report.partisanAlignment(), "partisanAlignment");
        TestSupport.checkUnitInterval(report.shadowDocketAbuse(), "shadowDocketAbuse");
        TestSupport.checkUnitInterval(report.legitimacy(), "legitimacy");
        TestSupport.checkUnitInterval(report.reversalRate(), "reversalRate");
        TestSupport.checkUnitInterval(report.constitutionalConflict(), "constitutionalConflict");
        TestSupport.checkUnitInterval(report.democraticResponsiveness(), "democraticResponsiveness");
        TestSupport.checkUnitInterval(report.administrativeCost(), "administrativeCost");
        TestSupport.checkUnitInterval(report.concurrenceRate(), "concurrenceRate");
        TestSupport.checkUnitInterval(report.dissentRate(), "dissentRate");
    }
}
