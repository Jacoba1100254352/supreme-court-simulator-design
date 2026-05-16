package constitutionalreview.experiment;


import java.nio.file.Path;


public record DiagnosticResult(
		String name,
		Path csvPath,
		Path markdownPath,
		Path manifestPath
)
{
}
