# ATA 96-70 — Governance Policies and Rules

## Inheritance Boundary Change Requests (IBCRs)

Per AMPEL360-FAM-IBD-001 Rev B §8.4, any proposal to reclassify a SHARED
entry as FORKED (or vice versa) in the Inheritance Boundary Declaration
requires an IBCR reviewed by both programme Chief Engineers and approved
by the AMPEL360 Family Programme Manager.

IBCRs are logged in this directory.

### IBCR Template

| Field | Value |
|---|---|
| IBCR ID | IBCR-xxxx |
| Date | YYYY-MM-DD |
| Requestor | [Name / Role] |
| Boundary Entry | [OPT-IN Axis / ATA] |
| Current Designation | SHARED / FORKED / MIXED |
| Proposed Designation | SHARED / FORKED / MIXED |
| Rationale | [Description] |
| Impact Assessment | [Description] |
| CE-BWB Approval | [Pending / Approved / Rejected] |
| CE-WTW Approval | [Pending / Approved / Rejected] |
| Family PM Approval | [Pending / Approved / Rejected] |

### Register

No IBCRs have been filed to date.

---

## Linked Governance Specifications

| Specification | KNU | Location |
|---|---|---|
| GEN-MODEL Role Formal Specification | KNU-ATA96-70-001 | `SSOT/LC05_ANALYSIS_MODELS/LC05-GEN-MODEL-ROLE-SPEC.md` |
| Model Topology Invariance Proof Sketch | KNU-ATA96-70-002 | `SSOT/LC05_ANALYSIS_MODELS/LC05-TOPOLOGY-INVARIANCE-PROOF.md` |

The GEN-MODEL specification formalises the observer/delineant mode
separation for LC05 analysis models. Certified node deletion requires
an approved IBCR per the template above. See `.askm/delineant/gate-rules.yaml`
for certification coupling rules.
