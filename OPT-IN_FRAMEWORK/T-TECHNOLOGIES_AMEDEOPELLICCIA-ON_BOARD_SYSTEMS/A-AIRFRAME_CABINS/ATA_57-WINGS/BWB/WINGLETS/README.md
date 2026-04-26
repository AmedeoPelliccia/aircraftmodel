# ATA 57 — Wings — BWB Winglets Sub-Area

**Domain:** T-TECHNOLOGIES / A-AIRFRAME_CABINS  
**Boundary:** BWB / WINGLETS (outboard wing-like region)  
**Doc ID:** T-A-ATA57-BWB-WGLT-001  
**Lifecycle:** WINGS_CUSTOM (LC57-01–LC57-13) — see `../LC57_PHASE_REGISTRY.yaml`  
**Status:** DRAFT  

## Scope
BWB winglet structural member spacing optimisation content for ATA 57 (Wings) for AMPEL360 Q100.
The winglets are an outboard wing-like region. "Ribs" and "stringers" may be used as structural
primitives with the following aliasing: `region: outboard` enables neutral member semantics
(member = rib or stringer depending on orientation).

This folder SHALL contain only WINGLETS-specific deltas. SHARED content remains in `../../`.
BWB LC57 lifecycle phases are defined in `../LC57_PHASE_REGISTRY.yaml` — do not duplicate.

## Structural Primitive Aliasing
The WINGLETS sub-area uses **neutral member primitives** to avoid geometry-specific naming:

| Primitive | Alias | Orientation | Notes |
|-----------|-------|-------------|-------|
| `member_spanwise` | rib | perpendicular to flow | chord-cutting member |
| `member_chordwise` | stringer | parallel to flow | span-running member |
| `region: outboard` | winglet section | η ≥ 0.85 | enables aliasing |

## Precedence
Type design basis > approved structural substantiation data > SHARED ATA57 > BWB overlay > WINGLETS sub-area > local WI

## Overlay Rules
- SHARED baseline location: `../../` (ATA_57 root)
- BWB LC57 lifecycle: `../LC57_PHASE_REGISTRY.yaml`
- This sub-area provides: **ΔARCH (member topology), ΔREQ (member spacing optimisation), ΔEVI (fatigue + divergence evidence)**
- Any member spacing register freeze SHALL be approved by Engineering and recorded in `ATA57_BWB_WINGLET_DELTA_LOG.yaml`

## Contents
- `ATA57_BWB_WINGLET_INDEX.yaml` — delta index (SSOT for WINGLETS deviations)
- `ATA57_BWB_WINGLET_DELTA_LOG.yaml` — auditable delta change log
- `SECONDARY_MEMBER_SPACING_OPT/` — member spacing 8-bit optimisation module:
  - `STD_MEMBER_SPACING_8BIT_ENCODING.md` — encoding standard for member spacing discretised to 8-bit registers
  - `CONSTRAINTS_FATIGUE_AND_DIVERGENCE.md` — fatigue life and aeroelastic divergence constraint definitions
  - `REQ_BWB_57_WINGLET_MEMBER_OPT.yaml` — structured requirements for member spacing optimisation
  - `MODELS/` — bay definitions, example register pack, solver configuration
  - `VERIFICATION_EVIDENCE/` — analysis and test evidence stubs

## Cross-References
- ATA 20 (standard practices — fasteners, repair, NDT)
- ATA 51/53/57 SHARED (structural interfaces, repair acceptability)
- BWB LC57 lifecycle: `../LC57_PHASE_REGISTRY.yaml`
- BLEND_ZONE sub-area: `../BLEND_ZONE/` (parallel BWB structural optimisation)
