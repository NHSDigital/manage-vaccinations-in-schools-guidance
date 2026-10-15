---
title: How Mavis handles parent contacts
theme: Managing cohorts
order: 12
eleventyComputed:
  eleventyNavigation:
    key: Parent contacts
---

[[toc]]

Mavis stores parent contact details for each child. These details are used to contact parents about vaccinations.

## How parent contacts are added

Parent contact details can be added to Mavis when:

- you upload a class list or child records
- a parent submits a consent response or clinic booking form that's matched to a child
- you add a contact manually to a child's record

## How parent contacts are updated

When you upload a class list or child records, Mavis uses the new parent contact details to replace existing contacts for the child. The existing contacts are archived. 

The way this works depends on the type of records you’re uploading. 

- **Class list uploads**: Mavis replaces all existing parent contacts, even if the new class list does not include any parent contact details for the child. This can leave a child with no parent contacts.
- **Child record uploads**: Mavis only replaces existing parent contacts if the upload includes at least one parent contact for the child. If no parent contacts are included, the child's existing contacts are kept.

This applies to all existing parent contacts, including those added manually or through consent responses.

Parent contacts added after an upload, including through consent responses or clinic bookings, are kept on the child’s record (unless a later upload replaces them).

You can also add, edit or remove parent contacts directly in a child's record in Mavis.

## Contacts are stored separately for each child

Mavis stores parent contact details separately for each child.

If a parent is linked to more than one child, updating their details on one child's record will not change their details on the other children's records.

## Which contacts receive communications

Mavis uses current parent contact details to send consent requests.

If a parent contact is archived after submitting a consent response, Mavis can still use the contact details from that response to send messages about the vaccination, such as reminders and vaccination confirmations.

## What happens to existing consent

Archiving a parent contact does not invalidate consent they've already given for a vaccination. The child can still be vaccinated.

## Keeping parent contact details up to date

Work with schools to make sure the contact details they provide are up to date and only include people with parental responsibility or delegated authority to consent to vaccinations.

You can use the [school communication templates](/email-templates-for-sais-and-schools/) to ask schools to check their contact details before sharing them.

For instructions on adding, editing or removing contacts, see [Viewing, editing and archiving child records](/guide/editing-cohorts/).
 
