package constitutionalreview.simulation;

import constitutionalreview.model.CaseType;
import constitutionalreview.model.CaseWorld;
import constitutionalreview.model.Justice;
import constitutionalreview.model.LegislativeOutputProfile;
import constitutionalreview.model.ReviewCase;
import constitutionalreview.util.Values;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public final class WorldGenerator {
    public CaseWorld generate(WorldSpec spec, long seed) {
        Random random = new Random(seed);
        List<Justice> justices = generateJustices(spec, random);
        List<ReviewCase> docket = generateDocket(spec, random);
        return new CaseWorld(justices, docket, spec.legislativeProfile().normalized());
    }

    private static List<Justice> generateJustices(WorldSpec spec, Random random) {
        List<Justice> justices = new ArrayList<>();
        for (int i = 0; i < spec.justicePoolSize(); i++) {
            double ideologicalCamp = i % 2 == 0 ? -1.0 : 1.0;
            double ideology = Values.clamp(
                    ideologicalCamp * (0.22 + spec.polarization() * 0.60) + random.nextGaussian() * 0.22,
                    -1.0,
                    1.0
            );
            double independence = Values.clamp01(0.64 - spec.appointmentCapture() * 0.28 + random.nextGaussian() * 0.12);
            double rightsSensitivity = Values.clamp01(0.55 + random.nextGaussian() * 0.18);
            double accountability = Values.clamp01(spec.publicPressure() * 0.55 + random.nextDouble() * 0.35);
            double institutionalism = Values.clamp01(0.58 + random.nextGaussian() * 0.15);
            double partisanLoyalty = Values.clamp01(spec.appointmentCapture() * 0.58 + random.nextDouble() * 0.25);
            double emergencyDeference = Values.clamp01(0.44 + spec.emergencyShare() * 0.35 + random.nextGaussian() * 0.13);
            justices.add(new Justice(
                    i,
                    ideology,
                    independence,
                    rightsSensitivity,
                    accountability,
                    institutionalism,
                    partisanLoyalty,
                    emergencyDeference
            ));
        }
        return justices;
    }

    private static List<ReviewCase> generateDocket(WorldSpec spec, Random random) {
        List<ReviewCase> docket = new ArrayList<>();
        LegislativeOutputProfile profile = spec.legislativeProfile().normalized();
        CaseType[] types = CaseType.values();
        for (int i = 0; i < spec.cases(); i++) {
            CaseType type = types[random.nextInt(types.length)];
            double rightsTypeBoost = type == CaseType.RIGHTS || type == CaseType.ELECTIONS ? 0.18 : 0.0;
            double executiveBoost = type == CaseType.EXECUTIVE_POWER ? 0.18 : 0.0;
            double legalAmbiguity = Values.clamp01(0.20 + profile.volatility() * 0.35 + random.nextDouble() * 0.48);
            double rightsBurden = Values.clamp01(0.10 + profile.rightsRisk() * 0.52 + rightsTypeBoost + random.nextGaussian() * 0.16);
            double democraticMandate = Values.clamp01(
                    0.35 + profile.publicLegitimacy() * 0.35 - profile.weakMandateRate() * 0.22 + random.nextGaussian() * 0.16
            );
            double partisanSalience = Values.clamp01(0.12 + profile.partisanSkew() * 0.42 + profile.volatility() * 0.20 + random.nextDouble() * 0.25);
            double lawIdeology = random.nextBoolean() ? 1.0 : -1.0;
            lawIdeology = Values.clamp(lawIdeology * (0.25 + partisanSalience * 0.75), -1.0, 1.0);
            double emergencyPressure = Values.clamp01(spec.emergencyShare() * 0.55 + profile.volatility() * 0.20 + executiveBoost + random.nextDouble() * 0.28);
            double defianceRisk = Values.clamp01(0.08 + executiveBoost + profile.partisanSkew() * 0.24 + random.nextDouble() * 0.26);
            double legislativeQuality = Values.clamp01(profile.legalQuality() + random.nextGaussian() * 0.13 - profile.weakMandateRate() * 0.12);
            double conflictPotential = Values.clamp01(
                    0.12 + rightsBurden * 0.22 + partisanSalience * 0.32 + emergencyPressure * 0.12 + profile.overridePressure() * 0.22
            );
            double publicAttention = Values.clamp01(0.20 + rightsBurden * 0.20 + democraticMandate * 0.20 + partisanSalience * 0.22 + random.nextDouble() * 0.24);
            docket.add(new ReviewCase(
                    "case-" + (i + 1),
                    type,
                    legalAmbiguity,
                    rightsBurden,
                    democraticMandate,
                    partisanSalience,
                    lawIdeology,
                    emergencyPressure,
                    defianceRisk,
                    legislativeQuality,
                    conflictPotential,
                    publicAttention
            ));
        }
        return docket;
    }
}
