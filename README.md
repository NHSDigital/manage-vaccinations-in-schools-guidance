# Manage vaccinations in schools guidance

This website hosts guidance for the Manage vaccinations in schools service.

The website can be found at [guide.manage-vaccinations-in-schools.nhs.uk](https://guide.manage-vaccinations-in-schools.nhs.uk).

Content lives within the [app](./app) folder as Markdown files.

The website is built using the [Eleventy](https://www.11ty.dev) static site generator, and hosted using [GitHub Pages](https://pages.github.com).

## Updating content

The canonical source of content for the user guide is a Google Doc. This document should be edited first and any changes reviewed if necessary before the user guide is updated.

The canonical source of content for the XLSX file download templates is Microsoft SharePoint. These documents should be edited first before downloading and updating the files in this repository.

### Screenshots

Screenshots can soon become out of date, to add them only if you need help orientate users or annotate a complex task.

If possible, show sections of the interface instead of the entire page. Again, this helps keep screenshots up to date as other parts of the service change.

Screenshots of full pages should be taken on a Mac with the browser width set to 1200 device pixels and using a 2× screen resolution. The resulting image should be cropped to be 2280px wide.

Screenshots of page elements should have a margin of 40 device pixels (80px).

## Syncing the live guide back to Google Docs

If the live Markdown guide has changed and the Google Doc needs to be updated to match it, use the `export_to_docx.py` script to generate a Word document from the Markdown files. You can then import the generated `.docx` file into Google Docs and copy the content into the canonical user guide document.

### Setup

From the `scripts` directory, install the required Python version and activate the virtual environment:

```bash
cd scripts
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Generate DOCX files

From the repository root, run:

```bash
python scripts/export_to_docx/export_to_docx.py app/guide/ latest-guide.docx
python scripts/export_to_docx/export_to_docx.py app/national-reporting/ latest-nr-guide.docx
```

This creates:

- `latest-guide.docx` for the main user guide
- `latest-nr-guide.docx` for the national reporting guide

Import these files into Google Docs, then copy the content into the canonical Google Docs.

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
