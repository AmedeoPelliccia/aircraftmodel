# AMPEL360 — BWB Specifics (I-INFRASTRUCTURES)

**Path:** `OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/AMPEL360/SPECIFICS/BWB`

Configuration-specific enablement node for the **Blended Wing Body (BWB)** airframe
of the AMPEL360 Q100. This node captures BWB-unique engineering truth (SSOT) and
publishable deliverables (PUB) that cut across multiple ATA chapters and cannot be
cleanly owned by a single chapter.

> **Scope note.** Chapter-owned BWB content (e.g., fuselage shells under ATA-53,
> wings under ATA-57, stabilizers under ATA-55) remains in its canonical
> `T-TECHNOLOGIES/A-AIRFRAME_CABINS/**` location. This node holds
> **cross-chapter BWB specifics**: planform, centerbody topology, BLI propulsion
> integration, cabin egress geometry, and aeroelastic coupling.

## Layout

```
BWB/
├── README.md
├── SSOT/                         # Lifecycle engineering (LC01–LC12)
│   ├── LC01_PROBLEM_STATEMENT/   # KNOTs, KNUs, RACI, tokenomics (seeded)
│   └── LC02..LC12/               # Requirements → Reconditioning
├── PUB/
│   └── AMM/
│       ├── CSDB/                 # S1000D: DM / PM / DML / BREX / ICN / COMMON / APPLICABILITY
│       ├── EXPORT/               # Rendered PDF/HTML
│       └── IETP/                 # Runtime viewer/config
└── BWB-XX-*/                     # BWB-specific subject folders
    ├── BWB-00-general
    ├── BWB-10-planform-and-geometry
    ├── BWB-20-centerbody-structure
    ├── BWB-30-outboard-wing-integration
    ├── BWB-40-pressure-vessel-topology
    ├── BWB-50-control-surfaces-and-allocation
    ├── BWB-60-propulsion-integration-bli
    ├── BWB-70-cabin-layout-and-egress
    ├── BWB-80-aeroelastics-and-loads
    └── BWB-90-tables-schemas-index
```

## Entry points

| Need | Start here |
|---|---|
| Uncertainties / KNOTs | `SSOT/LC01_PROBLEM_STATEMENT/KNOTS.csv` |
| Planned KNUs | `SSOT/LC01_PROBLEM_STATEMENT/KNU_PLAN.csv` |
| Tokenomics pool | `SSOT/LC01_PROBLEM_STATEMENT/TOKENOMICS_TT.yaml` |
| RACI matrix | `SSOT/LC01_PROBLEM_STATEMENT/RACI.csv` |
| Publications | `PUB/AMM/CSDB/` |

## BWB subject folders

| Folder | Scope | ATA cross-refs |
|---|---|---|
| `BWB-00-general` | General BWB configuration overview | — |
| `BWB-10-planform-and-geometry` | Reference planform, sweep, span, twist | ATA-06 |
| `BWB-20-centerbody-structure` | Centerbody structural topology, frames, skins | ATA-53 |
| `BWB-30-outboard-wing-integration` | Outboard wing junction, carry-through | ATA-57 |
| `BWB-40-pressure-vessel-topology` | Non-cylindrical pressure cabin sizing | ATA-53 |
| `BWB-50-control-surfaces-and-allocation` | Elevon / split-flap allocation, hinge moments | ATA-27, ATA-55 |
| `BWB-60-propulsion-integration-bli` | BLI inlet, nacelle integration, wake ingestion | ATA-71, ATA-72 |
| `BWB-70-cabin-layout-and-egress` | Cabin geometry, emergency egress path length | ATA-25 |
| `BWB-80-aeroelastics-and-loads` | Body-freedom flutter, gust loads, mass coupling | ATA-05 |
| `BWB-90-tables-schemas-index` | Cross-reference tables, JSON schemas, index | — |

## Traceability

All artifacts in this node MUST cross-link to the owning ATA chapters (e.g.,
ATA-53 fuselage sections, ATA-57 wings, ATA-27 flight controls for elevon
allocation, ATA-72 for BLI propulsors). BREX validation enforces
dangling-reference checks.
