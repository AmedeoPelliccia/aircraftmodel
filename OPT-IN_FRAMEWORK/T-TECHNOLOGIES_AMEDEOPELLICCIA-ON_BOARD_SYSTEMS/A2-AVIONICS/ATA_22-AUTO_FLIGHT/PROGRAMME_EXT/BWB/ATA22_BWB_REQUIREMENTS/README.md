# ATA 22 BWB Requirements — Folder README

**Doc ID:** T-A2-ATA22-BWB-REQ-000
**Variant:** AMPEL360 Q100 BWB
**Status:** DRAFT
**Lifecycle:** Standard (LC01–LC13)

---

## Scope

This folder contains BWB-specific delta requirements for ATA 22 Auto Flight, organised by ATA 22 sub-chapter. All content is delta-only over the SHARED baseline at `../../..`. SHARED requirements apply unless overridden here.

---

## File Index

| File | Sub-Chapter | Delta Ref(s) |
|---|---|---|
| `REQ_BWB_22_000_GENERAL.yaml` | 22-00 General | All |
| `REQ_BWB_22_100_AUTOPILOT_AND_FD.yaml` | 22-10 Autopilot & FD | DELTA-BWB-22-001, DELTA-BWB-22-002 |
| `REQ_BWB_22_200_FMS_GUIDANCE.yaml` | 22-20 FMS Guidance | DELTA-BWB-22-004 |
| `REQ_BWB_22_300_AUTO_THRUST.yaml` | 22-30 Auto-Thrust | DELTA-BWB-22-005 |
| `REQ_BWB_22_400_ENVELOPE_PROTECTION.yaml` | 22-40 Envelope Protection | DELTA-BWB-22-003 |

---

## Requirement Identification Convention

BWB requirement IDs follow the pattern: `BWB-22-{sub}-{seq}` where:
- `{sub}` = 3-digit sub-chapter (000, 100, 200, 300, 400)
- `{seq}` = 3-digit sequence within sub-chapter
