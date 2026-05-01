package constitutionalreview.institution;

import constitutionalreview.model.CaseWorld;
import constitutionalreview.model.CourtState;
import constitutionalreview.model.DocketType;
import constitutionalreview.model.Justice;
import constitutionalreview.model.ReviewCase;
import constitutionalreview.util.Values;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Random;

public final class ConstitutionalReviewProcess implements ReviewProcess {
    private final CourtDesign design;
    private final List<Justice> candidatePool;
    private final List<Justice> court;
    private int reviewedCases;

    public ConstitutionalReviewProcess(CourtDesign design, CaseWorld world, Random random) {
        this.design = design;
        this.candidatePool = new ArrayList<>(world.justicePool());
        this.court = selectCourt(design, world.justicePool(), random);
    }

    public CourtDesign design() {
        return design;
    }

    @Override
    public CourtDecision review(ReviewCase reviewCase, CourtState state, Random random) {
        reviewedCases++;
        StrategicActorPolicy.StrategicResponse strategicResponse = StrategicActorPolicy.choose(reviewCase, state, design, random);
        double effectiveEmergencyPressure = Values.clamp01(
                reviewCase.emergencyPressure()
                        + strategicResponse.emergencyPressureDelta()
                        + state.executiveEmergencyStrategy() * 0.20
                        + state.conflictLoad() * 0.04
        );
        boolean emergency = random.nextDouble() < effectiveEmergencyPressure;
        boolean initialMeritsReview = meritsReview(reviewCase, emergency, random);
        boolean enBanc = enBanc(reviewCase, emergency, random);
        List<Justice> participating = participatingJustices(reviewCase, enBanc, random);
        int recused = Math.max(0, Math.min(court.size(), court.size() - participating.size()));

        VoteCount voteCount = vote(reviewCase, state, participating, emergency, random);
        EmergencyProcedure emergencyProcedure = emergencyProcedure(reviewCase, emergency, initialMeritsReview, voteCount, participating.size(), random);
        boolean meritsReview = initialMeritsReview || emergencyProcedure.meritsAccelerated();
        int requiredVotes = requiredVotes(participating.size(), reviewCase);
        boolean invalidated = meritsReview && voteCount.yes() >= requiredVotes;
        boolean shadowRelief = emergencyProcedure.stage() == EmergencyProcedureStage.SHADOW_STAY;

        boolean councilWarning = design.auxiliaryReview() == AuxiliaryReview.CONSTITUTIONAL_COUNCIL
                && legalConcern(reviewCase) > 0.54;
        boolean crossDisagreement = crossCheckDisagreement(reviewCase, invalidated, random);
        if (crossDisagreement && design.auxiliaryReview() == AuxiliaryReview.CROSS_CHECKING_COURT) {
            invalidated = false;
        }
        if (design.auxiliaryReview() == AuxiliaryReview.DUAL_SUPREME_COURTS && crossDisagreement) {
            invalidated = reviewCase.rightsBurden() > 0.68 || voteCount.yes() >= requiredVotes + 1;
        }

        OverrideDecision overrideDecision = legislativeOverride(reviewCase, invalidated, state, strategicResponse, random);
        boolean override = overrideDecision.successful();
        double precedentShift = precedentShift(reviewCase, invalidated, shadowRelief, crossDisagreement);
        boolean precedentReversal = invalidated && (precedentShift > 0.48 || reviewCase.legalAmbiguity() > 0.74);
        int concurrences = concurrences(voteCount, participating.size(), random);
        int dissents = Math.max(0, voteCount.no() - (participating.size() - voteCount.yes() > 0 ? 1 : 0));

        double rightsProtection = rightsProtection(reviewCase, invalidated, shadowRelief, overrideDecision);
        double partisanAlignment = partisanAlignment(reviewCase, voteCount, participating);
        double shadowAbuse = shadowDocketAbuse(reviewCase, emergency, meritsReview, emergencyProcedure);
        double conflict = constitutionalConflict(reviewCase, invalidated, shadowRelief, crossDisagreement, overrideDecision, state);
        double precedentStability = precedentStability(state, precedentShift, shadowAbuse, conflict);
        double statutoryStability = statutoryStability(reviewCase, invalidated, shadowRelief, emergencyProcedure, overrideDecision, conflict);
        double interbranchCompliance = interbranchCompliance(reviewCase, crossDisagreement, councilWarning, overrideDecision, conflict, state);
        double legalStability = Values.average(precedentStability, statutoryStability, interbranchCompliance);
        double legitimacy = legitimacy(reviewCase, meritsReview, emergencyProcedure, recused, participating.size(), shadowAbuse, partisanAlignment, councilWarning);
        double responsiveness = democraticResponsiveness(reviewCase, invalidated, overrideDecision, councilWarning);
        double administrativeCost = administrativeCost(reviewCase, emergencyProcedure, enBanc, crossDisagreement, councilWarning);

        boolean emergencyDenied = emergency
                && reviewCase.requestedEmergencyRelief() > 0.42
                && !shadowRelief
                && !emergencyProcedure.temporaryStay()
                && !emergencyProcedure.meritsAccelerated();
        state.applyDecision(
                precedentShift,
                conflict,
                invalidated,
                emergencyDenied,
                shadowRelief,
                overrideDecision.attempted(),
                overrideDecision.successful(),
                overrideDecision.outcome() == OverrideOutcome.RIGHTS_CARVEOUT_BLOCKED,
                reviewCase.publicAttention(),
                reviewCase.democraticMandate(),
                reviewCase.rightsBurden(),
                reviewCase.partisanSalience(),
                reviewCase.executiveDefianceRisk(),
                strategicResponse.legislativeCompliance(),
                strategicResponse.legislativeEvasion(),
                strategicResponse.delayedReenactment(),
                strategicResponse.executiveEmergencyFlood(),
                strategicResponse.overrideCampaign(),
                strategicResponse.appointmentPressureCampaign()
        );
        int replacements = updateCourtAfterCase(reviewCase, state, random);
        return new CourtDecision(
                reviewCase.id(),
                reviewCase.type(),
                reviewCase.docketType(),
                meritsReview,
                invalidated,
                emergency,
                shadowRelief,
                emergencyProcedure.stage(),
                emergencyProcedure.reasonedOrder(),
                emergencyProcedure.temporaryStay(),
                emergencyProcedure.meritsAccelerated(),
                emergencyProcedure.expired(),
                enBanc,
                councilWarning,
                crossDisagreement,
                override,
                overrideDecision.attempted(),
                overrideDecision.outcome(),
                precedentReversal,
                replacements,
                participating.size(),
                recused,
                voteCount.yes(),
                voteCount.no(),
                concurrences,
                dissents,
                legalStability,
                precedentStability,
                statutoryStability,
                interbranchCompliance,
                rightsProtection,
                partisanAlignment,
                shadowAbuse,
                legitimacy,
                responsiveness,
                conflict,
                precedentShift,
                administrativeCost,
                state.legislativeDefiance(),
                state.executiveEmergencyStrategy(),
                state.appointmentManipulationPressure(),
                state.overrideAdaptation(),
                strategicResponse.legislativeCompliance(),
                strategicResponse.legislativeEvasion(),
                strategicResponse.delayedReenactment(),
                strategicResponse.executiveEmergencyFlood(),
                strategicResponse.overrideCampaign(),
                strategicResponse.appointmentPressureCampaign()
        );
    }

    private static List<Justice> selectCourt(CourtDesign design, List<Justice> pool, Random random) {
        List<Justice> candidates = new ArrayList<>(pool);
        switch (design.appointmentMethod()) {
            case NONPARTISAN_COMMISSION -> candidates.sort(Comparator
                    .comparingDouble((Justice justice) -> -justice.independence())
                    .thenComparingDouble(justice -> Math.abs(justice.ideology())));
            case LEGISLATIVE_SUPERMAJORITY -> candidates.sort(Comparator
                    .comparingDouble((Justice justice) -> Math.abs(justice.ideology()))
                    .thenComparingDouble(justice -> -justice.institutionalism()));
            case LOTTERY_FROM_APPELLATE_POOL, ROTATING_PANEL -> shuffle(candidates, random);
            case PRESIDENT_SENATE -> candidates.sort(Comparator
                    .comparingDouble((Justice justice) -> -Math.abs(justice.ideology()))
                    .thenComparingDouble(justice -> -justice.partisanLoyalty()));
        }
        List<Justice> court = new ArrayList<>();
        for (Justice candidate : candidates) {
            court.add(adjustForInstitution(candidate, design));
            if (court.size() == design.courtSize()) {
                break;
            }
        }
        return court;
    }

    private static Justice adjustForInstitution(Justice justice, CourtDesign design) {
        double independence = justice.independence();
        double accountability = justice.accountabilityPressure();
        double loyalty = justice.partisanLoyalty();
        if (design.termLimitPolicy() == TermLimitPolicy.LIFE_TENURE) {
            independence += 0.08;
            accountability -= 0.06;
        } else if (design.termLimitPolicy() == TermLimitPolicy.RETENTION_ELECTION) {
            accountability += 0.18;
            loyalty += 0.06;
        } else {
            independence += 0.04;
            accountability += 0.04;
        }
        if (design.removalStandard() == RemovalStandard.ETHICS_TRIBUNAL) {
            independence += 0.04;
            accountability += 0.08;
        } else if (design.removalStandard() == RemovalStandard.RETENTION_RECALL) {
            accountability += 0.18;
            independence -= 0.08;
        }
        return new Justice(
                justice.id(),
                justice.ideology(),
                Values.clamp01(independence * design.independenceWeight()),
                justice.rightsSensitivity(),
                Values.clamp01(accountability * design.accountabilityWeight()),
                justice.institutionalism(),
                Values.clamp01(loyalty),
                justice.emergencyDeference()
        );
    }

    private boolean meritsReview(ReviewCase reviewCase, boolean emergency, Random random) {
        if (!emergency) {
            return true;
        }
        if (reviewCase.docketType() == DocketType.EMERGENCY_STAY_APPLICATION) {
            return false;
        }
        return switch (design.emergencyDocketRule()) {
            case OPEN_EMERGENCY -> random.nextDouble() > 0.35;
            case REASONED_FAST_TRACK -> random.nextDouble() > 0.18;
            case SUPERMAJORITY_STAY -> random.nextDouble() > 0.10;
            case NO_RELIEF_WITHOUT_MERITS -> true;
        };
    }

    private boolean enBanc(ReviewCase reviewCase, boolean emergency, Random random) {
        if (design.reviewMode() == ReviewMode.FULL_COURT || design.reviewMode() == ReviewMode.DUAL_COURTS) {
            return true;
        }
        double probability = 0.12 + reviewCase.rightsBurden() * 0.20 + reviewCase.partisanSalience() * 0.18;
        if (emergency) {
            probability += 0.08;
        }
        return random.nextDouble() < Values.clamp01(probability);
    }

    private List<Justice> participatingJustices(ReviewCase reviewCase, boolean enBanc, Random random) {
        List<Justice> ordered = new ArrayList<>(court);
        if (!enBanc && design.reviewMode() != ReviewMode.FULL_COURT) {
            shuffle(ordered, random);
            int panelSize = Math.min(court.size(), design.reviewMode() == ReviewMode.SPECIALIZED_PANELS ? 5 : 3);
            ordered = new ArrayList<>(ordered.subList(0, panelSize));
        }
        List<Justice> participating = new ArrayList<>();
        for (Justice justice : ordered) {
            if (!shouldRecuse(justice, reviewCase, random)) {
                participating.add(justice);
            }
        }
        int minimum = Math.min(3, ordered.size());
        if (participating.size() < minimum) {
            for (Justice justice : ordered) {
                if (!participating.contains(justice)) {
                    participating.add(justice);
                }
                if (participating.size() == minimum) {
                    break;
                }
            }
        }
        return participating;
    }

    private boolean shouldRecuse(Justice justice, ReviewCase reviewCase, Random random) {
        double conflict = reviewCase.partisanSalience() * justice.partisanLoyalty() * (1.0 - justice.independence());
        double probability = switch (design.recusalRule()) {
            case SELF_POLICED -> conflict * 0.10;
            case PUBLIC_EXPLANATION -> conflict * 0.22;
            case PEER_PANEL -> conflict * 0.38;
            case AUTOMATIC_CONFLICT_SCREEN -> conflict * 0.55;
        };
        return random.nextDouble() < Values.clamp01(probability);
    }

    private VoteCount vote(
            ReviewCase reviewCase,
            CourtState state,
            List<Justice> justices,
            boolean emergency,
            Random random
    ) {
        int yes = 0;
        for (Justice justice : justices) {
            double legalConcern = legalConcern(reviewCase);
            double deference = reviewCase.democraticMandate() * 0.32
                    + reviewCase.legislativeQuality() * 0.18
                    + justice.institutionalism() * 0.12;
            double rightsConcern = reviewCase.rightsBurden() * justice.rightsSensitivity() * 0.44;
            double partisanPull = reviewCase.partisanSalience()
                    * (-reviewCase.lawIdeology() * justice.ideology())
                    * justice.partisanLoyalty()
                    * (1.0 - justice.independence())
                    * 0.30;
            double emergencyDeference = emergency ? justice.emergencyDeference() * 0.18 : 0.0;
            double stabilityPenalty = state.precedentStability() * 0.08;
            double accountabilityPull = justice.accountabilityPressure() * reviewCase.democraticMandate() * 0.09;
            double score = legalConcern * 0.42
                    + rightsConcern
                    + partisanPull
                    - deference
                    - emergencyDeference
                    - stabilityPenalty
                    - accountabilityPull
                    + random.nextGaussian() * 0.07;
            if (score > 0.04) {
                yes++;
            }
        }
        return new VoteCount(yes, justices.size() - yes);
    }

    private int requiredVotes(int participating, ReviewCase reviewCase) {
        double share = design.votingThreshold().requiredShare(reviewCase.rightsBurden() > 0.68);
        if (design.emergencyDocketRule() == EmergencyDocketRule.SUPERMAJORITY_STAY && reviewCase.emergencyPressure() > 0.62) {
            share = Math.max(share, 0.60);
        }
        return Math.max(1, (int) Math.ceil(participating * share - 0.000_001));
    }

    private EmergencyProcedure emergencyProcedure(
            ReviewCase reviewCase,
            boolean emergency,
            boolean initialMeritsReview,
            VoteCount voteCount,
            int participating,
            Random random
    ) {
        if (!emergency) {
            return new EmergencyProcedure(EmergencyProcedureStage.NONE, false, false, false, false);
        }

        int majority = Math.max(1, participating / 2 + 1);
        int supermajority = Math.max(1, (int) Math.ceil(participating * 0.60 - 0.000_001));
        boolean emergencyVotes = voteCount.yes() >= majority && reviewCase.requestedEmergencyRelief() > 0.42;
        boolean supermajorityVotes = voteCount.yes() >= supermajority && reviewCase.requestedEmergencyRelief() > 0.42;

        return switch (design.emergencyDocketRule()) {
            case OPEN_EMERGENCY -> {
                if (emergencyVotes && !initialMeritsReview) {
                    yield new EmergencyProcedure(EmergencyProcedureStage.SHADOW_STAY, false, true, false, false);
                }
                if (random.nextDouble() < 0.22) {
                    yield new EmergencyProcedure(EmergencyProcedureStage.RESPONSE_WINDOW, false, false, false, false);
                }
                yield new EmergencyProcedure(EmergencyProcedureStage.APPLICATION_ONLY, false, false, false, false);
            }
            case REASONED_FAST_TRACK -> {
                if (supermajorityVotes && random.nextDouble() < 0.58) {
                    yield new EmergencyProcedure(EmergencyProcedureStage.REASONED_TEMPORARY_STAY, true, true, false, false);
                }
                if (random.nextDouble() < 0.62 || reviewCase.rightsBurden() > 0.58) {
                    yield new EmergencyProcedure(EmergencyProcedureStage.MERITS_ACCELERATED, true, false, true, false);
                }
                yield new EmergencyProcedure(EmergencyProcedureStage.RESPONSE_WINDOW, true, false, false, false);
            }
            case SUPERMAJORITY_STAY -> {
                if (supermajorityVotes) {
                    yield new EmergencyProcedure(EmergencyProcedureStage.REASONED_TEMPORARY_STAY, true, true, false, false);
                }
                if (random.nextDouble() < 0.45) {
                    yield new EmergencyProcedure(EmergencyProcedureStage.MERITS_ACCELERATED, true, false, true, false);
                }
                yield new EmergencyProcedure(EmergencyProcedureStage.EXPIRED_WITHOUT_RELIEF, true, false, false, true);
            }
            case NO_RELIEF_WITHOUT_MERITS -> new EmergencyProcedure(EmergencyProcedureStage.MERITS_ACCELERATED, true, false, true, false);
        };
    }

    private boolean crossCheckDisagreement(ReviewCase reviewCase, boolean invalidated, Random random) {
        if (design.auxiliaryReview() == AuxiliaryReview.NONE || design.auxiliaryReview() == AuxiliaryReview.CONSTITUTIONAL_COUNCIL) {
            return false;
        }
        double probability = 0.06
                + reviewCase.legalAmbiguity() * 0.16
                + reviewCase.partisanSalience() * 0.12
                + reviewCase.lowerCourtConflict() * 0.08;
        if (invalidated && reviewCase.democraticMandate() > 0.64) {
            probability += 0.12;
        }
        return random.nextDouble() < Values.clamp01(probability);
    }

    private OverrideDecision legislativeOverride(
            ReviewCase reviewCase,
            boolean invalidated,
            CourtState state,
            StrategicActorPolicy.StrategicResponse strategicResponse,
            Random random
    ) {
        if (!invalidated || design.overrideRule() == OverrideRule.NONE) {
            return new OverrideDecision(false, false, OverrideOutcome.NONE);
        }
        double base = reviewCase.overridePressure() * 0.34
                + strategicResponse.overridePressureDelta()
                + reviewCase.democraticMandate() * 0.30
                + reviewCase.publicAttention() * 0.18
                + state.conflictLoad() * 0.12
                + state.legislativeDefiance() * 0.12
                + state.overrideAdaptation() * 0.10
                - reviewCase.rightsBurden() * 0.24
                + (strategicResponse.legislativeCompliance() ? -0.05 : 0.0);
        boolean attempted = random.nextDouble() < Values.clamp01(base + 0.18);
        if (!attempted) {
            return new OverrideDecision(false, false, OverrideOutcome.NONE);
        }
        if (reviewCase.rightsBurden() > 0.72 && design.overrideRule() != OverrideRule.POPULAR_REFERENDUM) {
            return new OverrideDecision(true, false, OverrideOutcome.RIGHTS_CARVEOUT_BLOCKED);
        }
        double probability = switch (design.overrideRule()) {
            case NONE -> 0.0;
            case LEGISLATIVE_SUPERMAJORITY -> base - 0.12;
            case DELAYED_REENACTMENT -> base + 0.02;
            case POPULAR_REFERENDUM -> base + reviewCase.publicAttention() * 0.12 - reviewCase.partisanSalience() * 0.08;
        };
        if (random.nextDouble() >= Values.clamp01(probability)) {
            return new OverrideDecision(true, false, OverrideOutcome.FAILED);
        }
        OverrideOutcome outcome = switch (design.overrideRule()) {
            case NONE -> OverrideOutcome.NONE;
            case LEGISLATIVE_SUPERMAJORITY -> OverrideOutcome.ORDINARY_SUPERMAJORITY;
            case DELAYED_REENACTMENT -> OverrideOutcome.DELAYED_REENACTMENT;
            case POPULAR_REFERENDUM -> OverrideOutcome.REFERENDUM_APPROVAL;
        };
        if (state.conflictLoad() > 0.52 && reviewCase.overridePressure() > 0.58 && random.nextDouble() < 0.35) {
            outcome = OverrideOutcome.REPEATED_OVERRIDE;
        }
        return new OverrideDecision(true, outcome != OverrideOutcome.NONE, outcome);
    }

    private int concurrences(VoteCount voteCount, int participating, Random random) {
        double base = switch (design.opinionCoalitionRule()) {
            case FREE_CONCURRENCE -> 0.34;
            case MAJORITY_OPINION_DISCIPLINE -> 0.12;
            case CONSENSUS_PANEL -> 0.08;
            case FRAGMENTATION_TOLERANT -> 0.46;
        };
        int majority = Math.max(voteCount.yes(), voteCount.no());
        int concurrences = 0;
        for (int i = 0; i < majority; i++) {
            if (random.nextDouble() < base) {
                concurrences++;
            }
        }
        return Math.min(participating, concurrences);
    }

    private double legalConcern(ReviewCase reviewCase) {
        double concern = reviewCase.rightsBurden() * 0.40
                + reviewCase.constitutionalConflictPotential() * 0.28
                + (1.0 - reviewCase.legislativeQuality()) * 0.20
                + reviewCase.legalAmbiguity() * 0.12
                + reviewCase.lowerCourtErrorRisk() * 0.10;
        if (design.auxiliaryReview() == AuxiliaryReview.CONSTITUTIONAL_COUNCIL) {
            concern *= 0.92;
        }
        return Values.clamp01(concern);
    }

    private double rightsProtection(ReviewCase reviewCase, boolean invalidated, boolean shadowRelief, OverrideDecision overrideDecision) {
        double protection = reviewCase.rightsBurden() > 0.55
                ? (invalidated || shadowRelief ? 0.82 : 0.30)
                : (invalidated ? 0.55 : 0.70);
        if (overrideDecision.successful() && reviewCase.rightsBurden() > 0.55) {
            protection -= 0.22;
        }
        if (overrideDecision.outcome() == OverrideOutcome.RIGHTS_CARVEOUT_BLOCKED) {
            protection += 0.08;
        }
        return Values.clamp01(protection + reviewCase.legislativeQuality() * 0.08);
    }

    private double partisanAlignment(ReviewCase reviewCase, VoteCount voteCount, List<Justice> justices) {
        if (justices.isEmpty()) {
            return 0.0;
        }
        double averageIdeology = 0.0;
        for (Justice justice : justices) {
            averageIdeology += justice.ideology();
        }
        averageIdeology /= justices.size();
        double voteDirection = voteCount.yes() >= voteCount.no() ? -reviewCase.lawIdeology() : reviewCase.lawIdeology();
        return Values.clamp01(Math.abs(averageIdeology * voteDirection) * reviewCase.partisanSalience());
    }

    private double shadowDocketAbuse(ReviewCase reviewCase, boolean emergency, boolean meritsReview, EmergencyProcedure emergencyProcedure) {
        if (!emergency) {
            return 0.0;
        }
        double rulePenalty = switch (design.emergencyDocketRule()) {
            case OPEN_EMERGENCY -> 0.32;
            case REASONED_FAST_TRACK -> 0.14;
            case SUPERMAJORITY_STAY -> 0.08;
            case NO_RELIEF_WITHOUT_MERITS -> 0.02;
        };
        double abuse = rulePenalty
                + (!meritsReview ? 0.22 : 0.0)
                + (emergencyProcedure.stage() == EmergencyProcedureStage.SHADOW_STAY ? 0.24 : 0.0)
                - (emergencyProcedure.reasonedOrder() ? 0.08 : 0.0)
                - (emergencyProcedure.meritsAccelerated() ? 0.07 : 0.0);
        abuse += reviewCase.partisanSalience() * 0.12 + reviewCase.legalAmbiguity() * 0.08;
        return Values.clamp01(abuse);
    }

    private double constitutionalConflict(
            ReviewCase reviewCase,
            boolean invalidated,
            boolean shadowRelief,
            boolean crossDisagreement,
            OverrideDecision overrideDecision,
            CourtState state
    ) {
        double conflict = reviewCase.constitutionalConflictPotential() * 0.38
                + reviewCase.executiveDefianceRisk() * 0.18
                + reviewCase.lowerCourtConflict() * 0.08
                + state.conflictLoad() * 0.12
                + state.legislativeDefiance() * 0.10
                + state.executiveEmergencyStrategy() * 0.08;
        if (invalidated) {
            conflict += reviewCase.democraticMandate() * 0.14;
        }
        if (shadowRelief) {
            conflict += 0.12;
        }
        if (crossDisagreement) {
            conflict += 0.16;
        }
        if (overrideDecision.attempted()) {
            conflict += 0.06;
        }
        if (overrideDecision.successful()) {
            conflict += reviewCase.rightsBurden() * 0.15;
        }
        if (overrideDecision.outcome() == OverrideOutcome.REPEATED_OVERRIDE) {
            conflict += 0.12;
        } else if (overrideDecision.outcome() == OverrideOutcome.RIGHTS_CARVEOUT_BLOCKED) {
            conflict += 0.08;
        }
        return Values.clamp01(conflict);
    }

    private double precedentStability(CourtState state, double precedentShift, double shadowAbuse, double conflict) {
        return Values.clamp01(state.precedentStability() - precedentShift * 0.28 - shadowAbuse * 0.18 - conflict * 0.12 + 0.12);
    }

    private double statutoryStability(
            ReviewCase reviewCase,
            boolean invalidated,
            boolean shadowRelief,
            EmergencyProcedure emergencyProcedure,
            OverrideDecision overrideDecision,
            double conflict
    ) {
        double stability = 0.68
                + reviewCase.legislativeQuality() * 0.18
                + reviewCase.democraticMandate() * 0.08
                - reviewCase.legalAmbiguity() * 0.08
                - conflict * 0.12;
        if (invalidated) {
            stability -= 0.18 + reviewCase.publicAttention() * 0.06;
        }
        if (shadowRelief) {
            stability -= 0.10;
        }
        if (emergencyProcedure.expired()) {
            stability -= 0.05;
        }
        if (overrideDecision.successful()) {
            stability += 0.08;
        }
        if (overrideDecision.outcome() == OverrideOutcome.REPEATED_OVERRIDE) {
            stability -= 0.12;
        } else if (overrideDecision.outcome() == OverrideOutcome.RIGHTS_CARVEOUT_BLOCKED) {
            stability -= 0.05;
        }
        return Values.clamp01(stability);
    }

    private double interbranchCompliance(
            ReviewCase reviewCase,
            boolean crossDisagreement,
            boolean councilWarning,
            OverrideDecision overrideDecision,
            double conflict,
            CourtState state
    ) {
        double compliance = 0.76
                + reviewCase.legislativeQuality() * 0.08
                + reviewCase.democraticMandate() * 0.04
                - reviewCase.executiveDefianceRisk() * 0.18
                - reviewCase.partisanSalience() * 0.10
                - reviewCase.lowerCourtConflict() * 0.05
                - conflict * 0.26
                - state.conflictLoad() * 0.10;
        if (crossDisagreement) {
            compliance -= 0.08;
        }
        if (overrideDecision.attempted()) {
            compliance -= 0.04;
        }
        if (overrideDecision.successful()) {
            compliance += 0.05;
        }
        if (overrideDecision.outcome() == OverrideOutcome.REPEATED_OVERRIDE) {
            compliance -= 0.10;
        }
        if (councilWarning) {
            compliance += 0.04;
        }
        return Values.clamp01(compliance);
    }

    private double legitimacy(
            ReviewCase reviewCase,
            boolean meritsReview,
            EmergencyProcedure emergencyProcedure,
            int recused,
            int participating,
            double shadowAbuse,
            double partisanAlignment,
            boolean councilWarning
    ) {
        double reasonGiving = meritsReview ? 0.18 : -0.12;
        double recusalDiscipline = participating == 0 ? 0.0 : Math.min(0.16, recused * 0.04);
        double councilBoost = councilWarning ? 0.06 : 0.0;
        double emergencyProcessBoost = (emergencyProcedure.reasonedOrder() ? 0.04 : 0.0)
                + (emergencyProcedure.meritsAccelerated() ? 0.04 : 0.0)
                - (emergencyProcedure.stage() == EmergencyProcedureStage.SHADOW_STAY ? 0.08 : 0.0);
        return Values.clamp01(
                0.48
                        + reviewCase.publicAttention() * 0.16
                        + reviewCase.legislativeQuality() * 0.10
                        + reasonGiving
                        + recusalDiscipline
                        + councilBoost
                        + emergencyProcessBoost
                        - shadowAbuse * 0.24
                        - partisanAlignment * 0.20
        );
    }

    private double democraticResponsiveness(ReviewCase reviewCase, boolean invalidated, OverrideDecision overrideDecision, boolean councilWarning) {
        double respect = invalidated ? 1.0 - reviewCase.democraticMandate() * 0.42 : 0.58 + reviewCase.democraticMandate() * 0.26;
        if (overrideDecision.successful()) {
            respect += 0.18;
        } else if (overrideDecision.attempted()) {
            respect += 0.04;
        }
        if (reviewCase.rightsBurden() > 0.65 && !invalidated) {
            respect -= 0.12;
        }
        if (overrideDecision.outcome() == OverrideOutcome.RIGHTS_CARVEOUT_BLOCKED && reviewCase.rightsBurden() > 0.65) {
            respect -= 0.05;
        }
        if (councilWarning) {
            respect += 0.04;
        }
        return Values.clamp01(respect);
    }

    private double precedentShift(ReviewCase reviewCase, boolean invalidated, boolean shadowRelief, boolean crossDisagreement) {
        double shift = invalidated ? 0.18 + reviewCase.legalAmbiguity() * 0.18 + reviewCase.rightsBurden() * 0.10 : 0.04;
        if (shadowRelief) {
            shift += 0.12;
        }
        if (crossDisagreement) {
            shift += 0.08;
        }
        return Values.clamp01(shift);
    }

    private double administrativeCost(ReviewCase reviewCase, EmergencyProcedure emergencyProcedure, boolean enBanc, boolean crossDisagreement, boolean councilWarning) {
        double cost = design.administrativeCost() + reviewCase.legalAmbiguity() * 0.10;
        if (emergencyProcedure.stage() != EmergencyProcedureStage.NONE) {
            cost += 0.05;
        }
        if (emergencyProcedure.stage() == EmergencyProcedureStage.RESPONSE_WINDOW) {
            cost += 0.03;
        } else if (emergencyProcedure.reasonedOrder() || emergencyProcedure.meritsAccelerated()) {
            cost += 0.06;
        }
        if (enBanc) {
            cost += 0.04;
        }
        if (crossDisagreement) {
            cost += 0.10;
        }
        if (councilWarning) {
            cost += 0.08;
        }
        return Values.clamp01(cost);
    }

    private int updateCourtAfterCase(ReviewCase reviewCase, CourtState state, Random random) {
        double probability = replacementProbability(reviewCase, state);
        if (random.nextDouble() >= probability) {
            return 0;
        }
        int replacements = design.appointmentMethod() == AppointmentMethod.ROTATING_PANEL ? 2 : 1;
        if (design.termLimitPolicy() == TermLimitPolicy.RETENTION_ELECTION
                && state.conflictLoad() > 0.48
                && random.nextDouble() < 0.30) {
            replacements++;
        }
        replacements = Math.min(replacements, Math.max(1, court.size() / 3));
        for (int i = 0; i < replacements; i++) {
            replaceOneJustice(random);
        }
        return replacements;
    }

    private double replacementProbability(ReviewCase reviewCase, CourtState state) {
        double scheduled = switch (design.termLimitPolicy()) {
            case LIFE_TENURE -> 0.025;
            case EIGHTEEN_YEAR_STAGGERED -> 0.095;
            case TWELVE_YEAR_NONRENEWABLE -> 0.135;
            case RETENTION_ELECTION -> 0.075 + state.conflictLoad() * 0.065;
        };
        if (design.reviewMode() == ReviewMode.PANEL_EN_BANC || design.reviewMode() == ReviewMode.SPECIALIZED_PANELS) {
            scheduled += 0.025;
        }
        if (design.appointmentMethod() == AppointmentMethod.ROTATING_PANEL) {
            scheduled += 0.055;
        }
        if (reviewedCases % 18 == 0 && design.termLimitPolicy() != TermLimitPolicy.LIFE_TENURE) {
            scheduled += 0.18;
        }
        if (reviewCase.publicAttention() > 0.72 && design.removalStandard() == RemovalStandard.RETENTION_RECALL) {
            scheduled += 0.05;
        }
        scheduled += state.appointmentManipulationPressure() * 0.06;
        return Values.clamp01(scheduled);
    }

    private void replaceOneJustice(Random random) {
        Justice outgoing = outgoingJustice(random);
        court.remove(outgoing);
        Justice replacement = replacementJustice(random);
        court.add(replacement);
    }

    private Justice outgoingJustice(Random random) {
        return switch (design.termLimitPolicy()) {
            case LIFE_TENURE -> court.get(random.nextInt(court.size()));
            case EIGHTEEN_YEAR_STAGGERED, TWELVE_YEAR_NONRENEWABLE -> court.get(reviewedCases % court.size());
            case RETENTION_ELECTION -> court.stream()
                    .max(Comparator.comparingDouble(Justice::partisanLoyalty))
                    .orElseGet(() -> court.get(random.nextInt(court.size())));
        };
    }

    private Justice replacementJustice(Random random) {
        List<Justice> candidates = candidatePool.stream()
                .filter(candidate -> court.stream().noneMatch(active -> active.id() == candidate.id()))
                .toList();
        if (candidates.isEmpty()) {
            candidates = candidatePool;
        }
        Justice selected = switch (design.appointmentMethod()) {
            case NONPARTISAN_COMMISSION -> candidates.stream()
                    .min(Comparator.comparingDouble((Justice justice) -> Math.abs(justice.ideology()))
                            .thenComparingDouble(justice -> -justice.independence()))
                    .orElse(candidates.get(random.nextInt(candidates.size())));
            case LEGISLATIVE_SUPERMAJORITY -> candidates.stream()
                    .min(Comparator.comparingDouble((Justice justice) -> Math.abs(justice.ideology()))
                            .thenComparingDouble(justice -> -justice.institutionalism()))
                    .orElse(candidates.get(random.nextInt(candidates.size())));
            case LOTTERY_FROM_APPELLATE_POOL, ROTATING_PANEL -> candidates.get(random.nextInt(candidates.size()));
            case PRESIDENT_SENATE -> partisanAppointment(candidates, random);
        };
        return adjustForInstitution(selected, design);
    }

    private Justice partisanAppointment(List<Justice> candidates, Random random) {
        double appointingSide = ((reviewedCases / 16) % 2 == 0) ? 1.0 : -1.0;
        return candidates.stream()
                .max(Comparator.comparingDouble((Justice justice) -> appointingSide * justice.ideology() + justice.partisanLoyalty() * 0.25)
                        .thenComparingDouble(Justice::independence))
                .orElse(candidates.get(random.nextInt(candidates.size())));
    }

    private static void shuffle(List<Justice> values, Random random) {
        for (int i = values.size() - 1; i > 0; i--) {
            int index = random.nextInt(i + 1);
            Justice temp = values.get(i);
            values.set(i, values.get(index));
            values.set(index, temp);
        }
    }

    private record VoteCount(int yes, int no) {
    }

    private record EmergencyProcedure(
            EmergencyProcedureStage stage,
            boolean reasonedOrder,
            boolean temporaryStay,
            boolean meritsAccelerated,
            boolean expired
    ) {
    }

    private record OverrideDecision(boolean attempted, boolean successful, OverrideOutcome outcome) {
    }
}
