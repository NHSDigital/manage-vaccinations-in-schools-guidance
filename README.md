# Manage vaccinations in schools guidance

This website hosts guidance for the Manage vaccinations in schools service.

~~The website can be found at [guide.mavis.england.nhs.uk](https://guide.mavis.england.nhs.uk)~~.

Content lives within the [app](./app) folder as Markdown files.

The website is built using the [Eleventy](https://www.11ty.dev) static site generator, and hosted using [GitHub Pages](https://pages.github.com).

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
