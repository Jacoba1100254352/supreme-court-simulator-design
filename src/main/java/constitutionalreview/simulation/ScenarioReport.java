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
        double certiorariPathRate,
        double certiorariAdmissionRate,
        double paidPetitionRate,
        double ifpPetitionRate,
        double courtRequestedResponseRate,
        double cvsgRequestRate,
        double paidCfrRequestRate,
        double ifpCfrRequestRate,
        double solicitorGeneralSignalRate,
        double amicusIntensity,
        double lowerCourtSplitDepth,
        double genuineLowerCourtSplitRate,
        double lowerCourtIdeologicalDrift,
        double lowerCourtResistanceRisk,
        double splitMaturity,
        double relistRate,
        double specialistCounselRate,
        double barCapital,
        double claimStrength,
        double vehicleQuality,
        double vehicleDefectRisk,
        double forumShoppingPressure,
        double preReviewSettlementPressure,
        double settledBeforeReviewRate,
        double strategicPlaintiffSelection,
        double repeatPlayerAdvantage,
        double governmentNoncomplianceRisk,
        double governmentNoncomplianceRate,
        double enforcementCapacity,
        double emergencyOpportunism,
        double recusalIncentivePressure,
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
        double constitutionalRemandRate,
        double publicInterestFilteredRate,
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
        double individualOneShotClaimantRate,
        double organizedRightsClaimantRate,
        double businessRepeatPlayerClaimantRate,
        double governmentClaimantRate,
        double expertBarClinicClaimantRate,
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
        double precedentDurability,
        double emergencyDownstreamEffect,
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
                precedentDurability,
                lowerCourtCompliance,
                enforcementCapacity,
                MetricDefinition.lowerIsBetter(lowerCourtResistanceRisk),
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
                MetricDefinition.lowerIsBetter(emergencyDownstreamEffect),
                MetricDefinition.lowerIsBetter(governmentNoncomplianceRate),
                MetricDefinition.lowerIsBetter(recusalIncentivePressure),
                MetricDefinition.lowerIsBetter(forumShoppingPressure),
                MetricDefinition.lowerIsBetter(emergencyOpportunism),
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
                practicalOpenNoncomplianceRate,
                governmentNoncomplianceRate,
                emergencyDownstreamEffect,
                lowerCourtResistanceRisk,
                forumShoppingPressure,
                emergencyOpportunism
        );
    }

    public double directionalScore() {
        return Values.average(
                stabilityRightsScore(),
                legitimacyControlScore(),
                rightsClaimantSuccess,
                precedentDurability,
                lowerCourtCompliance,
                eliteAcceptance,
                MetricDefinition.lowerIsBetter(administrativeCost)
        );
    }

    public double repeatPlayerLearning() {
        return Values.average(repeatPlayerAdvantage, strategicPlaintiffSelection, forumShoppingPressure);
    }

    public double emergencyIncentiveLearning() {
        return Values.average(emergencyOpportunism, executiveEmergencyStrategy, emergencyDownstreamEffect);
    }

    public double complianceLearning() {
        return Values.average(lowerCourtCompliance, enforcementCapacity, interbranchCompliance);
    }

    public double paidCertPetitionShare() {
        return ratio(paidPetitionRate, paidPetitionRate + ifpPetitionRate);
    }

    public double ifpCertPetitionShare() {
        return ratio(ifpPetitionRate, paidPetitionRate + ifpPetitionRate);
    }

    public double emergencyGrantConditionalRate() {
        return ratio(emergencyGrantRate, emergencyOrderRate);
    }

    public double emergencyGrantPerEmergencyStayDocket() {
        return ratio(emergencyGrantRate, emergencyStayDocketRate);
    }

    public double meritsAccelerationPerEmergencyStayDocket() {
        return ratio(meritsAccelerationRate, emergencyStayDocketRate);
    }

    private static double ratio(double numerator, double denominator) {
        if (denominator <= 0.0) {
            return 0.0;
        }
        return numerator / denominator;
    }
}
