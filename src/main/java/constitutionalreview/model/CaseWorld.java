package constitutionalreview.model;


import java.util.List;


public record CaseWorld(
		List<Justice> justicePool,
		List<ReviewCase> docket,
		LegislativeOutputProfile legislativeProfile
)
{
}
