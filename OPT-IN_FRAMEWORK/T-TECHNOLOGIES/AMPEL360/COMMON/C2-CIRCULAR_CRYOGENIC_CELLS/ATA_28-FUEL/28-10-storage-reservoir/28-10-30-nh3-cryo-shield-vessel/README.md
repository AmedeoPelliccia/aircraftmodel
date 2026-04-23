# ATA 28-10-30 — NH₃ Cryo-Shield Vessel

| Field | Value |
|---|---|
| **ATA-100 Slot** | 28-10 Storage |
| **PCT** | PCT-28-BWB |
| **STATUS** | **CONDITIONAL — pending trade study LC04** |

## Conditional placeholder

This subsection is reserved for an ammonia (NH₃) carrier path used as a
secondary prime material in the BWB architecture. Its inclusion is
**conditional** on the outcome of the LC04 trade study evaluating:

- NH₃ vs pure-LH₂ end-to-end mass and volume budget
- Cracker integration cost (see `28-20-30-nh3-cracker-h2-feed/`)
- Toxicity and double-containment certification path
- Ground infrastructure availability (see I-INFRASTRUCTURES IN-50)

If the trade study selects the NH₃-carrier path, this slot will host the
double-walled pressurised vessel design (≈10 bar, 298 K) with cryo-shield
interface. If the trade rejects NH₃, this directory will be removed and the
slot returned to `reserved`.

## Inputs awaited

| Input | Source | Phase |
|---|---|---|
| NH₃-path go/no-go decision | LC04 design review | LC04 |
| PEMFC inlet H₂ purity spec | ATA 47-40 | LC04 |
| Embrittlement model for NH₃ wetted parts | `28-70-30/` | LC05 |
