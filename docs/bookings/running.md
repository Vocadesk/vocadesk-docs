---
title: Running bookings day to day
summary: Look after a live Cliniko connection, covering the audit log, alert emails, summary-email lines, the patient email, nightly key checks, data deletion, and changing or removing the key.
tags:
  - bookings
  - calls
  - integrations
keywords:
  - cliniko
  - audit log
  - alerts
  - summary email
  - patient email
  - retention
  - api key
  - disconnect
  - offboarding
---

# Running bookings day to day

Once a clinic is live, most of the work is reading: the audit log, the call summaries and
the occasional alert email. This page explains each, plus the jobs that run on their own
and how to change or remove the Cliniko key.

## The first week {#first-week}

For a new agent, check these every day for the first week:

- the **Audit log** on the Bookings tab: lots of **Verification failed** rows can mean
  patients' phone numbers or dates of birth are missing in Cliniko, or that the
  verification setting is too strict for the clinic's patients;
- the booking calls themselves in [Calls](../calls.md): listen to a few, and check the
  changes in Cliniko;
- any alert email.

## The audit log {#audit}

The **Audit log** card lists every read and change agents made in Cliniko, newest first,
with a **View call** link for each row. It is append-only and never stores patient names,
dates of birth, phone numbers or the key.

| Action | Meaning |
|---|---|
| Looked up patient | The agent searched for the caller. **Details** shows how many patients matched. |
| Verification failed | The caller's details or number didn't match. |
| Listed appointments | The agent read the patient's upcoming appointments. |
| Looked up free times | The agent searched for times to offer. |
| Rescheduled | An appointment was moved. |
| Moved back | A move was undone because another patient took the time. |
| Cancelled | An appointment was cancelled. |
| Checked the connection | The key was checked: at connect, on **Re-verify**, on **Replace key** or overnight. |

The **Outcome** is **OK** when the step worked. Other outcomes:

| Outcome | Meaning |
|---|---|
| Refused | The caller wasn't verified or a verification limit was reached (also when Cliniko refused a request). |
| Not allowed | The change isn't allowed by phone, for example inside the cancellation notice window. |
| Not found | No matching patient or appointment. |
| Not supported / Not bookable online | The appointment can't be moved by phone. |
| No free times | No time was free in the range the caller asked about. |
| Time was taken | The chosen time went before the change was made. |
| Unconfirmed | The change was sent but couldn't be confirmed. Check it in Cliniko. |
| Key rejected | Cliniko refused the key. |
| Role too narrow | Cliniko refused a request because of the key owner's role. |
| Unavailable / Rate limited | Cliniko was down, slow or busy. |

## Alert emails {#alerts}

Some events email the clinic straight away. Alerts go to the addresses in **Call Summary
Recipients** on the client's **Info** tab, or to its **Contact Email** if that list is
empty, and include the call ID.

| Subject | What happened | What to do |
|---|---|---|
| A booking change could not be confirmed | A change was sent to Cliniko but couldn't be confirmed. The caller was told the clinic will confirm. | Check the appointment in Cliniko and call the patient back. |
| A booking change was undone | A move was undone because another patient took the time at the same moment. The appointment is back where it was. | Usually nothing. Call the patient back if they still need a new time. |
| A moved appointment overlaps another booking | A move went through but overlaps another entry in the practitioner's diary. | Check the diary and fix the overlap. |
| Your practice system connection stopped working | Cliniko rejected the key. Bookings are off for all of the client's agents. | [Replace the key](#replace-key). |

## The summary email {#summary-email}

On a booking call, the [call-summary email](../settings.md#call-summary-emails) has an
**Appointment** section with one line per outcome, for example:

- "Appointment moved from Tuesday 12 November at 2:30 pm to Friday 15 November at 10:00 am."
- "Appointment on Tuesday 12 November at 2:30 pm cancelled (sick)."
- "Move attempted and undone because the new time was taken. The appointment stays on …"
- "Could not confirm that the reschedule went through. Please check the appointment in your
  practice system."
- "The caller could not be verified; a message was taken."
- "The caller decided to keep their appointment."
- "No matching appointment was found."
- "No free times were found; a message was taken."
- "The appointment can only be moved by the clinic; a message was taken."

If the caller changed their mind after a change, the line ends with "The caller changed
their mind afterwards; a message was taken."

## The email to the patient {#patient-email}

With [Email to the patient](index.md#patient-notice) set to **Send an email**, the
patient gets an email after a move or cancel that stands. It is not sent for a move that
was undone, or if Cliniko holds no email address for the patient.

- **From**: the operator's summary-email sender, or `no-reply@callcat.ai`.
- **Subject**: "Your appointment has been moved - *clinic name*" or "Your appointment has
  been cancelled - *clinic name*".
- **Body**: "Hello *first name*," (the patient's preferred first name in Cliniko, else
  their first name; "Hello," if Cliniko has neither), then "Your appointment with Dana has been moved from Tuesday 12 November at 2:30 pm
  to **Friday 15 November at 10:00 am**." (or "…on *time* has been cancelled."), then
  "This was arranged by phone. If this is not right, please contact *clinic name*."

Each email is a **Patient notice email** cost line on the call.

## Jobs that run on their own {#jobs}

- **Overnight key check.** Every connected key is checked once a night. Businesses,
  practitioners, appointment types and Cliniko's notice are refreshed, and an agent whose
  businesses are no longer online-bookable loses its bookings switch. If Cliniko rejects
  the key, the connection becomes **Key rejected**, bookings are switched off for all the
  client's agents and the clinic gets an alert. A rejected key isn't checked again until
  you replace it.
- **Daily data deletion.** See [below](#retention).

After changing something in Cliniko (a new practitioner, an appointment type shown online,
a new notice), press **Re-verify** to pick it up straight away.

## Data deletion {#retention}

Every day, call data older than [Keep call data for](index.md#retention) (90 days by
default) is deleted for these calls of the client:

- calls with a booking outcome or an audit-log row;
- **every** call of an agent that currently has bookings on, including calls from before
  bookings were switched on.

The transcript, summary, extracted data and recording are deleted. The call itself stays
in the calls list with its booking outcome, so billing and counts are unaffected. This
still runs after Cliniko is disconnected.

## Change the key {#replace-key}

Replace the key when it is rejected, when the Cliniko user leaves, or as a routine change.

1. Create a new key in Cliniko (see [Set up Cliniko bookings](setup.md#cliniko-user)).
2. On the Bookings tab, press **Replace key**, paste the new key and press **Replace**.
   The new key is checked first; settings and agents are kept.
3. If the connection was **Key rejected**, turn the agents' switches back on. A rejected
   key switches them all off.
4. Archive the old key in Cliniko.

## Stop bookings {#stop}

| To stop… | Do this | What's kept |
|---|---|---|
| One agent | Turn its switch off in the **Agents** card. | Everything else. |
| One clinic | **Disconnect** on the connection card, then archive the key in Cliniko. | Nothing: the key and settings are deleted; agents' switches go off. |
| A whole operator | A super-admin turns the operator's **Bookings** switch off (see [Administration](../admin.md#bookings-enabled)). | Everything, ready to turn back on. |

Each takes effect straight away, even on a call in progress.

## Related

- What callers hear → [What happens on a booking call](calls.md)
- Fix a problem → [Bookings troubleshooting](troubleshooting.md)
