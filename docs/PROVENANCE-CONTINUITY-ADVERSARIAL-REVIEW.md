# DPIE-PC-0.1 Adversarial Review

**Department of Provenance & Epistemic Integrity**  
**Target:** DPIE-PC-0.1  
**Review mode:** adversarial pre-extension review  
**Date:** 2026-08-28

> This review is paired with `DPIE-PC-CORE-0.1`, which reduces the attack surface to explicit invariants and testable state transitions.

## 1. Verdict

The conceptual model survives the original ten §18 cases, but a specification-only review is insufficient. The principal remaining risk is **provenance strengthening without new admissible evidence**.

The hardening work therefore defines four distinct objects:

```text
IDENTITY → LINEAGE → EVIDENCE → EPISTEMIC STATUS
```

and requires provenance loss, inference, verification, identity mapping, and presentation state to remain distinguishable.

## 2. Hardening findings

### H1 — Material transformation identity

Material transformations require independently addressable output identity when continuity is claimed. Otherwise an implementation can mutate content while preserving the appearance of a single historical artifact.

### H2 — Aggregation

Aggregations require explicit multi-predecessor representation and dependency completeness. A singular `source` field is inadequate where multiple predecessors materially determine the result.

### H3 — Metadata inheritance

Metadata cannot be copied forward merely because content survives conversion. Preservation requires an explicit basis; otherwise continuity is degraded or broken.

### H4 — Presentation integrity

The UI is part of the conformance surface. A machine state of `UNRESOLVED`, `CONFLICTED`, `INFERRED`, or `BROKEN` cannot be rendered as `CONTINUOUS` without an evidence-bearing transition.

### H5 — Transitive non-collapse

A→B→C establishes graph reachability, not direct A→C evidence. Implementations must preserve the distinction between direct edges and derived reachability.

### H6 — Temporal separation

Event, recording, publication, verification, and retrieval times are distinct facts. Substitution between them is provenance laundering.

### H7 — Unknown semantics

Null, missing, unavailable, redacted, and unknown values must not silently acquire positive or negative meaning.

### H8 — Schema loss

A weaker export schema must not inherit the semantics of a richer schema after material uncertainty/status information has been dropped. The loss must remain visible.

## 3. Adversarial suite

The expanded suite contains 30 attacks in `CONFORMANCE-ATTACKS-0.1.md`, including identity collision, fork/merge collapse, replay, cross-system identity drift, partial transformations, temporal inversion, unauthorized edges, transitive shortcuts, null semantics, schema downgrade, authority substitution, adversarial duplication, edge deletion, and verification-time substitution.

## 4. Core invariant

The implementation must be able to explain every material upward provenance transition:

```text
before_state
     ↓
new admissible evidence
     ↓
after_state
```

Copying, hashing, normalization, publication, verification, repetition, re-upload, authority claims, similarity, and model confidence are not sufficient by themselves.

## 5. Gate

No subsequent normative layer should be added until an implementation can pass the attack oracle and preserve the following distinctions:

```text
CONTINUOUS
DEGRADED
BROKEN
UNRESOLVED
CONFLICTED
INFERRED
```

The system must fail closed against unjustified provenance strengthening.

## 6. Core proposition

> **A provenance system is conforming only when it can preserve the difference between what is known, what is connected, what is supported, what is inferred, and what has been lost.**
