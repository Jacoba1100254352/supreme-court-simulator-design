package constitutionalreview.simulation;

import constitutionalreview.institution.CourtDesign;
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
            return new AdmissionDecision(false, false, false, false, paid(reviewCase), ifp(reviewCase), 0.0, reviewCase.conditionalReversalProbability());
        }

        double score = admissionScore(reviewCase, design);
        boolean admitted = random.nextDouble() < score;
        boolean transferredToMerits = admitted && transferredToMerits(reviewCase, score, random);
        return new AdmissionDecision(
                true,
                admitted,
                !admitted,
                transferredToMerits,
                paid(reviewCase),
                ifp(reviewCase),
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
                + reviewCase.publicAttention() * 0.08
                + reviewCase.solicitorGeneralSignal() * 0.06
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
        double designGatekeeping = design.appointmentFragmentation() > 2 ? 0.02 : 0.0;
        double score = 0.18
                + reviewCase.certiorariPressure() * 0.22
                + reviewCase.lowerCourtConflict() * 0.17
                + reviewCase.lowerCourtErrorRisk() * 0.10
                + reviewCase.solicitorGeneralSignal() * 0.15
                + amicusSignal * 0.10
                + reviewCase.splitMaturity() * 0.08
                + relistSignal * 0.07
                + (reviewCase.specialistCounsel() ? 0.05 : 0.0)
                + reviewCase.conditionalReversalProbability() * 0.08
                + pathAdjustment
                + designGatekeeping
                - reviewCase.vehicleDefectRisk() * 0.16
                + (design.vacancyDeadlockRisk() * -0.03);
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
        return random.nextDouble() < Values.clamp01(0.72 + admissionScore * 0.18);
    }

    private static boolean paid(ReviewCase reviewCase) {
        return reviewCase.petitionType() == PetitionType.PAID_CERT;
    }

    private static boolean ifp(ReviewCase reviewCase) {
        return reviewCase.petitionType() == PetitionType.IFP_CERT;
    }
}
