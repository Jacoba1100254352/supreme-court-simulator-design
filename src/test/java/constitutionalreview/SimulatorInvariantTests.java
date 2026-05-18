package constitutionalreview;


import constitutionalreview.model.LegislativeOutputProfile;
import constitutionalreview.simulation.ScenarioCatalog;
import constitutionalreview.simulation.ScenarioReport;
import constitutionalreview.simulation.Simulator;
import constitutionalreview.simulation.WorldSpec;

import java.util.List;


public final class SimulatorInvariantTests
{
	private SimulatorInvariantTests() {
	}
	
	public static void run() {
		Simulator simulator = new Simulator();
		List<ScenarioReport> first = simulator.compare(
				ScenarioCatalog.defaultScenarios(),
				WorldSpec.baseline(20, LegislativeOutputProfile.neutral()),
				8,
				1234L
		);
		List<ScenarioReport> second = simulator.compare(
				ScenarioCatalog.defaultScenarios(),
				WorldSpec.baseline(20, LegislativeOutputProfile.neutral()),
				8,
				1234L
		);
		TestSupport.check(first.size() == second.size(), "deterministic runs should produce same report count");
		for (int i = 0; i < first.size(); i++) {
			ScenarioReport a = first.get(i);
			ScenarioReport b = second.get(i);
			TestSupport.check(a.scenarioKey().equals(b.scenarioKey()), "scenario order should be deterministic");
			TestSupport.check(Math.abs(a.directionalScore() - b.directionalScore()) < 0.000_000_1, "directional score should be deterministic");
			checkReport(a);
		}
	}
	
	private static void checkReport(ScenarioReport report) {
		TestSupport.check(report.totalCases() == 160, "total cases should equal runs * cases");
		TestSupport.checkUnitInterval(report.directionalScore(), "directionalScore");
		TestSupport.checkUnitInterval(report.certiorariPathRate(), "certiorariPathRate");
		TestSupport.checkUnitInterval(report.certiorariAdmissionRate(), "certiorariAdmissionRate");
		TestSupport.checkUnitInterval(report.courtRequestedResponseRate(), "courtRequestedResponseRate");
		TestSupport.checkUnitInterval(report.cvsgRequestRate(), "cvsgRequestRate");
		TestSupport.checkUnitInterval(report.paidCfrRequestRate(), "paidCfrRequestRate");
		TestSupport.checkUnitInterval(report.ifpCfrRequestRate(), "ifpCfrRequestRate");
		TestSupport.checkUnitInterval(report.lowerCourtSplitDepth(), "lowerCourtSplitDepth");
		TestSupport.checkUnitInterval(report.genuineLowerCourtSplitRate(), "genuineLowerCourtSplitRate");
		TestSupport.checkUnitInterval(report.lowerCourtIdeologicalDrift(), "lowerCourtIdeologicalDrift");
		TestSupport.checkUnitInterval(report.lowerCourtResistanceRisk(), "lowerCourtResistanceRisk");
		TestSupport.checkUnitInterval(report.barCapital(), "barCapital");
		TestSupport.checkUnitInterval(report.claimStrength(), "claimStrength");
		TestSupport.checkUnitInterval(report.vehicleQuality(), "vehicleQuality");
		TestSupport.checkUnitInterval(report.forumShoppingPressure(), "forumShoppingPressure");
		TestSupport.checkUnitInterval(report.preReviewSettlementPressure(), "preReviewSettlementPressure");
		TestSupport.checkUnitInterval(report.settledBeforeReviewRate(), "settledBeforeReviewRate");
		TestSupport.checkUnitInterval(report.strategicPlaintiffSelection(), "strategicPlaintiffSelection");
		TestSupport.checkUnitInterval(report.repeatPlayerAdvantage(), "repeatPlayerAdvantage");
		TestSupport.checkUnitInterval(report.repeatPlayerLearning(), "repeatPlayerLearning");
		TestSupport.checkUnitInterval(report.emergencyIncentiveLearning(), "emergencyIncentiveLearning");
		TestSupport.checkUnitInterval(report.complianceLearning(), "complianceLearning");
		TestSupport.checkUnitInterval(report.governmentNoncomplianceRisk(), "governmentNoncomplianceRisk");
		TestSupport.checkUnitInterval(report.governmentNoncomplianceRate(), "governmentNoncomplianceRate");
		TestSupport.checkUnitInterval(report.enforcementCapacity(), "enforcementCapacity");
		TestSupport.checkUnitInterval(report.emergencyOpportunism(), "emergencyOpportunism");
		TestSupport.checkUnitInterval(report.recusalIncentivePressure(), "recusalIncentivePressure");
		TestSupport.checkUnitInterval(report.legalStability(), "legalStability");
		TestSupport.checkUnitInterval(report.precedentStability(), "precedentStability");
		TestSupport.checkUnitInterval(report.statutoryStability(), "statutoryStability");
		TestSupport.checkUnitInterval(report.interbranchCompliance(), "interbranchCompliance");
		TestSupport.checkUnitInterval(report.rightsProtection(), "rightsProtection");
		TestSupport.checkUnitInterval(report.partisanAlignment(), "partisanAlignment");
		TestSupport.checkUnitInterval(report.shadowDocketAbuse(), "shadowDocketAbuse");
		TestSupport.checkUnitInterval(report.emergencyLegitimacyRisk(), "emergencyLegitimacyRisk");
		TestSupport.checkUnitInterval(report.legitimacy(), "legitimacy");
		TestSupport.checkUnitInterval(report.reversalRate(), "reversalRate");
		TestSupport.checkUnitInterval(report.constitutionalConflict(), "constitutionalConflict");
		TestSupport.checkUnitInterval(report.democraticResponsiveness(), "democraticResponsiveness");
		TestSupport.checkUnitInterval(report.administrativeCost(), "administrativeCost");
		TestSupport.checkUnitInterval(report.strategicPressure(), "strategicPressure");
		TestSupport.checkUnitInterval(report.legislativeDefiance(), "legislativeDefiance");
		TestSupport.checkUnitInterval(report.executiveEmergencyStrategy(), "executiveEmergencyStrategy");
		TestSupport.checkUnitInterval(report.appointmentManipulationPressure(), "appointmentManipulationPressure");
		TestSupport.checkUnitInterval(report.overrideAdaptation(), "overrideAdaptation");
		TestSupport.checkUnitInterval(report.legislativeComplianceRate(), "legislativeComplianceRate");
		TestSupport.checkUnitInterval(report.legislativeEvasionRate(), "legislativeEvasionRate");
		TestSupport.checkUnitInterval(report.delayedReenactmentStrategyRate(), "delayedReenactmentStrategyRate");
		TestSupport.checkUnitInterval(report.executiveEmergencyFloodRate(), "executiveEmergencyFloodRate");
		TestSupport.checkUnitInterval(report.overrideCampaignRate(), "overrideCampaignRate");
		TestSupport.checkUnitInterval(report.appointmentPressureCampaignRate(), "appointmentPressureCampaignRate");
		TestSupport.checkUnitInterval(report.meritsAccelerationRate(), "meritsAccelerationRate");
		TestSupport.checkUnitInterval(report.justiceReplacementRate(), "justiceReplacementRate");
		TestSupport.checkUnitInterval(report.overrideAttemptRate(), "overrideAttemptRate");
		TestSupport.checkUnitInterval(report.constitutionalRemandRate(), "constitutionalRemandRate");
		TestSupport.checkUnitInterval(report.publicInterestFilteredRate(), "publicInterestFilteredRate");
		TestSupport.checkUnitInterval(report.rightsCarveoutBlockRate(), "rightsCarveoutBlockRate");
		TestSupport.checkUnitInterval(report.concurrenceRate(), "concurrenceRate");
		TestSupport.checkUnitInterval(report.dissentRate(), "dissentRate");
		double claimantTypeTotal = report.individualOneShotClaimantRate() + report.organizedRightsClaimantRate()
				+ report.businessRepeatPlayerClaimantRate() + report.governmentClaimantRate()
				+ report.expertBarClinicClaimantRate();
		TestSupport.check(Math.abs(claimantTypeTotal - 1.0) < 0.000_000_1, "claimant type rates should sum to one");
		TestSupport.checkUnitInterval(report.rightsClaimantCaseRate(), "rightsClaimantCaseRate");
		TestSupport.checkUnitInterval(report.rightsClaimantSuccess(), "rightsClaimantSuccess");
		TestSupport.check(
				report.rightsClaimantSuccess() <= report.rightsClaimantCaseRate() + 0.000_000_1,
				"aggregate claimant success should not exceed claimant case share"
		);
		TestSupport.checkUnitInterval(report.rightsDomainClaimantSuccess(), "rightsDomainClaimantSuccess");
		TestSupport.checkUnitInterval(report.emergencyRightsClaimantSuccess(), "emergencyRightsClaimantSuccess");
		TestSupport.checkUnitInterval(report.structuralDomainClaimantSuccess(), "structuralDomainClaimantSuccess");
		TestSupport.checkUnitInterval(report.electionDomainClaimantSuccess(), "electionDomainClaimantSuccess");
		TestSupport.checkUnitInterval(report.executivePowerDomainClaimantSuccess(), "executivePowerDomainClaimantSuccess");
		TestSupport.checkUnitInterval(report.administrativeDomainClaimantSuccess(), "administrativeDomainClaimantSuccess");
		TestSupport.checkUnitInterval(report.economicDomainClaimantSuccess(), "economicDomainClaimantSuccess");
		TestSupport.checkUnitInterval(report.precedentDurability(), "precedentDurability");
		TestSupport.checkUnitInterval(report.emergencyDownstreamEffect(), "emergencyDownstreamEffect");
		TestSupport.checkUnitInterval(report.lowerCourtCompliance(), "lowerCourtCompliance");
		double docketTypeTotal = report.facialChallengeRate() + report.asAppliedChallengeRate() + report.electionDisputeRate()
				+ report.emergencyStayDocketRate() + report.executivePowerDisputeRate() + report.administrativeLawRate()
				+ report.rightsClaimRate();
		TestSupport.check(Math.abs(docketTypeTotal - 1.0) < 0.000_000_1, "docket type rates should sum to one");
	}
}
