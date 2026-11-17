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

This page is the reference for the **Bookings** tab. The Cliniko user manual walks
through the whole feature:

| Page | What it covers |
|---|---|
| [Set up Cliniko bookings](setup.md) | Preparing Cliniko, connecting it, choosing settings, switching agents on, testing and going live |
| [What happens on a booking call](calls.md) | What the caller is asked and hears, step by step, and when the agent takes a message instead |
| [Running bookings day to day](running.md) | Audit log, alert emails, summary emails, the patient email, nightly checks, data deletion, changing or removing the key |
| [Bookings troubleshooting](troubleshooting.md) | Common problems and questions, and how to fix them |

## Who sees the Bookings tab

Bookings live on the **Bookings** tab of a [client](../clients.md), between **Embeds** and
**Info**. The tab is for operator admins and super-admins; regular users don't see it.

- **Operator admins** see the tab only once a super-admin has switched **Bookings** on
  for their operator (see [Administration](../admin.md#bookings-enabled)).
- **Super-admins** always see it. While the operator's switch is off they get a banner,
  and connecting, saving settings and switching agents on are refused. Only
  **Disconnect** still works.

## What v1 does and does not do

- It **moves and cancels** existing appointments. It does not create new bookings or
  patients, and it never writes to a patient's record.
- It works for **scenario-mode, English** agents only.
- A move keeps the **same practitioner and appointment type**. Anything else becomes a
  message for the clinic.

## Connect Cliniko {#connection}

Create a **dedicated Cliniko user** with the minimum role that can view patients and
manage appointments, generate the API key from that user, and paste it into the
**Cliniko connection** card. A key carries the full permissions of the user who made it,
so a narrow role limits the damage if the key ever leaks.
[Set up Cliniko bookings](setup.md#cliniko-user) has the step-by-step version.

After you connect, the card shows:

- the **last 4 characters** of the key, never the key itself (it is stored encrypted and
  can't be read back);
- the **key owner and their role**, with a warning if the role is broad (Administrator,
  Bookkeeper or Power receptionist);
- the **status** (**Connected**, **Key rejected** or **Disconnected**), when the key was
  **last verified**, and the **last error** if there was one.

The key is re-verified every night. Use **Re-verify** to check it now.

!!! warning "Role too narrow"
    If Cliniko refuses one of the requests the connection needs, the card says
    **This Cliniko user's role is too narrow**. Give that user a role that can view
    patients and manage appointments, or generate the key from a different user, then
    re-verify or replace the key.

**Replace key** swaps in a new key. The new key is checked first, and your settings and
agents are kept. An agent whose businesses are no longer valid for the new key loses its
bookings switch. If Cliniko rejects a key at any time, the connection is marked
**Key rejected** and bookings are switched off for all of the client's agents until you
replace it.

### Disconnecting

**Disconnect** deletes our stored copy of the key immediately and switches bookings off
for all of the client's agents. **Settings are not kept**: connecting again starts from
the defaults. **The key stays valid in Cliniko until you archive it there**, so archive
it in Cliniko too. The panel reminds you after you disconnect.

## Businesses and what can be changed by phone {#businesses}

This card lists the Cliniko **businesses** the key can see. Each shows whether it is
**Online-bookable**, its timezone, and the **practitioner and appointment type
combinations** that are enabled for online booking, with their length.

**Phone offers follow your Cliniko online-booking limits.** An appointment can be moved by
phone only when its business, practitioner and appointment type are all enabled for online
booking and it is no longer than the appointment type's length. Any other appointment can
be cancelled by phone but not moved. Moving it becomes a message for the clinic.

The card also shows **About N booking flows per minute at once**: an estimate of what the
connection's Cliniko rate limit allows (about 10 for one Cliniko user). It is not a
guarantee, and the limit is shared with any other software using the same Cliniko user.

If online booking is switched off in Cliniko altogether, no appointment can be moved by
phone. Cancelling is still possible. A business whose timezone can't be worked out is
marked **Timezone unknown** and bookings are blocked there. **Notes from the last check**
lists anything else Cliniko's answer raised.

## Settings

Each setting has its own **?** button. **Save** is enabled once something has changed and
saves only what you changed.

### How callers are verified {#verification}

What the agent asks for before it reads out any appointment. Options: **Date of birth**
(the default), **Full name**, **Surname and date of birth**, or **Full name and date of
birth**. The caller ID is also matched against the phone numbers Cliniko holds for the
patient.

!!! warning "Caller ID can be spoofed"
    Caller ID is not authenticated. With the default (date of birth only), someone who
    calls from a spoofed number and knows a patient's date of birth can reach that
    patient's appointments. A stricter set of details lowers the risk. Record this limit
    in your data protection impact assessment.

### Callers with no caller ID {#no-caller-id}

Withheld numbers, the web widget and the browser test call have no number to match. The
agent asks for these details instead: **Surname and date of birth** (the default),
**Full name and date of birth**, or **Don't book: take a message**.

!!! warning "Weaker than a number on file"
    Without a caller ID the details alone open the record, which is weaker than calling
    from a number held in Cliniko. The web widget and the browser test call need no login.
    Repeated wrong guesses are limited by the [daily cap](#daily-cap).

### Details match, but the number isn't on file {#unknown-number}

What happens when the caller's details match one patient whose phone numbers don't include
the number they're calling from: **Take a message** (the default), or **Ask for the full
name too, and accept**.

!!! warning "The full-name option tells callers their details matched"
    With the full-name option the agent asks for more details only in this case, so
    callers learn that their details matched a patient. With **Take a message** the caller
    hears the same thing whether the details or the number was wrong.

### After a change {#after-change}

What the agent does once an appointment has been moved or cancelled: **Carry on with the
intake questions** (the default), or **Close with a booking line**: the agent confirms
the change ("Your appointment is now Friday the 15th of November at 10am with Dana."),
asks whether there is anything else, and skips the intake questions.

### Email to the patient {#patient-notice}

Optionally send the patient an email after a change: **No email** (the default) or
**Send an email**. It goes to the address Cliniko holds for the patient, never to the
calling number. Each email is its own cost line in your price. Cliniko can already email
patients about changes, so check that patients don't get two.
[Running bookings day to day](running.md#patient-email) shows what the email says.

### Cancellation notice {#cancellation-notice}

Applies to **cancelling and to rescheduling**. Inside the window the agent takes a message
instead of making the change. Options: **Use Cliniko's rule** (its minimum notice for
patient cancellations), **Custom hours** (whole hours, 1 to 8760), or **No notice
window**.

The panel shows Cliniko's current value. If Cliniko's notice is **unset or 0**, you must
choose **Custom hours**, and agents can't have bookings switched on until you do.

### Keep call data for {#retention}

Transcripts, recordings, summaries and extracted data of this client's booking-agent calls
are deleted after this many days (default 90, range 1 to 3650). The change applies to this
client only. [Running bookings day to day](running.md#retention) lists exactly which calls
are covered.

!!! warning "Recordings hold the date of birth"
    Dates of birth are removed from transcripts, but a recording still holds the spoken
    date of birth until it is deleted under this rule. Confirm the number against your
    agreement with the clinic.

### No-caller-ID daily cap {#daily-cap}

The number of failed verifications allowed per day on calls without a caller ID (default
10, range 0 to 1000). When it is reached, bookings on such calls stop for this client
until the next day (UTC). Set it to 0 to stop them straight away.

## Switch bookings on for an agent {#agent-switch}

The **Agents** card appears once Cliniko is connected. Each agent has a **bookings switch**
and a **Businesses** picker. Tick the Cliniko business or businesses the agent may act
for, then turn the switch on. To change the businesses of an agent that is already on,
change the ticks and press **Save businesses**.

The switch can only be turned on while the connection is **Connected** and the operator's
Bookings switch is on. It is greyed out, with a note, for an agent that is **disabled**,
not in **scenario mode**, or not **English**. A business that isn't online-bookable can't
be ticked.

If the switch is refused, the reason shows under the agent. The rules are:

- Cliniko is connected and verified;
- at least one business is chosen, every chosen business is **online-bookable**, and the
  chosen businesses share **one timezone**;
- Cliniko's cancellation notice is set (or you've set custom hours).

Switching an agent off is always allowed. Turning an agent's switch off, or disconnecting
Cliniko, takes effect during a live call: the agent takes a message at the next booking
step. Duplicating an agent to a different client does not copy its bookings settings.

## Audit log {#audit}

Every read and change an agent makes in Cliniko is logged, newest first, 50 rows at a time
(**Load older** for more). Columns: **Time**, **Action**, **Outcome**, **Agent**, **Call**
(a **View call** link), **Details** and **Time taken**.

Actions: **Looked up patient**, **Verification failed**, **Listed appointments**,
**Looked up free times**, **Rescheduled**, **Moved back**, **Cancelled** and **Checked the
connection**. Use it to review the first calls of a new agent.
[Running bookings day to day](running.md#audit) explains the outcomes.

The log never stores patient names, dates of birth or phone numbers.

## Related

- Add or edit the agents that use bookings → [Agents](../agents/index.md)
- Turn the feature on for an operator → [Administration](../admin.md#bookings-enabled)
