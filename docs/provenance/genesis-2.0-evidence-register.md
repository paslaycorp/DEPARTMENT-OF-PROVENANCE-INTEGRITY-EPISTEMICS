# Genesis 2.0 Evidence Register

## Purpose

This register identifies the evidence required to support a rigorous comparison between Genesis 2.0 and AEIF. It is intentionally conservative: a source is not treated as verified merely because a claim is publicly repeated.

## Evidence classes

| Class | Meaning |
|---|---|
| PRIMARY | Original specification, repository artifact, publication, post, or other source attributable to the originating system/author |
| REPOSITORY | Versioned artifact in the AEIF repository, including commits and specifications |
| SECONDARY | Independent reporting, analysis, or commentary used for corroboration/context |
| DERIVED | A claim computed or reasoned from already recorded evidence |
| UNRESOLVED | Material evidence that has not yet been located, authenticated, or reconciled |

## Register

| ID | Evidence item | Required provenance | Current state | Use |
|---|---|---|---|---|
| E-001 | Genesis 2.0 primary public description | URL, publication date, author/account, capture date, immutable copy/hash where permitted | PENDING | Establish Genesis terminology and mechanisms |
| E-002 | Genesis 2.0 original/public specification, if available | Version, publication date, canonical location, hash/capture | PENDING | Establish technical semantics |
| E-003 | Genesis 2.0 repository/artifact history, if public | Repository URL, commit SHA, dates, artifact paths | PENDING | Establish chronology and implementation evidence |
| E-004 | AEIF repository history | Commit SHA, path, date, version | PENDING | Establish AEIF chronology |
| E-005 | AEIF specifications | Artifact identifier, version, date, repository location, hash | PENDING | Establish AEIF semantics |
| E-006 | Independent corroborating sources | Source identity, date, URL, relation to primary evidence | PENDING | Corroborate material claims |
| E-007 | Contradictory evidence | Source identity, date, exact conflict, capture/hash | RETAINED | Prevent one-sided provenance conclusions |

## Capture protocol

For each evidence item, record as much of the following as the source permits:

- canonical URL or repository location;
- author or originating account;
- publication or commit date;
- capture date;
- version or commit SHA;
- artifact filename/path;
- cryptographic hash where an immutable artifact can be hashed;
- relevant claim(s);
- whether the source is primary, secondary, derived, or unresolved;
- known contradictions;
- chain-of-custody or acquisition notes.

## Chronology rule

Chronological priority should be established from dated primary artifacts wherever possible. A later public description cannot by itself establish when an underlying mechanism was first conceived or implemented.

## Provenance rule

Do not fill an unknown provenance field with an inferred value. Use PENDING or UNRESOLVED until evidence supports a stronger state.

## Relationship to the comparison ledger

The evidence register supplies the evidentiary substrate for [`genesis-2.0-comparison-ledger.md`](genesis-2.0-comparison-ledger.md). The ledger should reference evidence items rather than silently importing unsupported assertions.

## Audit note

This register is designed to preserve an auditable distinction between what is known, what is documented, what is derived, and what remains unknown. It does not make an authorship, copying, or priority determination.
