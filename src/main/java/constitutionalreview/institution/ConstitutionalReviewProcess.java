package constitutionalreview.institution;

import constitutionalreview.model.CaseWorld;
import constitutionalreview.model.CourtState;
import constitutionalreview.model.Justice;
import constitutionalreview.model.ReviewCase;
import constitutionalreview.util.Values;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Random;

public final class ConstitutionalReviewProcess implements ReviewProcess {
    private final CourtDesign design;
    private final List<Justice> court;

    public ConstitutionalReviewProcess(CourtDesign design, CaseWorld world, Random random) {
        this.design = design;
        this.court = selectCourt(design, world.justicePool(), random);
    }

    public CourtDesign design() {
        return design;
    }

    @Override
    public CourtDecision review(ReviewCase reviewCase, CourtState state, Random random) {
        boolean emergency = random.nextDouble() < reviewCase.emergencyPressure();
        boolean meritsReview = meritsReview(reviewCase, emergency, random);
        boolean enBanc = enBanc(reviewCase, emergency, random);
        List<Justice> participating = participatingJustices(reviewCase, enBanc, random);
        int recused = Math.max(0, Math.min(court.size(), court.size() - participating.size()));

        VoteCount voteCount = vote(reviewCase, state, participating, emergency, random);
        int requiredVotes = requiredVotes(participating.size(), reviewCase);
        boolean invalidated = meritsReview && voteCount.yes() >= requiredVotes;
        boolean shadowRelief = emergency && !meritsReview && emergencyShadowRelief(reviewCase, voteCount, participating.size());

        boolean councilWarning = design.auxiliaryReview() == AuxiliaryReview.CONSTITUTIONAL_COUNCIL
                && legalConcern(reviewCase) > 0.54;
        boolean crossDisagreement = crossCheckDisagreement(reviewCase, invalidated, random);
        if (crossDisagreement && design.auxiliaryReview() == AuxiliaryReview.CROSS_CHECKING_COURT) {
            invalidated = false;
        }
        if (design.auxiliaryReview() == AuxiliaryReview.DUAL_SUPREME_COURTS && crossDisagreement) {
            invalidated = reviewCase.rightsBurden() > 0.68 || voteCount.yes() >= requiredVotes + 1;
        }

        boolean override = legislativeOverride(reviewCase, invalidated, random);
        double precedentShift = precedentShift(reviewCase, invalidated, shadowRelief, crossDisagreement);
        boolean precedentReversal = invalidated && (precedentShift > 0.48 || reviewCase.legalAmbiguity() > 0.74);
        int concurrences = concurrences(voteCount, participating.size(), random);
        int dissents = Math.max(0, voteCount.no() - (participating.size() - voteCount.yes() > 0 ? 1 : 0));

        double rightsProtection = rightsProtection(reviewCase, invalidated, shadowRelief, override);
        double partisanAlignment = partisanAlignment(reviewCase, voteCount, participating);
        double shadowAbuse = shadowDocketAbuse(reviewCase, emergency, meritsReview, shadowRelief);
        double conflict = constitutionalConflict(reviewCase, invalidated, shadowRelief, crossDisagreement, override, state);
        double stability = legalStability(state, precedentShift, shadowAbuse, conflict);
        double legitimacy = legitimacy(reviewCase, meritsReview, recused, participating.size(), shadowAbuse, partisanAlignment, councilWarning);
        double responsiveness = democraticResponsiveness(reviewCase, invalidated, override, councilWarning);
        double administrativeCost = administrativeCost(reviewCase, emergency, enBanc, crossDisagreement, councilWarning);

        state.applyDecision(precedentShift, conflict);
        return new CourtDecision(
                reviewCase.id(),
                reviewCase.type(),
                meritsReview,
                invalidated,
                emergency,
                shadowRelief,
                enBanc,
                councilWarning,
                crossDisagreement,
                override,
                precedentReversal,
                participating.size(),
                recused,
                voteCount.yes(),
                voteCount.no(),
                concurrences,
                dissents,
                stability,
                rightsProtection,
                partisanAlignment,
                shadowAbuse,
                legitimacy,
                responsiveness,
                conflict,
                precedentShift,
                administrativeCost
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

    private boolean emergencyShadowRelief(ReviewCase reviewCase, VoteCount voteCount, int participating) {
        if (design.emergencyDocketRule() == EmergencyDocketRule.NO_RELIEF_WITHOUT_MERITS) {
            return false;
        }
        int required = design.emergencyDocketRule() == EmergencyDocketRule.OPEN_EMERGENCY
                ? Math.max(1, participating / 2 + 1)
                : Math.max(1, (int) Math.floor(participating * 0.60) + 1);
        return reviewCase.emergencyPressure() > 0.45 && voteCount.yes() >= required;
    }

    private boolean crossCheckDisagreement(ReviewCase reviewCase, boolean invalidated, Random random) {
        if (design.auxiliaryReview() == AuxiliaryReview.NONE || design.auxiliaryReview() == AuxiliaryReview.CONSTITUTIONAL_COUNCIL) {
            return false;
        }
        double probability = 0.06 + reviewCase.legalAmbiguity() * 0.16 + reviewCase.partisanSalience() * 0.12;
        if (invalidated && reviewCase.democraticMandate() > 0.64) {
            probability += 0.12;
        }
        return random.nextDouble() < Values.clamp01(probability);
    }

    private boolean legislativeOverride(ReviewCase reviewCase, boolean invalidated, Random random) {
        if (!invalidated || design.overrideRule() == OverrideRule.NONE) {
            return false;
        }
        double base = reviewCase.democraticMandate() * 0.45 + reviewCase.publicAttention() * 0.20 - reviewCase.rightsBurden() * 0.24;
        double probability = switch (design.overrideRule()) {
            case NONE -> 0.0;
            case LEGISLATIVE_SUPERMAJORITY -> base - 0.12;
            case DELAYED_REENACTMENT -> base + 0.02;
            case POPULAR_REFERENDUM -> base + reviewCase.publicAttention() * 0.12 - reviewCase.partisanSalience() * 0.08;
        };
        return random.nextDouble() < Values.clamp01(probability);
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
                + reviewCase.legalAmbiguity() * 0.12;
        if (design.auxiliaryReview() == AuxiliaryReview.CONSTITUTIONAL_COUNCIL) {
            concern *= 0.92;
        }
        return Values.clamp01(concern);
    }

    private double rightsProtection(ReviewCase reviewCase, boolean invalidated, boolean shadowRelief, boolean override) {
        double protection = reviewCase.rightsBurden() > 0.55
                ? (invalidated || shadowRelief ? 0.82 : 0.30)
                : (invalidated ? 0.55 : 0.70);
        if (override && reviewCase.rightsBurden() > 0.55) {
            protection -= 0.22;
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

    private double shadowDocketAbuse(ReviewCase reviewCase, boolean emergency, boolean meritsReview, boolean shadowRelief) {
        if (!emergency) {
            return 0.0;
        }
        double rulePenalty = switch (design.emergencyDocketRule()) {
            case OPEN_EMERGENCY -> 0.32;
            case REASONED_FAST_TRACK -> 0.14;
            case SUPERMAJORITY_STAY -> 0.08;
            case NO_RELIEF_WITHOUT_MERITS -> 0.02;
        };
        double abuse = rulePenalty + (!meritsReview ? 0.22 : 0.0) + (shadowRelief ? 0.24 : 0.0);
        abuse += reviewCase.partisanSalience() * 0.12 + reviewCase.legalAmbiguity() * 0.08;
        return Values.clamp01(abuse);
    }

    private double constitutionalConflict(
            ReviewCase reviewCase,
            boolean invalidated,
            boolean shadowRelief,
            boolean crossDisagreement,
            boolean override,
            CourtState state
    ) {
        double conflict = reviewCase.constitutionalConflictPotential() * 0.38
                + reviewCase.executiveDefianceRisk() * 0.18
                + state.conflictLoad() * 0.12;
        if (invalidated) {
            conflict += reviewCase.democraticMandate() * 0.14;
        }
        if (shadowRelief) {
            conflict += 0.12;
        }
        if (crossDisagreement) {
            conflict += 0.16;
        }
        if (override) {
            conflict += reviewCase.rightsBurden() * 0.15;
        }
        return Values.clamp01(conflict);
    }

    private double legalStability(CourtState state, double precedentShift, double shadowAbuse, double conflict) {
        return Values.clamp01(state.precedentStability() - precedentShift * 0.28 - shadowAbuse * 0.18 - conflict * 0.12 + 0.12);
    }

    private double legitimacy(
            ReviewCase reviewCase,
            boolean meritsReview,
            int recused,
            int participating,
            double shadowAbuse,
            double partisanAlignment,
            boolean councilWarning
    ) {
        double reasonGiving = meritsReview ? 0.18 : -0.12;
        double recusalDiscipline = participating == 0 ? 0.0 : Math.min(0.16, recused * 0.04);
        double councilBoost = councilWarning ? 0.06 : 0.0;
        return Values.clamp01(
                0.48
                        + reviewCase.publicAttention() * 0.16
                        + reviewCase.legislativeQuality() * 0.10
                        + reasonGiving
                        + recusalDiscipline
                        + councilBoost
                        - shadowAbuse * 0.24
                        - partisanAlignment * 0.20
        );
    }

    private double democraticResponsiveness(ReviewCase reviewCase, boolean invalidated, boolean override, boolean councilWarning) {
        double respect = invalidated ? 1.0 - reviewCase.democraticMandate() * 0.42 : 0.58 + reviewCase.democraticMandate() * 0.26;
        if (override) {
            respect += 0.18;
        }
        if (reviewCase.rightsBurden() > 0.65 && !invalidated) {
            respect -= 0.12;
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

    private double administrativeCost(ReviewCase reviewCase, boolean emergency, boolean enBanc, boolean crossDisagreement, boolean councilWarning) {
        double cost = design.administrativeCost() + reviewCase.legalAmbiguity() * 0.10;
        if (emergency) {
            cost += 0.05;
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
}
