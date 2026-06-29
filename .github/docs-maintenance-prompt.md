# Docs maintenance task

You are maintaining the **Vocadesk public documentation** in this repository. Your job
is to keep it accurate, current, and well-connected as the product evolves — then stop
and let a human review your PR.

## What to do

1. Read `MAINTENANCE.md` for the map of documentation areas ↔ product repositories and
   the conventions.
2. Using the "Context for this run" appended below (what changed), update the affected
   pages under `docs/`. If the context is a routine audit, look for: stale wording,
   missing pages for features that exist, thin pages that deserve more detail, and
   broken or missing cross-links.
3. Follow the authoring rules in `README.md` exactly:
   - Every page has frontmatter `title`, `summary`, and at least one `tag`. Reuse
     existing tags so the auto cross-linking connects pages; only invent a tag for a
     genuinely new topic.
   - Give user-facing pages a `help_key` when the app should be able to deep-link to
     them. Keep `help_key` values unique.
   - Link between pages with Markdown links to the `.md` file.
4. **Stay public-safe.** This site is public. Never add secrets, credentials, internal
   URLs, exact infrastructure/deployment details, or anything that aids an attacker.
   Document product *behavior*, not internal implementation.
5. Run `python scripts/check_docs.py` and `mkdocs build` and fix anything they flag.

## What NOT to do

- Do not push to `main` — your changes go into a PR.
- Do not delete pages or remove `help_key`s without a clear reason (the app may link to
  them).
- Do not document unreleased or speculative features.

Make focused, reviewable changes. If nothing needs updating, make no changes.
