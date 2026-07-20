---
title: Billing
summary: How plans, per-minute pricing, usage, and invoices work for your clients.
tags:
  - billing
  - plans
  - usage
  - invoices
  - clients
keywords:
  - billing
  - plan
  - pricing
  - subscription
  - per minute
  - usage
  - invoice
  - overage
  - currency
help_key: billing.overview
---

# Billing

callcat.ai (former vocadesk) bills **per minute** against a **subscription plan** on each
[client](clients.md). This page is the operator-facing view of how charges are made
up.

## Plans

Each client is on a plan that defines:

- a **monthly base fee**,
- an amount of **included minutes**,
- a **per-minute rate** for usage,
- an **overage rate** for minutes beyond the included bundle,
- a **forwarding rate** for transferred minutes, and
- **limits** on agents and phone numbers.

Operators have a **plan catalog** they can tune per their own needs, and pricing is
**multi-currency** (the client's currency is set when the client is approved).

!!! note "Test clients aren't billed"
    Clients in `testing` status, and `test` calls, are excluded from charges. Move a
    client to `active` when you're ready to bill it.

## How a charge is built

For a full month a client's charge is:

```
base fee
+ included-minutes bundle
+ overage      (extra minutes × overage rate)
+ forwarding   (transferred minutes × forwarding rate)
```

Partial months and mid-cycle plan changes are prorated:

- **Upgrades** take effect immediately and are prorated.
- **Downgrades** take effect at the start of the next month.

## The Billing area

The **Billing** tab shows, per period:

- a **summary strip** — base, usage, overage, and forwarding totals,
- a **per-client breakdown** you can search and export, and
- **billing history** you can drill into month by month.

All amounts are shown in each client's currency.

## Usage & reconciliation

Completed calls are metered into the current billing cycle automatically. The figures
you see reflect real usage at the client's effective pricing, so you can track charges
without having to generate invoices first.

## What's next

- Set up and manage clients → [Clients](clients.md)
- Operator-wide options → [Settings](settings.md)
