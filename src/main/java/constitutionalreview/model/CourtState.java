package constitutionalreview.model;

import constitutionalreview.util.Values;

public final class CourtState {
    private double precedentStability = 0.68;
    private double conflictLoad = 0.18;
    private double legislativeDefiance = 0.08;
    private double executiveEmergencyStrategy = 0.08;
    private double appointmentManipulationPressure = 0.06;
    private double overrideAdaptation = 0.06;

    public double precedentStability() {
        return precedentStability;
    }

    public double conflictLoad() {
        return conflictLoad;
    }

    public double legislativeDefiance() {
        return legislativeDefiance;
    }

    public double executiveEmergencyStrategy() {
        return executiveEmergencyStrategy;
    }

    public double appointmentManipulationPressure() {
        return appointmentManipulationPressure;
    }

    public double overrideAdaptation() {
        return overrideAdaptation;
    }

    public void applyDecision(
            double precedentShift,
            double conflict,
            boolean invalidated,
            boolean emergencyDenied,
            boolean shadowRelief,
            boolean overrideAttempted,
            boolean overrideSuccessful,
            boolean rightsCarveoutBlocked,
            double publicAttention,
            double democraticMandate,
            double rightsBurden,
            double partisanSalience,
            double executiveDefianceRisk
    ) {
        precedentStability = Values.clamp01(precedentStability + 0.04 - precedentShift * 0.22);
        conflictLoad = Values.clamp01(conflictLoad * 0.72 + conflict * 0.28);
        legislativeDefiance = Values.clamp01(
                legislativeDefiance * 0.66
                        + (invalidated ? democraticMandate * 0.14 + publicAttention * 0.08 : -0.02)
                        + (overrideAttempted && !overrideSuccessful ? 0.07 : 0.0)
                        - (overrideSuccessful ? 0.04 : 0.0)
                        + conflict * 0.06
        );
        executiveEmergencyStrategy = Values.clamp01(
                executiveEmergencyStrategy * 0.68
                        + (emergencyDenied ? 0.16 : 0.0)
                        + (shadowRelief ? 0.07 : 0.0)
                        + executiveDefianceRisk * 0.08
                        + partisanSalience * 0.04
        );
        appointmentManipulationPressure = Values.clamp01(
                appointmentManipulationPressure * 0.72
                        + conflict * 0.14
                        + partisanSalience * 0.08
                        + (invalidated ? publicAttention * 0.06 : 0.0)
        );
        overrideAdaptation = Values.clamp01(
                overrideAdaptation * 0.64
                        + (invalidated ? democraticMandate * 0.06 : 0.0)
                        + (overrideAttempted && !overrideSuccessful ? 0.12 : 0.0)
                        + (rightsCarveoutBlocked ? rightsBurden * 0.16 : 0.0)
                        - (overrideSuccessful ? 0.05 : 0.0)
        );
    }
}
