package constitutionalreview.simulation;

import constitutionalreview.institution.CourtDecision;
import constitutionalreview.institution.FormalLegalResponse;
import constitutionalreview.institution.OverrideOutcome;
import constitutionalreview.institution.PracticalImplementationResponse;
import constitutionalreview.model.CaseType;
import constitutionalreview.model.DocketType;

public final class MetricsAccumulator {
    private int totalCases;
    private int petitionFiled;
    private int admitted;
    private int screenOuts;
    private int meritsTransfers;
    private int certiorariPaths;
    private int certiorariAdmissions;
    private int paidPetitions;
    private int ifpPetitions;
    private int meritsReviews;
    private int invalidations;
    private int emergencyOrders;
    private int emergencyGrants;
    private int shadowRelief;
    private int reasonedEmergencyOrders;
    private int temporaryStays;
    private int meritsAccelerations;
    private int expiredEmergencyOrders;
    private int enBanc;
    private int crossDisagreements;
    private int councilWarnings;
    private int constitutionalRemands;
    private int publicInterestFiltered;
    private int overrideAttempts;
    private int overrides;
    private int rightsCarveoutBlocks;
    private int repeatedOverrides;
    private int legislativeCompliance;
    private int legislativeEvasion;
    private int delayedReenactmentStrategies;
    private int executiveEmergencyFloods;
    private int overrideCampaigns;
    private int appointmentPressureCampaigns;
    private int reversals;
    private int justiceReplacements;
    private int recusedJustices;
    private int quorumFailures;
    private int participatingJustices;
    private int concurrences;
    private int dissents;
    private int facialChallenges;
    private int asAppliedChallenges;
    private int electionDisputes;
    private int emergencyStayDockets;
    private int executivePowerDisputes;
    private int administrativeLawChallenges;
    private int rightsClaims;
    private int formalRepeals;
    private int formalReplacements;
    private int formalNarrowedReenactments;
    private int formalWeakOverrides;
    private int formalAmendments;
    private int formalCourtCurbing;
    private int formalOpenDefiance;
    private int practicalDelays;
    private int practicalAdministrativeSubstitution;
    private int practicalSymbolicCompliance;
    private int practicalBureaucraticResistance;
    private int practicalOpenNoncompliance;
    private int governmentNoncompliance;
    private int rightsClaimantCases;
    private int rightsDomainClaimantCases;
    private int structuralDomainClaimantCases;
    private int electionDomainClaimantCases;
    private int executivePowerDomainClaimantCases;
    private int administrativeDomainClaimantCases;
    private int economicDomainClaimantCases;
    private double admissionScore;
    private double conditionalReversalProbability;
    private double solicitorGeneralSignal;
    private double amicusBriefs;
    private double lowerCourtSplitDepth;
    private double splitMaturity;
    private double relistCount;
    private double specialistCounsel;
    private double vehicleDefectRisk;
    private double strategicPlaintiffSelection;
    private double repeatPlayerAdvantage;
    private double governmentNoncomplianceRisk;
    private double recusalIncentivePressure;
    private double legalStability;
    private double precedentStability;
    private double statutoryStability;
    private double interbranchCompliance;
    private double rightsProtection;
    private double partisanAlignment;
    private double shadowDocketAbuse;
    private double emergencyLegitimacyRisk;
    private double legitimacy;
    private double constitutionalConflict;
    private double democraticResponsiveness;
    private double administrativeCost;
    private double rightsClaimantSuccess;
    private double rightsDomainClaimantSuccess;
    private double structuralDomainClaimantSuccess;
    private double electionDomainClaimantSuccess;
    private double executivePowerDomainClaimantSuccess;
    private double administrativeDomainClaimantSuccess;
    private double economicDomainClaimantSuccess;
    private double doctrinalDepth;
    private double remedialBreadth;
    private double precedentDurability;
    private double emergencyDownstreamEffect;
    private double fragmentationIndex;
    private double lowerCourtCompliance;
    private double eliteAcceptance;
    private double publicConfidence;
    private double legislativeDefiance;
    private double executiveEmergencyStrategy;
    private double appointmentManipulationPressure;
    private double overrideAdaptation;

    public void add(CourtDecision decision) {
        totalCases++;
        petitionFiled += decision.petitionFiled() ? 1 : 0;
        admitted += decision.admitted() ? 1 : 0;
        screenOuts += decision.screenedOut() ? 1 : 0;
        meritsTransfers += decision.transferredToMerits() ? 1 : 0;
        certiorariPaths += decision.certiorariPath() ? 1 : 0;
        certiorariAdmissions += decision.certiorariPath() && decision.admitted() ? 1 : 0;
        paidPetitions += decision.paidPetition() ? 1 : 0;
        ifpPetitions += decision.ifpPetition() ? 1 : 0;
        meritsReviews += decision.meritsReview() ? 1 : 0;
        invalidations += decision.invalidated() ? 1 : 0;
        emergencyOrders += decision.emergencyOrder() ? 1 : 0;
        emergencyGrants += decision.emergencyOrderDetail().granted() ? 1 : 0;
        shadowRelief += decision.shadowRelief() ? 1 : 0;
        reasonedEmergencyOrders += decision.reasonedEmergencyOrder() ? 1 : 0;
        temporaryStays += decision.temporaryStay() ? 1 : 0;
        meritsAccelerations += decision.meritsAccelerated() ? 1 : 0;
        expiredEmergencyOrders += decision.expiredEmergencyOrder() ? 1 : 0;
        enBanc += decision.enBanc() ? 1 : 0;
        crossDisagreements += decision.crossCheckDisagreement() ? 1 : 0;
        councilWarnings += decision.councilWarning() ? 1 : 0;
        constitutionalRemands += decision.constitutionalRemand() ? 1 : 0;
        publicInterestFiltered += decision.publicInterestFiltered() ? 1 : 0;
        overrideAttempts += decision.overrideAttempted() ? 1 : 0;
        overrides += decision.legislativeOverride() ? 1 : 0;
        rightsCarveoutBlocks += decision.overrideOutcome() == OverrideOutcome.RIGHTS_CARVEOUT_BLOCKED ? 1 : 0;
        repeatedOverrides += decision.overrideOutcome() == OverrideOutcome.REPEATED_OVERRIDE ? 1 : 0;
        legislativeCompliance += decision.legislativeCompliance() ? 1 : 0;
        legislativeEvasion += decision.legislativeEvasion() ? 1 : 0;
        delayedReenactmentStrategies += decision.delayedReenactment() ? 1 : 0;
        executiveEmergencyFloods += decision.executiveEmergencyFlood() ? 1 : 0;
        overrideCampaigns += decision.overrideCampaign() ? 1 : 0;
        appointmentPressureCampaigns += decision.appointmentPressureCampaign() ? 1 : 0;
        reversals += decision.precedentReversal() ? 1 : 0;
        justiceReplacements += decision.justiceReplacements();
        recusedJustices += decision.recusedJustices();
        quorumFailures += decision.quorumFailure() ? 1 : 0;
        participatingJustices += decision.participatingJustices();
        concurrences += decision.concurrences();
        dissents += decision.dissents();
        addDocketType(decision.docketType());
        addFormalResponse(decision.formalLegalResponse());
        addPracticalResponse(decision.practicalImplementationResponse());
        governmentNoncompliance += decision.governmentNoncompliance() ? 1 : 0;
        addDomainClaimantSuccess(decision);
        admissionScore += decision.admissionScore();
        conditionalReversalProbability += decision.conditionalReversalProbability();
        solicitorGeneralSignal += decision.solicitorGeneralSignal();
        amicusBriefs += decision.amicusBriefs();
        lowerCourtSplitDepth += decision.lowerCourtSplitDepth();
        splitMaturity += decision.splitMaturity();
        relistCount += decision.relistCount();
        specialistCounsel += decision.specialistCounsel() ? 1.0 : 0.0;
        vehicleDefectRisk += decision.vehicleDefectRisk();
        strategicPlaintiffSelection += decision.strategicPlaintiffSelection();
        repeatPlayerAdvantage += decision.repeatPlayerAdvantage();
        governmentNoncomplianceRisk += decision.governmentNoncomplianceRisk();
        recusalIncentivePressure += decision.recusalIncentivePressure();
        legalStability += decision.legalStability();
        precedentStability += decision.precedentStability();
        statutoryStability += decision.statutoryStability();
        interbranchCompliance += decision.interbranchCompliance();
        rightsProtection += decision.rightsProtection();
        partisanAlignment += decision.partisanAlignment();
        shadowDocketAbuse += decision.shadowDocketAbuse();
        emergencyLegitimacyRisk += decision.emergencyLegitimacyRisk();
        legitimacy += decision.legitimacy();
        constitutionalConflict += decision.constitutionalConflict();
        democraticResponsiveness += decision.democraticResponsiveness();
        administrativeCost += decision.administrativeCost();
        rightsClaimantSuccess += decision.rightsClaimantSuccess();
        doctrinalDepth += decision.doctrinalDepth();
        remedialBreadth += decision.remedialBreadth();
        precedentDurability += decision.precedentDurability();
        emergencyDownstreamEffect += decision.emergencyDownstreamEffect();
        fragmentationIndex += decision.fragmentationIndex();
        lowerCourtCompliance += decision.lowerCourtCompliance();
        eliteAcceptance += decision.eliteAcceptance();
        publicConfidence += decision.publicConfidence();
        legislativeDefiance += decision.legislativeDefiance();
        executiveEmergencyStrategy += decision.executiveEmergencyStrategy();
        appointmentManipulationPressure += decision.appointmentManipulationPressure();
        overrideAdaptation += decision.overrideAdaptation();
    }

    public ScenarioReport toReport(String scenarioKey, String scenarioName) {
        double cases = Math.max(1.0, totalCases);
        double justicesInCases = Math.max(1.0, recusedJustices + participatingJustices);
        return new ScenarioReport(
                scenarioKey,
                scenarioName,
                totalCases,
                petitionFiled / cases,
                admitted / cases,
                screenOuts / cases,
                meritsTransfers / cases,
                certiorariPaths / cases,
                certiorariAdmissions / Math.max(1.0, certiorariPaths),
                paidPetitions / cases,
                ifpPetitions / cases,
                solicitorGeneralSignal / cases,
                amicusBriefs / cases,
                lowerCourtSplitDepth / cases,
                splitMaturity / cases,
                relistCount / cases,
                specialistCounsel / cases,
                vehicleDefectRisk / cases,
                strategicPlaintiffSelection / cases,
                repeatPlayerAdvantage / cases,
                governmentNoncomplianceRisk / cases,
                governmentNoncompliance / cases,
                recusalIncentivePressure / cases,
                conditionalReversalProbability / cases,
                meritsReviews / cases,
                invalidations / cases,
                legalStability / cases,
                precedentStability / cases,
                statutoryStability / cases,
                interbranchCompliance / cases,
                rightsProtection / cases,
                partisanAlignment / cases,
                shadowDocketAbuse / cases,
                emergencyLegitimacyRisk / cases,
                legitimacy / cases,
                reversals / cases,
                constitutionalConflict / cases,
                democraticResponsiveness / cases,
                independenceAccountabilityBalance(),
                administrativeCost / cases,
                emergencyOrders / cases,
                emergencyGrants / cases,
                shadowRelief / cases,
                reasonedEmergencyOrders / cases,
                temporaryStays / cases,
                meritsAccelerations / cases,
                expiredEmergencyOrders / cases,
                recusedJustices / justicesInCases,
                quorumFailures / cases,
                justiceReplacements / cases,
                concurrences / Math.max(1.0, participatingJustices),
                dissents / Math.max(1.0, participatingJustices),
                fragmentationIndex / cases,
                1.0 - (enBanc / cases),
                enBanc / cases,
                crossDisagreements / cases,
                councilWarnings / cases,
                constitutionalRemands / cases,
                publicInterestFiltered / cases,
                overrideAttempts / cases,
                overrides / cases,
                rightsCarveoutBlocks / cases,
                repeatedOverrides / cases,
                legislativeDefiance / cases,
                executiveEmergencyStrategy / cases,
                appointmentManipulationPressure / cases,
                overrideAdaptation / cases,
                legislativeCompliance / cases,
                legislativeEvasion / cases,
                delayedReenactmentStrategies / cases,
                executiveEmergencyFloods / cases,
                overrideCampaigns / cases,
                appointmentPressureCampaigns / cases,
                formalRepeals / cases,
                formalReplacements / cases,
                formalNarrowedReenactments / cases,
                formalWeakOverrides / cases,
                formalAmendments / cases,
                formalCourtCurbing / cases,
                formalOpenDefiance / cases,
                practicalDelays / cases,
                practicalAdministrativeSubstitution / cases,
                practicalSymbolicCompliance / cases,
                practicalBureaucraticResistance / cases,
                practicalOpenNoncompliance / cases,
                rightsClaimantCases / cases,
                rightsClaimantSuccess / cases,
                rightsDomainClaimantSuccess / Math.max(1.0, rightsDomainClaimantCases),
                structuralDomainClaimantSuccess / Math.max(1.0, structuralDomainClaimantCases),
                electionDomainClaimantSuccess / Math.max(1.0, electionDomainClaimantCases),
                executivePowerDomainClaimantSuccess / Math.max(1.0, executivePowerDomainClaimantCases),
                administrativeDomainClaimantSuccess / Math.max(1.0, administrativeDomainClaimantCases),
                economicDomainClaimantSuccess / Math.max(1.0, economicDomainClaimantCases),
                doctrinalDepth / cases,
                remedialBreadth / cases,
                precedentDurability / cases,
                emergencyDownstreamEffect / cases,
                lowerCourtCompliance / cases,
                eliteAcceptance / cases,
                publicConfidence / cases,
                facialChallenges / cases,
                asAppliedChallenges / cases,
                electionDisputes / cases,
                emergencyStayDockets / cases,
                executivePowerDisputes / cases,
                administrativeLawChallenges / cases,
                rightsClaims / cases
        );
    }

    private void addDocketType(DocketType docketType) {
        switch (docketType) {
            case FACIAL_CHALLENGE -> facialChallenges++;
            case AS_APPLIED_CHALLENGE -> asAppliedChallenges++;
            case ELECTION_DISPUTE -> electionDisputes++;
            case EMERGENCY_STAY_APPLICATION -> emergencyStayDockets++;
            case EXECUTIVE_POWER_DISPUTE -> executivePowerDisputes++;
            case ADMINISTRATIVE_LAW_CHALLENGE -> administrativeLawChallenges++;
            case RIGHTS_CLAIM -> rightsClaims++;
        }
    }

    private void addFormalResponse(FormalLegalResponse response) {
        switch (response) {
            case REPEAL -> formalRepeals++;
            case REPLACEMENT_STATUTE -> formalReplacements++;
            case NARROWED_REENACTMENT -> formalNarrowedReenactments++;
            case WEAK_FORM_OVERRIDE -> formalWeakOverrides++;
            case CONSTITUTIONAL_AMENDMENT -> formalAmendments++;
            case COURT_CURBING -> formalCourtCurbing++;
            case OPEN_DEFIANCE -> formalOpenDefiance++;
            case NONE, ACQUIESCENT_COMPLIANCE -> {
            }
        }
    }

    private void addPracticalResponse(PracticalImplementationResponse response) {
        switch (response) {
            case IMPLEMENTATION_DELAY -> practicalDelays++;
            case ADMINISTRATIVE_SUBSTITUTION -> practicalAdministrativeSubstitution++;
            case SYMBOLIC_COMPLIANCE -> practicalSymbolicCompliance++;
            case BUREAUCRATIC_RESISTANCE -> practicalBureaucraticResistance++;
            case OPEN_NONCOMPLIANCE -> practicalOpenNoncompliance++;
            case NONE, PROMPT_IMPLEMENTATION -> {
            }
        }
    }

    private void addDomainClaimantSuccess(CourtDecision decision) {
        if (!decision.rightsClaimantCase()) {
            return;
        }
        rightsClaimantCases++;
        switch (decision.caseType()) {
            case RIGHTS -> {
                rightsDomainClaimantCases++;
                rightsDomainClaimantSuccess += decision.rightsClaimantSuccess();
            }
            case STRUCTURAL -> {
                structuralDomainClaimantCases++;
                structuralDomainClaimantSuccess += decision.rightsClaimantSuccess();
            }
            case ELECTIONS -> {
                electionDomainClaimantCases++;
                electionDomainClaimantSuccess += decision.rightsClaimantSuccess();
            }
            case EXECUTIVE_POWER -> {
                executivePowerDomainClaimantCases++;
                executivePowerDomainClaimantSuccess += decision.rightsClaimantSuccess();
            }
            case ADMINISTRATIVE_STATE -> {
                administrativeDomainClaimantCases++;
                administrativeDomainClaimantSuccess += decision.rightsClaimantSuccess();
            }
            case ECONOMIC_REGULATION -> {
                economicDomainClaimantCases++;
                economicDomainClaimantSuccess += decision.rightsClaimantSuccess();
            }
        }
    }

    private double independenceAccountabilityBalance() {
        double cases = Math.max(1.0, totalCases);
        double avgRights = rightsProtection / cases;
        double avgResponsive = democraticResponsiveness / cases;
        double avgEliteAcceptance = eliteAcceptance / cases;
        double avgPublicConfidence = publicConfidence / cases;
        double lowPartisan = MetricDefinition.lowerIsBetter(partisanAlignment / cases);
        double lowShadow = MetricDefinition.lowerIsBetter(shadowDocketAbuse / cases);
        double lowEmergencyRisk = MetricDefinition.lowerIsBetter(emergencyLegitimacyRisk / cases);
        double lowGovernmentNoncompliance = MetricDefinition.lowerIsBetter(governmentNoncompliance / cases);
        double lowEmergencyDownstream = MetricDefinition.lowerIsBetter(emergencyDownstreamEffect / cases);
        return (avgRights + avgResponsive + avgEliteAcceptance + avgPublicConfidence + lowPartisan + lowShadow + lowEmergencyRisk + lowGovernmentNoncompliance + lowEmergencyDownstream) / 9.0;
    }
}
