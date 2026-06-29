---
title: Clients
summary: Create and manage the end-customers whose calls your agents handle.
tags:
  - clients
  - getting-started
  - billing
keywords:
  - client
  - end customer
  - client status
  - deactivate client
  - branding
help_key: clients.overview
---

# Clients

A **client** is an end-customer of your [operator](concepts.md#operator) — the
business whose calls your agents answer. Each client has its own agents, phone
numbers, calls, branding, and subscription.

## Creating a client

From **Clients → New client**, set:

- **Name** and **industry** — the industry can seed sensible defaults for new agents.
- **Contact details** — name, email, phone.
- **Branding** — a logo and colour used where the client is shown.

Once created, open the client to find tabs for **Calls**, **Agents**, **Phone
numbers**, **Embeds**, and **Info**.

## Client status

A client moves through a small set of states:

| Status | Meaning |
|---|---|
| `testing` | Set up but not yet billed — ideal while you build and test agents. |
| `active` | Live and billed against its [plan](billing.md). |
| `pending_deactivation` | Scheduled to deactivate (e.g. at the end of the billing period). |
| `inactive` | No longer served; data is retained but agents don't take calls. |

!!! note "Clients are deactivated, not deleted"
    There's no hard delete. Stopping service sets the client to inactive and
    preserves its history. A client with agents still attached can't be deactivated
    until those are handled.

## Plans & limits

Each client carries a subscription [plan](billing.md) that sets how many
[agents](agents/index.md) and [phone numbers](phone-numbers.md) it can have, plus its
per-minute pricing. When a client hits a limit, the relevant **New** action is
disabled with a notice — upgrade the client's plan to raise it.

## What's next

- Add an agent for the client → [Agents](agents/index.md)
- Understand pricing and usage → [Billing](billing.md)
