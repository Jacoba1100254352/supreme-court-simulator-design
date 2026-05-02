package constitutionalreview.simulation;

import constitutionalreview.util.Values;

public record ScenarioReport(
        String scenarioKey,
        String scenarioName,
        int totalCases,
        double petitionFiledRate,
        double admissionRate,
        double screenOutRate,
        double meritsTransferRate,
        double paidPetitionRate,
        double ifpPetitionRate,
        double solicitorGeneralSignalRate,
        double amicusIntensity,
        double splitMaturity,
        double relistRate,
        double specialistCounselRate,
        double vehicleDefectRisk,
        double conditionalReversalProbability,
        double meritsReviewRate,
        double invalidationRate,
        double legalStability,
        double precedentStability,
        double statutoryStability,
        double interbranchCompliance,
        double rightsProtection,
        double partisanAlignment,
        double shadowDocketAbuse,
        double emergencyLegitimacyRisk,
        double legitimacy,
        double reversalRate,
        double constitutionalConflict,
        double democraticResponsiveness,
        double independenceAccountabilityBalance,
        double administrativeCost,
        double emergencyOrderRate,
        double emergencyGrantRate,
        double shadowReliefRate,
        double reasonedEmergencyOrderRate,
        double temporaryStayRate,
        double meritsAccelerationRate,
        double expiredEmergencyOrderRate,
        double recusalRate,
        double quorumFailureRate,
        double justiceReplacementRate,
        double concurrenceRate,
        double dissentRate,
        double fragmentationIndex,
        double panelRate,
        double enBancRate,
        double crossCheckDisagreementRate,
        double councilWarningRate,
        double overrideAttemptRate,
        double overrideRate,
        double rightsCarveoutBlockRate,
        double repeatedOverrideRate,
        double legislativeDefiance,
        double executiveEmergencyStrategy,
        double appointmentManipulationPressure,
        double overrideAdaptation,
        double legislativeComplianceRate,
        double legislativeEvasionRate,
        double delayedReenactmentStrategyRate,
        double executiveEmergencyFloodRate,
        double overrideCampaignRate,
        double appointmentPressureCampaignRate,
        double formalRepealRate,
        double formalReplacementRate,
        double formalNarrowedReenactmentRate,
        double formalWeakOverrideRate,
        double formalAmendmentRate,
        double formalCourtCurbingRate,
        double formalOpenDefianceRate,
        double practicalDelayRate,
        double practicalAdministrativeSubstitutionRate,
        double practicalSymbolicComplianceRate,
        double practicalBureaucraticResistanceRate,
        double practicalOpenNoncomplianceRate,
        double rightsClaimantCaseRate,
        double rightsClaimantSuccess,
        double rightsDomainClaimantSuccess,
        double structuralDomainClaimantSuccess,
        double electionDomainClaimantSuccess,
        double executivePowerDomainClaimantSuccess,
        double administrativeDomainClaimantSuccess,
        double economicDomainClaimantSuccess,
        double doctrinalDepth,
        double remedialBreadth,
        double lowerCourtCompliance,
        double eliteAcceptance,
        double publicConfidence,
        double facialChallengeRate,
        double asAppliedChallengeRate,
        double electionDisputeRate,
        double emergencyStayDocketRate,
        double executivePowerDisputeRate,
        double administrativeLawRate,
        double rightsClaimRate
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
                MetricDefinition.lowerIsBetter(shadowDocketAbuse),
                MetricDefinition.lowerIsBetter(emergencyLegitimacyRisk),
                MetricDefinition.lowerIsBetter(strategicPressure())
        );
    }

    public double strategicPressure() {
        return Values.average(
                legislativeDefiance,
                executiveEmergencyStrategy,
                appointmentManipulationPressure,
                overrideAdaptation,
                legislativeEvasionRate,
                executiveEmergencyFloodRate,
                overrideCampaignRate,
                appointmentPressureCampaignRate,
                formalCourtCurbingRate,
                formalOpenDefianceRate,
                practicalOpenNoncomplianceRate
        );
    }

    public double directionalScore() {
        return Values.average(
                stabilityRightsScore(),
                legitimacyControlScore(),
                rightsClaimantSuccess,
                eliteAcceptance,
                MetricDefinition.lowerIsBetter(administrativeCost)
        );
    }
}
