package constitutionalreview;


import constitutionalreview.institution.*;
import constitutionalreview.simulation.Scenario;
import constitutionalreview.simulation.ScenarioCatalog;

import java.util.List;


public final class ScenarioCatalogTests
{
	private ScenarioCatalogTests() {
	}
	
	public static void run() {
		List<String> keys = ScenarioCatalog.scenarioKeys();
		TestSupport.check(keys.contains("current-us-like"), "catalog should include current-us-like");
		TestSupport.check(keys.contains("cross-checking-courts"), "catalog should include cross-checking-courts");
		TestSupport.check(keys.contains("constitutional-council"), "catalog should include constitutional-council");
		TestSupport.check(keys.contains("judicial-electorate-selection"), "catalog should include judicial-electorate-selection");
		TestSupport.check(keys.contains("judicial-electorate-all-federal"), "catalog should include all-federal judicial electorate variant");
		TestSupport.check(keys.contains("judicial-electorate-appellate-only"), "catalog should include appellate-only judicial electorate variant");
		TestSupport.check(keys.contains("judicial-electorate-selected-circuits"), "catalog should include selected-circuits judicial electorate variant");
		TestSupport.check(keys.contains("judicial-electorate-state-high-courts"), "catalog should include state-high-court judicial electorate variant");
		TestSupport.check(keys.contains("randomized-merits-panels"), "catalog should include randomized-merits-panels");
		TestSupport.check(keys.contains("mandatory-written-emergency-reasoning"), "catalog should include mandatory-written-emergency-reasoning");
		TestSupport.check(keys.contains("automatic-merits-follow-up"), "catalog should include automatic-merits-follow-up");
		TestSupport.check(keys.contains("strong-recusal-enforcement"), "catalog should include strong-recusal-enforcement");
		TestSupport.check(keys.contains("jurisdiction-stripping-constraints"), "catalog should include jurisdiction-stripping-constraints");
		TestSupport.check(keys.contains("legislative-override-window"), "catalog should include legislative-override-window");
		TestSupport.check(keys.contains("constitutional-remand"), "catalog should include constitutional-remand");
		TestSupport.check(keys.contains("public-interest-litigation-filter"), "catalog should include public-interest-litigation-filter");
		TestSupport.check(keys.contains("emergency-integrity-package"), "catalog should include emergency-integrity-package");
		TestSupport.check(keys.contains("remand-override-window-package"), "catalog should include remand-override-window-package");
		TestSupport.check(keys.contains("panel-jurisdiction-safeguards"), "catalog should include panel-jurisdiction-safeguards");
		TestSupport.check(keys.contains("council-concrete-hybrid"), "catalog should include council-concrete-hybrid");
		List<Scenario> scenarios = ScenarioCatalog.scenariosForKeys(keys);
		TestSupport.check(scenarios.size() == keys.size(), "every scenario key should resolve");
		TestSupport.check(ScenarioCatalog.defaultScenarios().size() >= 10, "default scenario set should be broad");
		CourtDesign design = judicialElectorateDesign(
				JudicialSelectorPool.ALL_FEDERAL_JUDGES,
				JudicialNomineePool.FEDERAL_APPELLATE_JUDGES
		);
		TestSupport.check(design.usesJudicialElectorate(), "judicial electorate design should report its appointment mode");
		TestSupport.check(design.judicialSelectorPool() == JudicialSelectorPool.ALL_FEDERAL_JUDGES, "selector pool should be configurable");
		TestSupport.check(design.judicialNomineePool() == JudicialNomineePool.FEDERAL_APPELLATE_JUDGES, "nominee pool should be configurable");
		TestSupport.check(design.judicialElectorateInsulation() > 0.0, "judicial electorate design should expose insulation parameter");
		CourtDesign presidential = new CourtDesign(
				"pool normalization",
				AppointmentMethod.PRESIDENT_SENATE,
				JudicialSelectorPool.ALL_FEDERAL_JUDGES,
				JudicialNomineePool.FEDERAL_APPELLATE_JUDGES,
				9,
				TermLimitPolicy.LIFE_TENURE,
				RemovalStandard.GOOD_BEHAVIOR_IMPEACHMENT,
				RecusalRule.SELF_POLICED,
				EmergencyDocketRule.OPEN_EMERGENCY,
				VotingThreshold.SIMPLE_MAJORITY,
				OpinionCoalitionRule.FREE_CONCURRENCE,
				ReviewMode.FULL_COURT,
				AuxiliaryReview.NONE,
				OverrideRule.NONE,
				1.0,
				1.0,
				0.1
		);
		TestSupport.check(!presidential.usesJudicialElectorate(), "non-judicial appointment should not use judicial electorate");
		TestSupport.check(presidential.judicialSelectorPool() == JudicialSelectorPool.NOT_APPLICABLE, "non-judicial selector pool should normalize away");
	}
	
	private static CourtDesign judicialElectorateDesign(
			JudicialSelectorPool selectorPool,
			JudicialNomineePool nomineePool
	) {
		return new CourtDesign(
				"custom judicial electorate",
				AppointmentMethod.JUDICIAL_ELECTORATE,
				selectorPool,
				nomineePool,
				11,
				TermLimitPolicy.EIGHTEEN_YEAR_STAGGERED,
				RemovalStandard.ETHICS_TRIBUNAL,
				RecusalRule.PEER_PANEL,
				EmergencyDocketRule.REASONED_FAST_TRACK,
				VotingThreshold.SIMPLE_MAJORITY,
				OpinionCoalitionRule.MAJORITY_OPINION_DISCIPLINE,
				ReviewMode.FULL_COURT,
				AuxiliaryReview.NONE,
				OverrideRule.NONE,
				1.1,
				1.0,
				0.2
		);
	}
}
