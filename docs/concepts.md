---
title: Core concepts
summary: The objects Vocadesk is built around — operators, clients, agents, calls, phone numbers, and embeds.
tags:
  - getting-started
  - concepts
keywords:
  - operator
  - client
  - agent
  - call
  - embed
  - phone number
  - data model
help_key: concepts.overview
---

# Core concepts

Everything in Vocadesk hangs off a small set of objects. Learn these once and the
rest of the product makes sense.

## The hierarchy

```
Operator (your business)
└── Client (an end-customer you serve)
    └── Agent (an AI persona for that client)
        ├── Phone number (a Twilio number routed to the agent)
        ├── Embed (a web-call button on a website)
        └── Call (one phone or web conversation)
```

## Objects

### Operator
A **business account / workspace**. It owns your clients, agents, calls, and
billing. The people who log in are **users** that belong to the operator. Roles are
`user`, `admin`, and `super_admin`.

### Client
An **end-customer of yours** — the business whose calls an agent answers. One
operator has many clients. A client carries its own subscription plan, branding, and
contact details. Clients are deactivated (not hard-deleted) when you stop serving
them.

### Agent
A configured **AI persona** that belongs to a client. An agent has:

- a **persona** and **voice** (see [Configuring an agent](agents/configuration.md)),
- a **knowledge base** and a list of **intake questions**,
- a **[conversation design](agents/conversation-design.md)** mode, and
- **[call-forwarding](agents/call-forwarding.md)** rules for handing off to a human.

### Call
One voice conversation. A call has a type:

| `callType` | Origin |
|---|---|
| `phone` | A real inbound PSTN call to a Twilio number. |
| `web` | A web call from an embedded button on a website. |
| `test` | A browser test call placed from the dashboard. |

Every call captures a transcript, a recording, duration, cost, and an optional
post-call analysis (summary, sentiment, extracted data).

### Phone number
A telephone number bound to an agent so inbound PSTN calls reach it. How many
numbers you can attach depends on the client's plan.

### Embed
A **web-call configuration** — the "Talk to us" button you drop onto a website. An
embed routes web callers to a specific agent. Each embed has an allowlist of origins
and its own concurrency limits.

## Where to go next

- Configure your first agent → [Agents](agents/index.md)
- Look up a term → [Glossary](glossary.md)
