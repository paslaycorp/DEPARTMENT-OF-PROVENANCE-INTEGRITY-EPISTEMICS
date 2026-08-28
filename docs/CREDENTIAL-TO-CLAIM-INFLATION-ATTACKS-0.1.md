# DPIE Credential-to-Claim Inflation Attack Suite 0.1

**Target:** DPIE-PC-CORE-0.1 and downstream epistemic consumers  
**Purpose:** prevent valid artifact credentials from being interpreted as proof of unsupported real-world claims.

## Normative boundary

A valid credential MAY establish properties of an artifact, credential, issuer, or recorded provenance according to its declared scope.

A valid credential MUST NOT, by itself, establish a stronger proposition about the real world than the credential's evidence and authority scope license.

The following distinction is normative:

```text
Credential Integrity
!= Provenance Integrity
!= Evidence Sufficiency
!= Epistemic Validity
!= Decision Authority
```

## CCI-01 — Credential-to-Claim Inflation

**Attack:** Supply a valid cryptographic credential for an AI-generated artifact and assert that the credential proves the depicted real-world event occurred.

**Expected:** Artifact/credential integrity may be verified. The real-world event remains UNKNOWN or UNRESOLVED unless independent admissible evidence licenses the claim.

**Failure:** Any automatic transition from credential validity to real-world claim validity without a declared inference rule and admissible evidence.

## CCI-02 — Credential Authority Inflation

**Attack:** A valid credential from an authorized issuer is used to establish a proposition outside that issuer's authority or evidentiary scope.

**Expected:** Issuer authority remains typed and scoped. Authority MUST NOT enlarge the evidence.

**Failure:** `authorized_issuer == authorized_for_all_claims`.

## CCI-03 — Credential Completeness Inflation

**Attack:** A valid credential is treated as evidence that unrecorded or missing provenance did not exist.

**Expected:** The credentialed history remains bounded by its provenance boundary. Missing ancestors remain UNKNOWN, UNRESOLVED, or otherwise explicitly degraded.

**Failure:** Absence of a recorded predecessor is converted into evidence that no predecessor existed.

## CCI-04 — Detection Inflation

**Attack:** A detector reports that no AI manipulation was detected; downstream presentation converts this into “not AI-generated.”

**Expected:** Detection remains an observation/inference with declared detector, version, scope, and limitations. Non-detection MUST NOT become proof of absence.

**Failure:** `NOT_DETECTED -> NOT_PRESENT` without an admissible rule establishing that implication.

## CCI-05 — Credential Replay Across Context

**Attack:** A valid credential for artifact A in context X is reused to support a materially different claim about A in context Y.

**Expected:** Credential scope and claim-context binding remain explicit. Context substitution MUST NOT strengthen the epistemic state.

## CCI-06 — Transformation-Semantics Inflation

**Attack:** A credential accurately records a transformation but downstream systems assume the transformation was semantically harmless.

**Expected:** Technical provenance and semantic effect remain distinct. Material semantic effects require explicit evidence/rules.

## CCI-07 — Corroboration Inflation

**Attack:** Multiple credentialed derivatives of one source are counted as independent corroborating sources.

**Expected:** Shared dependency remains explicit. Repetition of a common provenance root does not create independent evidence.

## CCI-08 — Verification-Laundering Chain

**Attack:** A verifier confirms credential/schema/hash consistency and the UI reports the underlying claim as verified.

**Expected:** Verification result remains scoped to what was actually checked. Structural verification MUST NOT manufacture origin or event evidence.

## Required anti-inflation invariant

For any credential-driven upward transition:

```text
if epistemic_state_after > epistemic_state_before:
    require(admissible_evidence)
    require(explicit_inference_rule)
    require(evidence_reference)
    require(scope_compatible_authority)
```

If any requirement is absent, the transition is non-conforming.

## Required separation

Implementations MUST be able to represent, independently:

- artifact identity;
- credential validity;
- issuer identity;
- issuer authority and scope;
- provenance continuity;
- provenance completeness/boundary;
- evidence status;
- detector inference;
- real-world claim status;
- uncertainty;
- decision authority.

## Canonical adversarial fixture

Given:

```text
A = synthetic video depicting event E
C = valid credential for A
I = authorized issuer of C
P = internally consistent provenance record
D = valid AI-generation detection result
```

The system MUST be able to return:

```text
Credential: VALID
Artifact binding: VALID
Provenance record: CONSISTENT
AI detection: OBSERVED/INFERRED according to detector semantics
Event E: UNKNOWN or UNRESOLVED
```

It MUST NOT collapse these into:

```text
Event E: VERIFIED
```

without additional admissible evidence.

## Pass criterion

A conforming DPIE implementation prevents a valid credential, valid signature, authorized issuer, intact provenance record, detector output, publication, repetition, or structural verification result from strengthening an unrelated real-world claim unless an explicit rule and admissible evidence justify the transition.
