---
title: Testing your agent
summary: Talk to an agent from your browser before going live — what test calls do, the modes available, and what to check.
tags:
  - agents
  - testing
  - calls
  - getting-started
keywords:
  - test call
  - test agent
  - try agent
  - browser call
  - go live
  - preview agent
help_key: agents.testing
---

# Testing your agent

Before attaching a phone number or publishing a web button, **talk to your agent from
the browser**. Test calls let you hear exactly how it sounds and behaves, and iterate
fast — at no cost.

## Placing a test call

Open the agent and use **Test call**. Your browser asks for microphone access, then
you're connected straight to the agent. Talk to it as a caller would.

- Test calls are **not billed** to the client and are recorded with `callType: test`.
- They appear in [Calls](../calls.md) like any other call, with a transcript and
  recording, so you can review what happened afterwards.

!!! tip "Use a testing client"
    Keep a [client](../clients.md) in `testing` status for experiments — its calls are
    never billed, so you can iterate freely.

## Test-call modes

The dashboard can place a test call a few different ways. They all talk to the same
agent; pick whichever connects cleanly for you:

| Mode | What it is |
|---|---|
| **Native** | A direct in-browser call to the voice runtime — the default, lowest-overhead path. |
| **Phone (Twilio)** | Routes the browser call through the telephone stack, closer to a real inbound call. |
| **Comparison** | A vendor agent mode, for comparing behavior side by side. |

## What to check before going live

- **Greeting** — does it name your business and the agent, and invite the caller in?
- **Knowledge** — ask the factual questions a caller would; confirm the agent answers
  from its [knowledge base](configuration.md#knowledge-base) before pushing on with
  intake.
- **Intake** — give partial information up front and confirm the agent skips questions
  you've already answered and asks for what's missing.
- **[Forwarding](call-forwarding.md)** — trigger each forwarding condition out loud and
  confirm the agent connects (on a test call the transfer is *signalled* — no real
  number is dialled, so you're verifying the decision, not the dialing).
- **Voice & language** — the right [voice and language](voices.md) for your audience.

## Going live

When it sounds right:

- For phone: attach a [phone number](../phone-numbers.md).
- For web: publish an [embed](../embeds.md) button.

Then review real conversations in [Calls](../calls.md) and keep tuning.
