# ATA 57 BWB — Blend Zone TDF Secondary Module

**Doc ID:** T-A-ATA57-BWB-BLEND-TDF-001  
**Parent:** `../` (BLEND_ZONE)  
**Status:** DRAFT  

## Scope
Secondary module for Blend Zone **Topological Design Field (TDF) Optimisation**.

The BWB blend zone is a transition structural field between the centre body and the outboard wing.
It does not decompose into ribs and frames. Instead, it is modelled as a patch grid where each patch
carries an 8-bit structural register encoding normalised density/thickness.

## Contents
- `STD_TDF_8BIT_ENCODING.md` — encoding standard: register → physical parameter mapping
- `CONSTRAINTS_FATIGUE_AND_DIVERGENCE.md` — fatigue life and aeroelastic divergence constraint definitions
- `REQ_BWB_57_BLEND_TDF_OPT.yaml` — structured requirements (IDs `BWB-57-TDF-001`–`005`)
- `MODELS/` — patch grid definition, example register map, solver configuration
- `VERIFICATION_EVIDENCE/` — analysis stubs (fatigue, divergence) and determinism test stub

## Key Design Rules
1. **No rib/frame primitives** in the blend zone — TDF patches are the atomic structural unit.
2. **8-bit register** per patch: values 0–255 mapped to physical parameter range (see `STD_TDF_8BIT_ENCODING.md`).
3. **Boundary conditions**: registers at structural hard-points (spar carry-through, pressure floor attach, systems hard-points) are **fixed** (not optimisable).
4. **Fatigue constraint**: every patch ≥ 80,000 flight cycles (Miner's Rule, CFRP B-basis).
5. **Divergence constraint**: V_div ≥ 1.15 × VD (CS-25.629(d)) on DLM eigenvalue of blend zone stiffness matrix.
6. **Determinism**: same inputs → same register map; SHA-256 hash recorded per run.
