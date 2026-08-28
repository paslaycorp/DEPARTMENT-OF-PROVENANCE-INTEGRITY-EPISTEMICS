DPIE Scope Specification


Department of Provenance & Epistemic Integrity


Specification: DPIE-SCOPE-0.1

Status: Foundational

Established: 2026-08-27



1. Purpose


The Department of Provenance & Epistemic Integrity (DPIE) defines methods, specifications, models, implementations, and records for establishing, preserving, evaluating, and communicating the provenance, integrity, and epistemic status of information used by human and artificial intelligence systems.


DPIE is concerned with maintaining a defensible relationship between a claim and the evidence upon which that claim depends.


2. Scope


DPIE covers:




provenance;


evidence identity;


artifact identity;


chronology;


lineage;


custody and transformation;


integrity assessment;


epistemic-state characterization;


uncertainty;


corroboration and independence;


verification;


decision admissibility;


authority boundaries;


temporal attestation;


auditability;


human-AI information integrity.




3. Fundamental Boundary


DPIE distinguishes the world from representations of the world.


Observations, measurements, records, documents, communications, sensor outputs, and other source material originate outside the verification system.


DPIE may characterize such material.


DPIE SHALL NOT treat its own characterization as equivalent to the original observation.


4. Provenance Boundary


A material provenance claim SHOULD be traceable through:


Claim → Evidence → Artifact → Version → Time → Hash → Location


Where a required element is unavailable, the absence SHALL remain explicitly represented as unknown, pending, or unresolved.


Unknown information SHALL NOT silently become an assumption.


5. Evidence Boundary


Evidence is not synonymous with assertion.


A statement that a fact exists is not, by itself, evidence establishing that fact.


Evidence SHALL be identifiable independently from the conclusion drawn from that evidence whenever practical.


A system SHALL preserve the distinction between:




source evidence;


derived evidence;


interpreted evidence;


corroborating evidence;


contradictory evidence;


unavailable evidence.




6. Integrity Boundary


Integrity concerns the condition and continuity of an information object or evidence chain.


Integrity assessment may include:




cryptographic identity;


structural consistency;


completeness;


modification;


contradiction;


continuity;


custody;


transformation history.




Integrity SHALL remain distinct from truth.


An artifact may be intact while containing a false proposition.


An artifact may be modified while the underlying proposition remains true.


7. Authenticity Boundary


Authenticity concerns whether an artifact is what it purports to be.


Authenticity SHALL NOT automatically imply:




factual correctness;


truth of its contents;


legitimacy of its claims;


authority of its author.




Authenticity, integrity, provenance, and truth are separate properties.


8. Epistemic Boundary


DPIE distinguishes, at minimum:


OBSERVED → EVIDENCED → DERIVED → INFERRED → PREDICTED → SIMULATED / COUNTERFACTUAL


These states SHALL NOT be treated as interchangeable.


A transition between epistemic states requires an identifiable basis.


An inference SHALL NOT be represented as an observation merely because confidence in the inference is high.


A prediction SHALL NOT be represented as an established historical fact merely because it later appears correct.


9. Independence Boundary


Multiple records do not necessarily constitute independent corroboration.


Where evidence shares a common source, transformation, dependency, or derivation path, that relationship SHOULD be represented.


A system SHALL NOT count derived copies of the same underlying evidence as independent confirmation merely because they exist as separate artifacts.


10. Transformation Boundary


When evidence is transformed, the transformation SHOULD be represented as part of provenance.


Examples include:




transcription;


OCR;


parsing;


normalization;


extraction;


summarization;


translation;


model inference;


human interpretation;


format conversion.




Where practical, both input and output artifacts SHOULD remain identifiable.


11. Verification Boundary


Verification SHALL operate against an identified specification, semantic rule set, or other explicit authority.


The Verification Kernel SHALL NOT silently become an alternate specification.


A verification result SHALL identify, where applicable:




subject evaluated;


inputs;


evidence;


applicable rule;


specification version;


authority;


result;


limitations.




Verification characterizes a subject against rules.


Verification does not manufacture evidence.


12. Evidence Non-Manufacture Principle


DPIE SHALL NOT manufacture evidence of its own correctness.


A decision is not automatically evidence supporting the correctness of that decision.


Formally:


Decisionₜ ↛ Evidenceₜ₊₁


Evidence concerning system correctness must arise from an appropriately independent observation, test, audit, measurement, or external record.


13. Authority Boundary


No implementation acquires normative authority merely by asserting authority.


Normative authority SHALL originate from an explicitly identified specification, governance mechanism, or authorized decision structure.


Implementation is subordinate to specification.


Verification is subordinate to the applicable rule set.


14. Historical Record Boundary


Historical records SHALL be preserved rather than silently rewritten.


Where a record is corrected, the correction SHOULD identify:




prior state;


new state;


reason for change;


supporting evidence;


applicable time;


responsible authority.




A repository's creation date does not retroactively establish the creation date of earlier work.


Historical claims require historical evidence.


15. Attribution Boundary


DPIE may preserve and characterize:




authorship;


chronology;


publication;


technical lineage;


artifact identity;


technical correspondence.




Technical similarity alone SHALL NOT be represented as proof of:




copying;


infringement;


intent;


ownership;


legal liability.




Those conclusions require evidence appropriate to the proposition being asserted.


16. Implementation Boundary


Specifications, implementations, tests, evidence, and claims are distinct artifact classes.


Conformance of an implementation to a specification does not establish the universal truth of that specification.


Passing tests establishes tested behavior under tested conditions.


It does not establish untested behavior.


17. Coverage Principle


Material claims SHOULD identify, where applicable:




claim identifier;


subject;


source;


evidence;


artifact;


version;


time;


transformation;


provenance;


integrity status;


epistemic status;


authority;


uncertainty;


applicable rule;


verification result;


limitations.




18. Non-Goals


DPIE does not, solely through its existence or implementation:




establish universal truth;


guarantee factual correctness;


replace domain expertise;


replace scientific methodology;


replace legal judgment;


establish ownership of third-party intellectual property;


certify every implementation claiming compatibility;


convert probabilistic conclusions into certainty.




19. Normative Language


The terms MUST, MUST NOT, SHALL, SHALL NOT, SHOULD, SHOULD NOT, and MAY are normative when used within DPIE specifications.


Their meaning is determined by the applicable specification and version.


20. License Separation


The repository's LICENSE file governs rights granted to users of the licensed material.


This specification defines the intended technical, provenance, and epistemic scope of DPIE.


The MIT License SHALL NOT be interpreted as establishing:




authorship;


historical priority;


patent rights;


trademark rights;


factual truth;


epistemic authority;




beyond the rights expressly granted by that license.


21. Core Principle




A system may characterize what can legitimately be claimed from evidence. It cannot manufacture the evidence required to justify that claim.



