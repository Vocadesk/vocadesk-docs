---
title: Conversation design
summary: Choose how an agent runs a call — simple intake, Questions & conditions (scenario), or a Decision tree.
tags:
  - agents
  - conversation-design
  - scenario
  - decision-tree
  - questions
  - forwarding
keywords:
  - conversation design
  - mode
  - questions and forwarding
  - questions and conditions
  - scenario
  - conditional instructions
  - decision tree
  - triggers
help_key: agents.conversation_design
---

# Conversation design

**Conversation design** is *how* an agent runs the call. callcat.ai (former vocadesk) offers three modes,
from simplest to most powerful. You pick one per agent on the agent page.

| Mode | Best for | Who can use it |
|---|---|---|
| **Questions & forwarding** | Straight intake plus simple "if X, transfer" rules. | Existing agents already using it (legacy). |
| **Questions & conditions** | Intake plus instructions that fire only when a topic comes up. | Everyone — the default for new agents. |
| **Decision tree** | Fully scripted, branching conversations. | Operators a super admin has enabled it for. |

!!! info "Defaults and availability"
    New agents start in **Questions & conditions**. **Questions & forwarding** is a
    legacy mode kept only for agents that already use it, so their setup is preserved.
    **Decision tree** is off by default; a super admin enables it per operator
    (Super Admin dashboard → Operators → Decision tree toggle), and it then appears
    in the mode switcher for every agent under that operator.

## Questions & forwarding (simple)

The classic setup: the agent works through your
[intake questions](configuration.md#intake-questions) and, separately, applies a flat
list of [call-forwarding rules](call-forwarding.md) — "if the caller says X,
transfer to this number."

Use it when intake and forwarding are independent and you don't need the agent to
change its behavior based on what the caller says.

## Questions & conditions (scenario)

The recommended mode. You keep your standard intake questions **and** add
**conditional instructions** — called **triggers** — that only activate when a
condition is met.

A trigger has:

- a **condition** in plain language (for example *"the caller wants to book a
  viewing"*), and
- one or more **actions**: **say** something, **ask** extra questions, and/or
  **forward** the call.

When a caller raises a topic that matches a trigger, the agent acts on it
immediately — even mid-intake — instead of finishing every standard question first.

!!! warning "Write specific conditions"
    Vague conditions ("the caller needs help") make the agent fire triggers at the
    wrong time, or miss them. Be concrete about what the caller says or wants.

Forwarding is just an action on a trigger here — see
[Call forwarding & transfers](call-forwarding.md) for how that behaves.

## Decision tree (advanced)

A **decision tree** scripts the whole call as a branching flow: each step is either a
yes/no condition or an action (say something, collect a field, transfer, answer from
knowledge, or end). It replaces standard intake entirely and gives you precise
control over every branch.

Decision tree suits complex, highly-regulated, or heavily-scripted call flows. A
super admin must enable it for your operator before it appears in the mode
switcher below.

## Switching modes

The mode switcher on the agent page only shows the modes available to you. Switching
to **Questions & conditions** brings your existing forwarding rules across as
forward-only triggers, so nothing is lost.
