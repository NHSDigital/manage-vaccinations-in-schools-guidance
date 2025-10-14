---
title: Class list upload template
theme: File upload templates
order: 2
eleventyComputed:
  eleventyNavigation:
    key: Class list upload template
---

This template shows what information you need to upload when importing class lists into Mavis.

{% from "attachment/macro.njk" import attachment %}
{{ attachment({
  text: "Class list import template",
  summary: "Microsoft Excel spreadsheet, 17 KB",
  href: "/files/class-list-import-template.xlsx"
}) }}