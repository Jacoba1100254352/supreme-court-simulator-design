package constitutionalreview.model;

import constitutionalreview.util.Values;

public record LegislativeOutputProfile(
        String sourceName,
        double enactedVolume,
        double legalQuality,
        double weakMandateRate,
        double rightsRisk,
        double partisanSkew,
        double volatility,
        double publicLegitimacy,
        double overridePressure
) {
    public static LegislativeOutputProfile neutral() {
        return new LegislativeOutputProfile(
                "neutral synthetic legislature",
                0.45,
                0.62,
                0.22,
                0.20,
                0.28,
                0.24,
                0.58,
                0.22
        );
    }

    public LegislativeOutputProfile withSourceName(String sourceName) {
        return new LegislativeOutputProfile(
                sourceName,
                enactedVolume,
                legalQuality,
                weakMandateRate,
                rightsRisk,
                partisanSkew,
                volatility,
                publicLegitimacy,
                overridePressure
        );
    }

    public LegislativeOutputProfile blend(LegislativeOutputProfile other, double otherWeight) {
        double weight = Values.clamp01(otherWeight);
        double keep = 1.0 - weight;
        return new LegislativeOutputProfile(
                sourceName + " + " + other.sourceName,
                enactedVolume * keep + other.enactedVolume * weight,
                legalQuality * keep + other.legalQuality * weight,
                weakMandateRate * keep + other.weakMandateRate * weight,
                rightsRisk * keep + other.rightsRisk * weight,
                partisanSkew * keep + other.partisanSkew * weight,
                volatility * keep + other.volatility * weight,
                publicLegitimacy * keep + other.publicLegitimacy * weight,
                overridePressure * keep + other.overridePressure * weight
        );
    }

    public LegislativeOutputProfile normalized() {
        return new LegislativeOutputProfile(
                sourceName,
                Values.clamp01(enactedVolume),
                Values.clamp01(legalQuality),
                Values.clamp01(weakMandateRate),
                Values.clamp01(rightsRisk),
                Values.clamp01(partisanSkew),
                Values.clamp01(volatility),
                Values.clamp01(publicLegitimacy),
                Values.clamp01(overridePressure)
        );
    }
}
