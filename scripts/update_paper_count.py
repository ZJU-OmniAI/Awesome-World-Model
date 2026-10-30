#!/usr/bin/env python3
"""Update both README badges from the unique structured bibliography."""

import argparse
import re

from build_paper_index import ROOT, load_papers


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify without writing")
    args = parser.parse_args()
    papers = load_papers()
    ids = [p["id"] for p in papers]
    if len(ids) != len(set(ids)):
        raise SystemExit("Duplicate paper IDs; fix data/papers.json before counting.")
    count = len(ids)
    for name in ["README.md", "README_cn.md"]:
        path = ROOT / name
        text = path.read_text(encoding="utf-8")
        updated, matched = re.subn(r"(Papers-)\d+(-blue\.svg)", rf"\g<1>{count}\g<2>", text)
        if matched != 1:
            raise SystemExit(f"Expected one Papers badge in {name}, found {matched}.")
        if args.check and updated != text:
            raise SystemExit(f"Stale paper count in {name}.")
        if not args.check and updated != text:
            path.write_text(updated, encoding="utf-8")
        print(f"{name}: {count} papers.")


if __name__ == "__main__":
    main()
