---
title: Checking important notices
group: Setup
order: 4
eleventyComputed:
  eleventyNavigation:
    key: Important notices
---

{% from "inset-text/macro.njk" import insetText %}
{{ insetText({
  html: "Only <a href='/guide/users/#superusers'>superusers</a> can view important notices."
}) }}

Whenever you log in to Mavis, you should go to **Notices** to see if there’s anything you need to be aware of.

![Screenshot of important notices page.](/assets/images/notices.png)

Records might be flagged as invalid if the child has 2 NHS numbers (if they’re adopted, for example).

If you see that a record has been flagged as sensitive, you need to follow this up with the child’s school and agree how to manage future contact outside Mavis.

You should remove all sensitive and invalid records from the cohort by clicking on the child’s name, scrolling down to **Cohorts** and clicking **Remove from cohort**.
