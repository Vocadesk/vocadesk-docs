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

## Free weeks

Each operator has a small number of **free-week packages** (5 by default; a
super-admin can change this per operator). From a client's **Info** tab you can give
an `active` client **one** free week:

- it starts the moment you give it and ends **exactly 7 days later**, used or not;
- calls placed in that window are **not charged**, until the waived usage reaches the
  cap (10 in your billing currency by default, e.g. £10 / $10; a super-admin can set a
  different cap for your operator). The call that crosses the cap is split, and later
  calls bill normally;
- a client can only ever receive **one** free week, and it can't be taken back;
- only a super-admin can **extend** a free week (by 7 days at a time, from its current end,
  or from now if it has already ended) or **void** it early. A week whose cap is already
  reached can't be extended.

Waived minutes never count against the plan's included bundle or overage. They show
on the Billing tab and as an informational line on the invoice. Because calls are
metered once a day, the "waived so far" figure lags by up to a day.

## Usage & reconciliation

Completed calls are metered into the current billing cycle automatically. The figures
you see reflect real usage at the client's effective pricing, so you can track charges
without having to generate invoices first.

## What's next

- Set up and manage clients → [Clients](clients.md)
- Operator-wide options → [Settings](settings.md)
