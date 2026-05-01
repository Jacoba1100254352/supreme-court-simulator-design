package constitutionalreview.util;

import java.util.Locale;

public final class Values {
    private Values() {
    }

    public static double clamp01(double value) {
        if (Double.isNaN(value)) {
            return 0.0;
        }
        return Math.max(0.0, Math.min(1.0, value));
    }

    public static double clamp(double value, double min, double max) {
        if (Double.isNaN(value)) {
            return min;
        }
        return Math.max(min, Math.min(max, value));
    }

    public static double average(double... values) {
        if (values.length == 0) {
            return 0.0;
        }
        double total = 0.0;
        for (double value : values) {
            total += clamp01(value);
        }
        return total / values.length;
    }

    public static String format3(double value) {
        return String.format(Locale.ROOT, "%.3f", value);
    }

    public static String csv(String value) {
        if (value == null) {
            return "";
        }
        boolean quoted = value.indexOf(',') >= 0 || value.indexOf('"') >= 0 || value.indexOf('\n') >= 0 || value.indexOf('\r') >= 0;
        String escaped = value.replace("\"", "\"\"");
        return quoted ? "\"" + escaped + "\"" : escaped;
    }
}
