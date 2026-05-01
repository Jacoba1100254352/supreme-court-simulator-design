package constitutionalreview.institution;

import constitutionalreview.model.CourtState;
import constitutionalreview.model.ReviewCase;
import constitutionalreview.util.Values;

import java.util.Random;

public final class StrategicActorPolicy {
    private StrategicActorPolicy() {
    }

    public static StrategicResponse choose(ReviewCase reviewCase, CourtState state, CourtDesign design, Random random) {
        double politicalIncentive = Values.clamp01(
                reviewCase.democraticMandate() * 0.28
                        + reviewCase.publicAttention() * 0.22
                        + reviewCase.partisanSalience() * 0.24
                        + state.conflictLoad() * 0.16
                        + state.legislativeDefiance() * 0.10
        );
        double complianceProbability = Values.clamp01(
                0.68
                        + reviewCase.legislativeQuality() * 0.12
                        - reviewCase.executiveDefianceRisk() * 0.16
                        - state.legislativeDefiance() * 0.20
                        - state.overrideAdaptation() * 0.10
        );
        boolean comply = random.nextDouble() < complianceProbability;
        boolean evade = !comply && random.nextDouble() < Values.clamp01(politicalIncentive + state.overrideAdaptation() * 0.25);
        boolean reenact = evade && random.nextDouble() < Values.clamp01(reviewCase.overridePressure() * 0.55 + state.overrideAdaptation() * 0.35);
        boolean overrideCampaign = random.nextDouble() < Values.clamp01(
                reviewCase.overridePressure() * 0.36
                        + politicalIncentive * 0.26
                        + state.overrideAdaptation() * 0.22
                        - reviewCase.rightsBurden() * 0.18
        );
        boolean emergencyFlood = random.nextDouble() < Values.clamp01(
                reviewCase.emergencyPressure() * 0.34
                        + reviewCase.executiveDefianceRisk() * 0.24
                        + state.executiveEmergencyStrategy() * 0.28
                        + reviewCase.partisanSalience() * 0.10
        );
        boolean appointmentPressure = random.nextDouble() < Values.clamp01(
                state.appointmentManipulationPressure() * 0.34
                        + state.conflictLoad() * 0.20
                        + reviewCase.publicAttention() * 0.16
                        + (design.appointmentMethod() == AppointmentMethod.PRESIDENT_SENATE ? 0.08 : -0.04)
        );
        return new StrategicResponse(
                comply,
                evade,
                reenact,
                emergencyFlood,
                overrideCampaign,
                appointmentPressure,
                emergencyFlood ? 0.11 + state.executiveEmergencyStrategy() * 0.10 : 0.0,
                overrideCampaign ? 0.12 + state.overrideAdaptation() * 0.12 : 0.0,
                comply ? 0.07 : -0.05
        );
    }

    public record StrategicResponse(
            boolean legislativeCompliance,
            boolean legislativeEvasion,
            boolean delayedReenactment,
            boolean executiveEmergencyFlood,
            boolean overrideCampaign,
            boolean appointmentPressureCampaign,
            double emergencyPressureDelta,
            double overridePressureDelta,
            double complianceDelta
    ) {
    }
}
