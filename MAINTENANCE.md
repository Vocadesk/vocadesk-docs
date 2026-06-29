# Keeping the docs in sync with the product

The goal: documentation evolves with Vocadesk as automatically as possible, while a
human still approves every change.

## The loop

1. **Authoring conventions do most of the work.** Each page's `summary` + `tags` +
   `help_key` frontmatter keep search, the auto "Related" links, the in-product
   help-map, and the `llms.txt` RAG index correct without manual upkeep. See
   [README → Authoring rules](README.md#authoring-rules-read-before-adding-a-page).

2. **Every change is validated.** `scripts/check_docs.py` runs in CI before each
   deploy and fails the build if frontmatter, tags, summaries, or `help_key`
   uniqueness regress. Run it locally with `python scripts/check_docs.py`.

3. **AI maintenance opens PRs.** `.github/workflows/docs-maintenance.yml` runs Claude
   Code against this repo (weekly, on demand, or when a product repo signals a change),
   updates the docs, and opens a Pull Request for review. It needs an `ANTHROPIC_API_KEY`
   secret; without it the workflow is a clean no-op.

## Documentation area ↔ product repository map

When a product repo changes a documented area, update the matching page(s):

| Area / pages | Driven by (product repo) |
|---|---|
| `agents/*`, `phone-numbers.md` | vocafront2 (agent UI), vocaback2 (agent API), voice-runtime2 (call behavior) |
| `agents/conversation-design.md`, `agents/call-forwarding.md` | vocafront2 + voice-runtime2 (scenario / decision-tree / forwarding) |
| `embeds.md` | embed-gateway, embed-sdk, vocafront2 (embeds UI) |
| `calls.md` | voice-runtime2 (events), vocaback2 (persistence), vocafront2 (call UI) |
| `billing.md` | vocabill, vocagateway, vocafront2 (billing UI) |
| `clients.md`, `settings.md` | vocaback2, vocafront2 |
| `architecture.md` | any structural change across services |

## Triggering an update from a product repo

Add a step to a product repo's pipeline (e.g. on merge to its main) that signals the
docs repo, with a short note of what changed:

```yaml
- name: Ask docs to update
  run: |
    gh api repos/Vocadesk/vocadesk-docs/dispatches \
      -f event_type=docs-update \
      -f 'client_payload[context]=Agent forwarding behavior changed: triggers now forward immediately. Update agents/call-forwarding.md.'
  env:
    GH_TOKEN: ${{ secrets.DOCS_DISPATCH_TOKEN }}   # a token that can dispatch to vocadesk-docs
```

The maintenance workflow picks up the `context`, makes the edit, and opens a PR.

## Adding a new in-product Help button

1. Add (or pick) a page and give it a `help_key`, e.g. `calls.overview`.
2. Deploy the docs — the build regenerates `help-map.json`.
3. In the app, drop `<HelpButton helpKey="calls.overview" />` (optionally with an
   `anchor` for a specific section). No doc path is hardcoded.
