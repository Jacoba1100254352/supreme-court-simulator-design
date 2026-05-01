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
        double overridePressure,
        double lowerCourtConflict,
        double lowerCourtErrorRisk,
        double certiorariPressure
) {
    public ReviewCase withId(String id) {
        return new ReviewCase(
                id,
                type,
                docketType,
                legalAmbiguity,
                rightsBurden,
                democraticMandate,
                partisanSalience,
                lawIdeology,
                emergencyPressure,
                requestedEmergencyRelief,
                executiveDefianceRisk,
                legislativeQuality,
                constitutionalConflictPotential,
                publicAttention,
                overridePressure,
                lowerCourtConflict,
                lowerCourtErrorRisk,
                certiorariPressure
        );
    }
}
