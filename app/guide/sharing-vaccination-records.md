---
title: Sharing vaccination records with GPs and NHS England
theme: Recording vaccinations
order: 30
---

The table below shows which vaccination records Mavis shares automatically
and which ones you need to share manually for each vaccination programme.

| Vaccination programme | Shared with GPs by Mavis? | Shared with NHS England by Mavis? | Shared with CHIS by Mavis? |     What you need to do     |
|:---------------------:|:-------------------------:|:---------------------------------:|:--------------------------:|:---------------------------:|
| Flu                   | Yes*                      | Yes                               | No                         | Send record to CHIS         |
| HPV                   | Yes*                      | Yes                               | No                         | Send record to CHIS         |
| MenACWY               | No                        | Not required                      | No                         | Send record to GPs and CHIS |
| Td/IPV                | No                        | Not required                      | No                         | Send record to GPs and CHIS |
| MMR(V)                | No                        | Not required                      | No                         | Send record to GPs and CHIS |

**\* Applies only if the child’s record includes an NHS number.**

Exceptions apply if a child has self-consented under Gillick competence and asked for their parents not to be notified. See below.

## Sharing records with NHS England and GPs

### MenACWY, Td/IPV and MMR(V)

Mavis does not automatically share records for:

* MenACWY
* Td/IPV
* MMR or MMRV

You must share these records manually.

To do this, download a child-level vaccination report from the **Reports** area of Mavis and send it to the child’s GP practice. For more information, read [Downloading vaccination reports](/guide/reporting/).

### Flu and HPV

Flu and HPV vaccinations recorded in Mavis are automatically synced with NHS England systems and the child’s GP practice.

You do not need to inform them about these vaccinations, except in some cases of self-consent - see below.

> [!NOTE]
> You should let your CHIS provider know that they do not need to send flu and HPV vaccination records to GP practices because Mavis does this automatically.

#### Check whether a record has been shared

The child’s vaccination record in Mavis will show a **Synced** label when it was successfully synced with NHS England systems.

![Screenshot of synced vaccination record.](/assets/images/fhir-imms-synced.png)

The record will show a **Sync pending** label if it’s in progress but not yet synced.

If a record cannot be synced, Mavis explains why and in some cases will tell you what action to take.

### If a child self-consents under Gillick competence

If a child self-consents under Gillick competence and asks for their parents not to be informed, the record will not be synced and you must let the child’s GP know they were vaccinated. These records will be flagged to Superusers as an important notice - see [Checking important notices](/guide/notices/).

![Screenshot of a vaccination record that is not synced.](/assets/images/fhir-imms-not-synced.png)

## Sharing records with CHIS

You must share vaccination records for all programmes with CHIS manually.

To do this, download child-level vaccination reports as CSV files from the **Reports** area of Mavis and send them to your CHIS provider. For more information, read [Downloading vaccination reports](/guide/reporting/).
