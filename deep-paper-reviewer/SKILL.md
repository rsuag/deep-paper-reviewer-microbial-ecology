---
name: deep-paper-reviewer
description: Deep scientific review, evidence audit, and constrained revision for environmental microbiology, microbial ecology, and biogeochemistry manuscripts. Use for pre-submission review, reviewer simulation, methods/statistics checks, DOCX or Markdown manuscript revision, response-to-reviewers work, re-review, figure/SI/dataset audits, citation verification, or interpretation of amplicon, metagenomic-read, MAG, transcript, process-rate, RDA/VPA/Mantel/MRM/NST, niche-breadth, diversity, and distance-decay results.
---

# Deep Paper Reviewer

## Start

1. Identify the requested mode: `quick`, `full`, `methods`, `revision`, or `re-review`. Default to `full` for assessment and `revision` when the user asks for file edits.
2. Record the target journal, authoritative manuscript version, permitted edit scope, marking method, and available source data.
3. Read only the references required by the chosen mode:
   - Always read [review-framework.md](references/review-framework.md).
   - For statistical or methodological claims, read [statistics-and-reproducibility.md](references/statistics-and-reproducibility.md).
   - For editing or reviewer responses, read [revision-protocol.md](references/revision-protocol.md).
   - For modes and output schemas, read [modes-and-output.md](references/modes-and-output.md).
4. Run `scripts/audit_manuscript.py` on DOCX, Markdown, or text manuscripts when local file access is available. Treat its findings as screening signals, not final scientific judgments.

## Evidence-First Workflow

1. State the paper's central question, hypotheses, claimed novelty, and core conclusion in one sentence each.
2. Build a claim-evidence ledger for every major conclusion: claim, evidence layer, source location, inference level, alternative explanation, and verdict.
3. Review through six non-overlapping lenses: scientific logic, methods/statistics, domain mechanism, language/journal style, figures/data traceability, and adversarial rejection risk.
4. Label interpretive statements as `SUPPORTED`, `REASONABLE_INFERENCE`, `TESTABLE_HYPOTHESIS`, `UNSUPPORTED`, or `UNVERIFIABLE`.
5. Synthesize duplicate concerns and rank them as rejection risk, major revision, minor revision, or optional improvement.
6. In revision mode, convert accepted concerns into explicit rules, make only traceable edits, and preserve untouched text and document objects.
7. Re-run the evidence ledger, deterministic audit, numerical cross-check, and a fresh reviewer simulation.

## Non-Negotiable Domain Rules

- Never invent data, results, references, accession numbers, or mechanisms.
- Do not turn associations into drivers, controls, regulation, adaptation, or causation.
- Treat latitude and geographic distance as organizing gradients or correlates unless the design identifies causal effects.
- Keep amplicon ASVs, metagenomic read profiles, MAG gene content, transcripts, proteins, and measured process rates distinct.
- Describe MAG gene presence as genomic or metabolic potential. Treat non-recovery cautiously when MAGs are incomplete.
- Treat Levins-type sample-matrix values as realized sample niche breadth or a sample-occupancy-based proxy, not physiological tolerance.
- Separate occupancy, community-context heterogeneity, and local dominance. Do not collapse them into `generalist` or `specialist` without matching analyses.
- Distinguish alpha diversity, beta-compositional dispersion, beta-diversity turnover, distance-decay, and gamma diversity.
- Interpret VPA fractions as model-explained, shared, and residual variation, not causal partitioning.
- Interpret NST and other null-model outputs as model-dependent assembly signatures, not proof of a single ecological process.
- Prefer the narrative: broad community-scale pattern, finer ASV or lineage sorting, then genome-resolved metabolic hypotheses.
- Require every figure, table, SI item, dataset citation, number, and statistical statement to match its source.

## Review Independence

When multi-agent tools are available, run the six review lenses independently before synthesis. When they are unavailable, perform separate passes and do not claim that independent agents were used. The final editor may consolidate or arbitrate findings but may not fabricate reviewer comments.

## Revision Safety

- Never overwrite the authoritative source unless explicitly requested.
- Preserve citation fields, embedded figures, styles, and unrelated user edits.
- Mark only changed text using the requested method.
- Do not perform a full-document rewrite for a targeted request.
- Separate evidence correction from stylistic preference.
- Report remaining risks that editing cannot solve.

## Upstream Basis

This workflow adapts selected reviewer-panel, claim-verification, revision, and re-review concepts from Cheng-I Wu's Academic Research Skills under CC BY-NC 4.0. See the repository-level `NOTICE.md`. The domain rules and audit workflow here are specialized for environmental microbial ecology.
