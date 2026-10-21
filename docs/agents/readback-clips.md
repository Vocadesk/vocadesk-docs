---
title: Readback clips
summary: How your agent reads back spelled names, emails and phone numbers with pre-recorded letters and digits in its own voice, and what happens when a voice has no clips.
tags:
  - agents
  - voice
  - voices
  - dictation
keywords:
  - readback
  - read back
  - clips
  - pre-recorded
  - spelling
  - letters
  - digits
  - email
  - phone number
  - live speech
  - fallback
help_key: readback_clips
---

# Readback clips

When a caller gives a name, an email address or a phone number, your agent reads it
back so the caller can say "yes" or correct it. Reading letters and digits one at a
time is the hardest thing for a synthetic voice: letters can be swallowed, run together
into one word ("A, M, D" heard as "Amd"), or said with a different rhythm every time.

**Readback clips** fix this. Instead of asking the voice to speak each letter live, the
agent plays short recordings of each letter, digit and symbol, made in advance with
**the same voice** your agent uses, and puts them together with the right pauses.

## What the caller hears

The caller hears the same agent voice and the same words as before:

> "I have T, O, M, then B, A, K, E, R. Is that right?"

What changes is how it sounds: the readback starts straight away (there is nothing to
wait for), every letter is clear and separate, and the pace is the same on every call.
The wording of the readback is not changed by clips.

## Which values use clips

Clips are used when the agent reads back a value the caller **spelled or dictated**:

- **Names** spelled letter by letter.
- **Email addresses**: letters, digits, and the symbols *at*, *dot*, *dash*,
  *underscore*, *plus* and *apostrophe*.
- **Phone numbers** and other digit sequences, with the usual grouping pauses.
- The short readback sentences around them, such as "Is that right?".

Everything else the agent says (greetings, questions, answers from your knowledge
base) is spoken live, as always. Clips exist in English and Hebrew; a Hebrew agent reads
a Latin-letter email address with its own Hebrew voice.

## When a voice has no clips: live speech

The agent only uses clips for a voice whose **complete** set has been prepared and
checked. If a voice has no clips yet, or the set is incomplete, or a clip fails its
check, the agent simply speaks the readback live, exactly as it did before clips
existed. **A call never fails or goes quiet because of missing clips.** The only
difference is that the readback sounds like normal live speech.

Super-admins see which case applied: the test-call cost window shows a line
**"Readback clips (N tokens played)"** when clips were used and
**"Readback: live TTS (no clip library for this voice)"** when they were not.
Clips cost nothing per call, so the line shows no charge.

## How a new voice or preset gets its clips

There is nothing to do. A scheduled job looks at the voice presets, finds any voice
that has no clips, records and checks them, and stores them. A preset added today
normally has its clips by the next morning. (A custom voice that is not one of the
presets is prepared when the same job is started by hand with that voice.)

How the check works: every clip is transcribed again and compared with the letter it
should be. A clip that does not pass is not used, and the voice stays on live speech
until it is fixed.

In the super-admin voice picker (staging) every preset carries a small marker:

| Marker | Meaning |
| --- | --- |
| **Readback clips ready** | The full set is prepared and checked. |
| **Readback clips missing** | Not prepared yet; the agent uses live speech. |
| **Readback clips need review** | Some clips failed the check and are listed; the agent uses live speech until they are re-recorded. |

!!! note "Rollout"
    Readback clips are being introduced step by step, staging first, voice by voice,
    after the owner has listened to the samples. Until a voice is switched on, its
    readbacks stay on live speech.

## What's next

- Choose a voice → [Voices & languages](voices.md)
- Hear it for yourself → [Testing your agent](testing.md)
