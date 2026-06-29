---
title: Calls
summary: Review every conversation — transcripts, recordings, summaries, sentiment, and the data the agent captured.
tags:
  - calls
  - transcripts
  - recordings
  - analysis
keywords:
  - call
  - transcript
  - recording
  - call summary
  - sentiment
  - extracted data
  - call review
help_key: calls.overview
---

# Calls

Every conversation an agent has — by phone, web, or test — is recorded as a **call**.
The **Calls** area is where you review what happened.

## Call types

| Type | Where it came from |
|---|---|
| **Phone** | A real inbound call to a [phone number](phone-numbers.md). |
| **Web** | A visitor using an [embed](embeds.md) button on a website. |
| **Test** | A browser [test call](agents/index.md#creating-an-agent) from the dashboard (not billed). |

## The calls list

The list shows recent calls with the agent, caller, time, duration, and outcome.
Filter by client, agent, date range, or type to find what you need. Open any call
for its full detail.

## A call's detail

Each call captures:

- **Transcript** — the full back-and-forth, turn by turn, with timestamps. On a live
  call the transcript streams in as it happens.
- **Recording** — audio of the conversation you can play back.
- **Duration & cost** — how long it ran and what it cost against the client's plan.
- **Outcome** — whether it completed normally, was transferred to a human, or ended
  early.

## Post-call analysis

Shortly after a call ends, Vocadesk adds an automatic analysis:

- **Summary** — a short, readable recap of the conversation.
- **Sentiment** — overall caller sentiment (positive, neutral, or negative).
- **Extracted data** — the structured answers to your
  [intake questions](agents/configuration.md#intake-questions), pulled from what the
  caller said, plus anything captured by
  [conditional instructions](agents/conversation-design.md#questions-conditions-scenario).

!!! tip "Summaries by email"
    Operators can have a summary emailed after each completed call — see
    [Settings](settings.md#call-summary-emails).

## Following up

Use the summary and extracted data to follow up with callers — the agent's job is
to capture the right information and route or escalate it, so a human can act on it
quickly. For escalations during the call, see
[Call forwarding & transfers](agents/call-forwarding.md).
