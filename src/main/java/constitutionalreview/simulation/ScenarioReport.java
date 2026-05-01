package constitutionalreview.simulation;

import constitutionalreview.util.Values;

public record ScenarioReport(
        String scenarioKey,
        String scenarioName,
        int totalCases,
        double meritsReviewRate,
        double invalidationRate,
        double legalStability,
        double rightsProtection,
        double partisanAlignment,
        double shadowDocketAbuse,
        double legitimacy,
        double reversalRate,
        double constitutionalConflict,
        double democraticResponsiveness,
        double independenceAccountabilityBalance,
        double administrativeCost,
        double emergencyOrderRate,
        double shadowReliefRate,
        double recusalRate,
        double concurrenceRate,
        double dissentRate,
        double panelRate,
        double enBancRate,
        double crossCheckDisagreementRate,
        double councilWarningRate,
        double overrideRate
) {
    public double stabilityRightsScore() {
        return Values.average(
                legalStability,
                rightsProtection,
                MetricDefinition.lowerIsBetter(reversalRate),
                MetricDefinition.lowerIsBetter(constitutionalConflict)
        );
    }

    public double legitimacyControlScore() {
        return Values.average(
                legitimacy,
                democraticResponsiveness,
                independenceAccountabilityBalance,
                MetricDefinition.lowerIsBetter(partisanAlignment),
                MetricDefinition.lowerIsBetter(shadowDocketAbuse)
        );
    }

    public double directionalScore() {
        return Values.average(
                stabilityRightsScore(),
                legitimacyControlScore(),
                MetricDefinition.lowerIsBetter(administrativeCost)
        );
    }
}
