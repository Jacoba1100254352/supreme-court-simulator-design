package constitutionalreview.simulation;

import constitutionalreview.institution.AppointmentMethod;
import constitutionalreview.institution.CourtDesign;
import constitutionalreview.model.ClaimantType;
import constitutionalreview.model.AccessPath;
import constitutionalreview.model.PetitionType;
import constitutionalreview.model.ReviewCase;
import constitutionalreview.util.Values;

import java.util.Random;

public final class AdmissionFilter {
    private AdmissionFilter() {
    }

    public static AdmissionDecision evaluate(ReviewCase reviewCase, CourtDesign design, Random random) {
        double petitionProbability = petitionProbability(reviewCase);
        boolean petitionFiled = random.nextDouble() < petitionProbability;
        if (!petitionFiled) {
            return new AdmissionDecision(false, false, false, false, paid(reviewCase), ifp(reviewCase), false, false, 0.0, reviewCase.conditionalReversalProbability());
        }

        double preliminaryScore = admissionScore(reviewCase, design);
        boolean courtRequestedResponse = courtRequestedResponse(reviewCase, preliminaryScore, random);
        boolean cvsgRequested = cvsgRequested(reviewCase, courtRequestedResponse, random);
        double score = Values.clamp01(preliminaryScore
                + (courtRequestedResponse ? 0.055 : 0.0)
                + (cvsgRequested ? 0.13 : 0.0));
        if (certiorariPath(reviewCase)) {
            score = certiorariGateScore(reviewCase, score, courtRequestedResponse, cvsgRequested);
        }
        boolean admitted = random.nextDouble() < score;
        boolean transferredToMerits = admitted && transferredToMerits(reviewCase, score, random);
        return new AdmissionDecision(
                true,
                admitted,
                !admitted,
                transferredToMerits,
                paid(reviewCase),
                ifp(reviewCase),
                courtRequestedResponse,
                cvsgRequested,
                score,
                reviewCase.conditionalReversalProbability()
        );
    }

    private static double petitionProbability(ReviewCase reviewCase) {
        double base = switch (reviewCase.petitionType()) {
            case PAID_CERT -> 0.76;
            case IFP_CERT -> 0.54;
            case DIRECT_APPEAL -> 0.94;
            case CONSTITUTIONAL_COMPLAINT, ABSTRACT_REFERRAL, FILTERED_REFERRAL -> 0.98;
            case EMERGENCY_APPLICATION -> 1.0;
        };
        return Values.clamp01(base
                + reviewCase.lowerCourtConflict() * 0.08
                + reviewCase.lowerCourtSplitDepth() * 0.08
                + reviewCase.publicAttention() * 0.08
                + reviewCase.solicitorGeneralSignal() * 0.06
                + reviewCase.barCapital() * 0.05
                + reviewCase.claimStrength() * 0.05
                + reviewCase.strategicPlaintiffSelection() * 0.08
                + reviewCase.repeatPlayerAdvantage() * 0.06
                + reviewCase.forumShoppingPressure() * 0.04
                - reviewCase.preReviewSettlementPressure() * 0.05
                - reviewCase.vehicleDefectRisk() * 0.22);
    }

    private static double admissionScore(ReviewCase reviewCase, CourtDesign design) {
        double amicusSignal = Math.min(1.0, reviewCase.amicusBriefs() / 4.0);
        double relistSignal = reviewCase.relistCount() >= 3 && reviewCase.relistCount() <= 4
                ? 0.72
                : Math.min(0.45, reviewCase.relistCount() * 0.10);
        double pathAdjustment = switch (reviewCase.accessPath()) {
            case PAID_CERTIORARI, DISCRETIONARY_CERTIORARI -> 0.02;
            case IFP_CERTIORARI -> -0.20;
            case EMERGENCY_APPLICATION -> 0.24;
            case ABSTRACT_EX_ANTE_REVIEW -> 0.28;
            case ABSTRACT_EX_POST_REVIEW -> 0.18;
            case COURT_REFERRAL_CONCRETE_REVIEW, FILTERED_QPC -> 0.10;
            case DIRECT_CONSTITUTIONAL_COMPLAINT, AMPARO -> -0.18;
            case INTERBRANCH_DISPUTE, ELECTORAL_REVIEW -> 0.20;
        };
        if (design.auxiliaryReview() == constitutionalreview.institution.AuxiliaryReview.PUBLIC_INTEREST_FILTER) {
            pathAdjustment += reviewCase.rightsBurden() > 0.52 || reviewCase.publicAttention() > 0.56
                    ? 0.08
                    : -0.12;
        }
        if (design.auxiliaryReview() == constitutionalreview.institution.AuxiliaryReview.CONSTITUTIONAL_REMAND) {
            pathAdjustment += 0.03;
        }
        double designGatekeeping = design.appointmentFragmentation() > 2 ? 0.02 : 0.0;
        if (design.appointmentMethod() == AppointmentMethod.JUDICIAL_ELECTORATE) {
            designGatekeeping += design.judicialElectorateInsulation() * 0.012;
        }
        double score = 0.18
                + reviewCase.certiorariPressure() * 0.22
                + reviewCase.lowerCourtConflict() * 0.12
                + reviewCase.lowerCourtSplitDepth() * 0.13
                + reviewCase.lowerCourtErrorRisk() * 0.10
                + reviewCase.claimStrength() * 0.10
                + reviewCase.vehicleQuality() * 0.09
                + (reviewCase.genuineLowerCourtSplit() ? 0.06 : 0.0)
                + reviewCase.solicitorGeneralSignal() * 0.15
                + amicusSignal * 0.10
                + reviewCase.splitMaturity() * 0.08
                + relistSignal * 0.07
                + (reviewCase.specialistCounsel() ? 0.05 : 0.0)
                + reviewCase.barCapital() * 0.06
                + reviewCase.strategicPlaintiffSelection() * 0.05
                + reviewCase.repeatPlayerAdvantage() * 0.05
                + reviewCase.forumShoppingPressure() * 0.02
                + reviewCase.conditionalReversalProbability() * 0.08
                + pathAdjustment
                + designGatekeeping
                - reviewCase.preReviewSettlementPressure() * 0.06
                - reviewCase.vehicleDefectRisk() * 0.16
                + (design.vacancyDeadlockRisk() * -0.03);
        return Values.clamp01(score);
    }

    private static boolean courtRequestedResponse(ReviewCase reviewCase, double admissionScore, Random random) {
        double amicusSignal = Math.min(1.0, reviewCase.amicusBriefs() / 4.0);
        double base = switch (reviewCase.petitionType()) {
            case PAID_CERT -> 0.014;
            case IFP_CERT -> 0.006;
            case DIRECT_APPEAL, ABSTRACT_REFERRAL, FILTERED_REFERRAL, CONSTITUTIONAL_COMPLAINT -> 0.05;
            case EMERGENCY_APPLICATION -> reviewCase.emergencyApplication().responseRequested() ? 0.54 : 0.16;
        };
        double probability = base
                + reviewCase.solicitorGeneralSignal() * 0.035
                + amicusSignal * 0.018
                + reviewCase.lowerCourtSplitDepth() * 0.018
                + (reviewCase.genuineLowerCourtSplit() ? 0.012 : 0.0)
                + reviewCase.vehicleQuality() * 0.012
                + admissionScore * 0.014
                - reviewCase.vehicleDefectRisk() * 0.012;
        if (reviewCase.petitionType() == PetitionType.EMERGENCY_APPLICATION
                && reviewCase.emergencyApplication().referredToFullCourt()) {
            probability += 0.22;
        }
        return random.nextDouble() < Values.clamp01(probability);
    }

    private static boolean cvsgRequested(ReviewCase reviewCase, boolean courtRequestedResponse, Random random) {
        if (!courtRequestedResponse || !certiorariPath(reviewCase)) {
            return false;
        }
        double governmentCue = reviewCase.claimantType() == ClaimantType.GOVERNMENT_SG_OR_AG ? 0.025 : 0.0;
        double probability = 0.006
                + reviewCase.solicitorGeneralSignal() * 0.045
                + reviewCase.publicAttention() * 0.008
                + reviewCase.lowerCourtSplitDepth() * 0.010
                + governmentCue;
        return random.nextDouble() < Values.clamp01(probability);
    }

    private static double certiorariGateScore(
            ReviewCase reviewCase,
            double preliminaryScore,
            boolean courtRequestedResponse,
            boolean cvsgRequested
    ) {
        double amicusSignal = Math.min(1.0, reviewCase.amicusBriefs() / 4.0);
        double base = reviewCase.petitionType() == PetitionType.IFP_CERT ? 0.006 : 0.030;
        double score = base
                + preliminaryScore * 0.16
                + (courtRequestedResponse ? 0.070 : 0.0)
                + (cvsgRequested ? 0.180 : 0.0)
                + reviewCase.solicitorGeneralSignal() * 0.050
                + amicusSignal * 0.035
                + reviewCase.barCapital() * 0.024
                + reviewCase.claimStrength() * 0.030
                + reviewCase.vehicleQuality() * 0.025
                + (reviewCase.genuineLowerCourtSplit() ? 0.045 : 0.0)
                - reviewCase.vehicleDefectRisk() * 0.030;
        return Values.clamp01(score);
    }

    private static boolean transferredToMerits(ReviewCase reviewCase, double admissionScore, Random random) {
        if (reviewCase.accessPath() == AccessPath.EMERGENCY_APPLICATION) {
            return random.nextDouble() < Values.clamp01(reviewCase.emergencyApplication().meritsFollowThroughProbability() + admissionScore * 0.22);
        }
        if (reviewCase.accessPath() == AccessPath.DIRECT_CONSTITUTIONAL_COMPLAINT
                || reviewCase.accessPath() == AccessPath.AMPARO) {
            return random.nextDouble() < Values.clamp01(0.42 + admissionScore * 0.36);
        }
        return random.nextDouble() < Values.clamp01(0.72 + admissionScore * 0.18 - reviewCase.preReviewSettlementPressure() * 0.10);
    }

    private static boolean paid(ReviewCase reviewCase) {
        return reviewCase.petitionType() == PetitionType.PAID_CERT;
    }

    private static boolean ifp(ReviewCase reviewCase) {
        return reviewCase.petitionType() == PetitionType.IFP_CERT;
    }

    private static boolean certiorariPath(ReviewCase reviewCase) {
        return reviewCase.accessPath() == AccessPath.DISCRETIONARY_CERTIORARI
                || reviewCase.accessPath() == AccessPath.PAID_CERTIORARI
                || reviewCase.accessPath() == AccessPath.IFP_CERTIORARI;
    }
}
