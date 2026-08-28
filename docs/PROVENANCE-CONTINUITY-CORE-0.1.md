# DPIE Provenance Continuity Core

**Specification:** DPIE-PC-CORE-0.1  
**Parent:** DPIE-PC-0.1  
**Status:** Experimental hardening layer  
**Date:** 2026-08-28

## 1. Purpose

This document reduces provenance continuity to a small set of testable invariants. It is intentionally narrower than DPIE-PC-0.1.

The core question is:

> Given an artifact and a claimed predecessor relationship, what evidence permits the relationship to be classified as continuous rather than merely plausible?

## 2. Four distinct objects

An implementation SHALL distinguish at minimum:

1. **Identity** — which artifact/event instance is being referred to.
2. **Lineage** — the claimed relationship between predecessor, transition, and successor.
3. **Evidence** — records supporting or contradicting that relationship.
4. **Epistemic status** — the status of the claim made by the relationship.

No field representing one of these concepts SHALL be treated as automatically establishing another.

## 3. Provenance state

A relationship SHALL have an explicit continuity state:

```text
CONTINUOUS
DEGRADED
BROKEN
UNRESOLVED
CONFLICTED
INFERRED
```

Implementations MAY add states, but SHALL NOT collapse these states where the distinction is material to auditability.

### 3.1 CONTINUOUS

The relevant predecessor relationship is resolvable and supported by admissible evidence sufficient for the applicable rule set.

### 3.2 DEGRADED

The relationship remains partially resolvable, but one or more material provenance properties are unavailable, qualified, or weakened.

### 3.3 BROKEN

A material relationship required for continuity is known to be unavailable or absent.

### 3.4 UNRESOLVED

The available evidence does not determine which relationship or state is correct.

### 3.5 CONFLICTED

Material provenance assertions or evidence support incompatible relationships or states.

### 3.6 INFERRED

The relationship is a reasoned candidate rather than an established historical relationship.

## 4. Non-strengthening invariant

Let `S(x)` be the provenance state of a relationship and let `E` be the admissible evidence currently available.

Processing an artifact, copying metadata, hashing, normalization, publication, verification, re-upload, repetition, or inference SHALL NOT increase provenance status unless new admissible evidence is introduced that justifies the increase under the applicable rule set.

Informally:

```text
processing alone ≠ new evidence
```

A system SHALL be able to identify the evidence that caused any material upward state transition.

## 5. Loss monotonicity

Once a material provenance fact becomes unavailable, a downstream transformation SHALL NOT represent that fact as preserved unless the transformation has an explicit preservation basis.

Therefore:

```text
known → lost
```

MAY become `known → restored-as-evidenced` only when new admissible evidence establishes the fact.

It SHALL NOT become:

```text
known → lost → silently known
```

## 6. Identity invariant

Artifact identity and artifact content SHALL be independently represented.

The following operations SHALL NOT, by themselves, establish artifact identity:

- byte similarity;
- semantic similarity;
- normalization equivalence;
- hash equality across uncontrolled identity domains;
- filename equality;
- URL equality;
- publication location;
- author/account equality.

An explicit identity mapping MAY establish a relationship between identifiers across systems, but that mapping is itself a provenance assertion requiring evidence and provenance state.

## 7. Edge evidence invariant

A provenance edge is not self-authenticating because it exists in a provenance store.

For every material edge, an implementation SHALL be able to distinguish:

```text
EDGE ASSERTION
EDGE EVIDENCE
EDGE VERIFICATION
EDGE AUTHORITY
```

These MAY reference the same underlying record, but they SHALL remain conceptually distinguishable.

## 8. Transitive non-collapse

Given:

```text
A → B
B → C
```

an implementation MAY derive:

```text
A → C
```

as a transitive lineage result, but SHALL NOT represent `A → C` as a directly observed edge unless direct evidence exists.

Derived graph reachability is not direct provenance evidence.

## 9. Independence invariant

If:

```text
A → B
A → C
A → D
```

then B, C, and D SHALL NOT automatically count as three independent sources for claims inherited from A.

Independence analysis SHALL account for shared provenance dependencies where those dependencies materially affect corroboration.

## 10. Temporal invariant

The following SHALL remain distinguishable:

- event time;
- recording time;
- publication time;
- verification time;
- retrieval time.

One timestamp SHALL NOT silently substitute for another.

Chronological inconsistency SHALL remain visible as a contradiction or unresolved condition rather than being repaired by reordering records.

## 11. Verification non-creation

Verification evaluates evidence or conformance to a rule set. Verification SHALL NOT create the historical event or provenance relationship being evaluated.

A successful verification therefore establishes, at most, a verification result over identified inputs and rules.

It does not establish authorship, origin, truth, or historical occurrence unless the verification procedure itself has independent evidence sufficient for that claim.

## 12. Presentation invariant

The externally presented provenance state SHALL NOT be stronger than the machine-readable state without an explicit evidence-bearing transition that justifies the change.

A UI that displays an unresolved, conflicted, inferred, or broken relationship as continuous is non-conforming even if the underlying database preserves the weaker state.

## 13. Schema-loss invariant

When serialization, export, conversion, or schema downgrade removes a material provenance property, the resulting artifact SHALL carry a loss/degradation condition where continuity is affected.

A weaker schema SHALL NOT silently acquire the semantics of the richer schema.

## 14. Rollback, fork, merge, concurrency

A rollback, fork, merge, or concurrent successor is a new graph event.

It SHALL NOT erase or rewrite prior historical states merely because a later state becomes canonical for operational purposes.

Concurrent transitions SHALL remain distinguishable where ordering is unknown or genuinely concurrent.

## 15. Minimal continuity proof

An implementation claiming `CONTINUOUS` for a material relationship SHOULD be able to answer:

1. What predecessor identity is claimed?
2. What successor identity is claimed?
3. What transition connects them?
4. What evidence supports the transition?
5. What actor/process produced or recorded it, or is that unknown?
6. What time facts are established, and which are merely recorded?
7. What transformations occurred?
8. What information was lost?
9. What verification was performed, by what rule set?
10. What authority, if any, makes the relationship admissible?

If material answers are unavailable, the implementation SHALL not silently treat the relationship as fully continuous.

## 16. State-transition discipline

A conforming implementation SHOULD make material upward transitions explicit:

```text
UNRESOLVED ──new evidence──> CONTINUOUS
INFERRED   ──new evidence──> CONTINUOUS
DEGRADED   ──new evidence──> CONTINUOUS
```

The following SHALL NOT constitute sufficient transition evidence by themselves:

```text
copy
hash
similarity
normalization
publication
verification
repetition
re-upload
authority claim
model confidence
```

## 17. Conformance principle

The strongest implementation is not the one that produces the longest lineage.

It is the one that can demonstrate, for every material relationship:

```text
IDENTITY
  ↓
TRANSITION
  ↓
EVIDENCE
  ↓
STATUS
  ↓
LIMITATIONS
```

and can show why the status did not become stronger without new admissible evidence.

## 18. Core proposition

> **A provenance system is conforming only when it can preserve the difference between what is known, what is connected, what is supported, what is inferred, and what has been lost.**
