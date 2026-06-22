# Modes and Output

## Quick

Use for triage. Output rejection risk, top five concerns, strongest novelty, and three immediate actions.

## Full

Run all six review lenses. Output:

1. Overall assessment and rejection risk.
2. Major concerns, ordered by severity.
3. Minor concerns.
4. Overstated claims with replacements.
5. Missing Results-Discussion links.
6. Figure, SI, dataset, and reference audit.
7. Required versus optional analyses.
8. Revision priorities.
9. Three to five directly usable rewrites.

## Methods

Focus on design, sampling hierarchy, transformations, compositionality, model assumptions, effect sizes, multiple testing, reproducibility, and agreement between code, tables, and prose.

## Revision

Produce a rule-to-edit map before editing. For every change record: rule, source location, old claim, new claim, evidence basis, and whether the edit is scientific, logical, numerical, cross-reference, or language-only. Preserve the source and create a new marked version.

## Re-Review

Use a traceability matrix:

| Original concern | Required action | Revised location | Verified evidence | Status | Residual risk |
|---|---|---|---|---|---|

Allowed statuses: `RESOLVED`, `PARTLY_RESOLVED`, `NOT_RESOLVED`, `NEW_CONCERN`, `UNVERIFIABLE`.

Do not accept an author's response as proof. Verify the revised manuscript and underlying result.

## Decision Calibration

- **Reject risk:** central question or design cannot support the claimed contribution.
- **Major revision:** core evidence exists, but interpretation, validation, or structure requires substantial correction.
- **Minor revision:** conclusions are supported and remaining issues do not change the central interpretation.
- **Ready:** no material evidence-chain failure remains; routine editorial checks may remain.
