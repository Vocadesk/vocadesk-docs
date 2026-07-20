# callcat.ai (former vocadesk) Documentation

Public docs for the callcat.ai (former vocadesk) platform, built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
and deployed to GitHub Pages on every push to `main`.

**Live:** https://vocadesk.github.io/vocadesk-docs/

## Run locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve        # live preview at http://127.0.0.1:8000
.venv/bin/mkdocs build        # one-off build into ./site
```

## How it's structured

```
docs/                 Markdown content (one folder per top-level area)
hooks/docs_hooks.py   build-time automation (see below)
mkdocs.yml            site config, theme, nav, search, tags
.github/workflows/    build + deploy to GitHub Pages
```

## Authoring rules (read before adding a page)

Every page starts with YAML frontmatter. These fields drive the automation, so fill
them in:

```yaml
---
title: Call forwarding & transfers          # shown in nav, search, related links
summary: One sentence describing the page.   # used in related links, llms.txt, help-map
tags:                                        # topic tags — drive auto cross-linking
  - agents
  - forwarding
keywords: [transfer, hand off]               # extra search/RAG hints (optional)
help_key: agents.call_forwarding             # optional — see "Help buttons" below
---
```

- **`tags` power the cross-linking.** Pages that share tags are linked automatically
  under a **Related** section at the bottom — there are no hand-maintained "see also"
  lists. Reuse existing tags so pages connect; only invent a tag when a genuinely new
  topic appears.
- **`summary`** is reused in three places — keep it to one clear sentence.
- Link between pages with normal Markdown links to the `.md` file
  (`[text](../concepts.md#client)`); MkDocs rewrites them to final URLs.

## Help buttons (in-product deep links)

Give a page (or a granular sub-page) a `help_key`. The build emits
`help-map.json` at the site root:

```
https://vocadesk.github.io/vocadesk-docs/help-map.json
```

mapping `help_key -> { url, title, summary }`. The dashboard's `<HelpButton>`
component resolves a key (e.g. `agents.call_forwarding`) to the exact doc URL, so UI
code never hardcodes documentation paths. Add a `help_key`, redeploy, and the button
works.

## Machine index for a future help-chat agent

The build also emits `llms.txt` at the site root — a flat, link-rich list of every
page with its summary and tags. A future RAG / help-chat agent can use it as a table
of contents, then fetch individual pages as its knowledge base. Because content is
plain Markdown with structured frontmatter, it chunks and embeds cleanly.

## Keeping docs in sync with the product

Docs live as code so they can be updated alongside features:

1. When a feature changes, update the matching page(s) in the same change set.
2. `summary` + `tags` keep search, related links, and the help-map current
   automatically — you only edit prose.
3. (Planned) a CI agent proposes doc-update PRs when product repos change documented
   areas, plus a periodic drift audit.
