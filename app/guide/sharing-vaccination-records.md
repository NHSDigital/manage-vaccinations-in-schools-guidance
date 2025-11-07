---
title: Sharing vaccination records with GPs and NHS England
theme: Recording vaccinations
order: 29
eleventyComputed:
  eleventyNavigation:
    key: Sharing vaccination records
---

When you record a vaccination for flu or HPV in Mavis it is automatically synced with immunisation records held by NHS England and the child’s GP. You do not need to inform them about these vaccinations (except in some cases of self consent - see below). You should also inform your CHIS provider that they do not need to send these records to GPs.

The child’s vaccination record will show a ‘Synced’ label when the vaccination record was successfully synced.

![Screenshot of synced vaccination record.](/assets/images/fhir-imms-synced.png)

The record will show a ‘Sync pending’ label if it is in progress but not yet synced.
If it is not synced or could not be synced, the additional text will explain why, and in some cases it will tell you what actions you must take. For example:

- if the child asked for their parents not to be notified after giving self consent via Gillick competency, you must let the child’s GP know they were vaccinated
- if it cannot be synced because of a missing NHS number, you must add an NHS number to the child's record before this record will sync

![Screenshot of a vaccination record that is not synced.](/assets/images/fhir-imms-not-synced.png)
