---
title: Sharing vaccination records between Mavis and SystmOne
theme: Statistics and reports
order: 35
eleventyComputed:
  eleventyNavigation:
    key: Sharing vaccination records with SystmOne
---

SAIS teams who use Mavis alongside SystmOne as an electronic patient record need to ensure that vaccination records created in Mavis also appear in SystmOne.

Mavis automatically sends vaccination records to children’s GP practices. If a child’s GP practice also uses SystmOne, the record will automatically appear in your SystmOne system.

However, if the child's GP practice uses EMIS or Medicus, you'll need to import those records into SystmOne manually.

Until there’s fully automated data sharing, you should periodically download vaccination records from Mavis and upload them in bulk to SystmOne. SystmOne will automatically ignore any duplicates, so you don’t need to filter out records that have already synced.

## Upload Mavis records to SystmOne

### Download a vaccination report from Mavis

1. From the **Programmes** tab in Mavis, select the correct academic year and programme and select **Download vaccination report**.
2. Select a date range.
3. Select the **CSV for SystmOne (TPP)** file format and **Continue**.

### Upload the file to SystemOne

1. Open SystmOne.
2. Use the application menu to navigate to **Setup** then **Bulk Operations** then **Childhood Vaccination Upload**.

![Screenshot of how to find the Childhood Vaccination Upload in SystmOne.](/assets/images/s1-menus.png)

3. Select the data file you want to upload.
4. Select **Import file**.

### Review and resolve records

1. Resolve any records that appear in the **Unmatched Patients** tab.
2. Check that any records that appear in the **Ready for Upload** tab look as expected.
3. Review any errors shown in the **Errors** tab:
    - to double-check the errors, you can download a CSV of the errors and use filters to check that all of the errors are *"This item already exists on the child's record. Details of this item will not be included in any task created as a result of this upload."*
    - you’ll need to review and resolve any other errors separately

4. Select **Accept Changes**.

### Confirm the upload

1. You’ll see an error message saying that errors exist with the upload.

![Screenshot of the SystmOne error message when errors exist with the upload.](/assets/images/s1-error-message.png)

2. Select **OK** to dismiss the error message.
3. The new records will have been added to SystmOne successfully and the duplicates ignored.
4. You can verify this by checking the patient record for one of the records that was in the **Ready for Upload** tab.
