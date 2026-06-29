---
title: Call forwarding & transfers
summary: Set the conditions under which an agent hands a call to a human, and understand exactly how the transfer behaves.
tags:
  - agents
  - forwarding
  - conversation-design
  - scenario
  - calls
keywords:
  - call forwarding
  - transfer
  - hand off to human
  - forwarding rules
  - forward trigger
  - escalation
help_key: agents.call_forwarding
---

# Call forwarding & transfers

**Call forwarding** lets an agent hand a live call to a person when your conditions
are met. How you configure it depends on the agent's
[conversation design](conversation-design.md):

- In **Questions & forwarding**, you use a flat list of **forwarding rules**.
- In **Questions & conditions**, forwarding is a **forward action on a trigger**.

Both end up doing the same thing at call time.

## Forwarding rules (simple mode)

Enable **Call forwarding** on the agent, then add one or more rules. Each rule is:

> **If** *&lt;condition in plain language&gt;*, transfer to *&lt;phone number&gt;*.

For example: *If the caller has an urgent maintenance issue, transfer to
+44 7700 900123.*

- The number must be in international format (with a country code), e.g.
  `+1 555 123 4567`.
- You can add several rules; the agent transfers on the first one whose condition is
  met in full.

## Forward triggers (Questions & conditions)

In [scenario mode](conversation-design.md#questions-conditions-scenario), add a
trigger, give it a **condition**, and enable the **Forward** action with a number.
You can combine **say** and **ask** on the same trigger — the agent will say your
line and collect any extra questions, then connect the caller.

!!! info "Forwarding ends the agent's part of the call"
    When a trigger forwards, the agent does **not** go back to finish standard intake
    afterwards. The moment a forward condition applies, the agent connects the caller
    — it won't keep asking the remaining questions first.

## How a transfer behaves

When the agent decides to transfer:

1. It says one short, natural line first — *"Sure, let me connect you now, one
   moment please."* — so the caller always hears the hand-off.
2. It connects the caller in the **same turn** (it never promises a transfer and then
   forgets to do it, and it never announces the transfer twice).
3. A transfer is **not** treated as the end of the call — the agent doesn't say
   goodbye or sign off; it just connects.

### Caller asks for a human, but no condition matches

If a caller simply asks to speak to someone without meeting a specific forwarding
condition, the agent does **not** transfer. Instead it explains that it's the AI
assistant handling the line, assures the caller their details will reach the right
person, and continues collecting information.

!!! tip "Make conditions explicit"
    Transfers only happen on conditions you define. If you want "asks for a manager"
    to forward, add that as an explicit condition.

## Channel differences

- **Phone (PSTN) calls** are transferred by dialing the configured number.
- **Web and test calls** signal the browser to hand off — no outbound phone call is
  placed from the server.

## Verifying it works

Place a [test call](index.md#creating-an-agent) and trigger your condition out loud.
You should hear the agent's connecting line, after which the transfer is signalled.
Test calls won't dial a real phone, so this confirms the *decision*, not the dialing.
