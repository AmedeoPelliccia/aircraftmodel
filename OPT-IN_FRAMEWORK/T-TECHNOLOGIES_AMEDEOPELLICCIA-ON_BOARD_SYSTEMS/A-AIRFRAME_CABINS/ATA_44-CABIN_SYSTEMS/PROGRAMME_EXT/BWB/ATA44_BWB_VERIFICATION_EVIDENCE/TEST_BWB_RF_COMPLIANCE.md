# EVI-BWB-44-005 — BWB External Comm RF Compliance Test

**Doc ID:** T-A-ATA44-BWB-EVI-005
**Evidence Type:** RF Compliance Test
**Delta Ref:** DELTA-BWB-44-001 (antenna context, BWB fuselage OML)
**Req Ref:** BWB-44-300-002
**Standard:** ETSI EN 303 360
**LC Gate:** LC07 (stub)
**Status:** STUB

---

## Test Objective

Demonstrate RF emissions compliance at BWB-specific external antenna installations
on the composite BWB outer mould line.

> Δ BWB: BWB composite skin has different shielding characteristics vs WTW
> metallic/hybrid fuselage. RF compliance for each antenna installation position
> on the BWB lower surface must be verified.

## Test Scope

- Each external communication antenna position on BWB lower surface
- RF emission characterisation vs ETSI EN 303 360 limits
- Cabin composite skin shielding effectiveness measurement

## Test Cases

| Test ID | Antenna position | Frequency band | Pass criteria |
|---------|-----------------|---------------|--------------|
| TC-BWB-44-801 | Ext comm antenna 1 (Bay 1 lower) | TBD MHz | ETSI EN 303 360 limits |
| TC-BWB-44-802 | Ext comm antenna 2 (AFT lower) | TBD MHz | ETSI EN 303 360 limits |
| TC-BWB-44-803 | Composite skin shielding effectiveness | Broadband | ≥ TBD dB [LC05] |

---

## Related Documents

- [REQ_BWB_44_300_EXTERNAL_COMM.yaml](../ATA44_BWB_REQUIREMENTS/REQ_BWB_44_300_EXTERNAL_COMM.yaml)
- [WTW parallel](../../WTW/ATA44_WTW_VERIFICATION_EVIDENCE/TEST_WTW_RF_COMPLIANCE.md)
