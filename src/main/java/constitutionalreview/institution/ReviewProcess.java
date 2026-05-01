package constitutionalreview.institution;

import constitutionalreview.model.CourtState;
import constitutionalreview.model.ReviewCase;

import java.util.Random;

public interface ReviewProcess {
    CourtDecision review(ReviewCase reviewCase, CourtState state, Random random);
}
