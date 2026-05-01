package constitutionalreview.simulation;

import constitutionalreview.model.CaseType;
import constitutionalreview.model.DocketType;

public record LegalDomainProfile(
        double legalAmbiguityShift,
        double rightsBurdenShift,
        double democraticMandateShift,
        double partisanSalienceShift,
        double emergencyPressureShift,
        double requestedEmergencyReliefShift,
        double executiveDefianceRiskShift,
        double legislativeQualityShift,
        double conflictPotentialShift,
        double publicAttentionShift,
        double overridePressureShift
) {
    public static LegalDomainProfile forCase(CaseType type, DocketType docketType) {
        LegalDomainProfile profile = switch (type) {
            case RIGHTS -> new LegalDomainProfile(0.03, 0.20, -0.04, 0.04, 0.02, 0.02, 0.02, -0.02, 0.08, 0.07, 0.04);
            case ELECTIONS -> new LegalDomainProfile(0.05, 0.08, -0.06, 0.15, 0.14, 0.10, 0.08, -0.03, 0.12, 0.12, 0.08);
            case EXECUTIVE_POWER -> new LegalDomainProfile(0.06, 0.02, 0.00, 0.08, 0.13, 0.11, 0.18, -0.02, 0.12, 0.08, 0.06);
            case ADMINISTRATIVE_STATE -> new LegalDomainProfile(0.09, -0.03, 0.02, 0.03, 0.02, 0.01, 0.04, -0.05, 0.06, -0.02, 0.03);
            case STRUCTURAL -> new LegalDomainProfile(0.07, 0.00, 0.01, 0.05, 0.01, 0.01, 0.05, 0.00, 0.09, 0.03, 0.04);
            case ECONOMIC_REGULATION -> new LegalDomainProfile(0.02, -0.06, 0.07, 0.04, 0.00, 0.00, 0.01, 0.02, 0.02, 0.01, 0.05);
        };
        return profile.plus(docketProfile(docketType));
    }

    private static LegalDomainProfile docketProfile(DocketType docketType) {
        return switch (docketType) {
            case FACIAL_CHALLENGE -> new LegalDomainProfile(0.04, 0.02, 0.00, 0.03, 0.00, 0.00, 0.01, -0.01, 0.06, 0.04, 0.03);
            case AS_APPLIED_CHALLENGE -> new LegalDomainProfile(0.02, -0.01, 0.01, -0.01, 0.00, 0.00, 0.00, 0.02, -0.01, -0.02, -0.01);
            case ELECTION_DISPUTE -> new LegalDomainProfile(0.05, 0.07, -0.08, 0.16, 0.14, 0.12, 0.10, -0.03, 0.13, 0.14, 0.09);
            case EMERGENCY_STAY_APPLICATION -> new LegalDomainProfile(0.02, 0.03, -0.02, 0.05, 0.22, 0.20, 0.09, -0.02, 0.08, 0.08, 0.05);
            case EXECUTIVE_POWER_DISPUTE -> new LegalDomainProfile(0.04, 0.00, 0.01, 0.08, 0.14, 0.12, 0.18, -0.02, 0.13, 0.08, 0.07);
            case ADMINISTRATIVE_LAW_CHALLENGE -> new LegalDomainProfile(0.08, -0.03, 0.02, 0.02, 0.02, 0.01, 0.04, -0.05, 0.05, -0.02, 0.03);
            case RIGHTS_CLAIM -> new LegalDomainProfile(0.04, 0.18, -0.04, 0.05, 0.03, 0.02, 0.03, -0.02, 0.09, 0.07, 0.05);
        };
    }

    private LegalDomainProfile plus(LegalDomainProfile other) {
        return new LegalDomainProfile(
                legalAmbiguityShift + other.legalAmbiguityShift,
                rightsBurdenShift + other.rightsBurdenShift,
                democraticMandateShift + other.democraticMandateShift,
                partisanSalienceShift + other.partisanSalienceShift,
                emergencyPressureShift + other.emergencyPressureShift,
                requestedEmergencyReliefShift + other.requestedEmergencyReliefShift,
                executiveDefianceRiskShift + other.executiveDefianceRiskShift,
                legislativeQualityShift + other.legislativeQualityShift,
                conflictPotentialShift + other.conflictPotentialShift,
                publicAttentionShift + other.publicAttentionShift,
                overridePressureShift + other.overridePressureShift
        );
    }
}
