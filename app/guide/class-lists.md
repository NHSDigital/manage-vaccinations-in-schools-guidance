---
title: Adding class lists
group: Sessions
order: 29
---

To ensure you have an accurate cohort before a school session, Mavis allows you to import individual school class lists. Mavis will update the cohort list with any contact details provided and automatically identify and movers in and out. 

Class lists from each school can be uploaded using the following template:

{% from "attachment/macro.njk" import attachment %}
{{ attachment({
  text: "Class list import template",
  summary: "Microsoft Excel spreadsheet, 17 KB",
  href: "/files/class-list-import-template.xlsx"
}) }}

Class lists for each school are uploaded separately, and each school can only have one class list.

Mavis will identify any children not present in the class list as movers out and prompt you to remove them from the school. This will record their new school as unknown until they appear in another school list.

## Uploading a class list file

First, you need to reformat the class list provided by the school ready for upload:

1. Navigate to the relevant Excel file for the school and open it. If there are multiple tabs in the Excel sheet, the records need to be combined into a single table.
2. If present, remove the helper text row from the table (row 2).
3. Go to **File > Save a copy** and then choose the format **CSV UTF-8 (Comma delimited) (.csv)** and save it.

In Mavis:

1. Go to **Programmes**.
2. Go to **HPV**.
3. Go to the correct school.
4. Select **Import class list**.
5. Choose the .csv version of the class list and select **Continue**. If there are any validation issues, Mavis will not import the file. Correct the issues listed and try again.
6. Wait for the file to finish importing.

## Reviewing children who have moved schools

![Screenshot of page showing children who have moved into a school.](/assets/images/session-moved-in.png 'Mavis shows a list of all the children who appeared in the school list, but weren’t in the cohort for that school before.')

1. Go to **Review children who have changed schools**.
2. Go to the **Moved in** tab.
3. Confirm or ignore the change of school for each child as appropriate.
4. Go to the **Moved out** tab. Mavis shows a list of all the children who were at the school in the cohort list, but weren’t in the class list.
5. Confirm or ignore the change of school for each child as appropriate.
