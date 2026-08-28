# DPIE-PC-0.1 Hostile Audit

**Target:** `docs/PROVENANCE-CONTINUITY.md`  
**Target ref:** `architecture/dpie-scope-0.1`  
**Target content SHA:** `3c35f07ace5b186864769446a25fe2e1ed8473ab`  
**Review mode:** adversarial / fail-closed  
**Date:** 2026-08-28

## Executive verdict

**DPIE-PC-0.1 should not be treated as a sufficiently testable normative standard yet.** Its core prohibitions are directionally coherent, but critical controls are expressed as SHOULD/MAY, several central terms are undefined, and the specification does not define an evidence/admissibility model capable of making provenance strengthening objectively testable.

The most serious defect is not that the document permits obvious fabrication. It is that a system can comply with the SHALL requirements while producing records whose epistemic meaning is underdetermined. The document currently constrains bad presentation more strongly than it constrains the evidentiary conditions for a positive continuity claim.

## Normative inventory

### SHALL / SHALL NOT

1. §2: broken chain SHALL remain represented as a provenance condition.
2. §3: later artifact SHALL NOT silently replace predecessor identity.
3. §4: transformation SHALL preserve a resolvable predecessor relationship unless unavailable.
4. §4: unavailable relationship SHALL identify provenance loss explicitly.
5. §4: absence of provenance SHALL NOT silently become continuity.
6. §6: derived artifact SHALL NOT gain stronger epistemic status merely through derivation.
7. §6: inherited provenance SHALL remain distinguishable from direct observation/authorship.
8. §7: artifact identity SHALL remain distinct from content.
9. §7: content change SHALL NOT be represented as predecessor rewrite where historical identity remains identifiable.
10. §7: hashes SHALL NOT alone establish authorship, truth, or authority.
11. §8: absence of optional property SHALL NOT be interpreted as proof it did not exist.
12. §9: provenance continuity SHALL NOT collapse epistemic distinctions.
13. §9: later artifact SHALL NOT be promoted merely because its chain is longer.
14. §10: lineage SHALL be considered in corroboration/independence.
15. §10: common-predecessor derivatives SHALL NOT automatically constitute independent evidence.
16. §11: system SHALL NOT manufacture missing relationship.
17. §12: material historical states SHALL be preserved.
18. §12: correction SHALL create/preserve prior→corrected relationship.
19. §12: correction SHALL NOT erase prior state.
20. §13: publication SHALL be treated as provenance event.
21. §14: AI output SHALL NOT be represented as direct observation merely because system produced it.
22. §14: model-generated content SHALL remain distinguishable from source evidence and human-authored source material.
23. §15: verification SHALL NOT create missing provenance.
24. §15: verification result SHALL remain distinguishable from evidence.
25. §15: successful verification SHALL NOT retroactively convert unproven provenance into observed history.
26. §16: meaning/admissibility SHALL derive from applicable specification/governance/authorized structure.
27. §20: spec SHALL be interpreted consistently with parent specification.
28. §20: where more specific, this spec SHALL govern continuity.
29. §19: system SHALL NOT manufacture continuity through seven listed laundering mechanisms.

### SHOULD / SHOULD NOT

1. §3: material transition SHOULD be explicit.
2. §5: input/output artifacts SHOULD remain independently identifiable where practical.
3. §5: transformation event SHOULD identify operation, actor/process, time, governing specification where available.
4. §7: material content change SHOULD receive distinct identity/version.
5. §8: edge SHOULD identify predecessor, successor, type, actor, time, transformation, authority, evidence, integrity, uncertainty/limitations where applicable.
6. §10: graph SHOULD expose shared dependencies where materially relevant.
7. §13: publication SHOULD retain/reference source, version, publication event, transformation history where available.
8. §14: AI-mediated operation SHOULD be represented.
9. §17: minimum continuity record SHOULD contain required fields.
10. §18: implementation SHOULD be evaluated against adversarial cases.
11. §18: implementation SHOULD demonstrate resulting continuity condition.

### MAY

1. §2: artifact MAY have provenance while continuity is broken.
2. §3: sequence MAY contain illustrative states.
3. §6: derivative MAY inherit relevant provenance.
4. §7: hashes MAY provide identity evidence.
5. §11: candidate relationship MAY be recorded as inference.
6. §15: verification MAY evaluate a rule set.
7. §17: implementations MAY add fields.

## FATAL / CRITICAL findings

### F-01 — Positive continuity has no evidentiary threshold

**Attack:** An implementation creates an edge `A --DERIVED--> B`, records actor/process/time, and marks the edge continuous. Nothing in the document defines the minimum evidence required before the positive continuity claim is permissible.

**Why it works:** §4 requires a resolvable relationship but never defines what makes a relationship resolvable. §8 makes supporting evidence a SHOULD field, not a prerequisite. §17 makes the minimum record a SHOULD.

**Result:** A record of a relationship can be mistaken for evidence of the relationship.

**Severity:** FATAL.

**Repair direction:** Define a positive continuity predicate and an admissible-evidence threshold. A continuity assertion must be distinguishable from the evidence supporting it.

### F-02 — "Admissibility" is delegated away

§16 says meaning and admissibility SHALL derive from a specification, governance mechanism, or authorized decision structure. But DPIE-PC-0.1 does not specify the minimum properties those external structures must satisfy.

**Attack:** Governance declares a self-authored provenance record admissible. Under §16 the declaration is valid as a source of admissibility, while §19 prohibits implementation assertion as historical evidence. The boundary between admissibility and evidence is therefore unresolved.

**Severity:** FATAL unless the parent specification closes the gap explicitly.

### F-03 — Evidence is not recursively bounded

The document uses "supporting evidence" but never specifies whether evidence can itself be an artifact governed by DPIE, and if so how its provenance is established.

**Attack:** E is used as evidence that A→B. E is itself a derivative of A or B. E then supports the edge, and the edge supports E's provenance. A circular support structure can be recorded without violating an explicit SHALL.

**Severity:** FATAL for evidence-based conformance.

### F-04 — Material transitions can be omitted while remaining formally compliant

§3 says each material transition SHOULD be explicit. An adversarial implementation can ignore SHOULD requirements while complying with every SHALL.

**Attack:** A→B is a material transformation, but no explicit edge is recorded. No SHALL in §3 requires its recording. §4 applies to a "provenance-bearing transformation," but the implementation can deny that the transformation is provenance-bearing because the record is absent.

**Severity:** CRITICAL/FATAL depending on whether §4 is interpreted independently of record creation.

### F-05 — Independent identity is optional exactly where continuity needs it

§5 says input/output independent identity SHOULD remain where practical; §7 says distinct identity for material change SHOULD occur.

**Attack:** A materially transformed B retains A's identifier. The implementation records a transformation relation. The historical identity distinction is now dependent on whether the implementation voluntarily follows SHOULD guidance.

**Severity:** CRITICAL.

### F-06 — "Resolved" is not operationally defined

Continuity is "the ability to resolve" a relationship, and §4 requires a resolvable relationship. But no resolution procedure or acceptance test exists.

**Attack:** System X considers a signed actor assertion sufficient to resolve A→B. System Y requires reproducible transformation evidence. Both claim compliance.

**Severity:** FATAL for interoperability/conformance.

### F-07 — The epistemic ladder is ambiguous and potentially non-monotonic

§9 presents `OBSERVED → EVIDENCED → DERIVED → INFERRED → PREDICTED → SIMULATED / COUNTERFACTUAL` but never states whether this is an ordering, a taxonomy, a lifecycle, or merely examples.

**Attack:** A derivative can be both derived and evidenced. An inference can be evidenced. A simulation can be observed as an execution while its output remains simulated. A single linear arrow cannot encode these dimensions without loss.

**Severity:** CRITICAL.

## CRITICAL semantic gaps

### C-01 — "Relevant predecessor" is undefined

The phrase appears in §§2 and 4. Without criteria for relevance, an implementation can omit inconvenient predecessors and remain compliant.

### C-02 — "Material" is undefined

Material transition, material content change, material provenance relationship, and material historical state all depend on an undefined threshold.

### C-03 — "Available" is undefined

"Where properties are available" permits arbitrary omission unless availability itself has a defined test.

### C-04 — "Authorized state transition" is undefined

§2 places continuity across authorized transitions, but authorization is not specified. A malicious implementation can classify a disputed transition as unauthorized and thereby avoid continuity obligations.

### C-05 — Actor/process/time are not evidence-bearing by default

A recorded actor, process, or time field is an assertion. The specification does not distinguish asserted, attested, independently corroborated, cryptographically bound, and verified values.

### C-06 — Verification scope is unconstrained

§15 permits verification against an "identified rule set" without requiring the verifier to establish what the rule set can actually prove.

### C-07 — Publication can preserve a false provenance claim

§13 correctly denies publication the power to establish factual correctness, but it does not explicitly deny publication the power to strengthen provenance status. A published false lineage can become socially authoritative without violating the text.

### C-08 — AI transparency is label-level, not process-level

§14 requires distinguishability but makes representation of the AI operation itself a SHOULD. "AI-mediated" can therefore become a label without sufficient causal detail.

### C-09 — Minimum record is not actually mandatory

The heading says "Minimum Continuity Record," but §17 uses SHOULD throughout. A system can omit the supposed minimum fields and remain formally compliant if all SHALL requirements are otherwise met.

### C-10 — Adversarial evaluation is optional

§18 is entirely SHOULD. A system can claim conformance without executing the named adversarial cases.

## Counterexample: brokenness laundering

Kimi's preliminary objection that `BROKEN / MISSING_PREDECESSOR` itself implies knowledge is **not universally fatal**. The current §11 already allows a distinction between a missing relationship and an explicitly inferred candidate. The real defect is that the specification does not define the proposition encoded by a break.

These are epistemically different:

- `NO_KNOWN_PREDECESSOR`
- `PREDECESSOR_EXPECTED_BUT_UNAVAILABLE`
- `PREDECESSOR_CLAIMED_UNVERIFIED`
- `PREDECESSOR_INFERRED`
- `PREDECESSOR_CONFIRMED`
- `PREDECESSOR_CONFLICTED`

The current six continuity labels cannot safely carry all of those dimensions.

**Verdict:** CRITICAL, repairable.

## Graph attacks

### G-01 — Transitive-edge collapse

`A→B→C` does not imply direct evidence for `A→C`. The specification implies this through lineage language but never explicitly prohibits representing transitive closure as direct provenance evidence.

### G-02 — Fork collapse

`A→B` and `A→C` can be reduced to one canonical successor without violating an explicit SHALL if the discarded edge is not considered material. "Material" is undefined.

### G-03 — Merge laundering

`A,B→C` can be serialized as `A→C` with B hidden in metadata. §5 names aggregation but does not require explicit multi-parent semantics.

### G-04 — Edge deletion

Removing an edge while retaining endpoints is not explicitly defined as a provenance event. Historical preservation may not catch an edge-level deletion.

### G-05 — Unauthorized assertion

§16 says implementation does not define truth, but does not require an unauthorized assertion to remain separately represented from a provenance edge. An assertion can therefore enter the graph before its authority is resolved.

## Temporal attacks

### T-01 — Asserted event time vs recorded time

§8 and §17 say "time" or "temporal status" but do not define multiple temporal predicates.

A record created at T2 can assert an event occurred at T1. Nothing in DPIE-PC-0.1 establishes T1.

### T-02 — Verification time substitution

A verifier can establish that a record existed at T2 while a consumer interprets the verification as evidence of the underlying event at T1.

### T-03 — Temporal inversion

The specification does not define what happens when successor time precedes predecessor time. It should not silently reorder the graph.

## Independence attack

§10 correctly blocks automatic independence from common predecessors, but it does not define independence. A common predecessor is sufficient to block one easy false inference, not sufficient to establish independence among everything else.

Example: P1 and P2 independently copy the same upstream source S. Neither directly derives from the other, but both inherit S's epistemic weakness. The specification does not provide a general dependency-closure rule.

**Verdict:** CRITICAL.

## Schema-conversion attack

A rich DPIE record can be converted into a weak schema containing only `"Derived from prior version"`. The current specification has no explicit preservation-of-semantics rule for serialization or schema downgrade.

The historical preservation SHALL in §12 applies to historical states, but not clearly to semantic fields in an exported representation.

**Verdict:** CRITICAL.

## AI attack

The AI requirements prevent one narrow error—calling model output direct observation—but leave the continuity impact of nondeterministic or opaque transformations unspecified.

A black-box model can transform A→B where the exact model state, retrieval context, tools, prompt, and post-processing are unavailable. The spec does not say whether lineage is still continuous, degraded, or unresolved; it only says the output must remain distinguishable.

**Verdict:** CRITICAL.

## Compliance-theater attack

A system containing only:

```text
artifact_id = X
status = DEGRADED
predecessor = UNKNOWN
limitations = UNKNOWN
```

may satisfy some formal requirements because §17 is SHOULD and §18 is SHOULD. This does not necessarily violate the core, because the document does not explicitly say such a record establishes continuity. But the title "Minimum Continuity Record" and the broad language around preserving provenance create an avoidable ambiguity.

**Verdict:** REPAIRABLE.

## What survives

1. The prohibition against treating hashes as authorship/truth/authority is strong and correctly scoped.
2. §6 clearly rejects epistemic promotion by derivation alone.
3. §11 explicitly prohibits manufacturing missing relationships and permits inferred candidates only if visibly marked.
4. §12 protects prior states from correction-based erasure.
5. §15 correctly separates verification result from provenance evidence and rejects retroactive historical promotion.
6. §19 identifies several concrete laundering mechanisms and makes them SHALL NOT rules.
7. §8's rule that absent optional properties are not negative facts is valuable and should survive.

## The strongest attack

The strongest attack is **not** "the system can lie about a timestamp." It is more fundamental:

> **DPIE-PC-0.1 does not define the evidentiary conditions under which a positive provenance relationship is entitled to be called resolved/continuous.**

Therefore an implementation can comply with the explicit anti-laundering SHALL NOT rules while recording a provenance edge whose evidentiary basis is merely an assertion. The specification prevents several known bad inferences, but it does not yet define the positive proof obligation for continuity.

That makes the central distinction asymmetrical:

`BAD CLAIM → prohibited in many cases`

but not yet:

`GOOD CONTINUITY CLAIM → requires defined evidence conditions`

## Core verdict

### FATAL

- No defined positive evidentiary threshold for continuity.
- "Resolvable" is undefined.
- Evidence/admissibility lacks a bounded model and recursive provenance treatment.
- Conformance can vary materially between implementations.

### CRITICAL

- Material transitions are SHOULD.
- Independent identities are SHOULD.
- Minimum record is SHOULD.
- Adversarial testing is SHOULD.
- Material/relevant/available/authorized are undefined.
- Epistemic ladder semantics are unclear.
- Temporal predicates are collapsed.
- Independence lacks dependency-closure semantics.
- Schema downgrade lacks explicit semantic-loss handling.
- AI-mediated continuity lacks a defined degradation rule.

### REPAIRABLE

- Brokenness state vocabulary.
- Transitive-edge prohibition.
- Fork/merge/concurrency semantics.
- Edge deletion semantics.
- Assertion-vs-edge representation.
- Compliance-theater ambiguity.

### NON-FATAL

- Optional extra fields are fine if the core schema is strengthened.
- Publication as an event is conceptually sound.

### STRONG

- Identity/content distinction.
- Hash limitation.
- Derivation does not establish truth/authenticity/authority.
- Verification does not create provenance.
- Corrections cannot erase material history.
- Missing provenance cannot be silently invented.

### UNDECIDABLE

- Whether parent DPIE-SCOPE-0.1 already supplies the missing evidence/admissibility/authority definitions.
- Whether the intended continuity state is per-edge, per-artifact, per-chain, or multidimensional.

## Required pre-0.2 gate

Before another normative layer is added, DPIE should define, at minimum:

1. A formal distinction between **claim**, **evidence**, **assertion**, **verification result**, and **provenance fact**.
2. A positive continuity predicate: conditions under which a relationship may be marked continuous/resolved.
3. Evidence provenance: evidence must itself have provenance and cannot recursively bootstrap its own admissibility.
4. Explicit temporal predicates.
5. Explicit identity semantics.
6. Multi-parent, fork, merge, concurrency, and transitive-edge semantics.
7. Semantic-loss rules for schema conversion/export.
8. A rule for AI/opaque/nondeterministic transformations.
9. A state model that separates relationship status from epistemic status rather than forcing one six-value label to carry both.
10. Conversion of the controls that are essential to the central invariant from SHOULD to SHALL.

## Final answer to the rejection question

**DPIE-PC-0.1 should not be rejected as a concept. It should be rejected as a completed normative conformance specification.**

Its core is defensible. Its current positive proof obligations are not.

The project should therefore pause expansion and harden the core before adding another layer.
