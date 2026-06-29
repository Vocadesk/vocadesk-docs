"""Build-time hooks for the Vocadesk docs.

Two jobs, both driven off page frontmatter so they stay correct as content grows:

1. Auto cross-linking — every page gets a "Related" block linking the other pages
   that share the most ``tags``. No hand-maintained "see also" lists.

2. Machine indexes for integrations:
   - ``help-map.json`` — ``help_key`` -> {url, title, summary}. The app's in-product
     Help buttons resolve a stable key to the exact doc URL (decouples UI from paths).
   - ``llms.txt`` — a flat, link-rich index of every page for a future help-chat /
     RAG agent to use as a table of contents.

Pure stdlib + PyYAML (ships with MkDocs). No external services.
"""

from __future__ import annotations

import json
import os
import re
from collections import defaultdict

import yaml

# Populated in on_files(), read in later hooks. MkDocs runs hooks in one process.
_PAGE_META: dict[str, dict] = {}            # src_uri -> {title, summary, tags, keywords, help_key}
_TAG_INDEX: dict[str, list[str]] = defaultdict(list)  # tag -> [src_uri]
_HELP_MAP: dict[str, dict] = {}             # help_key -> {url, title, summary}

_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_MAX_RELATED = 5
_SKIP_RELATED = {"tags.md", "index.md"}     # index/landing pages curate their own links


def _parse_frontmatter(text: str) -> dict:
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def _as_list(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    return [str(v) for v in value]


def on_files(files, config):
    """Index every page's frontmatter before any page is rendered."""
    _PAGE_META.clear()
    _TAG_INDEX.clear()
    for f in files:
        if not f.src_uri.endswith(".md") or not f.abs_src_path:
            continue
        try:
            with open(f.abs_src_path, encoding="utf-8") as fh:
                fm = _parse_frontmatter(fh.read())
        except OSError:
            fm = {}
        tags = _as_list(fm.get("tags"))
        meta = {
            "title": fm.get("title"),
            "summary": fm.get("summary"),
            "tags": tags,
            "keywords": _as_list(fm.get("keywords")),
            "help_key": fm.get("help_key"),
        }
        _PAGE_META[f.src_uri] = meta
        for tag in tags:
            _TAG_INDEX[tag].append(f.src_uri)
    return files


def _relative_md_link(from_src: str, to_src: str) -> str:
    from_dir = os.path.dirname(from_src)
    rel = os.path.relpath(to_src, from_dir or ".")
    return rel.replace(os.sep, "/")


def on_page_markdown(markdown, page, config, files):
    """Append a tag-driven 'Related' section to each content page."""
    src = page.file.src_uri
    if src in _SKIP_RELATED:
        return markdown
    meta = _PAGE_META.get(src)
    if not meta or not meta["tags"]:
        return markdown

    scores: dict[str, int] = defaultdict(int)
    for tag in meta["tags"]:
        for other in _TAG_INDEX.get(tag, []):
            if other != src:
                scores[other] += 1
    if not scores:
        return markdown

    ranked = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))[:_MAX_RELATED]
    lines = ["", "", "## Related", ""]
    for other_src, _ in ranked:
        other = _PAGE_META[other_src]
        title = other.get("title") or other_src
        link = _relative_md_link(src, other_src)
        summary = other.get("summary")
        suffix = f" — {summary}" if summary else ""
        lines.append(f"- [{title}]({link}){suffix}")
    return markdown + "\n".join(lines) + "\n"


def on_page_content(html, page, config, files):
    """Collect Help-button keys with their resolved (canonical) URLs."""
    meta = _PAGE_META.get(page.file.src_uri) or {}
    help_key = page.meta.get("help_key") or meta.get("help_key")
    if help_key:
        _HELP_MAP[str(help_key)] = {
            "url": page.canonical_url or page.abs_url or page.url,
            "title": page.title,
            "summary": page.meta.get("summary") or meta.get("summary") or "",
        }
    return html


def on_post_build(config):
    """Emit help-map.json and llms.txt alongside the built site."""
    site_dir = config["site_dir"]
    os.makedirs(site_dir, exist_ok=True)

    with open(os.path.join(site_dir, "help-map.json"), "w", encoding="utf-8") as fh:
        json.dump(_HELP_MAP, fh, indent=2, ensure_ascii=False, sort_keys=True)

    base = (config.get("site_url") or "").rstrip("/")
    out = ["# Vocadesk Documentation", "",
           "> Machine-readable page index for help-chat / RAG agents.", ""]
    for src, meta in sorted(_PAGE_META.items()):
        if src == "tags.md":
            continue
        title = meta.get("title") or src
        url = base + "/" + src.replace("index.md", "").replace(".md", "/")
        url = url.replace("//", "/").replace("https:/", "https://").replace("http:/", "http://")
        bits = [f"- [{title}]({url})"]
        if meta.get("summary"):
            bits.append(f": {meta['summary']}")
        if meta.get("tags"):
            bits.append(f" (tags: {', '.join(meta['tags'])})")
        out.append("".join(bits))
    with open(os.path.join(site_dir, "llms.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
