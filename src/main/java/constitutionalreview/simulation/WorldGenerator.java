package constitutionalreview.simulation;


import constitutionalreview.model.*;
import constitutionalreview.util.Values;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;


public final class WorldGenerator
{
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
		List<ReviewCase> filings = new ArrayList<>();
		LegislativeOutputProfile profile = spec.legislativeProfile().normalized();
		DocketType[] docketTypes = DocketType.values();
		for (int i = 0; i < spec.cases(); i++) {
			CaseType type = caseType(spec, profile, random);
			DocketType docketType = docketType(type, docketTypes, spec, profile, random);
			AccessPath accessPath = accessPath(type, docketType, profile, random);
			ReviewTiming reviewTiming = reviewTiming(accessPath, docketType);
			PetitionType petitionType = petitionType(accessPath, random);
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
			double lowerCourtConflict = Values.clamp01(
					0.10 + legalAmbiguity * 0.22 + partisanSalience * 0.22 + conflictPotential * 0.20 + random.nextDouble() * 0.24
			);
			double lowerCourtErrorRisk = Values.clamp01(
					0.08 + (1.0 - legislativeQuality) * 0.24 + legalAmbiguity * 0.28 + rightsBurden * 0.12 + random.nextGaussian() * 0.10
			);
			double lowerCourtSplitDepth = Values.clamp01(
					lowerCourtConflict * 0.56
							+ legalAmbiguity * 0.18
							+ partisanSalience * 0.10
							+ publicAttention * 0.08
							+ random.nextGaussian() * 0.08
			);
			boolean genuineLowerCourtSplit = random.nextDouble() < Values.clamp01(
					0.06
							+ lowerCourtSplitDepth * 0.58
							+ lowerCourtConflict * 0.16
							+ legalAmbiguity * 0.05
			);
			double lowerCourtIdeologicalDrift = Values.clamp01(
					0.08
							+ spec.polarization() * 0.14
							+ partisanSalience * 0.18
							+ lowerCourtConflict * 0.16
							+ Math.abs(lawIdeology) * 0.08
							+ random.nextGaussian() * 0.08
			);
			double certiorariPressure = Values.clamp01(
					0.14
							+ lowerCourtConflict * 0.18
							+ lowerCourtSplitDepth * 0.18
							+ lowerCourtIdeologicalDrift * 0.06
							+ lowerCourtErrorRisk * 0.18
							+ publicAttention * 0.16
							+ emergencyPressure * 0.08
							+ domain.conflictPotentialShift()
			);
			ClaimantType claimantType = claimantType(type, docketType, rightsBurden, publicAttention, executiveBoost, adminBoost, random);
			double claimStrength = Values.clamp01(
					0.18
							+ rightsBurden * 0.22
							+ lowerCourtErrorRisk * 0.22
							+ (1.0 - legislativeQuality) * 0.18
							+ conflictPotential * 0.12
							+ (genuineLowerCourtSplit ? 0.05 : 0.0)
							+ random.nextGaussian() * 0.08
			);
			double barCapital = barCapital(claimantType, publicAttention, partisanSalience, executiveBoost, adminBoost, random);
			double solicitorGeneralSignal = solicitorGeneralSignal(type, docketType, publicAttention, executiveBoost, random);
			int amicusBriefs = amicusBriefs(publicAttention, partisanSalience, solicitorGeneralSignal, random);
			double splitMaturity = Values.clamp01(lowerCourtSplitDepth * 0.58 + lowerCourtConflict * 0.18 + legalAmbiguity * 0.12 + random.nextDouble() * 0.16);
			int relistCount = relistCount(certiorariPressure, solicitorGeneralSignal, amicusBriefs, random);
			boolean specialistCounsel = random.nextDouble() < Values.clamp01(0.08 + publicAttention * 0.18 + solicitorGeneralSignal * 0.14 + barCapital * 0.36);
			double vehicleQuality = Values.clamp01(
					0.38
							+ claimStrength * 0.20
							+ lowerCourtSplitDepth * 0.12
							+ (genuineLowerCourtSplit ? 0.08 : 0.0)
							+ barCapital * 0.16
							+ (specialistCounsel ? 0.08 : 0.0)
							- legalAmbiguity * 0.08
							+ random.nextGaussian() * 0.08
			);
			double strategicPlaintiffSelection = Values.clamp01(
					0.10
							+ publicAttention * 0.20
							+ partisanSalience * 0.20
							+ rightsBurden * 0.12
							+ emergencyPressure * 0.10
							+ (specialistCounsel ? 0.08 : 0.0)
							+ barCapital * 0.10
							+ random.nextGaussian() * 0.08
			);
			double forumShoppingPressure = Values.clamp01(
					0.08
							+ publicAttention * 0.14
							+ partisanSalience * 0.16
							+ rightsBurden * 0.10
							+ lowerCourtIdeologicalDrift * 0.16
							+ strategicPlaintiffSelection * 0.14
							+ barCapital * 0.05
							+ random.nextGaussian() * 0.07
			);
			double repeatPlayerAdvantage = Values.clamp01(
					0.12
							+ solicitorGeneralSignal * 0.24
							+ Math.min(1.0, amicusBriefs / 5.0) * 0.14
							+ (specialistCounsel ? 0.14 : 0.0)
							+ barCapital * 0.20
							+ executiveBoost * 0.12
							+ adminBoost * 0.08
							+ emergencyPressure * 0.08
							+ random.nextGaussian() * 0.07
			);
			double vehicleDefectRisk = Values.clamp01(
					0.30
							+ legalAmbiguity * 0.14
							- vehicleQuality * 0.28
							- legislativeQuality * 0.16
							- lowerCourtSplitDepth * 0.08
							- strategicPlaintiffSelection * 0.10
							- repeatPlayerAdvantage * 0.06
							+ random.nextGaussian() * 0.10
			);
			double conditionalReversalProbability = Values.clamp01(
					0.46
							+ claimStrength * 0.11
							+ vehicleQuality * 0.06
							+ lowerCourtErrorRisk * 0.16
							+ lowerCourtSplitDepth * 0.12
							+ Math.abs(lawIdeology) * partisanSalience * 0.08
							+ solicitorGeneralSignal * 0.08
							+ repeatPlayerAdvantage * 0.06
							- vehicleDefectRisk * 0.10
			);
			double governmentNoncomplianceRisk = Values.clamp01(
					defianceRisk * 0.42
							+ profile.weakMandateRate() * 0.14
							+ profile.overridePressure() * 0.12
							+ partisanSalience * 0.12
							+ emergencyPressure * 0.08
							+ repeatPlayerAdvantage * 0.08
			);
			double enforcementCapacity = Values.clamp01(
					0.56
							+ legislativeQuality * 0.18
							+ profile.publicLegitimacy() * 0.12
							- defianceRisk * 0.18
							- profile.weakMandateRate() * 0.10
							- conflictPotential * 0.08
							+ random.nextGaussian() * 0.07
			);
			double lowerCourtResistanceRisk = Values.clamp01(
					lowerCourtIdeologicalDrift * 0.28
							+ lowerCourtConflict * 0.12
							+ conflictPotential * 0.18
							+ governmentNoncomplianceRisk * 0.16
							+ partisanSalience * 0.10
							- enforcementCapacity * 0.18
							+ random.nextGaussian() * 0.06
			);
			double preReviewSettlementPressure = Values.clamp01(
					0.10
							+ lowerCourtErrorRisk * 0.10
							+ vehicleDefectRisk * 0.12
							+ repeatPlayerAdvantage * 0.10
							+ legalAmbiguity * 0.08
							+ enforcementCapacity * 0.06
							- rightsBurden * 0.10
							- publicAttention * 0.08
							- emergencyPressure * 0.12
							+ random.nextGaussian() * 0.06
			);
			double emergencyOpportunism = Values.clamp01(
					emergencyPressure * 0.24
							+ requestedEmergencyRelief * 0.12
							+ repeatPlayerAdvantage * 0.18
							+ strategicPlaintiffSelection * 0.16
							+ forumShoppingPressure * 0.10
							+ governmentNoncomplianceRisk * 0.10
							+ profile.volatility() * 0.08
			);
			double recusalIncentivePressure = Values.clamp01(
					partisanSalience * 0.32
							+ publicAttention * 0.18
							+ repeatPlayerAdvantage * 0.18
							+ emergencyPressure * 0.10
							+ Math.abs(lawIdeology) * 0.08
			);
			EmergencyApplication emergencyApplication = emergencyApplication(
					docketType,
					accessPath,
					emergencyPressure,
					requestedEmergencyRelief,
					executiveBoost,
					electionBoost,
					rightsBurden,
					publicAttention,
					random
			);
			filings.add(new ReviewCase(
					"filing-" + (i + 1),
					type,
					docketType,
					accessPath,
					reviewTiming,
					petitionType,
					claimantType,
					legalAmbiguity,
					rightsBurden,
					claimStrength,
					vehicleQuality,
					democraticMandate,
					partisanSalience,
					lawIdeology,
					emergencyPressure,
					requestedEmergencyRelief,
					defianceRisk,
					legislativeQuality,
					conflictPotential,
					publicAttention,
					overridePressure,
					lowerCourtConflict,
					lowerCourtErrorRisk,
					lowerCourtSplitDepth,
					genuineLowerCourtSplit,
					lowerCourtIdeologicalDrift,
					lowerCourtResistanceRisk,
					certiorariPressure,
					solicitorGeneralSignal,
					amicusBriefs,
					splitMaturity,
					relistCount,
					specialistCounsel,
					barCapital,
					vehicleDefectRisk,
					conditionalReversalProbability,
					forumShoppingPressure,
					preReviewSettlementPressure,
					strategicPlaintiffSelection,
					repeatPlayerAdvantage,
					governmentNoncomplianceRisk,
					enforcementCapacity,
					emergencyOpportunism,
					recusalIncentivePressure,
					emergencyApplication
			));
		}
		return filings;
	}
	
	private static AccessPath accessPath(CaseType type, DocketType docketType, LegislativeOutputProfile profile, Random random) {
		if (docketType == DocketType.EMERGENCY_STAY_APPLICATION) {
			return AccessPath.EMERGENCY_APPLICATION;
		}
		if (type == CaseType.ELECTIONS) {
			return random.nextDouble() < 0.70 ? AccessPath.ELECTORAL_REVIEW : AccessPath.EMERGENCY_APPLICATION;
		}
		if (type == CaseType.STRUCTURAL && random.nextDouble() < 0.42) {
			return random.nextBoolean() ? AccessPath.ABSTRACT_EX_ANTE_REVIEW : AccessPath.INTERBRANCH_DISPUTE;
		}
		if (type == CaseType.RIGHTS && random.nextDouble() < 0.24 + profile.rightsRisk() * 0.12) {
			return random.nextBoolean() ? AccessPath.DIRECT_CONSTITUTIONAL_COMPLAINT : AccessPath.AMPARO;
		}
		if (type == CaseType.ADMINISTRATIVE_STATE && random.nextDouble() < 0.34) {
			return AccessPath.COURT_REFERRAL_CONCRETE_REVIEW;
		}
		if (random.nextDouble() < 0.18) {
			return AccessPath.FILTERED_QPC;
		}
		double paidCertShare = Values.clamp01(
				0.326
						+ (profile.publicLegitimacy() - 0.58) * 0.03
						+ (profile.rightsRisk() - 0.20) * 0.03
						- (profile.weakMandateRate() - 0.22) * 0.02
		);
		return random.nextDouble() < paidCertShare ? AccessPath.PAID_CERTIORARI : AccessPath.IFP_CERTIORARI;
	}
	
	private static ReviewTiming reviewTiming(AccessPath accessPath, DocketType docketType) {
		if (accessPath == AccessPath.EMERGENCY_APPLICATION || docketType == DocketType.EMERGENCY_STAY_APPLICATION) {
			return ReviewTiming.EMERGENCY_INTERIM;
		}
		return switch (accessPath) {
			case ABSTRACT_EX_ANTE_REVIEW -> ReviewTiming.EX_ANTE_PRE_PROMULGATION;
			case ABSTRACT_EX_POST_REVIEW, INTERBRANCH_DISPUTE -> ReviewTiming.IMMEDIATE_POST_PROMULGATION_ABSTRACT;
			case COURT_REFERRAL_CONCRETE_REVIEW, FILTERED_QPC, DIRECT_CONSTITUTIONAL_COMPLAINT, AMPARO -> ReviewTiming.EX_POST_CONCRETE;
			case ELECTORAL_REVIEW -> ReviewTiming.IMMEDIATE_POST_PROMULGATION_ABSTRACT;
			case DISCRETIONARY_CERTIORARI, PAID_CERTIORARI, IFP_CERTIORARI -> ReviewTiming.LATE_EX_POST;
			case EMERGENCY_APPLICATION -> ReviewTiming.EMERGENCY_INTERIM;
		};
	}
	
	private static PetitionType petitionType(AccessPath accessPath, Random random) {
		return switch (accessPath) {
			case IFP_CERTIORARI -> PetitionType.IFP_CERT;
			case PAID_CERTIORARI, DISCRETIONARY_CERTIORARI -> PetitionType.PAID_CERT;
			case EMERGENCY_APPLICATION -> PetitionType.EMERGENCY_APPLICATION;
			case DIRECT_CONSTITUTIONAL_COMPLAINT, AMPARO -> PetitionType.CONSTITUTIONAL_COMPLAINT;
			case FILTERED_QPC, COURT_REFERRAL_CONCRETE_REVIEW -> PetitionType.FILTERED_REFERRAL;
			case ABSTRACT_EX_ANTE_REVIEW, ABSTRACT_EX_POST_REVIEW, INTERBRANCH_DISPUTE, ELECTORAL_REVIEW ->
					random.nextDouble() < 0.18 ? PetitionType.DIRECT_APPEAL : PetitionType.ABSTRACT_REFERRAL;
		};
	}
	
	private static ClaimantType claimantType(
			CaseType type,
			DocketType docketType,
			double rightsBurden,
			double publicAttention,
			double executiveBoost,
			double adminBoost,
			Random random
	) {
		double government = 0.06 + executiveBoost * 0.36 + adminBoost * 0.16 + (docketType == DocketType.ELECTION_DISPUTE ? 0.16 : 0.0);
		double business = 0.12 + (type == CaseType.ECONOMIC_REGULATION ? 0.24 : 0.0) + adminBoost * 0.12;
		double organizedRights = 0.10 + rightsBurden * 0.20 + publicAttention * 0.10;
		double expertClinic = 0.06 + rightsBurden * 0.08 + publicAttention * 0.08;
		double individual = Math.max(0.08, 1.0 - government - business - organizedRights - expertClinic);
		double total = government + business + organizedRights + expertClinic + individual;
		double draw = random.nextDouble() * total;
		if ((draw -= government) < 0.0) {
			return ClaimantType.GOVERNMENT_SG_OR_AG;
		}
		if ((draw -= business) < 0.0) {
			return ClaimantType.BUSINESS_REPEAT_PLAYER;
		}
		if ((draw -= organizedRights) < 0.0) {
			return ClaimantType.ORGANIZED_RIGHTS_GROUP;
		}
		if ((draw -= expertClinic) < 0.0) {
			return ClaimantType.EXPERT_BAR_CLINIC;
		}
		return ClaimantType.INDIVIDUAL_ONE_SHOT;
	}
	
	private static double barCapital(
			ClaimantType claimantType,
			double publicAttention,
			double partisanSalience,
			double executiveBoost,
			double adminBoost,
			Random random
	) {
		double base = switch (claimantType) {
			case INDIVIDUAL_ONE_SHOT -> 0.18;
			case ORGANIZED_RIGHTS_GROUP -> 0.52;
			case BUSINESS_REPEAT_PLAYER -> 0.62;
			case GOVERNMENT_SG_OR_AG -> 0.70 + executiveBoost * 0.10 + adminBoost * 0.06;
			case EXPERT_BAR_CLINIC -> 0.78;
		};
		return Values.clamp01(base + publicAttention * 0.10 + partisanSalience * 0.04 + random.nextGaussian() * 0.09);
	}
	
	private static double solicitorGeneralSignal(
			CaseType type, DocketType docketType, double publicAttention, double executiveBoost, Random random) {
		double base = 0.02 + executiveBoost * 0.42 + publicAttention * 0.10;
		if (type == CaseType.ADMINISTRATIVE_STATE || type == CaseType.EXECUTIVE_POWER || docketType == DocketType.EXECUTIVE_POWER_DISPUTE) {
			base += 0.16;
		}
		return random.nextDouble() < Values.clamp01(base)
				? Values.clamp01(0.45 + random.nextDouble() * 0.55)
				: 0.0;
	}
	
	private static int amicusBriefs(double publicAttention, double partisanSalience, double solicitorGeneralSignal, Random random) {
		double intensity = Values.clamp01(publicAttention * 0.48 + partisanSalience * 0.24 + solicitorGeneralSignal * 0.16);
		int briefs = 0;
		while (briefs < 8 && random.nextDouble() < intensity * Math.pow(0.70, briefs)) {
			briefs++;
		}
		return briefs;
	}
	
	private static int relistCount(double certiorariPressure, double solicitorGeneralSignal, int amicusBriefs, Random random) {
		double probability = Values.clamp01(certiorariPressure * 0.42 + solicitorGeneralSignal * 0.18 + Math.min(1.0, amicusBriefs / 4.0) * 0.12);
		int relists = 0;
		while (relists < 6 && random.nextDouble() < probability * Math.pow(0.68, relists)) {
			relists++;
		}
		return relists;
	}
	
	private static EmergencyApplication emergencyApplication(
			DocketType docketType,
			AccessPath accessPath,
			double emergencyPressure,
			double requestedEmergencyRelief,
			double executiveBoost,
			double electionBoost,
			double rightsBurden,
			double publicAttention,
			Random random
	) {
		if (docketType != DocketType.EMERGENCY_STAY_APPLICATION && accessPath != AccessPath.EMERGENCY_APPLICATION) {
			return EmergencyApplication.none();
		}
		EmergencyApplicationClass applicationClass;
		double draw = random.nextDouble();
		if (rightsBurden > 0.72 && draw < 0.18) {
			applicationClass = EmergencyApplicationClass.CAPITAL;
		} else if (draw < 0.28) {
			applicationClass = EmergencyApplicationClass.REFILED;
		} else if (draw < 0.86) {
			applicationClass = EmergencyApplicationClass.SUBSTANTIVE;
		} else {
			applicationClass = EmergencyApplicationClass.OTHER;
		}
		EmergencyApplicantType applicantType = executiveBoost > 0.12
				? EmergencyApplicantType.FEDERAL_GOVERNMENT
				: electionBoost > 0.10
				  ? EmergencyApplicantType.ELECTION_ACTOR
						: random.nextDouble() < 0.34
						  ? EmergencyApplicantType.STATE_GOVERNMENT
								: EmergencyApplicantType.PRIVATE_ORGANIZATION;
		EmergencyReliefType reliefType = requestedEmergencyRelief > 0.72
				? EmergencyReliefType.INJUNCTION
				: random.nextDouble() < 0.18
				  ? EmergencyReliefType.CERT_BEFORE_JUDGMENT
						: EmergencyReliefType.STAY;
		boolean responseRequested = random.nextDouble() < Values.clamp01(0.38 + publicAttention * 0.32);
		boolean referredToFullCourt = random.nextDouble() < Values.clamp01(0.24 + publicAttention * 0.26 + emergencyPressure * 0.20);
		EmergencyStatusQuoEffect statusQuoEffect = executiveBoost > 0.12
				? EmergencyStatusQuoEffect.PRESERVES_ENACTED_POLICY
				: requestedEmergencyRelief > 0.68
				  ? EmergencyStatusQuoEffect.ALTERS_STATUS_QUO
						: EmergencyStatusQuoEffect.UNCLEAR;
		return new EmergencyApplication(
				applicationClass,
				applicantType,
				EmergencyApplicantType.PRIVATE_ORGANIZATION,
				reliefType,
				responseRequested,
				referredToFullCourt,
				statusQuoEffect,
				Values.clamp01(emergencyPressure * 0.64 + requestedEmergencyRelief * 0.24),
				Values.clamp01(publicAttention * 0.34 + emergencyPressure * 0.22),
				Values.clamp01(0.10 + publicAttention * 0.16 + requestedEmergencyRelief * 0.14)
		);
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
	
	private static CaseType caseType(WorldSpec spec, LegislativeOutputProfile profile, Random random) {
		double rights = 0.20 + profile.rightsRisk() * 0.08;
		double structural = 0.16 + profile.partisanSkew() * 0.03;
		double elections = 0.04 + spec.publicPressure() * 0.03;
		double executive = 0.08 + spec.emergencyShare() * 0.07 + profile.volatility() * 0.03;
		double administrative = 0.17 + (1.0 - profile.legalQuality()) * 0.04;
		double economic = Math.max(0.10, 1.0 - rights - structural - elections - executive - administrative);
		double total = rights + structural + elections + executive + administrative + economic;
		double draw = random.nextDouble() * total;
		if ((draw -= rights) < 0.0) {
			return CaseType.RIGHTS;
		}
		if ((draw -= structural) < 0.0) {
			return CaseType.STRUCTURAL;
		}
		if ((draw -= elections) < 0.0) {
			return CaseType.ELECTIONS;
		}
		if ((draw -= executive) < 0.0) {
			return CaseType.EXECUTIVE_POWER;
		}
		if ((draw -= administrative) < 0.0) {
			return CaseType.ADMINISTRATIVE_STATE;
		}
		return CaseType.ECONOMIC_REGULATION;
	}
	
	public CaseWorld generate(WorldSpec spec, long seed) {
		Random random = new Random(seed);
		List<Justice> justices = generateJustices(spec, random);
		List<ReviewCase> docket = generateDocket(spec, random);
		return new CaseWorld(justices, docket, spec.legislativeProfile().normalized());
	}
}
