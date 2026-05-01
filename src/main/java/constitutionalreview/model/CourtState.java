package constitutionalreview.model;

import constitutionalreview.util.Values;

public final class CourtState {
    private double precedentStability = 0.68;
    private double conflictLoad = 0.18;

    public double precedentStability() {
        return precedentStability;
    }

    public double conflictLoad() {
        return conflictLoad;
    }

    public void applyDecision(double precedentShift, double conflict) {
        precedentStability = Values.clamp01(precedentStability + 0.04 - precedentShift * 0.22);
        conflictLoad = Values.clamp01(conflictLoad * 0.72 + conflict * 0.28);
    }
}
