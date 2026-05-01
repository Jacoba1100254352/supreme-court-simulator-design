package constitutionalreview;

import constitutionalreview.importer.LegislativeOutputImporter;
import constitutionalreview.model.LegislativeOutputProfile;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public final class LegislativeOutputImporterTests {
    private LegislativeOutputImporterTests() {
    }

    public static void run() throws IOException {
        Path temp = Files.createTempFile("legislative-output", ".csv");
        Files.writeString(temp, """
                caseWeight,productivity,welfare,weakPublicMandatePassage,minorityHarm,lobbyCapture,policyShift,legitimacy
                1.0,0.40,0.70,0.20,0.10,0.30,0.25,0.65
                3.0,0.80,0.50,0.40,0.50,0.60,0.45,0.45
                """);
        LegislativeOutputProfile profile = LegislativeOutputImporter.importCsv(temp);
        TestSupport.check(profile.enactedVolume() > 0.65 && profile.enactedVolume() < 0.75, "weighted productivity should import");
        TestSupport.check(profile.rightsRisk() > 0.35 && profile.rightsRisk() < 0.45, "minority harm should map to rights risk");
        TestSupport.check(profile.publicLegitimacy() > 0.49 && profile.publicLegitimacy() < 0.56, "legitimacy should import");
        Files.deleteIfExists(temp);
    }
}
