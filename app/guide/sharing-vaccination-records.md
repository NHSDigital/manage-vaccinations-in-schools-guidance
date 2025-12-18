---
title: Sharing vaccination records with GPs and NHS England
theme: Recording vaccinations
order: 30
eleventyComputed:
  eleventyNavigation:
    key: Sharing vaccination records
---

When you record a vaccination in Mavis it is automatically sent to NHS England and the child’s GP. You do not need to inform them about these vaccinations (except in some cases of self consent - see below).

You should check with your local CHIS provider how best to tell them about these vaccinations. CHIS providers do not need to send these vaccination records to GPs since this happens automatically through Mavis. For more information, see the [Downloading vaccination reports](/guide/reporting.md) page.

The child’s vaccination record will show a ‘Synced’ label when the vaccination record was successfully synced.

![Screenshot of synced vaccination record.](/assets/images/fhir-imms-synced.png)

The record will show a ‘Sync pending’ label if it is in progress but not yet synced.
If it is not synced or could not be synced, the additional text will explain why, and in some cases it will tell you what actions you must take. For example:

- if the child asked for their parents not to be notified after giving self consent via Gillick competency, you must let the child’s GP know they were vaccinated
- if it cannot be synced because of a missing NHS number, you must add an NHS number to the child's record before this record will sync

![Screenshot of a vaccination record that is not synced.](/assets/images/fhir-imms-not-synced.png)

The information sharing works both ways. Mavis automatically searches vaccination records held by NHS England—including those received from GP practices—for children in your cohort and adds any missing information to the child’s vaccination history. For example, if a child was already vaccinated by their GP, the record will be visible in Mavis so you can avoid double-vaccinating them.

Note that, for now, only vaccinations recorded since the start of September 2025 will be searched for and added to the child’s vaccination history.

> [!NOTE]
> Mavis can only receive this data for children with NHS numbers. If there are any children without NHS numbers in your session, you need to check if they have already been vaccinated.
