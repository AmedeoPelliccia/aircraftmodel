# EVI-BWB-44-006 — BWB CMS Inter-Bay Wiring QA Inspection

**Doc ID:** T-A-ATA44-BWB-EVI-006
**Evidence Type:** Inspection
**Delta Ref:** DELTA-BWB-44-004
**Req Refs:** BWB-44-100-005, BWB-44-000-003
**Standard:** CS-25.1353
**LC Gate:** LC06 (stub)
**Status:** STUB

---

## Inspection Objective

Verify BWB ATA 44 inter-bay harness routing compliance:
1. Harness segregation at spar bay penetrations (signal vs power)
2. Grommet/doubler condition and routing clearance
3. Bonding resistance at each ZC, BBU, and IBN installation site per bay
4. No single harness run crossing more than one spar bay boundary without a BBU

---

## Inspection Scope

| Item | Inspection method | Accept criteria |
|------|-----------------|----------------|
| Harness segregation at bay wall penetration | Visual | ≥25 mm separation (power/signal) |
| Grommet / doubler condition | Visual + dimensional | No damage; hole diameter within limits |
| Harness bend radius at each penetration | Dimensional | ≥10× cable OD |
| ZC bonding resistance (each bay) | Low-resistance ohmmeter | ≤2.5 mΩ |
| BBU bonding resistance (each boundary) | Low-resistance ohmmeter | ≤2.5 mΩ |
| IBN bonding resistance (each bay) | Low-resistance ohmmeter | ≤5.0 mΩ |
| Harness clamping and strain relief | Visual | No bare conductor; backshell within 50 mm of grommet |

---

## Related Documents

- [ICD_BWB_HARNESS_ROUTING_001.md](../ATA44_BWB_INTERFACES/ICD_BWB_HARNESS_ROUTING_001.md)
- [ACC_BWB_INSTALLATION_LIMITS.md](../ATA44_BWB_ACCEPTABILITY/ACC_BWB_INSTALLATION_LIMITS.md)
- [ATA 20 Standard Practices](../../../../ATA_20-STANDARD_PRACTICES/README.md)
- [WTW parallel](../../WTW/ATA44_WTW_VERIFICATION_EVIDENCE/INSPECTION_WTW_WIRING_QA.md)
