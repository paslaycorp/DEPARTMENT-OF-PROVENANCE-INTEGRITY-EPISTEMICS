# DPIE-PC Hardening Entry Point

This branch is the adversarial hardening track for DPIE-PC-0.1.

## Read in this order

1. `PROVENANCE-CONTINUITY.md` — base continuity specification.
2. `PROVENANCE-CONTINUITY-ADVERSARIAL-REVIEW.md` — findings and hardening decisions.
3. `PROVENANCE-CONTINUITY-CORE-0.1.md` — reduced formal core.
4. `PROVENANCE-CONTINUITY-STATE-MACHINE-0.1.md` — conservative state transitions.
5. `PROVENANCE-CONTINUITY-ATTACK-ORACLE-0.1.md` — anti-laundering oracle.
6. `CONFORMANCE-ATTACKS-0.1.md` — 30 implementation attacks.
7. `tests/pc-core-attack-vectors.json` — machine-readable attack vectors.
8. `CREDENTIAL-TO-CLAIM-INFLATION-ATTACKS-0.1.md` — credential/attestation boundary attacks.
9. `tests/credential-claim-inflation-vectors.json` — machine-readable credential inflation vectors.

## Current gate

Do not add another normative layer until the implementation can demonstrate:

> **No provenance or epistemic state becomes stronger without new admissible evidence.**

Credential validity, issuer authority, structural verification, detection, publication, repetition, and artifact binding are evidence-bearing conditions with bounded scope. They MUST NOT silently inflate an unrelated real-world claim.

The hardening track therefore prioritizes executable conformance over additional conceptual breadth.
