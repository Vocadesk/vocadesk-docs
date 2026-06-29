#!/usr/bin/env python3
"""Validate the docs' frontmatter conventions so the automation stays correct.

Run locally (`python scripts/check_docs.py`) or in CI before the build. Enforces:

  * every content page has `title`, `summary`, and at least one `tag`
    (these drive search, related links, help-map, and llms.txt);
  * `help_key` values are unique (each in-product Help button maps to one page);

and warns (non-fatally) about pages that share no tag with any other page, since
those get no auto-generated "Related" links.

Exit code 1 on any error, 0 otherwise. Pure stdlib + PyYAML (ships with MkDocs).
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
SKIP = {"tags.md"}  # plugin-rendered, no prose frontmatter required
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as exc:  # malformed frontmatter is an error
        raise ValueError(f"invalid YAML frontmatter: {exc}") from exc


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    help_keys: dict[str, list[str]] = defaultdict(list)
    tag_index: dict[str, list[str]] = defaultdict(list)
    page_tags: dict[str, list[str]] = {}

    md_files = sorted(p for p in DOCS_DIR.rglob("*.md"))
    for path in md_files:
        rel = path.relative_to(DOCS_DIR).as_posix()
        if rel in SKIP:
            continue
        try:
            fm = parse_frontmatter(path)
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue

        if not isinstance(fm.get("title"), str) or not fm["title"].strip():
            errors.append(f"{rel}: missing `title`")
        if not isinstance(fm.get("summary"), str) or not fm["summary"].strip():
            errors.append(f"{rel}: missing `summary` (used in related links / help-map / llms.txt)")

        tags = fm.get("tags") or []
        if isinstance(tags, str):
            tags = [tags]
        if not tags:
            errors.append(f"{rel}: needs at least one `tag` (drives auto cross-linking)")
        page_tags[rel] = [str(t) for t in tags]
        for t in page_tags[rel]:
            tag_index[t].append(rel)

        hk = fm.get("help_key")
        if hk:
            help_keys[str(hk)].append(rel)

    for key, pages in sorted(help_keys.items()):
        if len(pages) > 1:
            errors.append(f"duplicate help_key '{key}' on: {', '.join(pages)}")

    for rel, tags in sorted(page_tags.items()):
        if tags and not any(len(tag_index[t]) > 1 for t in tags):
            warnings.append(f"{rel}: no tag shared with another page → no Related links")

    print(f"Checked {len(page_tags)} content pages, {len(help_keys)} help keys.")
    for w in warnings:
        print(f"  warning: {w}")
    for e in errors:
        print(f"  ERROR:   {e}")

    if errors:
        print(f"\n{len(errors)} error(s). Fix frontmatter and re-run.")
        return 1
    print("All docs frontmatter checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
