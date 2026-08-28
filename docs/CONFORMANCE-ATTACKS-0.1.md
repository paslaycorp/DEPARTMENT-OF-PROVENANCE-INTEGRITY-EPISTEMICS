# DPIE-PC-0.1 Conformance Attack Matrix

**Target:** DPIE-PC-CORE-0.1  
**Purpose:** implementation-level adversarial testing

This matrix is designed so an implementation can be tested without relying on prose interpretation.

## Test contract

For each attack, provide:

- input artifacts/events;
- claimed edges;
- available evidence;
- transformation operations;
- expected continuity state;
- actual continuity state;
- evidence responsible for any upward state transition.

A test FAILS if the implementation reports a stronger state than the evidence permits.

| ID | Attack | Expected result |
|---|---|---|
| A01 | Copy with no attribution | DEGRADED or UNRESOLVED |
| A02 | Substantive edit represented as copy | DEGRADED or BROKEN |
| A03 | AI output with missing source/input lineage | INFERRED or UNRESOLVED |
| A04 | Aggregate with omitted parent | DEGRADED or BROKEN |
| A05 | Two conflicting predecessors | CONFLICTED |
| A06 | Deleted predecessor with plausible replacement | UNRESOLVED or INFERRED |
| A07 | Recorded timestamp without verification | DEGRADED or UNRESOLVED |
| A08 | Publication used as authorship proof | DEGRADED or UNRESOLVED |
| A09 | Re-upload under new identifier | UNRESOLVED unless identity mapping evidence exists |
| A10 | Metadata stripped by conversion | DEGRADED or BROKEN |
| A11 | Hash match used as authorship | Must not strengthen state |
| A12 | A→B→C presented as direct A→C evidence | INFERRED for A→C unless direct evidence exists |
| A13 | Ten derivatives of one source counted as ten independent sources | Independence remains shared/dependent |
| A14 | Null actor interpreted as "no actor" | FAIL; unknown must remain unknown |
| A15 | Null timestamp interpreted as "no event time" | FAIL; unknown must remain unknown |
| A16 | Rich-schema export to weak schema | DEGRADED where material fields are lost |
| A17 | Rollback after publication | New transition; prior history retained |
| A18 | Fork with incompatible successors | Both branches retained |
| A19 | Concurrent successors with unknown order | CONFLICTED or explicitly concurrent |
| A20 | Unauthorized actor asserts edge | Assertion recorded; normative provenance not established |
| A21 | Verifier approves structurally consistent chain | Verification result only; no origin creation |
| A22 | UI displays unresolved edge as continuous | FAIL |
| A23 | Candidate mirror substituted for deleted source | INFERRED or UNRESOLVED |
| A24 | Normalized artifacts declared identical | Identity mapping required |
| A25 | Verification time substituted for event time | FAIL |
| A26 | Provenance metadata copied after preservation cannot be established | DEGRADED/BROKEN |
| A27 | Canonical source silently replaces historical predecessor | FAIL |
| A28 | Edge deleted while endpoints remain | Missing history must remain detectable |
| A29 | Cross-system ID remapping without mapping event | DEGRADED/UNRESOLVED |
| A30 | Repeated assertion increases confidence without new evidence | FAIL |

## Required anti-laundering assertion

For every test:

```text
if state_after > state_before:
    require(new_admissible_evidence)
    require(evidence_reference)
```

If either requirement is absent, the upward transition is non-conforming.

## Reference scenarios

### Scenario 1 — Silent repair

```text
A --transform--> B
B loses predecessor metadata
C is created from B
```

Expected: C cannot silently inherit a fully continuous A→C chain.

### Scenario 2 — Verification laundering

```text
A --?--> B
verifier checks that B's metadata is internally consistent
```

Expected: verification may establish consistency of the record; it does not establish the missing A→B event.

### Scenario 3 — Corroboration laundering

```text
A → B
A → C
A → D
```

Expected: B/C/D are three derivatives, not automatically three independent sources.

### Scenario 4 — Transitive shortcut

```text
A → B → C
```

Expected: graph reachability establishes possible lineage; it does not create direct A→C evidence.

### Scenario 5 — Schema downgrade

```text
rich(A) --export--> weak(B)
```

If B cannot carry uncertainty, actor, temporal status, or transformation information material to continuity, B must expose the resulting loss/degradation.

## Pass criterion

A DPIE implementation passes only if it fails closed against provenance strengthening without new admissible evidence and preserves provenance loss rather than silently repairing it.
