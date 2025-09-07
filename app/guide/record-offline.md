---
title: Recording vaccinations offline
theme: Recording vaccinations
order: 27
eleventyComputed:
  eleventyNavigation:
    key: Recording vaccinations offline
---

To record vaccinations in Mavis, you need to have internet access. If a reliable internet connection is not available, you should work offline instead.

## Preparing to work offline

The vaccination record spreadsheet contains a record for all children in the session, whether they are ready to vaccinate or not.

To download the spreadsheet for a session:

1. Go to **Sessions**.
2. Filter for **Scheduled** sessions.
3. Click the link for the school you’re interested in.
4. Click on the **Record offline** link at the top of the page to download the Excel file.
5. Save this locally.
6. Once downloaded, a copy of the spreadsheet should be shared with all the nurses and admins attending the session.

![Screenshot of the offline recording spreadsheet.](/assets/images/offline-spreadsheet.png)

Rows in the spreadsheet can be given a colour to indicate the child's consent status:

- **Red** indicates that consent has been refused.
- **Orange** indicates that the child has conflicting consent.

## Recording a vaccination offline

To prepare to vaccinate a child:

1. Make sure you have the session vaccination spreadsheet open.
2. Find the row for the child using their name and date of birth if necessary.
3. Scroll across to review the child’s consent status and triage outcome.
4. If there is a change in a child’s consent status or triage outcome on the day, the spreadsheet should be edited with this change and then annotated to indicate the change. The annotation is necessary so that it can be manually added to Mavis after the session.

To record a vaccination offline if the child was vaccinated:

1. Choose ‘Y’ from the dropdown menu in the vaccinated column.
2. Enter the date and time of the vaccination (in the format YYYYMMDD and HH:MM:SS) and your email address in the relevant columns.
3. Choose the correct details for the vaccine and the batch used in the relevant columns using the dropdown menus.
4. Any notes about the vaccination should be added to the notes column.

If a child was not vaccinated:

1. Choose ‘N’ from the dropdown menu in the vaccinated column.
2. Choose the correct reason why the vaccine was not performed in the relevant column using the dropdown menu.
3. Any notes about the vaccination should be added to the notes column.

### Entering valid information

When filling out the spreadsheet, you need to make sure you use accepted formats. If you don’t use accepted formats, you won’t be able to upload the spreadsheet.

To view a list of accepted formats:

1. Go to **Import**.
2. Click on **Import records**.
3. Select **Vaccination records** and **Continue**.
4. Open the link ‘How to format your CSV for vaccination records’.

## Adding offline data to Mavis

Once you have a reliable internet connection again, you can update Mavis with the results of the session.

Before doing this, the individual spreadsheets from each nurse should first be amalgamated into a single spreadsheet containing all the vaccination records from the session.

### Manual changes to child records

Before uploading the vaccination record spreadsheet, any changes in consent status, Gillick competence or triage decisions should first be made manually in Mavis. To do this, please follow the guidance in other sections of this user guide.

### Uploading the spreadsheet

Note that only one person should upload a spreadsheet per session; you should not upload different versions of the spreadsheet for the same vaccination session.

Before uploading the spreadsheet, you first have to save a copy of the data from Excel as a CSV:

1. Open the spreadsheet in Excel.
2. Go to **File > Save a copy** and then choose format “CSV UTF-8 (Comma delimited) (.csv)” and save it.
3. A dialog box displays telling you that this file format does not support multiple sheets - click on OK.

Then in Mavis:

1. Go to **Import**.
2. Click on **Import records**.

![Screenshot of Import page.](/assets/images/import-records.png)

3. Select **Vaccination records** and **Continue**.
4. Click on **Choose File**.
5. Open the file and select **Continue**. If there are any validation issues, Mavis will not import the file.
6. Correct the issues listed and try again.
7. Wait for the file to finish importing.

### Updating subcutaneous vaccinations

Finally, if any vaccinations were subcutaneous rather intramuscular, this needs to be updated manually on an individual vaccination record.

To do this:

1. Go to the relevant session in Mavis.
2. Go to the **Children** tab.
3. Filter for **Vaccinated** children.
4. Find the name of the child in the list and click on their name.
5. On the child record, scroll down the page to find the vaccination record.
6. Click on **Edit vaccination record**.
7. Click on **Change** next to the existing vaccination method.
8. Update the details of the method and click **Continue**.
9. Review the change to the record and then click **Save changes**.

### Updating dose volume for flu (nasal spray)

If a child refuses the second half of a nasal spray flu vaccination, you can record this as a half dose in Mavis. However, if you’re recording vaccinations offline, you cannot do this on the spreadsheet - instead, you’ll need to:

1. Record the vaccination as a full dose on the offline spreadsheet.
2. Make a note on the spreadsheet that only half the dose was given.
3. Manually update the child’s vaccination record in Mavis after you’ve uploaded the spreadsheet.

To do this:

1. Follow the steps described above to find and edit the child’s vaccination record (see steps 1 to 6 in ‘Updating subcutaneous vaccinations’).
2. Click on **Change** next to the existing **Dose volume** shown in the vaccination details.
3. Mavis will ask if the child got the full dose or a half dose. Select half dose then click **Continue**.
4. Review the change to the record, then click **Save changes**.
