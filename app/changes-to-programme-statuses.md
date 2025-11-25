---
layout: status-changes
date: 2025-11-28
title: Programme statuses in Mavis
changes:
  - caption: Child is eligible for vaccination
    statuses:
      - description: No consent response
        old:
          text: No outcome
        new:
          text: Eligible
          hint: No response
          colour: white
        now:
          text: Needs consent
          hint: No response
          colour: blue
      - description: Answers to health questions need triage
        now:
          text: Needs triage
          colour: blue
      - description: Conflicting consent responses
        old:
          text: No outcome
        new:
          text: Eligible
          hint: Conflicting consent
          colour: white
        now:
          text: Has a refusal
          hint: Conflicting consent
          colour: dark-orange
      - description: Parent refused consent
        old:
          text: Could not vaccinate
          hint: Refused vaccine
          colour: red
        new:
          text: Eligible
          hint: Consent refused
          colour: white
        now:
          text: Has a refusal
          hint: Parent refused
          colour: dark-orange
      - description: Child triaged as ‘delay vaccination’
        old:
          text: No outcome
        new:
          text: Eligible
          hint: Delay vaccination
          colour: white
        now:
          text: Unable to vaccinate
          hint: Delay vaccination
          colour: red
      - description: Child triaged as ‘do not vaccinate’
        old:
          text: Could not vaccinate
          hint: Contraindicated
          colour: red
        new:
          text: Eligible
          hint: Contraindicated
          colour: white
        now:
          text: Unable to vaccinate
          hint: Contraindicated on [date]
          colour: red
  - caption: Child is eligible for vaccination, consent has been given and triage completed
    statuses:
      - description: No session outcomes recorded yet
        old:
          text: No outcome
        new:
          text: Due vaccination
          hint: Consent given
          colour: aqua-green
        now:
          text: Due vaccination
          hint: "[Vaccine type]"
          colour: green
      - description: Child refused vaccine in their last session
        old:
          text: No outcome
          hint: Refused vaccine
        new:
          text: Due vaccination
          hint: Child refused on [date]
          colour: aqua-green
        now:
          text: Unable to vaccinate
          hint: Child refused on [date]
          colour: red
      - description: Child was absent in their last session
        old:
          text: No outcome
          hint: Absent
        new:
          text: Due vaccination
          hint: Child absent on [date]
          colour: aqua-green
        now:
          text: Unable to vaccinate
          hint: Child absent on [date]
          colour: red
      - description: Child was unwell in their last session
        old:
          text: No outcome
          hint: Unwell
        new:
          text: Due vaccination
          hint: Child unwell on [date]
          colour: aqua-green
        now:
          text: Unable to vaccinate
          hint: Child unwell on [date]
          colour: red
      - description: Child contraindicated in their last session
        old:
          text: No outcome
          hint: Contraindicated
        new:
          text: Due vaccination
          hint: Child contraindicated on [date]
          colour: aqua-green
        now:
          text: Unable to vaccinate
          hint: Contraindicated on [date]
          colour: red
  - caption: Child is fully vaccinated
    statuses:
      - description: Vaccinated
        old:
          text: Vaccinated
          colour: green
        new:
          text: Vaccinated
          hint: Vaccinated on [date]
          colour: green
        now:
          text: Vaccinated
          hint: Vaccinated on [date]
          colour: white
      - description: Already vaccinated
        old:
          text: Vaccinated
          colour: green
        new:
          text: Vaccinated
          hint: Already had the vaccine
          colour: green
        now:
          text: Vaccinated
          hint: Already vaccinated
          colour: white
---

Mavis is still in its ‘private beta’ phase, which means we regularly update it in response to user feedback and testing. These updates help make sure the service meets the needs of our users.

On 3 November 2025, we updated the words used in Mavis to describe children’s programme statuses across all vaccination programmes.

We’ve now made **further updates** to improve clarity and make the statuses easier to use and understand.

The new statuses help you track each child’s journey through the vaccination process and quickly see what action is needed.

## New statuses at a glance

All children who are eligible to be vaccinated at a session now have one of the following **programme statuses**:

- Needs consent
- Has a refusal
- Needs triage
- Due vaccination
- Unable to vaccinate
- Vaccinated

Each status may include **supporting text** that gives more detail about the child’s record or next steps, for example:

- Has a refusal – Conflicting consent
- Unable to vaccinate – Child absent on [date]

### Unable to vaccinate on the day

If a child is marked **Unable to vaccinate** because they were absent, refused the vaccine or were unwell, their status will automatically change back to **Due vaccination** the following day.

### Fewer tabs in sessions

You can now see all programme statuses for all children in a session on the **Children** tab.

The **Consent** and **Triage** tabs have been removed because they are no longer needed.

## Updated statuses

Below you can see what’s changed, with a list of all programme statuses and supporting text used in different scenarios.
