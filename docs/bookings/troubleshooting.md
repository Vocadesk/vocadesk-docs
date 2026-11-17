---
title: Bookings troubleshooting
summary: Fixes for common Cliniko bookings problems, such as a key that won't connect, an agent switch that is refused, callers who can't be verified and appointments that can't be moved.
tags:
  - bookings
  - troubleshooting
keywords:
  - cliniko
  - not working
  - key rejected
  - role too narrow
  - can't verify
  - no free times
  - faq
---

# Bookings troubleshooting

If something here doesn't solve it, note the call (its **View call** link in the audit
log) and contact support.

## Connecting {#connecting}

??? question "I can't see the Bookings tab"
    The tab is for operator admins and super-admins, and an operator admin only sees it
    after a super-admin has switched **Bookings** on for the operator
    ([Administration](../admin.md#bookings-enabled)). Regular users never see it.

??? question "\"This doesn't look like a Cliniko API key\" or \"Cliniko rejected this key\""
    Copy the key again in full; Cliniko shows it only once, so if you no longer have it,
    create a new one. Check the key hasn't been archived in Cliniko, and that the user who
    created it still has **Allow yourself to create and use API keys** set to **Yes**.

??? question "\"This Cliniko user's role is too narrow\""
    Cliniko refused a request the connection needs, such as reading patients,
    practitioners or appointments. Give the Cliniko user a role that can view patients and
    manage appointments, then press **Re-verify** (or **Replace key** with a key from a
    user who has that role).

??? question "The card warns the key belongs to a user with a broad role"
    The key owner is an Administrator, Bookkeeper or Power receptionist. It works, but a
    leaked key could do everything that user can. Create a dedicated user with a narrower
    role and use **Replace key** ([Set up Cliniko bookings](setup.md#cliniko-user)).

??? question "A business shows \"Not online-bookable\" or is missing practitioners"
    Phone offers follow Cliniko's online-booking setup. Make sure online bookings are on,
    and that the business, the practitioner and the appointment type are each shown in
    online bookings, with the practitioner offering that type at that business. Then press
    **Re-verify**. See [Prepare Cliniko](setup.md#prepare-cliniko).

??? question "\"Timezone unknown: bookings are blocked for this business\""
    Cliniko didn't give a timezone for the business or the key owner. Set the timezone in
    Cliniko, then press **Re-verify**.

## Switching agents on {#agent-switch}

??? question "The agent's switch is greyed out"
    The agent must be **enabled**, in **scenario mode** and **English**; the note under the
    agent says which. The switch is also greyed out while the connection isn't
    **Connected** (for example **Key rejected**) or the operator's Bookings switch is off.

??? question "\"Cliniko's cancellation notice is unset or 0\""
    Cliniko has no minimum notice for cancellations. Either set one in Cliniko and press
    **Re-verify**, or choose **Custom hours** under
    [Cancellation notice](index.md#cancellation-notice) and save.

??? question "\"The chosen businesses must share one timezone\""
    One agent can only act for businesses in the same timezone. Use a separate agent for
    the other businesses.

??? question "An agent's bookings switch turned itself off"
    Either Cliniko rejected the key (the connection shows **Key rejected**; see
    [Change the key](running.md#replace-key)), or the overnight check found the agent's
    businesses are no longer online-bookable. Fix the business in Cliniko, press
    **Re-verify**, and switch the agent back on.

## On calls {#calls}

??? question "The agent didn't offer to change the appointment"
    Check the agent's bookings switch is on and Cliniko is **Connected**. The booking steps
    start when the caller asks about an appointment they **already have**; a new booking,
    a different practitioner or a different appointment type becomes a message.

??? question "A real patient couldn't be verified"
    Open the call's rows in the audit log. Common causes:

    - the date of birth in Cliniko is missing or different;
    - the patient called from a number not on their Cliniko record (with the default
      [unknown-number setting](index.md#unknown-number) the agent takes a message);
    - the name in Cliniko is spelled differently (names must match exactly, apart from
      capitals, accents and punctuation);
    - another patient has the same details and number, so the agent can't tell them apart;
    - a daily limit was reached (see [the limits](calls.md#verify)).

??? question "The agent says it can't move an appointment, only cancel it"
    The appointment's practitioner or appointment type isn't online-bookable, or the
    appointment is longer than its appointment type. The agent takes a message for the
    clinic to move it.

??? question "The agent won't change an appointment that is soon"
    It is inside the [cancellation notice](index.md#cancellation-notice) window, which
    covers moves as well as cancellations. The agent takes a message.

??? question "The agent finds no free times, but the diary has gaps"
    The agent only offers times that online booking would offer: the same practitioner
    and appointment type, inside Cliniko's lead time and booking window, and at most four
    weeks ahead. Gaps shorter than the appointment type, or outside the practitioner's
    online availability, aren't offered.

??? question "The caller was told the clinic will confirm the change"
    Cliniko didn't confirm the change in time. The clinic got an alert email
    ("A booking change could not be confirmed"). Check the appointment in Cliniko and
    call the patient.

??? question "The transcript shows [date of birth]"
    That's by design: dates of birth are removed from transcripts. The recording still has
    it until [data deletion](running.md#retention).

??? question "Some of an agent's older calls lost their transcripts and recordings"
    Once an agent has bookings on, **all** its calls older than
    [Keep call data for](index.md#retention) are cleared each day, including calls from
    before bookings were switched on. See [Data deletion](running.md#retention).

## Related

- Set up from the start → [Set up Cliniko bookings](setup.md)
- General problems → [Troubleshooting](../troubleshooting.md)
