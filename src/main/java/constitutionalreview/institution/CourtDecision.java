package constitutionalreview.institution;

import constitutionalreview.model.CaseType;

public record CourtDecision(
        String caseId,
        CaseType caseType,
        boolean meritsReview,
        boolean invalidated,
        boolean emergencyOrder,
        boolean shadowRelief,
        boolean enBanc,
        boolean councilWarning,
        boolean crossCheckDisagreement,
        boolean legislativeOverride,
        boolean precedentReversal,
        int participatingJustices,
        int recusedJustices,
        int votesForInvalidation,
        int votesAgainstInvalidation,
        int concurrences,
        int dissents,
        double legalStability,
        double rightsProtection,
        double partisanAlignment,
        double shadowDocketAbuse,
        double legitimacy,
        double democraticResponsiveness,
        double constitutionalConflict,
        double precedentShift,
        double administrativeCost
) {
}
