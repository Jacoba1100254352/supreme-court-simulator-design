package constitutionalreview.institution;

import constitutionalreview.model.CaseWorld;
import constitutionalreview.model.CourtState;
import constitutionalreview.model.DocketType;
import constitutionalreview.model.EmergencyMeritsFollowThrough;
import constitutionalreview.model.Justice;
import constitutionalreview.model.ReviewCase;
import constitutionalreview.model.AccessPath;
import constitutionalreview.simulation.AdmissionDecision;
import constitutionalreview.simulation.AdmissionFilter;
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

    private CourtDecision screenedOutDecision(ReviewCase reviewCase, AdmissionDecision admissionDecision, CourtState state) {
        double rightsProtection = reviewCase.rightsBurden() > 0.55 ? 0.26 : 0.62;
        double legalStability = Values.clamp01(0.72 + reviewCase.legislativeQuality() * 0.06 - reviewCase.legalAmbiguity() * 0.08);
        double lowerCourtCompliance = Values.clamp01(0.62 + reviewCase.lowerCourtConflict() * 0.08 - reviewCase.lowerCourtErrorRisk() * 0.10);
        double legitimacy = Values.clamp01(0.42 + admissionDecision.admissionScore() * 0.10 - reviewCase.publicAttention() * 0.08);
        double conflict = Values.clamp01(reviewCase.constitutionalConflictPotential() * 0.22 + state.conflictLoad() * 0.08);
        return new CourtDecision(
                reviewCase.id(),
                reviewCase.type(),
                reviewCase.docketType(),
                reviewCase.accessPath(),
                reviewCase.reviewTiming(),
                admissionDecision.petitionFiled(),
                false,
                admissionDecision.screenedOut(),
                false,
                admissionDecision.paidPetition(),
                admissionDecision.ifpPetition(),
                admissionDecision.admissionScore(),
                admissionDecision.conditionalReversalProbability(),
                certiorariPath(reviewCase),
                reviewCase.solicitorGeneralSignal(),
                reviewCase.amicusBriefs(),
                reviewCase.splitMaturity(),
                reviewCase.lowerCourtSplitDepth(),
                reviewCase.relistCount(),
                reviewCase.specialistCounsel(),
                reviewCase.vehicleDefectRisk(),
                reviewCase.strategicPlaintiffSelection(),
                reviewCase.repeatPlayerAdvantage(),
                reviewCase.governmentNoncomplianceRisk(),
                false,
                reviewCase.recusalIncentivePressure(),
                false,
                false,
                false,
                false,
                EmergencyProcedureStage.NONE,
                EmergencyOrder.none(),
                false,
                false,
                false,
                false,
                false,
                false,
                false,
                false,
                false,
                publicInterestFiltered(reviewCase, admissionDecision),
                false,
                false,
                OverrideOutcome.NONE,
                FormalLegalResponse.NONE,
                PracticalImplementationResponse.NONE,
                false,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                legalStability,
                legalStability,
                legalStability,
                lowerCourtCompliance,
                rightsProtection,
                0.0,
                0.0,
                0.0,
                legitimacy,
                0.42,
                conflict,
                0.0,
                legalStability,
                0.0,
                rightsClaimantCase(reviewCase),
                rightsClaimantSuccess(reviewCase, false, false, false),
                0.0,
                0.0,
                0.0,
                lowerCourtCompliance,
                lowerCourtCompliance,
                legitimacy,
                Values.clamp01(design.administrativeCost() * 0.36),
                state.legislativeDefiance(),
                state.executiveEmergencyStrategy(),
                state.appointmentManipulationPressure(),
                state.overrideAdaptation(),
                false,
                false,
                false,
                false,
                false,
                false
        );
    }

    @Override
    public CourtDecision review(ReviewCase reviewCase, CourtState state, Random random) {
        reviewedCases++;
        AdmissionDecision admissionDecision = AdmissionFilter.evaluate(reviewCase, design, random);
        if (!admissionDecision.admitted()) {
            return screenedOutDecision(reviewCase, admissionDecision, state);
        }
        StrategicActorPolicy.StrategicResponse strategicResponse = StrategicActorPolicy.choose(reviewCase, state, design, random);
        double effectiveEmergencyPressure = Values.clamp01(
                reviewCase.emergencyPressure()
                        + strategicResponse.emergencyPressureDelta()
                        + state.executiveEmergencyStrategy() * 0.20
                        + state.conflictLoad() * 0.04
                        + reviewCase.repeatPlayerAdvantage() * 0.05
                        + reviewCase.strategicPlaintiffSelection() * 0.04
        );
        boolean emergency = random.nextDouble() < effectiveEmergencyPressure;
        boolean initialMeritsReview = admissionDecision.transferredToMerits() && meritsReview(reviewCase, emergency, random);
        boolean enBanc = enBanc(reviewCase, emergency, random);
        List<Justice> participating = participatingJustices(reviewCase, enBanc, random);
        int recused = Math.max(0, Math.min(court.size(), court.size() - participating.size()));
        boolean quorumFailure = quorumFailure(recused, participating.size(), enBanc, random);

        VoteCount voteCount = vote(reviewCase, state, participating, emergency, random);
        EmergencyProcedure emergencyProcedure = emergencyProcedure(reviewCase, emergency, initialMeritsReview, voteCount, participating.size(), random);
        EmergencyOrder emergencyOrder = emergencyOrder(reviewCase, emergencyProcedure, voteCount, participating.size(), random);
        boolean meritsReview = initialMeritsReview || emergencyProcedure.meritsAccelerated();
        if (quorumFailure) {
            meritsReview = false;
        }
        int requiredVotes = requiredVotes(participating.size(), reviewCase);
        boolean invalidated = meritsReview && !quorumFailure && voteCount.yes() >= requiredVotes;
        boolean shadowRelief = emergencyProcedure.stage() == EmergencyProcedureStage.SHADOW_STAY;

        boolean councilWarning = (design.auxiliaryReview() == AuxiliaryReview.CONSTITUTIONAL_COUNCIL
                || design.auxiliaryReview() == AuxiliaryReview.CONSTITUTIONAL_REMAND)
                && legalConcern(reviewCase) > 0.54;
        boolean crossDisagreement = crossCheckDisagreement(reviewCase, invalidated, random);
        if (crossDisagreement && design.auxiliaryReview() == AuxiliaryReview.CROSS_CHECKING_COURT) {
            invalidated = false;
        }
        if (design.auxiliaryReview() == AuxiliaryReview.DUAL_SUPREME_COURTS && crossDisagreement) {
            invalidated = reviewCase.rightsBurden() > 0.68 || voteCount.yes() >= requiredVotes + 1;
        }
        boolean constitutionalRemand = constitutionalRemand(reviewCase, invalidated, random);
        if (constitutionalRemand) {
            invalidated = false;
            councilWarning = true;
        }

        OverrideDecision overrideDecision = legislativeOverride(reviewCase, invalidated, state, strategicResponse, random);
        boolean override = overrideDecision.successful();
        double precedentShift = precedentShift(reviewCase, invalidated, shadowRelief, crossDisagreement);
        boolean precedentReversal = invalidated && (precedentShift > 0.48 || reviewCase.legalAmbiguity() > 0.74);
        int concurrences = concurrences(voteCount, participating.size(), random);
        int dissents = Math.max(0, voteCount.no() - (participating.size() - voteCount.yes() > 0 ? 1 : 0));

        double rightsProtection = rightsProtection(reviewCase, invalidated, shadowRelief, constitutionalRemand, overrideDecision);
        double partisanAlignment = partisanAlignment(reviewCase, voteCount, participating);
        double shadowAbuse = shadowDocketAbuse(reviewCase, emergency, meritsReview, emergencyProcedure);
        double emergencyLegitimacyRisk = emergencyOrder.legitimacyRisk();
        double emergencyDownstreamEffect = emergencyDownstreamEffect(reviewCase, emergencyProcedure, emergencyOrder, shadowRelief);
        double conflict = constitutionalConflict(reviewCase, invalidated, shadowRelief, crossDisagreement, constitutionalRemand, emergencyDownstreamEffect, overrideDecision, state);
        double precedentStability = precedentStability(state, precedentShift, shadowAbuse, conflict);
        double statutoryStability = statutoryStability(reviewCase, invalidated, shadowRelief, constitutionalRemand, emergencyProcedure, overrideDecision, conflict);
        boolean governmentNoncompliance = governmentNoncompliance(reviewCase, strategicResponse, conflict, state, random);
        double interbranchCompliance = interbranchCompliance(reviewCase, crossDisagreement, councilWarning, governmentNoncompliance, overrideDecision, conflict, state);
        double legalStability = Values.average(precedentStability, statutoryStability, interbranchCompliance);
        double legitimacy = legitimacy(reviewCase, meritsReview, emergencyProcedure, recused, participating.size(), shadowAbuse, partisanAlignment, councilWarning);
        double responsiveness = democraticResponsiveness(reviewCase, invalidated, constitutionalRemand, overrideDecision, councilWarning);
        boolean rightsClaimantCase = rightsClaimantCase(reviewCase);
        double rightsClaimantSuccess = rightsClaimantSuccess(reviewCase, invalidated, shadowRelief, constitutionalRemand);
        double doctrinalDepth = doctrinalDepth(reviewCase, invalidated, precedentShift, emergencyProcedure);
        double remedialBreadth = remedialBreadth(reviewCase, invalidated, shadowRelief, constitutionalRemand, emergencyProcedure, overrideDecision);
        double fragmentationIndex = fragmentationIndex(concurrences, dissents, voteCount, participating.size());
        double precedentDurability = precedentDurability(precedentStability, doctrinalDepth, fragmentationIndex, emergencyDownstreamEffect, shadowAbuse);
        double lowerCourtCompliance = lowerCourtCompliance(reviewCase, meritsReview, invalidated, constitutionalRemand, governmentNoncompliance, admissionDecision, state);
        double eliteAcceptance = eliteAcceptance(interbranchCompliance, overrideDecision, strategicResponse);
        double publicConfidence = publicConfidence(legitimacy, emergencyLegitimacyRisk, partisanAlignment, strategicResponse);
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
                emergencyDownstreamEffect,
                governmentNoncompliance,
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
                reviewCase.accessPath(),
                reviewCase.reviewTiming(),
                admissionDecision.petitionFiled(),
                admissionDecision.admitted(),
                admissionDecision.screenedOut(),
                admissionDecision.transferredToMerits(),
                admissionDecision.paidPetition(),
                admissionDecision.ifpPetition(),
                admissionDecision.admissionScore(),
                admissionDecision.conditionalReversalProbability(),
                certiorariPath(reviewCase),
                reviewCase.solicitorGeneralSignal(),
                reviewCase.amicusBriefs(),
                reviewCase.splitMaturity(),
                reviewCase.lowerCourtSplitDepth(),
                reviewCase.relistCount(),
                reviewCase.specialistCounsel(),
                reviewCase.vehicleDefectRisk(),
                reviewCase.strategicPlaintiffSelection(),
                reviewCase.repeatPlayerAdvantage(),
                reviewCase.governmentNoncomplianceRisk(),
                governmentNoncompliance,
                recusalIncentivePressure(reviewCase, recused, quorumFailure),
                meritsReview,
                invalidated,
                emergency,
                shadowRelief,
                emergencyProcedure.stage(),
                emergencyOrder,
                emergencyProcedure.reasonedOrder(),
                emergencyProcedure.temporaryStay(),
                emergencyProcedure.meritsAccelerated(),
                emergencyProcedure.expired(),
                enBanc,
                quorumFailure,
                councilWarning,
                crossDisagreement,
                constitutionalRemand,
                publicInterestFiltered(reviewCase, admissionDecision),
                override,
                overrideDecision.attempted(),
                overrideDecision.outcome(),
                strategicResponse.formalResponse(),
                strategicResponse.practicalImplementationResponse(),
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
                emergencyLegitimacyRisk,
                legitimacy,
                responsiveness,
                conflict,
                precedentShift,
                precedentDurability,
                emergencyDownstreamEffect,
                rightsClaimantCase,
                rightsClaimantSuccess,
                doctrinalDepth,
                remedialBreadth,
                fragmentationIndex,
                lowerCourtCompliance,
                eliteAcceptance,
                publicConfidence,
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
            return design.emergencyDocketRule() == EmergencyDocketRule.AUTOMATIC_MERITS_FOLLOW_UP
                    && random.nextDouble() > 0.10;
        }
        return switch (design.emergencyDocketRule()) {
            case OPEN_EMERGENCY -> random.nextDouble() > 0.35;
            case REASONED_FAST_TRACK -> random.nextDouble() > 0.18;
            case SUPERMAJORITY_STAY -> random.nextDouble() > 0.10;
            case NO_RELIEF_WITHOUT_MERITS, MANDATORY_WRITTEN_REASONING, AUTOMATIC_MERITS_FOLLOW_UP -> true;
        };
    }

    private boolean enBanc(ReviewCase reviewCase, boolean emergency, Random random) {
        if (design.reviewMode() == ReviewMode.FULL_COURT || design.reviewMode() == ReviewMode.DUAL_COURTS) {
            return true;
        }
        double probability = 0.10
                + reviewCase.rightsBurden() * 0.18
                + reviewCase.partisanSalience() * 0.16
                + reviewCase.lowerCourtSplitDepth() * 0.14;
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
        double conflict = reviewCase.partisanSalience() * justice.partisanLoyalty() * (1.0 - justice.independence())
                + reviewCase.recusalIncentivePressure() * 0.18
                + reviewCase.repeatPlayerAdvantage() * 0.06;
        double probability = switch (design.recusalRule()) {
            case SELF_POLICED -> conflict * 0.08;
            case PUBLIC_EXPLANATION -> conflict * 0.22;
            case PEER_PANEL -> conflict * 0.38;
            case AUTOMATIC_CONFLICT_SCREEN -> conflict * 0.64;
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
            double repeatPlayerPull = reviewCase.repeatPlayerAdvantage() * (1.0 - justice.independence()) * 0.08;
            double plaintiffSelectionSignal = reviewCase.strategicPlaintiffSelection() * reviewCase.rightsBurden() * 0.06;
            double score = legalConcern * 0.42
                    + rightsConcern
                    + partisanPull
                    + plaintiffSelectionSignal
                    - deference
                    - emergencyDeference
                    - stabilityPenalty
                    - accountabilityPull
                    - repeatPlayerPull
                    + random.nextGaussian() * 0.07;
            if (score > 0.04) {
                yes++;
            }
        }
        return new VoteCount(yes, justices.size() - yes);
    }

    private int requiredVotes(int participating, ReviewCase reviewCase) {
        double share = reviewCase.rightsBurden() > 0.68
                ? Math.max(design.votingThreshold().requiredShare(true), design.remedyVotingThresholds().rightsClaimShare())
                : Math.max(design.votingThreshold().requiredShare(false), design.remedyVotingThresholds().lawStrikeShare());
        if ((design.emergencyDocketRule() == EmergencyDocketRule.SUPERMAJORITY_STAY
                || design.emergencyDocketRule() == EmergencyDocketRule.MANDATORY_WRITTEN_REASONING)
                && reviewCase.emergencyPressure() > 0.62) {
            share = Math.max(share, design.remedyVotingThresholds().emergencyReliefShare());
        }
        return Math.max(1, (int) Math.ceil(participating * share - 0.000_001));
    }

    private boolean quorumFailure(int recused, int participating, boolean enBanc, Random random) {
        if (recused == 0 || design.recusalConsequenceType() != RecusalConsequenceType.QUORUM_FAILURE_AFFIRMANCE) {
            return false;
        }
        int quorum = enBanc ? Math.max(3, (int) Math.ceil(design.courtSize() * 0.50)) : Math.min(3, design.courtSize());
        double probability = design.quorumFailureRisk()
                + (participating < quorum ? 0.18 : 0.0)
                + Math.max(0, recused - 1) * 0.018;
        return random.nextDouble() < Values.clamp01(probability);
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
            case MANDATORY_WRITTEN_REASONING -> {
                if (supermajorityVotes) {
                    yield new EmergencyProcedure(EmergencyProcedureStage.REASONED_TEMPORARY_STAY, true, true, false, false);
                }
                if (random.nextDouble() < 0.54 || reviewCase.rightsBurden() > 0.64) {
                    yield new EmergencyProcedure(EmergencyProcedureStage.MERITS_ACCELERATED, true, false, true, false);
                }
                yield new EmergencyProcedure(EmergencyProcedureStage.RESPONSE_WINDOW, true, false, false, false);
            }
            case AUTOMATIC_MERITS_FOLLOW_UP -> {
                if (emergencyVotes) {
                    yield new EmergencyProcedure(EmergencyProcedureStage.REASONED_TEMPORARY_STAY, true, true, true, false);
                }
                yield new EmergencyProcedure(EmergencyProcedureStage.MERITS_ACCELERATED, true, false, true, false);
            }
            case NO_RELIEF_WITHOUT_MERITS -> new EmergencyProcedure(EmergencyProcedureStage.MERITS_ACCELERATED, true, false, true, false);
        };
    }

    private EmergencyOrder emergencyOrder(
            ReviewCase reviewCase,
            EmergencyProcedure emergencyProcedure,
            VoteCount voteCount,
            int participating,
            Random random
    ) {
        if (emergencyProcedure.stage() == EmergencyProcedureStage.NONE) {
            return EmergencyOrder.none();
        }
        boolean granted = emergencyProcedure.temporaryStay()
                || emergencyProcedure.meritsAccelerated()
                || emergencyProcedure.stage() == EmergencyProcedureStage.SHADOW_STAY;
        boolean explanation = emergencyProcedure.reasonedOrder()
                || design.emergencyDocketRule() != EmergencyDocketRule.OPEN_EMERGENCY
                || random.nextDouble() < 0.18 + reviewCase.publicAttention() * 0.20;
        boolean voteDisclosed = explanation || random.nextDouble() < 0.20 + reviewCase.partisanSalience() * 0.22;
        int disagreement = 0;
        int minority = Math.max(0, Math.min(voteCount.yes(), voteCount.no()));
        for (int i = 0; i < minority; i++) {
            if (random.nextDouble() < Values.clamp01(reviewCase.emergencyApplication().publicDisagreementRisk() + reviewCase.partisanSalience() * 0.18)) {
                disagreement++;
            }
        }
        EmergencyMeritsFollowThrough followThrough = EmergencyMeritsFollowThrough.NONE;
        if (design.emergencyDocketRule() == EmergencyDocketRule.AUTOMATIC_MERITS_FOLLOW_UP && granted) {
            followThrough = voteCount.yes() >= voteCount.no()
                    ? EmergencyMeritsFollowThrough.LATER_MERITS_AFFIRMED
                    : EmergencyMeritsFollowThrough.LATER_MERITS_REVERSED;
        } else if (emergencyProcedure.meritsAccelerated()) {
            followThrough = random.nextBoolean()
                    ? EmergencyMeritsFollowThrough.DEFERRED_TO_ORAL_ARGUMENT
                    : EmergencyMeritsFollowThrough.LATER_CERT_GRANTED;
        } else if (granted && random.nextDouble() < reviewCase.emergencyApplication().meritsFollowThroughProbability()) {
            followThrough = random.nextBoolean()
                    ? EmergencyMeritsFollowThrough.LATER_MERITS_AFFIRMED
                    : EmergencyMeritsFollowThrough.LATER_MERITS_REVERSED;
        }
        double abuse = shadowDocketAbuse(reviewCase, true, emergencyProcedure.meritsAccelerated(), emergencyProcedure);
        double legitimacyRisk = emergencyLegitimacyRisk(reviewCase, emergencyProcedure, explanation, disagreement, granted);
        return new EmergencyOrder(granted, explanation, voteDisclosed, disagreement, followThrough, abuse, legitimacyRisk);
    }

    private boolean crossCheckDisagreement(ReviewCase reviewCase, boolean invalidated, Random random) {
        if (design.auxiliaryReview() == AuxiliaryReview.NONE
                || design.auxiliaryReview() == AuxiliaryReview.CONSTITUTIONAL_COUNCIL
                || design.auxiliaryReview() == AuxiliaryReview.CONSTITUTIONAL_REMAND
                || design.auxiliaryReview() == AuxiliaryReview.PUBLIC_INTEREST_FILTER) {
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
        if (design.overrideRule() == OverrideRule.JURISDICTION_STRIPPING_CONSTRAINT) {
            return new OverrideDecision(true, false, OverrideOutcome.FAILED);
        }
        if (reviewCase.rightsBurden() > 0.72 && design.overrideRule() != OverrideRule.POPULAR_REFERENDUM) {
            return new OverrideDecision(true, false, OverrideOutcome.RIGHTS_CARVEOUT_BLOCKED);
        }
        double probability = switch (design.overrideRule()) {
            case NONE -> 0.0;
            case LEGISLATIVE_SUPERMAJORITY -> base - 0.12;
            case DELAYED_REENACTMENT -> base + 0.02;
            case POPULAR_REFERENDUM -> base + reviewCase.publicAttention() * 0.12 - reviewCase.partisanSalience() * 0.08;
            case LEGISLATIVE_WINDOW -> base - 0.04 + reviewCase.democraticMandate() * 0.08 - state.overrideAdaptation() * 0.08;
            case JURISDICTION_STRIPPING_CONSTRAINT -> 0.0;
        };
        if (random.nextDouble() >= Values.clamp01(probability)) {
            return new OverrideDecision(true, false, OverrideOutcome.FAILED);
        }
        OverrideOutcome outcome = switch (design.overrideRule()) {
            case NONE -> OverrideOutcome.NONE;
            case LEGISLATIVE_SUPERMAJORITY -> OverrideOutcome.ORDINARY_SUPERMAJORITY;
            case DELAYED_REENACTMENT -> OverrideOutcome.DELAYED_REENACTMENT;
            case POPULAR_REFERENDUM -> OverrideOutcome.REFERENDUM_APPROVAL;
            case LEGISLATIVE_WINDOW -> OverrideOutcome.DELAYED_REENACTMENT;
            case JURISDICTION_STRIPPING_CONSTRAINT -> OverrideOutcome.FAILED;
        };
        if (design.overrideRule() != OverrideRule.LEGISLATIVE_WINDOW
                && state.conflictLoad() > 0.52
                && reviewCase.overridePressure() > 0.58
                && random.nextDouble() < 0.35) {
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
                + reviewCase.lowerCourtErrorRisk() * 0.10
                + reviewCase.lowerCourtSplitDepth() * 0.08;
        if (design.auxiliaryReview() == AuxiliaryReview.CONSTITUTIONAL_COUNCIL) {
            concern *= 0.92;
        } else if (design.auxiliaryReview() == AuxiliaryReview.CONSTITUTIONAL_REMAND && reviewCase.legislativeQuality() > 0.52) {
            concern *= 0.96;
        } else if (design.auxiliaryReview() == AuxiliaryReview.PUBLIC_INTEREST_FILTER && reviewCase.rightsBurden() < 0.42) {
            concern *= 0.88;
        }
        return Values.clamp01(concern);
    }

    private double rightsProtection(
            ReviewCase reviewCase,
            boolean invalidated,
            boolean shadowRelief,
            boolean constitutionalRemand,
            OverrideDecision overrideDecision
    ) {
        double protection = reviewCase.rightsBurden() > 0.55
                ? (invalidated || shadowRelief ? 0.82 : 0.30)
                : (invalidated ? 0.55 : 0.70);
        if (constitutionalRemand && reviewCase.rightsBurden() > 0.55) {
            protection += 0.24;
        } else if (constitutionalRemand) {
            protection += 0.06;
        }
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
            case MANDATORY_WRITTEN_REASONING -> 0.05;
            case AUTOMATIC_MERITS_FOLLOW_UP -> 0.04;
        };
        double abuse = rulePenalty
                + (!meritsReview ? 0.22 : 0.0)
                + (emergencyProcedure.stage() == EmergencyProcedureStage.SHADOW_STAY ? 0.24 : 0.0)
                - (emergencyProcedure.reasonedOrder() ? 0.08 : 0.0)
                - (emergencyProcedure.meritsAccelerated() ? 0.07 : 0.0);
        abuse += reviewCase.partisanSalience() * 0.12 + reviewCase.legalAmbiguity() * 0.08;
        return Values.clamp01(abuse);
    }

    private double emergencyLegitimacyRisk(
            ReviewCase reviewCase,
            EmergencyProcedure emergencyProcedure,
            boolean explanation,
            int disagreement,
            boolean granted
    ) {
        if (emergencyProcedure.stage() == EmergencyProcedureStage.NONE) {
            return 0.0;
        }
        double opacity = explanation ? 0.08 : 0.26;
        double meritsLike = emergencyProcedure.meritsAccelerated() ? 0.08 : 0.18;
        double disagreementRisk = Math.min(0.22, disagreement * 0.06);
        double statusQuoRisk = switch (reviewCase.emergencyApplication().statusQuoEffect()) {
            case ALTERS_STATUS_QUO -> 0.18;
            case PRESERVES_ENACTED_POLICY -> 0.10;
            case PRESERVES_INJUNCTION, UNCLEAR -> 0.08;
            case NONE -> 0.0;
        };
        double grantedRisk = granted ? 0.08 : 0.02;
        return Values.clamp01(
                reviewCase.publicAttention() * 0.20
                        + reviewCase.rightsBurden() * 0.12
                        + opacity
                        + meritsLike
                        + disagreementRisk
                        + statusQuoRisk
                        + grantedRisk
        );
    }

    private double rightsClaimantSuccess(ReviewCase reviewCase, boolean invalidated, boolean shadowRelief, boolean constitutionalRemand) {
        if (!rightsClaimantCase(reviewCase)) {
            return 0.0;
        }
        if (invalidated || shadowRelief) {
            return 1.0;
        }
        return constitutionalRemand ? 0.55 : 0.0;
    }

    private boolean rightsClaimantCase(ReviewCase reviewCase) {
        return reviewCase.rightsBurden() >= 0.45;
    }

    private double doctrinalDepth(ReviewCase reviewCase, boolean invalidated, double precedentShift, EmergencyProcedure emergencyProcedure) {
        double depth = precedentShift * 0.62 + reviewCase.legalAmbiguity() * 0.12;
        if (invalidated) {
            depth += reviewCase.publicAttention() * 0.12;
        }
        if (emergencyProcedure.meritsAccelerated()) {
            depth += 0.06;
        }
        return Values.clamp01(depth);
    }

    private double remedialBreadth(
            ReviewCase reviewCase,
            boolean invalidated,
            boolean shadowRelief,
            boolean constitutionalRemand,
            EmergencyProcedure emergencyProcedure,
            OverrideDecision overrideDecision
    ) {
        double breadth = 0.0;
        if (invalidated) {
            breadth += 0.46 + reviewCase.publicAttention() * 0.18 + reviewCase.rightsBurden() * 0.10;
        }
        if (shadowRelief || emergencyProcedure.temporaryStay()) {
            breadth += 0.18;
        }
        if (constitutionalRemand) {
            breadth += 0.26;
        }
        if (overrideDecision.successful()) {
            breadth -= 0.16;
        }
        return Values.clamp01(breadth);
    }

    private double fragmentationIndex(int concurrences, int dissents, VoteCount voteCount, int participating) {
        if (participating <= 0) {
            return 0.0;
        }
        int majority = Math.max(voteCount.yes(), voteCount.no());
        double majorityCohesionPenalty = 1.0 - (majority / (double) participating);
        double separateOpinions = (concurrences + dissents) / (double) Math.max(1, participating);
        return Values.clamp01(majorityCohesionPenalty + separateOpinions * 0.45);
    }

    private double lowerCourtCompliance(
            ReviewCase reviewCase,
            boolean meritsReview,
            boolean invalidated,
            boolean constitutionalRemand,
            boolean governmentNoncompliance,
            AdmissionDecision admissionDecision,
            CourtState state
    ) {
        double compliance = 0.68
                - reviewCase.lowerCourtConflict() * 0.18
                - reviewCase.lowerCourtErrorRisk() * 0.12
                - reviewCase.lowerCourtSplitDepth() * 0.08
                - state.conflictLoad() * 0.10
                + (meritsReview ? 0.08 : -0.03)
                + (admissionDecision.transferredToMerits() ? 0.04 : 0.0);
        if (invalidated) {
            compliance -= 0.08;
        }
        if (constitutionalRemand) {
            compliance += 0.09;
        }
        if (governmentNoncompliance) {
            compliance -= 0.16;
        }
        return Values.clamp01(compliance);
    }

    private double eliteAcceptance(
            double interbranchCompliance,
            OverrideDecision overrideDecision,
            StrategicActorPolicy.StrategicResponse strategicResponse
    ) {
        double acceptance = interbranchCompliance
                + (strategicResponse.legislativeCompliance() ? 0.08 : 0.0)
                - (strategicResponse.legislativeEvasion() ? 0.10 : 0.0)
                - (strategicResponse.practicalImplementationResponse() == PracticalImplementationResponse.OPEN_NONCOMPLIANCE ? 0.24 : 0.0)
                - (strategicResponse.formalResponse() == FormalLegalResponse.COURT_CURBING ? 0.18 : 0.0)
                - (overrideDecision.attempted() ? 0.06 : 0.0);
        return Values.clamp01(acceptance);
    }

    private double publicConfidence(
            double legitimacy,
            double emergencyLegitimacyRisk,
            double partisanAlignment,
            StrategicActorPolicy.StrategicResponse strategicResponse
    ) {
        double confidence = legitimacy
                - emergencyLegitimacyRisk * 0.18
                - partisanAlignment * 0.12
                - (strategicResponse.appointmentPressureCampaign() ? 0.08 : 0.0)
                - (strategicResponse.formalResponse() == FormalLegalResponse.COURT_CURBING ? 0.10 : 0.0);
        return Values.clamp01(confidence);
    }

    private double constitutionalConflict(
            ReviewCase reviewCase,
            boolean invalidated,
            boolean shadowRelief,
            boolean crossDisagreement,
            boolean constitutionalRemand,
            double emergencyDownstreamEffect,
            OverrideDecision overrideDecision,
            CourtState state
    ) {
        double conflict = reviewCase.constitutionalConflictPotential() * 0.38
                + reviewCase.executiveDefianceRisk() * 0.18
                + reviewCase.lowerCourtConflict() * 0.08
                + reviewCase.lowerCourtSplitDepth() * 0.05
                + state.conflictLoad() * 0.12
                + state.legislativeDefiance() * 0.10
                + state.executiveEmergencyStrategy() * 0.08
                + emergencyDownstreamEffect * 0.12;
        if (invalidated) {
            conflict += reviewCase.democraticMandate() * 0.14;
        }
        if (shadowRelief) {
            conflict += 0.12;
        }
        if (crossDisagreement) {
            conflict += 0.16;
        }
        if (constitutionalRemand) {
            conflict -= 0.07;
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
            boolean constitutionalRemand,
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
        if (constitutionalRemand) {
            stability += 0.08;
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
            boolean governmentNoncompliance,
            OverrideDecision overrideDecision,
            double conflict,
            CourtState state
    ) {
        double compliance = 0.76
                + reviewCase.legislativeQuality() * 0.08
                + reviewCase.democraticMandate() * 0.04
                - reviewCase.executiveDefianceRisk() * 0.18
                - reviewCase.governmentNoncomplianceRisk() * 0.12
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
        if (governmentNoncompliance) {
            compliance -= 0.18;
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

    private double democraticResponsiveness(
            ReviewCase reviewCase,
            boolean invalidated,
            boolean constitutionalRemand,
            OverrideDecision overrideDecision,
            boolean councilWarning
    ) {
        double respect = invalidated ? 1.0 - reviewCase.democraticMandate() * 0.42 : 0.58 + reviewCase.democraticMandate() * 0.26;
        if (constitutionalRemand) {
            respect += 0.08;
        }
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
        double shift = invalidated
                ? 0.16 + reviewCase.legalAmbiguity() * 0.16 + reviewCase.rightsBurden() * 0.09 + reviewCase.lowerCourtSplitDepth() * 0.06
                : 0.04;
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
        if (design.auxiliaryReview() == AuxiliaryReview.CONSTITUTIONAL_REMAND) {
            cost += 0.04;
        }
        if (design.auxiliaryReview() == AuxiliaryReview.PUBLIC_INTEREST_FILTER) {
            cost += 0.03;
        }
        if (design.emergencyDocketRule() == EmergencyDocketRule.AUTOMATIC_MERITS_FOLLOW_UP
                || design.emergencyDocketRule() == EmergencyDocketRule.MANDATORY_WRITTEN_REASONING) {
            cost += 0.03;
        }
        return Values.clamp01(cost);
    }

    private boolean constitutionalRemand(ReviewCase reviewCase, boolean invalidated, Random random) {
        if (design.auxiliaryReview() != AuxiliaryReview.CONSTITUTIONAL_REMAND || !invalidated) {
            return false;
        }
        double probability = 0.18
                + reviewCase.legislativeQuality() * 0.18
                + reviewCase.democraticMandate() * 0.12
                + reviewCase.lowerCourtSplitDepth() * 0.10
                - reviewCase.rightsBurden() * 0.14;
        return random.nextDouble() < Values.clamp01(probability);
    }

    private boolean publicInterestFiltered(ReviewCase reviewCase, AdmissionDecision admissionDecision) {
        return design.auxiliaryReview() == AuxiliaryReview.PUBLIC_INTEREST_FILTER
                && admissionDecision.screenedOut()
                && reviewCase.rightsBurden() < 0.45
                && reviewCase.publicAttention() < 0.55;
    }

    private static boolean certiorariPath(ReviewCase reviewCase) {
        return reviewCase.accessPath() == AccessPath.DISCRETIONARY_CERTIORARI
                || reviewCase.accessPath() == AccessPath.PAID_CERTIORARI
                || reviewCase.accessPath() == AccessPath.IFP_CERTIORARI;
    }

    private double emergencyDownstreamEffect(
            ReviewCase reviewCase,
            EmergencyProcedure emergencyProcedure,
            EmergencyOrder emergencyOrder,
            boolean shadowRelief
    ) {
        if (emergencyProcedure.stage() == EmergencyProcedureStage.NONE) {
            return 0.0;
        }
        double effect = reviewCase.emergencyPressure() * 0.18
                + reviewCase.requestedEmergencyRelief() * 0.12
                + reviewCase.governmentNoncomplianceRisk() * 0.12
                + (emergencyOrder.granted() ? 0.12 : 0.02)
                + (shadowRelief ? 0.18 : 0.0)
                + (emergencyProcedure.temporaryStay() ? 0.06 : 0.0)
                - (emergencyProcedure.reasonedOrder() ? 0.08 : 0.0)
                - (emergencyProcedure.meritsAccelerated() ? 0.10 : 0.0);
        if (emergencyOrder.meritsFollowThrough() == EmergencyMeritsFollowThrough.LATER_MERITS_REVERSED) {
            effect += 0.10;
        } else if (emergencyOrder.meritsFollowThrough() != EmergencyMeritsFollowThrough.NONE) {
            effect -= 0.04;
        }
        if (design.emergencyDocketRule() == EmergencyDocketRule.AUTOMATIC_MERITS_FOLLOW_UP) {
            effect -= 0.08;
        }
        return Values.clamp01(effect);
    }

    private boolean governmentNoncompliance(
            ReviewCase reviewCase,
            StrategicActorPolicy.StrategicResponse strategicResponse,
            double conflict,
            CourtState state,
            Random random
    ) {
        double probability = reviewCase.governmentNoncomplianceRisk() * 0.36
                + state.legislativeDefiance() * 0.18
                + state.executiveEmergencyStrategy() * 0.12
                + conflict * 0.16
                + (strategicResponse.practicalImplementationResponse() == PracticalImplementationResponse.OPEN_NONCOMPLIANCE ? 0.32 : 0.0)
                + (strategicResponse.practicalImplementationResponse() == PracticalImplementationResponse.BUREAUCRATIC_RESISTANCE ? 0.10 : 0.0)
                - (strategicResponse.legislativeCompliance() ? 0.12 : 0.0);
        return random.nextDouble() < Values.clamp01(probability);
    }

    private static double recusalIncentivePressure(ReviewCase reviewCase, int recused, boolean quorumFailure) {
        return Values.clamp01(
                reviewCase.recusalIncentivePressure()
                        + recused * 0.035
                        + (quorumFailure ? 0.18 : 0.0)
        );
    }

    private static double precedentDurability(
            double precedentStability,
            double doctrinalDepth,
            double fragmentationIndex,
            double emergencyDownstreamEffect,
            double shadowAbuse
    ) {
        return Values.clamp01(
                precedentStability
                        + doctrinalDepth * 0.12
                        - fragmentationIndex * 0.10
                        - emergencyDownstreamEffect * 0.12
                        - shadowAbuse * 0.10
        );
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
