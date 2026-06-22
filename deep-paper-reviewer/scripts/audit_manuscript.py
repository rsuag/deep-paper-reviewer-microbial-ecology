#!/usr/bin/env python3
"""Deterministic preflight for environmental microbial ecology manuscripts."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def read_paragraphs(path: Path) -> list[str]:
    if path.suffix.lower() == ".docx":
        with ZipFile(path) as archive:
            root = ET.fromstring(archive.read("word/document.xml"))
        return ["".join(node.text or "" for node in p.iter(W + "t")) for p in root.iter(W + "p")]
    return path.read_text(encoding="utf-8").splitlines()


def section_name(text: str, current: str) -> str:
    normalized = re.sub(r"^\d+(?:\.\d+)*\.?\s*", "", text.strip()).lower()
    for name in ("abstract", "introduction", "materials and methods", "methods", "results", "discussion", "conclusions", "references"):
        if normalized == name or normalized.startswith(name + " "):
            return name
    return current


def audit(paragraphs: list[str]) -> dict:
    findings = []
    sections = {}
    refs = {"figures": set(), "tables": set(), "datasets": set(), "supplementary": set()}
    current = "front matter"
    causal = re.compile(r"\b(drive[sd]?|driving|regulate[sd]?|control|controls|controlling|determine[sd]?|prove[sd]?|demonstrate[sd]?|adaptation)\b", re.I)
    citation = re.compile(r"\([A-Z][A-Za-z'\-]+(?: et al\.)?,?\s*\d{4}[a-z]?[^)]*\)")
    for number, raw in enumerate(paragraphs, 1):
        text = raw.strip()
        if not text:
            continue
        current = section_name(text, current)
        sections[current] = sections.get(current, 0) + 1
        for pattern, key in ((r"\bFig\.\s*S?\d+[a-z]?", "figures"), (r"\bTable\s*S?\d+", "tables"), (r"\bDataset\s*S?\d+", "datasets"), (r"\b(?:Fig\.|Table)\s*S\d+", "supplementary")):
            refs[key].update(re.findall(pattern, text, flags=re.I))
        if re.search(r"\?\?\?|\bTBD\b|\bTO\s*DO\b", text, re.I):
            findings.append({"severity": "high", "rule": "placeholder", "paragraph": number, "section": current, "text": text[:240]})
        if re.search(r"\b[Pp]\s*=\s*0\.000\b", text):
            findings.append({"severity": "medium", "rule": "p-zero", "paragraph": number, "section": current, "text": text[:240]})
        if current == "results" and citation.search(text):
            findings.append({"severity": "medium", "rule": "results-literature-citation", "paragraph": number, "section": current, "text": text[:240]})
        causal_text = re.sub(
            r"(?:statistical )?significance was determined|\b(?:not|never) demonstrated\b|\bhas not been demonstrated\b|\b(?:rather than|do not|does not|cannot) demonstrate\w*",
            "",
            text,
            flags=re.I,
        )
        if current in {"results", "discussion", "conclusions"} and causal.search(causal_text):
            findings.append({"severity": "review", "rule": "causal-language", "paragraph": number, "section": current, "text": text[:240]})
        niche_claim = re.search(r"niche breadth.{0,100}(tolerance|generalist|specialist)", text, re.I)
        explicit_caution = re.search(r"rather than|does not|cannot|not (?:a )?direct|not measuring", text, re.I)
        if current != "references" and niche_claim and not explicit_caution:
            findings.append({"severity": "review", "rule": "niche-inference", "paragraph": number, "section": current, "text": text[:240]})
        mag_activity = re.search(
            r"\bMAGs?\b.{0,60}\b(?:demonstrate[sd]?|show(?:ed|s)?|confirm(?:ed|s)?|reveal(?:ed|s)?)\b.{0,60}\b(?:activity|expression|process rates?|nitrification rates?)\b"
            r"|\b(?:activity|expression|process rates?|nitrification rates?)\b.{0,60}\bMAGs?\b",
            text,
            re.I,
        )
        if current != "references" and mag_activity:
            findings.append({"severity": "review", "rule": "mag-activity-inference", "paragraph": number, "section": current, "text": text[:240]})
    return {
        "paragraph_count": len(paragraphs),
        "section_nonempty_paragraphs": sections,
        "cross_references": {key: sorted(values) for key, values in refs.items()},
        "findings": findings,
        "note": "Screening findings require scientific review; they are not automatic errors.",
    }


def markdown(report: dict) -> str:
    lines = ["# Manuscript Preflight", "", f"Paragraphs scanned: {report['paragraph_count']}", "", "## Findings", ""]
    if not report["findings"]:
        lines.append("No configured signals detected.")
    else:
        lines.append("| Severity | Rule | Paragraph | Section | Excerpt |")
        lines.append("|---|---|---:|---|---|")
        for item in report["findings"]:
            excerpt = item["text"].replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {item['severity']} | {item['rule']} | {item['paragraph']} | {item['section']} | {excerpt} |")
    lines.extend(["", "## Cross-References", ""])
    for key, values in report["cross_references"].items():
        lines.append(f"- {key}: {', '.join(values) if values else 'none detected'}")
    lines.extend(["", f"> {report['note']}"])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manuscript", type=Path)
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = audit(read_paragraphs(args.manuscript))
    content = json.dumps(report, indent=2, ensure_ascii=False) + "\n" if args.format == "json" else markdown(report)
    if args.output:
        args.output.write_text(content, encoding="utf-8")
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
