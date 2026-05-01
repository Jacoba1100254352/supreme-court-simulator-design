package constitutionalreview.simulation;

import constitutionalreview.institution.CourtDecision;

public final class MetricsAccumulator {
    private int totalCases;
    private int meritsReviews;
    private int invalidations;
    private int emergencyOrders;
    private int shadowRelief;
    private int enBanc;
    private int crossDisagreements;
    private int councilWarnings;
    private int overrides;
    private int reversals;
    private int recusedJustices;
    private int participatingJustices;
    private int concurrences;
    private int dissents;
    private double legalStability;
    private double rightsProtection;
    private double partisanAlignment;
    private double shadowDocketAbuse;
    private double legitimacy;
    private double constitutionalConflict;
    private double democraticResponsiveness;
    private double administrativeCost;

    public void add(CourtDecision decision) {
        totalCases++;
        meritsReviews += decision.meritsReview() ? 1 : 0;
        invalidations += decision.invalidated() ? 1 : 0;
        emergencyOrders += decision.emergencyOrder() ? 1 : 0;
        shadowRelief += decision.shadowRelief() ? 1 : 0;
        enBanc += decision.enBanc() ? 1 : 0;
        crossDisagreements += decision.crossCheckDisagreement() ? 1 : 0;
        councilWarnings += decision.councilWarning() ? 1 : 0;
        overrides += decision.legislativeOverride() ? 1 : 0;
        reversals += decision.precedentReversal() ? 1 : 0;
        recusedJustices += decision.recusedJustices();
        participatingJustices += decision.participatingJustices();
        concurrences += decision.concurrences();
        dissents += decision.dissents();
        legalStability += decision.legalStability();
        rightsProtection += decision.rightsProtection();
        partisanAlignment += decision.partisanAlignment();
        shadowDocketAbuse += decision.shadowDocketAbuse();
        legitimacy += decision.legitimacy();
        constitutionalConflict += decision.constitutionalConflict();
        democraticResponsiveness += decision.democraticResponsiveness();
        administrativeCost += decision.administrativeCost();
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
                recusedJustices / justicesInCases,
                concurrences / Math.max(1.0, participatingJustices),
                dissents / Math.max(1.0, participatingJustices),
                1.0 - (enBanc / cases),
                enBanc / cases,
                crossDisagreements / cases,
                councilWarnings / cases,
                overrides / cases
        );
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
