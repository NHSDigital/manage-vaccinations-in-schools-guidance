---
title: Adding vaccination history
theme: Managing cohorts
order: 5
---

[[toc]]

You should upload relevant historical vaccination records before scheduling school sessions. 

This allows Mavis to:

* identify which vaccinations a child has already had 
* only send consent requests for children who have not had the vaccine already

If you later find out that a child has already been vaccinated, you can update their record in Mavis (see ‘Manually recording a child as already vaccinated’ below).

You should include vaccination records for anyone in the cohort who was vaccinated elsewhere, if you have them. These records will be stored in Mavis and will not be sent anywhere else.

## What vaccination history you need to upload

How much vaccination history you need to upload depends on the programme. 

> [!NOTE]
> If you do not upload vaccination histories for a year group, but then you schedule a session that includes that year group, the parents of every child in that year will get a consent request, including those already vaccinated.

#### Flu
Do not upload flu vaccination records from previous academic years. 

Only upload a record if the flu vaccination was given in the current academic year.

#### HPV

Upload records of any previous HPV vaccinations given to children in your cohort from age 9 onwards. 

For example:
if you’re vaccinating children in Year 8, upload records from the previous 4 years 
if you’re running a catch-up session for Year 10, upload records from the previous 6 years 

#### MenACWY

Upload records of any previous MenACWY vaccinations given to children in your cohort from age 10 onwards. 

For example, if you’re vaccinating children in Year 9, upload records from the previous 3 years. 

#### MMR(V)

Mavis needs each child’s full MMR vaccination history from 12 months of age onwards. 

This means you should upload vaccination history as far back as the oldest child in the cohort minus one year. 

For example:
if you’re vaccinating Year 6 children (where the oldest child is 11), upload records from the previous 10 years
if you’re vaccinating Year 11 children (where the oldest child is 16), upload records from the previous 15 years

#### Td/IPV

Upload records of any previous Td/IPV (3-in-1) vaccinations given to children in your cohort from age 9 onwards.

For example, if you’re vaccinating children in Year 9, upload records of Td/IPV vaccinations from the previous 5 years. 

> [!NOTE]
> Do not upload records of any previous tetanus-, diphtheria- or polio-containing vaccines that are not Td/IPV, for example the 6-in-1 vaccine or the 4-in-1 pre-school booster. Mavis is not authorised to hold this information. 

## How to import historical vaccination records

Use the following template to upload historical vaccination records for HPV, MenACWY and Td/IPV from the last 3 years. 

For MMR(V), you should go as far back as the oldest member of the cohort minus one year. For example, if you’re vaccinating Year 6 children (where the oldest child is 11), you’d upload records for the last 10 years. For Year 11 children (where the oldest child is 16), this would mean uploading records for the last 15 years.

This does not apply to flu.

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
