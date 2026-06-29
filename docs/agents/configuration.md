---
title: Configuring an agent
summary: Set an agent's persona, voice, language, greeting, knowledge base, and intake questions.
tags:
  - agents
  - configuration
  - voice
  - knowledge-base
  - questions
keywords:
  - persona
  - voice
  - language
  - greeting
  - knowledge base
  - intake questions
  - data collection
help_key: agents.configuration
---

# Configuring an agent

This page covers **who the agent is** — its persona, voice, and what it knows and
asks. For how it runs the conversation, see
[Conversation design](conversation-design.md); for hand-off, see
[Call forwarding](call-forwarding.md).

## Persona

A **persona** is a ready-made package of voice + personality + language, shown with a
photo and a short description (for example *"Warm and professional British
receptionist"*). Choosing a persona sets a sensible default voice, greeting, and
language in one click.

- Open **Change persona** on the agent page to browse personas.
- Personas are grouped by **language** — pick the language first, then the voice.
- The persona's avatar follows the agent everywhere it appears (the agents list, the
  edit page), so the picture always matches the selected voice.

!!! note "Some personas are restricted"
    A few personas (for example Hebrew-language voices) are only available to
    super-admin users.

## Voice & language

Each persona maps to a specific voice from a speech provider. The agent speaks — and
expects to hear — the persona's language. If a caller switches language mid-call, the
agent keeps replying in its configured language unless told otherwise.

## Greeting & opening question

The **greeting** is the first thing the agent says when it picks up, for example:

> "Thank you for calling Elegant Homes, this is Grace. How can I help you today?"

A good greeting names the business, names the agent, and invites the caller to
explain why they're calling. The caller's answer is scanned immediately for anything
that already answers one of your intake questions, so the agent never re-asks for
something the caller just told it.

## Knowledge base

The **knowledge base** is free-text the agent can use to answer factual questions
about the business — hours, services, pricing, location, process. If a caller asks
something covered here, the agent answers first, then continues collecting any
information it still needs.

!!! tip "Answer first, collect second"
    Callers' questions take priority. The agent will answer from the knowledge base
    before pushing on with intake — this feels natural and avoids interrogations.

## Intake questions

**Intake questions** are the structured information you want from every caller — name,
phone number, reason for calling, and so on. Each question has:

- the **spoken question** the agent asks,
- an internal **field name** used to store the answer (never read aloud), and
- a **type** (text, phone, email, …) and whether it's **required**.

The agent asks one question at a time, skips anything the caller already provided,
and validates answers as they're given (for example, reading an email address back
phonetically to confirm spelling).

Reorder questions by dragging them; the order is the order they're asked.

## Saving

Changes autosave as you edit. A status indicator shows **"All changes saved"** once a
change has persisted.
