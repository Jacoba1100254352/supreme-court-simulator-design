package constitutionalreview.model;

public record ReviewCase(
        String id,
        CaseType type,
        DocketType docketType,
        double legalAmbiguity,
        double rightsBurden,
        double democraticMandate,
        double partisanSalience,
        double lawIdeology,
        double emergencyPressure,
        double requestedEmergencyRelief,
        double executiveDefianceRisk,
        double legislativeQuality,
        double constitutionalConflictPotential,
        double publicAttention,
        double overridePressure
) {
}
