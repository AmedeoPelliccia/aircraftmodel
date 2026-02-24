# TEST — BWB Envelope Protection Test

**Evidence ID:** EV-BWB-22-004
**Doc ID:** T-A2-ATA22-BWB-TEST-002
**Delta Ref:** DELTA-BWB-22-003
**CS-25 Ref:** CS-25.143(f), CS-25.253, CS-25.337
**Method:** Simulator (boundary verification) + Flight test
**Status:** STUB
**Lifecycle:** Standard (LC01–LC13)
**Content Deferred To:** LC05 (simulator), LC06 (flight test)

---

## 1. Purpose

This test stub defines the scope and structure of BWB envelope protection testing. It covers delta test cases for the BWB-specific alpha/beta limits, load factor protection, and high-speed protection arising from DELTA-BWB-22-003. SHARED baseline envelope test cases are not repeated.

---

## 2. Test Programme Overview (Stub)

| Test Phase | Facility | Objective | LC Gate |
|---|---|---|---|
| Limit parameterisation verification | FCC bench | Verify protection limits loaded correctly from aerodynamic model tables | LC05 |
| Alpha protection — buffet onset | Simulator | Verify alpha protection activates at correct AoA before buffet onset | LC05 |
| Beta protection | Simulator | Verify beta limit protection within sideslip structural boundary | LC05 |
| Load factor protection | Simulator | Verify nz high/low protection at design limits | LC05 |
| High-speed protection | Simulator | Verify VMO/MMO protection with flutter margin | LC05 |
| Flight test — alpha protection | Aircraft | Confirm alpha protection behaviour in flight | LC06 |
| Flight test — high-speed | Aircraft | Confirm VMO/MMO protection with flutter clearance | LC06 |

---

## 3. Delta Test Cases (Stub)

### TC-BWB-22-EP-001: Alpha Protection — Soft Alert Trigger

| Field | Value |
|---|---|
| Test Case ID | TC-BWB-22-EP-001 |
| Delta Ref | DELTA-BWB-22-003 |
| Requirement | BWB-22-400-001 |
| Objective | Verify soft alpha alert activates at TBD deg below buffet onset (LC03) |
| Facility | FFS / simulator |
| Pass Criteria | EICAS caution generated at alpha = TBD (LC03); autoflight guidance target reduces AoA |
| Status | STUB |
| LC Gate | LC05 |

### TC-BWB-22-EP-002: Alpha Protection — Hard Limit

| Field | Value |
|---|---|
| Test Case ID | TC-BWB-22-EP-002 |
| Delta Ref | DELTA-BWB-22-003 |
| Requirement | BWB-22-400-001 |
| Objective | Verify hard alpha limit prevents aircraft from reaching BWB buffet onset AoA during autoflight |
| Facility | FFS / simulator |
| Pass Criteria | Alpha does not exceed TBD deg (LC03) in any autoflight mode; appropriate alert generated |
| Status | STUB |
| LC Gate | LC05 |

### TC-BWB-22-EP-003: Load Factor Protection (nz high)

| Field | Value |
|---|---|
| Test Case ID | TC-BWB-22-EP-003 |
| Delta Ref | DELTA-BWB-22-003 |
| Requirement | BWB-22-400-003 |
| Objective | Verify nz high limit prevents exceedance of structural design limit load factor |
| Facility | FFS / simulator |
| Pass Criteria | nz does not exceed TBD g (CS-25.337 limit, LC03) during autoflight manoeuvres |
| Status | STUB |
| LC Gate | LC05 |

### TC-BWB-22-EP-004: High-Speed Protection (VMO/MMO)

| Field | Value |
|---|---|
| Test Case ID | TC-BWB-22-EP-004 |
| Delta Ref | DELTA-BWB-22-003 |
| Requirement | BWB-22-400-002 |
| Objective | Verify VMO/MMO protection activates with BWB flutter margin and prevents speed exceedance |
| Facility | FFS at altitude |
| Pass Criteria | Speed does not exceed VMO/MMO + TBD kt/Mach during autoflight descent in idle/dive scenario |
| Status | STUB |
| LC Gate | LC05 |

### TC-BWB-22-EP-005: FDR Recording of Protection Engagements

| Field | Value |
|---|---|
| Test Case ID | TC-BWB-22-EP-005 |
| Delta Ref | DELTA-BWB-22-003 |
| Requirement | BWB-22-400-005 |
| Objective | Verify FDR records all protection engagement events with required parameters |
| Facility | FCC bench / simulator |
| Pass Criteria | Each protection engagement generates FDR entry with parameter, limit, and duration |
| Status | STUB |
| LC Gate | LC05 |

---

## 4. Flight Test Considerations

High-speed flutter flight test points require:
- Dedicated flutter clearance programme per CS-25.629
- Structural response instrumentation on composite panels
- Phased expansion to VMO/MMO per agreed flutter test plan

**Flutter test plan:** TBD (LC04) — separate from this autoflight test document.

---

## 5. Open Items

| Item | Description | LC Gate |
|---|---|---|
| OI-EP-001 | Populate all limit values from aerodynamic and structural analysis | LC03 |
| OI-EP-002 | Define full test matrix (weight, CG, altitude, speed coverage) | LC04 |
| OI-EP-003 | Coordinate high-speed flutter test plan with structures | LC04 |
| OI-EP-004 | Define FDR parameter list for protection recording | LC04 |
