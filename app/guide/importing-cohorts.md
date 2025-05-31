---
title: Importing cohorts into Mavis
theme: Managing cohorts
order: 3
eleventyComputed:
  eleventyNavigation:
    key: Importing cohorts into Mavis
---

[[toc]]

Mavis is designed to be used with complete age-based cohorts, including those already vaccinated in previous academic years.

Before using Mavis for vaccination programmes, SAIS teams will need to:

- import full details of the cohort in the team’s area
- upload relevant historical vaccination records for all children in the cohort

We explain how to do this below.

## Uploading cohort records

> [!NOTE]
> You should upload cohort records before you upload vaccination records or class lists.

The cohort should include all children in your SAIS team’s area, as follows:

- all children in the target year (or years) for the vaccination programme, which is usually:
  - HPV - Year 8
  - MenACWY and Td/IPV - Year 9
  - flu - all years from Reception (Year 0) to Year 11 (or up to Year 13 or 14 for Special Educational Needs schools, where applicable)
- all children in older year groups, up to Year 11, whether they have already been vaccinated or not

You’ll only need to upload the older year groups the first time you use Mavis. Once the cohort has been set up and used to record vaccinations for a particular year group, those records will stay in Mavis.

### What to include

You must include include the following information for each child in the cohort:

- unique reference number (URN) for their school (use 888888 for school unknown, or 999999 for home-schooled)
- first name
- last name
- date of birth
- postcode

The template below shows what other information can be imported into Mavis for child records.

{% from "attachment/macro.njk" import attachment %}
{{ attachment({
  text: "Cohort import template",
  summary: "Microsoft Excel spreadsheet, 18 KB",
  href: "/files/cohort-import-template.xlsx"
}) }}

If you haven’t included a child’s NHS number, we’ll retrieve it from the Personal Demographics Service (PDS) - Mavis automatically searches PDS to find a match for the child, using the information you’ve provided (their date of birth must be correct for this to work).

### Preparing files for upload

You can use the template provided below, or your own files as long as the headings and formatting match those in our template.

To upload files successfully:

- the cohort records must be in the format shown in the template above (note that for flu, Reception is Year 0 in Mavis)
- information marked as ‘Required’ in our template must be included for each child
- files need to be in .csv format
- if you have an Excel file with multiple tabs, you will need to consolidate this into a single tab before saving it as a CSV file, or create a separate CSV file for each tab
- make sure the file you’re uploading has no more than 10,000 rows

> [!NOTE]
> Large cohort files can fail to upload, due to their size. If your CSV file has over 10,000 rows, we recommend you split it into smaller files - for example 2 files with 5,000 rows.

### How to upload a cohort file

1. From the dashboard, go to **Import records** (or click on Imports in the top navigation).
2. Click on the **Import records** button near the top of the page.
3. Select **Child records**, then click Continue.
4. Click on **Choose File**, then select the CSV file you want to import.
5. Click **Continue**. If there are any validation issues, Mavis will not import the file. Correct the issues listed in the file and try again.
6. Wait for the file to finish importing.

![Screenshot of programme overview.](/assets/images/programme-overview.png 'Mavis shows the number of children within each programme cohort.')

Once the file has finished uploading, there may be some import issues which you need to review before doing anything else.

## Resolving issues when uploading files

Mavis will highlight any potential duplicates found in the uploaded file and compared with what was already in Mavis as an import issue.

Go to the **Import** tab. Under **Import issues**, for each record:

1. Select **Review**.
2. Select which version of the record you want to keep and select **Resolve duplicate**.

If there are some parts of each that are correct, you can note down any correct information from the version you choose to discard, discard it, then go to the child record and manually edit the information there (this feature will be more developed in a future release of Mavis).
