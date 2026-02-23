# PNR_BLOCKCHAIN_THREAD_POLICY.md
# Document ID: AMPEL360-FAM-ARCH-ELC-001-PNR
# Revision: B
# Date: 2026-02-23
# Parent Document: AMPEL360-FAM-ARCH-ELC-001 Rev B (§5 ELC Governance)
# Related Document: AMPEL360-FAM-ARCH-ELC-001-DET (Determinism Contract)
# Related Document: AMPEL360-FAM-ARCH-ELC-001-QCC (Qualifying Capacity Manifesto)

# PNR Blockchain Thread Policy

**AMPEL360-FAM-ARCH-ELC-001-PNR · Rev B · 2026-02-23**

---

> *«La inmutabilidad en blockchain debe entenderse en términos relativos:
> como capacidad de detección de alteraciones, integridad verificable
> y trazabilidad de modificaciones bajo políticas de consenso —
> no como permanencia metafísica absoluta.»*
>
> — *Fórmula redactable* derived from AEPD (2019/2020), "Blockchain (II):
> Conceptos básicos desde la protección de datos."

---

## Revision History

| Rev | Date       | Author Role           | Change Summary                                                    |
|-----|------------|-----------------------|-------------------------------------------------------------------|
| A   | 2026-02-23 | System Architect (SA) | Initial release — PNR Thread framework                            |
| B   | 2026-02-23 | System Architect (SA) | Add §10: Qualifying Capacity Authorization Model (ref QCC manifesto) |

---

## §1  Purpose & Doctrinal Position

This document governs the **PNR (Part Number Registry) Blockchain Thread** for
the AMPEL360 WTW programme. The Thread is the distributed evidence layer that
anchors cryptographic commitments at defined governance events across the ELC
(Elastic Lifecycle) framework.

### §1.1  Relative Immutability

The distributed ledger is a **neutral evidence layer**, NOT a guarantee of
absolute immutability.

Immutability is understood in **relative terms**:

- **Integrity detection**: any alteration to an anchored record is
  cryptographically detectable via hash comparison.
- **Verifiable integrity**: any party with the off-chain artefact and the
  on-chain commitment hash can independently verify the record has not been
  tampered with.
- **Modification traceability**: all corrections, supersessions, and
  revocations are themselves recorded, attributed, and consensus-validated —
  the chain of custody is complete.

This interpretation explicitly rejects **metaphysical permanence**. A
hash-anchored record CAN be superseded, corrected, or retired. Every record
carries a **validity state** (`ACTIVE`, `SUPERSEDED`, `REVOKED`, `EXPIRED`)
that is itself part of the auditable chain.

> The right of correction and the right of erasure are architecturally
> compatible with this framework: corrections are recorded as SUPERSEDED
> transitions; erasure rights are satisfied by off-chain data management
> without invalidating the on-chain commitment proof structure.

This position is normatively grounded in §2 (Normative References) below and
constitutes a **doctrinal correction** to any language in co-governed
artefacts that treats immutability as absolute (see §8 Relationship to
DETERMINISM\_CONTRACT).

### §1.2  Technological Neutrality

The PNR Thread is:

- **Portable**: not dependent on any specific ledger network, vendor, or
  consensus mechanism. The anchoring interface is an abstract commitment
  protocol, not an implementation.
- **Verifiable**: using open standards — SHA-256 hashing (FIPS 180-4),
  RFC 6979 deterministic signatures, and YAML/JSON canonical serialisation.
- **Interoperable**: alphanumeric PNR identifiers are ledger-agnostic. The
  Thread can be anchored to any of:
  - Ethereum (public or private PoS network)
  - Hyperledger Fabric (permissioned enterprise ledger)
  - A permissioned notary service
  - A simple append-only Git log (minimum viable implementation)

The choice of anchoring substrate is a programme configuration decision and
does not alter the policy semantics defined here.

### §1.3  Non-Dispersive Anchoring

The Thread enforces strict separation between on-chain and off-chain content:

| Layer | Content | Governance |
|-------|---------|------------|
| **On-chain (anchored)** | Cryptographic commitments only: hashes, validity states, freeze-point attestations, consensus timestamps, PNR identifiers | Immutable commitment proofs; state transitions via consensus |
| **Off-chain (governed)** | Method packages, design data, IP-sensitive content, family templates, compilation manifests, Supplier Evidence Packages | SSOT repository; governed by ELC framework |

**Prohibited on-chain**:

- Engineering content or technical specifications
- Trade secrets or proprietary design data
- Personally identifiable information (PII)
- Supplier commercial data

**Mandatory**: Role identifiers are used instead of personal names for all
on-chain records, ensuring data protection compliance from inception.

---

## §2  Normative References

The following documents constitute normative authority for this policy.
Compliance with the principles they establish is mandatory.

| Ref ID | Document | Relevance | URL |
|--------|----------|-----------|-----|
| **NR-01** | AEPD (2019/2020). "Blockchain (II): Conceptos básicos desde la protección de datos." Agencia Española de Protección de Datos. | Establishes that immutability in blockchain must be understood relatively: as integrity detection and traceability under governance, not absolute permanence. Grounds §1.1 of this policy. | <https://www.aepd.es/prensa-y-comunicacion/blog/blockchain-II-conceptos-basicos-proteccion-de-datos> |
| **NR-02** | AEPD (2024). Technical note on blockchain and the right to erasure — proof of concept showing that commitment on-chain / data off-chain architecture is compatible with data protection rights. Agencia Española de Protección de Datos. | Grounds §1.3 Non-Dispersive Anchoring and §9 Data Protection & IP Safeguards. Confirms architectural compatibility of on-chain/off-chain split with GDPR erasure rights. | <https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/la-aepd-publica-una-nota-tecnica-en-relacion-con-blockchain-y> |
| **NR-03** | BOE RD 4/2010. Real Decreto 4/2010, Esquema Nacional de Interoperabilidad (ENI), Artículo 11 — Principio de neutralidad tecnológica y adaptabilidad. | Establishes the principle of technological neutrality and use of open standards for interoperability. Grounds §1.2 of this policy. | <https://www.boe.es/buscar/doc.php?id=BOE-A-2010-1331> |

---

## §3  Activation Model: Supplier Lines On-Demand

The Thread activates at defined trigger points when governance scope is
entered, and deactivates when that scope is satisfied. Activation is
**on-demand** — the Thread is not continuously active; it opens for specific
events and closes when evidence is captured and verified.

### §3.1  Activation Triggers

| Trigger | Event Type | PNR Event Code | Thread State |
|---------|-----------|----------------|--------------|
| Freeze Point passage (FP-01 → FP-05) | Interface/architecture milestone | `FP01` … `FP05` | Opens STL if supplier involvement; records commitment |
| ELC Compilation event | Compiler run producing new manifest | `COMP` | Records compile\_hash commitment |
| ADR approval (triggers recompilation) | Architectural Decision Record approved | `ADR` | Records ADR commitment; opens recompilation scope |
| Gate evaluation (SLC phase exit) | SLC lifecycle gate passed | `GATE` | Records gate outcome; drift check anchored |
| Supplier qualification event | Supplier quality evidence package accepted | `SQUAL` | Closes STL for supplier; records SEP Merkle root |
| Reconditioning cycle (SLC11 exit) | MRO reconditioning complete, re-entry | `RECOND` | Records reconditioning commitment; re-activates as needed |

### §3.2  Deactivation

A Thread line deactivates when:

1. The triggering scope is closed (STL\_CLOSE event recorded, §4), OR
2. The validity state transitions to `EXPIRED` due to supersession or
   programme phase exit.

---

## §4  Supplier Thread Lines (STL)

Supplier Thread Lines formalise the handshake between the OEM and suppliers
for evidence capture. Each STL has exactly three lifecycle events, making
non-dispersion demonstrable end-to-end.

### §4.1  STL Lifecycle Events

#### Event 1: `STL_OPEN`

Opens the scope and temporal window for a supplier evidence capture cycle.

**Records on-chain**:

```yaml
stl_open:
  pnr_id: "PNR:A360:C:STL:00001"
  event_type: "STL_OPEN"
  anchored_at: "2026-02-23T10:00:00Z"
  stl_id: "STL-A360-C-ATA28-001"
  supplier_role_id: "SUP-ROLE-ATA28-CRYO-001"
  family_code: "C"
  ata_chapter: "ATA-28"
  trigger_event: "FP-01"
  scope_description: "H2 cryo system ICD freeze evidence capture"
  temporal_window:
    opens: "2026-02-23T10:00:00Z"
    closes_no_later_than: "2026-04-30T23:59:59Z"
  consensus_proof:
    oem_procurement_role: "OEM-PROC-001"
    supplier_quality_role: "SUP-QA-001"
    timestamp: "2026-02-23T10:00:00Z"
  validity_state: "ACTIVE"
  previous_pnr_id: null
  previous_commitment_hash: null
```

**Off-chain scope** (NOT anchored; referenced by commitment hash only):
Scope definition document, ICD version reference, audit checklist template.

---

#### Event 2: `STL_ATTEST`

Supplier anchors the cryptographic commitment (hash or Merkle root) of their
**Supplier Evidence Package (SEP)**. The SEP itself remains **off-chain only**.

**SEP off-chain contents** (never on-chain):

- Manufacturing router / process recipe
- Part-Specific Identification Document (PSID)
- Material and process certificates
- Inspection records and non-conformance reports
- Calibration data and traceability records
- Test reports and acceptance data

**Records on-chain** (commitment proof only):

```yaml
stl_attest:
  pnr_id: "PNR:A360:C:STL:00002"
  event_type: "STL_ATTEST"
  anchored_at: "2026-03-15T14:30:00Z"
  stl_id: "STL-A360-C-ATA28-001"
  supplier_role_id: "SUP-ROLE-ATA28-CRYO-001"
  sep_commitment:
    sep_merkle_root: "<SHA-256 Merkle root of SEP document set, 64 hex chars>"
    sep_document_count: 7
    sep_canonical_form: "SHA-256/YAML-sorted-keys"
  consensus_proof:
    supplier_quality_role: "SUP-QA-001"
    timestamp: "2026-03-15T14:30:00Z"
  validity_state: "ACTIVE"
  previous_pnr_id: "PNR:A360:C:STL:00001"
  previous_commitment_hash: "<SHA-256 of STL_OPEN payload, 64 hex chars>"
```

---

#### Event 3: `STL_CLOSE`

OEM verifies the on-chain commitment against the off-chain SEP and closes the
Thread line. The final state reflects the outcome of verification.

**Final states**:

| State | Meaning |
|-------|---------|
| `verified` | SEP Merkle root confirmed; all documents match; STL closed with positive outcome |
| `disputed` | Discrepancy found between commitment and off-chain SEP; formal dispute open |
| `superseded` | SEP updated after ATT; new STL\_OPEN/ATTEST cycle initiated; this line retired |

**Records on-chain**:

```yaml
stl_close:
  pnr_id: "PNR:A360:C:STL:00003"
  event_type: "STL_CLOSE"
  anchored_at: "2026-03-20T09:00:00Z"
  stl_id: "STL-A360-C-ATA28-001"
  verification_outcome: "verified"
  verified_by_role: "OEM-QA-001"
  sep_merkle_root_verified: "<SHA-256 Merkle root confirmed, 64 hex chars>"
  consensus_proof:
    oem_procurement_role: "OEM-PROC-001"
    oem_qa_role: "OEM-QA-001"
    timestamp: "2026-03-20T09:00:00Z"
  validity_state: "ACTIVE"
  final_state: "verified"
  previous_pnr_id: "PNR:A360:C:STL:00002"
  previous_commitment_hash: "<SHA-256 of STL_ATTEST payload, 64 hex chars>"
```

---

## §5  Validity State Model

Every on-chain record carries a `validity_state` that is itself part of the
auditable chain. State transitions are governance events subject to the same
consensus level as the original anchoring.

### §5.1  State Machine

```
                    ┌─────────────────────────────────────┐
                    │                                     │
            ACTIVE ─┼──► SUPERSEDED  (correction issued) │
                    │                                     │
                    ├──► REVOKED     (record invalidated) │
                    │                                     │
                    └──► EXPIRED     (temporal window     │
                                      elapsed)            │
                         └─────────────────────────────────┘
```

All transitions are **uni-directional and append-only**. There is no
transition back to `ACTIVE` from any terminal state; a new PNR record
must be created.

### §5.2  State Transition Table

| From State | To State    | Trigger | Required Consensus | Meaning |
|------------|-------------|---------|-------------------|---------|
| `ACTIVE`   | `SUPERSEDED`| Correction or update | Same as original anchoring | Prior record remains referenceable; new record is authoritative |
| `ACTIVE`   | `REVOKED`   | Invalidation finding | SA + Programme Lead (minimum) | Record removed from authoritative chain; prior record retained for audit |
| `ACTIVE`   | `EXPIRED`   | Temporal window elapsed or programme phase exit | Automatic (no consensus required) | Record has passed its governance scope; no longer operative |
| `SUPERSEDED` | —         | — | — | Terminal state; no further transitions |
| `REVOKED`  | —           | — | — | Terminal state; no further transitions |
| `EXPIRED`  | —           | — | — | Terminal state; no further transitions |

### §5.3  State Transition Audit Entry Schema

Every state transition **must** produce a corresponding audit entry:

```yaml
validity_state_transition:
  transition_id: "<UUID or sequential PNR-scoped ID>"
  pnr_id_affected: "<PNR ID of record being transitioned>"
  prior_state: "ACTIVE"
  new_state: "SUPERSEDED"
  transition_reason: "<Free text description of reason>"
  transition_timestamp: "<ISO-8601 UTC>"
  new_pnr_id: "<PNR ID of superseding record, if SUPERSEDED>"
  consensus_proof:
    approver_role_1: "<role identifier>"
    approver_role_2: "<role identifier>"
    timestamp: "<ISO-8601 UTC>"
  transition_hash: "<SHA-256 of this transition payload, 64 hex chars>"
```

### §5.4  Transition Consensus Rule

> State transitions require the **same consensus level** as the original
> anchoring event. A record anchored under Freeze Point consensus (SA +
> Programme Lead) cannot be superseded by a single approver.

---

## §6  Consensus Policies

The following consensus policy interfaces are defined. These are abstract
governance roles and are NOT bound to specific blockchain voting mechanisms —
they are implementable on any substrate (smart contract, multi-sig wallet,
governance API, notary sign-off).

| Event | Required Consensus | Notes |
|-------|--------------------|-------|
| Freeze Point attestation (FP-01 → FP-05) | SA + Programme Lead | Both roles must sign/attest |
| Compilation acceptance (COMP) | CI/CD pipeline + SA sign-off | Automated CI commit + manual SA approval |
| ADR approval (ADR event) | Contributor + SA + Programme Lead | Three-party; contributor proposes, SA and PL approve |
| Supplier line activation (STL\_OPEN) | OEM Procurement + Supplier Quality | Both parties must co-sign the scope |
| Supplier line close (STL\_CLOSE) | OEM Procurement + OEM QA | Two OEM roles for independence |
| Emergency recompilation | SA alone (interim) | Full consensus (SA + PL) required within 5 working days |
| Validity state change | Same consensus as original event | See §5.4 |

---

## §7  Alphanumeric Convention for On-Chain Anchoring

### §7.1  PNR Identifier Format

```
PNR:<programme_id>:<family_code>:<event_type>:<sequence>
```

| Field | Values | Description |
|-------|--------|-------------|
| `programme_id` | `A360` | Programme identifier (AMPEL360 WTW) |
| `family_code` | `A`–`G`, `*` | ELC family code; `*` for programme-wide events |
| `event_type` | `FP01`–`FP05`, `COMP`, `ADR`, `GATE`, `STL`, `SQUAL`, `RECOND` | Event type code |
| `sequence` | `00001`–`99999` | Zero-padded 5-digit sequence within event type and family |

**Examples**:

```
PNR:A360:C:FP01:00001    # Family C, Freeze Point 1 passage
PNR:A360:*:COMP:00042    # Programme-wide, compilation event 42
PNR:A360:C:STL:00001     # Family C, Supplier Thread Line open
PNR:A360:*:ADR:00007     # Programme-wide, ADR approval event 7
PNR:A360:A:GATE:00015    # Family A, gate evaluation 15
```

### §7.2  Minimal On-Chain Commitment Payload Schema

```yaml
# Minimal PNR on-chain commitment payload
pnr_commitment:
  pnr_id: "<PNR:<programme_id>:<family_code>:<event_type>:<sequence>>"
  event_type: "<event type code>"
  anchored_at: "<ISO-8601 UTC timestamp>"
  commitment_hash: "<SHA-256 of off-chain artefact or canonical payload, 64 hex chars>"
  validity_state: "<ACTIVE | SUPERSEDED | REVOKED | EXPIRED>"
  consensus_proof:
    "<role_id_1>": "<attestation token or signature reference>"
    "<role_id_2>": "<attestation token or signature reference>"
    timestamp: "<ISO-8601 UTC>"
  previous_pnr_id: "<prior PNR ID in chain, or null>"
  previous_commitment_hash: "<SHA-256 of prior payload, or null>"
```

All fields are mandatory. `previous_pnr_id` and `previous_commitment_hash`
are `null` only for the genesis record of a given chain.

---

## §8  Relationship to DETERMINISM\_CONTRACT

The following table maps each concept in `AMPEL360-FAM-ARCH-ELC-001-DET`
(Determinism Contract) to its reinterpretation or extension under this policy.

| DETERMINISM\_CONTRACT Concept | PNR Policy Interpretation |
|-------------------------------|--------------------------|
| "Immutable after creation" (§6.1) | Reinterpreted as **relative immutability**: non-destructively versioned; the compilation manifest MAY be superseded via a new compilation anchored as SUPERSEDED transition. The prior manifest remains referenceable. |
| "append-only; mutations require a new compilation" | Confirmed and extended: the new compilation MUST be anchored as a PNR COMP event that supersedes the prior COMP event. Both remain in the chain. |
| "Signed (or at minimum, hash-chained) so tampering is detectable" | Confirmed and extended: the PNR Thread provides the canonical hash-chain and optional multi-party consensus signatures. |
| `compile_hash` (§4.1) | The `compile_hash` is the `commitment_hash` field in a `COMP`-type PNR commitment. |
| Drift Detection (§5) | Drift events may trigger an ADR PNR event; the ADR commitment anchors the governance decision to recompile. |
| Emergency Recompilation (§7.3) | Maps to Emergency Recompilation consensus policy (§6 of this document): SA alone for interim, full consensus within 5 days. |
| Governance: who may trigger recompilation (§7.1) | Maps to Compilation acceptance consensus (§6): CI/CD + SA sign-off for normal; SA alone for emergency. |

---

## §9  Data Protection & IP Safeguards

In compliance with NR-02 (AEPD 2024) and the principles of data minimisation:

### §9.1  No Personal Data On-Chain

All on-chain records use **role identifiers** (e.g., `SA-001`, `OEM-QA-001`,
`SUP-ROLE-ATA28-CRYO-001`). No personal names, email addresses, or individual
identifiers are anchored on-chain.

### §9.2  No IP or Engineering Content On-Chain

Only **commitment hashes** (SHA-256 digests) of off-chain artefacts are
anchored. No design data, engineering specifications, trade secrets, supplier
commercial data, or programme-sensitive content is placed on-chain.

### §9.3  Right to Rectification

The `SUPERSEDED` state transition mechanism (§5) provides the technical
implementation of the right to rectification:

1. The inaccurate record is transitioned to `SUPERSEDED` (audit entry recorded).
2. A new PNR record with corrected data is anchored as the authoritative record.
3. The prior record remains in the chain for audit continuity but is no longer
   operative.

### §9.4  Right to Erasure Compatibility

Per NR-02, the on-chain/off-chain architecture is compatible with erasure
rights:

- On-chain: only commitment hashes remain; a hash of deleted data reveals
  nothing about the data content.
- Off-chain: the actual data is erased from the SSOT repository per the
  applicable data protection procedure.
- The on-chain record transitions to `REVOKED` with the transition reason
  documenting the erasure event (without recording the erased data).

### §9.5  Data Minimisation

The minimal on-chain payload (§7.2) contains only what is strictly necessary
to establish commitment proof, chain integrity, and governance traceability.
No optional fields are added to on-chain records without a formal ADR
justifying the necessity.

---

## §10  Qualifying Capacity Authorization Model

This section gives operative effect within this policy to the **Qualifying
Capacity Manifesto** (`AMPEL360-FAM-ARCH-ELC-001-QCC`). Together, §10 of
this document and the QCC manifesto form the complete authorization framework
for the Thread.

### §10.1  Core Principle

No action on the PNR Thread is legitimate unless the acting party satisfies
the authorization formula simultaneously:

> **Authorization = Delegation ∧ Skills**

This applies to all Thread events: emitting, attesting, transitioning validity
states, executing STL events, and observing records. Roles are human-readable
labels only; the system evaluates verifiable **Qualifying Capacity Claims
(QCC)**.

### §10.2  Consensus Proof Interpretation

The `consensus_proof` blocks defined throughout this policy (§4 STL events,
§6 Consensus Policies, §7 Alphanumeric Convention) SHALL be interpreted as
follows:

- Each role identifier listed in a `consensus_proof` block MUST hold, at the
  time of anchoring, **both** a valid `DELEGATION` QCC covering the event scope
  AND a valid `SKILL` QCC satisfying the skill policy for the event type.
- The role name in `consensus_proof` is a scope-resolution key for the
  authorization evaluator, not a statement of authority in itself.
- A `consensus_proof` entry from a role with no valid QCCs is invalid
  regardless of the role's organisational position.

### §10.3  Qualifying Capacity Claims (QCC)

QCCs are defined and governed by `AMPEL360-FAM-ARCH-ELC-001-QCC`. Key
properties:

- **Two types**: `DELEGATION` (scope authority) and `SKILL` (process competence)
- **Time-bounded**: explicit `issued_at` and `expires_at` fields; evaluated at
  the moment of action, not at role assignment time
- **Revocable**: issuer may revoke before expiry; revocation is anchored on-chain
- **Cryptographically anchored**: each QCC is committed to the Thread as a
  `QCC`-type PNR event (see §10.4)
- **Off-chain content**: credential documents (scope details, assessment data)
  remain off-chain; only the credential hash is on-chain

### §10.4  QCC Anchoring as PNR Event

The issuance and state transitions of QCCs are anchored on the PNR Thread
using the alphanumeric convention (§7):

```
PNR:A360:<actor_role_id>:QCC:<sequence>
```

The minimal on-chain QCC anchor payload and state transition schema are defined
in `AMPEL360-FAM-ARCH-ELC-001-QCC §6`.

### §10.5  Visibility Control

Visibility of Thread records is NOT a generic privilege. An actor may observe
a Thread event only if they hold valid QCCs satisfying the `READ_POLICY` for
the event type (defined in `AMPEL360-FAM-ARCH-ELC-001-QCC §4.3`). Absence
of a `READ_POLICY` defaults to the `WRITE_POLICY` for maximum restriction.

### §10.6  Authorization Reproducibility

Every authorization evaluation MUST be deterministic and logged. Given the
same event parameters, the same QCC credential set, and the same policy
version, the evaluator MUST produce the same verdict. Non-determinism in
authorization is a defect equivalent in severity to a compiler non-determinism
defect under `AMPEL360-FAM-ARCH-ELC-001-DET`.

---

## Appendix A: Glossary

| Term | Definition |
|------|-----------|
| **PNR** | Part Number Registry — the distributed evidence framework that anchors cryptographic commitments for part number governance events across the Elastic Lifecycle (ELC) |
| **Thread** | The ordered sequence of PNR commitment records forming the auditable chain for a programme, family, or event scope |
| **STL** | Supplier Thread Line — the three-event (OPEN/ATTEST/CLOSE) handshake protocol for supplier evidence capture |
| **SEP** | Supplier Evidence Package — the off-chain document set attested by the supplier; referenced on-chain by Merkle root only |
| **Commitment hash** | SHA-256 digest of a canonical form of an off-chain artefact, anchored on-chain as proof of existence and integrity |
| **Validity state** | The current governance status of a PNR record: `ACTIVE`, `SUPERSEDED`, `REVOKED`, or `EXPIRED` |
| **Relative immutability** | Immutability understood as integrity detection and modification traceability under governance, not metaphysical permanence |
| **Non-dispersive anchoring** | The principle that only cryptographic commitments are anchored on-chain; all engineering content remains off-chain |
| **Consensus proof** | The set of role-attributed attestations required to anchor or transition a PNR record; each attesting role must hold valid QCCs (§10) |
| **QCC** | Qualifying Capacity Claim — a verifiable credential attesting delegation or skill for a defined actor, scope, and time window (see AMPEL360-FAM-ARCH-ELC-001-QCC) |
| **Qualifying capacity** | The demonstrable, accredited competence of an actor to execute a specific type of action in a defined context; the primary authorization criterion |
| **Authorization formula** | `Auth(actor, event) = Delegation(actor, scope(event)) ∧ Skills(actor, type(event), policy(event))` — the core axiom of the QCC model |

---

<p align="center"><em>AMPEL360 WTW · PNR Blockchain Thread Policy · AMPEL360-FAM-ARCH-ELC-001-PNR Rev A</em></p>
