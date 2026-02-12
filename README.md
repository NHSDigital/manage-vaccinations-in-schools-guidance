# Manage vaccinations in schools guidance

This website hosts guidance for the Manage vaccinations in schools service.

The website can be found at [guide.manage-vaccinations-in-schools.nhs.uk](https://guide.manage-vaccinations-in-schools.nhs.uk).

Content lives within the [app](./app) folder as Markdown files.

The website is built using the [Eleventy](https://www.11ty.dev) static site generator, and hosted using [GitHub Pages](https://pages.github.com).

## Updating content

The canonical source of content for the user guide is a Google Doc. This document should be edited first and any changes reviewed if necessary before the user guide is updated.

The canonical source of content for the XLSX file download templates is Microsoft SharePoint. These documents should be edited first before downloading and updating the files in this repository.

## Updating the GOV.UK Notify templates

### Using GitHub Actions

The Notify templates can be updated automatically using GitHub Actions. This is done by manually triggering the
`update_notify_templates` workflow.

### Manually (locally)

Set up python in the `update_notify_templates` directory:

```bash
cd update_notify_templates
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Put a copy of the Notify API key in `update_notify_templates/.env`, by making a copy of
`update_notify_templates/.env.example` and replacing the placeholder with the actual key.
This key only needs to be of the type `Test - pretends to send messages`, because only template access is required.

To update the Notify templates, run the following command from the `update_notify_templates` directory:

```bash
python update_notify_templates.py
```

These changes then need to be committed and pushed to the repository's `main` branch.

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
