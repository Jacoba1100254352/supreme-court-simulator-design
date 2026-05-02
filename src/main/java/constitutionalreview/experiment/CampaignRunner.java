package constitutionalreview.experiment;

import constitutionalreview.importer.LegislativeOutputImporter;
import constitutionalreview.model.LegislativeOutputProfile;
import constitutionalreview.reporting.ReportProvenance;
import constitutionalreview.simulation.Scenario;
import constitutionalreview.simulation.ScenarioCatalog;
import constitutionalreview.simulation.ScenarioReport;
import constitutionalreview.simulation.Simulator;
import constitutionalreview.simulation.WorldSpec;
import constitutionalreview.util.Values;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

public final class CampaignRunner {
    private CampaignRunner() {
    }

    public static CampaignResult runV0(
            Path outputDir,
            int runs,
            int casesPerRun,
            long seed,
            LegislativeOutputProfile importedProfile,
            Path legislativeInput
    ) throws IOException {
        return run(
                "Constitutional Review Campaign v0",
                "constitutional-review-campaign-v0",
                outputDir,
                v0Cases(casesPerRun, importedProfile),
                ScenarioCatalog.defaultScenarios(),
                runs,
                casesPerRun,
                seed,
                importedProfile,
                legislativeInput
        );
    }

    public static CampaignResult runV1(
            Path outputDir,
            int runs,
            int casesPerRun,
            long seed,
            LegislativeOutputProfile importedProfile,
            Path legislativeInput
    ) throws IOException {
        return run(
                "Constitutional Review Campaign v1",
                "constitutional-review-campaign-v1",
                outputDir,
                v1Cases(casesPerRun, importedProfile),
                ScenarioCatalog.defaultScenarios(),
                runs,
                casesPerRun,
                seed,
                importedProfile,
                legislativeInput
        );
    }

    public static CampaignResult runV2(
            Path outputDir,
            int runs,
            int casesPerRun,
            long seed,
            LegislativeOutputProfile importedProfile,
            Path legislativeInput
    ) throws IOException {
        return run(
                "Constitutional Review Campaign v2",
                "constitutional-review-campaign-v2",
                outputDir,
                v2Cases(casesPerRun, importedProfile),
                ScenarioCatalog.defaultScenarios(),
                runs,
                casesPerRun,
                seed,
                importedProfile,
                legislativeInput
        );
    }

    public static CampaignResult runManipulationStress(
            Path outputDir,
            int runs,
            int casesPerRun,
            long seed,
            LegislativeOutputProfile importedProfile,
            Path legislativeInput
    ) throws IOException {
        return run(
                "Adversarial Manipulation Stress Campaign v2",
                "manipulation-stress-v2",
                outputDir,
                manipulationCases(casesPerRun, importedProfile),
                ScenarioCatalog.defaultScenarios(),
                runs,
                casesPerRun,
                seed,
                importedProfile,
                legislativeInput
        );
    }

    private static CampaignResult run(
            String reportName,
            String fileStem,
            Path outputDir,
            List<CampaignCase> cases,
            List<Scenario> scenarios,
            int runs,
            int casesPerRun,
            long seed,
            LegislativeOutputProfile importedProfile,
            Path legislativeInput
    ) throws IOException {
        Files.createDirectories(outputDir);
        Simulator simulator = new Simulator();
        List<CampaignRow> rows = new ArrayList<>();
        for (int i = 0; i < cases.size(); i++) {
            CampaignCase campaignCase = cases.get(i);
            List<ScenarioReport> reports = simulator.compare(
                    scenarios,
                    campaignCase.worldSpec(),
                    runs,
                    seed + i * 10_003L
            );
            for (ScenarioReport report : reports) {
                rows.add(new CampaignRow(campaignCase, report));
            }
        }

        Path csvPath = outputDir.resolve(fileStem + ".csv");
        Path markdownPath = outputDir.resolve(fileStem + ".md");
        Path manifestPath = outputDir.resolve(fileStem + "-manifest.json");
        CampaignResult result = new CampaignResult(csvPath, markdownPath, manifestPath, rows);
        Files.writeString(csvPath, csv(result));
        Files.writeString(markdownPath, markdown(reportName, result, runs, casesPerRun, seed, cases, scenarios, importedProfile));
        ReportProvenance.write(
                manifestPath,
                reportName,
                runs,
                casesPerRun,
                seed,
                cases.size(),
                scenarios.size(),
                legislativeInput,
                List.of(csvPath, markdownPath)
        );
        return result;
    }

    private static List<CampaignCase> v0Cases(int casesPerRun, LegislativeOutputProfile importedProfile) {
        LegislativeOutputProfile neutral = LegislativeOutputProfile.neutral();
        LegislativeOutputProfile importedBlend = importedProfile == null
                ? neutral
                : neutral.blend(importedProfile, 0.65).withSourceName("neutral/imported blend");
        List<CampaignCase> cases = new ArrayList<>();
        cases.add(new CampaignCase(
                "baseline",
                "Baseline",
                "Moderate polarization, ordinary emergency pressure, and neutral legislative output.",
                1.0,
                WorldSpec.baseline(casesPerRun, neutral)
        ));
        cases.add(new CampaignCase(
                "partisan-appointment-pressure",
                "Partisan Appointment Pressure",
                "High appointment capture and polarized justice pool.",
                1.0,
                new WorldSpec(casesPerRun, 31, 0.78, 0.76, 0.44, 0.18, neutral)
        ));
        cases.add(new CampaignCase(
                "rights-risk-legislation",
                "Rights-Risk Legislation",
                "Legislative output creates concentrated rights burdens and weak mandates.",
                1.0,
                new WorldSpec(casesPerRun, 31, 0.58, 0.48, 0.48, 0.18, new LegislativeOutputProfile(
                        "rights-risk synthetic legislature",
                        0.55,
                        0.42,
                        0.45,
                        0.62,
                        0.38,
                        0.36,
                        0.46,
                        0.52
                ))
        ));
        cases.add(new CampaignCase(
                "shadow-docket-stress",
                "Shadow-Docket Stress",
                "High emergency pressure and executive-defiance disputes.",
                1.0,
                new WorldSpec(casesPerRun, 31, 0.55, 0.50, 0.46, 0.56, new LegislativeOutputProfile(
                        "emergency-pressure synthetic legislature",
                        0.50,
                        0.52,
                        0.32,
                        0.30,
                        0.44,
                        0.58,
                        0.52,
                        0.45
                ))
        ));
        cases.add(new CampaignCase(
                "high-democratic-mandate",
                "High Democratic Mandate",
                "Popular, high-mandate laws create accountability pressure against invalidation.",
                1.0,
                new WorldSpec(casesPerRun, 31, 0.42, 0.36, 0.66, 0.14, new LegislativeOutputProfile(
                        "high-mandate synthetic legislature",
                        0.48,
                        0.68,
                        0.10,
                        0.18,
                        0.18,
                        0.18,
                        0.76,
                        0.16
                ))
        ));
        cases.add(new CampaignCase(
                "constitutional-conflict",
                "Constitutional Conflict",
                "Polarized laws, executive defiance, and public attention raise court-legislature conflict.",
                1.0,
                new WorldSpec(casesPerRun, 31, 0.72, 0.68, 0.58, 0.34, new LegislativeOutputProfile(
                        "conflict synthetic legislature",
                        0.62,
                        0.44,
                        0.42,
                        0.40,
                        0.68,
                        0.54,
                        0.44,
                        0.66
                ))
        ));
        if (importedProfile != null) {
            cases.add(new CampaignCase(
                    "imported-legislative-output",
                    "Imported Legislative Output",
                    "Docket assumptions derived from a legislative simulator campaign CSV.",
                    1.0,
                    new WorldSpec(casesPerRun, 31, 0.58, 0.50, 0.50, 0.24, importedBlend)
            ));
        }
        return cases;
    }

    static List<CampaignCase> v1Cases(int casesPerRun, LegislativeOutputProfile importedProfile) {
        List<CampaignCase> cases = new ArrayList<>(v0Cases(casesPerRun, importedProfile));
        LegislativeOutputProfile neutral = LegislativeOutputProfile.neutral();
        cases.add(new CampaignCase(
                "low-appointment-capture",
                "Low Appointment Capture",
                "Appointment incentives are less partisan and the justice pool is less polarized.",
                0.75,
                new WorldSpec(casesPerRun, 35, 0.38, 0.18, 0.44, 0.18, neutral)
        ));
        cases.add(new CampaignCase(
                "extreme-appointment-capture",
                "Extreme Appointment Capture",
                "Appointment incentives are highly partisan and vacancies become ideological leverage points.",
                1.0,
                new WorldSpec(casesPerRun, 35, 0.86, 0.88, 0.48, 0.20, neutral)
        ));
        cases.add(new CampaignCase(
                "low-emergency-pressure",
                "Low Emergency Pressure",
                "Few cases arrive through urgent stay requests or executive emergency disputes.",
                0.75,
                new WorldSpec(casesPerRun, 31, 0.52, 0.42, 0.45, 0.04, neutral)
        ));
        cases.add(new CampaignCase(
                "extreme-emergency-pressure",
                "Extreme Emergency Pressure",
                "Emergency applications, executive-power disputes, and time-sensitive election conflicts are common.",
                1.0,
                new WorldSpec(casesPerRun, 31, 0.62, 0.54, 0.48, 0.72, new LegislativeOutputProfile(
                        "extreme-emergency synthetic legislature",
                        0.54,
                        0.48,
                        0.38,
                        0.34,
                        0.50,
                        0.66,
                        0.48,
                        0.54
                ))
        ));
        cases.add(new CampaignCase(
                "low-rights-risk",
                "Low Rights Risk",
                "Legislative output is legally careful, low-volatility, and rarely burdens protected interests.",
                0.75,
                new WorldSpec(casesPerRun, 31, 0.46, 0.36, 0.50, 0.12, new LegislativeOutputProfile(
                        "low-rights-risk synthetic legislature",
                        0.42,
                        0.74,
                        0.08,
                        0.06,
                        0.14,
                        0.12,
                        0.74,
                        0.08
                ))
        ));
        cases.add(new CampaignCase(
                "extreme-rights-risk",
                "Extreme Rights Risk",
                "Legislative output often creates concentrated rights burdens under contested public mandates.",
                1.0,
                new WorldSpec(casesPerRun, 31, 0.64, 0.54, 0.50, 0.26, new LegislativeOutputProfile(
                        "extreme-rights-risk synthetic legislature",
                        0.62,
                        0.34,
                        0.48,
                        0.78,
                        0.46,
                        0.46,
                        0.40,
                        0.70
                ))
        ));
        cases.add(new CampaignCase(
                "weak-mandate-legislation",
                "Weak-Mandate Legislation",
                "Many reviewed laws have low public legitimacy and high override pressure after invalidation.",
                1.0,
                new WorldSpec(casesPerRun, 31, 0.58, 0.48, 0.42, 0.22, new LegislativeOutputProfile(
                        "weak-mandate synthetic legislature",
                        0.58,
                        0.46,
                        0.68,
                        0.34,
                        0.42,
                        0.38,
                        0.30,
                        0.74
                ))
        ));
        cases.add(new CampaignCase(
                "strong-mandate-legislation",
                "Strong-Mandate Legislation",
                "Popular legislation creates the hardest democratic-responsiveness pressure for review.",
                0.75,
                new WorldSpec(casesPerRun, 31, 0.42, 0.34, 0.70, 0.12, new LegislativeOutputProfile(
                        "strong-mandate synthetic legislature",
                        0.50,
                        0.70,
                        0.04,
                        0.16,
                        0.16,
                        0.14,
                        0.84,
                        0.10
                ))
        ));
        return cases;
    }

    static List<CampaignCase> v2Cases(int casesPerRun, LegislativeOutputProfile importedProfile) {
        List<CampaignCase> cases = new ArrayList<>(v1Cases(casesPerRun, importedProfile));
        cases.addAll(manipulationCases(casesPerRun, importedProfile));
        return cases;
    }

    static List<CampaignCase> manipulationCases(int casesPerRun, LegislativeOutputProfile importedProfile) {
        LegislativeOutputProfile neutral = LegislativeOutputProfile.neutral();
        LegislativeOutputProfile importedBlend = importedProfile == null
                ? neutral
                : neutral.blend(importedProfile, 0.55).withSourceName("adversarial/imported blend");
        List<CampaignCase> cases = new ArrayList<>();
        cases.add(new CampaignCase(
                "appointment-timing-manipulation",
                "Appointment Timing Manipulation",
                "Political actors time vacancies under high capture and public pressure.",
                1.0,
                new WorldSpec(casesPerRun, 37, 0.86, 0.92, 0.72, 0.20, importedBlend)
        ));
        cases.add(new CampaignCase(
                "emergency-application-flood",
                "Emergency Application Flood",
                "Executives and litigants route controversial policies through urgent stay requests.",
                1.0,
                new WorldSpec(casesPerRun, 33, 0.66, 0.58, 0.54, 0.84, new LegislativeOutputProfile(
                        "emergency-flood synthetic legislature",
                        0.62,
                        0.42,
                        0.44,
                        0.38,
                        0.56,
                        0.82,
                        0.44,
                        0.58
                ))
        ));
        cases.add(new CampaignCase(
                "override-evasion-loop",
                "Override Evasion Loop",
                "Legislatures repeatedly revise invalidated laws to test rights carveouts and override thresholds.",
                1.0,
                new WorldSpec(casesPerRun, 31, 0.72, 0.62, 0.68, 0.26, new LegislativeOutputProfile(
                        "override-evasion synthetic legislature",
                        0.58,
                        0.36,
                        0.32,
                        0.58,
                        0.52,
                        0.48,
                        0.72,
                        0.88
                ))
        ));
        cases.add(new CampaignCase(
                "recusal-pressure-campaign",
                "Recusal Pressure Campaign",
                "High-salience litigants try to force or avoid recusals around ideologically charged cases.",
                0.85,
                new WorldSpec(casesPerRun, 35, 0.80, 0.74, 0.78, 0.34, new LegislativeOutputProfile(
                        "recusal-pressure synthetic legislature",
                        0.48,
                        0.50,
                        0.42,
                        0.46,
                        0.70,
                        0.48,
                        0.42,
                        0.62
                ))
        ));
        cases.add(new CampaignCase(
                "court-expansion-retaliation",
                "Court Expansion Retaliation",
                "A polarized political system reacts to judicial conflict with expansion threats and capture pressure.",
                0.85,
                new WorldSpec(casesPerRun, 45, 0.90, 0.86, 0.66, 0.30, new LegislativeOutputProfile(
                        "expansion-retaliation synthetic legislature",
                        0.54,
                        0.40,
                        0.48,
                        0.44,
                        0.74,
                        0.54,
                        0.40,
                        0.72
                ))
        ));
        return cases;
    }

    private static String csv(CampaignResult result) {
        StringBuilder builder = new StringBuilder();
        builder.append(String.join(",",
                "caseKey",
                "caseName",
                "caseDescription",
                "caseWeight",
                "legislativeSource",
                "scenarioKey",
                "scenario",
                "totalCases",
                "petitionFiledRate",
                "admissionRate",
                "screenOutRate",
                "meritsTransferRate",
                "paidPetitionRate",
                "ifpPetitionRate",
                "solicitorGeneralSignalRate",
                "amicusIntensity",
                "splitMaturity",
                "relistRate",
                "specialistCounselRate",
                "vehicleDefectRisk",
                "conditionalReversalProbability",
                "directionalScore",
                "stabilityRightsScore",
                "legitimacyControlScore",
                "legalStability",
                "precedentStability",
                "statutoryStability",
                "interbranchCompliance",
                "rightsProtection",
                "partisanAlignment",
                "shadowDocketAbuse",
                "emergencyLegitimacyRisk",
                "legitimacy",
                "reversalRate",
                "constitutionalConflict",
                "democraticResponsiveness",
                "independenceAccountabilityBalance",
                "administrativeCost",
                "invalidationRate",
                "meritsReviewRate",
                "emergencyOrderRate",
                "emergencyGrantRate",
                "shadowReliefRate",
                "reasonedEmergencyOrderRate",
                "temporaryStayRate",
                "meritsAccelerationRate",
                "expiredEmergencyOrderRate",
                "recusalRate",
                "quorumFailureRate",
                "justiceReplacementRate",
                "concurrenceRate",
                "dissentRate",
                "fragmentationIndex",
                "panelRate",
                "enBancRate",
                "crossCheckDisagreementRate",
                "councilWarningRate",
                "overrideAttemptRate",
                "overrideRate",
                "rightsCarveoutBlockRate",
                "repeatedOverrideRate",
                "strategicPressure",
                "legislativeDefiance",
                "executiveEmergencyStrategy",
                "appointmentManipulationPressure",
                "overrideAdaptation",
                "legislativeComplianceRate",
                "legislativeEvasionRate",
                "delayedReenactmentStrategyRate",
                "executiveEmergencyFloodRate",
                "overrideCampaignRate",
                "appointmentPressureCampaignRate",
                "formalRepealRate",
                "formalReplacementRate",
                "formalNarrowedReenactmentRate",
                "formalWeakOverrideRate",
                "formalAmendmentRate",
                "formalCourtCurbingRate",
                "formalOpenDefianceRate",
                "practicalDelayRate",
                "practicalAdministrativeSubstitutionRate",
                "practicalSymbolicComplianceRate",
                "practicalBureaucraticResistanceRate",
                "practicalOpenNoncomplianceRate",
                "rightsClaimantCaseRate",
                "rightsClaimantSuccess",
                "rightsDomainClaimantSuccess",
                "structuralDomainClaimantSuccess",
                "electionDomainClaimantSuccess",
                "executivePowerDomainClaimantSuccess",
                "administrativeDomainClaimantSuccess",
                "economicDomainClaimantSuccess",
                "doctrinalDepth",
                "remedialBreadth",
                "lowerCourtCompliance",
                "eliteAcceptance",
                "publicConfidence",
                "facialChallengeRate",
                "asAppliedChallengeRate",
                "electionDisputeRate",
                "emergencyStayDocketRate",
                "executivePowerDisputeRate",
                "administrativeLawRate",
                "rightsClaimRate"
        )).append('\n');
        for (CampaignRow row : result.rows()) {
            ScenarioReport report = row.report();
            CampaignCase campaignCase = row.campaignCase();
            builder.append(Values.csv(campaignCase.key())).append(',')
                    .append(Values.csv(campaignCase.name())).append(',')
                    .append(Values.csv(campaignCase.description())).append(',')
                    .append(format(campaignCase.weight())).append(',')
                    .append(Values.csv(campaignCase.worldSpec().legislativeProfile().sourceName())).append(',')
                    .append(Values.csv(report.scenarioKey())).append(',')
                    .append(Values.csv(report.scenarioName())).append(',')
                    .append(report.totalCases()).append(',')
                    .append(format(report.petitionFiledRate())).append(',')
                    .append(format(report.admissionRate())).append(',')
                    .append(format(report.screenOutRate())).append(',')
                    .append(format(report.meritsTransferRate())).append(',')
                    .append(format(report.paidPetitionRate())).append(',')
                    .append(format(report.ifpPetitionRate())).append(',')
                    .append(format(report.solicitorGeneralSignalRate())).append(',')
                    .append(format(report.amicusIntensity())).append(',')
                    .append(format(report.splitMaturity())).append(',')
                    .append(format(report.relistRate())).append(',')
                    .append(format(report.specialistCounselRate())).append(',')
                    .append(format(report.vehicleDefectRisk())).append(',')
                    .append(format(report.conditionalReversalProbability())).append(',')
                    .append(format(report.directionalScore())).append(',')
                    .append(format(report.stabilityRightsScore())).append(',')
                    .append(format(report.legitimacyControlScore())).append(',')
                    .append(format(report.legalStability())).append(',')
                    .append(format(report.precedentStability())).append(',')
                    .append(format(report.statutoryStability())).append(',')
                    .append(format(report.interbranchCompliance())).append(',')
                    .append(format(report.rightsProtection())).append(',')
                    .append(format(report.partisanAlignment())).append(',')
                    .append(format(report.shadowDocketAbuse())).append(',')
                    .append(format(report.emergencyLegitimacyRisk())).append(',')
                    .append(format(report.legitimacy())).append(',')
                    .append(format(report.reversalRate())).append(',')
                    .append(format(report.constitutionalConflict())).append(',')
                    .append(format(report.democraticResponsiveness())).append(',')
                    .append(format(report.independenceAccountabilityBalance())).append(',')
                    .append(format(report.administrativeCost())).append(',')
                    .append(format(report.invalidationRate())).append(',')
                    .append(format(report.meritsReviewRate())).append(',')
                    .append(format(report.emergencyOrderRate())).append(',')
                    .append(format(report.emergencyGrantRate())).append(',')
                    .append(format(report.shadowReliefRate())).append(',')
                    .append(format(report.reasonedEmergencyOrderRate())).append(',')
                    .append(format(report.temporaryStayRate())).append(',')
                    .append(format(report.meritsAccelerationRate())).append(',')
                    .append(format(report.expiredEmergencyOrderRate())).append(',')
                    .append(format(report.recusalRate())).append(',')
                    .append(format(report.quorumFailureRate())).append(',')
                    .append(format(report.justiceReplacementRate())).append(',')
                    .append(format(report.concurrenceRate())).append(',')
                    .append(format(report.dissentRate())).append(',')
                    .append(format(report.fragmentationIndex())).append(',')
                    .append(format(report.panelRate())).append(',')
                    .append(format(report.enBancRate())).append(',')
                    .append(format(report.crossCheckDisagreementRate())).append(',')
                    .append(format(report.councilWarningRate())).append(',')
                    .append(format(report.overrideAttemptRate())).append(',')
                    .append(format(report.overrideRate())).append(',')
                    .append(format(report.rightsCarveoutBlockRate())).append(',')
                    .append(format(report.repeatedOverrideRate())).append(',')
                    .append(format(report.strategicPressure())).append(',')
                    .append(format(report.legislativeDefiance())).append(',')
                    .append(format(report.executiveEmergencyStrategy())).append(',')
                    .append(format(report.appointmentManipulationPressure())).append(',')
                    .append(format(report.overrideAdaptation())).append(',')
                    .append(format(report.legislativeComplianceRate())).append(',')
                    .append(format(report.legislativeEvasionRate())).append(',')
                    .append(format(report.delayedReenactmentStrategyRate())).append(',')
                    .append(format(report.executiveEmergencyFloodRate())).append(',')
                    .append(format(report.overrideCampaignRate())).append(',')
                    .append(format(report.appointmentPressureCampaignRate())).append(',')
                    .append(format(report.formalRepealRate())).append(',')
                    .append(format(report.formalReplacementRate())).append(',')
                    .append(format(report.formalNarrowedReenactmentRate())).append(',')
                    .append(format(report.formalWeakOverrideRate())).append(',')
                    .append(format(report.formalAmendmentRate())).append(',')
                    .append(format(report.formalCourtCurbingRate())).append(',')
                    .append(format(report.formalOpenDefianceRate())).append(',')
                    .append(format(report.practicalDelayRate())).append(',')
                    .append(format(report.practicalAdministrativeSubstitutionRate())).append(',')
                    .append(format(report.practicalSymbolicComplianceRate())).append(',')
                    .append(format(report.practicalBureaucraticResistanceRate())).append(',')
                    .append(format(report.practicalOpenNoncomplianceRate())).append(',')
                    .append(format(report.rightsClaimantCaseRate())).append(',')
                    .append(format(report.rightsClaimantSuccess())).append(',')
                    .append(format(report.rightsDomainClaimantSuccess())).append(',')
                    .append(format(report.structuralDomainClaimantSuccess())).append(',')
                    .append(format(report.electionDomainClaimantSuccess())).append(',')
                    .append(format(report.executivePowerDomainClaimantSuccess())).append(',')
                    .append(format(report.administrativeDomainClaimantSuccess())).append(',')
                    .append(format(report.economicDomainClaimantSuccess())).append(',')
                    .append(format(report.doctrinalDepth())).append(',')
                    .append(format(report.remedialBreadth())).append(',')
                    .append(format(report.lowerCourtCompliance())).append(',')
                    .append(format(report.eliteAcceptance())).append(',')
                    .append(format(report.publicConfidence())).append(',')
                    .append(format(report.facialChallengeRate())).append(',')
                    .append(format(report.asAppliedChallengeRate())).append(',')
                    .append(format(report.electionDisputeRate())).append(',')
                    .append(format(report.emergencyStayDocketRate())).append(',')
                    .append(format(report.executivePowerDisputeRate())).append(',')
                    .append(format(report.administrativeLawRate())).append(',')
                    .append(format(report.rightsClaimRate()))
                    .append('\n');
        }
        return builder.toString();
    }

    private static String markdown(
            String reportName,
            CampaignResult result,
            int runs,
            int casesPerRun,
            long seed,
            List<CampaignCase> cases,
            List<Scenario> scenarios,
            LegislativeOutputProfile importedProfile
    ) {
        StringBuilder builder = new StringBuilder();
        builder.append("# ").append(reportName).append("\n\n");
        builder.append("Deterministic batch campaign for comparing supreme-court and constitutional-review designs.\n\n");
        builder.append("## Run Configuration\n\n");
        builder.append("- runs per case: ").append(runs).append('\n');
        builder.append("- cases per run: ").append(casesPerRun).append('\n');
        builder.append("- base seed: ").append(seed).append('\n');
        builder.append("- scenarios per case: ").append(scenarios.size()).append('\n');
        builder.append("- experiment cases: ").append(cases.size()).append("\n\n");
        if (importedProfile == null) {
            builder.append("- legislative input: neutral synthetic profile\n\n");
        } else {
            builder.append("- legislative input: ")
                    .append(LegislativeOutputImporter.describe(importedProfile))
                    .append("\n\n");
        }

        builder.append("## Case Weights\n\n");
        builder.append("| Case | Weight | Legislative source | Description |\n");
        builder.append("| --- | ---: | --- | --- |\n");
        for (CampaignCase campaignCase : cases) {
            builder.append("| ")
                    .append(campaignCase.name())
                    .append(" | ")
                    .append(format(campaignCase.weight()))
                    .append(" | ")
                    .append(campaignCase.worldSpec().legislativeProfile().sourceName())
                    .append(" | ")
                    .append(campaignCase.description())
                    .append(" |\n");
        }

        List<WeightedScenarioReport> weightedReports = weightedReports(result.rows());
        builder.append("\n## Headline Findings\n\n");
        WeightedScenarioReport bestDirectional = weightedReports.stream()
                .max(Comparator.comparingDouble(WeightedScenarioReport::directionalScore))
                .orElseThrow();
        WeightedScenarioReport bestRights = weightedReports.stream()
                .max(Comparator.comparingDouble(WeightedScenarioReport::rightsProtection))
                .orElseThrow();
        WeightedScenarioReport lowestShadow = weightedReports.stream()
                .min(Comparator.comparingDouble(WeightedScenarioReport::shadowDocketAbuse))
                .orElseThrow();
        WeightedScenarioReport lowestEmergencyRisk = weightedReports.stream()
                .min(Comparator.comparingDouble(WeightedScenarioReport::emergencyLegitimacyRisk))
                .orElseThrow();
        WeightedScenarioReport lowestPartisan = weightedReports.stream()
                .min(Comparator.comparingDouble(WeightedScenarioReport::partisanAlignment))
                .orElseThrow();
        WeightedScenarioReport highestPublicConfidence = weightedReports.stream()
                .max(Comparator.comparingDouble(WeightedScenarioReport::publicConfidence))
                .orElseThrow();
        builder.append("- Highest directional score: ")
                .append(bestDirectional.scenarioName())
                .append(" at ")
                .append(format(bestDirectional.directionalScore()))
                .append(".\n");
        builder.append("- Highest rights protection: ")
                .append(bestRights.scenarioName())
                .append(" at ")
                .append(format(bestRights.rightsProtection()))
                .append(".\n");
        builder.append("- Lowest shadow-docket abuse: ")
                .append(lowestShadow.scenarioName())
                .append(" at ")
                .append(format(lowestShadow.shadowDocketAbuse()))
                .append(".\n");
        builder.append("- Lowest emergency legitimacy risk: ")
                .append(lowestEmergencyRisk.scenarioName())
                .append(" at ")
                .append(format(lowestEmergencyRisk.emergencyLegitimacyRisk()))
                .append(".\n");
        builder.append("- Lowest partisan alignment: ")
                .append(lowestPartisan.scenarioName())
                .append(" at ")
                .append(format(lowestPartisan.partisanAlignment()))
                .append(".\n");
        builder.append("- Highest public confidence index: ")
                .append(highestPublicConfidence.scenarioName())
                .append(" at ")
                .append(format(highestPublicConfidence.publicConfidence()))
                .append(".\n");
        builder.append("- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, claimant success, elite acceptance, and administrative feasibility.\n");

        builder.append("\n## Metric Direction Legend\n\n");
        builder.append("- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.\n");
        builder.append("- Higher direct outputs such as `rightsClaimantSuccess`, `doctrinalDepth`, `remedialBreadth`, `lowerCourtCompliance`, `eliteAcceptance`, and `publicConfidence` are usually better, but each should be read in domain context.\n");
        builder.append("- Lower `partisanAlignment`, `shadowDocketAbuse`, `emergencyLegitimacyRisk`, `reversalRate`, `constitutionalConflict`, `administrativeCost`, and `strategicPressure` are usually better.\n");
        builder.append("- Petition, admission, emergency, replacement, recusal, concurrence, dissent, fragmentation, panel, en banc, council, cross-check, formal-response, practical-response, and override rates are diagnostic rather than automatically good or bad.\n");

        builder.append("\n## Scenario Averages Across Cases\n\n");
        builder.append("| Scenario | Directional | Admission | Screen out | Rights protection | Claimant success | Doctrinal depth | Remedy breadth | Lower-court compliance | Elite acceptance | Public confidence | Partisan align. | Shadow abuse | Emergency risk | Emergency grants | Fragmentation | Strategic | Court-curbing | Open noncomp. | Admin cost |\n");
        builder.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |\n");
        weightedReports.stream()
                .sorted(Comparator.comparingDouble(WeightedScenarioReport::directionalScore).reversed())
                .forEach(report -> builder.append("| ")
                        .append(report.scenarioName())
                        .append(" | ")
                        .append(format(report.directionalScore()))
                        .append(" | ")
                        .append(format(report.admissionRate()))
                        .append(" | ")
                        .append(format(report.screenOutRate()))
                        .append(" | ")
                        .append(format(report.rightsProtection()))
                        .append(" | ")
                        .append(format(report.rightsClaimantSuccess()))
                        .append(" | ")
                        .append(format(report.doctrinalDepth()))
                        .append(" | ")
                        .append(format(report.remedialBreadth()))
                        .append(" | ")
                        .append(format(report.lowerCourtCompliance()))
                        .append(" | ")
                        .append(format(report.eliteAcceptance()))
                        .append(" | ")
                        .append(format(report.publicConfidence()))
                        .append(" | ")
                        .append(format(report.partisanAlignment()))
                        .append(" | ")
                        .append(format(report.shadowDocketAbuse()))
                        .append(" | ")
                        .append(format(report.emergencyLegitimacyRisk()))
                        .append(" | ")
                        .append(format(report.emergencyGrantRate()))
                        .append(" | ")
                        .append(format(report.fragmentationIndex()))
                        .append(" | ")
                        .append(format(report.strategicPressure()))
                        .append(" | ")
                        .append(format(report.formalCourtCurbingRate()))
                        .append(" | ")
                        .append(format(report.practicalOpenNoncomplianceRate()))
                        .append(" | ")
                        .append(format(report.administrativeCost()))
                        .append(" |\n"));
        builder.append("\n## Domain-Specific Rights Claimant Success\n\n");
        builder.append("| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |\n");
        builder.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |\n");
        weightedReports.stream()
                .sorted(Comparator.comparingDouble(WeightedScenarioReport::directionalScore).reversed())
                .forEach(report -> builder.append("| ")
                        .append(report.scenarioName())
                        .append(" | ")
                        .append(format(report.rightsClaimantCaseRate()))
                        .append(" | ")
                        .append(format(report.rightsClaimantSuccess()))
                        .append(" | ")
                        .append(format(report.rightsDomainClaimantSuccess()))
                        .append(" | ")
                        .append(format(report.structuralDomainClaimantSuccess()))
                        .append(" | ")
                        .append(format(report.electionDomainClaimantSuccess()))
                        .append(" | ")
                        .append(format(report.executivePowerDomainClaimantSuccess()))
                        .append(" | ")
                        .append(format(report.administrativeDomainClaimantSuccess()))
                        .append(" | ")
                        .append(format(report.economicDomainClaimantSuccess()))
                        .append(" |\n"));
        appendCaseSlices(builder, result.rows());
        return builder.toString();
    }

    private static void appendCaseSlices(StringBuilder builder, List<CampaignRow> rows) {
        Map<String, List<CampaignRow>> byCase = new LinkedHashMap<>();
        for (CampaignRow row : rows) {
            byCase.computeIfAbsent(row.campaignCase().key(), ignored -> new ArrayList<>()).add(row);
        }
        builder.append("\n## Stress Case Leaders\n\n");
        builder.append("| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |\n");
        builder.append("| --- | --- | --- | --- | --- |\n");
        for (List<CampaignRow> caseRows : byCase.values()) {
            CampaignCase campaignCase = caseRows.get(0).campaignCase();
            ScenarioReport bestDirectional = caseRows.stream()
                    .map(CampaignRow::report)
                    .max(Comparator.comparingDouble(ScenarioReport::directionalScore))
                    .orElseThrow();
            ScenarioReport bestRights = caseRows.stream()
                    .map(CampaignRow::report)
                    .max(Comparator.comparingDouble(ScenarioReport::rightsProtection))
                    .orElseThrow();
            ScenarioReport lowestShadow = caseRows.stream()
                    .map(CampaignRow::report)
                    .min(Comparator.comparingDouble(ScenarioReport::shadowDocketAbuse))
                    .orElseThrow();
            ScenarioReport lowestPartisan = caseRows.stream()
                    .map(CampaignRow::report)
                    .min(Comparator.comparingDouble(ScenarioReport::partisanAlignment))
                    .orElseThrow();
            builder.append("| ")
                    .append(campaignCase.name())
                    .append(" | ")
                    .append(bestDirectional.scenarioName())
                    .append(" (")
                    .append(format(bestDirectional.directionalScore()))
                    .append(") | ")
                    .append(bestRights.scenarioName())
                    .append(" (")
                    .append(format(bestRights.rightsProtection()))
                    .append(") | ")
                    .append(lowestShadow.scenarioName())
                    .append(" (")
                    .append(format(lowestShadow.shadowDocketAbuse()))
                    .append(") | ")
                    .append(lowestPartisan.scenarioName())
                    .append(" (")
                    .append(format(lowestPartisan.partisanAlignment()))
                    .append(") |\n");
        }
    }

    private static List<WeightedScenarioReport> weightedReports(List<CampaignRow> rows) {
        Map<String, WeightedTotals> totals = new LinkedHashMap<>();
        for (CampaignRow row : rows) {
            WeightedTotals total = totals.computeIfAbsent(
                    row.report().scenarioKey(),
                    key -> new WeightedTotals(row.report().scenarioName())
            );
            total.add(row.campaignCase().weight(), row.report());
        }
        return totals.entrySet().stream()
                .map(entry -> entry.getValue().toReport(entry.getKey()))
                .toList();
    }

    private static String format(double value) {
        return String.format(Locale.ROOT, "%.3f", value);
    }

    private static final class WeightedTotals {
        private final String scenarioName;
        private double weight;
        private double directionalScore;
        private double petitionFiledRate;
        private double admissionRate;
        private double screenOutRate;
        private double meritsTransferRate;
        private double stabilityRightsScore;
        private double legitimacyControlScore;
        private double legalStability;
        private double precedentStability;
        private double statutoryStability;
        private double interbranchCompliance;
        private double rightsProtection;
        private double partisanAlignment;
        private double shadowDocketAbuse;
        private double emergencyLegitimacyRisk;
        private double legitimacy;
        private double reversalRate;
        private double constitutionalConflict;
        private double democraticResponsiveness;
        private double strategicPressure;
        private double formalCourtCurbingRate;
        private double formalOpenDefianceRate;
        private double practicalOpenNoncomplianceRate;
        private double legislativeEvasionRate;
        private double executiveEmergencyFloodRate;
        private double administrativeCost;
        private double invalidationRate;
        private double emergencyGrantRate;
        private double quorumFailureRate;
        private double fragmentationIndex;
        private double rightsClaimantCaseRate;
        private double rightsClaimantSuccess;
        private double rightsDomainClaimantSuccess;
        private double structuralDomainClaimantSuccess;
        private double electionDomainClaimantSuccess;
        private double executivePowerDomainClaimantSuccess;
        private double administrativeDomainClaimantSuccess;
        private double economicDomainClaimantSuccess;
        private double doctrinalDepth;
        private double remedialBreadth;
        private double lowerCourtCompliance;
        private double eliteAcceptance;
        private double publicConfidence;
        private double meritsAccelerationRate;
        private double justiceReplacementRate;
        private double overrideAttemptRate;
        private double overrideRate;

        private WeightedTotals(String scenarioName) {
            this.scenarioName = scenarioName;
        }

        private void add(double rowWeight, ScenarioReport report) {
            weight += rowWeight;
            directionalScore += report.directionalScore() * rowWeight;
            petitionFiledRate += report.petitionFiledRate() * rowWeight;
            admissionRate += report.admissionRate() * rowWeight;
            screenOutRate += report.screenOutRate() * rowWeight;
            meritsTransferRate += report.meritsTransferRate() * rowWeight;
            stabilityRightsScore += report.stabilityRightsScore() * rowWeight;
            legitimacyControlScore += report.legitimacyControlScore() * rowWeight;
            legalStability += report.legalStability() * rowWeight;
            precedentStability += report.precedentStability() * rowWeight;
            statutoryStability += report.statutoryStability() * rowWeight;
            interbranchCompliance += report.interbranchCompliance() * rowWeight;
            rightsProtection += report.rightsProtection() * rowWeight;
            partisanAlignment += report.partisanAlignment() * rowWeight;
            shadowDocketAbuse += report.shadowDocketAbuse() * rowWeight;
            emergencyLegitimacyRisk += report.emergencyLegitimacyRisk() * rowWeight;
            legitimacy += report.legitimacy() * rowWeight;
            reversalRate += report.reversalRate() * rowWeight;
            constitutionalConflict += report.constitutionalConflict() * rowWeight;
            democraticResponsiveness += report.democraticResponsiveness() * rowWeight;
            strategicPressure += report.strategicPressure() * rowWeight;
            formalCourtCurbingRate += report.formalCourtCurbingRate() * rowWeight;
            formalOpenDefianceRate += report.formalOpenDefianceRate() * rowWeight;
            practicalOpenNoncomplianceRate += report.practicalOpenNoncomplianceRate() * rowWeight;
            legislativeEvasionRate += report.legislativeEvasionRate() * rowWeight;
            executiveEmergencyFloodRate += report.executiveEmergencyFloodRate() * rowWeight;
            administrativeCost += report.administrativeCost() * rowWeight;
            invalidationRate += report.invalidationRate() * rowWeight;
            emergencyGrantRate += report.emergencyGrantRate() * rowWeight;
            quorumFailureRate += report.quorumFailureRate() * rowWeight;
            fragmentationIndex += report.fragmentationIndex() * rowWeight;
            rightsClaimantCaseRate += report.rightsClaimantCaseRate() * rowWeight;
            rightsClaimantSuccess += report.rightsClaimantSuccess() * rowWeight;
            rightsDomainClaimantSuccess += report.rightsDomainClaimantSuccess() * rowWeight;
            structuralDomainClaimantSuccess += report.structuralDomainClaimantSuccess() * rowWeight;
            electionDomainClaimantSuccess += report.electionDomainClaimantSuccess() * rowWeight;
            executivePowerDomainClaimantSuccess += report.executivePowerDomainClaimantSuccess() * rowWeight;
            administrativeDomainClaimantSuccess += report.administrativeDomainClaimantSuccess() * rowWeight;
            economicDomainClaimantSuccess += report.economicDomainClaimantSuccess() * rowWeight;
            doctrinalDepth += report.doctrinalDepth() * rowWeight;
            remedialBreadth += report.remedialBreadth() * rowWeight;
            lowerCourtCompliance += report.lowerCourtCompliance() * rowWeight;
            eliteAcceptance += report.eliteAcceptance() * rowWeight;
            publicConfidence += report.publicConfidence() * rowWeight;
            meritsAccelerationRate += report.meritsAccelerationRate() * rowWeight;
            justiceReplacementRate += report.justiceReplacementRate() * rowWeight;
            overrideAttemptRate += report.overrideAttemptRate() * rowWeight;
            overrideRate += report.overrideRate() * rowWeight;
        }

        private WeightedScenarioReport toReport(String scenarioKey) {
            double denominator = Math.max(1.0, weight);
            return new WeightedScenarioReport(
                    scenarioKey,
                    scenarioName,
                    directionalScore / denominator,
                    petitionFiledRate / denominator,
                    admissionRate / denominator,
                    screenOutRate / denominator,
                    meritsTransferRate / denominator,
                    stabilityRightsScore / denominator,
                    legitimacyControlScore / denominator,
                    legalStability / denominator,
                    precedentStability / denominator,
                    statutoryStability / denominator,
                    interbranchCompliance / denominator,
                    rightsProtection / denominator,
                    partisanAlignment / denominator,
                    shadowDocketAbuse / denominator,
                    emergencyLegitimacyRisk / denominator,
                    legitimacy / denominator,
                    reversalRate / denominator,
                    constitutionalConflict / denominator,
                    democraticResponsiveness / denominator,
                    strategicPressure / denominator,
                    formalCourtCurbingRate / denominator,
                    formalOpenDefianceRate / denominator,
                    practicalOpenNoncomplianceRate / denominator,
                    legislativeEvasionRate / denominator,
                    executiveEmergencyFloodRate / denominator,
                    administrativeCost / denominator,
                    invalidationRate / denominator,
                    emergencyGrantRate / denominator,
                    quorumFailureRate / denominator,
                    fragmentationIndex / denominator,
                    rightsClaimantCaseRate / denominator,
                    rightsClaimantSuccess / denominator,
                    rightsDomainClaimantSuccess / denominator,
                    structuralDomainClaimantSuccess / denominator,
                    electionDomainClaimantSuccess / denominator,
                    executivePowerDomainClaimantSuccess / denominator,
                    administrativeDomainClaimantSuccess / denominator,
                    economicDomainClaimantSuccess / denominator,
                    doctrinalDepth / denominator,
                    remedialBreadth / denominator,
                    lowerCourtCompliance / denominator,
                    eliteAcceptance / denominator,
                    publicConfidence / denominator,
                    meritsAccelerationRate / denominator,
                    justiceReplacementRate / denominator,
                    overrideAttemptRate / denominator,
                    overrideRate / denominator
            );
        }
    }

    private record WeightedScenarioReport(
            String scenarioKey,
            String scenarioName,
            double directionalScore,
            double petitionFiledRate,
            double admissionRate,
            double screenOutRate,
            double meritsTransferRate,
            double stabilityRightsScore,
            double legitimacyControlScore,
            double legalStability,
            double precedentStability,
            double statutoryStability,
            double interbranchCompliance,
            double rightsProtection,
            double partisanAlignment,
            double shadowDocketAbuse,
            double emergencyLegitimacyRisk,
            double legitimacy,
            double reversalRate,
            double constitutionalConflict,
            double democraticResponsiveness,
            double strategicPressure,
            double formalCourtCurbingRate,
            double formalOpenDefianceRate,
            double practicalOpenNoncomplianceRate,
            double legislativeEvasionRate,
            double executiveEmergencyFloodRate,
            double administrativeCost,
            double invalidationRate,
            double emergencyGrantRate,
            double quorumFailureRate,
            double fragmentationIndex,
            double rightsClaimantCaseRate,
            double rightsClaimantSuccess,
            double rightsDomainClaimantSuccess,
            double structuralDomainClaimantSuccess,
            double electionDomainClaimantSuccess,
            double executivePowerDomainClaimantSuccess,
            double administrativeDomainClaimantSuccess,
            double economicDomainClaimantSuccess,
            double doctrinalDepth,
            double remedialBreadth,
            double lowerCourtCompliance,
            double eliteAcceptance,
            double publicConfidence,
            double meritsAccelerationRate,
            double justiceReplacementRate,
            double overrideAttemptRate,
            double overrideRate
    ) {
    }
}
