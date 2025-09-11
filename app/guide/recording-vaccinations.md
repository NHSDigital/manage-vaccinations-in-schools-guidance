---
title: Recording a vaccination (or non-vaccination)
theme: Recording vaccinations
order: 24
eleventyComputed:
  eleventyNavigation:
    key: Recording a vaccination
---

To record a vaccination (or a vaccination that didn’t happen), follow the instructions below.

## Select the child and programme

1. Go to **Sessions**.
2. Filter for **In Progress** sessions.
3. Click on the name of the school you’re attending.
4. Click on **Record vaccinations** under the relevant programme.
5. A list of children’s names is displayed - you can filter the list by name or year group.
6. Click on the name of the child in front of you.

> [!NOTE]
> If you’re offering more than one vaccination programme at this session, make sure you select the relevant programme tab, near the top of the screen.

![Screenshot of programme tabs on the patient session page.](/assets/images/session-programme-tabs.png)

## Review the child’s details and do pre-screening checks

Once you’ve reviewed the information on the page, you’ll need to confirm the child’s identity and carry out pre-screening checks.

1. Select the relevant radio button to state whether the child or someone else confirmed their identity.
2. If it was someone else, enter their name and relationship to the child.
3. Run through the pre-screening checks and confirm you’ve checked the statements are correct. You can add notes if you want to.
4. Indicate whether you think the child is ready to vaccinate using the radio buttons at the bottom of the page.

![Screenshot of pre-screening questions on a patient record.](/assets/images/session-child-pre-screen.png 'Mavis will ask a series of pre-screening questions before you record a vaccination.')

## Record the outcome

If the child was vaccinated:

1. Use the relevant radio buttons to record how the vaccination was given.
2. Record the batch you used, then click **Continue**.
3. Check and confirm your answer, and add notes if you want to.
4. Make any changes (if necessary) and click **Confirm**.

If the child was not vaccinated:

1. Use the relevant radio button to record why the vaccine was not given, then **Continue**.
2. Check and confirm your answer, and add notes if you want to.
3. Make any changes (if necessary) and click **Confirm**.

## Sharing vaccination records with GPs and NHS England

When you record a vaccination for flu or HPV in Mavis it is automatically synced with immunisation records held by NHS England and the child’s GP. You do not need to inform them about these vaccinations (except in some cases of self consent - see below). You should also inform your CHIS provider that they do not need to send these records to GPs.

The child’s vaccination record will show a ‘Synced’ label when the vaccination record was successfully synced.

![Screenshot of synced vaccination record.](/assets/images/fhir-imms-synced.png)

The record will show a ‘Sync pending’ label if it is in progress but not yet synced.
If it is not synced or could not be synced, the additional text will explain why, and in some cases it will tell you what actions you must take. For example:

- if the child asked for their parents not to be notified after giving self consent via Gillick competency, you must let the child’s GP know they were vaccinated
- if it cannot be synced because of a missing NHS number, you must add an NHS number to the child's record before this record will sync

![Screenshot of a vaccination record that is not synced.](/assets/images/fhir-imms-not-synced.png)
