# Deep Paper Reviewer for Environmental Microbial Ecology

A Codex skill for evidence-constrained peer review and revision of manuscripts in environmental microbiology, microbial ecology, and biogeochemistry.

It combines a compact multi-perspective review and re-review workflow adapted from [Academic Research Skills](https://github.com/imbad0202/academic-research-skills) with domain-specific safeguards for amplicon sequencing, metagenomic read profiles, MAGs, ecological null models, multivariate statistics, and biogeochemical interpretation.

## Install

Copy the `deep-paper-reviewer` directory into `~/.codex/skills/`, then invoke it as `$deep-paper-reviewer`.

```bash
cp -R deep-paper-reviewer ~/.codex/skills/
```

## What It Adds

- Five modes: quick, full, methods, revision, and re-review.
- Claim-to-evidence tracking instead of language-only review.
- Explicit separation of amplicon, read-based, MAG, transcript, and process-rate evidence.
- Domain checks for VPA, RDA, Mantel/MRM, NST/null models, niche breadth, diversity, and distance-decay analyses.
- Figure, SI, dataset, citation, and numerical consistency audits.
- A deterministic preflight scanner for DOCX, Markdown, and plain text.
- Surgical revision rules that preserve untouched manuscript content.

## License and Attribution

Licensed under CC BY-NC 4.0. See `NOTICE.md` for upstream attribution and adaptation details.
