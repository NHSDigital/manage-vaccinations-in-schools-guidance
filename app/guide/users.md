---
title: Managing users
group: Setup
order: 2
---

Before accessing Mavis for the first time, users need to be given an appropriate role and workgroup. This can be done using the [Care Identity Management](https://manage-care-identities.care-identity-service2.nhs.uk/) service.

## Assigning a role

Users should be given one of the following 2 roles:

- ### Nurse Access Role (R8001)

  This role is for nursing staff who work in primary, secondary care, community care and mental health.

  Users with this role can perform nearly all actions in Mavis. To carry out superuser actions, like viewing important notices or deleting vaccination records, they also need to be added to the superuser workgroup (see below).

- ### Medical Secretary Access Role (R8006)

  This role is for staff who support nurses in an administrative role and require access to clinical information.

  Users with this role can perform all actions in Mavis except:

  - recording or editing triage
  - recording or editing vaccinations
  - recording or editing Gillick assessments
  - superuser actions (see below)

## Assigning the workgroup

Users need to be assigned to the `schoolagedimmunisations` workgroup. [Add this workgroup to your organisation](https://digital.nhs.uk/services/care-identity-service/applications-and-services/care-identity-management/user-guides/managing-workgroups/create-a-workgroup) before assigning it to individual users.

## Superusers

If users are added to the `mavissuperusers` workgroup, they can:

- view important notices about patients
- delete vaccination records

Superusers still need to be assigned to the `schoolagedimmunisations` workgroup and be given a role.
