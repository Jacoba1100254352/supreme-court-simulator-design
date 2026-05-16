package constitutionalreview.experiment;


import java.nio.file.Path;
import java.util.List;


public record CampaignResult(
		Path csvPath,
		Path markdownPath,
		Path manifestPath,
		List<CampaignRow> rows
)
{
}
