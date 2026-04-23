# ATA 28-70 — Embrittlement Monitoring

| Field | Value |
|---|---|
| **ATA-100 Slot** | 28-70 Reserved (used as ATA-extension) |
| **PCT** | PCT-28-BWB |
| **BREX Extension** | Declared in BREX-IDA360-Q100-v0.1 — extension justification: H₂ embrittlement is a structural-degradation phenomenon with no analogue in legacy ATA-28 |
| **Status** | ACTIVE |

## Scope

Hydrogen-embrittlement monitoring of all wetted metallic parts in the
LH₂ system. Use of the reserved slot is **explicitly declared** in the
project BREX with extension justification.

## Subsections

| Slot | Title | Notes |
|---|---|---|
| `28-70-10-sensor-network/` | Strain / acoustic-emission / electrochemical sensors | |
| `28-70-20-inspection-criteria/` | Periodic NDI inspection programme | |
| `28-70-30-lifecycle-degradation-model/` | Cumulative-damage model, RUL prediction | |

## Interfaces

- ATA 51 (Structures) — material selection feedback
- `28-10-20-lh2-vacuum-insulated-tank/` — primary monitored component
- `28-20-20-lh2-transfer-and-valves/` — secondary monitored components
