---
layout: post
date: 2025-11-03
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
      - description: Conflicting consent responses
        old:
          text: No outcome
        new:
          text: Eligible
          hint: Conflicting consent
          colour: white
      - description: Parent refused consent
        old:
          text: Could not vaccinate
          hint: Refused vaccine
          colour: red
        new:
          text: Eligible
          hint: Consent refused
          colour: white
      - description: Child triaged as ‘delay vaccination’
        old:
          text: No outcome
        new:
          text: Eligible
          hint: Delay vaccination
          colour: white
      - description: Child triaged as ‘do not vaccinate’
        old:
          text: Could not vaccinate
          hint: Contraindicated
          colour: red
        new:
          text: Eligible
          hint: Contraindicated
          colour: white
  - caption: Child is eligible for vaccination and consent has been given
    statuses:
      - description: No session outcomes recorded yet
        old:
          text: No outcome
        new:
          text: Due vaccination
          hint: Consent given
          colour: aqua-green
      - description: Child refused vaccine in their last session
        old:
          text: No outcome
          hint: Refused vaccine
        new:
          text: Due vaccination
          hint: Child refused on [date]
          colour: aqua-green
      - description: Child was absent in their last session
        old:
          text: No outcome
          hint: Absent
        new:
          text: Due vaccination
          hint: Child absent on [date]
          colour: aqua-green
      - description: Child was unwell in their last session
        old:
          text: No outcome
          hint: Unwell
        new:
          text: Due vaccination
          hint: Child unwell on [date]
          colour: aqua-green
      - description: Child contraindicated in their last session
        old:
          text: No outcome
          hint: Contraindicated
        new:
          text: Due vaccination
          hint: Child contraindicated on [date]
          colour: aqua-green
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
      - description: Already vaccinated
        old:
          text: Vaccinated
          colour: green
        new:
          text: Vaccinated
          hint: Already had the vaccine
          colour: green
---

We’ve updated some of the words we use in Mavis to describe children’s statuses across all vaccination programmes.

We’ve done this to make it clearer what each child’s current status is.

We no longer use the statuses **No outcome** and **Could not vaccinate**.

All children in a session now have one of the following 3 statuses:

- **Eligible**
- **Due vaccination**
- **Vaccinated**

Each status comes with **supporting text** that gives more detail, for example:

- Eligible – conflicting consent
- Due vaccination – consent given

## Updated statuses

Below you can see what’s changed, with a list of all programme statuses and supporting text used in different scenarios.

{% from "status-changes/macro.njk" import statusChanges %}
{% for change in changes %}
{{ statusChanges(change) }}
{% endfor %}
