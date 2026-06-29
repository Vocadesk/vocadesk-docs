---
title: Web calls & embeds
summary: Let website visitors talk to an agent from a button — create an embed, set its origins, and install the snippet.
tags:
  - embeds
  - web-calls
  - agents
  - integrations
keywords:
  - embed
  - web call
  - talk to us button
  - website widget
  - allowed origins
  - snippet
help_key: embeds.overview
---

# Web calls & embeds

An **embed** turns a button on your website into a live voice call with an
[agent](agents/index.md) — no phone number required. Visitors click, grant microphone
access, and talk to the agent right in the browser.

## Creating an embed

From a client's **Embeds** tab (or the Embeds area), create an embed and set:

- **Agent** — which agent answers these web calls.
- **Allowed origins** — the website domains permitted to start calls with this embed
  (an allowlist). Requests from anywhere else are rejected.
- **Bot protection** — optionally require a challenge before a call starts, to deter
  abuse.

Each embed has an id like `emb_abc123`.

## Installing it on a site

Add the embed snippet to the website and place a button that references the embed id.
Conceptually:

```html
<!-- Load the Vocadesk embed script (pin a specific version) -->
<script src="https://cdn.vocadesk.com/embed/vX.Y.Z/vocadesk.min.js" defer></script>

<!-- Anywhere you want the call button -->
<button data-vocadesk-embed="emb_abc123">Talk to us</button>
```

The button handles microphone permission, the call UI, and connecting to the agent.
You can also mount it programmatically and style it with CSS variables.

!!! note "Origins are enforced server-side"
    Listing your domains under **allowed origins** isn't just a suggestion — calls
    from other origins are refused. Add every domain (and subdomain) that should be
    able to start a call.

## Web calls in your reports

Web calls appear in [Calls](calls.md) like any other, with `callType: web`, full
transcripts, recordings, and post-call analysis. Forwarding and conditional
instructions work the same as on phone calls — see
[Conversation design](agents/conversation-design.md).

## Limits

One live call per visitor per embed is allowed at a time, and embeds can have their
own concurrency settings. If a visitor already has a call open, starting another is
blocked until the first ends.
