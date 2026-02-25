---
title: Vaccination records upload template
theme: File upload templates
order: 3
eleventyComputed:
  eleventyNavigation:
    key: Vaccination record upload template
---

This template shows what information you need to upload when importing historical vaccination records into Mavis.

{% from "attachment/macro.njk" import attachment %}
{{ attachment({
  text: "Vaccination records upload template",
  summary: "Microsoft Excel spreadsheet, 18 KB",
  href: "/files/historical-vaccination-records-import-template.xlsx"
}) }}
