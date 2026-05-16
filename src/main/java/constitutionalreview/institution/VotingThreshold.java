package constitutionalreview.institution;


public enum VotingThreshold
{
	SIMPLE_MAJORITY(0.50),
	SIXTY_PERCENT(0.60),
	TWO_THIRDS(2.0 / 3.0),
	RIGHTS_SUPERMAJORITY(0.60);
	
	private final double defaultShare;
	
	VotingThreshold(double defaultShare) {
		this.defaultShare = defaultShare;
	}
	
	public double requiredShare(boolean highRightsBurden) {
		if (this == RIGHTS_SUPERMAJORITY && highRightsBurden) {
			return 2.0 / 3.0;
		}
		return defaultShare;
	}
}
