---
title: Managing the cohort
group: Programmes
order: 11
eleventyComputed:
  eleventyNavigation:
    key: Managing cohorts
---

[[toc]]

## Introduction

Mavis can be used in one of two ways:

- with complete age-based cohorts, including those already vaccinated in previous academic years (all year 8 to 11s)
- with unvaccinated cohorts only (all year 8s, and year 9 to 11 catch up lists).

Mavis works better, particularly for reporting and monitoring uptake, when complete, age-based cohorts are imported before the programme begins.

To use Mavis with complete cohorts, as well as importing cohort details, you will also need to upload historic vaccination records for year 9 - 11s vaccinated in previous academic years. If these cannot be imported into Mavis, then you can set up Mavis with records for just the unvaccinated cohorts.

## Setting up complete, age-based cohorts in Mavis

### Creating the initial cohort lists (all year 8 to 11s)

{% from "inset-text/macro.njk" import insetText %}
{{ insetText({
  html: "You should upload cohort records before you upload vaccination records or class lists."
}) }}

You should include all the year 8, 9, 10 and 11 children in your area, whether they have already been vaccinated or not.

To upload cohort records and resolve any issues with the import, follow the instructions on this page:

- [Upload cohort records](/guide/uploading-cohorts/)

Once you have uploaded all the cohort files, you can go to the **Cohorts** tab and check the counts for each year group are as expected.

You can also check individual children’s records by navigating to the **Children** tab. You won’t be able to see the children listed under their school in the sessions tab until you have imported historic vaccination records and scheduled at least one session at that school.

### Importing historic vaccination records (years 9, 10 and 11)

You should upload historic vaccination records before scheduling school sessions, to ensure that only unvaccinated children are added to a session. (But don’t worry, if you identify that someone is already vaccinated at a later date, you can remove them from the session).

When you’re uploading vaccination records, use the same template you’d use for NIVS. You should upload all vaccination records from the last 3 years.

You should also include vaccination records for anyone in the current cohort who was vaccinated elsewhere, if you have them. These records will be stored in Mavis and won’t be sent anywhere else.

Vaccination record files need to be in .csv format. Records can be all in one file, or split across multiple files; Mavis is not picky about this. If you have an Excel file with multiple tabs, you will need to consolidate this into a single tab or create a separate CSV file for each tab.

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

Once the file has finished importing, there may be some import issues which you need to review before doing anything else.

#### Resolving issues importing historic vaccination records

Mavis will highlight any potential duplicates found in the uploaded file and compared with what was already in Mavis as an import issue.

Go to the **Import issues** tab. For each record:

1. Select **Review**.
2. Select which version of the record you want to keep and select resolve duplicate.

If there are some parts of each that are correct, you can note down any correct information from the version you choose to discard, discard it, then go to the child’s record and manually edit the information there (this feature will be more developed in a future release of Mavis).

### Checking cohorts and what to do next

Once you have uploaded all the cohort files and vaccination records, you can go to the **Cohorts** tab and check the counts for each year group show the number of children who need to be vaccinated in this programme year. 

You can also check individual children’s records by navigating to the **Children** tab. However, you won’t be able to see the children listed under their school in the sessions tab until you have scheduled at least one session at that school. 

Once you have confirmed that the cohort and vaccination records are successfully uploaded, you can proceed to:

- [Scheduling school sessions](/guide/sessions/) or
- [Adding class lists](/guide/class-lists/)

## Setting up unvaccinated cohorts only in Mavis

### Creating the initial cohort lists (year 8s and unvaccinated year 9 to 11s)

{% from "inset-text/macro.njk" import insetText %}
{{ insetText({
  html: "You should upload cohort records before you upload class lists."
}) }}

You should only include records for children in the year 9, 10 and 11 cohorts who haven’t already been vaccinated in previous years. If a cohort record is uploaded into Mavis without a corresponding vaccination record, then that child will receive a consent request, so it is important if you are not uploading historic vaccination records to filter out anyone who is already vaccinated at the cohorting stage.

To upload cohort records and resolve any issues with the import, follow the instructions on this page:

- [Upload cohort records](/guide/uploading-cohorts/)

### Checking cohorts and what to do next

Once you have uploaded all the cohort files, you can go to the Cohorts tab and check the counts for each year group are as expected. 

You can also check individual children’s records by navigating to the Children tab. However, you won’t be able to see the children listed under their school in the sessions tab until you have scheduled at least one session at that school. 

Once you have confirmed that the cohort is successfully uploaded, you can proceed to:

- [Scheduling school sessions](/guide/sessions/)
- [Adding class lists](/guide/class-lists/)

## Handling out-of-year-group children

{% include "fragments/out-of-year-group-children.md" %}

## Manually editing individual child records

1. Go to **Children**.
2. Search for the child by name and select their record.
3. Select **Edit child record**.
4. Find the information you want to edit and select **Change**.
5. Edit the information and select **Continue**.
6. Select **Save changes**.
