package constitutionalreview.model;

public record ReviewCase(
        String id,
        CaseType type,
        double legalAmbiguity,
        double rightsBurden,
        double democraticMandate,
        double partisanSalience,
        double lawIdeology,
        double emergencyPressure,
        double executiveDefianceRisk,
        double legislativeQuality,
        double constitutionalConflictPotential,
        double publicAttention
) {
}
