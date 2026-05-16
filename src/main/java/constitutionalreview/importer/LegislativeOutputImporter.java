package constitutionalreview.importer;


import constitutionalreview.model.LegislativeOutputProfile;
import constitutionalreview.util.Values;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;


public final class LegislativeOutputImporter
{
	private LegislativeOutputImporter() {
	}
	
	public static LegislativeOutputProfile importCsv(Path path) throws IOException {
		List<String> lines = Files.readAllLines(path);
		if (lines.isEmpty()) {
			throw new IllegalArgumentException("Legislative output CSV is empty: " + path);
		}
		List<String> header = parseLine(lines.get(0));
		List<Map<String, String>> rows = new ArrayList<>();
		for (int i = 1; i < lines.size(); i++) {
			String line = lines.get(i);
			if (line.isBlank()) {
				continue;
			}
			List<String> values = parseLine(line);
			Map<String, String> row = new LinkedHashMap<>();
			for (int column = 0; column < header.size(); column++) {
				row.put(header.get(column), column < values.size() ? values.get(column) : "");
			}
			rows.add(row);
		}
		if (rows.isEmpty()) {
			throw new IllegalArgumentException("Legislative output CSV has no data rows: " + path);
		}
		
		double enactedVolume = average(rows, List.of("enactedVolume", "productivity"), 0.45);
		double legalQuality = average(rows, List.of("legalQuality", "welfare", "publicAlignment"), 0.62);
		double weakMandate = average(rows, List.of("weakMandateRate", "weakPublicMandatePassage", "lowSupport"), 0.22);
		double rightsRisk = average(rows, List.of("rightsRisk", "minorityHarm", "concentratedHarmPassage"), 0.20);
		double partisanSkew = average(rows, List.of("partisanSkew", "capture", "lobbyCapture", "publicPreferenceDistortion"), 0.28);
		double volatility = average(rows, List.of("volatility", "policyShift", "statusQuoVolatility"), 0.24);
		double publicLegitimacy = average(rows, List.of("publicLegitimacy", "legitimacy", "avgSupport"), 0.58);
		double overridePressure = Values.average(weakMandate, rightsRisk, volatility, 1.0 - publicLegitimacy);
		
		return new LegislativeOutputProfile(
				path.getFileName().toString(),
				enactedVolume,
				legalQuality,
				weakMandate,
				rightsRisk,
				partisanSkew,
				volatility,
				publicLegitimacy,
				overridePressure
		).normalized();
	}
	
	private static double average(List<Map<String, String>> rows, List<String> names, double fallback) {
		double total = 0.0;
		double weightTotal = 0.0;
		for (Map<String, String> row : rows) {
			Double value = findNumber(row, names);
			if (value == null) {
				continue;
			}
			Double rowWeight = findNumber(row, List.of("caseWeight", "weight"));
			double weight = rowWeight == null ? 1.0 : Math.max(0.0, rowWeight);
			total += Values.clamp01(value) * weight;
			weightTotal += weight;
		}
		if (weightTotal == 0.0) {
			return fallback;
		}
		return total / weightTotal;
	}
	
	private static Double findNumber(Map<String, String> row, List<String> names) {
		for (String name : names) {
			for (Map.Entry<String, String> entry : row.entrySet()) {
				if (entry.getKey().equalsIgnoreCase(name)) {
					return parseNumber(entry.getValue());
				}
			}
		}
		return null;
	}
	
	private static Double parseNumber(String value) {
		if (value == null || value.isBlank()) {
			return null;
		}
		try {
			return Double.parseDouble(value.trim());
		} catch (NumberFormatException exception) {
			return null;
		}
	}
	
	private static List<String> parseLine(String line) {
		List<String> values = new ArrayList<>();
		StringBuilder current = new StringBuilder();
		boolean quoted = false;
		for (int i = 0; i < line.length(); i++) {
			char ch = line.charAt(i);
			if (quoted) {
				if (ch == '"') {
					if (i + 1 < line.length() && line.charAt(i + 1) == '"') {
						current.append('"');
						i++;
					} else {
						quoted = false;
					}
				} else {
					current.append(ch);
				}
			} else if (ch == '"') {
				quoted = true;
			} else if (ch == ',') {
				values.add(current.toString());
				current.setLength(0);
			} else {
				current.append(ch);
			}
		}
		values.add(current.toString());
		return values;
	}
	
	public static String describe(LegislativeOutputProfile profile) {
		return String.format(
				Locale.ROOT,
				"%s: volume=%s quality=%s weakMandate=%s rightsRisk=%s partisanSkew=%s volatility=%s legitimacy=%s",
				profile.sourceName(),
				Values.format3(profile.enactedVolume()),
				Values.format3(profile.legalQuality()),
				Values.format3(profile.weakMandateRate()),
				Values.format3(profile.rightsRisk()),
				Values.format3(profile.partisanSkew()),
				Values.format3(profile.volatility()),
				Values.format3(profile.publicLegitimacy())
		);
	}
}
