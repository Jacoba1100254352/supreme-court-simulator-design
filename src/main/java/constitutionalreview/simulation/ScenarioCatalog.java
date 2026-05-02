package constitutionalreview.simulation;

import constitutionalreview.institution.AppointmentMethod;
import constitutionalreview.institution.AuxiliaryReview;
import constitutionalreview.institution.ConstitutionalReviewProcess;
import constitutionalreview.institution.CourtDesign;
import constitutionalreview.institution.EmergencyDocketRule;
import constitutionalreview.institution.OpinionCoalitionRule;
import constitutionalreview.institution.OverrideRule;
import constitutionalreview.institution.RecusalRule;
import constitutionalreview.institution.RecusalConsequenceType;
import constitutionalreview.institution.RemedyVotingThresholds;
import constitutionalreview.institution.RemovalStandard;
import constitutionalreview.institution.ReviewProcess;
import constitutionalreview.institution.ReviewMode;
import constitutionalreview.institution.SizeChangeDifficulty;
import constitutionalreview.institution.TermLimitPolicy;
import constitutionalreview.institution.VotingThreshold;
import constitutionalreview.model.CaseWorld;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

public final class ScenarioCatalog {
    private static final List<String> DEFAULT_SCENARIO_KEYS = List.of(
            "current-us-like",
            "term-limited-balanced",
            "nonpartisan-commission",
            "expanded-court-fifteen",
            "supermajority-review",
            "recusal-and-emergency-reform",
            "panel-en-banc",
            "cross-checking-courts",
            "dual-supreme-courts",
            "comparative-constitutional-senates",
            "constitutional-council",
            "legislative-override",
            "accountability-retention-court",
            "emergency-restraint-court"
    );

    private ScenarioCatalog() {
    }

    public static List<Scenario> defaultScenarios() {
        return scenariosForKeys(DEFAULT_SCENARIO_KEYS);
    }

    public static List<String> defaultScenarioKeys() {
        return DEFAULT_SCENARIO_KEYS;
    }

    public static List<Scenario> allScenarios() {
        return entries().stream().map(ScenarioEntry::scenario).toList();
    }

    public static List<String> scenarioKeys() {
        return entries().stream().map(ScenarioEntry::key).toList();
    }

    public static List<Scenario> scenariosForKeys(List<String> keys) {
        Map<String, Scenario> byKey = new LinkedHashMap<>();
        for (ScenarioEntry entry : entries()) {
            byKey.put(entry.key(), entry.scenario());
        }
        List<Scenario> scenarios = new ArrayList<>();
        for (String key : keys) {
            Scenario scenario = byKey.get(key);
            if (scenario == null) {
                throw new IllegalArgumentException("Unknown scenario key: " + key);
            }
            scenarios.add(scenario);
        }
        return scenarios;
    }

    private static List<ScenarioEntry> entries() {
        return List.of(
                entry("current-us-like", new CourtDesign(
                        "Stylized current U.S.-like supreme court",
                        AppointmentMethod.PRESIDENT_SENATE,
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
                        1.00,
                        0.84,
                        0.10
                )),
                entry("term-limited-balanced", new CourtDesign(
                        "18-year staggered terms + regular appointments",
                        AppointmentMethod.PRESIDENT_SENATE,
                        9,
                        TermLimitPolicy.EIGHTEEN_YEAR_STAGGERED,
                        RemovalStandard.SUPERMAJORITY_MISCONDUCT,
                        RecusalRule.PUBLIC_EXPLANATION,
                        EmergencyDocketRule.REASONED_FAST_TRACK,
                        VotingThreshold.SIMPLE_MAJORITY,
                        OpinionCoalitionRule.MAJORITY_OPINION_DISCIPLINE,
                        ReviewMode.FULL_COURT,
                        AuxiliaryReview.NONE,
                        OverrideRule.NONE,
                        1.02,
                        1.00,
                        0.13
                )),
                entry("nonpartisan-commission", new CourtDesign(
                        "Nonpartisan commission appointments",
                        AppointmentMethod.NONPARTISAN_COMMISSION,
                        9,
                        TermLimitPolicy.EIGHTEEN_YEAR_STAGGERED,
                        RemovalStandard.ETHICS_TRIBUNAL,
                        RecusalRule.PEER_PANEL,
                        EmergencyDocketRule.REASONED_FAST_TRACK,
                        VotingThreshold.SIMPLE_MAJORITY,
                        OpinionCoalitionRule.MAJORITY_OPINION_DISCIPLINE,
                        ReviewMode.FULL_COURT,
                        AuxiliaryReview.NONE,
                        OverrideRule.NONE,
                        1.10,
                        1.02,
                        0.16
                )),
                entry("expanded-court-fifteen", new CourtDesign(
                        "Expanded 15-seat court",
                        AppointmentMethod.PRESIDENT_SENATE,
                        15,
                        TermLimitPolicy.EIGHTEEN_YEAR_STAGGERED,
                        RemovalStandard.SUPERMAJORITY_MISCONDUCT,
                        RecusalRule.PUBLIC_EXPLANATION,
                        EmergencyDocketRule.REASONED_FAST_TRACK,
                        VotingThreshold.SIMPLE_MAJORITY,
                        OpinionCoalitionRule.FRAGMENTATION_TOLERANT,
                        ReviewMode.FULL_COURT,
                        AuxiliaryReview.NONE,
                        OverrideRule.NONE,
                        1.00,
                        1.00,
                        0.18
                )),
                entry("supermajority-review", new CourtDesign(
                        "60 percent invalidation threshold",
                        AppointmentMethod.PRESIDENT_SENATE,
                        9,
                        TermLimitPolicy.LIFE_TENURE,
                        RemovalStandard.GOOD_BEHAVIOR_IMPEACHMENT,
                        RecusalRule.PUBLIC_EXPLANATION,
                        EmergencyDocketRule.SUPERMAJORITY_STAY,
                        VotingThreshold.SIXTY_PERCENT,
                        OpinionCoalitionRule.MAJORITY_OPINION_DISCIPLINE,
                        ReviewMode.FULL_COURT,
                        AuxiliaryReview.NONE,
                        OverrideRule.NONE,
                        1.02,
                        0.92,
                        0.12
                )),
                entry("recusal-and-emergency-reform", new CourtDesign(
                        "Peer recusal + reasoned emergency docket",
                        AppointmentMethod.PRESIDENT_SENATE,
                        9,
                        TermLimitPolicy.EIGHTEEN_YEAR_STAGGERED,
                        RemovalStandard.ETHICS_TRIBUNAL,
                        RecusalRule.PEER_PANEL,
                        EmergencyDocketRule.REASONED_FAST_TRACK,
                        VotingThreshold.SIMPLE_MAJORITY,
                        OpinionCoalitionRule.MAJORITY_OPINION_DISCIPLINE,
                        ReviewMode.FULL_COURT,
                        AuxiliaryReview.NONE,
                        OverrideRule.NONE,
                        1.06,
                        1.04,
                        0.17
                )),
                entry("panel-en-banc", new CourtDesign(
                        "Three-judge panels with en banc correction",
                        AppointmentMethod.ROTATING_PANEL,
                        11,
                        TermLimitPolicy.TWELVE_YEAR_NONRENEWABLE,
                        RemovalStandard.ETHICS_TRIBUNAL,
                        RecusalRule.PEER_PANEL,
                        EmergencyDocketRule.REASONED_FAST_TRACK,
                        VotingThreshold.SIMPLE_MAJORITY,
                        OpinionCoalitionRule.CONSENSUS_PANEL,
                        ReviewMode.PANEL_EN_BANC,
                        AuxiliaryReview.NONE,
                        OverrideRule.NONE,
                        1.08,
                        1.04,
                        0.20
                )),
                entry("cross-checking-courts", new CourtDesign(
                        "Supreme court with cross-checking constitutional court",
                        AppointmentMethod.LEGISLATIVE_SUPERMAJORITY,
                        9,
                        TermLimitPolicy.TWELVE_YEAR_NONRENEWABLE,
                        RemovalStandard.ETHICS_TRIBUNAL,
                        RecusalRule.AUTOMATIC_CONFLICT_SCREEN,
                        EmergencyDocketRule.SUPERMAJORITY_STAY,
                        VotingThreshold.SIMPLE_MAJORITY,
                        OpinionCoalitionRule.MAJORITY_OPINION_DISCIPLINE,
                        ReviewMode.FULL_COURT,
                        AuxiliaryReview.CROSS_CHECKING_COURT,
                        OverrideRule.NONE,
                        1.12,
                        1.02,
                        0.25
                )),
                entry("dual-supreme-courts", new CourtDesign(
                        "Dual supreme courts with disagreement filter",
                        AppointmentMethod.LEGISLATIVE_SUPERMAJORITY,
                        11,
                        TermLimitPolicy.TWELVE_YEAR_NONRENEWABLE,
                        RemovalStandard.ETHICS_TRIBUNAL,
                        RecusalRule.AUTOMATIC_CONFLICT_SCREEN,
                        EmergencyDocketRule.SUPERMAJORITY_STAY,
                        VotingThreshold.SIMPLE_MAJORITY,
                        OpinionCoalitionRule.MAJORITY_OPINION_DISCIPLINE,
                        ReviewMode.DUAL_COURTS,
                        AuxiliaryReview.DUAL_SUPREME_COURTS,
                        OverrideRule.NONE,
                        1.10,
                        1.02,
                        0.30
                )),
                entry("comparative-constitutional-senates", new CourtDesign(
                        "Comparative 16-seat constitutional senates",
                        AppointmentMethod.LEGISLATIVE_SUPERMAJORITY,
                        16,
                        TermLimitPolicy.TWELVE_YEAR_NONRENEWABLE,
                        RemovalStandard.ETHICS_TRIBUNAL,
                        RecusalRule.PEER_PANEL,
                        EmergencyDocketRule.SUPERMAJORITY_STAY,
                        VotingThreshold.SIXTY_PERCENT,
                        OpinionCoalitionRule.MAJORITY_OPINION_DISCIPLINE,
                        ReviewMode.SPECIALIZED_PANELS,
                        AuxiliaryReview.NONE,
                        OverrideRule.NONE,
                        1.12,
                        1.04,
                        0.24,
                        2,
                        0.67,
                        0.18,
                        false,
                        68,
                        SizeChangeDifficulty.SUPERMAJORITY_STATUTE,
                        RecusalConsequenceType.SUBSTITUTE_JUSTICE,
                        0.004,
                        new RemedyVotingThresholds(0.50, 0.67, 0.67, 0.67, 0.67, 0.67)
                )),
                entry("constitutional-council", new CourtDesign(
                        "Pre-enactment constitutional council",
                        AppointmentMethod.NONPARTISAN_COMMISSION,
                        9,
                        TermLimitPolicy.TWELVE_YEAR_NONRENEWABLE,
                        RemovalStandard.ETHICS_TRIBUNAL,
                        RecusalRule.PEER_PANEL,
                        EmergencyDocketRule.REASONED_FAST_TRACK,
                        VotingThreshold.SIMPLE_MAJORITY,
                        OpinionCoalitionRule.CONSENSUS_PANEL,
                        ReviewMode.SPECIALIZED_PANELS,
                        AuxiliaryReview.CONSTITUTIONAL_COUNCIL,
                        OverrideRule.DELAYED_REENACTMENT,
                        1.08,
                        1.08,
                        0.24
                )),
                entry("legislative-override", new CourtDesign(
                        "Judicial review with legislative supermajority override",
                        AppointmentMethod.LEGISLATIVE_SUPERMAJORITY,
                        9,
                        TermLimitPolicy.EIGHTEEN_YEAR_STAGGERED,
                        RemovalStandard.SUPERMAJORITY_MISCONDUCT,
                        RecusalRule.PUBLIC_EXPLANATION,
                        EmergencyDocketRule.REASONED_FAST_TRACK,
                        VotingThreshold.SIMPLE_MAJORITY,
                        OpinionCoalitionRule.MAJORITY_OPINION_DISCIPLINE,
                        ReviewMode.FULL_COURT,
                        AuxiliaryReview.NONE,
                        OverrideRule.LEGISLATIVE_SUPERMAJORITY,
                        1.02,
                        1.12,
                        0.17
                )),
                entry("accountability-retention-court", new CourtDesign(
                        "Retention-election accountability court",
                        AppointmentMethod.NONPARTISAN_COMMISSION,
                        9,
                        TermLimitPolicy.RETENTION_ELECTION,
                        RemovalStandard.RETENTION_RECALL,
                        RecusalRule.PUBLIC_EXPLANATION,
                        EmergencyDocketRule.REASONED_FAST_TRACK,
                        VotingThreshold.SIMPLE_MAJORITY,
                        OpinionCoalitionRule.FREE_CONCURRENCE,
                        ReviewMode.FULL_COURT,
                        AuxiliaryReview.NONE,
                        OverrideRule.POPULAR_REFERENDUM,
                        0.92,
                        1.18,
                        0.16
                )),
                entry("emergency-restraint-court", new CourtDesign(
                        "No emergency relief without merits review",
                        AppointmentMethod.NONPARTISAN_COMMISSION,
                        9,
                        TermLimitPolicy.EIGHTEEN_YEAR_STAGGERED,
                        RemovalStandard.ETHICS_TRIBUNAL,
                        RecusalRule.AUTOMATIC_CONFLICT_SCREEN,
                        EmergencyDocketRule.NO_RELIEF_WITHOUT_MERITS,
                        VotingThreshold.RIGHTS_SUPERMAJORITY,
                        OpinionCoalitionRule.MAJORITY_OPINION_DISCIPLINE,
                        ReviewMode.FULL_COURT,
                        AuxiliaryReview.NONE,
                        OverrideRule.NONE,
                        1.12,
                        1.02,
                        0.18
                ))
        );
    }

    private static ScenarioEntry entry(String key, CourtDesign design) {
        return new ScenarioEntry(key, new DesignScenario(key, design));
    }

    private record ScenarioEntry(String key, Scenario scenario) {
    }

    private record DesignScenario(String key, CourtDesign design) implements Scenario {
        @Override
        public String name() {
            return design.name();
        }

        @Override
        public ReviewProcess buildProcess(CaseWorld world, Random random) {
            return new ConstitutionalReviewProcess(design, world, random);
        }
    }
}
