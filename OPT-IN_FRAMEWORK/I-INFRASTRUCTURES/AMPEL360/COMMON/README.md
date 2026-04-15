# I-INFRASTRUCTURES / AMPEL360 / COMMON

**Shared Ground Infrastructure for WTW and BWB Configurations**

| Metadata | Value |
|----------|-------|
| **Document ID** | GQAOA-INFRA-A360-COMMON-001 |
| **Version** | v1.0-draft |
| **Status** | Normative |
| **Scope** | AMPEL360 WTW (Wide Tube & Wing) · AMPEL360 BWB (Blended Wing Body) |
| **OPT-INS axis** | I — Infrastructures |
| **VENTURE layer** | V1 (Scaffold) + V5 (Publication) + V6 (Governance) |
| **UTA chapters** | ATA 03-I, 08-I, 10-I, 12-I, 85-I, IN-XX |
| **Last Updated** | 2026-04-15 |

---

## 1. Rationale

The AMPEL360 programme develops two airframe morphologies from a shared technological nucleus:

| Configuration | ID | Airframe | Certification path | Quantum |
|---------------|------|----------|-------------------|---------|
| **AMPEL360 WTW** | AMPEL-33 | Wide tube-and-wing (≥3.5 m dia.) | Near-term (CS-25 conventional + SC hydrogen) | Classical + selective QKD |
| **AMPEL360 BWB** | AMPEL-34 | Blended wing body | Long-term (CS-25 + novel type cert.) | Full quantum-enhanced |

Despite fundamental differences in airframe geometry, both configurations share a **single hydrogen propulsion philosophy** (H₂ PEM fuel cells + turbofan hybrid), a **single energy carrier** (LH₂), and a **single operational ecosystem** (airports, MROs, supply chains, training organisations).

**The ground does not care about wing shape.** It cares about:

- how hydrogen arrives, is stored, and is transferred to the aircraft,
- how the aircraft is serviced, parked, and maintained,
- how technicians are trained and certified,
- how data flows between the aircraft and ground systems.

This document defines the **common infrastructure backbone** — the I-axis content that is configuration-invariant and maintained once for both WTW and BWB.

---

## 2. Commonality Assessment

### 2.1 Infrastructure Chapter Map

| UTA Chapter | System | WTW | BWB | Common? | Notes |
|-------------|--------|-----|-----|---------|-------|
| **03-I** | Support infrastructure | Yes | Yes | **FULL** | Ground handling philosophy identical |
| **08-I** | Leveling & weighing infra | Yes | Yes | **PARTIAL** | Jacking points differ; GSE metrology common |
| **10-I** | Parking, mooring, storage, RTS | Yes | Yes | **PARTIAL** | Footprint differs; tie-down, utilities common |
| **12-I** | Servicing infra | Yes | Yes | **FULL** | H₂ refueling, fluid servicing identical |
| **85-I** | Fuel cell systems infra | Yes | Yes | **FULL** | Test rigs, bench infra, spares enablement |
| **IN-10** | H₂ production & sourcing | Yes | Yes | **FULL** | Same fuel spec, same sourcing chain |
| **IN-20** | Liquefaction, compression, storage | Yes | Yes | **FULL** | Same cryogenic infrastructure |
| **IN-30** | Transport logistics & delivery | Yes | Yes | **FULL** | Same tanker fleet, same last-mile |
| **IN-40** | Airport facilities & permits | Yes | Yes | **PARTIAL** | Civil works adapt to wingspan/footprint |
| **IN-50** | H₂ GSE, couplings, interfaces | Yes | Yes | **FULL** | Single refueling interface standard |
| **IN-60** | Safety zoning & emergency | Yes | Yes | **FULL** | Same H₂ hazard radii, same procedures |
| **IN-70** | Quality assurance & metering | Yes | Yes | **FULL** | Same fuel purity spec, same sampling |
| **IN-80** | Digital traceability & DPP | Yes | Yes | **FULL** | Same ledger, same DPP schema |
| **IN-90** | Tables, schemas, index | Yes | Yes | **FULL** | — |

### 2.2 Summary

| Category | Count | Percentage |
|----------|-------|------------|
| **FULL** common | 11 chapters | 79% |
| **PARTIAL** common | 3 chapters | 21% |
| Configuration-specific only | 0 chapters | 0% |

**Every infrastructure chapter has a common component.** Three chapters carry configuration-specific overlays for geometric differences (jacking/leveling, parking footprint, airport civil works).

---

## 3. Common Infrastructure Architecture

### 3.1 The H₂ Supply Chain (IN-10 through IN-80)

This is the backbone — entirely configuration-invariant. The hydrogen supply chain does not see the aircraft; it sees a **fuel port interface**.

```
IN-10 Production         IN-20 Liquefaction       IN-30 Transport
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ Green H₂     │───▶│ Liquefier    │───▶│ LH₂ tanker   │
│ Electrolyser │    │ (20 K, 1 bar)│    │ road/rail/    │
│ Solar/Wind   │    │              │    │ pipeline      │
└──────────────┘    └──────────────┘    └──────┬───────┘
                                               │
                    IN-40 Airport               ▼
                    ┌──────────────┐    ┌──────────────┐
                    │ Civil works  │    │ Airport LH₂  │
                    │ Permits      │◀───│ storage farm  │
                    │ Safety zones │    │ (IN-20 cont.) │
                    └──────────────┘    └──────┬───────┘
                                               │
         IN-60 Safety     IN-50 GSE            ▼
         ┌──────────┐    ┌──────────────┐    ┌──────────────┐
         │ Hazard   │◀──▶│ Bowser/hydrant│───▶│ AIRCRAFT     │
         │ zones    │    │ Couplings    │    │ fuel port    │
         │ Emergency│    │ Hoses, purge │    │ (ATA 28-20)  │
         └──────────┘    └──────────────┘    └──────────────┘
                                               │
         IN-70 QA         IN-80 Digital        ▼
         ┌──────────┐    ┌──────────────┐    ┌──────────────┐
         │ Fuel spec│    │ DPP ledger   │    │ Aircraft DPP │
         │ Sampling │    │ ATA 96       │    │ (on-board)   │
         │ Metering │    │ Hash chain   │    │              │
         └──────────┘    └──────────────┘    └──────────────┘
```

**Key invariant:** The refueling interface (IN-50) is a single standard regardless of airframe. Both WTW and BWB use the same:

- LH₂ coupling type and diameter
- Purge/inert gas sequence
- Flow rate and pressure envelope
- Fuel purity specification (ISO 14687 / SAE AS6968)
- Grounding and bonding protocol
- Emergency disconnect mechanism

### 3.2 Fuel Cell Infrastructure (85-I)

Also fully common. The PEM fuel cell stacks are the same technology for both configurations — only the number of stacks and their spatial installation differ (on-board, not infrastructure).

| 85-I Section | Content | Common? |
|-------------|---------|---------|
| 85-10 Test rigs & bench | Stack acceptance test rigs, endurance benches | **FULL** |
| 85-20 H₂ handling safety | Permits, ventilation, leak detection for FC maintenance | **FULL** |
| 85-30 Power interface racks | Load banks, inverter test rigs, HV safety | **FULL** |
| 85-40 Thermal management test | Coolant loop test benches, radiator rigs | **FULL** |
| 85-50 Maintenance tooling & GSE | FC extraction tools, module handling, calibration | **FULL** |
| 85-60 Spares & warehouse | FC module spares, repair warehouse enablement | **FULL** |
| 85-70 Training & certification | FC technician qualification, safety cert | **FULL** |
| 85-80 Digital traceability | FC DPP, operating hours, degradation data | **FULL** |

### 3.3 Servicing Infrastructure (12-I)

Common. The aircraft is serviced through standardized ground service points:

| 12-I Section | Content | Common? |
|-------------|---------|---------|
| 12-10 Replenishing equipment | LH₂ bowser, potable water, hydraulic fluid rigs | **FULL** |
| 12-20 Scheduled servicing enablement | Daily/weekly check facilities, lighting, access | **FULL** |
| 12-30 Unscheduled servicing enablement | AOG response equipment, mobile maintenance | **FULL** |

### 3.4 Partially Common Chapters

These carry a **common core** plus **configuration overlays**:

#### 08-I Leveling & Weighing Infrastructure

| Section | Common core | WTW overlay | BWB overlay |
|---------|------------|-------------|-------------|
| 08-30 GSE equipment & tooling | Scales, load cells, data loggers | Conventional tripod jacks | Wide-body cradle jacks, wing support stands |
| 08-40 Metrology & calibration | Calibration protocols, certificate mgmt | Standard laser tracker targets | Custom BWB reference datum targets |
| 08-50 Facility readiness | Hangar floor spec, level surfaces | Standard hangar door width | Wide-span hangar door (≥50 m) |
| 08-60 Safety zoning | Exclusion zones during weighing | Standard zones | Extended zones (wider footprint) |
| 08-70 Training & competency | Weighing crew certification | — | BWB-specific procedures addendum |
| 08-80 Digital logs & traceability | W&B database, export formats | — | — |

#### 10-I Parking, Mooring, Storage, RTS

| Section | Common core | WTW overlay | BWB overlay |
|---------|------------|-------------|-------------|
| 10-10 Parking & storage facilities | Apron surface spec, lighting, markings | ICAO Code C/D gate geometry | Non-standard gate geometry (wider, shallower) |
| 10-20 Mooring, tie-down, stands | Tie-down anchors, nose wheel chock | Standard tow bar interface | Custom tow bar adapter (nose gear geometry) |
| 10-30 Return-to-service enablement | RTS checklist infrastructure, MEL support | — | — |

#### IN-40 Airport Facilities, Civil Works, Permits

| Section | Common core | WTW overlay | BWB overlay |
|---------|------------|-------------|-------------|
| IN-40-10 Apron & taxiway | LH₂-compatible surface coatings, drainage | Standard pavement classification | Reinforced pavement for distributed gear loading |
| IN-40-20 Hydrant system | Cryogenic piping, insulation, valve stations | Standard pit spacing | Adjusted pit spacing (fuel port location) |
| IN-40-30 Passenger boarding | Jet bridge interface standards | Single-aisle bridge | Multi-door boarding (BWB cabin geometry) |
| IN-40-40 Cargo loading | ULD handling systems | Standard cargo door position | Rear/ventral cargo access adaptation |
| IN-40-50 Permits & regulatory | H₂ zoning permits, local authority liaison | — | Novel-type facility permit addendum |

---

## 4. SSOT + PUB Pattern (Common Nodes)

Every common infrastructure chapter carries the canonical scaffold:

```
I-INFRASTRUCTURES/AMPEL360/COMMON/
├── README.md                                    ← This document
│
├── ATA_03-I_SUPPORT_INFRA/
│   └── COMMON/
│       ├── SSOT/
│       │   ├── LC01_PROBLEM_STATEMENT/
│       │   │   ├── KNOTS.csv
│       │   │   ├── KNU_PLAN.csv
│       │   │   ├── TIMELINE.csv
│       │   │   ├── RACI.csv
│       │   │   ├── TOKENOMICS_TT.yaml
│       │   │   └── AWARDS_TT.csv
│       │   ├── LC02–LC14 ...
│       │   └── ...
│       └── PUB/
│           └── GSE_MANUAL/
│               ├── CSDB/ (DM/PM/DML/BREX/ICN/APPLICABILITY)
│               ├── EXPORT/
│               └── IETP/
│
├── ATA_12-I_SERVICING_INFRA/
│   └── COMMON/
│       ├── SSOT/ ...
│       └── PUB/ ...
│
├── ATA_85-I_FUEL_CELL_SYSTEMS_INFRA/
│   └── COMMON/
│       ├── SSOT/ ...
│       └── PUB/ ...
│
├── ATA_IN_H2_GSE_AND_SUPPLY_CHAIN/
│   └── COMMON/
│       ├── IN-10_H2_PRODUCTION/
│       │   ├── SSOT/ ...
│       │   └── PUB/ ...
│       ├── IN-20_LIQUEFACTION/
│       │   ├── SSOT/ ...
│       │   └── PUB/ ...
│       ├── IN-30_TRANSPORT/
│       │   ├── SSOT/ ...
│       │   └── PUB/ ...
│       ├── IN-50_H2_GSE/
│       │   ├── SSOT/ ...
│       │   └── PUB/ ...
│       ├── IN-60_SAFETY_ZONING/
│       │   ├── SSOT/ ...
│       │   └── PUB/ ...
│       ├── IN-70_QUALITY_ASSURANCE/
│       │   ├── SSOT/ ...
│       │   └── PUB/ ...
│       └── IN-80_DIGITAL_TRACEABILITY/
│           ├── SSOT/ ...
│           └── PUB/ ...
│
├── ATA_08-I_LEVELING_WEIGHING_INFRA/
│   ├── COMMON/                                  ← Shared core
│   │   ├── SSOT/ ...
│   │   └── PUB/ ...
│   ├── WTW_OVERLAY/                             ← WTW-specific jacking & datum
│   │   ├── SSOT/ ...
│   │   └── PUB/ ...
│   └── BWB_OVERLAY/                             ← BWB-specific cradle & datum
│       ├── SSOT/ ...
│       └── PUB/ ...
│
├── ATA_10-I_PARKING_MOORING_STORAGE_RTS_INFRA/
│   ├── COMMON/
│   │   ├── SSOT/ ...
│   │   └── PUB/ ...
│   ├── WTW_OVERLAY/
│   │   ├── SSOT/ ...
│   │   └── PUB/ ...
│   └── BWB_OVERLAY/
│       ├── SSOT/ ...
│       └── PUB/ ...
│
└── ATA_IN-40_AIRPORT_FACILITIES/
    ├── COMMON/
    │   ├── SSOT/ ...
    │   └── PUB/ ...
    ├── WTW_OVERLAY/
    │   ├── SSOT/ ...
    │   └── PUB/ ...
    └── BWB_OVERLAY/
        ├── SSOT/ ...
        └── PUB/ ...
```

### 4.1 Overlay Rules

1. **COMMON** content is the SSOT. It is authored and maintained once.
2. **Overlays** (WTW_OVERLAY, BWB_OVERLAY) contain only delta content — what differs from COMMON.
3. Overlays **SHALL NOT** duplicate content already in COMMON.
4. Publication modules (PM) in PUB apply S1000D **applicability filtering** (ACT/PCT) to merge COMMON + overlay content at render time. The technician sees one manual; the CSDB maintains one truth with applicability tags.
5. KNOTs in overlays reference parent KNOTs in COMMON where applicable.
6. TT pools in overlays draw from the same programme-level allocation — no double-counting.

### 4.2 Applicability Model

The CSDB uses PCT (Product Cross-reference Table) to distinguish configurations:

| Product ID | Configuration | Description |
|-----------|---------------|-------------|
| `A360-WTW` | AMPEL360 Wide Tube & Wing | AMPEL-33 hydrogen tube-and-wing |
| `A360-BWB` | AMPEL360 Blended Wing Body | AMPEL-34 hydrogen BWB |
| `A360-ALL` | Both configurations | Common content |

Data modules carry applicability annotations:

```xml
<applic>
  <displayText>
    <simplePara>All AMPEL360 configurations</simplePara>
  </displayText>
  <assert applicPropertyIdent="model" applicPropertyType="prodattr"
          applicPropertyValues="A360-WTW A360-BWB"/>
</applic>
```

Overlay DMs carry configuration-specific applicability:

```xml
<applic>
  <displayText>
    <simplePara>AMPEL360 BWB only</simplePara>
  </displayText>
  <assert applicPropertyIdent="model" applicPropertyType="prodattr"
          applicPropertyValues="A360-BWB"/>
</applic>
```

---

## 5. Key Common Standards & Specifications

| Standard | Scope | Applicability |
|----------|-------|---------------|
| ISO 14687 | Hydrogen fuel quality | Both (fuel spec is aircraft-independent) |
| SAE AS6968 | Hydrogen purity for aviation | Both |
| ISO 13985 | LH₂ land vehicle fuel tanks | Supply chain (tankers) |
| EN 17127 | Hydrogen refueling protocols | Both (ground interface) |
| ICAO Annex 14 | Aerodrome design | Both (gate geometry diverges per config) |
| NFPA 2 | Hydrogen technologies code | Both (safety zoning) |
| SAE ARP4761 | Safety assessment | Both (infra safety cases) |
| IEC 62282 | Fuel cell technologies | Both (FC test infrastructure) |
| ISO 19880 | Gaseous hydrogen fueling stations | Both (adapted for LH₂) |

---

## 6. KNOT Register (Common Infrastructure)

Seed KNOTs for the common infrastructure backbone:

| KNOT ID | Title | Scope | Status | Residual | Owner |
|---------|-------|-------|--------|----------|-------|
| KNOT-IN-10-00-001 | Green H₂ sourcing pathway | Electrolyser capacity vs programme demand forecast | OPEN | 85 | STK_SE |
| KNOT-IN-20-00-001 | Airport LH₂ storage sizing | Tank farm capacity for dual-config turnaround | OPEN | 90 | STK_SE |
| KNOT-IN-30-00-001 | LH₂ last-mile delivery mode | Road tanker vs pipeline vs on-site production | OPEN | 80 | STK_OPS |
| KNOT-IN-50-00-001 | Universal refueling interface | Single coupling standard for WTW + BWB fuel ports | OPEN | 70 | STK_SE |
| KNOT-IN-50-00-002 | Refueling flow rate target | Target fill rate for ≤25 min turnaround | OPEN | 75 | STK_OPS |
| KNOT-IN-60-00-001 | H₂ safety exclusion radius | Regulatory acceptance of reduced safety zones | OPEN | 85 | STK_SAF |
| KNOT-85I-10-00-001 | FC bench test standardization | Common test rig spec for 150 kW PEM stacks | OPEN | 60 | STK_TEST |
| KNOT-85I-70-00-001 | FC technician certification | Training syllabus and competency framework | OPEN | 75 | STK_SE |
| KNOT-08I-30-00-001 | Jacking GSE commonality | Max common jacking equipment across configs | OPEN | 65 | STK_SE |
| KNOT-10I-10-00-001 | Gate geometry harmonization | ICAO code adaptation for BWB footprint | OPEN | 80 | STK_OPS |
| KNOT-IN-40-30-001 | Boarding bridge adaptation | Multi-door boarding concept for BWB | OPEN | 90 | STK_OPS |

---

## 7. TT Allocation (Common Pool)

```yaml
infrastructure_common_pool:
  programme: AMPEL360
  scope: "COMMON (WTW + BWB shared)"
  pool_tt: 50_000_000
  pool_deg: 18_000_000_000
  
  sub_allocation:
    IN_H2_supply_chain:  20_000_000 TT   # 40% — largest uncertainty, longest lead
    FC_infrastructure:   10_000_000 TT   # 20%
    servicing_infra:      5_000_000 TT   # 10%
    support_infra:        3_000_000 TT   #  6%
    leveling_weighing:    4_000_000 TT   #  8% — includes overlay work
    parking_mooring:      4_000_000 TT   #  8%
    airport_facilities:   4_000_000 TT   #  8% — includes overlay work
  
  overlay_policy:
    method: "shared_pool_with_config_tags"
    note: >
      Overlay KNUs draw from the same pool as COMMON.
      TT rewards carry a config tag (WTW/BWB/ALL) for audit,
      but the pool is not split. This incentivizes common solutions.
```

---

## 8. Relationship to VENTURE

VENTURE (GQAOA-ARCH-VENTURE-001) declares that infrastructure is part of the **common nucleus** shared between civil and defence missions. Within the AMPEL360 programme, this extends further: infrastructure is also shared between **airframe configurations** within the same programme.

The inheritance chain:

```
VENTURE (civil ∩ defence)
 └── AMPEL360 I-axis (programme-level infrastructure)
      └── COMMON (WTW ∩ BWB)
           ├── WTW_OVERLAY (delta only)
           └── BWB_OVERLAY (delta only)
```

This means AMPEL360 COMMON infrastructure artifacts are VENTURE-compliant by construction. A future defence variant (e.g., AMPEL360-MPA maritime patrol) would inherit the same COMMON backbone and add its own overlay.

---

## 9. Implementation Checklist

Any AMPEL360 infrastructure work package **SHALL**:

- [ ] Check if the content belongs in COMMON before creating a config-specific artifact
- [ ] Place common content in the COMMON directory, never in an overlay
- [ ] Tag all DMs with correct S1000D applicability (A360-ALL, A360-WTW, or A360-BWB)
- [ ] Register KNOTs with the common KNOT grammar
- [ ] Declare TT rewards against the common pool with config tags
- [ ] Ensure overlay content does not duplicate COMMON content
- [ ] Validate that PM assemblies correctly merge COMMON + overlay via PCT filtering

---

*GQAOA .INC · AI-assisted · 2026-04-15*
