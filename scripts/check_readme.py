#!/usr/bin/env python3
"""Offline validation of the curated list; no third-party dependencies."""

from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ENTRY = re.compile(
    r"^- \*\*\[(\d{4}-\d{2}-\d{2})\] (.+?)\*\* — `(Core|GUI|Construction|Related|Benchmark|Perspective)`",
    re.MULTILINE,
)
PAPER = re.compile(r"\[Paper\]\(https://arxiv\.org/abs/(\d{4}\.\d{4,5})\)")
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\s]+)\)")


def validate(root=ROOT):
    text = (root / "README.md").read_text(encoding="utf-8")
    errors = []
    seen = set()
    count = 0
    snapshot = re.search(r"Search and verification date: \*\*(\d{4}-\d{2}-\d{2})\*\*", (root / "SOURCES.md").read_text())
    if not snapshot:
        return ["Missing snapshot date in SOURCES.md"], 0
    cutoff = date.fromisoformat(snapshot.group(1))
    for section in re.split(r"^## ", text, flags=re.MULTILINE):
        entries = list(ENTRY.finditer(section))
        previous = None
        for index, entry in enumerate(entries):
            count += 1
            value, title, _ = entry.groups()
            try:
                submitted = date.fromisoformat(value)
            except ValueError:
                errors.append(f"Invalid date: {value} ({title})")
                continue
            if submitted > cutoff:
                errors.append(f"Entry is newer than the search snapshot: {title}")
            if previous is not None and submitted > previous:
                errors.append(f"Not newest-first within category: {title}")
            previous = submitted
            end = entries[index + 1].start() if index + 1 < len(entries) else len(section)
            body = section[entry.end():end]
            papers = PAPER.findall(body)
            if len(papers) != 1:
                errors.append(f"Expected one arXiv paper link: {title}")
            for paper in papers:
                if paper in seen:
                    errors.append(f"Duplicate paper: {paper}")
                seen.add(paper)
    if len(PAPER.findall(text)) != count:
        errors.append("Paper links and recognized entries differ; check entry formatting")
    advertised = re.search(r"\*\*(\d+) papers\*\*", text)
    if not advertised or int(advertised.group(1)) != count:
        errors.append(f"README paper count must equal {count}")
    source_count = re.search(r"\*\*(\d+) distinct papers\*\*", (root / "SOURCES.md").read_text())
    if not source_count or int(source_count.group(1)) != count:
        errors.append(f"SOURCES paper count must equal {count}")
    headings = {
        re.sub(r"[^\w\s-]", "", heading.lower()).replace(" ", "-")
        for heading in re.findall(r"^#{1,6} (.+)$", text, re.MULTILINE)
    }
    for url in LINK.findall(text):
        if url.startswith("#"):
            if url[1:] not in headings:
                errors.append(f"Missing README anchor: {url}")
        elif not re.match(r"[a-z][a-z0-9+.-]*:", url):
            if not (root / url.split("#", 1)[0]).exists():
                errors.append(f"Missing local target: {url}")
    for path in root.rglob("*.md"):
        for url in LINK.findall(path.read_text(encoding="utf-8")):
            if re.match(r"[a-z][a-z0-9+.-]*:", url) or url.startswith("#"):
                continue
            if not (path.parent / url.split("#", 1)[0]).exists():
                errors.append(f"Missing local target in {path.relative_to(root)}: {url}")
    return errors, count


if __name__ == "__main__":
    errors, count = validate()
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        sys.exit(1)
    print(f"PASS: {count} unique papers; dates, ordering, counts, anchors, and local links checked.")
