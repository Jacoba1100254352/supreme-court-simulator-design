package constitutionalreview;

public final class SimulatorTests {
    private SimulatorTests() {
    }

    public static void main(String[] args) throws Exception {
        ScenarioCatalogTests.run();
        SimulatorInvariantTests.run();
        LegislativeOutputImporterTests.run();
        CampaignRunnerTests.run();
        DiagnosticRunnerTests.run();
        System.out.println("All constitutional review simulator tests passed.");
    }
}
