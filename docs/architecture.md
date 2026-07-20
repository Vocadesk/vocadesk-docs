---
title: How callcat.ai (former vocadesk) works
summary: A developer-level overview of the platform's services and how a call flows through them.
tags:
  - architecture
  - developers
  - calls
  - integrations
keywords:
  - architecture
  - system overview
  - services
  - call flow
  - voice pipeline
  - how it works
help_key: architecture.overview
---

# How callcat.ai (former vocadesk) works

A high-level look at the moving parts, for developers and the technically curious.
This describes the *shape* of the system — not its internal configuration.

## Services

callcat.ai (former vocadesk) is a set of focused services rather than one monolith:

| Service | Role |
|---|---|
| **Dashboard** | The web app you use to manage clients, agents, embeds, and review calls. |
| **Management API** | The backend that owns all data and serves the dashboard. |
| **Voice runtime** | The real-time voice pipeline that bridges callers and the AI provider, and produces transcripts and recordings. |
| **Embed gateway & SDK** | Mints short-lived tokens for web calls and provides the drop-in browser button. |
| **Billing** | Subscriptions, plans, usage metering, and invoices. |

The dashboard talks only to the Management API; the voice runtime publishes what
happens on a call as a stream of events that the API persists.

## How a call flows

```
Caller (phone, web, or test)
   │
   ▼
Voice runtime  ──►  AI provider (speech + language)
   │  publishes events: started, transcript, ended, transferred, analyzed
   ▼
Management API  ──►  stores the call, transcript, recording, summary
   │
   ▼
Dashboard  ──►  you review it
```

1. A call arrives — from a phone number, a web [embed](embeds.md) button, or a
   browser [test call](agents/index.md#creating-an-agent).
2. The voice runtime looks up the [agent](agents/index.md), builds its instructions
   from the persona, knowledge, questions, and
   [conversation design](agents/conversation-design.md), and starts talking.
3. As the conversation happens, it streams **events** — the call started, each
   transcript turn, a transfer, the call ended, and a post-call analysis.
4. The Management API records those into the call's history.
5. You see the result in [Calls](calls.md).

## Channels

The same agent and the same pipeline serve three channels:

- **Phone** — calls over the telephone network to an assigned
  [phone number](phone-numbers.md).
- **Web** — browser calls from an [embed](embeds.md), authorized by a short-lived
  token from the embed gateway.
- **Test** — browser calls from the dashboard, for building and tuning agents.

## Integrating

The most common integration point is the **web embed** — a single script tag and a
button put a live agent on any website. See [Web calls & embeds](embeds.md).

!!! note "This is the public overview"
    Operational details — deployment, secrets, and internal runbooks — live in
    callcat.ai (former vocadesk)'s private engineering docs, not here.
