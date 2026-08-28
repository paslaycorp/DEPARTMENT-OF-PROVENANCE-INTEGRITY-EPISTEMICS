# DPIE Provenance Continuity Specification

**Department of Provenance & Epistemic Integrity**

**Specification:** DPIE-PC-0.1  
**Status:** Foundational  
**Established:** 2026-08-28  
**Parent Specification:** DPIE-SCOPE-0.1

## 1. Purpose

This specification defines the requirements for preserving provenance across the creation, transformation, verification, publication, and derivation of information artifacts.

DPIE treats provenance as a continuing relationship rather than a property that terminates at the first recorded artifact.

## 2. Provenance Continuity

Provenance continuity is the ability to resolve an artifact's relationship to relevant predecessor artifacts, events, authorities, and evidence across authorized state transitions.

Provenance continuity is distinct from provenance existence.

An artifact MAY have provenance while its continuity is broken.

A broken provenance chain SHALL remain represented as a provenance condition rather than being silently repaired by inference or assumption.

## 3. Core Model

A provenance-bearing sequence MAY contain states such as:

```text
Artifact₀
   │
   ├── CREATED
   ▼
Artifact₁
   │
   ├── TRANSFORMED
   ▼
Artifact₂
   │
   ├── VERIFIED
   ▼
Artifact₃
   │
   ├── PUBLISHED
   ▼
Artifact₄
   │
   └── DERIVED
        ▼
     Artifact₅
```

Each material transition SHOULD be represented as an explicit provenance relation.

A later artifact SHALL NOT silently replace the historical identity of its predecessor.

## 4. Continuity Invariant

A provenance-bearing transformation SHALL preserve a resolvable relationship to its relevant predecessor unless that relationship is unavailable.

Where the relationship is unavailable, the resulting state SHALL identify the provenance loss as unknown, pending, unresolved, or otherwise explicitly characterized.

Absence of provenance information SHALL NOT be silently converted into continuity.

## 5. Transformation Rule

A transformation changes the representation, structure, content, interpretation, or state of an artifact.

Examples include:

- transcription;
- OCR;
- parsing;
- normalization;
- extraction;
- summarization;
- translation;
- model inference;
- human interpretation;
- format conversion;
- aggregation.

Where practical, both input and output artifacts SHOULD remain independently identifiable.

The transformation event SHOULD identify the operation, applicable actor or process, time, and governing specification where those properties are available.

## 6. Derivation Rule

A derived artifact SHALL NOT acquire stronger epistemic status merely because it is derived from another artifact.

Derivation establishes lineage. It does not, by itself, establish truth, correctness, authenticity, independence, or authority.

A derivative MAY inherit relevant provenance relationships from its predecessors, but inherited provenance SHALL remain distinguishable from direct observation or direct authorship.

## 7. Identity Preservation

Artifact identity SHALL remain distinct from artifact content.

A change in content SHALL NOT be represented as though the prior artifact itself had been rewritten when the historical artifact remains identifiable.

Where content changes materially, the resulting artifact SHOULD receive a distinct identity or version identifier.

Cryptographic hashes MAY provide artifact identity evidence but SHALL NOT by themselves establish authorship, truth, or authority.

## 8. Provenance Edge

A provenance edge represents a material relationship between artifacts or between an artifact and a provenance event.

A provenance edge SHOULD identify, where applicable:

- predecessor;
- successor;
- relationship type;
- actor or process;
- time;
- transformation;
- specification or authority;
- supporting evidence;
- integrity status;
- uncertainty or limitations.

The absence of an optional property SHALL NOT be interpreted as proof that the property did not exist.

## 9. Evidence and Epistemic Status

Provenance continuity SHALL NOT collapse epistemic distinctions.

In particular:

**OBSERVED → EVIDENCED → DERIVED → INFERRED → PREDICTED → SIMULATED / COUNTERFACTUAL**

A provenance chain may show how an inference was produced without converting the inference into an observation.

A later artifact SHALL NOT be promoted to a stronger epistemic state solely because it has a longer provenance chain.

## 10. Independence

Lineage SHALL be considered when evaluating corroboration and independence.

Separate artifacts derived from a common predecessor SHALL NOT automatically constitute independent evidence.

A provenance graph SHOULD expose shared dependencies where those dependencies materially affect an independence determination.

## 11. Provenance Loss

Provenance loss occurs when a material relationship required to reconstruct relevant lineage is unavailable, destroyed, ambiguous, or otherwise unresolvable.

A system encountering provenance loss SHALL NOT manufacture the missing relationship.

The system MAY record a candidate relationship as an inference, provided that the relationship is explicitly represented as inferred and is not presented as established provenance.

## 12. Historical Preservation

Historical states SHALL be preserved where they are material to provenance, integrity, attribution, chronology, or auditability.

A correction SHALL create or preserve a relationship between the prior state and corrected state.

A correction SHALL NOT erase the existence of the prior state merely because the prior state is no longer preferred.

## 13. Publication Continuity

Publication SHALL be treated as a provenance event rather than as a replacement of prior provenance.

A published artifact SHOULD retain or reference its relevant source, version, publication event, and transformation history where available.

Publication does not establish factual correctness merely because the artifact became publicly accessible.

## 14. AI-Mediated Transformation

Where an artificial intelligence system materially transforms or derives information, the AI-mediated operation SHOULD be represented as a transformation or derivation event.

AI output SHALL NOT be represented as direct observation merely because the system produced the output.

Model-generated content SHALL remain distinguishable from source evidence and from human-authored source material.

## 15. Continuity and Verification

Verification MAY evaluate whether a provenance chain satisfies an identified rule set.

Verification SHALL NOT create the missing provenance that it evaluates.

A verification result SHALL remain distinguishable from the provenance evidence on which the result depends.

A successful verification SHALL NOT retroactively convert an unproven provenance relationship into an observed historical fact.

## 16. Continuity and Authority

No provenance edge acquires normative authority merely because it is recorded by an implementation.

The meaning and admissibility of provenance relationships SHALL derive from the applicable specification, governance mechanism, or authorized decision structure.

Implementation records provenance; implementation does not unilaterally define historical truth.

## 17. Minimum Continuity Record

Where a material provenance transition is represented, the minimum record SHOULD contain:

- source artifact identity;
- resulting artifact identity;
- relationship or transition type;
- time or temporal status;
- actor, process, or unknown status;
- applicable specification or authority where relevant;
- integrity information where available;
- limitations or unresolved fields.

Implementations MAY add additional fields without weakening these distinctions.

## 18. Adversarial Cases

A conforming implementation SHOULD be evaluated against at least the following cases:

1. copy without attribution;
2. transformation that changes substantive content;
3. AI-generated derivative;
4. aggregation of multiple sources;
5. conflicting predecessors;
6. deleted predecessor;
7. unverifiable timestamp;
8. unsigned publication;
9. re-upload under a different identity;
10. provenance metadata stripped during conversion.

For each case, the implementation SHOULD demonstrate whether continuity is preserved, degraded, broken, or unresolved.

## 19. Non-Manufacture of Continuity

A system SHALL NOT manufacture provenance continuity by:

- treating repetition as independent lineage;
- treating similarity as identity;
- treating inference as historical observation;
- treating publication as authorship;
- treating verification as proof of origin;
- treating a missing predecessor as though it were known;
- treating an implementation assertion as historical evidence.

## 20. Relationship to DPIE-SCOPE-0.1

This specification extends the provenance, evidence, transformation, integrity, epistemic, verification, attribution, and historical boundaries established by DPIE-SCOPE-0.1.

It SHALL be interpreted consistently with that specification and its applicable version.

Where this specification is more specific, its provisions govern provenance continuity.

## 21. Core Principle

> **Provenance does not end when information changes hands, formats, systems, or authors. The chain either continues, or its break is itself part of the record.**
