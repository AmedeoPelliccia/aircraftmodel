# ATA 28-10-20 — LH₂ Vacuum-Insulated Tank

| Field | Value |
|---|---|
| **ATA-100 Slot** | 28-10 Storage |
| **PCT** | PCT-28-BWB |
| **Status** | ACTIVE |

## Scope

Cryogenic vessel for liquid hydrogen storage in the BWB hydrogen-hybrid
architecture. Inner vessel + vacuum jacket + multi-layer insulation (MLI)
with optional vapor-cooled shield (VCS).

### Key design parameters

| Parameter | Target |
|---|---|
| Storage temperature | 20 K |
| Operating pressure | 1–3 bar |
| Boil-off rate | ≤ 0.05 % mass/h |
| Gravimetric index | ≥ 0.40 |

### Interfaces

- Vacuum-jacket monitoring → `28-60-10-vacuum-jacket-monitoring/`
- Boil-off recovery → `28-60-30-boil-off-recovery-routing/`
- Quantity & state indicating → `28-40-10`, `28-40-20`
- Embrittlement monitoring → `28-70/`
