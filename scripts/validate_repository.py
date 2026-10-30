#!/usr/bin/env python3
"""Offline checks for bibliography, publication scope, assets and local links."""

import re
import sys
import unicodedata
from datetime import date
from urllib.parse import unquote, urlsplit

from build_paper_index import GROUPS, ROOT, load_papers, render


def anchors(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    found = set(re.findall(r'<a\s+id="([^"]+)"', text))
    used = {}
    for heading in re.findall(r"^#{1,6}\s+(.+)$", text, re.M):
        heading = re.sub(r"<[^>]+>", "", heading).lower()
        slug = "".join(c for c in heading if c in "-_ " or
                       unicodedata.category(c)[0] not in "PS")
        slug = slug.replace(" ", "-")
        number = used.get(slug, 0)
        used[slug] = number + 1
        found.add(f"{slug}-{number}" if number else slug)
    return found


def validate():
    errors = []
    papers = load_papers()
    files = sorted(p for p in ROOT.rglob("*") if p.is_file() and
                   not {".git", ".validation", "__pycache__"}.intersection(p.relative_to(ROOT).parts))
    source_dirs = {"materials", "source-materials", "raw-materials"}
    presentation_formats = {".ppt", ".pptx", ".pptm", ".key", ".odp"}
    for path in files:
        relative = path.relative_to(ROOT)
        if (relative.parts[0] in source_dirs or path.suffix.lower() in presentation_formats
                or relative.as_posix() == "data/materials.json"):
            errors.append(f"Original research files must stay outside the repository: {relative}")

    ids, urls = set(), set()
    groups = {key for key, _ in GROUPS}
    for paper in papers:
        for key in ["id", "name", "title", "paper", "collection", "summary_zh"]:
            if not paper.get(key):
                errors.append(f"Missing {key}: {paper.get('id')}")
        if paper["id"] in ids or paper["paper"] in urls:
            errors.append(f"Duplicate paper: {paper['id']}")
        ids.add(paper["id"])
        urls.add(paper["paper"])
        if not paper["paper"].startswith("https://"):
            errors.append(f"Non-HTTPS paper link: {paper['id']}")
        if paper["collection"] not in groups:
            errors.append(f"Unknown collection: {paper['id']}")
        if paper.get("first_submitted"):
            try:
                date.fromisoformat(paper["first_submitted"])
            except ValueError:
                errors.append(f"Invalid first_submitted: {paper['id']}")
        if "sources" in paper:
            errors.append(f"Internal source mappings must not be published: {paper['id']}")

    index = ROOT / "docs/paper-index.md"
    if not index.exists() or index.read_text(encoding="utf-8") != render(papers):
        errors.append("Paper index is stale; run scripts/build_paper_index.py")
    for name in ["README.md", "README_cn.md"]:
        text = (ROOT / name).read_text(encoding="utf-8")
        if re.findall(r"Papers-(\d+)-blue\.svg", text) != [str(len(papers))]:
            errors.append(f"Incorrect paper count: {name}")

    markdown = [p for p in files if p.suffix == ".md"]
    contents = {p: p.read_text(encoding="utf-8") for p in markdown}
    anchor_map = {p.resolve(): anchors(text) for p, text in contents.items()}
    checked_links = 0
    for path, content in contents.items():
        text = re.sub(r"```.*?```", "", content, flags=re.S)
        targets = re.findall(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)", text)
        targets += re.findall(r'(?:href|src)="([^"]+)"', text)
        for target in targets:
            target = target.strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("//"):
                continue
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path.resolve()
            checked_links += 1
            if not dest.exists():
                errors.append(f"Broken path in {path.relative_to(ROOT)}: {target}")
            elif parsed.fragment and dest.suffix == ".md" and unquote(parsed.fragment) not in anchor_map.get(dest, set()):
                errors.append(f"Broken anchor in {path.relative_to(ROOT)}: {target}")
        if "/Users/" in text or "file://" in text:
            errors.append(f"Machine-local path leaked into {path.relative_to(ROOT)}")
        if re.search(r"\bS0[123]:\d+|materials/(?:slides|slide-index)", text):
            errors.append(f"Internal source mapping in {path.relative_to(ROOT)}")
    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    if errors:
        return 1
    print(f"OK: {len(papers)} unique papers; {len(markdown)} Markdown files; "
          f"{checked_links} local links; no original research files or internal source mappings.")
    print("External URLs and scientific claims require separate source review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(validate())
