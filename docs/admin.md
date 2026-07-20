---
title: Administration & roles
summary: What admins and super-admins can do — roles, operator approval, plan pricing, impersonation, and restricted features.
tags:
  - administration
  - settings
  - team
  - billing
keywords:
  - roles
  - admin
  - super admin
  - permissions
  - operator approval
  - plan pricing
  - impersonation
  - restricted features
help_key: admin.overview
---

# Administration & roles

callcat.ai (former vocadesk) has three roles. Most people are `user`s; `admin` and `super_admin` unlock
progressively more.

## Roles

| Role | Can do |
|---|---|
| `user` | Day-to-day work — manage [clients](clients.md), [agents](agents/index.md), and review [calls](calls.md). |
| `admin` | Everything a user can, plus operator-level administration of your workspace. |
| `super_admin` | Platform-wide administration across operators (see below). |

Assign roles when you [invite teammates](settings.md#team-roles).

## Super-admin capabilities

Super-admins administer the platform itself, not just one workspace:

- **Approve new operators.** When a business signs up, a super-admin reviews and
  activates the operator — and sets its billing **currency** at that point (see
  [Billing → Multi-currency](billing.md)).
- **Tune plan pricing.** Super-admins maintain a per-operator **plan catalog** —
  adding, renaming, reordering, and retuning the plans (base fee, included minutes,
  per-minute, overage, and forwarding rates) an operator's clients can be put on. This
  is the editable layer on top of the default plan templates.
- **Impersonate an operator.** To support or troubleshoot, a super-admin can view a
  specific operator's workspace as if inside it, scoped to that operator's data.

!!! note "Currency is set at approval"
    An operator's billing currency is chosen when it's approved, before any billing
    exists. Everything defaults to GBP. See [Billing](billing.md).

## Restricted features

A few capabilities are limited to super-admins:

- The **Decision tree** [conversation design](agents/conversation-design.md#decision-tree-advanced)
  mode.
- Certain restricted **personas / voices** (for example native Hebrew voices) in the
  [voice picker](agents/voices.md).

Regular users won't see these options; that's expected.

## Related

- Invite your team and set roles → [Settings](settings.md#team-roles)
- Pricing your clients are billed on → [Billing](billing.md)
