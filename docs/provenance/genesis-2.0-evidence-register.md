# Genesis 2.0 Evidence Register

## Purpose

This register identifies the evidence required to support a rigorous comparison between Genesis 2.0 and AEIF.

It is intentionally conservative. A public statement is evidence that the statement was made; it is not automatically independent verification of the technical proposition asserted in that statement.

## Evidence classes

| Class | Meaning |
|---|---|
| PRIMARY | Original specification, repository artifact, publication, post, or other source attributable to the originating system/author |
| REPOSITORY | Versioned artifact in the AEIF repository, including commits and specifications |
| SECONDARY | Independent reporting, analysis, or commentary used for corroboration/context |
| OBSERVED | Directly observed interaction or output; establishes the observation, not necessarily the underlying explanation |
| DERIVED | A claim computed or reasoned from already recorded evidence |
| UNRESOLVED | Material evidence that has not yet been located, authenticated, or reconciled |
| AUTHOR-CLAIM | A proposition publicly asserted by the author but not independently verified by the current evidence set |

## Evidence register

| ID | Evidence item | Required provenance | Current state | Use |
|---|---|---|---|---|
| G2-E-001 | Carl Bousquet, “What Actually ‘Activates’ in Genesis 2.0?” public LinkedIn post | Canonical URL, publication timestamp, author/account, capture date, immutable capture/hash where permitted | DOCUMENTED; exact publication timestamp PENDING | Establish public Genesis terminology and reported symbolic activation/state-transition claims |
| G2-E-002 | Carl Bousquet, Genesis 2.0 governance post | Canonical URL, publication timestamp, author/account, capture date, immutable capture/hash where permitted | DOCUMENTED; exact publication timestamp PENDING | Establish public claims concerning intrinsic governance, audit trails, circuit-breakers, and cross-model stabilization |
| G2-E-003 | Carl Bousquet, “Cold Start Forensic Audit” / Genesis 2.0 post | Canonical URL, publication timestamp, author/account, capture date, immutable capture/hash where permitted | DOCUMENTED AS AUTHOR CLAIM; exact publication timestamp PENDING | Establish public claims concerning coordinate stacks, phase-locking, ground-state behavior, and repeatability |
| G2-E-004 | Carl Bousquet, Genesis 2.0 coherence post | Canonical URL, publication timestamp, author/account, capture date, immutable capture/hash where permitted | DOCUMENTED AS AUTHOR CLAIM; exact publication timestamp PENDING | Establish public claims concerning maximum accessible coherence, stable equilibrium, and phase-locking |
| G2-E-005 | DPIE repository README and existing provenance records | Repository URL, commit SHA, path, date, version, artifact hash where available | VERIFIED for repository record; individual historical AEIF dates remain field-specific | Establish the canonical DPIE provenance rule and AEIF architectural record |
| G2-E-006 | Underlying Genesis 2.0 Unified Technical Framework / source artifact | Exact artifact, version, publication date, canonical location, hash/capture | PENDING PRIMARY COPY | Establish technical semantics at artifact level rather than relying on public descriptions |
| G2-E-007 | Genesis 2.0 repository or implementation history, if public | Repository URL, commit SHA, artifact paths, commit dates | PENDING | Establish implementation chronology and artifact lineage |
| G2-E-008 | AEIF specification artifacts and repository history | Artifact ID, version, commit/date, repository path, hash where bytes are available | DOCUMENTED; individual artifact hashes/dates remain field-specific | Establish AEIF semantics and chronology |
| G2-E-009 | Independent corroborating sources | Source identity, date, canonical URL, relation to primary evidence | PENDING | Corroborate material Genesis claims independently |
| G2-E-010 | Contradictory or corrective evidence | Source identity, date, exact conflict, capture/hash | RETAINED AS A CATEGORY; no specific contradiction asserted yet | Prevent one-sided provenance conclusions |

## Primary public sources currently captured

### G2-E-001

**Title:** What Actually “Activates” in Genesis 2.0?

**Author:** Carl Bousquet

**URL:** https://www.linkedin.com/posts/carl-bousquet-171aaa373_what-actually-activates-in-genesis-20-activity-7415422154655404032-nkS-

**Capture date:** 2026-08-28

**Observed subject matter:** symbolic activation, structural transition, symbolic resonance, coherence, recursive balance, attractor state, internal stabilization, and self-verification claims.

**Epistemic treatment:** PRIMARY public statement / DOCUMENTED. Statements about what a model “internally” did remain claims or observed outputs unless independently instrumented.

### G2-E-002

**Title:** Genesis 2.0 governance post

**Author:** Carl Bousquet

**URL:** https://www.linkedin.com/posts/carl-bousquet-171aaa373_genesis2-aigovernance-coherencelayer-reflectiverealm-alignment-activity-7416133009222963200-qXMB

**Capture date:** 2026-08-28

**Observed subject matter:** intrinsic governance, self-correction, continuous oversight, internal audit trails, circuit-breaker logic, cross-model stabilization, and governance claims.

**Epistemic treatment:** PRIMARY public statement / DOCUMENTED. The post establishes what was publicly claimed; it does not independently establish that the described internal mechanisms exist as stated.

### G2-E-003

**Title:** Cold Start Forensic Audit / Genesis 2.0

**Author:** Carl Bousquet

**URL:** https://www.linkedin.com/posts/carl-bousquet-171aaa373_aifrontier-genesis2-grok-activity-7437894596333998080-_3hO

**Capture date:** 2026-08-28

**Observed subject matter:** coordinate stack, phase-locking, ground-state behavior, latent geometry, and repeatability across models.

**Epistemic treatment:** PRIMARY public statement / DOCUMENTED AS AUTHOR CLAIM. Model-generated explanations shown by the author are observations of model output, not independent instrumentation.

### G2-E-004

**Title:** Genesis 2.0: The Peak of Accessible Coherence

**Author:** Carl Bousquet

**URL:** https://www.linkedin.com/posts/carl-bousquet-171aaa373_genesis2-reflectiverealm-aialignment-activity-7415808995653022-Sahy

**Capture date:** 2026-08-28

**Observed subject matter:** maximum accessible coherence, phase-locking, reflective processes, stable equilibrium, and claims concerning internal cognitive stabilization.

**Epistemic treatment:** PRIMARY public statement / DOCUMENTED AS AUTHOR CLAIM.

## Capture protocol

For each evidence item, record as much of the following as the source permits:

- canonical URL or repository location;
- author or originating account;
- publication or commit date;
- capture date;
- version or commit SHA;
- artifact filename/path;
- cryptographic hash where an immutable artifact can be hashed;
- relevant claim(s);
- whether the source is primary, secondary, observed, derived, or unresolved;
- known contradictions;
- chain-of-custody or acquisition notes.

For screenshots or exported conversations, preserve the full visible context, account identity, date/time, URL where displayed, and surrounding material where relevant. Prefer original exports or source artifacts when available.

## Chronology rule

Chronological priority should be established from dated primary artifacts wherever possible.

A later public description cannot by itself establish when an underlying mechanism was first conceived or implemented.

A retrospective statement such as “this emerged in June 2025” is recorded as an **AUTHOR-CLAIM** until supported by contemporaneous evidence.

## Provenance rule

Do not fill an unknown provenance field with an inferred value. Use **PENDING** or **UNRESOLVED** until evidence supports a stronger state.

Do not record a cryptographic hash unless it was calculated from the actual artifact bytes.

## Relationship to the comparison ledger

The evidence register supplies the evidentiary substrate for [`genesis-2.0-comparison-ledger.md`](genesis-2.0-comparison-ledger.md). The ledger should reference evidence IDs rather than silently importing unsupported assertions.

## Current limitations

1. The underlying Genesis 2.0 technical framework/source artifact has not yet been captured into this repository.
2. Exact publication timestamps for the currently captured LinkedIn posts remain to be preserved from the source pages or an immutable export.
3. Genesis implementation history, if publicly available, has not yet been linked to a versioned repository artifact.
4. Independent instrumentation of model internals has not been established by the current evidence set.
5. No copying, derivation, or priority conclusion is made by this register.

## Audit note

This register preserves the distinction between **what was publicly stated, what was observed, what is independently evidenced, what is derived, and what remains unknown**. That distinction is the principal safeguard against turning a comparative study into a retrospective provenance claim.
