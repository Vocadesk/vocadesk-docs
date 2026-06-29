---
title: Embedding on your website
summary: Developer reference for installing the web-call button — script tag, events, error codes, theming, and programmatic mounting.
tags:
  - embeds
  - web-calls
  - integrations
  - developers
keywords:
  - embed sdk
  - script tag
  - install embed
  - vocadesk events
  - error codes
  - theming
  - mount
  - data-vocadesk-embed
help_key: embeds.developer
---

# Embedding on your website

A developer reference for putting a Vocadesk [web-call button](embeds.md) on a site.
Create the [embed](embeds.md#creating-an-embed) in the dashboard first to get its id
(`emb_…`) and add your site to its allowed origins.

## Install

Add the script once, then place a button anywhere. Pin a specific version and use the
integrity hash shown when you create the embed:

```html
<script
  src="https://cdn.vocadesk.com/embed/vX.Y.Z/vocadesk.min.js"
  integrity="sha384-…"
  crossorigin="anonymous"
  defer
></script>

<button data-vocadesk-embed="emb_abc123">Talk to us</button>
```

The script auto-binds any element with `data-vocadesk-embed` and handles microphone
permission, the call UI, and connecting to the agent. It works regardless of where in
the page it loads.

!!! note "Pin a version"
    Always reference a specific `vX.Y.Z` and its `integrity` hash. There is no
    auto-updating "latest" URL — pinning is what keeps the integrity check valid.

## Mount programmatically

If you'd rather control placement in code:

```js
const handle = window.Vocadesk.mount("#support-button", {
  embedId: "emb_abc123",
  label: "Talk to us",
});
// later:
handle.destroy();
```

## Events

The host element emits `CustomEvent`s you can listen for:

| Event | When | `detail` |
|---|---|---|
| `vocadesk:start` | A call begins | — |
| `vocadesk:end` | A call ends | `{ durationMs }` |
| `vocadesk:error` | Something went wrong | `{ code, message }` |

```js
const el = document.querySelector('[data-vocadesk-embed]');
el.addEventListener('vocadesk:end', (e) => console.log('call length', e.detail.durationMs));
el.addEventListener('vocadesk:error', (e) => console.warn(e.detail.code, e.detail.message));
```

## Error codes

| `code` | Meaning |
|---|---|
| `mic_denied` | The visitor denied microphone access. |
| `mic_unavailable` | No microphone is available. |
| `token_failed` | The call couldn't be authorized (often an origin not on the allowlist). |
| `ws_failed` | The realtime connection couldn't be established. |
| `concurrent_call_active` | This visitor already has a call open for this embed. |
| `network` | A network problem interrupted the call. |
| `unknown` | An unexpected error. |

## Theming

Style the button with CSS custom properties on the host element; size comes from the
element's own CSS:

```css
[data-vocadesk-embed] {
  --vocadesk-bg: #1e1b4b;
  --vocadesk-fg: #ffffff;
  --vocadesk-accent: #7c3aed;
  --vocadesk-danger: #ef4444;
  --vocadesk-muted: #a1a1aa;
}
```

## Good to know

- **Origins are enforced.** Only domains on the embed's
  [allowed origins](embeds.md#creating-an-embed) can start a call.
- **One call per visitor per embed** at a time — see `concurrent_call_active`.
- **Microphone required.** The page must be served over HTTPS and the visitor must
  grant mic access.
- **No third-party calls.** The embed only talks to Vocadesk's own endpoints — no
  analytics or external trackers — which keeps it safe to add to any site.

## Related

- Operator-facing overview → [Web calls & embeds](embeds.md)
- How a call flows end to end → [How Vocadesk works](architecture.md)
