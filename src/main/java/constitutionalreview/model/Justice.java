package constitutionalreview.model;

public record Justice(
        int id,
        double ideology,
        double independence,
        double rightsSensitivity,
        double accountabilityPressure,
        double institutionalism,
        double partisanLoyalty,
        double emergencyDeference
) {
}
