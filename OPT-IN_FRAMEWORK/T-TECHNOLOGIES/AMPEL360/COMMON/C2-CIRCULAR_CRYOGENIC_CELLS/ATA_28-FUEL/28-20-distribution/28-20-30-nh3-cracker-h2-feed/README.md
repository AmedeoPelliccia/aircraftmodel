# ATA 28-20-30 — NH₃ Cracker H₂ Feed (Conditioning)

| Field | Value |
|---|---|
| **ATA-100 Slot** | 28-20 Distribution |
| **PCT** | PCT-28-BWB |
| **STATUS** | **CONDITIONAL — pending trade study LC04** |

## Conditional placeholder

This subsection covers the catalytic NH₃-cracker stage that conditions
NH₃ vapour into PEMFC-grade H₂ feed for the conversion stack. It is part
of the **NH₃-carrier path** and is **conditional** on the LC04 trade
study (see `28-10-30-nh3-cryo-shield-vessel/`).

The cracker is correctly placed under `28-20 Distribution` because, in
ATA semantics, *conditioning + transfer to conversion stack inlet* is a
distribution function, not an indicating function (which was the prior
incorrect mapping).

If the trade selects NH₃, expected content:

- Catalytic reactor design (Ru / Ni catalyst trade)
- Reformate H₂/N₂ separation membrane
- Inlet purity gate (PPM-level NH₃ slip control)
- Thermal coupling with `28-60-20-pre-cool-and-conditioning/`

## Inputs awaited

| Input | Source | Phase |
|---|---|---|
| NH₃-path go/no-go | LC04 design review | LC04 |
| PEMFC purity spec (CO, NH₃, H₂O ppm limits) | ATA 47-40 | LC04 |
| Catalyst supplier shortlist | LC05 procurement | LC05 |
