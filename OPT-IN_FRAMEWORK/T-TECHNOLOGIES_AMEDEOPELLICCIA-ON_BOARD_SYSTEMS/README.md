# T-TECHNOLOGIES — AMEDEOPELLICCIA ON-BOARD SYSTEMS

**Programme Family:** AMPEL360 DB — Dual Branch (WTW + BWB)
**Alignment:** ATA iSpec 2200 · OPT-IN TLI v2.1
**Date:** 2026-02-23

This directory contains the shared-spine T-TECHNOLOGIES scaffold for all AMPEL360 on-board systems.
Boundaries are declared per IBD-001 Rev B: SHARED content lives here; FORKED content lives in programme repositories.

---

## Domain Index

| Code | Domain | Chapters |
|------|--------|----------|
| A | AIRFRAME_CABINS | ATA 20, 25, 44, 50, 51, 52, 53, 54, 55, 56, 57 |
| M | MECHANICS | ATA 27, 29, 32 |
| E1 | ENVIRONMENT | ATA 21, 26, 30, 35, 36, 37, 38, 47 |
| D | DATA | ATA 31, 45 |
| I | INFORMATION | ATA 46 |
| E2 | ENERGY | ATA 24, 49 |
| E3 | ELECTRICS | ATA 33, 39 |
| L1 | LOGICS (RESERVED) | — |
| L2 | LINKS | ATA 34 |
| C1 | COMMS | ATA 23 |
| C2 | CIRCULAR_CRYOGENIC_CELLS | ATA 28 |
| I2 | INTELLIGENCE | ATA 95, 97 |
| A2 | AVIONICS | ATA 22, 42 |
| O | OPERATING_SYSTEMS | ATA 40 |
| P | PROPULSION | ATA 60, 61, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80 |

---

## Boundary Legend

| Tag | Meaning |
|-----|---------|
| **SHARED** | Full technical content lives here (shared spine) |
| **FORKED** | Programme-specific — stub README + ICD pointers only |
| **MIXED** | Core scaffold SHARED here; programme extensions in forks |
| **RESERVED** | Placeholder only (no ATA chapter content yet) |

---

## Governing Rules

1. **SHARED** — may contain full technical content (specs, ICDs, models, DM scaffolds).
2. **FORKED** — SHALL contain **only** `README.md` (stub) + optional ICD pointer table.
3. **MIXED** — SHALL contain core scaffold + `PROGRAMME_EXT/` pointer stubs.
4. Every ATA directory SHALL contain `README.md`.

---

## Related Documents

- [IBD-001 Rev B](../../../SSOT/LC04_DESIGN_REVIEW/AMPEL360-FAM-IBD-001-RevB.md)
- [OPT-IN Framework README](../../README.md)
