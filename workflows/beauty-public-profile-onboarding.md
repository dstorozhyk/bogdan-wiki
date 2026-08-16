---
title: Beauty public profile onboarding
created: 2026-08-17
updated: 2026-08-17
type: workflow
status: approved
approval: user-directed
tags: [beauty, project, workflow]
sources:
  - "projects/beauty-growth-assistant/product-requirements.md"
  - "projects/beauty-growth-assistant/overview.md"
---

# Beauty public profile onboarding

## Outcome

Create a mobile-first professional page that lets a client understand the master, services, trust and location, then start a conversation or booking request.

The baseline page works **without CRM, calendar, analytics or full booking automation**.

## Approval boundary

This workflow defines product/content onboarding. It does not authorize publishing, deployment, contacting a master, using real client photos/reviews, or enabling automated booking/messages.

Implementation plans and untracked project docs are references, not proof of deployed architecture.

## 1. Collect the minimum identity set

Required:

- public master/studio name;
- specialty and short positioning line;
- city/area and service location wording;
- whether new clients are accepted;
- Instagram profile/link;
- Telegram or equivalent direct-chat link; Viber, WhatsApp and phone are optional.

Optional:

- approved portrait or mood image;
- short personal introduction.

If no photo is approved, use a service-first typographic composition. Do not invent a fake avatar or monogram persona.

## 2. Build the service menu

For each featured service collect:

- public name;
- price or honest `from` price;
- duration when useful;
- short clarification of what is included;
- any preparation or eligibility note that must be known before contact.

Start with the 3–5 services that best explain the offer. Do not make the first screen a full internal catalog.

## 3. Prepare trust evidence

Use only approved, attributable material:

- portfolio photos;
- one or more real reviews;
- experience/certification where meaningful;
- hygiene/safety or material-quality signals;
- clear location and route information.

Do not fabricate testimonials, client outcomes, popularity, availability or credentials.

## 4. Define the primary CTA

Choose one main action:

- write in Instagram;
- open Telegram/chat;
- call;
- submit a booking request, only if that module is approved and available.

The baseline fallback is always a direct contact action. CRM absence must not make the public page useless.

## 5. Assemble the page hierarchy

Recommended order:

1. identity, specialty, area/status;
2. primary contact/booking CTA;
3. services and prices;
4. portfolio/recent work;
5. review or trust block;
6. location/route;
7. social and chat contacts;
8. optional available slots or booking request only when connected.

The page is a professional identity card—not a mini-dashboard or generic SaaS landing page.

## 6. Apply visual direction

- design mobile-first;
- prioritize readability, services and work examples;
- use a light premium direction appropriate to the specialty;
- avoid default black-and-gold luxury clichés;
- keep hierarchy calm and personal rather than theatrical;
- do not expose internal metrics, dashboards or admin controls.

Bohdan does not replace Denys's manual frontend authorship unless explicitly asked to implement or change UI.

## 7. Review content with the owner

The owner approves:

- public name and positioning;
- images and reviews;
- services/prices;
- address/location detail;
- contact channels;
- wording of the primary CTA;
- any displayed availability.

Record missing items explicitly instead of filling them with invented placeholders in production content.

## 8. Verify the artifact

Before any release:

- test at narrow mobile widths;
- verify every contact and map link;
- confirm prices and public location wording;
- check image consent and review provenance;
- verify no dashboard, analytics, QR-on-page or internal CRM content leaked into the public surface;
- inspect visually, including no-photo state;
- obtain separate approval for deployment/publication.

## Optional maturity ladder

Only after separate product approval:

1. manual availability/slots;
2. booking request with manual confirmation;
3. reminders/templates controlled by the master;
4. client history and other CRM functions;
5. higher automation for trusted scenarios.

The default principle remains **automation without loss of control**.

## Related

- [[projects/beauty-growth-assistant/overview|Beauty Growth Assistant]]
- [[projects/beauty-growth-assistant/product-requirements|Beauty product requirements]]
- [[ai-assisted-product-lifecycle]]
