package constitutionalreview.simulation;

import constitutionalreview.model.LegislativeOutputProfile;

public record WorldSpec(
        int cases,
        int justicePoolSize,
        double polarization,
        double appointmentCapture,
        double publicPressure,
        double emergencyShare,
        LegislativeOutputProfile legislativeProfile
) {
    public static WorldSpec baseline(int cases, LegislativeOutputProfile profile) {
        return new WorldSpec(cases, 31, 0.52, 0.42, 0.45, 0.18, profile);
    }
}
