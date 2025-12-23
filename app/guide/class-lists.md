---
title: Importing class lists
theme: Organising sessions
order: 10
---

[[toc]]

To ensure you have an accurate cohort before a school session, Mavis allows you to import individual school class lists. Mavis will update the cohort list with any contact details provided and automatically identify any movers in and out.

Class lists from each school can be uploaded using the following template:

{% from "attachment/macro.njk" import attachment %}
{{ attachment({
  text: "Class list import template",
  summary: "Microsoft Excel spreadsheet, 17 KB",
  href: "/files/class-list-import-template.xlsx"
}) }}

Class lists for each school are uploaded separately, and each school can only have one class list.

## Uploading a class list file

If the school did not provide the list in CSV format, you need to reformat it ready for upload:

1. Navigate to the relevant Excel file for the school and open it. If there are multiple tabs in the Excel sheet, the records need to be combined into a single table.
2. If present, remove the helper text row from the table (row 2).
3. Go to **File > Save a copy** and then choose the format **CSV UTF-8 (Comma delimited) (.csv)** and save it.

In Mavis:

1. Go to **Imports** in the top navigation.
2. Select **Upload records**.
3. Select **Class list records** then **Continue**.
4. Search for the school by name and select **Continue**.
5. Select which year groups these records are for.
6. Select **Choose File**, then select the CSV file you want to import.
7. Select **Continue**. If there are any validation issues, Mavis will not import the file. Correct the issues listed in the file and try again.
8. Wait for the file to finish uploading.

Mavis may add a missing NHS number or replace an incorrect one in your upload by searching PDS. (See [See how Mavis uses PDS to find NHS numbers](/guide/importing-cohorts#see-how-mavis-uses-pds-to-find-nhs-numbers))

> [!NOTE]
> If a school does not provide postcodes for every child, you can still upload the class lists. You will have to add any missing NHS numbers manually.

## Reviewing and approving uploads

![Screenshot of review screen for class import.](/assets/images/review-class-import.png)

When you upload class lists, Mavis will identify children it already has records for.

If it’s an exact duplicate, Mavis will simply not import the record again - you’ll see a notification telling you how many records were not imported because they already exist in Mavis.

If the file upload includes additional information for the child, such as their gender or preferred name, this will be added to the existing record if you approve the upload.

If Mavis identifies any near matches with existing child records, you will need to review the missing or conflicting details after approving the upload, and confirm which record to keep and which record to archive.

Click **Approve and import records**

You’ll need to review close matches and school moves after importing.

1. Click **Review** for each record listed.
2. For close matches, select which version of the record you want to keep and select **Resolve duplicate**.

There is also an option to keep both child records. For example, in the case of twins, Mavis will identify a near match, but you can select **Keep both records**. The existing record will stay in Mavis and the uploaded record will be added.

If there are some parts of each record that are correct, you can:

1. note down any correct information from the version you choose to archive
2. archive that record
3. go to the record you are keeping and edit the information there

> [!NOTE]
> If less than 70% of records, uploaded with a postcode, match an NHS number in PDS, the upload will be rejected, and you’ll see an error message. You should review the file, correcting any formatting issues (for example, make sure the first name and last name columns and the date of birth rows are in the correct position) and try uploading it again.

> [!NOTE]
>Some records may have changed since you uploaded your file. For example, another import might have been approved that includes some of the records in your file, or a child's school or NHS number may have changed in Mavis. If this happens, you’ll need to review those records again and confirm you still want to import the remaining changes from your file.

## Reviewing children who have moved schools

When importing class lists, Mavis will automatically identify if a child’s school has changed and raise this on the School moves page.

To review a child changing school, follow the instructions on this page of the user guide:

- [Reviewing school moves](/guide/school-moves)

## Handling out-of-year-group children

{% include "fragments/out-of-year-group-children.md" %}
