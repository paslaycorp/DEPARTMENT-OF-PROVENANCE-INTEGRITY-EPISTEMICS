# DPIE Fast-Track Platform Specification v0.1

## Purpose

Reassemble DPIE as a commercially testable multi-sector evidence, provenance, integrity, and decision platform without weakening the existing epistemic core.

## Non-Negotiable Core

The fast-track layer SHALL NOT redefine or bypass:

- AEIF epistemic semantics
- ECR_p provenance capacity
- ECR_i integrity capacity
- Transition Governor admissibility
- Verification Kernel operations and identity/version binding
- Decision Lattice semantics
- explicit uncertainty and UNKNOWN states
- immutable/auditable decision history

## Product Boundary

```text
Business Input
    -> Sector Adapter
    -> Canonical Evidence Envelope
    -> Provenance / Identity
    -> Epistemic Characterization
    -> Verification Kernel
    -> Transition Governor
    -> Decision + Uncertainty + Evidence Trail
    -> Sector Output Adapter
```

Adapters translate domain representations. They MUST NOT alter epistemic semantics, verification authority, rule identity, or transition admissibility.

## Adapter Contract

Every adapter MUST define:

1. adapter_id
2. sector
3. adapter_version
4. input_schema_version
5. canonicalization rules
6. provenance requirements
7. validation rules
8. output mapping
9. failure behavior
10. declared external dependencies

Adapter execution MUST be deterministic with respect to the declared input, rule-set identity, adapter version, and available external evidence.

## Security Baseline

The public demo/pilot boundary SHALL include:

- authenticated API access
- tenant isolation
- strict schema validation
- request size/type limits
- content hashing for evidence artifacts
- replay-resistant request identifiers
- rate limiting
- secrets outside source control
- structured security/audit logging with sensitive-data redaction
- fail-closed authorization and integrity failures
- immutable result/audit identifiers

Adapters MUST execute within a trust boundary that prevents them from acquiring kernel authority.

## Demo Surface

The initial demo SHALL support one complete workflow:

`sample business evidence -> adapter -> DPIE -> decision -> explainable result -> audit/evidence view`

The demo should expose outcomes rather than requiring customers to understand the internal epistemic machinery.

Minimum result fields:

- decision/verdict
- confidence or bounded confidence representation
- provenance state
- integrity state
- evidence count
- unresolved uncertainty
- reason codes
- rule-set identity/version
- adapter identity/version
- verification/audit identifier

## First Vertical

Insurance remains the first production-shaped adapter because FAP-Core/FAP-Insurance already provides a concrete verification workload and a realistic evidence model. This is an implementation accelerator, not a restriction on DPIE's multi-sector scope.

## Expansion Strategy

After the insurance adapter proves the contract, add a second sector specifically to test generality. The second adapter should be chosen for architectural discrimination, not novelty for its own sake.

A sector is a good second adapter when it introduces materially different evidence types, authority rules, or uncertainty patterns while still producing a commercially understandable output.

## Commercial Path

1. Public/synthetic demo
2. Developer sandbox
3. Single-workflow pilot
4. Usage-based API/service
5. Enterprise adapters and audit/reporting

Primary value proposition: defensible verification and decision infrastructure, not generic AI analysis.

## Acceptance Gate

DPIE Fast Track is ready for external trials only when:

- an external adapter can be implemented without modifying the epistemic core;
- malformed and unauthorized inputs fail safely;
- tenant boundaries are testable;
- every decision identifies the applicable adapter/rule/kernel versions;
- unresolved uncertainty is preserved rather than silently collapsed;
- an external user can understand the result without knowing AEIF internals;
- the same evidence and versions reproduce the same decision record.
