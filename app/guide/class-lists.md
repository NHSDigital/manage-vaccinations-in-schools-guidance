---
title: Importing class lists
group: Organising sessions
order: 8
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

First, you need to reformat the class list provided by the school ready for upload:

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

## Reviewing children who have moved schools

When importing class lists, Mavis will automatically identify if a child’s school has changed and raise this on the School moves page.

To review a child changing school, follow the instructions on this page of the user guide:

* [Reviewing school moves](/guide/school-moves)

## Handling out-of-year-group children

{% include "fragments/out-of-year-group-children.md" %}
