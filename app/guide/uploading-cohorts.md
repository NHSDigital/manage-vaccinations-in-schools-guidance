---
title: Uploading cohort records
group: Programmes
order: 12
---

Cohort records can be uploaded using the following template:

{% from "attachment/macro.njk" import attachment %}
{{ attachment({
  text: "Cohort import template",
  summary: "Microsoft Excel spreadsheet, 18 KB",
  href: "/files/cohort-import-template.xlsx"
}) }}

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

Once the file has finished importing, there may be some import issues which you need to review before doing anything else.

### Resolving issues importing a cohort list

Mavis will highlight any potential duplicates found in the uploaded file and compared with what was already in Mavis as an import issue.

Go to the **Import issues** tab. For each record:

1. Select **Review**.
2. Select which version of the record you want to keep and select resolve duplicate.

If there are some parts of each that are correct, you can note down any correct information from the version you choose to discard, discard it, then go to the child record and manually edit the information there (this feature will be more developed in a future release of Mavis).
