# DPIE-PC-0.1 Adversarial Review

**Department of Provenance & Epistemic Integrity**  
**Target:** DPIE-PC-0.1  
**Review mode:** adversarial pre-extension review  
**Date:** 2026-08-28

## 1. Review objective

This review attacks the continuity model before any additional specification layer is added. The purpose is not to prove that continuity exists, but to determine whether an implementation can falsely report continuity while remaining superficially compliant.

The governing distinction is:

> **Provenance continuity ≠ provenance existence.**

A conforming implementation must preserve uncertainty, loss, conflict, and identity ambiguity rather than converting them into a clean-looking lineage.

## 2. Adversarial matrix

| # | Attack case | Expected condition | Failure mode to detect | Result |
|---|---|---|---|---|
| 1 | Copy without attribution | Degraded / unresolved | Copy is treated as independently authored or fully continuous | PASS — attribution is not manufactured |
| 2 | Substantive transformation | Continuous only with explicit transformation | Output is treated as equivalent to source | PASS — transformation is required to remain visible |
| 3 | AI-generated derivative | Derived, AI-mediated | Model output is represented as observation or source-authored | PASS — AI operation remains distinguishable |
| 4 | Multi-source aggregation | Multi-parent lineage | Aggregate receives a single synthetic predecessor | PASS — shared/multiple dependencies remain representable |
| 5 | Conflicting predecessors | Conflicted / unresolved | System chooses one predecessor silently | PASS — conflict cannot become continuity by selection |
| 6 | Deleted predecessor | Broken / unavailable | Missing predecessor is reconstructed as known | PASS — loss remains explicit |
| 7 | Unverifiable timestamp | Temporal status unresolved | Timestamp is treated as verified merely because recorded | PASS — unverifiable time remains qualified |
| 8 | Unsigned publication | Published, attribution/integrity limited | Publication is treated as proof of origin or authority | PASS — publication does not establish authorship |
| 9 | Re-upload under different identity | Identity ambiguity / possible continuity | Similarity or content match is treated as identity | PASS — identity is distinct from content |
| 10 | Metadata stripped in conversion | Continuity degraded / broken | Conversion silently preserves a claim that metadata survived | PASS — provenance loss is representable |

## 3. Attack findings

### 3.1 Copy without attribution

The specification correctly prevents attribution from being inferred from mere possession of a copy. A copied artifact can remain materially related to a predecessor while the actor or attribution field is unknown.

**Residual risk:** an implementation may display a clean source field while internally retaining an unknown actor. Conformance testing should therefore inspect machine-readable state, not only presentation.

### 3.2 Substantive transformation

The transformation rule is strong enough to reject identity collapse, but the phrase "where practical" around independent identification leaves an implementation discretion point. A system could exploit that discretion to emit transformed content without a durable output identity.

**Required hardening:** for material transformations, independent output identity should be mandatory where the implementation claims continuity across the transition.

### 3.3 AI-generated derivative

The AI rule blocks the most serious epistemic substitution: generated output cannot become observation merely through generation. However, provenance of the model operation itself can remain underspecified.

**Residual risk:** model/version, prompt or input set, execution context, and post-processing may be omitted while the artifact is still labeled "AI-mediated."

### 3.4 Aggregation

Multiple predecessors are permitted by the model, but the minimum record is phrased around a singular source artifact identity. That is insufficient for an aggregation whose meaning depends materially on several inputs.

**Required hardening:** permit and, where applicable, require a set of predecessor identities and explicit dependency completeness status.

### 3.5 Conflicting predecessors

The unresolved/conflict logic prevents silent winner selection. This is a key continuity safeguard.

**Residual risk:** a system can preserve both predecessors but still mark one as the canonical source in a UI without exposing the conflict. Auditability therefore requires conflict state to survive presentation layers.

### 3.6 Deleted predecessor

The specification correctly distinguishes unavailable lineage from known lineage. It also prohibits reconstructing the missing relationship as fact.

**Residual risk:** external caches, mirrors, or similarity search can tempt an implementation to silently substitute a candidate artifact.

### 3.7 Unverifiable timestamp

The minimum record allows temporal status, and the text permits unresolved fields. This is sufficient to prevent an unverifiable timestamp from automatically becoming verified history.

**Residual risk:** "time recorded" and "time verified" can be conflated unless represented as separate statuses.

### 3.8 Unsigned publication

The publication rule correctly denies publication the power to establish authorship or truth. This is an important separation between dissemination and authority.

**Residual risk:** publication systems commonly imply authenticity through account identity, domain identity, or UI badges. DPIE should treat those as evidence-bearing assertions, not as automatic provenance facts.

### 3.9 Re-upload under a different identity

The identity-preservation rule is appropriately resistant to similarity-based identity claims. Content equality is not sufficient to establish artifact identity.

**Residual risk:** exact hash equality may be overinterpreted. The specification already says hashes do not establish authorship, truth, or authority; conformance tests should explicitly verify that implementations do not promote hash matches into those claims.

### 3.10 Metadata stripping during conversion

This is the strongest attack against continuity because the content can remain visually identical while the lineage record disappears. The current specification permits the break to be represented, which is correct.

**Residual risk:** an implementation may copy old metadata forward after a conversion even though the conversion process did not preserve it. This creates fabricated continuity rather than merely losing continuity.

**Required hardening:** metadata inheritance must require an explicit preservation basis; absence of proof of preservation must not be treated as preservation.

## 4. Cross-cutting attacks

### 4.1 Presentation laundering

A system may preserve uncertainty internally but render a definitive lineage externally. This is a conformance failure because provenance conditions are part of the epistemic record.

### 4.2 Canonicalization laundering

A system may designate a canonical artifact, source, timestamp, or predecessor for operational convenience and accidentally convert that designation into historical truth.

### 4.3 Confidence laundering

A probabilistic or inferred relationship may be displayed with confidence scoring but without its epistemic class. Numerical confidence must not erase the distinction between established and inferred provenance.

### 4.4 Chain-length laundering

A long chain may appear more trustworthy than a short chain. DPIE-PC-0.1 already rejects this at the epistemic layer; implementations should test that ranking, UI, and search behavior do not reintroduce the error.

### 4.5 Repetition laundering

Repeated claims across derivatives of the same predecessor must not be counted as independent corroboration. Shared dependency must remain visible where it affects independence.

## 5. Adversarial verdict

**DPIE-PC-0.1 survives the ten encoded attack cases at the specification level, with three material hardening points before the next layer:**

1. **Material transformations:** require durable output identity when continuity is claimed.
2. **Aggregation:** explicitly support multiple predecessors and dependency completeness.
3. **Metadata preservation:** require an explicit basis before inheriting provenance metadata across conversion.

A fourth cross-cutting requirement should be treated as a conformance concern:

4. **Presentation integrity:** uncertainty, conflict, provenance loss, and inferred relationships must survive the presentation layer and not be flattened into definitive lineage.

## 6. Gate for the next specification layer

Do not add another normative layer until an implementation-level conformance test can distinguish at least these states:

```text
CONTINUOUS
DEGRADED
BROKEN
UNRESOLVED
CONFLICTED
INFERRED
```

The test harness should also verify that a state transition cannot silently improve provenance status merely by copying, transforming, publishing, hashing, re-uploading, or repeatedly citing an artifact.

**Conclusion:** the core continuity boundary is defensible. The remaining risk is less the graph model than implementation behavior at identity, aggregation, metadata inheritance, and presentation boundaries.
