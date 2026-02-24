# ATA 50 — Cargo & Accessory Compartments · PROGRAMME_EXT / WTW

**Overlay type:** WTW-only delta layer  
**Baseline reference:** `../../` (ATA_50-CARGO_ACCESSORY_COMPARTMENTS SHARED root)  
**Programme:** AMPEL360 WTW (Wide Tube & Wing) — EIS 2035–40  
**Status:** LC01 scaffold · all numerical limits TBD (gate LC03–LC06)

---

## 1. Overlay Scope

This directory contains **only** the WTW-specific deltas over the ATA 50 SHARED baseline. No
SHARED content is duplicated here. Each delta document references the affected baseline
section and states the WTW departure.

| Delta type | Folder / File |
|---|---|
| ΔICD — WTW-specific interfaces | `ATA50_WTW_INTERFACES/` |
| ΔREQ — WTW-only requirements | `ATA50_WTW_REQUIREMENTS/` |
| ΔACC — WTW acceptability deltas | `ATA50_WTW_ACCEPTABILITY/` |
| ΔEVI — WTW evidence stubs | `ATA50_WTW_VERIFICATION_EVIDENCE/` |

---

## 2. Named Deltas

| Delta ID | Subject | Baseline ref | LC gate |
|---|---|---|---|
| DELTA-WTW-50-001 | Circular fuselage belly-hold envelope constraints | §3 baseline | LC03 |
| DELTA-WTW-50-002 | Cargo access door geometry & latch/hinge ICD | §4 baseline | LC03 |
| DELTA-WTW-50-003 | Liner attachment rail/clip pattern (circular XS) | §5 baseline | LC04 |
| DELTA-WTW-50-004 | Drain & vent path in lower fuselage skin | §6 baseline | LC04 |
| DELTA-WTW-50-005 | Fire containment liner interfaces (CS-25.855/856) | §7 baseline | LC04 |
| DELTA-WTW-50-006 | Belly-hold net/restraint attach interfaces | §8 baseline | LC05 |

---

## 3. Master Index

See `ATA50_WTW_INDEX.yaml` for machine-readable delta registry.

---

## 4. Compliance Traceability

See `ATA50_WTW_COMPLIANCE_MATRIX.md` for CS-25 / regulatory requirement mapping.

---

## 5. Cross-References

| ATA | Topic |
|---|---|
| ATA 25 | Equipment & furnishings — cargo compartment furnishings |
| ATA 52 | Doors — cargo door structure |
| ATA 53 | Fuselage — belly-hold structural interface |
| ATA 57 | Wings — wing-to-fuselage fairing, lower access |
| ATA 20 | Standard practices — liner fastening, sealant |
