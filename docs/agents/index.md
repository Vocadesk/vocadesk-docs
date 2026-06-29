---
title: Agents
summary: What an agent is and the three things you configure — who it is, how it converses, and when it transfers.
tags:
  - agents
  - getting-started
keywords:
  - agent
  - voice agent
  - receptionist
  - create agent
help_key: agents.overview
---

# Agents

An **agent** is an AI voice receptionist that belongs to one
[client](../concepts.md#client). It answers calls in a voice and persona you choose,
follows the conversation design you set, collects the information you ask for, and
transfers to a human when your rules say so.

Configuring an agent comes down to three decisions:

<div class="grid cards" markdown>

-   :material-account-voice: **Who it is**

    Persona, voice, language, greeting, and the knowledge it can draw on.

    [→ Configuring an agent](configuration.md)

-   :material-sitemap: **How it converses**

    Plain intake, conditional instructions, or a full decision tree.

    [→ Conversation design](conversation-design.md)

-   :material-phone-forward: **When it hands off**

    Conditions under which the call is transferred to a person.

    [→ Call forwarding & transfers](call-forwarding.md)

</div>

## Creating an agent

1. Open a [client](../concepts.md#client) and go to its **Agents** tab.
2. Select **New agent** — a persona is suggested based on the client's country.
3. Adjust the [persona, voice, and knowledge](configuration.md).
4. Choose a [conversation design](conversation-design.md) and add your questions.
5. Add [forwarding rules](call-forwarding.md) if a human should ever take over.
6. **Test the agent** with a browser call before attaching a phone number.

!!! tip "Test before you go live"
    Use the **Test call** button on the agent page to talk to the agent from your
    browser. Nothing is billed to the client and the call is marked as a `test`.

## Plan limits

How many agents a client can have is set by its subscription plan. When a client is
at its limit, the **New agent** action is disabled with a "plan limit reached"
notice — upgrade the client's plan to add more.
