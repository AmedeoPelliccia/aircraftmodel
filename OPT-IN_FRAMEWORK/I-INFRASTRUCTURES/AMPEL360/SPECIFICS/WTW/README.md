# WTW Infrastructure Scaffold

**Path:** `OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/AMPEL360/SPECIFICS/WTW/`

Configuration-specific ground infrastructure for the **AMPEL360 WTW** (Wide Tube & Wing) airframe — hydrogen-powered tube-and-wing variant (AMPEL-33).

## Scope

This directory holds WTW-only infrastructure artifacts that complement the shared [COMMON](../../COMMON/README.md) backbone. Content here covers:

| Area | Description |
|------|-------------|
| **08-I / 10-I WTW Overlays** | Jacking geometry, gate footprint, and GSE deltas for conventional tube-and-wing |
| **IN-40 WTW Overlay** | Airport civil-works adaptations for WTW wingspan and gear geometry |
| **Caudal Cryo-Bay Access** | Platforms, maintenance stands, and entry procedures for the aft LH₂ / NH₃ bay |
| **N₂ Inerting Ground Support** | Pre-flight purge, purity verification, and cracker ground-run procedures |
| **NH₃ Handling Infrastructure** | Storage, transfer, safety zoning, spill response, quality, and training for NH₃ GSE |
| **Turnaround Procedures** | Ground-ops turnaround profile and sequencing |

## Directory Convention

Every leaf area follows the **SSOT + PUB** pattern:

```
<AREA>/
├── SSOT/           ← Single Source of Truth (lifecycle data)
│   ├── LC01_PROBLEM_STATEMENT/
│   ├── LC02_SYSTEM_REQUIREMENTS/
│   ├── ...
│   └── LCnn_.../
└── PUB/            ← Publication outputs
    └── <MANUAL>/
        ├── CSDB/   ← S1000D Common Source DataBase
        │   ├── DM/  PM/  DML/  BREX/  ICN/  APPLICABILITY/
        ├── EXPORT/
        └── IETP/
```

## Relationship to COMMON

WTW-specific content **SHALL NOT** duplicate artifacts already maintained in `COMMON/`. Overlay KNOTs reference parent KNOTs in COMMON where applicable. Publication modules use S1000D applicability filtering (`A360-WTW`) to merge COMMON + overlay at render time.

---

*GQAOA .INC · 2026-04-15*
