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

When importing class lists Mavis will automatically identify any changes in a child’s school in relation to their existing record and raise it on the **School moves** page.

![Screenshot of page showing children who have moved school.](/assets/images/school-move-list.png 'Mavis shows a list of all the children who have moved school.')

1. Go to **School moves** in the main navigation.
2. Click **Review** against a school move.
3. Check the information provided: the new school is shown on the left with the updated information highlighted.
4. Confirm or ignore the change of school for each child as appropriate.

![Screenshot of a school move review page.](/assets/images/school-move-review.png 'Mavis will show you the new school and the updated information for each child.')


