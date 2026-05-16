package constitutionalreview.experiment;


import constitutionalreview.simulation.WorldSpec;


public record CampaignCase(
		String key,
		String name,
		String description,
		double weight,
		WorldSpec worldSpec
)
{
}
