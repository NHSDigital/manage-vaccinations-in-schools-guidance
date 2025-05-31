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
- upload relevant historic vaccination records for all children in the cohort

We explain how to do this below.

## Uploading cohort records

{% from "components/inset-text/macro.njk" import insetText %}
{{ insetText({
  html: "You should upload cohort records before you upload vaccination records or class lists."
}) }}

The cohort should include all children in your SAIS team’s area, as follows:

- all children in the target year for the vaccination programme (Year 8 for HPV, Year 9 for MenACWY and Td/IPV)
- all children in older year groups, up to Year 11, whether they have already been vaccinated or not

You’ll only need to upload the older year groups the first time you use Mavis. Once the cohort has been set up and used to record vaccinations for a particular year group, those records will stay in Mavis.

To upload cohort records, use the following template:

{% from "attachment/macro.njk" import attachment %}
{{ attachment({
  text: "Cohort import template",
  summary: "Microsoft Excel spreadsheet, 18 KB",
  href: "/files/cohort-import-template.xlsx"
}) }}

Make sure the cohort records are in the format shown in the template above. Files need to be in .csv format. Records can be all in one file, or split across multiple files; Mavis is not picky about this. If you have an excel file with multiple tabs, you will need to consolidate this into a single tab or create a separate CSV file for each tab.

1. Go to the **Import** tab.
2. Click on the **Import records** button near the top of the page.
3. Select **Child records**, then click Continue.
4. Click on **Choose File**, then select the CSV file you want to import.
5. Click **Continue**. If there are any validation issues, Mavis will not import the file. Correct the issues listed in the file and try again.
6. Wait for the file to finish importing.

![Screenshot of programme cohorts tab.](/assets/images/programme-cohorts.png 'Mavis shows the number of children within each programme cohort.')

Once the file has finished importing, there may be some import issues which you need to review before doing anything else.

## Resolving issues when uploading files

Mavis will highlight any potential duplicates found in the uploaded file and compared with what was already in Mavis as an import issue.

Go to the **Import** tab. Under **Import issues**, for each record:

1. Select **Review**.
2. Select which version of the record you want to keep and select **Resolve duplicate**.

If there are some parts of each that are correct, you can note down any correct information from the version you choose to discard, discard it, then go to the child record and manually edit the information there (this feature will be more developed in a future release of Mavis).
