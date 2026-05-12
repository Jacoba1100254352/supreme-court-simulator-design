package constitutionalreview.institution;

public enum JudicialSelectorPool {
    NOT_APPLICABLE(
            "Not applicable",
            0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0
    ),
    ALL_FEDERAL_JUDGES(
            "All Article III federal judges",
            870,
            0.78,
            0.62,
            0.18,
            0.18,
            0.06
    ),
    FEDERAL_APPELLATE_JUDGES(
            "Federal appellate judges",
            180,
            0.84,
            0.44,
            0.24,
            0.13,
            0.04
    ),
    SELECTED_CIRCUITS(
            "Judges from selected circuits",
            90,
            0.74,
            0.24,
            0.38,
            0.22,
            0.03
    ),
    STATE_SUPREME_COURT_JUSTICES(
            "State supreme court justices",
            350,
            0.68,
            0.56,
            0.28,
            0.18,
            0.06
    ),
    FEDERAL_AND_STATE_HIGH_COURT_JUDGES(
            "Federal and state high-court judges",
            1_250,
            0.76,
            0.78,
            0.16,
            0.20,
            0.08
    );

    private final String label;
    private final int approximateVoters;
    private final double professionalInsulation;
    private final double jurisdictionalBreadth;
    private final double captureRisk;
    private final double selectionNoise;
    private final double administrativeCost;

    JudicialSelectorPool(
            String label,
            int approximateVoters,
            double professionalInsulation,
            double jurisdictionalBreadth,
            double captureRisk,
            double selectionNoise,
            double administrativeCost
    ) {
        this.label = label;
        this.approximateVoters = approximateVoters;
        this.professionalInsulation = professionalInsulation;
        this.jurisdictionalBreadth = jurisdictionalBreadth;
        this.captureRisk = captureRisk;
        this.selectionNoise = selectionNoise;
        this.administrativeCost = administrativeCost;
    }

    public String label() {
        return label;
    }

    public int approximateVoters() {
        return approximateVoters;
    }

    public double professionalInsulation() {
        return professionalInsulation;
    }

    public double jurisdictionalBreadth() {
        return jurisdictionalBreadth;
    }

    public double captureRisk() {
        return captureRisk;
    }

    public double selectionNoise() {
        return selectionNoise;
    }

    public double administrativeCost() {
        return administrativeCost;
    }
}
