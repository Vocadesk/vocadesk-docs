---
title: What happens on a booking call
summary: Step by step, what a caller is asked and hears when they move or cancel a Cliniko appointment with an agent, and when the agent takes a message instead.
tags:
  - bookings
  - calls
  - agents
keywords:
  - cliniko
  - reschedule
  - cancel appointment
  - verification
  - date of birth
  - read back
  - take a message
  - free times
---

# What happens on a booking call

This page follows a booking call from the caller's side. The quoted lines are the fixed
words the agent says. Other wording comes from the agent's conversation and varies from
call to call. The examples use an appointment with Dana on Tuesday the 12th of November
at 2:30pm.

## When the booking steps start {#start}

At any point in the call, a caller who wants to **look up, check, change, move,
reschedule or cancel an appointment they already have** is taken into the booking steps.
The agent recognises this from what the caller says; there is no keyword to say. It comes
before the agent's other triggers about appointments.

The booking steps aren't offered:

- on an agent without the bookings switch, or one that isn't in scenario mode;
- while the agent is forwarding the call or ending it.

A caller who wants a **new** appointment, a different practitioner or a different
appointment type gets a message taken for the clinic: v1 only moves and cancels existing
appointments.

## 1. Verifying the caller {#verify}

The agent asks for the details set in
[How callers are verified](index.md#verification), one at a time:

| Setting | The caller is asked for |
|---|---|
| Date of birth (default) | date of birth |
| Full name | full name |
| Surname and date of birth | surname, then date of birth |
| Full name and date of birth | full name, then date of birth |

If the call has **no caller ID** (withheld number, web widget, browser test call), the
details from [Callers with no caller ID](index.md#no-caller-id) are added, surname and
date of birth by default. If that setting is **Don't book: take a message**, the agent
says "I can't confirm that on this call, so I'll take a message for the clinic." straight
away.

- **Names** are captured the same careful way as names in the intake questions, with
  spelling and a read-back.
- **The date of birth is read back** in words, for example "The fourth of March nineteen
  eighty-five, is that right?". The lookup only runs after a clear yes. A future date, or
  one more than 120 years ago, is asked for again.
- The agent says "One moment while I check." while it looks the patient up.

**How the match works.** The details must match a Cliniko patient exactly, ignoring
capitals, accents, hyphens, apostrophes and spaces (José Smith-Jones matches jose
smithjones). There is no guessing at near matches. A full name may use the patient's
first name or their preferred first name. When there is a caller ID, it must be one of the
phone numbers Cliniko holds for that patient. If it isn't, the
[unknown-number setting](index.md#unknown-number) decides: take a message (default), or
ask for the full name too.

**If the details don't match**, the caller hears that no booking was found with those
details, without being told which detail was wrong, and is asked once more for all of
them. After a **second** failure the agent says "I can't confirm that on this call, so
I'll take a message for the clinic." and returns to the rest of the call. The booking
steps aren't offered again on that call.

Other limits stop repeated guessing across calls. When one is reached, the caller hears
the same "take a message" line:

| Limit | Value |
|---|---|
| Failed verifications per call | 2 |
| Failed verifications per calling number, per day | 6 |
| Failed number checks against one patient, per day | 6 (that patient can't be verified by phone for the rest of the day) |
| Failed verifications on calls with no caller ID, per client, per day | the [daily cap](index.md#daily-cap), 10 by default |

Days are counted in UTC. If two patients fit the same details equally well (for example
twins calling from a shared number), the agent can't tell them apart and takes a message.

Once verified, the caller stays verified for the rest of the call. A call can only act on
**one patient's** appointments.

## 2. Finding the appointment {#find}

The agent reads out up to **three** upcoming appointments, nearest first, with the
practitioner and the time, for example "Tuesday the 12th of November at 2:30pm with
Dana". If there are several, the caller can pick by order ("the second one"), day ("the
Tuesday one") or practitioner. Only appointments at the businesses chosen for the agent
are listed.

- **No upcoming appointment**: the agent says it can't find a booking under those
  details, and offers to take a message, or to transfer the call if the agent has
  [forwarding](../agents/call-forwarding.md) set up.
- **An appointment that can't be moved by phone** (not online-bookable, or longer than its
  appointment type): the agent offers to cancel it or take a message.
- **An appointment inside the [cancellation notice](index.md#cancellation-notice)
  window**: it can't be moved or cancelled by phone. The agent takes a message.

When the agent takes a message it says "I'll pass that on to the clinic." and carries on
with the call; the message is in the call's summary.

## 3a. Moving an appointment {#move}

1. The agent looks up free times for the **same practitioner and appointment type** at the
   same business, up to four weeks ahead and within the clinic's online-booking lead time
   and booking window ("One moment while I check.").
2. It offers **three** times at a time, in the clinic's local time. The caller can ask for
   a day, a date range, or the morning (before 12), afternoon (12 to 5pm) or evening
   (after 5pm). "Anything later?" gives the next three.
3. If nothing is free in that range, the agent offers a later window once, then takes a
   message.
4. When the caller picks a time, the agent reads the change back: "I'll move your
   appointment with Dana from Tuesday the 12th of November at 2:30pm to Friday the 15th of
   November at 10am. Shall I go ahead?"
5. Only a **clear yes** makes the change ("yes", "yeah", "go ahead", "that's right",
   "yes, Friday at 10 is fine"). "Yes, but make it 3", "wait", "I guess so" or a yes
   followed by "actually…" are not a yes. If the answer is unclear, the agent asks "Shall
   I go ahead and move it to Friday at 10am?", then "Shall I leave it as it is?". Anything
   but a clear go-ahead leaves the appointment alone: "No problem, I'll leave your
   appointment as it is."
6. After the yes: "One moment while I make that change.", then "Your appointment is now
   Friday the 15th of November at 10am with Dana."

**If the time was taken meanwhile**, the agent says so, looks again once and offers new
times. If someone else booked the same time in the moment the change was made, the move
is undone: "I'm sorry, that time was just taken by someone else, so your appointment
stays as it was, Tuesday the 12th of November at 2:30pm with Dana." The clinic gets an
alert email.

In Cliniko the appointment simply moves, keeping its length. No note is added.

## 3b. Cancelling an appointment {#cancel}

1. The agent reads it back: "I'll cancel your appointment with Dana on Tuesday the 12th of
   November at 2:30pm. Shall I go ahead?"
2. Only a clear yes cancels it ("yes, cancel it"). Unclear answers get "Shall I go ahead
   and cancel it?", then "Shall I leave it as it is?".
3. After the yes: "Your appointment on Tuesday the 12th of November at 2:30pm is
   cancelled."

In Cliniko the appointment is cancelled with a cancellation reason the agent picks from
what the caller said (feeling better, condition worse, sick, away, work or other) and the
note "Cancelled by phone agent at caller's request". Repeats of the appointment are not
cancelled.

## 4. After the change {#after}

What happens next follows [After a change](index.md#after-change):

- **Carry on with the intake questions** (default): the agent goes on with the agent's
  next unanswered question.
- **Close with a booking line**: the agent reads out the change once, asks whether there
  is anything else, and if not, says a plain goodbye. The change isn't repeated at the end.

If the caller changes their mind after a change, the agent takes a message for the
clinic; it doesn't undo the change itself. If [Email to the patient](index.md#patient-notice)
is on, the patient gets an email about the change.

## When something goes wrong {#errors}

| Situation | The caller hears |
|---|---|
| Cliniko is down, slow or busy, or the key stopped working | "Sorry, I can't do that right now. I'll pass that on to the clinic." |
| The change was sent but Cliniko didn't confirm it in time | "I couldn't confirm that went through; the clinic will confirm with you." The clinic gets an alert email to check the appointment. |
| Bookings were switched off for the agent or operator, or Cliniko was disconnected, during the call | A "take a message" line at the next booking step. |

The agent never retries a change on its own, so a change can't be made twice.

## What the call record shows {#record}

- **Transcript**: every date of birth is replaced with **[date of birth]**, in the
  caller's and the agent's turns. Appointment times stay.
- **Recording**: still holds the spoken date of birth until it is deleted under
  [Keep call data for](index.md#retention).
- **Summary and extracted data**: never include a date of birth or appointment type. Only
  the agent's own question fields are kept in the extracted data.
- **Summary email**: an **Appointment** section with one line per outcome. See
  [Running bookings day to day](running.md#summary-email).
- **Audit log**: one row per lookup and change. See [Running bookings day to day](running.md#audit).

## Related

- Set up bookings for a clinic → [Set up Cliniko bookings](setup.md)
- Every setting explained → [Appointment bookings](index.md)
