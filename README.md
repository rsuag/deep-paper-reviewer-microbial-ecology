# Deep Paper Reviewer for Environmental Microbial Ecology

A Codex skill for evidence-constrained peer review and revision of manuscripts in environmental microbiology, microbial ecology, and biogeochemistry.

**Try the STREAMS evidence map:** locate candidate manuscript passages for eight selected reporting items, then review each against the [official STREAMS guidelines](https://streamsmicrobiome.org/streams-guidelines/). The map does not assign compliance scores.

```bash
python3 deep-paper-reviewer/scripts/streams_map.py examples/mini-manuscript.md
python3 deep-paper-reviewer/scripts/streams_map.py /path/to/manuscript.docx --format json
```

The first command runs on a small synthetic example included here; the second accepts your own DOCX, Markdown, or UTF-8 text file. Paragraph numbers point back to the input. Search cues can miss valid reporting or match incomplete statements, so verify each candidate and mark non-applicable items yourself.

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
- An optional STREAMS evidence map for selected methods and data-sharing items.
- Surgical revision rules that preserve untouched manuscript content.

## License and Attribution

Licensed under CC BY-NC 4.0. See `NOTICE.md` for upstream attribution and adaptation details.

This independent tool draws on [Kelliher et al., *Nature Microbiology* (2025)](https://doi.org/10.1038/s41564-025-02186-2). It is not an official STREAMS checklist or a substitute for the [full guidance](https://streamsmicrobiome.org/streams-guidelines/). Cite the STREAMS paper for the guidelines and this repository separately for the software.
