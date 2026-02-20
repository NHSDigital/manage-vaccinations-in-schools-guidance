---
title: Adding and removing users
theme: Managing users
order: 2
---

This section is for the Registration Authority only. If you are a Mavis user, you will be given the appropriate level of access.

Before they can access Mavis for the first time, users need to be given an appropriate role and workgroup. This can be done using the [Care Identity Management](https://manage-care-identities.care-identity-service2.nhs.uk/) service.

## Assigning a role

Users can be given 1 of the following sets of roles:

### Nurse access role (R8001) or health professional access role (R8003)

These roles are for nursing staff who work in primary, secondary care, community care and mental health.

Select either R8001 or R8003 for users according to which roles are already in use in their organisation.

Users with these roles can perform nearly all actions in Mavis. To carry out superuser actions, like viewing important notices or deleting vaccination records, they also need to be assigned additional activities (B0062 and B1611) (see below).

### Medical secretary access role (R8006) or admin/clinical support access role (R8008)

These roles are for staff who support nurses in an administrative role and require access to clinical information.

Select either R8006 or R8008 for users according to which roles are already in use in their organisation.

Users with these roles can perform all actions in Mavis except:

- recording or editing triage
- recording or editing vaccinations (unless they are also assigned the administration activity code (B0428) - see below)
- recording or editing Gillick assessments
- superuser actions (see below)

## Assigning activities

In addition to the roles listed above, the following activities can be assigned to users, enabling them to perform additional tasks in Mavis.

### Personal medication administration (B0428)

This enables healthcare assistants to record vaccinations when giving:

- nasal flu vaccine under a patient group direction (PGD) (they need to record which nurse identified and pre-screened the child, and supplied the vaccine)
- IM flu vaccine under national protocol (they need to record which nurse identified and pre-screened the child, and supplied the vaccine)
- nasal flu vaccine under a patient specific direction (PSD) (when a PSD has been added by a user with the independent prescribing activity code)

### Independent prescribing (B0420)

This enables users with prescribing duties to record PSDs for nasal flu. This activity code can be assigned independently or alongside the nurse role.

### Superuser activities (B0062 and B1611)

Local system administration (B0062) adds ability to delete vaccination records.

Access sensitive (S) flagged records (B1611) adds ability to view important notices about patients who have been flagged in the Personal Demographics Service (PDS).

We recommend that there are at least 2 superusers with activity codes B0062 and B1611 per organisation.

## Assigning users to a workgroup

Each SAIS team using Mavis has a different workgroup name. Users need to be assigned to the appropriate workgroup.

You may need to [add workgroups to your organisation](https://digital.nhs.uk/services/care-identity-service/applications-and-services/care-identity-management/user-guides/managing-workgroups/create-a-workgroup) before assigning individual users.

If you create a new workgroup, you must inform Mavis by emailing <england.mavis@nhs.net>.

## Removing users

When staff leave your organisation or no longer require Mavis access, remove their access promptly through the Care Identity Management service:

- end-date their Mavis role assignments (R8001, R8003, R8006 or R8008)

and/or

- remove the SAIS team-specific workgroup from their CIS2 record

This should be part of your standard leaver process for SAIS staff.
