# EVI-BWB-44-001 — BWB Distributed CMS Safety Analysis (FHA/FTA)

**Doc ID:** T-A-ATA44-BWB-EVI-001
**Evidence Type:** Safety Analysis (FHA, FTA, FMEA as applicable)
**Delta Refs:** DELTA-BWB-44-001, DELTA-BWB-44-002, DELTA-BWB-44-003
**Req Refs:** BWB-44-100-001, BWB-44-100-002, BWB-44-100-003, BWB-44-100-004
**Standard:** CS-25.1309
**LC Gate:** LC05 (stub — analysis at LC05)
**Status:** STUB

---

## Scope

Safety analysis for BWB-specific CMS failures in the distributed ZC/BBU architecture:

1. Per-bay ZC failure modes and effects (both ZCs in a bay failure)
2. Inter-bay BBU failure (zone isolation loss across bay boundary)
3. Full cabin CMS loss (all ZC + BBU failure)
4. PA synchronisation failure across bays (latency exceed or BBU loss)
5. Smoke event detection failure in one bay (ZC failure scenario)

---

## Analysis Approach (to be detailed at LC05)

| Step | Method | Tool |
|------|--------|------|
| Functional Hazard Assessment | FHA | TBD |
| Fault Tree Analysis (per bay ZC loss) | FTA | TBD |
| Failure Mode and Effects Analysis | FMEA | TBD |
| Common cause analysis | CCA | TBD |
| Safety assessment coverage (BBU failure independence) | DA | TBD |

---

## Key Failure Conditions to Assess

| Failure condition | Catastrophic / Hazardous / Major / Minor? | Notes |
|------------------|------------------------------------------|-------|
| All-bay PA announcement loss | TBD [LC05] | Emergency PA affected |
| Smoke detection loss in one bay | TBD [LC05] | Safety-critical |
| CMS status display loss (crew) | TBD [LC05] | Major likely |
| IFE total loss | TBD [LC05] | Minor |

---

## Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Complete distributed ZC FHA | Systems Safety | LC05 |
| Complete BBU failure FTA | Systems Safety | LC05 |
| Confirm smoke detection failure classification | Systems Safety / Avionics | LC05 |

---

## Related Documents

- [REQ_BWB_44_100_CABIN_CORE.yaml](../ATA44_BWB_REQUIREMENTS/REQ_BWB_44_100_CABIN_CORE.yaml)
- [ACC_BWB_DISPATCH_RULES.md](../ATA44_BWB_ACCEPTABILITY/ACC_BWB_DISPATCH_RULES.md)
- [WTW parallel](../../WTW/ATA44_WTW_VERIFICATION_EVIDENCE/ANALYSIS_WTW_CMS_SAFETY_1309.md)
