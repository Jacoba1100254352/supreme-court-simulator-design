package constitutionalreview.simulation;


public record AdmissionDecision(
		boolean petitionFiled,
		boolean admitted,
		boolean screenedOut,
		boolean transferredToMerits,
		boolean paidPetition,
		boolean ifpPetition,
		boolean courtRequestedResponse,
		boolean cvsgRequested,
		double admissionScore,
		double conditionalReversalProbability
)
{
}
