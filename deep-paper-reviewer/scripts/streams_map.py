#!/usr/bin/env python3
"""Locate manuscript passages for a small, reviewable subset of STREAMS items."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from audit_manuscript import read_paragraphs

SOURCE = "https://doi.org/10.1038/s41564-025-02186-2"
GUIDELINES = "https://streamsmicrobiome.org/streams-guidelines/"

# Short labels and search cues are original to this tool; consult STREAMS for full guidance.
ITEMS = (
    ("3.2", "Environmental context and location", r"\b(?:geograph\w*|latitude|longitude|coordinates?|sampling sites?|study sites?)\b"),
    ("6.3", "Sequencing methods", r"\b(?:sequenc\w*|illumina|nanopore|pacbio|read length|paired.end)\b"),
    ("7", "Bioinformatics analyses", r"\b(?:bioinformatic\w*|qiime\w*|dada2|kraken2|metaphlan|assembly pipeline|analysis workflow)\b"),
    ("7.3", "Database information", r"\b(?:reference database|taxonomic database|silva|gtdb|greengenes|unite database)\b"),
    ("7.4", "Statistical methods", r"\b(?:statistic\w*|permutation|anova|regression|false discovery rate|fdr|confidence interval)\b"),
    ("8.2", "Raw data access", r"\b(?:raw data|raw reads?|sequence reads?|sra|ena|ddbj|bioproject|accession number)\b"),
    ("8.4", "Software and source code access", r"\b(?:github|gitlab|source code|code availability|software availability)\b"),
    ("8.5", "Reproducible research", r"\b(?:reproducib\w*|container\w*|conda|environment file|workflow version|random seed)\b"),
)


def evidence_map(paragraphs: list[str]) -> dict:
    """Return candidate locations, never a compliance or completeness verdict."""
    candidates = {item_id: [] for item_id, _, _ in ITEMS}
    for number, raw in enumerate(paragraphs, 1):
        text = " ".join(raw.split())
        heading = re.sub(r"^#{1,6}\s*", "", text)
        if re.match(r"^(?:\d+[. ]+)?references\s*$", heading, re.I):
            break
        if not text:
            continue
        for item_id, _, cue in ITEMS:
            if len(candidates[item_id]) < 3 and re.search(cue, text, re.I):
                candidates[item_id].append({"paragraph": number, "excerpt": text[:220]})
    return {
        "source": SOURCE,
        "guidelines": GUIDELINES,
        "scope": "Eight selected STREAMS v1.0 items; keyword-based candidate locations only.",
        "items": [
            {"id": item_id, "label": label, "candidates": candidates[item_id]}
            for item_id, label, _ in ITEMS
        ],
        "note": "A match does not establish completeness. No match does not establish omission. Check applicability, evidence, and the full guidelines manually.",
    }


def markdown(report: dict) -> str:
    lines = [
        "# STREAMS evidence map",
        "",
        f"Selected items from [STREAMS]({report['source']}); consult the [full guidelines]({report['guidelines']}).",
        "",
        report["scope"],
        "",
        "| Item | Reporting area | Candidate paragraphs |",
        "|---|---|---|",
    ]
    for item in report["items"]:
        locations = ", ".join(str(c["paragraph"]) for c in item["candidates"])
        lines.append(f"| {item['id']} | {item['label']} | {locations or 'No keyword candidate'} |")
    lines.extend(["", "## Candidate excerpts", ""])
    for item in report["items"]:
        if item["candidates"]:
            lines.append(f"### {item['id']} {item['label']}")
            lines.append("")
            for candidate in item["candidates"]:
                lines.append(f"- Paragraph {candidate['paragraph']}: {candidate['excerpt']}")
            lines.append("")
    lines.extend([f"> {report['note']}", ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manuscript", type=Path, help="DOCX, Markdown, or UTF-8 text manuscript")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = evidence_map(read_paragraphs(args.manuscript))
    content = json.dumps(report, indent=2, ensure_ascii=False) + "\n" if args.format == "json" else markdown(report)
    if args.output:
        args.output.write_text(content, encoding="utf-8")
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
