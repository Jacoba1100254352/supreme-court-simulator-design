package constitutionalreview.simulation;

import constitutionalreview.institution.CourtDecision;
import constitutionalreview.institution.OverrideOutcome;
import constitutionalreview.model.DocketType;

public final class MetricsAccumulator {
    private int totalCases;
    private int meritsReviews;
    private int invalidations;
    private int emergencyOrders;
    private int shadowRelief;
    private int reasonedEmergencyOrders;
    private int temporaryStays;
    private int meritsAccelerations;
    private int expiredEmergencyOrders;
    private int enBanc;
    private int crossDisagreements;
    private int councilWarnings;
    private int overrideAttempts;
    private int overrides;
    private int rightsCarveoutBlocks;
    private int repeatedOverrides;
    private int reversals;
    private int justiceReplacements;
    private int recusedJustices;
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
    private double legalStability;
    private double precedentStability;
    private double statutoryStability;
    private double interbranchCompliance;
    private double rightsProtection;
    private double partisanAlignment;
    private double shadowDocketAbuse;
    private double legitimacy;
    private double constitutionalConflict;
    private double democraticResponsiveness;
    private double administrativeCost;
    private double legislativeDefiance;
    private double executiveEmergencyStrategy;
    private double appointmentManipulationPressure;
    private double overrideAdaptation;

    public void add(CourtDecision decision) {
        totalCases++;
        meritsReviews += decision.meritsReview() ? 1 : 0;
        invalidations += decision.invalidated() ? 1 : 0;
        emergencyOrders += decision.emergencyOrder() ? 1 : 0;
        shadowRelief += decision.shadowRelief() ? 1 : 0;
        reasonedEmergencyOrders += decision.reasonedEmergencyOrder() ? 1 : 0;
        temporaryStays += decision.temporaryStay() ? 1 : 0;
        meritsAccelerations += decision.meritsAccelerated() ? 1 : 0;
        expiredEmergencyOrders += decision.expiredEmergencyOrder() ? 1 : 0;
        enBanc += decision.enBanc() ? 1 : 0;
        crossDisagreements += decision.crossCheckDisagreement() ? 1 : 0;
        councilWarnings += decision.councilWarning() ? 1 : 0;
        overrideAttempts += decision.overrideAttempted() ? 1 : 0;
        overrides += decision.legislativeOverride() ? 1 : 0;
        rightsCarveoutBlocks += decision.overrideOutcome() == OverrideOutcome.RIGHTS_CARVEOUT_BLOCKED ? 1 : 0;
        repeatedOverrides += decision.overrideOutcome() == OverrideOutcome.REPEATED_OVERRIDE ? 1 : 0;
        reversals += decision.precedentReversal() ? 1 : 0;
        justiceReplacements += decision.justiceReplacements();
        recusedJustices += decision.recusedJustices();
        participatingJustices += decision.participatingJustices();
        concurrences += decision.concurrences();
        dissents += decision.dissents();
        addDocketType(decision.docketType());
        legalStability += decision.legalStability();
        precedentStability += decision.precedentStability();
        statutoryStability += decision.statutoryStability();
        interbranchCompliance += decision.interbranchCompliance();
        rightsProtection += decision.rightsProtection();
        partisanAlignment += decision.partisanAlignment();
        shadowDocketAbuse += decision.shadowDocketAbuse();
        legitimacy += decision.legitimacy();
        constitutionalConflict += decision.constitutionalConflict();
        democraticResponsiveness += decision.democraticResponsiveness();
        administrativeCost += decision.administrativeCost();
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
                meritsReviews / cases,
                invalidations / cases,
                legalStability / cases,
                precedentStability / cases,
                statutoryStability / cases,
                interbranchCompliance / cases,
                rightsProtection / cases,
                partisanAlignment / cases,
                shadowDocketAbuse / cases,
                legitimacy / cases,
                reversals / cases,
                constitutionalConflict / cases,
                democraticResponsiveness / cases,
                independenceAccountabilityBalance(),
                administrativeCost / cases,
                emergencyOrders / cases,
                shadowRelief / cases,
                reasonedEmergencyOrders / cases,
                temporaryStays / cases,
                meritsAccelerations / cases,
                expiredEmergencyOrders / cases,
                recusedJustices / justicesInCases,
                justiceReplacements / cases,
                concurrences / Math.max(1.0, participatingJustices),
                dissents / Math.max(1.0, participatingJustices),
                1.0 - (enBanc / cases),
                enBanc / cases,
                crossDisagreements / cases,
                councilWarnings / cases,
                overrideAttempts / cases,
                overrides / cases,
                rightsCarveoutBlocks / cases,
                repeatedOverrides / cases,
                legislativeDefiance / cases,
                executiveEmergencyStrategy / cases,
                appointmentManipulationPressure / cases,
                overrideAdaptation / cases,
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

    private double independenceAccountabilityBalance() {
        double cases = Math.max(1.0, totalCases);
        double avgRights = rightsProtection / cases;
        double avgResponsive = democraticResponsiveness / cases;
        double lowPartisan = MetricDefinition.lowerIsBetter(partisanAlignment / cases);
        double lowShadow = MetricDefinition.lowerIsBetter(shadowDocketAbuse / cases);
        return (avgRights + avgResponsive + lowPartisan + lowShadow) / 4.0;
    }
}
