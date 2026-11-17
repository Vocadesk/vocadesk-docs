---
title: Set up Cliniko bookings
summary: Step-by-step setup of Cliniko bookings for a clinic, from preparing Cliniko and creating the API key to testing an agent and going live.
tags:
  - bookings
  - integrations
  - agents
keywords:
  - cliniko
  - setup
  - api key
  - online bookings
  - test patient
  - go live
  - checklist
---

# Set up Cliniko bookings

This guide takes one clinic from nothing to live phone bookings. Plan for about an hour,
most of it in Cliniko. You need:

- a super-admin to switch **Bookings** on for your operator (step 1);
- someone who can change the clinic's **Cliniko settings** and add a Cliniko user;
- an **operator admin** login on callcat.ai for the clinic's [client](../clients.md);
- a **scenario-mode, English** [agent](../agents/index.md) for that client.

Before you start, agree with the clinic in writing how their patient data is handled: the
verification you will use, how long call data is kept, and who gets alert emails. The
warnings on the [settings](index.md#settings) are the points to record in their data
protection impact assessment.

## 1. Switch bookings on for the operator {#operator}

A super-admin opens **Super Admin → All Operators** and turns on the **Bookings** switch
in the operator's row (see [Administration](../admin.md#bookings-enabled)). The
**Bookings** tab then appears on every client of that operator.

## 2. Prepare Cliniko {#prepare-cliniko}

Phone offers follow the clinic's **online-booking** setup in Cliniko. Anything that isn't
online-bookable can be cancelled by phone but not moved. Check these in Cliniko (the
names below are Cliniko's; see [Cliniko's help](https://help.cliniko.com) if a menu has
moved):

1. **Online bookings are on.** If online booking is off for the whole account, no
   appointment can be moved by phone.
2. **Each business is shown in online bookings.**
3. **Each practitioner** who should be bookable by phone is shown in online bookings
   (**Settings → Users & practitioners**, edit the practitioner) and offers the right
   appointment types at that business.
4. **Each appointment type** that can be moved by phone has **Show in online bookings**
   ticked.
5. **Minimum notice for cancellations** (**Settings → General settings → Cancellations**)
   is set, or you plan to set custom hours on our side (step 5). Inside this window the
   agent never changes an appointment; it takes a message.
6. The online-booking **lead time** and **how far in advance** patients may book are what
   you want. The agent only offers times inside these limits, and never more than four
   weeks ahead.
7. **Patients have what the agent checks.** With the default verification the agent asks
   for the **date of birth** and matches the **caller ID** against the patient's phone
   numbers. Patients with no date of birth or no phone number in Cliniko can't be
   verified that way (see [step 5](#settings)).

!!! tip "Appointments longer than their type"
    An appointment that was stretched beyond its appointment type's length can only be
    cancelled by phone, not moved, so the agent never shortens or overbooks a slot.

## 3. Create a dedicated Cliniko user and API key {#cliniko-user}

The API key can do everything the Cliniko user who created it can do, so create a user
just for callcat.ai instead of using a manager's own login.

1. In Cliniko, add a new user for callcat.ai, for example **callcat.ai phone agent**.
   Give it the **narrowest role that can view patients and manage appointments**. Start
   with **Receptionist**. Avoid **Administrator**, **Bookkeeper** and **Power
   receptionist**: the panel accepts them but warns that the role is broad.
2. Sign in to Cliniko as that user. Open **My info** (under the user's name), set
   **Allow yourself to create and use API keys** to **Yes** and press **Update user**.
3. Under **API keys**, click **Manage API keys → Add an API key**, name it
   **callcat.ai**, and click **Create API key**.
4. **Copy the key now.** Cliniko shows it only once. Keep it somewhere safe until step 4
   and don't paste it into email or chat.

Cliniko's own guide: [Generate a Cliniko API key](https://help.cliniko.com/en/articles/1023957-generate-a-cliniko-api-key).

## 4. Connect Cliniko {#connect}

1. In callcat.ai, open **Clients**, choose the clinic's client, and open the **Bookings**
   tab.
2. In **Cliniko connection**, paste the key into **Cliniko API key** and press
   **Connect**. The key is checked against Cliniko first ("Checking the key…").
3. On success you see **Connected to Cliniko.**, the key's last 4 characters, the key
   owner and their role. The **Businesses**, **Settings** and **Agents** cards appear.

If connecting fails, the message says why:

| Message | What to do |
|---|---|
| This doesn't look like a Cliniko API key. | Copy the key again in full from Cliniko. |
| Cliniko rejected this key. Check it is active and copied in full. | The key was archived or mistyped. Create a new one. |
| This Cliniko user's role is too narrow | Give the Cliniko user a broader role, or create the key from another user. |
| Cliniko couldn't be reached. Try again in a moment. | A temporary problem. Try again. |
| Cliniko is rate limiting this key. Try again in a minute. | Other software is using the same Cliniko user heavily. Wait a minute. |

Then check the **Businesses and what can be changed by phone** card:

- every business that should take phone changes shows **Online-bookable**;
- the practitioner and appointment type list is what the clinic expects;
- each business has a timezone (a business marked **Timezone unknown** is blocked);
- **Notes from the last check** has nothing unexpected.

If something is missing, fix it in Cliniko (step 2) and press **Re-verify** on the
connection card.

## 5. Choose the settings {#settings}

Go through the **Settings** card with the clinic. The defaults suit most clinics; each
option is explained in the [settings reference](index.md#settings).

| Setting | Default | When to change it |
|---|---|---|
| How callers are verified | Date of birth | Choose a stricter option if the clinic wants more than caller ID plus date of birth, or **Full name** if many patients have no date of birth in Cliniko. |
| Callers with no caller ID | Surname and date of birth | Choose **Don't book: take a message** if the clinic doesn't want web-widget or withheld-number callers to change appointments. |
| Details match, but the number isn't on file | Take a message | Choose the full-name option if many patients call from numbers Cliniko doesn't have. Callers then learn their details matched. |
| After a change | Carry on with the intake questions | Choose **Close with a booking line** if a booking call should end once the change is made. |
| Email to the patient | No email | Choose **Send an email** only if Cliniko doesn't already email patients about changes. |
| Cancellation notice | Use Cliniko's rule | Choose **Custom hours** if Cliniko's notice is unset or 0 (required then), or if phone changes need a different window. |
| Keep call data for | 90 days | Match the clinic's agreement. |
| No-caller-ID daily cap | 10 | Lower it to be stricter; 0 stops bookings on calls without a caller ID. |

Press **Save**.

## 6. Switch bookings on for the agent {#agent}

1. In the **Agents** card, find the agent. It must be **enabled**, in **scenario mode**
   and **English**.
2. Under **Businesses**, tick the business or businesses this agent answers for. They
   must all be online-bookable and share one timezone.
3. Turn the agent's switch on. If it's refused, the reason shows under the agent (see
   [Bookings troubleshooting](troubleshooting.md#agent-switch)).

Nothing else changes in the agent's set-up. Bookings sit alongside its intake questions
and triggers: a caller who asks about an existing appointment is taken into the booking
steps, then the call carries on.

## 7. Test before going live {#test}

Test with a **test patient**, never a real one.

1. In Cliniko, create a test patient with a date of birth and **your own mobile number**,
   and book them two appointments a few days out: one with an online-bookable
   practitioner and type, and one you can cancel. Keep them outside the cancellation
   notice window.
2. **Phone test.** Call the agent's number from that mobile. Ask to move the first
   appointment, give the date of birth, pick an offered time and say yes. Check in
   Cliniko that it moved. Call again and cancel the second one.
3. **Wrong details.** Call again and give a wrong date of birth twice. The agent should
   say it can't confirm and take a message, without saying what was wrong.
4. **No caller ID.** Place a [browser test call](../agents/testing.md#placing-a-test-call).
   It has no caller ID, so the agent asks for the details in **Callers with no caller
   ID** (surname and date of birth by default).
5. Open the **Audit log** on the Bookings tab and the calls in [Calls](../calls.md). Check
   each step is there, the transcript shows **[date of birth]** instead of the date, and
   the summary email has an **Appointment** section.

[What happens on a booking call](calls.md) describes each step, so you can tell expected
behaviour from a problem.

## 8. Go live {#go-live}

Before you point real callers at the agent, check:

- [ ] The clinic has agreed the verification, data retention and alert recipients in
      writing.
- [ ] Alert emails reach someone who reads them. They go to the addresses in
      **Call Summary Recipients** on the client's **Info** tab, or to its **Contact
      Email** if that list is empty.
- [ ] The test patient and its appointments are archived in Cliniko.
- [ ] Someone checks the **Audit log** and the first week's booking calls (see
      [Running bookings day to day](running.md#first-week)).
- [ ] Bookings is switched on only for the agents that should have it.

## Related

- Every setting explained → [Appointment bookings](index.md)
- What callers hear → [What happens on a booking call](calls.md)
