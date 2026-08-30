# Lower-Court Precedent Treatment Summary v1

This report summarizes the public replication file for Masood, Kassow, and Songer (2019). The file contains one row per formally argued U.S. Supreme Court precedent and aggregate Shepard's lower-court response counts through 2016. It is direct doctrinal-uptake evidence, but it is not an individual-opinion extract or a practical-implementation compliance rate.

| Subset | Precedents | Cited only | Followed | Adverse | Followed / directional | Followed / cited-or-followed | Adverse / cited-or-adverse |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| All source precedents | 876 | 959329 | 235256 | 38297 | 86.000% | 19.694% | 3.839% |
| Published main-model rows | 861 | 955702 | 234076 | 38207 | 85.968% | 19.674% | 3.844% |
| Constitutional-issue precedents | 223 | 249777 | 47370 | 17753 | 72.739% | 15.942% | 6.636% |

Evidence boundary:

- The source-decision universe covers the 1995-2004 Supreme Court terms; lower-court responses are accumulated through 2016.
- The article defines `followed` as a positive treatment. The generated adverse count equals the source's other negative-treatment count plus its separate distinguished count.
- The 876-row file reconciles to the article's descriptive statistics. Exactly 861 rows have every field used by the main published models.
- The 223-row constitutional-issue subset is source-flagged; it is not a new hand-coded constitutional-case classification.
- Aggregate counts weight heavily treated precedents more heavily than lightly treated precedents and omit non-citing or ignored exposed cases.
- The public Dataverse release is CC0-1.0, but the underlying treatment categories were compiled by the study authors from Shepard's Citations. Individual treatment-event records are not present in the released file.
- Use these values as bounded doctrinal-uptake context only. They do not validate practical implementation, government compliance, remedy fidelity, or the simulator's synthetic case-average `lowerCourtCompliance` score.

Source: [Replication Data for: The Aggregate Dynamics of Lower Court Responses to the U.S. Supreme Court](https://doi.org/10.7910/DVN/DZZY7G); article DOI: [10.1086/703067](https://doi.org/10.1086/703067).
