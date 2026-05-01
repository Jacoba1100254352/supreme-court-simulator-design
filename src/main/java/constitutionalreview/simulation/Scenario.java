package constitutionalreview.simulation;

import constitutionalreview.institution.ReviewProcess;
import constitutionalreview.model.CaseWorld;

import java.util.Random;

public interface Scenario {
    String key();

    String name();

    ReviewProcess buildProcess(CaseWorld world, Random random);
}
