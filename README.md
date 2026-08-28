juju# DEPARTMENT-OF-PROVENANCE-INTEGRITY-EPISTEMICS
Founding Date:  August 27, 2026   STATUS:  Private, independent intellectual and technical initiative.   CORE PURPOSE:  DPIE develops methods and services for establishing provenance, preserving integrity, evaluating evidence, and maintaining epistemic discipline across human and artificial intelligence systems
# Department of Provenance & Epistemic Integrity

## Provenance Record

This directory is the canonical provenance record for the Department of Provenance & Epistemic Integrity (DPIE).

Its purpose is to preserve authorship, chronology, artifact identity, version history, disclosure history, lineage, and supporting evidence without retroactively altering the historical record.

## Core Rule

Every material provenance claim follows:

Claim → Artifact → Version → Date → Evidence → Hash → Location

## Provenance Principles

1. Historical dates SHALL be supported by evidence.
2. Missing evidence SHALL remain explicitly marked as unknown or pending.
3. No artifact SHALL be backdated solely from recollection.
4. Existing records SHALL NOT be silently overwritten.
5. Superseded artifacts SHALL remain preserved.
6. Hashes SHALL be calculated from the actual artifact bytes.
7.
FILE: PROVENANCE/README.md


Department of Provenance & Epistemic Integrity


Canonical Provenance Record


This directory contains the canonical provenance record for the Department of Provenance & Epistemic Integrity (DPIE).


Its purpose is to preserve authorship, chronology, artifact identity, version history, disclosure history, technical lineage, and evidentiary status without relying on retrospective reconstruction alone.


Core Rule


Every material provenance claim should be represented as:


Claim → Artifact → Version → Date → Evidence → Hash → Location


Where evidence is unavailable, the record must say so.


Unknown information is not to be replaced with an assumption.


Provenance Principles




Preserve original artifacts.


Preserve original chronology where evidence exists.


Never fabricate a creation date.


Never fabricate a cryptographic hash.


Distinguish creation from publication.


Distinguish authorship from ownership.


Distinguish technical overlap from copying.


Preserve contradictory evidence.


Record revisions rather than silently replacing prior versions.


Prefer primary records over recollection.


Preserve repository commit history.


Do not alter historical records merely to improve their appearance.




Artifact Families


The current provenance record includes the following known architectural artifacts and families:




Alexandrian Epistemic Integrity Framework (AEIF)


ECR_p


Transition Governor


ECR_i


Decision Lattice


Verification Kernel


PATRICK²


Temporal Attestation Vector (TAV)


Related semantic, provenance, integrity, verification, and decision-boundary artifacts




Status Vocabulary




VERIFIED — supported by sufficient primary evidence


DOCUMENTED — documented in an identifiable record but not independently verified in every respect


PENDING — evidence or artifact bytes are still required


UNRESOLVED — conflicting or insufficient evidence exists


SUPERSEDED — replaced by a later version


RETAINED — preserved despite supersession


WITHHELD — intentionally not publicly disclosed




Important Limitation


The existence of this repository establishes the public record from the point at which each artifact is actually committed or otherwise independently evidenced.


It does not retroactively manufacture dates for earlier work.


Earlier dates must be supported by contemporaneous evidence such as repository commits, dated publications, preserved documents, messages, exports, or other independently inspectable records.


FILE: PROVENANCE/ARTIFACT-LEDGER.json


{
"schema": "DPIE-Provenance-Ledger",
"version": "1.0.0",
"purpose": "Canonical machine-readable register of artifacts, chronology, evidence, hashes, disclosure and lineage.",
"provenance_rule": "Claim -> Artifact -> Version -> Date -> Evidence -> Hash -> Location",
"integrity_policy": {
"unknown_is_not_assumed": true,
"historical_dates_require_evidence": true,
"hashes_require_artifact_bytes": true,
"superseded_artifacts_are_retained": true,
"contradictory_evidence_is_preserved": true
},
"artifacts": [
{
"id": "AEIF-ART-0001",
"name": "ECR_p",
"version": "0.1.1",
"family": "AEIF",
"description": "Provenance-capacity artifact.",
"status": "DOCUMENTED",
"tests": "20/20",
"creation_date": "PENDING_PRIMARY_EVIDENCE",
"first_publication_date": "PENDING_PRIMARY_EVIDENCE",
"author": "Master / Paslay Corp",
"hash_sha256": "PENDING_ARTIFACT_BYTES",
"evidence": [
"Existing project records",
"Repository history when available",
"Preserved development artifacts"
],
"location": "AEIF/ECR-p/",
"lineage": [
"AEIF"
]
},
{
"id": "AEIF-ART-0002",
"name": "Transition Governor",
"version": "0.1",
"family": "AEIF",
"description": "Authority governing admissible state transitions.",
"status": "DOCUMENTED",
"tests": "17/17",
"creation_date": "PENDING_PRIMARY_EVIDENCE",
"first_publication_date": "PENDING_PRIMARY_EVIDENCE",
"author": "Master / Paslay Corp",
"hash_sha256": "PENDING_ARTIFACT_BYTES",
"evidence": [
"Existing project records",
"Repository history when available",
"Preserved development artifacts"
],
"location": "AEIF/TRANSITION-GOVERNOR/",
"lineage": [
"AEIF",
"ECR_p"
]
},
{
"id": "AEIF-ART-0003",
"name": "ECR_i",
"version": "0.1.1",
"family": "AEIF",
"description": "Integrity-capacity artifact.",
"status": "DOCUMENTED",
"tests": "18/18",
"creation_date": "PENDING_PRIMARY_EVIDENCE",
"first_publication_date": "PENDING_PRIMARY_EVIDENCE",
"author": "Master / Paslay Corp",
"hash_sha256": "PENDING_ARTIFACT_BYTES",
"evidence": [
"Existing project records",
"Repository history when available",
"Preserved development artifacts"
],
"location": "AEIF/ECR-i/",
"lineage": [
"AEIF",
"ECR_p",
"Transition Governor"
]
},
{
"id": "AEIF-ART-0004",
"name": "Decision Lattice",
"version": "0.2",
"family": "AEIF",
"description": "Typed decision structure combining provenance, integrity, requirement, authority and consequence.",
"status": "DOCUMENTED",
"creation_date": "PENDING_PRIMARY_EVIDENCE",
"first_publication_date": "PENDING_PRIMARY_EVIDENCE",
"author": "Master / Paslay Corp",
"hash_sha256": "PENDING_ARTIFACT_BYTES",
"evidence": [
"Existing project records",
"Repository history when available",
"Preserved development artifacts"
],
"location": "AEIF/DECISION-LATTICE/",
"lineage": [
"AEIF",
"ECR_p",
"Transition Governor",
"ECR_i"
]
},
{
"id": "AEIF-ART-0005",
"name": "Verification Kernel",
"version": "0.1",
"family": "AEIF",
"description": "Verification boundary and implementation layer operating against an explicit semantic rule set.",
"status": "DOCUMENTED",
"creation_date": "PENDING_PRIMARY_EVIDENCE",
"first_publication_date": "PENDING_PRIMARY_EVIDENCE",
"author": "Master / Paslay Corp",
"hash_sha256": "PENDING_ARTIFACT_BYTES",
"evidence": [
"Existing project records",
"Repository history when available",
"Preserved development artifacts"
],
"location": "AEIF/VERIFICATION-KERNEL/",
"lineage": [
"AEIF",
"ECR_p",
"Transition Governor",
"ECR_i",
"Decision Lattice"
]
},
{
"id": "AEIF-ART-0006",
"name": "PATRICK²",
"version": "0.5",
"family": "Epistemic Semantics",
"description": "Typed epistemic-state characterization semantics.",
"status": "DOCUMENTED",
"creation_date": "2026-08-10",
"first_publication_date": "PENDING_PRIMARY_EVIDENCE",
"author": "Master / Paslay Corp",
"hash_sha256": "55e57a6428ee647070d939014715a62ec3f385f8cde1438323d288f0a066f4fd",
"evidence": [
"Preserved project record",
"Known validated copybox artifact"
],
"location": "PATRICK2/",
"lineage": [
"Epistemic Integrity",
"Provenance",
"Typed State Semantics"
]
},
{
"id": "AEIF-ART-0007",
"name": "Temporal Attestation Vector",
"version": "PENDING",
"family": "Temporal Provenance",
"description": "Multi-domain temporal fingerprint using independent physical time observations.",
"status": "DOCUMENTED",
"creation_date": "PENDING_PRIMARY_EVIDENCE",
"first_publication_date": "PENDING_PRIMARY_EVIDENCE",
"author": "Master / Paslay Corp",
"hash_sha256": "PENDING_ARTIFACT_BYTES",
"evidence": [
"Existing project records"
],
"location": "TAV/",
"lineage": [
"Temporal Attestation",
"Provenance"
]
}
]
}


FILE: PROVENANCE/CHRONOLOGY.md


Chronology


Purpose


This document records the development and disclosure chronology of DPIE artifacts.


Dates are divided into separate categories because creation, internal development, public disclosure, repository publication and later revision are not necessarily the same event.


Chronology Rules


A date must identify what event it represents.


The following are distinct:




Conceptual development


Artifact creation


Internal revision


Private disclosure


Public disclosure


Repository commit


Release


Supersession




A remembered date without supporting evidence is recorded as CLAIMED, not VERIFIED.


Known Chronological Record


2026-08-10


PATRICK² v0.5 is documented in the existing project record as a validated technical artifact.


Recorded characteristics include typed epistemic-state characterization semantics, provenance/evidence relationships, and validation material.


Status:


DOCUMENTED


Additional primary evidence should be attached to establish the complete publication chronology.


2026-08-27


The Department of Provenance & Epistemic Integrity repository was established as the canonical public repository for the provenance record.


This repository date establishes the public GitHub record from this point forward.


It does not by itself establish the creation date of earlier artifacts.


Earlier AEIF Development


The following artifacts are documented as preceding components in the AEIF architecture:




ECR_p v0.1.1


Transition Governor v0.1


ECR_i v0.1.1


Decision Lattice v0.2


Verification Kernel v0.1




Their exact historical creation and publication dates remain:


PENDING_PRIMARY_EVIDENCE


Those dates must be populated from contemporaneous records rather than reconstructed from memory.


Future Entries


Every future material event should be appended rather than silently rewriting an earlier entry.


Recommended format:


DATE:
EVENT:
ARTIFACT:
VERSION:
EVENT TYPE:
EVIDENCE:
REPOSITORY COMMIT:
PUBLICATION LOCATION:
HASH:
NOTES:



FILE: PROVENANCE/ATTRIBUTION.md


Attribution and Authorship Record


Purpose


This document records authorship and attribution of the architectural work maintained by the Department of Provenance & Epistemic Integrity.


Primary Attribution


The DPIE architecture and the artifacts identified in this repository are attributed to:


Master / Paslay Corp


where the corresponding artifact records identify that attribution.


Attribution Standard


Attribution is based on documented development and publication evidence.


This repository does not make unsupported claims concerning another person's intent, conduct, copying, or infringement.


The following statements must remain separate:




A work was independently developed.


A work was publicly documented.


A work resembles another work.


A work incorporates another work.


A work copies another work.


A person owns intellectual property rights in a work.




Evidence supporting one proposition does not automatically establish another.


Public Record


The canonical public record is maintained in this GitHub repository.


Repository commits provide an auditable history of changes made to this repository after its establishment.


Earlier chronology requires earlier evidence.


Preservation Rule


Original artifacts must not be silently replaced.


Where an artifact is revised:




retain the earlier version;


assign the new version explicitly;


record the revision;


preserve hashes where artifact bytes exist;


identify the relationship between versions.




External Work


When comparing DPIE work with external work, the record should identify:




the external artifact;


its author;


its version;


its publication date;


the exact technical feature being compared;


the source supporting the comparison;


the degree of correspondence;


whether the correspondence is generic or structurally specific.




No conclusion about copying should be made solely from conceptual similarity.


FILE: PROVENANCE/EVIDENCE-REGISTER.md


Evidence Register


Purpose


This register identifies evidence supporting provenance, chronology, authorship, artifact identity and technical comparison.


Evidence Classes


E1 — Primary Artifact


The actual source artifact or source files.


Examples:




source code


specifications


manuscripts


formal models


datasets


signed releases




E2 — Repository History


Git commits, tags, releases and repository metadata.


E3 — Public Publication


Public posts, papers, repositories, documentation or other dated disclosures.


E4 — Private Disclosure


Dated private messages, documents or communications.


E5 — Cryptographic Evidence


SHA-256 or other cryptographic hashes tied to identified artifact bytes.


E6 — Independent Corroboration


Evidence from a source independent of the author.


E7 — Recollection


A retrospective statement concerning prior development.


Recollection may be recorded but should not be treated as equivalent to contemporaneous primary evidence.


Current Evidence




Evidence ID
Evidence
Status




EVID-0001
DPIE GitHub repository history
VERIFIED once commit is independently inspected


EVID-0002
Existing AEIF artifact inventory
DOCUMENTED


EVID-0003
ECR_p v0.1.1 validation record
DOCUMENTED


EVID-0004
Transition Governor v0.1 validation record
DOCUMENTED


EVID-0005
ECR_i v0.1.1 validation record
DOCUMENTED


EVID-0006
PATRICK² v0.5 record
DOCUMENTED


EVID-0007
Known SHA-256 for preserved PATRICK² artifact
VERIFIED


EVID-0008
Preserved LinkedIn correspondence concerning Genesis 2.0
PENDING ARCHIVAL CAPTURE


EVID-0009
Carl's stated development chronology
DOCUMENTED AS HIS STATEMENT


EVID-0010
Genesis 2.0 capability material
PENDING PRIMARY COPY




Evidence Handling


Screenshots should preserve:




full visible context;


account identity;


date/time where displayed;


URL where displayed;


surrounding comments where material.




Screenshots should never be treated as substitutes for original artifacts when the original is available.


For important evidence, preserve both:




the human-readable capture;


the original downloadable/exported artifact where available.




Hash Rule


Never record a hash unless it was calculated from the actual artifact bytes.


A missing hash is preferable to an invented hash.


FILE: PROVENANCE/DISCLOSURE-CLASSES.md


Disclosure Classes


Purpose


This document distinguishes how an artifact or claim became available.


Classes


D0 — Undisclosed


Known to exist but not disclosed outside the originating working environment.


D1 — Private


Shared with one or more specifically identified individuals or organizations.


D2 — Limited


Shared with a defined group, private repository, private document or controlled audience.


D3 — Public


Made publicly accessible through a publication, post, public repository or equivalent disclosure.


D4 — Canonical Public Record


Preserved in the DPIE canonical repository with identifiable version history.


Important Distinction


Disclosure class does not itself establish invention date.


For example:


A work may have existed privately before public disclosure.


The record therefore tracks:


development date ≠ private disclosure date ≠ public disclosure date ≠ repository date


unless evidence establishes that those events occurred together.


Current Repository


Material committed to this repository receives a D4 status from the applicable repository commit onward.


Earlier artifacts retain their historical disclosure status where evidence exists.


FILE: PROVENANCE/RELEASE-MANIFEST.md


Release Manifest


Department of Provenance & Epistemic Integrity


This manifest records canonical releases of the provenance record.


Release 0.1.0


Purpose


Initial establishment of the DPIE provenance framework.


Included Records




Provenance README


Artifact Ledger


Chronology


Attribution


Evidence Register


Disclosure Classes


Release Manifest




Integrity Conditions


The initial release establishes the recording framework.


It does not retroactively establish historical dates for artifacts whose contemporaneous evidence has not yet been attached.


Required Future Release Information


Each subsequent release should record:


RELEASE:
DATE:
COMMIT:
ARTIFACTS ADDED:
ARTIFACTS MODIFIED:
ARTIFACTS SUPERSEDED:
NEW EVIDENCE:
NEW HASHES:
CHRONOLOGY CHANGES:
DISCLOSURE CHANGES:
COMPARISON RECORDS:
NOTES:



Release Integrity Rule


A release must be reproducible from the repository state associated with its commit or tag.


No release should depend on an undocumented external modification.


Future Genesis Comparison


The Genesis 2.0 comparison should be maintained separately from the core attribution record.


The comparison must not state that copying occurred unless evidence establishes that conclusion.


It should instead document:


DPIE mechanism → Genesis mechanism → earliest documented occurrence → correspondence → evidence → conclusion


This preserves the distinction between technical convergence, independent development, prior art, attribution and copying.

