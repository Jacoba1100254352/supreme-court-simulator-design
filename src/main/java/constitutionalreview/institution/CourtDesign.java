package constitutionalreview.institution;

public record CourtDesign(
        String name,
        AppointmentMethod appointmentMethod,
        JudicialSelectorPool judicialSelectorPool,
        JudicialNomineePool judicialNomineePool,
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
        double administrativeCost,
        int appointmentFragmentation,
        double confirmationThreshold,
        double vacancyDeadlockRisk,
        boolean renewableTerms,
        Integer retirementAge,
        SizeChangeDifficulty sizeChangeDifficulty,
        RecusalConsequenceType recusalConsequenceType,
        double quorumFailureRisk,
        RemedyVotingThresholds remedyVotingThresholds
) {
    public CourtDesign(
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
        this(
                name,
                appointmentMethod,
                defaultSelectorPool(appointmentMethod),
                defaultNomineePool(appointmentMethod),
                courtSize,
                termLimitPolicy,
                removalStandard,
                recusalRule,
                emergencyDocketRule,
                votingThreshold,
                opinionCoalitionRule,
                reviewMode,
                auxiliaryReview,
                overrideRule,
                independenceWeight,
                accountabilityWeight,
                administrativeCost
        );
    }

    public CourtDesign(
            String name,
            AppointmentMethod appointmentMethod,
            JudicialSelectorPool judicialSelectorPool,
            JudicialNomineePool judicialNomineePool,
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
        this(
                name,
                appointmentMethod,
                judicialSelectorPool,
                judicialNomineePool,
                courtSize,
                termLimitPolicy,
                removalStandard,
                recusalRule,
                emergencyDocketRule,
                votingThreshold,
                opinionCoalitionRule,
                reviewMode,
                auxiliaryReview,
                overrideRule,
                independenceWeight,
                accountabilityWeight,
                administrativeCost,
                defaultAppointmentFragmentation(appointmentMethod),
                defaultConfirmationThreshold(appointmentMethod),
                defaultVacancyDeadlockRisk(appointmentMethod),
                termLimitPolicy == TermLimitPolicy.RETENTION_ELECTION,
                defaultRetirementAge(termLimitPolicy),
                defaultSizeChangeDifficulty(appointmentMethod),
                defaultRecusalConsequence(recusalRule),
                defaultQuorumFailureRisk(recusalRule),
                RemedyVotingThresholds.from(votingThreshold)
        );
    }

    public CourtDesign(
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
            double administrativeCost,
            int appointmentFragmentation,
            double confirmationThreshold,
            double vacancyDeadlockRisk,
            boolean renewableTerms,
            Integer retirementAge,
            SizeChangeDifficulty sizeChangeDifficulty,
            RecusalConsequenceType recusalConsequenceType,
            double quorumFailureRisk,
            RemedyVotingThresholds remedyVotingThresholds
    ) {
        this(
                name,
                appointmentMethod,
                defaultSelectorPool(appointmentMethod),
                defaultNomineePool(appointmentMethod),
                courtSize,
                termLimitPolicy,
                removalStandard,
                recusalRule,
                emergencyDocketRule,
                votingThreshold,
                opinionCoalitionRule,
                reviewMode,
                auxiliaryReview,
                overrideRule,
                independenceWeight,
                accountabilityWeight,
                administrativeCost,
                appointmentFragmentation,
                confirmationThreshold,
                vacancyDeadlockRisk,
                renewableTerms,
                retirementAge,
                sizeChangeDifficulty,
                recusalConsequenceType,
                quorumFailureRisk,
                remedyVotingThresholds
        );
    }

    public CourtDesign {
        if (judicialSelectorPool == null) {
            judicialSelectorPool = defaultSelectorPool(appointmentMethod);
        }
        if (judicialNomineePool == null) {
            judicialNomineePool = defaultNomineePool(appointmentMethod);
        }
        if (appointmentMethod != AppointmentMethod.JUDICIAL_ELECTORATE) {
            judicialSelectorPool = JudicialSelectorPool.NOT_APPLICABLE;
            judicialNomineePool = JudicialNomineePool.NOT_APPLICABLE;
        }
        if (courtSize < 3) {
            throw new IllegalArgumentException("courtSize must be at least 3");
        }
        appointmentFragmentation = Math.max(1, appointmentFragmentation);
        confirmationThreshold = Math.max(0.0, Math.min(1.0, confirmationThreshold));
        vacancyDeadlockRisk = Math.max(0.0, Math.min(1.0, vacancyDeadlockRisk));
        quorumFailureRisk = Math.max(0.0, Math.min(1.0, quorumFailureRisk));
        if (retirementAge != null && retirementAge < 45) {
            throw new IllegalArgumentException("retirementAge must be realistic when present");
        }
        if (remedyVotingThresholds == null) {
            remedyVotingThresholds = RemedyVotingThresholds.from(votingThreshold);
        }
        if (sizeChangeDifficulty == null) {
            sizeChangeDifficulty = SizeChangeDifficulty.ORDINARY_STATUTE;
        }
        if (recusalConsequenceType == null) {
            recusalConsequenceType = RecusalConsequenceType.REDUCED_PANEL;
        }
    }

    private static int defaultAppointmentFragmentation(AppointmentMethod appointmentMethod) {
        return switch (appointmentMethod) {
            case PRESIDENT_SENATE -> 2;
            case LEGISLATIVE_SUPERMAJORITY -> 3;
            case NONPARTISAN_COMMISSION -> 3;
            case JUDICIAL_ELECTORATE -> 5;
            case LOTTERY_FROM_APPELLATE_POOL, ROTATING_PANEL -> 4;
        };
    }

    private static double defaultConfirmationThreshold(AppointmentMethod appointmentMethod) {
        return switch (appointmentMethod) {
            case LEGISLATIVE_SUPERMAJORITY -> 0.67;
            case NONPARTISAN_COMMISSION -> 0.60;
            case JUDICIAL_ELECTORATE -> 0.52;
            case PRESIDENT_SENATE -> 0.50;
            case LOTTERY_FROM_APPELLATE_POOL, ROTATING_PANEL -> 0.55;
        };
    }

    private static double defaultVacancyDeadlockRisk(AppointmentMethod appointmentMethod) {
        return switch (appointmentMethod) {
            case LEGISLATIVE_SUPERMAJORITY -> 0.28;
            case NONPARTISAN_COMMISSION -> 0.12;
            case JUDICIAL_ELECTORATE -> 0.07;
            case PRESIDENT_SENATE -> 0.18;
            case LOTTERY_FROM_APPELLATE_POOL, ROTATING_PANEL -> 0.05;
        };
    }

    private static Integer defaultRetirementAge(TermLimitPolicy termLimitPolicy) {
        return switch (termLimitPolicy) {
            case LIFE_TENURE -> null;
            case EIGHTEEN_YEAR_STAGGERED -> 75;
            case TWELVE_YEAR_NONRENEWABLE -> 70;
            case RETENTION_ELECTION -> 70;
        };
    }

    private static SizeChangeDifficulty defaultSizeChangeDifficulty(AppointmentMethod appointmentMethod) {
        return appointmentMethod == AppointmentMethod.LEGISLATIVE_SUPERMAJORITY
                ? SizeChangeDifficulty.SUPERMAJORITY_STATUTE
                : SizeChangeDifficulty.ORDINARY_STATUTE;
    }

    private static RecusalConsequenceType defaultRecusalConsequence(RecusalRule recusalRule) {
        return switch (recusalRule) {
            case SELF_POLICED -> RecusalConsequenceType.REDUCED_PANEL;
            case PUBLIC_EXPLANATION -> RecusalConsequenceType.REARGUMENT;
            case PEER_PANEL -> RecusalConsequenceType.SUBSTITUTE_JUSTICE;
            case AUTOMATIC_CONFLICT_SCREEN -> RecusalConsequenceType.SUBSTITUTE_JUSTICE;
        };
    }

    private static double defaultQuorumFailureRisk(RecusalRule recusalRule) {
        return switch (recusalRule) {
            case SELF_POLICED -> 0.006;
            case PUBLIC_EXPLANATION -> 0.004;
            case PEER_PANEL -> 0.003;
            case AUTOMATIC_CONFLICT_SCREEN -> 0.002;
        };
    }

    private static JudicialSelectorPool defaultSelectorPool(AppointmentMethod appointmentMethod) {
        return appointmentMethod == AppointmentMethod.JUDICIAL_ELECTORATE
                ? JudicialSelectorPool.FEDERAL_AND_STATE_HIGH_COURT_JUDGES
                : JudicialSelectorPool.NOT_APPLICABLE;
    }

    private static JudicialNomineePool defaultNomineePool(AppointmentMethod appointmentMethod) {
        return appointmentMethod == AppointmentMethod.JUDICIAL_ELECTORATE
                ? JudicialNomineePool.FEDERAL_AND_STATE_HIGH_COURT_JUDGES
                : JudicialNomineePool.NOT_APPLICABLE;
    }

    public boolean usesJudicialElectorate() {
        return appointmentMethod == AppointmentMethod.JUDICIAL_ELECTORATE;
    }

    public double judicialElectorateInsulation() {
        if (!usesJudicialElectorate()) {
            return 0.0;
        }
        return (judicialSelectorPool.professionalInsulation() + judicialNomineePool.professionalFilter()) / 2.0;
    }

    public double judicialElectorateBreadth() {
        if (!usesJudicialElectorate()) {
            return 0.0;
        }
        return (judicialSelectorPool.jurisdictionalBreadth() + judicialNomineePool.candidateBreadth()) / 2.0;
    }

    public double judicialElectorateCaptureRisk() {
        if (!usesJudicialElectorate()) {
            return 0.0;
        }
        return (judicialSelectorPool.captureRisk() + judicialNomineePool.pipelineIdeologyRisk()) / 2.0;
    }

    public double judicialElectorateAdministrativeCost() {
        if (!usesJudicialElectorate()) {
            return 0.0;
        }
        return judicialSelectorPool.administrativeCost() + judicialNomineePool.administrativeCost();
    }
}
