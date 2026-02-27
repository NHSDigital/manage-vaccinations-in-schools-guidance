---
layout: page
title: Emails and text messages Mavis sends to parents
---

## Consent requests

For scheduled sessions, Mavis automatically contacts parents 3 weeks before a scheduled session to inform them about the vaccines and ask for consent. A reminder is sent 1 week before the session to those who have not responded.

{% from "contents-list/macro.njk" import contentsList %}
{{ contentsList({
  text: "Consent request templates",
  items: collections["consent-request"]
}) }}

## Consent response confirmation

Once a parent has completed a consent form, Mavis sends them a confirmation.

{{ contentsList({
  text: "Consent response confirmation templates",
  items: collections["consent-outcome"]
}) }}

## Triage outcomes

Once a nurse has triaged answers to health questions, Mavis sends the parent confirmation of their decision.

{{ contentsList({
  text: "Triage outcome templates",
  items: collections["triage-outcome"]
}) }}

## Session reminder

One day before a session, Mavis sends a reminder to parents who consented to a vaccination, with details of the upcoming session.

{{ contentsList({
  text: "Session reminder templates",
  items: collections["session-reminder"]
}) }}

## Session outcomes

Once a vaccination session has been completed, Mavis sends the parent confirmation of the vaccination given, or the reason it was not given.

{{ contentsList({
  text: "Session outcome templates",
  items: collections["session-outcome"]
}) }}

## Clinics

{{ contentsList({
  text: "Clinic templates",
  items: collections["clinics"]
}) }}
