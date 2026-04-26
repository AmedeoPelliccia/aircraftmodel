# Member Spacing 8-Bit Register Encoding Standard — BWB Winglets

**Doc ID:** T-A-ATA57-BWB-WGLT-ENC-001  
**Status:** DRAFT  
**Applies to:** AMPEL360 BWB — ATA 57 Wings — Winglets

---

## 1. Purpose

This document defines the encoding standard for member spacing in the BWB winglet
optimisation. Each member bay is assigned an 8-bit integer register (0–255) encoding
a normalised spacing parameter. The same GA integer chromosome representation as the
WTW rib spacing (see WTW `STD_RIB_SPACING_ENCODING.md`) is used, adapted for the
winglet geometry and neutral member primitive semantics.

---

## 2. Member Primitive Aliasing

| Register domain | Physical primitive | Alias (`region: outboard`) | Orientation |
|---|---|---|---|
| `member_spanwise` | rib (in classical sense) | neutral member | perpendicular to chord |
| `member_chordwise` | stringer | neutral stringer | parallel to chord |

For span-direction spacing optimisation, only `member_spanwise` registers are optimised.

---

## 3. Physical Parameter Mapping

The 8-bit register encodes the **normalised bay spacing** `s_norm`:

```
s_norm = s_min + r × Δs
```

Where:
- `r` — register value (integer, 0–255)
- `s_min` — minimum bay spacing (TBD mm, defined at DDR-57-BWB)
- `Δs` — step size = (s_max − s_min) / 255

**Resolution:** 256 discrete values → approximately 5 mm per step (e.g., for a 1270 mm range between s_min and s_max).

---

## 4. Boundary Conditions

The following bay registers are **FIXED** (not subject to optimisation):

| Register Class     | Constraint         | Reason                                    |
|--------------------|--------------------|-------------------------------------------|
| `TIP_CAP`          | r = 0 (s_min)      | Tip cap structural closure bay            |
| `ROOT_ATTACH`      | r = 255 (s_max)    | Root attach zone — maximum stiffness      |
| `ACCESS_PANEL_BAY` | r ≥ 192            | Minimum panel bay size for access         |

---

## 5. Version-Freeze Rule

Member spacing registers are version-frozen at DDR-57-BWB (LC57-03). Changes require a
delta entry in `../ATA57_BWB_WINGLET_DELTA_LOG.yaml` and Engineering approval.
Each frozen register pack is identified by a SHA-256 hash.

---

## 6. Relationship to Blend Zone TDF

The winglet inboard boundary condition is the blend zone outboard stiffness from
`../BLEND_ZONE/SECONDARY_TOPOLOGY_FIELD_OPT/MODELS/tdf_register_map.example.yaml`.
This ensures structural continuity between blend zone and winglet at η ≈ 0.85.
