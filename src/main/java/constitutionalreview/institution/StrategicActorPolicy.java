package constitutionalreview.institution;


import constitutionalreview.model.CourtState;
import constitutionalreview.model.ReviewCase;
import constitutionalreview.util.Values;

import java.util.Random;


public final class StrategicActorPolicy
{
	private StrategicActorPolicy() {
	}
	
	public static StrategicResponse choose(ReviewCase reviewCase, CourtState state, CourtDesign design, Random random) {
		double politicalIncentive = Values.clamp01(
				reviewCase.democraticMandate() * 0.28
						+ reviewCase.publicAttention() * 0.22
						+ reviewCase.partisanSalience() * 0.24
						+ reviewCase.strategicPlaintiffSelection() * 0.08
						+ reviewCase.repeatPlayerAdvantage() * 0.06
						+ reviewCase.forumShoppingPressure() * 0.05
						+ reviewCase.lowerCourtResistanceRisk() * 0.06
						+ state.conflictLoad() * 0.16
						+ state.legislativeDefiance() * 0.10
		);
		double complianceProbability = Values.clamp01(
				0.68
						+ reviewCase.legislativeQuality() * 0.12
						+ reviewCase.enforcementCapacity() * 0.10
						- reviewCase.executiveDefianceRisk() * 0.16
						- reviewCase.governmentNoncomplianceRisk() * 0.12
						- reviewCase.lowerCourtResistanceRisk() * 0.08
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
						+ reviewCase.emergencyOpportunism() * 0.16
		);
		boolean appointmentPressure = random.nextDouble() < Values.clamp01(
				state.appointmentManipulationPressure() * 0.34
						+ state.conflictLoad() * 0.20
						+ reviewCase.publicAttention() * 0.16
						+ appointmentPressureAdjustment(design)
		);
		FormalLegalResponse formalResponse = formalResponse(
				comply,
				evade,
				reenact,
				overrideCampaign,
				politicalIncentive,
				reviewCase,
				state,
				design,
				random
		);
		PracticalImplementationResponse practicalResponse = practicalResponse(
				comply,
				evade,
				politicalIncentive,
				reviewCase,
				state,
				random
		);
		return new StrategicResponse(
				comply,
				evade,
				reenact,
				emergencyFlood,
				overrideCampaign,
				appointmentPressure,
				formalResponse,
				practicalResponse,
				emergencyFlood ? 0.11 + state.executiveEmergencyStrategy() * 0.10 : 0.0,
				overrideCampaign ? 0.12 + state.overrideAdaptation() * 0.12 : 0.0,
				comply ? 0.07 : -0.05
		);
	}
	
	private static double appointmentPressureAdjustment(CourtDesign design) {
		return switch (design.appointmentMethod()) {
			case PRESIDENT_SENATE -> 0.08;
			case JUDICIAL_ELECTORATE -> -0.10 - design.judicialElectorateInsulation() * 0.04;
			case NONPARTISAN_COMMISSION, LEGISLATIVE_SUPERMAJORITY, LOTTERY_FROM_APPELLATE_POOL, ROTATING_PANEL -> -0.04;
		};
	}
	
	private static FormalLegalResponse formalResponse(
			boolean comply,
			boolean evade,
			boolean reenact,
			boolean overrideCampaign,
			double politicalIncentive,
			ReviewCase reviewCase,
			CourtState state,
			CourtDesign design,
			Random random
	) {
		if (overrideCampaign
				&& design.overrideRule() != OverrideRule.NONE
				&& design.overrideRule() != OverrideRule.JURISDICTION_STRIPPING_CONSTRAINT) {
			return FormalLegalResponse.WEAK_FORM_OVERRIDE;
		}
		if (design.overrideRule() == OverrideRule.JURISDICTION_STRIPPING_CONSTRAINT
				&& state.conflictLoad() > 0.50
				&& random.nextDouble() < 0.08) {
			return FormalLegalResponse.REPLACEMENT_STATUTE;
		}
		if (politicalIncentive > 0.72 && state.conflictLoad() > 0.54 && random.nextDouble() < 0.18) {
			return FormalLegalResponse.CONSTITUTIONAL_AMENDMENT;
		}
		if (state.appointmentManipulationPressure() > 0.46
				&& design.overrideRule() != OverrideRule.JURISDICTION_STRIPPING_CONSTRAINT
				&& random.nextDouble() < 0.24) {
			return FormalLegalResponse.COURT_CURBING;
		}
		if (reenact) {
			return random.nextDouble() < reviewCase.legalAmbiguity()
					? FormalLegalResponse.NARROWED_REENACTMENT
					: FormalLegalResponse.REPLACEMENT_STATUTE;
		}
		if (evade) {
			return FormalLegalResponse.REPLACEMENT_STATUTE;
		}
		if (comply && reviewCase.rightsBurden() > 0.62 && random.nextDouble() < 0.30) {
			return FormalLegalResponse.REPEAL;
		}
		return comply ? FormalLegalResponse.ACQUIESCENT_COMPLIANCE : FormalLegalResponse.NONE;
	}
	
	private static PracticalImplementationResponse practicalResponse(
			boolean comply,
			boolean evade,
			double politicalIncentive,
			ReviewCase reviewCase,
			CourtState state,
			Random random
	) {
		double defiance = Values.clamp01(
				reviewCase.executiveDefianceRisk() * 0.38
						+ reviewCase.governmentNoncomplianceRisk() * 0.22
						+ reviewCase.lowerCourtResistanceRisk() * 0.16
						+ state.legislativeDefiance() * 0.24
						+ state.conflictLoad() * 0.18
						+ politicalIncentive * 0.12
						- reviewCase.enforcementCapacity() * 0.18
		);
		if (defiance > 0.78 && random.nextDouble() < defiance * 0.32) {
			return PracticalImplementationResponse.OPEN_NONCOMPLIANCE;
		}
		if (evade && random.nextDouble() < 0.50) {
			return PracticalImplementationResponse.ADMINISTRATIVE_SUBSTITUTION;
		}
		if (!comply && random.nextDouble() < Values.clamp01(defiance + 0.12)) {
			return PracticalImplementationResponse.SYMBOLIC_COMPLIANCE;
		}
		if (reviewCase.publicAttention() < 0.44 && random.nextDouble() < Values.clamp01(defiance + 0.10)) {
			return PracticalImplementationResponse.IMPLEMENTATION_DELAY;
		}
		if (defiance > 0.52 && random.nextDouble() < 0.22) {
			return PracticalImplementationResponse.BUREAUCRATIC_RESISTANCE;
		}
		return comply ? PracticalImplementationResponse.PROMPT_IMPLEMENTATION : PracticalImplementationResponse.NONE;
	}
	
	public record StrategicResponse(
			boolean legislativeCompliance,
			boolean legislativeEvasion,
			boolean delayedReenactment,
			boolean executiveEmergencyFlood,
			boolean overrideCampaign,
			boolean appointmentPressureCampaign,
			FormalLegalResponse formalResponse,
			PracticalImplementationResponse practicalImplementationResponse,
			double emergencyPressureDelta,
			double overridePressureDelta,
			double complianceDelta
	)
	{
	}
}
