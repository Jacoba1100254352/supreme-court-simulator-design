package constitutionalreview.institution;

public record CourtDesign(
        String name,
        AppointmentMethod appointmentMethod,
        int courtSize,
        TermLimitPolicy termLimitPolicy,
        RemovalStandard removalStandard,
        RecusalRule recusalRule,
        EmergencyDocketRule emergencyDocketRule,
        VotingThreshold votingThreshold,
        OpinionCoalitionRule opinionCoalitionRule,
        ReviewMode reviewMode,
        AuxiliaryReview auxiliaryReview,
        OverrideRule overrideRule,
        double independenceWeight,
        double accountabilityWeight,
        double administrativeCost
) {
    public CourtDesign {
        if (courtSize < 3) {
            throw new IllegalArgumentException("courtSize must be at least 3");
        }
        if (courtSize % 2 == 0) {
            throw new IllegalArgumentException("courtSize must be odd to avoid unresolved tie behavior");
        }
    }
}
