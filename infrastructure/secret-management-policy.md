---
title: Secret management policy for agent operations
created: 2026-08-16
updated: 2026-08-16
type: guide
status: approved
approval: user-directed
tags: [infrastructure, workflow, security, secrets]
sources:
  - "session:default/20260813_055239_6fa82f3c"
---

# Secret management policy for agent operations

## Purpose

Allow agents to reuse approved credentials without repeatedly asking Denys, while minimizing credential exposure and machine-account privilege.

This page intentionally contains **no secret values, account identifiers, recovery material or tokens**.

## Storage boundaries

Runtime credentials belong in the approved Bitwarden infrastructure, not in:

- chat messages or summaries;
- persistent memory;
- wiki or skill files;
- source repositories;
- `.env` committed to source;
- shell history, process arguments or logs;
- screenshots or support artifacts.

If an existing authenticated browser session is available, check it before requesting credentials again.

## Bitwarden region and project boundary

- Hermes uses the **Bitwarden EU** environment.
- Agent runtime secrets belong to the dedicated **`hermes` project**.
- Direct BWS CLI operations must target the EU server.
- Machine credentials should receive only the project-scoped read/write access required by the workflow.
- Owner-vault access, organization administration and policy changes are not routine runtime privileges.

## Least-privilege lifecycle

1. Determine whether the workflow needs read, write or both.
2. Scope the machine credential to the smallest project/resource set.
3. Use interactive owner authentication only for token creation, policy changes or account administration.
4. Inject secrets into the runtime without persisting plaintext.
5. Do not print values during validation.
6. Verify by secret identifier/metadata or successful target action, not by echoing the secret.
7. Rotate/revoke access when exposure or scope drift is suspected.

Routine machine-token operations should not require repeated interactive 2FA after the token and policy have been authorized. 2FA remains relevant to owner login, token issuance and policy changes.

## Credential onboarding

When Denys explicitly provides or authorizes a new credential:

1. avoid repeating it in the response;
2. write it directly to the approved secret store using scoped access;
3. verify storage without displaying the value;
4. remove temporary plaintext artifacts when technically safe;
5. document only the secret's purpose and retrieval policy, never its value.

## Incident rule

If a secret appears in chat, logs, source, shell history or another uncontrolled surface, treat it as exposed. Do not copy it into the wiki as evidence; rotate or revoke it according to the affected service's workflow.

## Related

- [[vps-main]]
- [[agents/knowledge-policy|Agent knowledge policy]]
