---
title: Adding and removing users
theme: Managing users
order: 2
---
This section is for the Registration Authority only. If you are a Mavis user, you will be given the appropriate level of access.

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

## Assigning users to a workgroup

Each SAIS team using Mavis has a different workgroup name. Users need to be assigned to the appropriate workgroup. 

You may need to [add workgroups to your organisation](https://digital.nhs.uk/services/care-identity-service/applications-and-services/care-identity-management/user-guides/managing-workgroups/create-a-workgroup) before assigning individual users.

If you create a new workgroup, you must inform Mavis by emailing <england.mavis@nhs.net>.

## Superusers

If users are added to the `mavissuperusers` workgroup, they can:

- view important notices about children
- delete vaccination records

Superusers still need to be assigned to the `schoolagedimmunisations` workgroup and be given a role.

We recommend there are at least 2 superusers per organisation.

## Removing users

When staff leave your organisation or no longer require Mavis access, remove their access promptly through the Care Identity Management service:

- End-date their Mavis role assignments (R8001 or R8006)
- Remove them from the `schoolagedimmunisations` workgroup
- Remove them from the `mavissuperusers` workgroup if applicable

This should be part of your standard leaver process for SAIS staff.
