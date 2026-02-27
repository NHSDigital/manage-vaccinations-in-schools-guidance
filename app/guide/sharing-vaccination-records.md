---
title: Sharing vaccination records with GPs and NHS England
theme: Recording vaccinations
order: 30
---

All vaccinations recorded in Mavis from Monday 2 March 2026 are automatically shared with NHS England and GP practices. Any vaccinations recorded before this date should be reported manually.

You do not need to inform NHS England and GP practices of any vaccinations, except in cases where:

- the vaccinations were recorded before 2 March 2026
- a child self-consented under Gillick competence and asked for their parents not to be notified (see below)

If a child’s record does not include an NHS number, Mavis cannot automatically send any vaccination recorded for them to their GP practice.

> [!NOTE]
> You still need to send all vaccination records to CHIS. You should let your CHIS provider know that they do not need to send vaccination records to GP practices because Mavis does this automatically.

## Check whether a record has been shared

The child’s vaccination record in Mavis will show a **Synced** label when it was successfully synced with NHS England systems.

![Screenshot of synced vaccination record.](/assets/images/fhir-imms-synced.png)

The record will show a **Sync pending** label if it’s in progress but not yet synced.

If a record cannot be synced, Mavis explains why and in some cases will tell you what action to take.

## If a child self-consents under Gillick competence

If a child self-consents under Gillick competence and asks for their parents not to be informed, the record will not be synced and you must let the child’s GP know they were vaccinated. These records will be flagged to Superusers as an important notice - see [Checking important notices](/guide/notices/).

![Screenshot of a vaccination record that is not synced.](/assets/images/fhir-imms-not-synced.png)

## Sharing records with CHIS

You must share vaccination records for all programmes with CHIS manually.

To do this, download child-level vaccination reports as CSV files from the **Reports** area of Mavis and send them to your CHIS provider. For more information, read [Downloading vaccination reports](/guide/reporting/).
