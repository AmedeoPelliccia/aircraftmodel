# EVI-BWB-44-004 — BWB ARINC 664 Per-Bay Network Conformance Test

**Doc ID:** T-A-ATA44-BWB-EVI-004
**Evidence Type:** Network Conformance Test
**Delta Refs:** DELTA-BWB-44-003, DELTA-BWB-44-005
**Req Ref:** BWB-44-100-003
**Standard:** ARINC 664 Part 7
**LC Gate:** LC07 (stub)
**Status:** STUB

---

## Test Objective

Demonstrate that each per-bay ARINC 664 (AFDX) cabin segment and its inter-bay
Bay Bridge Units (BBU) conform to ARINC 664 Part 7 for VL scheduling, latency,
and jitter.

## Test Scope

- Per-bay AFDX switch pair conformance (each segment SEG-01, SEG-02, SEG-03)
- BBU inter-domain bridge conformance (BBU-01, BBU-02)
- End-to-end latency across bays (ZC-01 → ZC-03 via BBU-01 + BBU-02)

## Test Cases

| Test ID | Description | Pass Criteria |
|---------|-------------|--------------|
| TC-BWB-44-701 | SEG-01 VL jitter at ZC-01 port | ≤ ARINC 664 P7 jitter limit |
| TC-BWB-44-702 | SEG-02 VL latency (ZC-02 to CSU-02A) | ≤ TBD ms |
| TC-BWB-44-703 | BBU-01 bridge latency (SEG-01 to SEG-02) | ≤ TBD ms |
| TC-BWB-44-704 | End-to-end latency ZC-01 → ZC-03 (2 bridges) | ≤ TBD ms |
| TC-BWB-44-705 | BBU failure isolation (BBU-01 disconnected) | SEG-01 and SEG-02 operate independently |

---

## Related Documents

- [ARCH_BWB_NETWORK_SEGMENTATION.md](../ATA44_BWB_ARCHITECTURE/ARCH_BWB_NETWORK_SEGMENTATION.md)
- [ICD_BWB_NETWORK_SEGMENTATION_001.md](../ATA44_BWB_INTERFACES/ICD_BWB_NETWORK_SEGMENTATION_001.md)
- [WTW parallel](../../WTW/ATA44_WTW_VERIFICATION_EVIDENCE/TEST_WTW_NETWORK_CONFORMANCE.md)
