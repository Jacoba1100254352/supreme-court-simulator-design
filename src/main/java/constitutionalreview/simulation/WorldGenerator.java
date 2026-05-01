package constitutionalreview.simulation;

import constitutionalreview.model.CaseType;
import constitutionalreview.model.CaseWorld;
import constitutionalreview.model.DocketType;
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
        DocketType[] docketTypes = DocketType.values();
        for (int i = 0; i < spec.cases(); i++) {
            CaseType type = types[random.nextInt(types.length)];
            DocketType docketType = docketType(type, docketTypes, spec, profile, random);
            LegalDomainProfile domain = LegalDomainProfile.forCase(type, docketType);
            double rightsTypeBoost = type == CaseType.RIGHTS || type == CaseType.ELECTIONS || docketType == DocketType.RIGHTS_CLAIM ? 0.18 : 0.0;
            double executiveBoost = type == CaseType.EXECUTIVE_POWER || docketType == DocketType.EXECUTIVE_POWER_DISPUTE ? 0.18 : 0.0;
            double electionBoost = docketType == DocketType.ELECTION_DISPUTE ? 0.16 : 0.0;
            double emergencyTypeBoost = docketType == DocketType.EMERGENCY_STAY_APPLICATION ? 0.22 : 0.0;
            double adminBoost = docketType == DocketType.ADMINISTRATIVE_LAW_CHALLENGE ? 0.10 : 0.0;
            double legalAmbiguity = Values.clamp01(0.20 + profile.volatility() * 0.35 + domain.legalAmbiguityShift() + random.nextDouble() * 0.48);
            double rightsBurden = Values.clamp01(0.10 + profile.rightsRisk() * 0.52 + rightsTypeBoost + electionBoost * 0.5 + domain.rightsBurdenShift() + random.nextGaussian() * 0.16);
            double democraticMandate = Values.clamp01(
                    0.35 + profile.publicLegitimacy() * 0.35 - profile.weakMandateRate() * 0.22 - electionBoost * 0.12 + domain.democraticMandateShift() + random.nextGaussian() * 0.16
            );
            double partisanSalience = Values.clamp01(0.12 + profile.partisanSkew() * 0.42 + profile.volatility() * 0.20 + electionBoost + domain.partisanSalienceShift() + random.nextDouble() * 0.25);
            double lawIdeology = random.nextBoolean() ? 1.0 : -1.0;
            lawIdeology = Values.clamp(lawIdeology * (0.25 + partisanSalience * 0.75), -1.0, 1.0);
            double emergencyPressure = Values.clamp01(spec.emergencyShare() * 0.55 + profile.volatility() * 0.20 + executiveBoost + electionBoost + emergencyTypeBoost + domain.emergencyPressureShift() + random.nextDouble() * 0.28);
            double requestedEmergencyRelief = Values.clamp01(emergencyPressure * 0.70 + executiveBoost * 0.20 + domain.requestedEmergencyReliefShift() + random.nextDouble() * 0.20);
            double defianceRisk = Values.clamp01(0.08 + executiveBoost + electionBoost * 0.6 + profile.partisanSkew() * 0.24 + domain.executiveDefianceRiskShift() + random.nextDouble() * 0.26);
            double legislativeQuality = Values.clamp01(profile.legalQuality() + random.nextGaussian() * 0.13 - profile.weakMandateRate() * 0.12 - adminBoost * 0.10 + domain.legislativeQualityShift());
            double conflictPotential = Values.clamp01(
                    0.12 + rightsBurden * 0.22 + partisanSalience * 0.32 + emergencyPressure * 0.12 + profile.overridePressure() * 0.22 + executiveBoost * 0.08 + domain.conflictPotentialShift()
            );
            double publicAttention = Values.clamp01(0.20 + rightsBurden * 0.20 + democraticMandate * 0.20 + partisanSalience * 0.22 + domain.publicAttentionShift() + random.nextDouble() * 0.24);
            double overridePressure = Values.clamp01(profile.overridePressure() * 0.42 + democraticMandate * 0.24 + publicAttention * 0.18 + partisanSalience * 0.16 + domain.overridePressureShift());
            docket.add(new ReviewCase(
                    "case-" + (i + 1),
                    type,
                    docketType,
                    legalAmbiguity,
                    rightsBurden,
                    democraticMandate,
                    partisanSalience,
                    lawIdeology,
                    emergencyPressure,
                    requestedEmergencyRelief,
                    defianceRisk,
                    legislativeQuality,
                    conflictPotential,
                    publicAttention,
                    overridePressure
            ));
        }
        return docket;
    }

    private static DocketType docketType(
            CaseType type,
            DocketType[] docketTypes,
            WorldSpec spec,
            LegislativeOutputProfile profile,
            Random random
    ) {
        double emergencyWeight = spec.emergencyShare() + profile.volatility() * 0.35;
        if (random.nextDouble() < emergencyWeight * 0.22) {
            return DocketType.EMERGENCY_STAY_APPLICATION;
        }
        if (type == CaseType.ELECTIONS) {
            return DocketType.ELECTION_DISPUTE;
        }
        if (type == CaseType.EXECUTIVE_POWER) {
            return DocketType.EXECUTIVE_POWER_DISPUTE;
        }
        if (type == CaseType.ADMINISTRATIVE_STATE) {
            return DocketType.ADMINISTRATIVE_LAW_CHALLENGE;
        }
        if (type == CaseType.RIGHTS || random.nextDouble() < profile.rightsRisk() * 0.35) {
            return DocketType.RIGHTS_CLAIM;
        }
        if (random.nextDouble() < 0.58) {
            return DocketType.FACIAL_CHALLENGE;
        }
        return docketTypes[random.nextBoolean() ? 1 : 0];
    }
}
