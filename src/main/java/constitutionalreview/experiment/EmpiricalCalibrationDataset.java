package constitutionalreview.experiment;

import constitutionalreview.util.Values;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Set;
import java.util.stream.Stream;

public final class EmpiricalCalibrationDataset {
    private final Path sourceDirectory;
    private final List<CalibrationObservation> observations;
    private final Map<String, List<CalibrationObservation>> byMetric;

    private EmpiricalCalibrationDataset(Path sourceDirectory, List<CalibrationObservation> observations) {
        this.sourceDirectory = sourceDirectory;
        this.observations = List.copyOf(observations);
        Map<String, List<CalibrationObservation>> grouped = new LinkedHashMap<>();
        for (CalibrationObservation observation : observations) {
            grouped.computeIfAbsent(observation.metric(), ignored -> new ArrayList<>()).add(observation);
        }
        this.byMetric = grouped;
    }

    public static EmpiricalCalibrationDataset load(Path sourceDirectory) throws IOException {
        if (sourceDirectory == null || !Files.isDirectory(sourceDirectory)) {
            return new EmpiricalCalibrationDataset(sourceDirectory, List.of());
        }
        List<CalibrationObservation> observations = new ArrayList<>();
        try (Stream<Path> paths = Files.list(sourceDirectory)) {
            for (Path path : paths
                    .filter(Files::isRegularFile)
                    .filter(path -> path.getFileName().toString().endsWith(".csv"))
                    .sorted()
                    .toList()) {
                observations.addAll(readCsv(path));
            }
        }
        observations.sort(Comparator
                .comparing(CalibrationObservation::metric)
                .thenComparing(CalibrationObservation::term)
                .thenComparing(CalibrationObservation::sourceKey));
        return new EmpiricalCalibrationDataset(sourceDirectory, observations);
    }

    public List<CalibrationObservation> observations() {
        return observations;
    }

    public CalibrationRange range(String metric, double fallbackMin, double fallbackMax, double tolerance) {
        List<CalibrationObservation> values = byMetric.getOrDefault(metric, List.of());
        if (values.isEmpty()) {
            return new CalibrationRange(
                    metric,
                    fallbackMin,
                    fallbackMax,
                    Values.average(fallbackMin, fallbackMax),
                    0,
                    "",
                    "",
                    "fallback",
                    false
            );
        }
        List<Double> sorted = values.stream()
                .map(CalibrationObservation::value)
                .sorted()
                .toList();
        double sourceMin = sorted.get(0);
        double sourceMax = sorted.get(sorted.size() - 1);
        double width = sourceMax - sourceMin;
        double empiricalTolerance = Math.max(tolerance, Math.max(0.015, width * 0.25));
        double min = Values.clamp01(sourceMin - empiricalTolerance);
        double max = Values.clamp01(sourceMax + empiricalTolerance);
        return new CalibrationRange(
                metric,
                min,
                max,
                percentile(sorted, 0.50),
                values.size(),
                termRange(values),
                sourceKeys(values),
                "source-min-max-plus-tolerance",
                true
        );
    }

    public String sourceRangesCsv() {
        StringBuilder builder = new StringBuilder();
        builder.append(String.join(",",
                "metric",
                "observations",
                "termRange",
                "sourceKeys",
                "rawMin",
                "p05",
                "median",
                "p95",
                "rawMax"
        )).append('\n');
        byMetric.entrySet().stream()
                .sorted(Map.Entry.comparingByKey())
                .forEach(entry -> {
                    List<Double> values = entry.getValue().stream()
                            .map(CalibrationObservation::value)
                            .sorted()
                            .toList();
                    builder.append(Values.csv(entry.getKey())).append(',')
                            .append(entry.getValue().size()).append(',')
                            .append(Values.csv(termRange(entry.getValue()))).append(',')
                            .append(Values.csv(sourceKeys(entry.getValue()))).append(',')
                            .append(format(values.get(0))).append(',')
                            .append(format(percentile(values, 0.05))).append(',')
                            .append(format(percentile(values, 0.50))).append(',')
                            .append(format(percentile(values, 0.95))).append(',')
                            .append(format(values.get(values.size() - 1)))
                            .append('\n');
                });
        return builder.toString();
    }

    public String appendixMarkdown() {
        StringBuilder builder = new StringBuilder();
        builder.append("# Empirical Calibration Appendix v4\n\n");
        builder.append("Normalized source observations used to compute calibration ranges. The simulator does not read raw SCDB or shadow-docket archives at runtime; those large files are reduced into term-level source rows under `")
                .append(sourceDirectory == null ? "data/calibration" : sourceDirectory)
                .append("`.\n\n");
        builder.append("## Source Range Summary\n\n");
        builder.append("| Metric | Obs. | Terms | Sources | Raw min | P05 | Median | P95 | Raw max |\n");
        builder.append("| --- | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |\n");
        byMetric.entrySet().stream()
                .sorted(Map.Entry.comparingByKey())
                .forEach(entry -> {
                    List<Double> values = entry.getValue().stream()
                            .map(CalibrationObservation::value)
                            .sorted()
                            .toList();
                    builder.append("| `")
                            .append(entry.getKey())
                            .append("` | ")
                            .append(entry.getValue().size())
                            .append(" | ")
                            .append(termRange(entry.getValue()))
                            .append(" | ")
                            .append(sourceKeys(entry.getValue()))
                            .append(" | ")
                            .append(format(values.get(0)))
                            .append(" | ")
                            .append(format(percentile(values, 0.05)))
                            .append(" | ")
                            .append(format(percentile(values, 0.50)))
                            .append(" | ")
                            .append(format(percentile(values, 0.95)))
                            .append(" | ")
                            .append(format(values.get(values.size() - 1)))
                            .append(" |\n");
                });
        builder.append("\n## Source Files\n\n");
        sourceFiles().forEach(file -> builder.append("- `").append(file).append("`\n"));
        return builder.toString();
    }

    private List<String> sourceFiles() {
        if (sourceDirectory == null || !Files.isDirectory(sourceDirectory)) {
            return List.of();
        }
        try (Stream<Path> paths = Files.list(sourceDirectory)) {
            return paths
                    .filter(Files::isRegularFile)
                    .filter(path -> path.getFileName().toString().endsWith(".csv"))
                    .map(path -> path.getFileName().toString())
                    .sorted()
                    .toList();
        } catch (IOException exception) {
            return List.of();
        }
    }

    private static List<CalibrationObservation> readCsv(Path path) throws IOException {
        List<String> lines = Files.readAllLines(path);
        if (lines.isEmpty()) {
            return List.of();
        }
        List<String> headers = parseCsvLine(lines.get(0));
        Map<String, Integer> columns = new LinkedHashMap<>();
        for (int i = 0; i < headers.size(); i++) {
            columns.put(headers.get(i), i);
        }
        List<CalibrationObservation> observations = new ArrayList<>();
        for (int i = 1; i < lines.size(); i++) {
            if (lines.get(i).isBlank()) {
                continue;
            }
            List<String> row = parseCsvLine(lines.get(i));
            observations.add(new CalibrationObservation(
                    get(row, columns, "sourceKey"),
                    get(row, columns, "domain"),
                    get(row, columns, "metric"),
                    get(row, columns, "term"),
                    parseDouble(get(row, columns, "numerator")),
                    parseDouble(get(row, columns, "denominator")),
                    parseDouble(get(row, columns, "value")),
                    get(row, columns, "sourceUrl"),
                    get(row, columns, "notes")
            ));
        }
        return observations;
    }

    private static List<String> parseCsvLine(String line) {
        List<String> values = new ArrayList<>();
        StringBuilder current = new StringBuilder();
        boolean quoted = false;
        for (int i = 0; i < line.length(); i++) {
            char ch = line.charAt(i);
            if (ch == '"') {
                if (quoted && i + 1 < line.length() && line.charAt(i + 1) == '"') {
                    current.append('"');
                    i++;
                } else {
                    quoted = !quoted;
                }
            } else if (ch == ',' && !quoted) {
                values.add(current.toString());
                current.setLength(0);
            } else {
                current.append(ch);
            }
        }
        values.add(current.toString());
        return values;
    }

    private static String get(List<String> row, Map<String, Integer> columns, String column) {
        Integer index = columns.get(column);
        if (index == null || index >= row.size()) {
            return "";
        }
        return row.get(index);
    }

    private static double parseDouble(String value) {
        if (value == null || value.isBlank()) {
            return 0.0;
        }
        return Double.parseDouble(value);
    }

    private static double percentile(List<Double> sorted, double percentile) {
        if (sorted.isEmpty()) {
            return 0.0;
        }
        double raw = percentile * (sorted.size() - 1);
        int lower = (int) Math.floor(raw);
        int upper = (int) Math.ceil(raw);
        if (lower == upper) {
            return sorted.get(lower);
        }
        double fraction = raw - lower;
        return sorted.get(lower) * (1.0 - fraction) + sorted.get(upper) * fraction;
    }

    private static String termRange(List<CalibrationObservation> observations) {
        List<String> terms = observations.stream()
                .map(CalibrationObservation::term)
                .sorted()
                .toList();
        if (terms.isEmpty()) {
            return "";
        }
        if (terms.size() == 1) {
            return terms.get(0);
        }
        return terms.get(0) + "-" + terms.get(terms.size() - 1);
    }

    private static String sourceKeys(List<CalibrationObservation> observations) {
        Set<String> keys = new LinkedHashSet<>();
        for (CalibrationObservation observation : observations) {
            keys.add(observation.sourceKey());
        }
        return String.join(";", keys);
    }

    private static String format(double value) {
        return String.format(Locale.ROOT, "%.3f", value);
    }

    public record CalibrationObservation(
            String sourceKey,
            String domain,
            String metric,
            String term,
            double numerator,
            double denominator,
            double value,
            String sourceUrl,
            String notes
    ) {
    }

    public record CalibrationRange(
            String metric,
            double min,
            double max,
            double median,
            int observations,
            String termRange,
            String sourceKeys,
            String basis,
            boolean empirical
    ) {
    }
}
