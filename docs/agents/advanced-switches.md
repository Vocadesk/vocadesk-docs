---
title: Advanced agent switches (super-admin)
summary: Per-agent super-admin switches that change how the agent collects and speaks back spelled details and the next question.
tags:
  - agents
  - configuration
  - dictation
  - admin
keywords:
  - dictation mode
  - spelling
  - email spelling
  - runtime asks next question
  - super admin
  - advanced
help_key: agents.advanced_switches
help_keys:
  - agents.derive_email_spelling
  - agents.tuned_spelling
  - agents.dictation_mode
  - agents.runtime_next_question
---

# Advanced agent switches (super-admin)

These switches sit in the **Advanced (super admin)** card of the agent page. Only a
`super_admin` can see or change them. They are per agent, so you can try one on a
single agent. The first three are **on** by default; the last one is **off**.

## Reuse confirmed spellings in the email {#derive-email-spelling}

When the caller's email contains their name or company and they did not spell that
part, the agent uses the spelling they already confirmed instead of what it heard. A
spelling the caller spells out for the email always wins. This never invents anything:
it only reuses a spelling the caller confirmed on the same call.

Turn it **off** to make the agent use only what it heard for the email.

## Tuned spelling-accuracy rules {#tuned-spelling}

Adds stricter rules so the agent does not blend a spelled name with the version it
heard first. Example: it hears "Visaka", the caller spells V-I-S-O-C-K-A, and the agent
must store "Visocka", not a mix. It also switches on a small extra check of spelled
values by a fast AI model, so each captured spelling costs one small extra model call.

Turn it **off** to go back to the plain rules for this agent.

## Dictation mode {#dictation-mode}

When a caller spells an email, name, company, address or postcode, the system itself
collects the letters across turns, reads the result back, and takes the yes or no. The
AI model no longer decides when a spelling is finished or asks the caller to spell it
again.

Turn it **off** to hand that job back to the model.

## Runtime asks the next question {#runtime-next-question}

After the agent records a caller's answer, the runtime itself says a short **"Thanks."**
and then the agent's next configured question, instead of making a second AI call to
write it.

- **Cheaper and faster:** one AI call less per answered question, roughly one to two
  seconds sooner.
- **Fixed wording:** the acknowledgement is always the same short phrase.
- **Safe fallback:** anything unusual (the caller asks something, changes an earlier
  answer, interrupts) still goes to the AI as before.
- **Off by default.** Super-admin only. Turn it on for one agent, make a test call,
  and compare how it sounds before using it more widely.

## Related

- Spelled values in a call → [Configuring an agent](configuration.md#intake-questions)
