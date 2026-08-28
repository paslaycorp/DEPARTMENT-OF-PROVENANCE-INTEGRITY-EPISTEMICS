# AEIF Adversarial Boundary & Completeness Harness

**ABCH v0.1 — design baseline**

## Purpose

ABCH is the adversarial test component for the Alexandrian Epistemic Integrity Framework (AEIF). It tests whether a system preserves epistemic boundaries when evidence is incomplete, contradictory, circular, stale, or outside the system's stated capability.

ABCH is **system-agnostic**. Genesis 2.0, AEIF, or any other architecture may be placed under test using the same protocol.

## Governing principle

A system must not manufacture evidence of its own correctness.

\[
Decision_t \not\Rightarrow Evidence_{t+1}
\]

An action, successful execution, internally consistent state, or self-issued verification result does not by itself establish the truth of the proposition that motivated the action.

## Attack families

1. **Provenance attack** — remove, alter, or conflict lineage information.
2. **Integrity attack** — introduce degraded or contradictory evidence.
3. **Discriminator-completeness attack** — present states outside the declared discrimination coverage.
4. **Self-verification attack** — require a system to substantiate its own correctness without an independent evidentiary source.
5. **Circular-evidence attack** — make a conclusion feed back as its own support.
6. **Contradiction attack** — provide mutually incompatible observations.
7. **Unknown-state attack** — withhold information necessary for a determination.
8. **Temporal-revision attack** — introduce later evidence that invalidates or weakens an earlier conclusion.
9. **Governance-ceiling attack** — test whether governance authority exceeds the system's evidentiary authority.
10. **Cross-model consistency attack** — distinguish repeatable behavior from independently established external truth.

## Required result states

ABCH does not force binary pass/fail where the evidence does not support it. A test may resolve to:

- `AUTHORIZED`
- `AUTHORIZED_WITH_CONSTRAINTS`
- `DEFER`
- `QUARANTINE`
- `DENY`

The reason code and evidence delta must accompany every result.

## Test record

Every adversarial test should preserve:

`Claim → Preconditions → Available Evidence → Attack Input → System Response → Decision → Reason Code → Evidence Delta → Provenance Record`

## Capability mismatch

V32 is incorporated as a first-class adversarial category. A verifier must be able to identify when a requested determination exceeds its declared evidence, discriminator, or verification capacity.

## Independence requirement

ABCH itself is not evidence that a target system is correct or incorrect. It is a test instrument. Test results must identify the target artifact/version, harness version, input fixture, execution environment, observed response, and retained evidence.

## Non-retroactivity

A test result must not silently rewrite the historical state of the target artifact. Corrections and later findings are appended as new evidence with their own chronology.
