---
title: Phone numbers
summary: Attach a phone number to an agent so inbound calls are answered automatically.
tags:
  - phone-numbers
  - agents
  - calls
keywords:
  - phone number
  - inbound calls
  - assign number
  - twilio number
help_key: phone_numbers.overview
---

# Phone numbers

A **phone number** routes inbound phone (PSTN) calls to a specific
[agent](agents/index.md). Once a number is attached, every call to it is answered by
that agent.

## Assigning a number

From a client's **Phone numbers** tab, add a number and assign it to an agent. How
many numbers a client can hold is set by its [plan](billing.md).

!!! note "One agent per number"
    A phone number routes to exactly one agent. To change which agent answers, reassign
    the number — it can't point at two agents at once.

## Phone vs. web vs. test calls

- **Phone** calls come in over the telephone network to an assigned number.
- **Web** calls come from an [embed](embeds.md) button and need no number.
- **Test** calls are placed from the dashboard and need no number.

All three are reviewed together in [Calls](calls.md).

## Transfers

When an agent transfers a phone call (per your
[forwarding rules](agents/call-forwarding.md)), the call is connected to the number
you configured on the rule or trigger. On web and test calls the transfer is signalled
to the browser instead of dialling out.
