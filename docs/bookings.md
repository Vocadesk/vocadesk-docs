---
title: Appointment bookings (Cliniko)
summary: Let an agent move or cancel a caller's appointment in Cliniko during the call, and control how callers are verified, what is kept and which agents can do it.
tags:
  - bookings
  - clients
  - agents
  - integrations
  - settings
keywords:
  - cliniko
  - appointments
  - reschedule
  - cancel appointment
  - api key
  - verification
  - date of birth
  - caller id
  - audit log
  - retention
  - practice management
help_key: bookings.overview
help_keys:
  - bookings.connection
  - bookings.businesses
  - bookings.verification
  - bookings.no_caller_id
  - bookings.unknown_number
  - bookings.after_change
  - bookings.patient_notice
  - bookings.cancellation_notice
  - bookings.retention
  - bookings.daily_cap
  - bookings.agent_switch
  - bookings.audit
---

# Appointment bookings (Cliniko)

With **bookings**, an agent can look up a caller's upcoming appointment in
[Cliniko](https://www.cliniko.com), **move** it to another time or **cancel** it, all
during the call. The caller is identified first, the agent reads the change back, and
nothing is written to Cliniko until the caller says yes.

Bookings live on the **Bookings** tab of a [client](clients.md). The tab only appears
once a super-admin has switched **Bookings** on for your operator (see
[Administration](admin.md#bookings-enabled)). It is for operator admins and
super-admins; regular users don't see it.

What v1 does and does not do:

- It **moves and cancels** existing appointments. It does not create new bookings or
  patients.
- It works for **scenario-mode, English** agents only.
- Only the **same practitioner and appointment type** can be offered when moving an
  appointment.

## Connect Cliniko {#connection}

Create a **dedicated Cliniko user** with the minimum role that can view patients and
manage appointments, generate the API key from that user, and paste it into the
**Cliniko connection** card. A key carries the full permissions of the user who made it,
so a narrow role limits the damage if the key ever leaks.

After you connect, the card shows:

- the **last 4 characters** of the key, never the key itself (it is stored encrypted and
  can't be read back);
- the **key owner and their role**, with a warning if the role is broad;
- the **status** (connected, key rejected, or disconnected), when the key was **last
  verified**, and the **last error** if there was one.

The key is re-verified every night. Use **Re-verify** to check it now.

!!! warning "Role too narrow"
    If Cliniko refuses one of the requests the connection needs, the card says
    **This Cliniko user's role is too narrow**. Give that user a role that can view
    patients and manage appointments, or generate the key from a different user, then
    re-verify or replace the key.

**Replace key** swaps in a new key without losing your settings. The new key is checked
first. If Cliniko rejects a key at any time, the connection is marked **Key rejected**
and bookings are switched off for the client's agents until you replace it.

### Disconnecting

**Disconnect** deletes our stored copy of the key immediately and switches bookings off
for all of the client's agents. **The key stays valid in Cliniko until you archive it
there**, so archive it in Cliniko too. The panel reminds you after you disconnect.

## Businesses and what can be changed by phone {#businesses}

This card lists the Cliniko **businesses** the key can see, each with its timezone and the
**practitioner and appointment type combinations** that are enabled for online booking.

**Phone offers follow your Cliniko online-booking limits.** An appointment can be moved by
phone only when its business, practitioner and appointment type are all enabled for online
booking and it is no longer than the appointment type's length. Any other appointment can be
cancelled by phone, but moving it means taking a message for the clinic.

If online booking is switched off in Cliniko altogether, no appointment can be moved by
phone.

## Settings

### How callers are verified {#verification}

What the agent asks for before it reads out any appointment. Options: **date of birth**
(the default), **full name**, **surname and date of birth**, or **full name and date of
birth**. The caller ID is also matched against the phone numbers Cliniko holds for the
patient.

!!! warning "Caller ID can be spoofed"
    Caller ID is not authenticated. With the default (date of birth only), someone who
    calls from a spoofed number and knows a patient's date of birth can reach that
    patient's appointments. A stricter set of details lowers the risk. Record this limit
    in your data protection impact assessment.

### Callers with no caller ID {#no-caller-id}

Withheld numbers, the web widget and the browser test call have no number to match. The
agent asks for these details instead: **surname and date of birth** (the default),
**full name and date of birth**, or **don't book and take a message**.

!!! warning "Weaker than a number on file"
    Without a caller ID the details alone open the record, which is weaker than calling
    from a number held in Cliniko. The web widget and the browser test call need no login.
    Repeated wrong guesses are limited by the [daily cap](#daily-cap).

### Details match, but the number isn't on file {#unknown-number}

What happens when the caller's details match one patient whose phone numbers don't include
the number they're calling from: **take a message** (the default), or **ask for the full
name too and accept**.

!!! warning "The full-name option tells callers their details matched"
    With the full-name option the agent asks for more details only in this case, so
    callers learn that their details matched a patient. With **take a message** the caller
    hears the same thing whether the details or the number was wrong.

### After a change {#after-change}

What the agent does once an appointment has been moved or cancelled: **carry on with the
intake questions** (the default), or **close with a booking line** such as "Your
appointment is now Tuesday at 2:30pm with Dana. Is there anything else I can help with?"

### Email to the patient {#patient-notice}

Optionally send the patient an email after a change: **no email** (the default) or
**send an email**. It goes to the address Cliniko holds for the patient, never to the
calling number. Each email is its own cost line in your price. Cliniko can already email
patients about changes, so check that patients don't get two.

### Cancellation notice {#cancellation-notice}

Applies to **cancelling and to rescheduling**. Inside the window the agent takes a message
instead of making the change. Options: **use Cliniko's rule** (its minimum notice for
patient cancellations), **custom hours**, or **no notice window**.

The panel shows Cliniko's current value. If Cliniko's notice is **unset or 0**, you must
choose **custom hours**, and agents can't have bookings switched on until you do.

### Keep call data for {#retention}

Transcripts, recordings, summaries and extracted data of this client's booking-agent calls
are deleted after this many days (default 90). The change applies to this client only.

!!! warning "Recordings hold the date of birth"
    Dates of birth are removed from transcripts, but a recording still holds the spoken
    date of birth until it is deleted under this rule. Confirm the number against your
    agreement with the clinic.

### No-caller-ID daily cap {#daily-cap}

The number of failed verifications allowed per day on calls without a caller ID (default
10). When it is reached, bookings on such calls stop for this client until the next day
and an alert is sent. Set it to 0 to stop them straight away.

## Switch bookings on for an agent {#agent-switch}

In the **Agents** card, each agent has a **bookings switch** and a **business picker**.
Pick the Cliniko business or businesses the agent may act for, then turn the switch on.

The switch is refused, with the reason shown under the agent, unless:

- Cliniko is connected and verified;
- the agent runs in **scenario mode** and its language is **English**;
- at least one business is chosen, every chosen business is **online-bookable**, and the
  chosen businesses share **one timezone**;
- Cliniko's cancellation notice is set (or you've set custom hours).

Turning an agent's switch off, or disconnecting Cliniko, takes effect during a live call.
Duplicating an agent to a different client does not copy its bookings settings.

## Audit log {#audit}

Every read and change an agent makes in Cliniko is logged, newest first: when, what
(looked up a patient, listed appointments, looked up free times, rescheduled, cancelled,
moved back), the outcome, the agent, a link to the call and how long it took. Use it to
review the first calls of a new agent.

The log never stores patient names, dates of birth or phone numbers.

## Related

- Add or edit the agents that use bookings → [Agents](agents/index.md)
- Turn the feature on for an operator → [Administration](admin.md#bookings-enabled)
