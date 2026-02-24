# ATA 44 BWB — Interfaces (ΔICD)

**Parent:** [BWB README](../README.md)

## Scope

BWB-specific interface control documents for ATA 44 Cabin Systems. These cover
the zonal boundaries, endpoint maps, harness envelopes, controller placement, and
bay bridge topology that differ from the SHARED ATA 44 baseline.

## Files

| File | ICD ID | Subject | Delta |
|------|--------|---------|-------|
| `ICD_LIST.yaml` | — | Master ICD register | — |
| `ICD_BWB_CONTROLLER_PLACEMENT_001.md` | ICD-BWB-44-001 | Distributed ZC placement per bay | DELTA-BWB-44-001 |
| `ICD_BWB_NETWORK_SEGMENTATION_001.md` | ICD-BWB-44-002 | Per-bay AFDX segments + BBU bridge topology | DELTA-BWB-44-003 |
| `ICD_BWB_NETWORK_ENDPOINTS_001.md` | ICD-BWB-44-003 | ARINC 664 VL/port register per bay | DELTA-BWB-44-005 |
| `ICD_BWB_HARNESS_ROUTING_001.md` | ICD-BWB-44-004 | Inter-bay harness routing envelope (spar bay penetrations) | DELTA-BWB-44-004 |
| `ICD_BWB_IFE_PLACEMENT_001.md` | ICD-BWB-44-005 | Distributed IFE Bay Node placement | DELTA-BWB-44-006 |
