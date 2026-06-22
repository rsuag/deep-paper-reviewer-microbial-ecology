# Statistics and Reproducibility

## Universal Checks

- Match the unit of replication to the inferential unit; identify nested sites, plots, cores, technical replicates, and pairwise distances.
- Check transformations, zero handling, normalization, filtering thresholds, missingness, and multiple-testing correction.
- Report sample size, effect estimate, uncertainty, test, permutation count, and correction method where applicable.
- Verify every value against code output, figure, table, or dataset rather than copying prose between versions.
- Distinguish exploratory analyses from hypothesis tests.

## Community Ecology

- For alpha/gamma diversity, state metric and sampling normalization.
- For beta diversity, distinguish location from dispersion; use PERMANOVA and dispersion checks appropriately.
- For distance-decay, account for non-independence of pairwise distances and report the tested association separately from the plotted regression.
- For RDA/dbRDA, document transformation, variable selection, collinearity control, permutation design, and total explained variation.
- For Mantel/MRM, avoid causal interpretation and check spatial dependence and predictor collinearity.
- For VPA, identify exact predictor sets and adjusted fractions; negative or shared fractions require careful reporting.
- For NST/null models, report null model, distance metric, randomizations, grouping, small-group limitations, and sensitivity.
- For network analysis, do not equate association edges with interactions; check compositionality and stability.

## Niche and Distribution Metrics

- A Levins value from taxa-by-sample abundance is a realized sample-distribution measure.
- State the sample universe, prevalence threshold, abundance transformation, and whether zeros were structural or filtered.
- Keep occupancy, evenness across samples, local dominance, and social/community-context niche breadth separate.
- A broad observed distribution does not establish physiological tolerance or adaptation.

## Genome-Resolved Evidence

- Report MAG completeness, contamination, dereplication, taxonomy database/version, and novelty thresholds.
- Treat gene presence as metabolic potential and gene non-recovery as ambiguous in incomplete MAGs.
- Require pathway-level claims to specify completeness criteria and annotation evidence.
- Do not infer expression, substrate use, or process rate from gene presence alone.
- Keep reference genomes and newly recovered MAG counts distinct.

## Reproducibility Gate

For each headline number, record the generating script, input, output, software/version, parameters, random seed or permutation count, and manuscript destination. A value that cannot be regenerated is `UNVERIFIABLE`, not approximately correct.
