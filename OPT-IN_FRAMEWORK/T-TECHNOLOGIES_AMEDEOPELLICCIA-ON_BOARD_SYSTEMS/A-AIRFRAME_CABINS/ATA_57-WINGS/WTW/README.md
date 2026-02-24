# ATA 57 — Wings — WTW Variant Layer

**Domain:** T-TECHNOLOGIES / A-AIRFRAME_CABINS
**Boundary:** WTW (variant layer)
**Doc ID:** T-A-ATA57-WTW-001
**Lifecycle:** WINGS_CUSTOM (LC57-01–LC57-13)
**Status:** DRAFT

## Scope
WTW-specific content for ATA 57 (Wings) for AMPEL360 Q100.
This folder SHALL contain only WTW deltas and WTW-only methods; SHARED content remains in `../`.

## Precedence
Type design basis > approved structural substantiation data > SHARED ATA57 > WTW layer > local WI

Any deviation from SHARED wing standard practices SHALL be approved by Structural Engineering.

## Contents
- `LC57_PHASE_REGISTRY.yaml` — custom wing lifecycle phase definitions (LC57-01–LC57-13)
- `ATA57_WTW_INDEX.yaml` — delta index (SSOT for WTW deviations from SHARED baseline)
- `ATA57_WTW_DELTA_LOG.yaml` — auditable delta change log
- `MAINTENANCE/` — maintenance plan registry hook (spare/repair/supplier/circularity classification)
- `SECONDARY_RIB_SPACING_OPT/` — Wing Rib Spacing Optimisation secondary module

## Custom Lifecycle Phases
ATA 57 Wings employs extended lifecycle phases beyond the standard LC01–LC13 to capture wing-specific gate activities:

| Phase | ID      | Description |
|-------|---------|-------------|
| Conceptual | LC57-01 | Wing planform concept + aeroelastic trade space |
| Preliminary | LC57-02 | Structural layout, rib/spar bay count, material selection |
| Detailed | LC57-03 | Rib spacing optimisation, joint design, fatigue load cases |
| Stress Analysis | LC57-04 | FEM build, static/fatigue/damage-tolerance substantiation |
| Aeroelastic | LC57-05 | Flutter, divergence, aileron reversal margins |
| Manufacture | LC57-06 | Skin panel cure, spar assembly, rib attach fastening |
| Assembly | LC57-07 | Wing-box integration, control surface install |
| Systems | LC57-08 | Fuel/LH₂ systems integration, wiring routing |
| Structural Test | LC57-09 | Wing bending test, static/fatigue coupon campaigns |
| Flight Test | LC57-10 | Aeroelastic flight envelope expansion |
| Certification | LC57-11 | CS-25 Subpart C + Appendix J substantiation package |
| Production | LC57-12 | Production rate, tooling qualification |
| In-Service | LC57-13 | CPCP, repair classification, supplier circularity |

## Cross-References
- ATA 20 — Standard Practices (fasteners, surface treatments, NDT)
- ATA 51 — Structures – Standard Practices
- ATA 53 — Fuselage (wing-body attach)
- ATA 55 — Stabilisers (empennage structural standard)
- ATA 27 — Flight Controls (aileron/spoiler interface)
- ATA 28 — Fuel (wing tank structure interface)
