# DPIE Documentation Index

This directory contains the public documentation layer for the Department of Provenance & Epistemic Integrity (DPIE).

## Provenance architecture

The repository's canonical provenance relation is:

**Claim → Artifact → Version → Date → Evidence → Hash → Location**

Documentation in this directory must not create a competing provenance model. Comparative work, evidence registers, and chronology records are subordinate to the canonical record already established by the repository.

## Genesis 2.0 comparison

### Comparative analysis

[`comparative-analysis/genesis-2.0-vs-aeif.md`](comparative-analysis/genesis-2.0-vs-aeif.md)

Provenance-first comparison of publicly described Genesis 2.0 material with AEIF. The analysis separates similarity, correspondence, evidence, chronology, and provenance and explicitly rejects similarity-to-copying inference.

### Comparison ledger

[`provenance/genesis-2.0-comparison-ledger.md`](provenance/genesis-2.0-comparison-ledger.md)

Machine-readable-in-spirit human ledger of comparative propositions tied to evidence IDs and the canonical provenance relation.

### Evidence register

[`provenance/genesis-2.0-evidence-register.md`](provenance/genesis-2.0-evidence-register.md)

Register of Genesis and AEIF evidence, provenance requirements, capture state, limitations, and source-handling rules.

## Evidence-state rule

Public statements, model outputs, technical artifacts, independent corroboration, and derived interpretations are distinct evidence classes. A statement that a model verified something is not automatically independent verification of the underlying proposition.

## Chronology rule

Creation, internal development, private disclosure, public disclosure, repository publication, release, revision, and supersession are distinct events. A retrospective date remains an author claim unless contemporaneous evidence supports it.

## Integrity rule

Do not:

- fabricate dates;
- fabricate hashes;
- silently overwrite historical records;
- convert technical overlap into a copying claim;
- promote PENDING or UNRESOLVED evidence by inference;
- treat model self-report as independent instrumentation.

Do:

- preserve contradictory evidence;
- preserve superseded records;
- identify exact artifacts and versions;
- capture canonical source locations;
- calculate hashes only from actual artifact bytes;
- preserve repository commit history.

## Current status

The Genesis 2.0 comparison is **DOCUMENTED / PARTIALLY UNRESOLVED**. Meaningful technical correspondences have been recorded, but the underlying Genesis technical artifacts, exact versions, immutable captures, and complete chronology remain to be acquired before any stronger provenance conclusion can be made.
