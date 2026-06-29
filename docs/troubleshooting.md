---
title: Troubleshooting
summary: Common issues with agents, calls, and embeds — and how to fix them.
tags:
  - troubleshooting
  - agents
  - calls
  - embeds
keywords:
  - troubleshooting
  - problem
  - not working
  - no audio
  - agent silent
  - help
help_key: troubleshooting
---

# Troubleshooting

Quick fixes for the things people hit most often. If something here doesn't resolve
it, gather the call (or agent) details and contact support.

## Agents

??? question "The agent answers but I can't hear it on a test call"
    Test calls run in your browser. Check that your browser tab isn't muted and that
    audio output is allowed for the page, then place the test call again. The
    transcript updating while you hear nothing usually points to browser audio, not
    the agent.

??? question "The agent's thumbnail doesn't match its voice"
    The avatar follows the agent's selected [persona](agents/configuration.md#persona).
    If it ever looks wrong, re-open **Change persona** and reselect the voice — the
    picture and the voice are kept in sync.

??? question "The agent keeps asking questions instead of transferring"
    Forwarding only happens on conditions you define, and the condition must be met in
    full. Make your [forwarding](agents/call-forwarding.md) conditions specific (what
    the caller actually says or wants). A vague condition won't reliably trigger.

??? question "The agent transfers (or doesn't) at the wrong time"
    In [Questions & conditions](agents/conversation-design.md#questions-conditions-scenario),
    triggers fire on their condition text. Tighten the wording so it matches only the
    situation you mean.

## Calls

??? question "A call has a transcript but no recording"
    Recordings are produced after the call. Give it a moment and refresh. Very short
    or abnormally-ended calls may not have a recording.

??? question "I don't see test calls in billing"
    That's expected — `test` calls and clients in `testing` status are never billed.
    See [Billing](billing.md).

## Web embeds

??? question "The website button does nothing / the call won't start"
    Confirm the visitor's domain is in the embed's
    [allowed origins](embeds.md#creating-an-embed). Calls from origins that aren't on
    the allowlist are refused. Also check that the page can request microphone access.

??? question "A visitor can't start a second call"
    Only one live call per visitor per embed is allowed at a time. End the first call
    before starting another.

## Still stuck?

Note the client, agent, and (if relevant) the specific call, then reach out to
support with those details so it can be traced quickly.
