package constitutionalreview.model;


public record EmergencyApplication(
		EmergencyApplicationClass applicationClass,
		EmergencyApplicantType applicantType,
		EmergencyApplicantType respondentType,
		EmergencyReliefType reliefRequested,
		boolean responseRequested,
		boolean referredToFullCourt,
		EmergencyStatusQuoEffect statusQuoEffect,
		double urgency,
		double publicDisagreementRisk,
		double meritsFollowThroughProbability
)
{
	public static EmergencyApplication none() {
		return new EmergencyApplication(
				EmergencyApplicationClass.NONE,
				EmergencyApplicantType.NONE,
				EmergencyApplicantType.NONE,
				EmergencyReliefType.NONE,
				false,
				false,
				EmergencyStatusQuoEffect.NONE,
				0.0,
				0.0,
				0.0
		);
	}
	
	public boolean present() {
		return applicationClass != EmergencyApplicationClass.NONE;
	}
}
