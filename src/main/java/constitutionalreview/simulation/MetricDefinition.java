package constitutionalreview.simulation;

import constitutionalreview.util.Values;

import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public record MetricDefinition(
        String key,
        String label,
        MetricDirection direction,
        String note
) {
    private static final List<MetricDefinition> DEFINITIONS = List.of(
            new MetricDefinition("legalStability", "Legal stability", MetricDirection.HIGHER_IS_BETTER, "Precedent continuity and low conflict escalation."),
            new MetricDefinition("rightsProtection", "Rights protection", MetricDirection.HIGHER_IS_BETTER, "Protection of high-burden rights cases without treating every loss as a rights failure."),
            new MetricDefinition("partisanAlignment", "Partisan alignment", MetricDirection.LOWER_IS_BETTER, "Degree to which outcomes track the court's ideological direction in salient cases."),
            new MetricDefinition("shadowDocketAbuse", "Shadow-docket abuse", MetricDirection.LOWER_IS_BETTER, "Emergency or unexplained relief outside merits review."),
            new MetricDefinition("legitimacy", "Legitimacy", MetricDirection.HIGHER_IS_BETTER, "Reason-giving, recusal discipline, public attention, and low partisan odor."),
            new MetricDefinition("reversalRate", "Reversal rate", MetricDirection.LOWER_IS_BETTER, "Precedent or law reversal frequency."),
            new MetricDefinition("constitutionalConflict", "Constitutional conflict", MetricDirection.LOWER_IS_BETTER, "Institutional conflict after judicial action, cross-court disagreement, or override."),
            new MetricDefinition("democraticResponsiveness", "Democratic responsiveness", MetricDirection.HIGHER_IS_BETTER, "Respect for mandate and transparent override channels without collapsing rights protection."),
            new MetricDefinition("independenceAccountabilityBalance", "Independence/accountability balance", MetricDirection.HIGHER_IS_BETTER, "Combined score for low partisan alignment, responsive mandate handling, and rights protection."),
            new MetricDefinition("administrativeCost", "Administrative cost", MetricDirection.LOWER_IS_BETTER, "Procedural load from councils, cross-checking, panels, emergency processing, and en banc review."),
            new MetricDefinition("invalidationRate", "Invalidation rate", MetricDirection.DIAGNOSTIC, "Share of cases invalidating a law or government action."),
            new MetricDefinition("meritsReviewRate", "Merits review", MetricDirection.DIAGNOSTIC, "Share of cases resolved through merits review."),
            new MetricDefinition("courtRequestedResponseRate", "Court-requested response", MetricDirection.DIAGNOSTIC, "Intermediate screening stage before discretionary review or emergency disposition."),
            new MetricDefinition("cvsgRequestRate", "CVSG request", MetricDirection.DIAGNOSTIC, "Solicitor-General-views request as a high-salience gate signal."),
            new MetricDefinition("barCapital", "Bar capital", MetricDirection.DIAGNOSTIC, "Claimant-side appellate specialization and repeat-player legal capacity."),
            new MetricDefinition("claimStrength", "Claim strength", MetricDirection.DIAGNOSTIC, "Latent substantive constitutional merit distinct from vehicle quality."),
            new MetricDefinition("vehicleQuality", "Vehicle quality", MetricDirection.DIAGNOSTIC, "Record and procedural suitability distinct from underlying claim strength."),
            new MetricDefinition("genuineLowerCourtSplitRate", "Genuine split rate", MetricDirection.DIAGNOSTIC, "Share of filed matters with a modeled genuine lower-court split."),
            new MetricDefinition("settledBeforeReviewRate", "Pre-review settlement", MetricDirection.DIAGNOSTIC, "Share of admitted matters resolved before merits review."),
            new MetricDefinition("lowerCourtResistanceRisk", "Lower-court resistance", MetricDirection.LOWER_IS_BETTER, "Risk that lower courts narrow, delay, or resist implementation."),
            new MetricDefinition("forumShoppingPressure", "Forum-shopping pressure", MetricDirection.LOWER_IS_BETTER, "Strategic selection of procedural route or lower-court posture."),
            new MetricDefinition("enforcementCapacity", "Enforcement capacity", MetricDirection.HIGHER_IS_BETTER, "Administrative and political capacity to implement decisions."),
            new MetricDefinition("emergencyOpportunism", "Emergency opportunism", MetricDirection.LOWER_IS_BETTER, "Incentive to use emergency applications for interim advantage."),
            new MetricDefinition("emergencyOrderRate", "Emergency order rate", MetricDirection.DIAGNOSTIC, "Emergency docket activity."),
            new MetricDefinition("meritsAccelerationRate", "Merits acceleration", MetricDirection.DIAGNOSTIC, "Emergency cases pushed into merits review."),
            new MetricDefinition("recusalRate", "Recusal rate", MetricDirection.DIAGNOSTIC, "Conflict-screening intensity."),
            new MetricDefinition("justiceReplacementRate", "Justice replacement rate", MetricDirection.DIAGNOSTIC, "Appointment and replacement churn per case."),
            new MetricDefinition("concurrenceRate", "Concurrence rate", MetricDirection.DIAGNOSTIC, "Fragmentation in agreement."),
            new MetricDefinition("dissentRate", "Dissent rate", MetricDirection.DIAGNOSTIC, "Public disagreement inside the court."),
            new MetricDefinition("enBancRate", "En banc rate", MetricDirection.DIAGNOSTIC, "Full-court review rate."),
            new MetricDefinition("overrideAttemptRate", "Override attempt rate", MetricDirection.DIAGNOSTIC, "Legislative or popular override attempts."),
            new MetricDefinition("overrideRate", "Override rate", MetricDirection.DIAGNOSTIC, "Legislative or popular override activity.")
    );

    private static final Map<String, MetricDefinition> BY_KEY = DEFINITIONS.stream()
            .collect(Collectors.toUnmodifiableMap(MetricDefinition::key, Function.identity()));

    public static List<MetricDefinition> definitions() {
        return DEFINITIONS;
    }

    public static MetricDefinition require(String key) {
        MetricDefinition definition = BY_KEY.get(key);
        if (definition == null) {
            throw new IllegalArgumentException("Unknown metric: " + key);
        }
        return definition;
    }

    public static double higherIsBetter(double value) {
        return Values.clamp01(value);
    }

    public static double lowerIsBetter(double value) {
        return 1.0 - Values.clamp01(value);
    }
}
