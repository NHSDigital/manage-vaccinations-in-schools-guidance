---
title: Adding vaccination history
theme: Managing cohorts
order: 5
---

[[toc]]

Where relevant, you should upload relevant historical vaccination records for HPV, MenACWY or Td/IPV before scheduling school sessions. This is so that Mavis:

- knows which vaccinations a child has already had (if applicable)
- only sends consent requests for children who have not had the vaccine already

If you discover at a later stage that a child is already vaccinated, you can update their record in Mavis (see ‘Manually recording a child as 'already vaccinated'’ below).

You should also include vaccination records for anyone in the cohort who was vaccinated elsewhere, if you have them. These records will be stored in Mavis and will not be sent anywhere else.

> [!NOTE]
> For flu, you should not upload vaccination records for previous academic years. Only upload a record for a previous flu vaccination if it was given in the current academic year.

## How to import historical vaccination records

Use the following template to upload historical vaccination records for HPV, MenACWY and Td/IPV from the last 3 years. This does not apply to flu.

{% from "attachment/macro.njk" import attachment %}
{{ attachment({
  text: "Vaccination records import template",
  summary: "Microsoft Excel spreadsheet, 18 KB",
  href: "/files/historical-vaccination-records-import-template.xlsx"
}) }}

Vaccination record files need to be in .csv format. Records can be all in one file, or split across multiple files; Mavis is not picky about this. If you have an Excel file with multiple tabs, you will need to consolidate this into a single tab or create a separate CSV file for each tab.

For each of your vaccination record CSV files:

1. Go to the **Imports** tab.
2. Click on the **Upload records** button near the top of the page.
3. Select **Vaccination records**, then click Continue.
4. Click on **Choose File**, then select the CSV file you want to import.
5. Click **Continue**. If there are any validation issues, Mavis will not import the file. Correct the issues listed in the file and try again.
6. Wait for the file to finish uploading

Once the file has finished uploading, there may be some import issues which you need to review before doing anything else.

## Resolving issues when uploading files

Mavis will highlight any potential duplicates found in the uploaded file and compared with what was already in Mavis as an upload issue.

Go to the **Imports** tab. For each record under **Upload issues**:

1. Select **Review**.
2. Select which version of the record you want to keep and select resolve duplicate.

If there are some parts of each that are correct, you can note down any correct information from the version you choose to discard, discard it, then go to the child’s record and manually edit the information there (this feature will be more developed in a future release of Mavis).

## Manually recording a child as 'already vaccinated'

If a child’s historical vaccination record is missing from CHIS data, or you have not been able to upload their historical vaccination record into Mavis, you can manually record the child as ‘already vaccinated’ for a specific programme. You can only do this once sessions have been scheduled (setting up sessions is covered in the ['Sessions'](/guide/sessions.md) section of this user guide).

1. From Sessions, select a session that is not currently in progress.
2. Search for the child under the **Children** tab - then click on the child’s name to open the child record.
3. Select the relevant tab for the vaccination programme you want to record.
4. Click on the **Record as already vaccinated** link near the top of the page.
5. Check the details on the page and add a note to explain this was a historical vaccination - then click the **Confirm** button.

> [!NOTE]
> You can only carry out this action for sessions that are not in progress.
