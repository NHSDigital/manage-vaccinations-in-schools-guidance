---
title: Importing cohorts into Mavis
theme: Managing cohorts
order: 4
eleventyComputed:
  eleventyNavigation:
    key: Importing cohorts into Mavis
---

[[toc]]

Mavis is designed to be used with complete age-based cohorts, including those already vaccinated in previous school years.

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
  - flu and MMR(V) - all years from Reception (Year 0) to Year 11 (or up to Year 13 or 14 for Special Educational Needs schools, where applicable)
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

If you haven’t included a child’s NHS number, we’ll retrieve it from the Personal Demographics Service (PDS) - Mavis [automatically searches PDS](/guide/importing-cohorts#see-how-mavis-uses-pds-to-find-nhs-numbers). to find a match for the child, using the information you’ve provided (their date of birth must be correct for this to work).

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
2. Click on the **Upload records** button near the top of the page.
3. Select **Child records**, then click Continue.
4. Click on **Choose File**, then select the CSV file you want to import.
5. Click **Continue**. If there are any validation issues, Mavis will not import the file. Correct the issues listed in the file and try again.
6. Wait for the file to finish uploading.

![Screenshot of processed cohort import.](/assets/images/processed-cohort-import.png)

Once the file has finished uploading, there may be some import issues which you need to review before doing anything else.

## Reviewing and approving uploads

![Screenshot of review screen for cohort import.](/assets/images/review-cohort-import.png)

When you upload child records, Mavis will identify children it already has records for.

If it’s an exact duplicate, Mavis will simply not import the record again - you’ll see a notification telling you how many records were not imported because they already exist in Mavis.

If the file upload includes additional information for the child, such as their gender or preferred name, this will be added to the existing record if you approve the upload.

If Mavis identifies any near matches with existing child records, you will need to review the missing or conflicting details after approving the upload, and confirm which record to keep and which record to archive.

Click **Approve and import records**

You'll need to review close matches and school moves after importing.

1. Click **Review** for each record listed.
2. For close matches, select which version of the record you want to keep and select **Resolve duplicate**.

There is also an option to keep both child records. For example, in the case of twins, Mavis will identify a near match, but you can select **Keep both records**. The existing record will stay in Mavis and the uploaded record will be added.

If there are some parts of each record that are correct, you can:

1. note down any correct information from the version you choose to archive
2. archive that record
3. go to the record you are keeping and edit the information there

Mavis will also highlight if you’ve provided an NHS number for a child that is different from the NHS number held by PDS. Mavis will automatically replace the incorrect NHS number you provided with the correct one from PDS (see below).

> [!NOTE]
> If less than 70% of records match an NHS number in PDS, the upload will be rejected, and you’ll see an error message. You should review the file, correcting any formatting issues (for example, make sure the first name and last name columns and the date of birth rows are in the correct position) and try uploading it again.

> [!NOTE]
>Some records may have changed since you uploaded your file. For example, another import might have been approved that includes some of the records in your file, or a child's school or NHS number may have changed in Mavis. If this happens, you’ll need to review those records again and confirm you still want to import the remaining changes from your file.

## See how Mavis uses PDS to find NHS numbers

Mavis may add a missing NHS number or replace an incorrect one in your upload by searching the NHS Patient Demographics Service (PDS) (sometimes referred to as ‘the Spine’).

If this happens, a PDS history link appears beside the NHS number in the child’s record.

![Screenshot of PDS history link on child record.](/assets/images/pds-history-link.png)

If there are any doubts or queries about the NHS number, you can see how Mavis found it by clicking the PDS history link.

The NHS number lookup history shows the different steps Mavis takes to search for the NHS number, and explains the search methods.

![Screenshot of PDS search history.](/assets/images/pds-search-history.png)
