package constitutionalreview.institution;


public enum JudicialNomineePool
{
	NOT_APPLICABLE(
			"Not applicable",
			0.0,
			0.0,
			0.0,
			0.0,
			0.0
	),
	OPEN_TO_QUALIFIED_LAWYERS(
			"Open to qualified lawyers",
			0.44,
			1.00,
			0.30,
			0.55,
			0.05
	),
	SITTING_FEDERAL_JUDGES(
			"Sitting federal judges",
			0.76,
			0.62,
			0.22,
			0.58,
			0.04
	),
	FEDERAL_APPELLATE_JUDGES(
			"Federal appellate judges",
			0.86,
			0.30,
			0.18,
			0.62,
			0.03
	),
	STATE_HIGH_COURT_JUDGES(
			"State high-court judges",
			0.74,
			0.48,
			0.28,
			0.64,
			0.04
	),
	FEDERAL_AND_STATE_HIGH_COURT_JUDGES(
			"Federal and state high-court judges",
			0.80,
			0.74,
			0.20,
			0.66,
			0.06
	);
	
	private final String label;
	private final double professionalFilter;
	private final double candidateBreadth;
	private final double pipelineIdeologyRisk;
	private final double rightsPracticeExposure;
	private final double administrativeCost;
	
	JudicialNomineePool(
			String label,
			double professionalFilter,
			double candidateBreadth,
			double pipelineIdeologyRisk,
			double rightsPracticeExposure,
			double administrativeCost
	) {
		this.label = label;
		this.professionalFilter = professionalFilter;
		this.candidateBreadth = candidateBreadth;
		this.pipelineIdeologyRisk = pipelineIdeologyRisk;
		this.rightsPracticeExposure = rightsPracticeExposure;
		this.administrativeCost = administrativeCost;
	}
	
	public String label() {
		return label;
	}
	
	public double professionalFilter() {
		return professionalFilter;
	}
	
	public double candidateBreadth() {
		return candidateBreadth;
	}
	
	public double pipelineIdeologyRisk() {
		return pipelineIdeologyRisk;
	}
	
	public double rightsPracticeExposure() {
		return rightsPracticeExposure;
	}
	
	public double administrativeCost() {
		return administrativeCost;
	}
}
