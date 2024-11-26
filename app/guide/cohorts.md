---
title: Managing the cohort
group: Programmes
order: 11
eleventyComputed:
  eleventyNavigation:
    key: Managing cohorts
---

[[toc]]

## Creating the initial cohort list (year 8 to 11)

{% from "inset-text/macro.njk" import insetText %}
{{ insetText({
  html: "You should upload cohort records before you upload vaccination records or class lists."
}) }}

Cohort records can be uploaded using the following template:

{% from "attachment/macro.njk" import attachment %}
{{ attachment({
  text: "Cohort import template",
  summary: "Microsoft Excel spreadsheet, 18 KB",
  href: "/files/cohort-import-template.xlsx"
}) }}

You should include all the year 8, 9, 10 and 11 children in your area, whether they have already been vaccinated or not.

Make sure the cohort records are in the format shown in the template above. Files need to be in .csv format. Records can be all in one file, or split across multiple files; Mavis is not picky about this. If you have an excel file with multiple tabs, you will need to consolidate this into a single tab or create a separate CSV file for each tab.

1. Go to **Programmes**.
2. Go to **HPV**.
3. Go to the **Cohorts** tab.

![Screenshot of programme cohorts tab.](/assets/images/programme-cohorts.png 'Mavis shows the number of children within each programme cohort.')

For each of your cohort CSV files:

1. Select **Import child records**.
2. Select **Choose File**.
3. Open the file and select **Continue**. If there are any validation issues, Mavis will not import the file. Correct the issues listed in the file and try again.
4. Wait for the file to finish importing.

### Resolving issues importing a cohort list

Mavis will highlight any potential duplicates found with discrepancies between what was uploaded and what was already in Mavis.

Go to the **Import issues** tab. For each record:

1. Select **Review**.
2. Select which version of the record you want to keep and select resolve duplicate.

If there are some parts of each that are correct, you can note down any correct information from the version you choose to discard, discard it, then go to the child record and manually edit the information there (this feature will be more developed in a future release of Mavis).

Once you have uploaded all the cohort files, you can go to the **Cohorts** tab and check the counts for each year group are as expected.

## Importing historic vaccination records (year 9, 10 and 11)

When you’re uploading vaccination records, use the same template you’d use for NIVS. You should upload all vaccination records from the last 3 years.

You should also include vaccination records for anyone in the current cohort who was vaccinated elsewhere, if you have them. These records will be stored in Mavis and won’t be sent anywhere else.

Vaccination record files need to be in .csv format. Records can be all in one file, or split across multiple files; Mavis is not picky about this. If you have an excel file with multiple tabs, you will need to consolidate this into a single tab or create a separate CSV file for each tab.

1. Go to **Programmes**.
2. Select the programme you want.
3. Go to the **Vaccinations** tab.

![Screenshot of programme vaccinations tab.](/assets/images/programme-vaccinations.png 'Mavis shows a record of all vaccinations for a given programme.')

For each of your vaccination record CSV files:

1. Select **Import vaccination records**.
2. Select **Choose File**.
3. Open the file and select **Continue**. If there are any validation issues, Mavis will not import the file.
4. Correct the issues listed and try again.
5. Wait for the file to finish importing.

### Resolving issues importing historic vaccination records

Mavis will highlight any potential duplicates found between what was uploaded and what was already in Mavis.

Go to the **Import issues** tab. For each record:

1. Select **Review**.
2. Select which version of the record you want to keep and select resolve duplicate.

If there are some parts of each that are correct, you can note down any correct information from the version you choose to discard, discard it, then go to the child’s record and manually edit the information there (this feature will be more developed in a future release of Mavis).

## Uploading class lists

Class lists can be uploaded using the following template:

{{ attachment({
  text: "Class list import template",
  summary: "Microsoft Excel spreadsheet, 17 KB",
  href: "/files/class-list-import-template.xlsx"
}) }}

Class lists for each school are uploaded separately, and each school can only have one class list.

The class list must contain the entire cohort for that school, otherwise any children not listed will be removed from the school on Mavis (and recorded as school unknown).

First, you need to reformat the class list provided by the school ready for upload:

1. Navigate to the relevant Excel file for the school and open it. If there are multiple tabs in the Excel sheet, the records need to be combined into a single table.
2. Remove the helper text row from the table (row 2).
3. Go to **File > Save a copy** and then choose the format **CSV UTF-8 (Comma delimited) (.csv)** and save it.

In Mavis:

1. Go to **Programmes**.
2. Go to **HPV**.
3. Go to the correct school.
4. Select **Import class list**.
5. Choose the .csv version of the class list and select **Continue**. If there are any validation issues, Mavis will not import the file. Correct the issues listed and try again.
6. Wait for the file to finish importing.

### Reviewing children who have moved schools

![Screenshot of page showing children who have moved into a school.](/assets/images/session-moved-in.png 'Mavis shows a list of all the children who appeared in the school list, but weren’t in the cohort for that school before.')

1. Go to **Review children who have changed schools**.
2. Go to the **Moved in** tab.
3. Confirm or ignore the change of school for each child as appropriate.
4. Go to the **Moved out** tab. Mavis shows a list of all the children who were at the school in the cohort list, but weren’t in the class list.
5. Confirm or ignore the change of school for each child as appropriate.

## Manually editing individual child records

1. Go to **Children**.
2. Search for the child by name and select their record.
3. Select **Edit child record**.
4. Find the information you want to edit and select **Change**.
5. Edit the information and select **Continue**.
6. Select **Save changes**.
