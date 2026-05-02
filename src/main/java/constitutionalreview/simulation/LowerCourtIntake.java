package constitutionalreview.simulation;

import constitutionalreview.model.DocketType;
import constitutionalreview.model.ReviewCase;
import constitutionalreview.util.Values;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Random;

public final class LowerCourtIntake {
    private LowerCourtIntake() {
    }

    public static List<ReviewCase> selectForReview(List<ReviewCase> candidates, int targetCases, Random random) {
        List<ScoredCase> scored = new ArrayList<>();
        for (ReviewCase candidate : candidates) {
            scored.add(new ScoredCase(candidate, certScore(candidate, random)));
        }
        scored.sort(Comparator.comparingDouble(ScoredCase::score).reversed());
        List<ReviewCase> selected = new ArrayList<>();
        for (int i = 0; i < Math.min(targetCases, scored.size()); i++) {
            selected.add(scored.get(i).reviewCase().withId("case-" + (i + 1)));
        }
        return selected;
    }

    private static double certScore(ReviewCase reviewCase, Random random) {
        double emergencyBypass = reviewCase.docketType() == DocketType.EMERGENCY_STAY_APPLICATION ? 0.22 : 0.0;
        double amicusSignal = Math.min(1.0, reviewCase.amicusBriefs() / 4.0);
        double relistSignal = reviewCase.relistCount() >= 3 && reviewCase.relistCount() <= 4
                ? 0.18
                : reviewCase.relistCount() * 0.025;
        double score = reviewCase.certiorariPressure() * 0.30
                + reviewCase.lowerCourtConflict() * 0.20
                + reviewCase.lowerCourtErrorRisk() * 0.18
                + reviewCase.solicitorGeneralSignal() * 0.15
                + amicusSignal * 0.08
                + reviewCase.splitMaturity() * 0.06
                + relistSignal
                + (reviewCase.specialistCounsel() ? 0.04 : 0.0)
                + reviewCase.conditionalReversalProbability() * 0.06
                + reviewCase.rightsBurden() * 0.10
                + reviewCase.partisanSalience() * 0.08
                + reviewCase.publicAttention() * 0.06
                + reviewCase.emergencyPressure() * 0.06
                + emergencyBypass
                - reviewCase.vehicleDefectRisk() * 0.12
                + random.nextGaussian() * 0.035;
        return Values.clamp01(score);
    }

    private record ScoredCase(ReviewCase reviewCase, double score) {
    }
}
