package constitutionalreview.simulation;

public record AdmissionDecision(
        boolean petitionFiled,
        boolean admitted,
        boolean screenedOut,
        boolean transferredToMerits,
        boolean paidPetition,
        boolean ifpPetition,
        double admissionScore,
        double conditionalReversalProbability
) {
}
