# DPIE Provenance Continuity Attack Oracle

**Version:** 0.1

This oracle defines the minimum logic for detecting unjustified provenance strengthening.

## Inputs

For a claimed transition `T`:

- `before_state`
- `after_state`
- `evidence_before`
- `evidence_after`
- `operations`
- `identity_mapping`
- `loss_events`
- `verification_records`

## Oracle rules

### O1 — Upward transition requires evidence

If `after_state` is materially stronger than `before_state`, there MUST be newly admissible evidence or an explicitly defined rule that converts an existing condition without adding historical claims.

### O2 — Processing is not evidence

The following operations cannot, alone, justify an upward transition:

`COPY HASH NORMALIZE PUBLISH VERIFY REUPLOAD REPEAT SIMILARITY CANONICALIZE`

### O3 — Loss blocks silent inheritance

If a material provenance property is lost and no preservation basis or new evidence exists, downstream state cannot be represented as fully continuous with respect to that property.

### O4 — Inference remains inference

A candidate relationship produced by similarity, graph completion, model inference, or human reconstruction must remain `INFERRED` or `UNRESOLVED` until admissible evidence establishes it.

### O5 — Verification is scoped

A verification record can support only claims within the scope of its rule set, inputs, and evidence. Verification cannot silently expand into origin, authorship, truth, or authority.

### O6 — Identity mapping is explicit

Cross-system identifier changes require an identity-mapping assertion. Content equality alone is insufficient.

### O7 — Transitive edges are derived

A→B and B→C may establish graph reachability from A to C, but A→C is not direct evidence without a direct supporting record.

### O8 — Independence is dependency-aware

Repeated or derivative claims sharing a predecessor do not automatically become independent corroboration.

### O9 — Presentation cannot strengthen state

Rendered state must equal or be weaker than machine state unless the presentation itself introduces an evidence-bearing transition.

### O10 — Unknown is not negative

Null, absent, empty, redacted, unavailable, and unknown SHALL NOT be conflated without an explicit semantic rule.

## Decision

The oracle returns:

```text
PASS
```

only when all applicable rules hold.

Otherwise:

```text
FAIL: UNJUSTIFIED_PROVENANCE_STRENGTHENING
```

The oracle is intentionally conservative. When evidence is ambiguous, it should preserve the weaker state.
