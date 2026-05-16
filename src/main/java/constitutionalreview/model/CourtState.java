package constitutionalreview.model;


import constitutionalreview.util.Values;


public final class CourtState
{
	private double precedentStability = 0.68;
	private double conflictLoad = 0.18;
	private double legislativeDefiance = 0.08;
	private double executiveEmergencyStrategy = 0.08;
	private double appointmentManipulationPressure = 0.06;
	private double overrideAdaptation = 0.06;
	private double repeatPlayerLearning = 0.10;
	private double emergencyIncentiveLearning = 0.08;
	private double complianceLearning = 0.58;
	
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
	
	public double repeatPlayerLearning() {
		return repeatPlayerLearning;
	}
	
	public double emergencyIncentiveLearning() {
		return emergencyIncentiveLearning;
	}
	
	public double complianceLearning() {
		return complianceLearning;
	}
	
	public void applyDecision(
			double precedentShift,
			double conflict,
			boolean invalidated,
			boolean emergencyDenied,
			boolean shadowRelief,
			boolean reasonedEmergencyOrder,
			boolean meritsAccelerated,
			boolean overrideAttempted,
			boolean overrideSuccessful,
			boolean rightsCarveoutBlocked,
			double publicAttention,
			double democraticMandate,
			double rightsBurden,
			double partisanSalience,
			double executiveDefianceRisk,
			double repeatPlayerAdvantage,
			double strategicPlaintiffSelection,
			double forumShoppingPressure,
			double lowerCourtCompliance,
			double enforcementCapacity,
			double emergencyDownstreamEffect,
			boolean governmentNoncompliance,
			boolean legislativeCompliance,
			boolean legislativeEvasion,
			boolean delayedReenactment,
			boolean executiveEmergencyFlood,
			boolean overrideCampaign,
			boolean appointmentPressureCampaign
	) {
		precedentStability = Values.clamp01(precedentStability + 0.04 - precedentShift * 0.22);
		conflictLoad = Values.clamp01(
				conflictLoad * 0.70
						+ conflict * 0.26
						+ emergencyDownstreamEffect * 0.04
						+ (governmentNoncompliance ? 0.05 : 0.0)
		);
		legislativeDefiance = Values.clamp01(
				legislativeDefiance * 0.66
						+ (invalidated ? democraticMandate * 0.14 + publicAttention * 0.08 : -0.02)
						+ (legislativeEvasion ? 0.08 : 0.0)
						- (legislativeCompliance ? 0.05 : 0.0)
						+ (overrideAttempted && !overrideSuccessful ? 0.07 : 0.0)
						- (overrideSuccessful ? 0.04 : 0.0)
						+ conflict * 0.06
						+ (governmentNoncompliance ? 0.07 : 0.0)
		);
		executiveEmergencyStrategy = Values.clamp01(
				executiveEmergencyStrategy * 0.68
						+ (emergencyDenied ? 0.16 : 0.0)
						+ (executiveEmergencyFlood ? 0.10 : 0.0)
						+ (shadowRelief ? 0.07 : 0.0)
						+ emergencyDownstreamEffect * 0.12
						+ (governmentNoncompliance ? 0.06 : 0.0)
						+ executiveDefianceRisk * 0.08
						+ partisanSalience * 0.04
		);
		appointmentManipulationPressure = Values.clamp01(
				appointmentManipulationPressure * 0.72
						+ conflict * 0.14
						+ partisanSalience * 0.08
						+ (appointmentPressureCampaign ? 0.10 : 0.0)
						+ (invalidated ? publicAttention * 0.06 : 0.0)
		);
		overrideAdaptation = Values.clamp01(
				overrideAdaptation * 0.64
						+ (invalidated ? democraticMandate * 0.06 : 0.0)
						+ (delayedReenactment ? 0.10 : 0.0)
						+ (overrideCampaign ? 0.06 : 0.0)
						+ (overrideAttempted && !overrideSuccessful ? 0.12 : 0.0)
						+ (rightsCarveoutBlocked ? rightsBurden * 0.16 : 0.0)
						- (overrideSuccessful ? 0.05 : 0.0)
		);
		repeatPlayerLearning = Values.clamp01(
				repeatPlayerLearning * 0.74
						+ repeatPlayerAdvantage * 0.12
						+ strategicPlaintiffSelection * 0.08
						+ forumShoppingPressure * 0.06
						+ (invalidated || shadowRelief ? publicAttention * 0.06 : 0.0)
						+ (governmentNoncompliance ? 0.04 : 0.0)
		);
		emergencyIncentiveLearning = Values.clamp01(
				emergencyIncentiveLearning * 0.70
						+ (shadowRelief ? 0.16 : 0.0)
						+ (emergencyDenied ? 0.06 : 0.0)
						+ emergencyDownstreamEffect * 0.16
						+ executiveDefianceRisk * 0.06
						+ repeatPlayerAdvantage * 0.04
						- (reasonedEmergencyOrder ? 0.08 : 0.0)
						- (meritsAccelerated ? 0.10 : 0.0)
		);
		complianceLearning = Values.clamp01(
				complianceLearning * 0.76
						+ lowerCourtCompliance * 0.10
						+ enforcementCapacity * 0.08
						+ (legislativeCompliance ? 0.07 : 0.0)
						- (governmentNoncompliance ? 0.12 : 0.0)
						- (legislativeEvasion ? 0.06 : 0.0)
						- conflict * 0.06
		);
	}
}
