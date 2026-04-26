# ACC-WTW-002 — WTW ATA 44 Dispatch Rules (MEL)

**Doc ID:** T-A-ATA44-WTW-ACC-002
**Variant:** WTW
**ATA Subchapter:** 44-10 / 44-20
**Status:** DRAFT (LC01 — MEL provisions at LC05)
**Parent:** [Acceptability README](README.md)

---

## 1) Purpose

Documents WTW-specific dispatch rules for degraded CMS modes. These rules will feed
the MMEL and operator MEL process at LC05.

---

## 2) CMS Degraded Mode Dispatch

| Condition | Dispatch Allowed? | Dispatch Limit | Restoration |
|-----------|-----------------|----------------|-------------|
| CMC failed, CAC operational | TBD | TBD days | CMC replacement |
| CAC failed, CMC operational | TBD | TBD days | CAC replacement |
| Both CMC and CAC failed | TBD | No dispatch (provisional) | Both restored |
| IFE server failed | TBD (pax convenience only) | TBD days | IFE server replacement |
| 1 of 4 CSUs failed | TBD | TBD days | CSU replacement |
| 2 or more CSUs failed | TBD | TBD | TBD |
| Satcom antenna failed | TBD | TBD days | Antenna replacement |

---

## 3) WTW-Specific Dispatch Considerations

> Δ WTW-only:

- CAC failure in WTW does not affect cabin zones Z1/Z2 (CMC driven) — passenger impact is Z3/Z4 only.
- BWB uses distributed bay controllers; WTW centralised architecture means CMC failure affects all zones.
- IFE loss on WTW is passenger comfort only — no safety impact assumed.

---

## 4) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Define CMS MMEL provisions based on safety analysis | Safety / Certification | LC05 |
| Confirm IFE no-dispatch classification with authority | Certification | LC05 |
| Align with ATA 25 MEL where cabin systems and furnishings dispatch overlap | Cabin / Cert | LC05 |
