package constitutionalreview;

public final class TestSupport {
    private TestSupport() {
    }

    public static void check(boolean condition, String message) {
        if (!condition) {
            throw new AssertionError(message);
        }
    }

    public static void checkUnitInterval(double value, String name) {
        check(value >= 0.0 && value <= 1.0, name + " must be within [0,1], got " + value);
    }
}
