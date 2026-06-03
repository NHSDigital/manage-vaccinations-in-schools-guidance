---
title: Uploading class lists
theme: Uploading records to Mavis
order: 8
---

[[toc]]

Before a session takes place, you’ll need to get an up-to-date class list from the school and upload it to Mavis. 

You can use our [school class list request email template](https://guide.manage-vaccinations-in-schools.nhs.uk/email-templates-for-sais-and-schools/), if needed, when requesting this information from schools.

Uploading class lists:

- adds parent contact details for children in the session, which Mavis uses to send consent requests
- identifies children who have moved in our out of the school since you uploaded the cohort 

You can use this template:

{% from "attachment/macro.njk" import attachment %}
{{ attachment({
  text: "Class list upload template",
  summary: "Microsoft Excel spreadsheet, 17 KB",
  href: "/files/class-list-upload-template.xlsx"
}) }}

Make sure you upload class lists separately for each school. Each school can only have one class list.

## Uploading a class list file

If the school did not provide the list in CSV format, you need to reformat it ready for upload:

1. Navigate to the relevant Excel file for the school and open it. If there are multiple tabs in the Excel sheet, the records need to be combined into a single table.
2. If present, remove the helper text row from the table (row 2).
3. Go to **File > Save a copy** and then choose the format **CSV UTF-8 (Comma delimited) (.csv)** and save it.

In Mavis:

1. Go to **Imports** in the top navigation.
2. Select **Upload records**.
3. Select **Class list records** then **Continue**.
4. Search for the school by name and select **Continue**.
5. Select which year groups these records are for.
6. Select **Choose File**, then select the CSV file you want to import.
7. Select **Continue**. If there are any validation issues, Mavis will not import the file. Correct the issues listed in the file and try again.
8. Wait for the file to finish uploading.

Mavis may add a missing NHS number or replace an incorrect one in your upload by searching PDS. (See [See how Mavis uses PDS to find NHS numbers](importing-cohorts.md#see-how-mavis-uses-pds-to-find-nhs-numbers))

> [!NOTE]
> If a school does not provide postcodes for every child, you can still upload the class lists. You will have to add any missing NHS numbers manually.

## Reviewing and approving uploads

After you successfully upload a class list, Mavis checks the records and shows a summary of what will happen if you confirm the upload. Review the results and select **Approve and import records** to continue, or **Cancel and delete upload**. 

![Screenshot of review screen for class import.](/assets/images/review-class-import.png)

### Records already in Mavis

When you upload class lists, Mavis identiies children it already has records for.

If it’s an exact duplicate, Mavis will simply not import the record again - you’ll see a notification telling you how many records were not imported because they already exist in Mavis.

If the file upload includes additional information for the child, such as their gender or preferred name, this will be added to the existing record if you approve the upload.

### Close matches to existing records

If Mavis identifies any close matches to existing child records, you will need to review the missing or conflicting details after approving the upload, and confirm which record to keep and which record to archive.

Click **Approve and import records**

You’ll need to review close matches and school moves after importing.

1. Click **Review** for each record listed.
2. For close matches, select which version of the record you want to keep and select **Resolve duplicate**.

There is also an option to keep both child records. For example, in the case of twins, Mavis will identify a near match, but you can select **Keep both records**. The existing record will stay in Mavis and the uploaded record will be added.

If each record contains some correct information:

1. Note any correct information from the record you plan to archive.
2. Go to the record you are keeping and edit the information there.
3. Archive the record you no longer need.

> [!NOTE]
> If less than 70% of records, uploaded with a postcode, match an NHS number in PDS, the upload will be rejected, and you’ll see an error message. You should review the file, correcting any formatting issues (for example, make sure the first name and last name columns and the date of birth rows are in the correct position) and try uploading it again.

> [!NOTE]
> Some records may have changed since you uploaded your file. For example, another import might have been approved that includes some of the records in your file, or a child's school or NHS number may have changed in Mavis. If this happens, you’ll need to review those records again and confirm you still want to import the remaining changes from your file.

### School moves

Mavis will automatically identify if a child’s school has changed and raise this on the School moves page.

To review a child changing school, follow the instructions on this page of the user guide:

- [Reviewing school moves](school-moves.md)

## Handling out-of-year-group children

{% include "fragments/out-of-year-group-children.md" %}

## Removing incorrect parent-child relationships from the import

If you import a class list and later find that the parent-child relationships are incorrect, you can remove those relationships from Mavis.

For example, you might need to do this if the parent details in your CSV file are not lined up with the right children. You can then:
- remove the parent-child relationships from Mavis
- correct the CSV file
- re-upload the file

> [!NOTE]
> Removing a parent-child relationship from Mavis will invalidate any consent responses the parent has given for that child. You can choose to only remove relationships where no consent response has been given.

1. Go to **Imports** and select the **Completed imports** tab.
2. Select the relevant import to view its details.
3. At the bottom of the details, select **Remove all parent-child relationships from import**.

![Screenshot of remove parent-child relationships button](/assets/images/remove-parent-child-relationships-button.png)

4. When asked “Are you sure you want to remove all parent-child relationships included in this import”, select **Continue** to confirm, or **Cancel** to stop.

### If parents have given consent responses

If any parents in the import have submitted a consent response for any children in the import, you can choose to leave those parent-child relationships in place, if you know they are correct.

1. Follow steps 1 to 3 described above.
2. Mavis will tell you that one or more parents in the import have submitted consent responses for children in the import. It will also show the full consent details.
3. Choose one of the following options:
   - **Only remove parent–child relationships where no consent response has been submitted**
   The relationships and consent responses shown above will stay in Mavis
   - **Remove all parent–child relationships included in this import**
   This will invalidate the consent responses listed above

Select **Continue** to confirm, or **Cancel** to stop.

![Screenshot of remove parent-child relationships confirmation screen](/assets/images/remove-parent-child-relationships-confirm.png)
