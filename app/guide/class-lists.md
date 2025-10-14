---
title: Importing class lists
theme: Organising sessions
order: 10
---

[[toc]]

To ensure you have an accurate cohort before a school session, Mavis allows you to import individual school class lists. Mavis will update the cohort list with any contact details provided and automatically identify and movers in and out.

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

1. Go to **Import** in the top navigation.
2. Click on **Import records**.
3. Select **Class list records** and click **Continue**.
4. Search for the school by name and click **Continue.**
5. Select which year groups these records are for.

![Screenshot of choosing year groups for class list imports.](/assets/images/import-class-list-year-groups.png 'Select which year groups your class list import contains.')

Mavis may add a missing NHS number or replace an incorrect one in your upload by searching PDS. (See [See how Mavis uses PDS to find NHS numbers](/guide/importing-cohorts#see-how-mavis-uses-pds-to-find-nhs-numbers))

> [!NOTE]
> If a school does not provide postcodes for every child, you can still upload the class lists. You will have to add any missing NHS numbers manually.

> [!NOTE]
> If less than 70% of records, uploaded with a postcode, match an NHS number in PDS, the upload will be rejected, and you’ll see an error message. You should review the file, correcting any formatting issues (for example, make sure the first name and last name columns and the date of birth rows are in the correct position) and try uploading it again.


## Reviewing children who have moved schools

When importing class lists, Mavis will automatically identify if a child’s school has changed and raise this on the School moves page.

To review a child changing school, follow the instructions on this page of the user guide:

- [Reviewing school moves](/guide/school-moves)

## Handling out-of-year-group children

{% include "fragments/out-of-year-group-children.md" %}
