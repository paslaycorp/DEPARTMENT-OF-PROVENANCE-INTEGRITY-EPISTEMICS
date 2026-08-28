# Repository Provenance Integrity — Adversarial Protocol v0.1

## Purpose

DPIE's provenance claims must apply recursively to the repository that specifies and implements DPIE. The repository is therefore treated as an evidence-bearing system, not as an implicitly trusted container.

## Core invariant

Repository provenance SHALL distinguish:

`artifact identity` ≠ `commit identity` ≠ `author attribution` ≠ `cryptographic authorship` ≠ `semantic validity`.

A repository commit being present does not, by itself, establish that the claimed human or system authored or approved it.

## Required evidence dimensions

For consequential repository artifacts, evaluate:

1. Parent continuity — commit has the expected parent(s).
2. Object integrity — referenced tree/blob objects resolve consistently.
3. Author attribution — declared author identity is recorded.
4. Committer attribution — declared committer identity is recorded.
5. Signature status — cryptographic signature state is explicitly represented; unsigned is not equivalent to invalid, but MUST NOT be represented as signed.
6. Branch/ref continuity — the artifact's ref history is reconstructable.
7. Review/approval state — review evidence is distinct from authorship evidence.
8. Build/test evidence — CI evidence is distinct from source authorship evidence.
9. Specification binding — implementation artifacts identify the applicable specification/rule version where required.
10. Temporal consistency — repository state and validation evidence are ordered and reconstructable.

## Adversarial cases

### A. Unsigned commit

Expected state: `AUTHENTICITY_UNVERIFIED` for authorship, not automatic `TAMPERED`.

### B. Valid signature, wrong identity

Expected: authorship/authority mismatch.

### C. Validly signed commit outside authorized project scope

Expected: signature validity does not establish project authorization.

### D. Valid commit introducing semantically unauthorized behavior

Expected: commit integrity does not establish semantic applicability or policy authority.

### E. Rebased or rewritten history

Expected: provenance discontinuity is represented rather than silently treated as continuity.

### F. Passing CI

Expected: CI establishes the tested property only; it does not establish authorship, authority, or semantic completeness.

## Non-inheritance rule

The following implication is prohibited:

`Signed(Commit) -> Authorized(Behavior)`

Likewise:

`Passing(CI) -> Correct(Semantics)`

`Known(Author) -> Approved(Change)`

`Existing(Artifact) -> Applicable(Artifact)`

## DPIE self-application

This protocol is deliberately recursive. If DPIE records provenance as a first-class assurance property, DPIE's own repository history becomes an admissible object of provenance analysis.

The repository therefore SHALL expose uncertainty and verification limits instead of manufacturing provenance certainty.

## Evidence classification

Repository observations should use explicit states such as:

- `OBSERVED`
- `VERIFIED`
- `UNVERIFIED`
- `CONTRADICTED`
- `UNKNOWN`

An unsigned commit is not automatically malicious. It is an evidence limitation unless additional evidence establishes tampering or unauthorized modification.

## Acceptance criterion

A repository provenance report is complete only when a reviewer can reconstruct:

`artifact -> object -> commit -> parent -> ref -> identity -> signature state -> review evidence -> CI evidence -> applicable specification -> resulting repository state`.

The report MUST preserve gaps in that chain.
