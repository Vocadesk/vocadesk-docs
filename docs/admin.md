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
help_keys:
  - admin.hebrew_enabled
  - admin.order_taking_enabled
  - admin.decision_tree_enabled
---

# Administration & roles

callcat.ai has three roles. Most people are `user`s; `admin` and `super_admin` unlock
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
- **Free-week packages.** From the operator row's menu, set how many
  [free weeks](billing.md#free-weeks) an operator may give its clients (default 5) and
  the cap per week (platform default 10 in the operator's currency), see the weeks
  already given, and void one early.

!!! note "Currency is set at approval"
    An operator's billing currency is chosen when it's approved, before any billing
    exists. Everything defaults to GBP. See [Billing](billing.md).

## Operator feature switches {#operator-switches}

Three features are off for every new operator. A super-admin turns each one on per
operator, in the **Super Admin dashboard** (one switch per operator in the table).
Regular users and admins cannot change them. Turning a switch off later hides the
feature again but does not delete anything already built.

### Hebrew {#hebrew-enabled}

Lets the operator pick **Hebrew agent personas** and use the dashboard in Hebrew.
Hebrew agents that already exist keep working whether the switch is on or off. The
same switch is on the operator's own Settings page, visible to super-admins only.

### Order taking {#order-taking-enabled}

Shows the **Catalog / product info** and **Order taking** cards in the agent page for
that operator. See [Catalog & order taking](agents/catalog-and-orders.md). Without
this switch an operator cannot add a menu or let an agent take orders.

### Decision tree {#decision-tree-enabled}

Adds the **Decision tree** mode to the
[conversation design](agents/conversation-design.md#decision-tree-advanced) switcher
for every agent of that operator. Use it for fully scripted calls.

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
