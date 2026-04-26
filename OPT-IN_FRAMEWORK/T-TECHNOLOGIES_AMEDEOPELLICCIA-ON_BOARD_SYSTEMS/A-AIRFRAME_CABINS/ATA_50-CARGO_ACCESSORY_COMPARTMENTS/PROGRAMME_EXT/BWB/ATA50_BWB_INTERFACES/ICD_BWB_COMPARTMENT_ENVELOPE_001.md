# ICD-BWB-50-001 — Multi-Bay Flat-Deck Cargo Compartment Envelope

**Delta:** DELTA-BWB-50-001
**Programme:** AMPEL360 BWB
**ATA:** 50 — Cargo & Accessory Compartments
**Baseline ref:** ATA50-SHARED §3
**LC Gate:** LC03
**Status:** TBD

## 1. Scope

This ICD defines the BWB-specific cargo compartment envelope for the distributed
multi-bay flat-deck cargo architecture. Each structural bay is bounded by consecutive
spar webs and has its own envelope definition. Quantities marked TBD are locked at LC03.

## 2. BWB Delta Statement

**ΔICD vs. SHARED:** SHARED baseline defines a generic cargo volume envelope.
The BWB overlay redefines this as a per-bay table with spar-referenced coordinates
replacing the single WTW circular-cross-section belly-hold constraint.

## 3. Bay Envelope Table (per structural bay)

| Bay ID | Fwd Spar | Aft Spar | Floor Width (m) | Usable Height (m) | Net Volume (m³) |
|--------|----------|----------|-----------------|-------------------|-----------------|
| BAY-C1 | SPAR-2   | SPAR-3   | TBD             | TBD               | TBD             |
| BAY-C2 | SPAR-3   | SPAR-4   | TBD             | TBD               | TBD             |
| BAY-C3 | SPAR-4   | SPAR-5   | TBD             | TBD               | TBD             |
| BAY-C4 | SPAR-5   | SPAR-6   | TBD             | TBD               | TBD             |

Notes:
- Floor node coordinates referenced to aircraft datum (FS/BL/WL) at LC03.
- Net usable volume excludes structural members, wiring conduits and drain fittings.
- Maximum cargo density limit: TBD kg/m³ (LC05 structural loads confirm).

## 4. Envelope Constraints

- Floor flatness tolerance: ±TBD mm over any 1 m span (LC04).
- Ceiling clearance above cargo unit top: TBD mm minimum.
- Lateral spar web clearance: TBD mm minimum from cargo container edge.
- No cargo unit SHALL bridge more than one bay boundary (BWB-50-000-003).

## 5. Interface References

- ATA 53: Primary structure spar web defines bay boundaries.
- ATA 25: Cargo liner panels within this envelope — see DELTA-BWB-50-003.
- ATA 50-SHARED §3: Baseline cargo compartment requirements invoked by reference.
