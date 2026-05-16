package constitutionalreview.simulation;


import constitutionalreview.institution.ReviewProcess;
import constitutionalreview.model.CaseWorld;
import constitutionalreview.model.CourtState;
import constitutionalreview.model.ReviewCase;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;


public final class Simulator
{
	private final WorldGenerator worldGenerator = new WorldGenerator();
	
	private static long mix(long seed, int run, int stream) {
		long value = seed;
		value ^= 0x9E3779B97F4A7C15L + ((long) run << 6) + ((long) run >> 2);
		value ^= 0xBF58476D1CE4E5B9L * (stream + 31L);
		return value;
	}
	
	public List<ScenarioReport> compare(List<Scenario> scenarios, WorldSpec worldSpec, int runs, long seed) {
		MetricsAccumulator[] accumulators = new MetricsAccumulator[scenarios.size()];
		for (int i = 0; i < accumulators.length; i++) {
			accumulators[i] = new MetricsAccumulator();
		}
		
		for (int run = 0; run < runs; run++) {
			CaseWorld world = worldGenerator.generate(worldSpec, mix(seed, run, 17));
			for (int scenarioIndex = 0; scenarioIndex < scenarios.size(); scenarioIndex++) {
				Scenario scenario = scenarios.get(scenarioIndex);
				Random scenarioRandom = new Random(mix(seed, run, scenarioIndex + 101));
				ReviewProcess process = scenario.buildProcess(world, scenarioRandom);
				CourtState state = new CourtState();
				for (ReviewCase reviewCase : world.docket()) {
					accumulators[scenarioIndex].add(process.review(reviewCase, state, scenarioRandom));
				}
			}
		}
		
		List<ScenarioReport> reports = new ArrayList<>();
		for (int i = 0; i < scenarios.size(); i++) {
			Scenario scenario = scenarios.get(i);
			reports.add(accumulators[i].toReport(scenario.key(), scenario.name()));
		}
		return reports;
	}
}
