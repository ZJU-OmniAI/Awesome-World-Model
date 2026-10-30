#!/usr/bin/env python3
"""Render the bibliography from data/papers.json; --check never writes."""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GROUPS = [
    ("foundations", "基础研究"),
    ("surveys", "综述"),
    ("wam-visual-planning", "视觉规划与动作解码"),
    ("wam-geometry-motion", "几何与运动接口"),
    ("wam-representation", "预测表征与动作决策"),
    ("wam-joint", "世界与动作联合建模"),
    ("wam-feedback", "价值、评价与决策反馈"),
    ("wam-tactile", "触觉与接触建模"),
    ("wam-efficiency", "高效世界动作建模"),
    ("problem-memory", "状态、记忆与多阶段规划"),
    ("problem-physics", "动作与物理正确性"),
    ("benchmarks", "评测基准"),
]


def load_papers():
    return json.loads((ROOT / "data/papers.json").read_text(encoding="utf-8"))


def cell(value):
    return str(value).replace("|", "&#124;").replace("\n", " ")


def render(papers):
    lines = [
        "# 论文索引",
        "",
        "[世界模型](../README_cn.md) · [World Action Models](02-world-action-models.md) · "
        "[问题分类](03-problem-taxonomy.md)",
        "",
    ]
    lines.extend(f"- [{label}](#{key})" for key, label in GROUPS)
    lines.append("")
    for key, label in GROUPS:
        rows = sorted(
            [p for p in papers if p["collection"] == key],
            key=lambda p: (p["first_submitted"] or "9999-99-99", p["id"]),
        )
        lines += [f'<a id="{key}"></a>', f"## {label}", "",
                  "| 日期 | 论文 | 简介 |",
                  "|---|---|---|"]
        for p in rows:
            title = cell(p["title"])
            description = (f'<a id="paper-{p["id"]}"></a>**{cell(p["name"])}** · '
                           f'[{title}]({p["paper"]})')
            lines.append(f"| {p['first_submitted'] or '—'} | {description} | {cell(p['summary_zh'])} |")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    papers = load_papers()
    unknown = {p["collection"] for p in papers} - {key for key, _ in GROUPS}
    if unknown:
        raise SystemExit(f"Unknown collections: {sorted(unknown)}")
    target = ROOT / "docs/paper-index.md"
    expected = render(papers)
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != expected:
            raise SystemExit("Paper index is stale. Run python3 scripts/build_paper_index.py")
        print(f"Paper index is current: {len(papers)} entries.")
    else:
        target.write_text(expected, encoding="utf-8")
        print(f"Generated {target.relative_to(ROOT)}: {len(papers)} entries.")


if __name__ == "__main__":
    main()
