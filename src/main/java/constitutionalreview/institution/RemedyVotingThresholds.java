package constitutionalreview.institution;


public record RemedyVotingThresholds(
		double ordinaryMeritsShare,
		double lawStrikeShare,
		double rightsClaimShare,
		double emergencyReliefShare,
		double precedentOverruleShare,
		double impeachmentShare
)
{
	public RemedyVotingThresholds {
		ordinaryMeritsShare = clampShare(ordinaryMeritsShare);
		lawStrikeShare = clampShare(lawStrikeShare);
		rightsClaimShare = clampShare(rightsClaimShare);
		emergencyReliefShare = clampShare(emergencyReliefShare);
		precedentOverruleShare = clampShare(precedentOverruleShare);
		impeachmentShare = clampShare(impeachmentShare);
	}
	
	public static RemedyVotingThresholds from(VotingThreshold votingThreshold) {
		double ordinary = votingThreshold.requiredShare(false);
		double rights = votingThreshold.requiredShare(true);
		return new RemedyVotingThresholds(
				ordinary,
				ordinary,
				rights,
				Math.max(ordinary, 0.50),
				Math.max(ordinary, 0.60),
				Math.max(ordinary, 0.67)
		);
	}
	
	private static double clampShare(double share) {
		if (Double.isNaN(share)) {
			return 0.50;
		}
		return Math.max(0.0, Math.min(1.0, share));
	}
}
