package constitutionalreview.institution;


import constitutionalreview.model.EmergencyMeritsFollowThrough;


public record EmergencyOrder(
		boolean granted,
		boolean explanationProvided,
		boolean voteDisclosed,
		int publicDisagreementCount,
		EmergencyMeritsFollowThrough meritsFollowThrough,
		double abuseScore,
		double legitimacyRisk
)
{
	public static EmergencyOrder none() {
		return new EmergencyOrder(false, false, false, 0, EmergencyMeritsFollowThrough.NONE, 0.0, 0.0);
	}
}
