package constitutionalreview.reporting;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HexFormat;
import java.util.List;
import java.util.Locale;
import java.util.stream.Stream;


public final class ReportProvenance
{
	private ReportProvenance() {
	}
	
	public static void write(
			Path manifestPath,
			String reportName,
			int runs,
			int cases,
			long seed,
			int caseCount,
			int scenarioCount,
			Path legislativeInput,
			List<Path> artifacts
	) throws IOException {
		Files.createDirectories(manifestPath.getParent());
		StringBuilder builder = new StringBuilder();
		builder.append("{\n");
		append(builder, "reportName", reportName, true);
		append(builder, "provenanceFormat", "constitutional-review-report-v2", true);
		append(builder, "sourceTree", "tracked local project artifact; inspect repository history for commit identity", true);
		append(builder, "javaRelease", System.getProperty("constitutionalreview.javaRelease", "21"), true);
		append(builder, "javaCommand", System.getProperty("sun.java.command", "unknown"), true);
		append(builder, "runs", runs, true);
		append(builder, "casesPerRun", cases, true);
		append(builder, "seed", seed, true);
		append(builder, "experimentCaseCount", caseCount, true);
		append(builder, "scenarioCount", scenarioCount, true);
		if (legislativeInput == null) {
			append(builder, "legislativeInput", "none", true);
		} else {
			append(builder, "legislativeInput", legislativeInput.toString(), true);
			append(builder, "legislativeInputSha256", sha256(legislativeInput), true);
		}
		builder.append("  \"artifacts\": [\n");
		for (int i = 0; i < artifacts.size(); i++) {
			Path artifact = artifacts.get(i);
			builder.append("    {");
			builder.append("\"path\": \"").append(json(artifact.toString())).append("\", ");
			builder.append("\"sha256\": \"").append(json(sha256(artifact))).append("\"");
			builder.append("}");
			if (i + 1 < artifacts.size()) {
				builder.append(',');
			}
			builder.append('\n');
		}
		builder.append("  ]\n");
		builder.append("}\n");
		Files.writeString(manifestPath, builder.toString());
	}
	
	private static void append(StringBuilder builder, String key, String value, boolean comma) {
		builder.append("  \"").append(json(key)).append("\": \"").append(json(value)).append("\"");
		if (comma) {
			builder.append(',');
		}
		builder.append('\n');
	}
	
	private static void append(StringBuilder builder, String key, int value, boolean comma) {
		builder.append("  \"").append(json(key)).append("\": ").append(value);
		if (comma) {
			builder.append(',');
		}
		builder.append('\n');
	}
	
	private static void append(StringBuilder builder, String key, long value, boolean comma) {
		builder.append("  \"").append(json(key)).append("\": ").append(value);
		if (comma) {
			builder.append(',');
		}
		builder.append('\n');
	}
	
	private static String sha256(Path path) throws IOException {
		try {
			MessageDigest digest = MessageDigest.getInstance("SHA-256");
			if (Files.isDirectory(path)) {
				try (Stream<Path> stream = Files.list(path)) {
					for (Path child : stream
							.filter(Files::isRegularFile)
							.sorted()
							.toList()) {
						digest.update(child.getFileName().toString().getBytes(java.nio.charset.StandardCharsets.UTF_8));
						digest.update((byte) 0);
						digest.update(sha256(child).getBytes(java.nio.charset.StandardCharsets.UTF_8));
						digest.update((byte) 0);
					}
				}
				return HexFormat.of().formatHex(digest.digest()).toLowerCase(Locale.ROOT);
			}
			return HexFormat.of().formatHex(digest.digest(Files.readAllBytes(path))).toLowerCase(Locale.ROOT);
		} catch (NoSuchAlgorithmException exception) {
			throw new IllegalStateException("SHA-256 digest is unavailable.", exception);
		}
	}
	
	private static String json(String value) {
		return value
				.replace("\\", "\\\\")
				.replace("\"", "\\\"")
				.replace("\n", "\\n")
				.replace("\r", "\\r")
				.replace("\t", "\\t");
	}
}
