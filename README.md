# Manage vaccinations in schools guidance

This website hosts guidance for the Manage vaccinations in schools service.

The website can be found at [guide.manage-vaccinations-in-schools.nhs.uk](https://guide.manage-vaccinations-in-schools.nhs.uk).

Content lives within the [app](./app) folder as Markdown files.

The website is built using the [Eleventy](https://www.11ty.dev) static site generator, and hosted using [GitHub Pages](https://pages.github.com).

## Updating content

The canonical source of content for the user guide is a Google Doc. This document should be edited first and any changes reviewed if necessary before the user guide is updated.

The canonical source of content for the XLSX file download templates is Microsoft SharePoint. These documents should be edited first before downloading and updating the files in this repository.

### Updating screenshots

To get an updated set of screenshots from the latest deployed version, setup with the following:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```
Ensure you are on the latest version of Mavis. Reset the database used in your local deployment of the service, visiting the `/reset` endpoint.

Then run: 
```bash
python dynamic_screenshots/generate_images.py
``` 
The images will be stored in the `app/assets/images` directory.

If it fails with several timeout error, re-run the script. This happens due to temporary database performance issues.

Currently, there is not sufficient logic to generate screenshots of the following:
* 'Notices' tab ([`notices.png`](app/assets/images/notices.png)) 
* Offline recording spreadsheet ([`offline-spreadsheet.png`](/app/assets/images/offline-spreadsheet.png)). 

These will have to be generated manually and added to the `app/assets/images` directory if they need updating.

#### To add a new image:
- Add image metadata, including name and path, to the `images.py` file.
- If further processing is needed from the path, such as click-throughs, create a function in `process_images.py`.


## Running locally

First install [Node.js](https://nodejs.org/en).

Then install the dependencies by running this command:

```bash
npm install
```

You can then run the site locally by running:

```bash
npm start
```

The static site is built using this command:

```bash
npm run build
```

## Deployment

The [`deploy.yml`](./.github/workflows/deploy.yml) file is used to build the site and deploy it to GitHub Pages every time a change is made and pushed to the `main` branch.
