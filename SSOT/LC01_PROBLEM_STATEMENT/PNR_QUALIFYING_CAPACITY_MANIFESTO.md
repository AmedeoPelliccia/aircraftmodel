# PNR_QUALIFYING_CAPACITY_MANIFESTO.md
# Document ID: AMPEL360-FAM-ARCH-ELC-001-QCC
# Revision: A
# Date: 2026-02-23
# Parent Document: AMPEL360-FAM-ARCH-ELC-001-PNR Rev B (§10 Qualifying Capacity Authorization Model)
# Related Document: AMPEL360-FAM-ARCH-ELC-001-DET (Determinism Contract)

# PNR Thread — Qualifying Capacity Manifesto

**AMPEL360-FAM-ARCH-ELC-001-QCC · Rev A · 2026-02-23**

---

> *«En el PNR Thread, la autoridad se ejerce a través de la evidencia,
> no por simple declaración de jerarquía.
> La capacidad calificante es el criterio primario;
> la organización, el contexto que la limita.»*
>
> — Principio XII, Manifiesto de Capacidad Calificante en el PNR Thread.

---

## Revision History

| Rev | Date       | Author Role           | Change Summary                                    |
|-----|------------|-----------------------|---------------------------------------------------|
| A   | 2026-02-23 | System Architect (SA) | Initial release — Qualifying Capacity framework   |

---

## §1  Purpose & Doctrinal Scope

This document governs the **Qualifying Capacity Authorization Model** for the
PNR (Part Number Registry) Blockchain Thread of the AMPEL360 programme.

It establishes the normative framework under which any actor — human, system,
or organisational unit — is authorized to execute, attest, or observe events
on the Thread. It formalizes and gives operational effect to the twelve
principles of the Qualifying Capacity Manifesto.

This document is a companion to `AMPEL360-FAM-ARCH-ELC-001-PNR` (PNR
Blockchain Thread Policy). Together they form the complete authorization
and evidence framework for the Thread. In any conflict, the more restrictive
provision applies.

### §1.1  Core Axiom

> **Authorization = Delegation ∧ Skills**

No action on the PNR Thread is legitimate unless the acting party satisfies
**both** conditions simultaneously:

1. **Delegation** — a valid delegation grant covering the scope of the action
   (programme, supplier, facility, family, part, event type), active at the
   moment of the action.

2. **Skills** — verifiable evidence of qualifying capacity that satisfies the
   skill policy defined for the event type, active at the moment of the action.

The absence of either condition is an absolute disqualification. No
organisational role, title, seniority, or historical precedent compensates for
a missing or expired Delegation or Skill claim.

### §1.2  Position on Roles

Roles survive in this framework only as **human-readable labels**. They provide
context and scope for the search space of qualifying capacity claims, but
convey no authority in themselves. The system logic evaluates verifiable claims
— not titles.

A role that carries no verifiable delegation and no verifiable skill evidence
is an empty label with no operative effect on the Thread.

---

## §2  The Twelve Normative Principles

The following twelve principles are normative requirements (MUST / SHALL). They
are stated both in English (operative text) and in the original Spanish
(authentic voice of the manifesto).

---

### Principle I — Capacity over Hierarchy

**Normative:** No action on the Thread SHALL be legitimized by job title,
organisational chart position, or declared seniority. The sole criterion is
demonstrable qualifying capacity in the context of the specific action.

> *«Ninguna acción se legitima por cargo, organigrama o título, sino por
> capacidad calificante demostrable.»*

**Operative effect:** The authorization evaluator MUST NOT accept organisational
hierarchy as a substitute for missing delegation or skill claims.

---

### Principle II — Capacity is Contextual

**Normative:** No actor "has a right" to execute, attest, or view a Thread
event by virtue of their job title. Authorization MUST be evaluated against
what the actor is capable of doing and can prove they know how to do, in the
defined context of the specific event.

> *«Ningún actor "tiene derecho" a ejecutar, atestar o ver un evento por cómo
> se llama su puesto, sino por lo que es capaz de hacer y probar que sabe
> hacer, en un contexto definido.»*

**Operative effect:** Authorization evaluation MUST be scoped to the specific
event type, family, ATA chapter, and programme context. A valid QCC for event
type `COMP` does not authorize event type `FP01`.

---

### Principle III — The Authorization Formula

**Normative:** All relevant actions on the Thread MUST satisfy the authorization
formula:

```
Auth(actor, event) = Delegation(actor, scope(event)) ∧ Skills(actor, type(event), policy(event))
```

Without valid delegation: no mandate. Without verified skill: no competence.
Both are required simultaneously, evaluated at the moment of the action.

> *«Toda acción relevante sobre el Thread se entiende como:
> Autorización = Delegación ∧ Skills.
> Sin delegación válida, no hay mandato; sin skill comprobada, no hay
> competencia.»*

**Operative effect:** The authorization evaluator MUST implement this formula
as a logical AND of two independently verified claims. Short-circuit evaluation
is not permitted — both claims MUST be verified even if one fails.

---

### Principle IV — Delegation and Skill are Orthogonal

**Normative:** Delegation and Skills are separate, orthogonal dimensions of
authorization:

- **Delegation** defines the **where and for whom**: programme, supplier,
  facility, family code, ATA chapter, part number, event type scope.
- **Skills** define the **what and how**: process type, inspection method,
  release authority, change disposition, repair technique.

> *«La delegación define el dónde y para quién: programa, proveedor,
> instalación, línea, familia, parte.
> La skill define el qué y cómo: proceso, inspección, liberación,
> disposición de cambio, reparación.»*

**Operative effect:** A delegation claim and a skill claim MUST be separately
issued, separately verifiable, and separately revocable. The intersection of
their scopes defines the authorization boundary.

---

### Principle V — Simultaneous Satisfaction Required

**Normative:** No actor SHALL emit or observe a Thread event unless they
simultaneously satisfy, at the moment of the attempted action:

1. A valid delegation grant covering the scope of the Thread event, AND
2. Skill evidence that satisfies the skill policy for the event type, at the
   date and time of the action attempt.

> *«Ningún actor deberá emitir ni visualizar un evento si no satisface
> simultáneamente: delegación válida para el ámbito del thread, y evidencias
> de skill que satisfacen la política del tipo de evento, en la fecha y hora
> del intento de acción.»*

**Operative effect:** The authorization evaluation MUST be performed at
runtime, not at role assignment time. Pre-authorization caching that does not
account for credential expiry is prohibited.

---

### Principle VI — Skills are Accredited, Not Asserted

**Normative:** Skills MUST NOT be self-asserted by the actor. Each skill claim
MUST be backed by a Qualifying Capacity Credential (QCC) that is:

- **Signed** by an accepted issuer (see §5.2 Accepted Issuers);
- **Time-bounded**: with explicit `issued_at` and `expires_at` fields;
- **Revocable**: the issuer may revoke the credential before expiry;
- **Cryptographically anchored**: the credential hash is committed to the PNR
  Thread (see §6 Credential Anchoring).

> *«Las habilidades no se afirman; se acreditan. Cada skill debe estar
> respaldada por credenciales verificables: firmadas por un emisor aceptado,
> acotadas en el tiempo y revocables, ancladas mediante compromisos
> criptográficos.»*

**Operative effect:** The authorization evaluator MUST verify the credential
signature, temporal validity, and revocation status before accepting a skill
claim. An unverifiable credential MUST be treated as absent.

---

### Principle VII — Minimal Verifiable Proofs on the Ledger

**Normative:** The ledger MUST NOT store personal merits, curricula vitae,
training histories, or biographical data. The ledger stores only **minimal
verifiable proofs** demonstrating that, at the moment of each event, the
acting party was authorized by qualifying capacity.

> *«El ledger no guarda méritos personales ni currículos: guarda pruebas
> mínimas y verificables de que, en el momento de cada evento, quien actuó
> estaba habilitado por capacidad calificante.»*

**Operative effect:** The on-chain QCC anchor (§6) records only the credential
hash, role identifier, scope reference, and temporal validity bounds — nothing
more. All credential content is off-chain and governed by data protection
policies.

---

### Principle VIII — Claims, Not Titles

**Normative:** The authorization logic of the system MUST obey **verifiable
claims**, not role titles. Roles are permitted only as human-readable context
labels. The system MUST NOT grant any privilege based on role name alone.

> *«Los roles sobreviven solo como etiquetas humanas; la lógica del sistema
> no obedece a títulos, obedece a claims verificables.»*

**Operative effect:** In the authorization evaluator, role names MUST be
resolved to QCC claim sets before evaluation. An actor whose role name is
present but whose QCC set is empty or expired MUST be treated as unauthorized.

---

### Principle IX — Visibility as Consequence

**Normative:** Visibility of Thread events is NOT a generic privilege. An
actor MAY view a Thread event only if they hold:

1. Valid delegation for the scope of the event, AND
2. Sufficient skill evidence to understand and take responsibility for what
   they observe.

> *«La visibilidad no es un privilegio genérico, es una consecuencia: solo
> ve aquello quien tiene delegación en el ámbito y skill suficiente para
> entender y responsabilizarse de lo que ve.»*

**Operative effect:** Access control for read operations on Thread records
MUST apply the same `Auth(actor, event)` formula as write operations. A
separate, lighter-weight skill policy for read access MAY be defined per
event type (see §4.3 Visibility Policy).

---

### Principle X — Reproducible Authorization Decisions

**Normative:** Every authorization decision MUST be reproducible. Given the
same event parameters, the same credential set, and the same policy version,
the authorization evaluator MUST always produce the same verdict.
Non-determinism in authorization evaluation is a defect.

> *«Toda decisión de autorización debe ser reproducible: dado el mismo evento,
> las mismas credenciales y la misma política, el sistema debe llegar al mismo
> veredicto; no hay arbitrariedad, solo evaluación de pruebas.»*

**Operative effect:** Authorization policies MUST be version-controlled
artefacts with deterministic evaluation semantics. Policy changes MUST be
anchored as PNR events before they take effect (see §7 Policy Versioning).
Evaluation logs MUST be retained as audit evidence.

---

### Principle XI — Protection Without Exclusion

**Normative:** The model protects both the system and the people who operate
within it:

- No actor is "protected" by a hollow role that carries no verifiable
  qualifying capacity.
- No actor is excluded if they can demonstrate, in verifiable form, the
  competence and the delegation required.

> *«El modelo protege tanto al sistema como a las personas: nadie queda
> "protegido" por un rol vacío, nadie queda excluido si demuestra, de forma
> verificable, la competencia y la delegación necesarias.»*

**Operative effect:** The onboarding process for new actors onto the Thread
MUST be driven by QCC issuance, not by organisational assignment. Actors whose
credentials lapse MUST be automatically de-authorized; re-authorization
requires new credential issuance.

---

### Principle XII — Evidence Over Hierarchy

**Normative:** Authority on the PNR Thread is exercised **through evidence**,
not through declarations of hierarchy. Qualifying capacity is the primary
criterion; organisation is the context that bounds it.

> *«En el PNR Thread, la autoridad se ejerce a través de la evidencia, no por
> simple declaración de jerarquía. La capacidad calificante es el criterio
> primario; la organización, el contexto que la limita.»*

**Operative effect:** Any appeal to organisational authority in lieu of
verifiable qualifying capacity MUST be rejected by the authorization evaluator.
Escalation paths MUST proceed through QCC issuance, not through bypass
mechanisms.

---

## §3  Qualifying Capacity Claim (QCC) Structure

A **Qualifying Capacity Claim** is a verifiable credential issued by an
accepted authority that attests to either a **delegation grant** or a
**skill qualification** for a defined actor role, scope, and time window.

### §3.1  QCC Types

| Type | Symbol | Purpose |
|------|--------|---------|
| `DELEGATION` | `D` | Grants authority to act within a defined scope (programme, family, ATA, event types) |
| `SKILL` | `S` | Attests qualifying capacity for a specific process type or event type |

Both types are independently issued, independently verified, and independently
revocable. The authorization formula requires one valid `DELEGATION` QCC and
one valid `SKILL` QCC simultaneously.

### §3.2  QCC Identifier Format

```
QCC:<programme_id>:<actor_role_id>:<type>:<sequence>
```

| Field | Values | Description |
|-------|--------|-------------|
| `programme_id` | `A360` | Programme identifier |
| `actor_role_id` | Role identifier string | The role for which the claim is issued |
| `type` | `D` (delegation), `S` (skill) | QCC type |
| `sequence` | `00001`–`99999` | Zero-padded 5-digit sequence per actor and type |

**Examples**:

```
QCC:A360:SA-001:D:00001          # Delegation QCC for System Architect role
QCC:A360:OEM-QA-001:S:00003      # Skill QCC for OEM QA role, third issuance
QCC:A360:SUP-ROLE-ATA28-001:S:00001  # Skill QCC for Supplier role
```

### §3.3  QCC Payload (off-chain canonical form)

The QCC credential document is stored **off-chain** in the SSOT repository.
Only its hash is anchored on-chain (§6). The canonical form for hashing is
YAML with sorted keys, no comments, UTF-8, LF line endings.

```yaml
# Qualifying Capacity Claim — off-chain credential document
qcc:
  qcc_id: "QCC:A360:SA-001:D:00001"
  qcc_type: "DELEGATION"            # DELEGATION | SKILL
  actor_role_id: "SA-001"
  validity_state: "ACTIVE"          # ACTIVE | SUPERSEDED | REVOKED | EXPIRED

  # Temporal bounds (both required)
  issued_at: "2026-02-23T10:00:00Z"
  expires_at: "2027-02-23T23:59:59Z"

  # Issuer (accepted authority — see §5.2)
  issuer_id: "PROG-LEAD-001"
  issuer_signature_ref: "<signature reference or attestation token>"

  # Scope (for DELEGATION type)
  delegation_scope:
    programme_id: "A360"
    family_codes: ["A", "B", "C", "D", "E", "F", "G", "*"]
    event_types: ["FP01", "FP02", "FP03", "FP04", "FP05", "COMP", "ADR", "GATE"]
    ata_chapters: ["*"]              # "*" means all; list specific chapters to restrict
    suppliers: ["*"]
    facilities: ["*"]

  # Skill reference (for SKILL type — omit for DELEGATION)
  # skill_reference:
  #   skill_code: "INSP-CRYO-001"
  #   process_type: "inspection"
  #   method_reference: "ATA-28-10-INSP-METHOD-A"
  #   qualification_standard: "EN 9100 §8.4.3"
  #   assessment_ref: "<off-chain assessment document reference>"

  # Chain (null for genesis QCC of this actor/type)
  prior_qcc_id: null
  prior_credential_hash: null

  # Self-hash (SHA-256 of this document with credential_hash field zeroed)
  credential_hash: "<SHA-256 hex, 64 chars>"
```

---

## §4  Authorization Evaluation Model

### §4.1  Evaluation Algorithm

The authorization evaluator MUST execute the following algorithm at every
action attempt. The evaluation MUST be deterministic and logged.

```
function evaluate(actor_role_id, event, policy_version):

  1. Resolve active QCC set for actor_role_id:
     D_set = { qcc ∈ QCC_store | qcc.actor_role_id = actor_role_id
                               ∧ qcc.qcc_type = "DELEGATION"
                               ∧ qcc.validity_state = "ACTIVE"
                               ∧ now() ∈ [qcc.issued_at, qcc.expires_at] }

     S_set = { qcc ∈ QCC_store | qcc.actor_role_id = actor_role_id
                               ∧ qcc.qcc_type = "SKILL"
                               ∧ qcc.validity_state = "ACTIVE"
                               ∧ now() ∈ [qcc.issued_at, qcc.expires_at] }

  2. Verify each QCC in D_set and S_set:
     - Issuer signature valid (issuer_id ∈ accepted_issuers(policy_version))
     - Credential hash matches on-chain anchor (§6)
     - Revocation status: not REVOKED or SUPERSEDED

  3. Find matching delegation:
     D_match = { d ∈ D_set | scope(event) ⊆ delegation_scope(d) }
     if D_match is empty: RETURN DENIED (reason: "no valid delegation")

  4. Find matching skill:
     skill_policy = skill_policy(event.event_type, policy_version)
     S_match = { s ∈ S_set | satisfies(s, skill_policy) }
     if S_match is empty: RETURN DENIED (reason: "no valid skill")

  5. RETURN AUTHORIZED(
       delegation_qcc_id = select_best(D_match),
       skill_qcc_id = select_best(S_match),
       evaluated_at = now(),
       policy_version = policy_version
     )
```

### §4.2  Evaluation Log Entry

Every authorization evaluation MUST produce a log entry retained for audit:

```yaml
authorization_evaluation:
  evaluated_at: "<ISO-8601 UTC>"
  actor_role_id: "<role identifier>"
  event_type: "<PNR event type>"
  pnr_scope: "<programme:family:event_type>"
  policy_version: "<policy document ID and revision>"
  verdict: "<AUTHORIZED | DENIED>"
  denial_reason: "<reason string | null>"
  delegation_qcc_id: "<QCC ID used | null>"
  skill_qcc_id: "<QCC ID used | null>"
  evaluation_hash: "<SHA-256 of this log entry, 64 hex chars>"
```

### §4.3  Visibility Policy

Read access to Thread events applies the same formula with a lighter-weight
skill policy. Each event type defines two policy levels:

| Policy Level | Used for | Skill requirement |
|-------------|----------|-------------------|
| `WRITE_POLICY` | Emitting, attesting, transitioning events | Full qualifying capacity for process type |
| `READ_POLICY` | Observing, querying event records | Understanding of process type sufficient to take responsibility |

The `READ_POLICY` for an event type MUST be defined explicitly; absence of a
`READ_POLICY` defaults to the `WRITE_POLICY` (most restrictive).

---

## §5  Credential Governance

### §5.1  QCC Lifecycle

```
            ACTIVE ──► SUPERSEDED  (new QCC issued; prior superseded)
                   ──► REVOKED     (issuer invalidation; misconduct, scope change)
                   ──► EXPIRED     (expires_at elapsed; automatic)
```

All transitions are uni-directional and append-only. Re-authorization requires
issuance of a new QCC; reactivation of a REVOKED or EXPIRED credential is not
permitted.

### §5.2  Accepted Issuers

An issuer is accepted if they hold a valid `DELEGATION` QCC with an
`event_types` scope that includes `QCC_ISSUE` for the relevant actor scope.
Accepted issuer roles for the AMPEL360 programme include:

| Issuer Role | Authority Scope |
|-------------|----------------|
| Programme Lead | All QCCs for programme-scope actors |
| System Architect (SA) | QCCs for technical roles within their system scope |
| OEM Quality Authority | Skill QCCs for OEM-side roles |
| Supplier Quality Authority | Skill QCCs for supplier-side roles within their facility scope |
| External Certification Body | Skill QCCs requiring regulatory qualification (DAL, EN 9100, etc.) |

An issuer MUST NOT issue a QCC with a scope broader than their own delegation.

### §5.3  Credential Revocation

A QCC MAY be revoked before its expiry by the issuer or by any actor with
Programme Lead delegation, in the following circumstances:

- The actor's competence has been found deficient or fraudulently asserted
- The actor's organisational scope has changed (new role, departure)
- A safety finding requires immediate de-authorization
- The actor requests revocation (resignation, voluntary withdrawal)

Revocation MUST be recorded as a validity state transition of the QCC anchor
(§6.2) with a transition reason. The revocation does NOT expose the credential
content — only the QCC ID and revocation timestamp are on-chain.

### §5.4  Credential Expiry Policy

| QCC Type | Maximum Validity Period | Renewal Trigger |
|----------|------------------------|-----------------|
| `DELEGATION` | 24 months | Programme phase transition or organisational change |
| `SKILL` (standard) | 12 months | Annual competence review |
| `SKILL` (regulatory) | Per certification body requirement | Regulatory recurrent training cycle |
| `SKILL` (emergency) | 30 days | Issued under emergency authorization; full credential required within 30 days |

---

## §6  Credential Anchoring (On-Chain)

### §6.1  QCC Anchor Record

When a QCC is issued, its credential hash MUST be anchored on the PNR Thread
as a `QCC_ISSUE` event. This creates a verifiable, tamper-evident record that
the credential existed and was valid at anchoring time.

**On-chain QCC anchor payload** (minimal, per non-dispersive anchoring):

```yaml
qcc_anchor:
  pnr_id: "PNR:A360:SA-001:QCC:00001"
  event_type: "QCC"
  anchored_at: "<ISO-8601 UTC>"
  qcc_id: "QCC:A360:SA-001:D:00001"
  qcc_type: "DELEGATION"             # DELEGATION | SKILL
  actor_role_id: "SA-001"
  issuer_id: "PROG-LEAD-001"
  issued_at: "<ISO-8601 UTC>"
  expires_at: "<ISO-8601 UTC>"
  commitment_hash: "<SHA-256 of off-chain QCC document, 64 hex chars>"
  validity_state: "ACTIVE"
  consensus_proof:
    issuer_id: "PROG-LEAD-001"
    timestamp: "<ISO-8601 UTC>"
  previous_pnr_id: null
  previous_commitment_hash: null
```

Note: only the credential hash, identity fields, temporal bounds, and issuer
are on-chain. The credential content (delegation scope details, skill
assessment data) remains off-chain.

### §6.2  QCC State Transition Anchor

When a QCC transitions to `SUPERSEDED`, `REVOKED`, or `EXPIRED`, a state
transition event MUST be anchored:

```yaml
qcc_state_transition:
  pnr_id: "PNR:A360:SA-001:QCC:00002"
  event_type: "QCC"
  anchored_at: "<ISO-8601 UTC>"
  qcc_id_affected: "QCC:A360:SA-001:D:00001"
  prior_state: "ACTIVE"
  new_state: "REVOKED"
  transition_reason_code: "SCOPE_CHANGE"  # See §5.3 — no free text on-chain
  new_qcc_id: null                        # null if REVOKED; new QCC ID if SUPERSEDED
  consensus_proof:
    revoking_role: "PROG-LEAD-001"
    timestamp: "<ISO-8601 UTC>"
  commitment_hash: "<SHA-256 of this transition payload, 64 hex chars>"
  previous_pnr_id: "PNR:A360:SA-001:QCC:00001"
  previous_commitment_hash: "<SHA-256 of prior anchor, 64 hex chars>"
```

---

## §7  Policy Versioning

Authorization policies — the skill policy sets that define what QCC evidence
satisfies each event type — are themselves versioned artefacts governed by the
PNR Thread.

### §7.1  Policy Version Anchoring

A policy version becomes operative when it is anchored as a `POLICY` event on
the PNR Thread, with consensus at SA + Programme Lead level. Policy changes
take effect at the `anchored_at` timestamp of the POLICY event.

### §7.2  Policy Transition

When a new policy version supersedes a prior one:

1. All active QCCs are evaluated against the new policy.
2. QCCs that no longer satisfy the new policy MUST be superseded; new QCCs
   are issued under the new requirements.
3. A grace period MAY be defined in the POLICY event (e.g., 30 days) during
   which both old and new policy versions are accepted.

### §7.3  Reproducibility Guarantee

The combination of `(event parameters, QCC credential set, policy version)`
fully determines the authorization verdict. This is the qualifying capacity
analogue of the DETERMINISM_CONTRACT's compile hash guarantee.

---

## §8  Relationship to PNR Blockchain Thread Policy

| PNR Policy Concept (AMPEL360-FAM-ARCH-ELC-001-PNR) | QCC Model Interpretation |
|----------------------------------------------------|--------------------------|
| `consensus_proof` block in commitment payloads | Each attesting role in `consensus_proof` MUST hold valid QCCs satisfying both the DELEGATION and SKILL policies for the event type |
| Role identifiers (e.g., `SA-001`, `OEM-QA-001`) | Role identifiers in `consensus_proof` are resolved to QCC claim sets by the authorization evaluator; the role name alone conveys no authority |
| Consensus policy table (§6 of PNR policy) | The roles listed in the consensus table are QCC scope identifiers; the actual authorization is evaluated against live QCC claim sets, not role assignments |
| Supplier Thread Lines (§4 of PNR policy) | `STL_OPEN` activation requires valid QCCs for both OEM Procurement role and Supplier Quality role; `STL_CLOSE` requires OEM QA skill QCC for verification scope |
| Validity state transitions (§5 of PNR policy) | Any actor executing a validity state transition MUST hold QCCs at the same consensus level as the original anchoring, per Principle V |
| Emergency recompilation (§6 of PNR policy) | SA-alone interim authorization requires the SA role to hold an active DELEGATION QCC plus a SKILL QCC covering `COMP` event type |

---

## §9  Data Protection Safeguards for QCC Framework

In extension of `AMPEL360-FAM-ARCH-ELC-001-PNR §9`:

### §9.1  No Personal Data in QCC Anchors

QCC anchors on-chain use role identifiers only (`actor_role_id`, `issuer_id`).
No personal names, employee IDs, or biographic data are anchored.

### §9.2  Credential Content is Off-Chain

The QCC credential document — which may contain assessment references, training
records, and scope descriptions — is stored off-chain under applicable data
protection governance. Only the `credential_hash` is on-chain.

### §9.3  Right to Erasure for QCC Content

If an individual's credential data is subject to an erasure request:

1. The off-chain credential document is erased per the applicable procedure.
2. The on-chain QCC anchor transitions to `REVOKED` with reason code
   `DATA_ERASURE`.
3. The credential hash on-chain remains as a proof-of-existence token only;
   no credential content is recoverable from it.

### §9.4  Minimum Data Principle for Transition Reason Codes

On-chain transition reason codes (§6.2) MUST use defined codes from a
controlled vocabulary, not free text, to prevent inadvertent personal data
disclosure. Controlled reason codes include:
`SCOPE_CHANGE`, `COMPETENCE_LAPSE`, `SAFETY_FINDING`, `VOLUNTARY_WITHDRAWAL`,
`SUPERSEDED_BY_NEW`, `DATA_ERASURE`, `CREDENTIAL_FRAUD`.

---

## Appendix A: Glossary

| Term | Definition |
|------|-----------|
| **QCC** | Qualifying Capacity Claim — a verifiable credential attesting delegation or skill for a defined actor, scope, and time window |
| **Delegation QCC** | A QCC of type `DELEGATION` that grants authority to act within a defined programme/family/event-type scope |
| **Skill QCC** | A QCC of type `SKILL` that attests qualifying capacity for a specific process type or event type |
| **Qualifying capacity** | The demonstrable, accredited competence of an actor to execute a specific type of action in a defined context |
| **Authorization formula** | `Auth(actor, event) = Delegation(actor, scope(event)) ∧ Skills(actor, type(event), policy(event))` |
| **Accepted issuer** | An actor holding a delegation QCC that grants authority to issue QCCs for a defined scope |
| **Visibility policy** | The authorization rule governing read access to Thread events; derived from the authorization formula with a READ_POLICY skill level |
| **Policy version** | A versioned artefact defining the skill policy requirements per event type; changes anchored as PNR POLICY events |
| **Evaluation log** | The deterministic, auditable record of each authorization evaluation, retained as evidence of reproducible decision-making |
| **Credential hash** | SHA-256 digest of the canonical form of the off-chain QCC document; anchored on-chain as proof of credential existence and integrity |

---

<p align="center"><em>AMPEL360 · PNR Thread Qualifying Capacity Manifesto · AMPEL360-FAM-ARCH-ELC-001-QCC Rev A</em></p>
