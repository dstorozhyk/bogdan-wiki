---
title: Emergency fund quarterly review
created: 2026-08-17
updated: 2026-08-17
type: workflow
status: approved
approval: user-directed
tags: [finance, workflow]
sources:
  - "finance/emergency-fund/strategy.md"
  - "finance/emergency-fund/dashboard.md"
---

# Emergency fund quarterly review

## Trigger

Run:

- every three months;
- after a material change in essential monthly expenses or income;
- after using any emergency-fund tier;
- after a platform, custody, regulatory or access incident.

This workflow prepares a decision. It does **not** authorize trades, transfers, lock-ups or account changes.

## 1. Refresh source data

Before analysis, record a verification date and update:

- essential monthly expenses;
- actual balance by instrument;
- currency and location;
- time needed to access funds;
- maturity/lock date;
- fees, taxes and withdrawal constraints.

The dashboard values dated 2026-06-25 are historical until manually refreshed.

## 2. Recalculate resilience

With a calculation tool, determine:

- total reserve;
- months of essential expenses covered;
- progress against 3-, 6- and 9-month phases;
- amount and percentage in each liquidity tier;
- concentration by institution, jurisdiction and asset/issuer;
- gap to target for each tier.

Do not infer live value from stale market prices or old screenshots.

## 3. Test access rather than labels

For each instrument ask:

- Can it be accessed in the expected tier window?
- Does access depend on market hours, settlement, KYC or a functioning card rail?
- Is there a lock, minimum lot or early-redemption penalty?
- Would the same incident impair several instruments at once?

If an instrument no longer meets the tier's access objective, treat it as a tier mismatch even when its nominal value is stable.

## 4. Review platform and instrument risk

Verify current, sourced facts:

- broker/exchange/bank availability for Denys's account and jurisdiction;
- custody or reserve disclosures where relevant;
- incidents, withdrawal restrictions or material policy changes;
- current regulatory/tax treatment;
- current yield after fees and taxes;
- funding/withdrawal route still works with a small test when needed.

Use dated research as a question list, not as proof that June 2026 conditions still apply.

## 5. Compare yield only after risk

Compare expected after-fee/after-tax return between instruments with similar liquidity. A higher yield does not compensate automatically for:

- longer lock-up;
- weaker custody or issuer quality;
- greater account-freeze/withdrawal risk;
- concentration in one platform;
- operational complexity.

If extra return is small relative to additional risk, prefer the simpler/liquid option.

## 6. Produce a decision packet

Prepare:

- refreshed table of actual vs target;
- top three resilience gaps;
- proposed transfers/rebalancing in priority order;
- evidence and verification date for every volatile claim;
- fees/taxes/settlement assumptions;
- actions that require Denys approval;
- explicit `do nothing` option.

## 7. Approval and execution boundary

Before any external financial action, Denys approves:

- exact instrument/account;
- exact amount;
- funding and withdrawal route;
- lock or maturity;
- material fees/tax assumptions.

After approval, execute one scoped action at a time and verify the destination credit. Never report success from a send/confirmation screen alone.

## 8. Record the review

Update the dashboard `last_updated` only when balances were actually refreshed. Preserve prior snapshots when historical comparison matters. Record any changed strategy separately from balance changes.

## Success criteria

- actual balances have a verification date;
- the fund's months of coverage and tier gaps are calculated;
- no current recommendation depends solely on stale rates/policies;
- all proposed actions have explicit approval boundaries;
- the next review trigger is clear.

## Related

- [[emergency-fund-liquidity-tiers]]
- [[finance/emergency-fund/strategy|Emergency fund strategy]]
- [[finance/emergency-fund/dashboard|Emergency fund dashboard]]
