# ATA 57 BWB — Winglets Secondary Member Spacing Module

**Doc ID:** T-A-ATA57-BWB-WGLT-MSO-001  
**Parent:** `../` (WINGLETS)  
**Status:** DRAFT  

## Scope
Secondary module for BWB Winglet **Member Spacing Optimisation**.

The BWB winglet is an outboard wing-like region. Member spacing is optimised using discrete
8-bit registers per bay, with constraints from fatigue life and aeroelastic divergence.
Neutral member primitives (`member_spanwise`, `member_chordwise`) are used with `region: outboard`
aliasing to maintain geometry neutrality.

## Contents
- `STD_MEMBER_SPACING_8BIT_ENCODING.md` — encoding standard: register → physical spacing mapping
- `CONSTRAINTS_FATIGUE_AND_DIVERGENCE.md` — fatigue life and aeroelastic divergence constraint definitions
- `REQ_BWB_57_WINGLET_MEMBER_OPT.yaml` — structured requirements (IDs `BWB-57-WG-001`–`005`)
- `MODELS/` — bay definitions, example register pack, solver configuration
- `VERIFICATION_EVIDENCE/` — analysis stubs (fatigue, divergence) and determinism test stub

## Key Design Rules
1. **Neutral member primitives**: `member_spanwise` (rib alias) and `member_chordwise` (stringer alias).
   `region: outboard` enables these neutral names for the winglet domain.
2. **8-bit register** per bay: values 0–255 mapped to physical spacing range (see `STD_MEMBER_SPACING_8BIT_ENCODING.md`).
3. **Fixed registers**: tip cap, root attach zone, and access panel bay registers are **fixed**.
4. **Fatigue constraint**: every bay ≥ 80,000 flight cycles (Miner's Rule, CFRP B-basis γ = 2.0).
5. **Divergence constraint**: V_div ≥ 1.15 × VD (CS-25.629(d)) on DLM eigenvalue of winglet stiffness.
6. **Inboard boundary condition**: uses blend zone TDF output stiffness from `../BLEND_ZONE/` as inboard constraint.
7. **Determinism**: same inputs → same register map; SHA-256 hash recorded per run.
