# EVI-BWB-44-003 — BWB IFE Bay Node Flammability Test

**Doc ID:** T-A-ATA44-BWB-EVI-003
**Evidence Type:** Flammability Test
**Delta Ref:** DELTA-BWB-44-006
**Req Ref:** BWB-44-200-003
**Standard:** CS-25.853(a)
**LC Gate:** LC07 (stub — test reports at LC07)
**Status:** STUB

---

## Test Objective

Demonstrate that IFE Bay Node (IBN) LRU materials comply with CS-25.853(a)
flammability requirements for materials installed in the pressurised cabin.

## Test Article

- IBN LRU (all variants installed in BWB spar bays)
- All non-metallic materials per IBN BOM

## Test Method

Per FAA/EASA AC 25.853 / AMC 25.853 materials test specification.

## Test Cases

| Test ID | Material / Component | Method | Pass criteria |
|---------|---------------------|--------|--------------|
| TC-BWB-44-601 | IBN chassis / covers | 60-s vertical | Burn ≤152 mm; drip not continue burning |
| TC-BWB-44-602 | IBN internal wiring insulation | 60-s vertical | Per CS-25.853(a) |
| TC-BWB-44-603 | IBN mounting tray foam pad (if any) | 12-s vertical | Burn ≤76 mm |

---

## Related Documents

- [REQ_BWB_44_200_IFE.yaml](../ATA44_BWB_REQUIREMENTS/REQ_BWB_44_200_IFE.yaml)
- [WTW parallel](../../WTW/ATA44_WTW_VERIFICATION_EVIDENCE/TEST_WTW_IFE_FLAMMABILITY_853.md)
