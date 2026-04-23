# ATA 28-50 — H₂ Safety and Leak Detection

| Field | Value |
|---|---|
| **ATA-100 Slot** | 28-50 Reserved (used as ATA-extension) |
| **PCT** | PCT-28-BWB (28-50-20) · PCT-28-COMMON (28-50-10) |
| **BREX Extension** | Declared in BREX-IDA360-Q100-v0.1 — extension justification: H₂-specific safety function with no analogue in legacy ATA-28 |
| **Status** | ACTIVE |

## Scope

H₂-specific safety functions that have no canonical home in the legacy
ATA-28 sub-chapter map. Use of the reserved slot is **explicitly declared**
in the project BREX with extension justification per iSpec 2200 §3.9.5.

## Subsections

| Slot | Title | Applicability |
|---|---|---|
| `28-50-10-hydrogen-leak-sensors/` | Catalytic / semiconductor / fibre-optic leak sensors | BWB + WTW (H₂ paths) |
| `28-50-20-inerting-and-purge/` | Inerting (N₂) and purge sequences | BWB |

## Inter-ATA interfaces

- ATA 26 (Fire Protection) — leak event → isolation
- ATA 47 (Inert Gas / N₂) — purge gas supply
