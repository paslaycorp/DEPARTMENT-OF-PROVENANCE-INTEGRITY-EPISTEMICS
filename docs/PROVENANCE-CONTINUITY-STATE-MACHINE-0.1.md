# DPIE Provenance Continuity State Machine

**Version:** 0.1  
**Purpose:** formalize conservative provenance status transitions

## State set

```text
C = CONTINUOUS
D = DEGRADED
B = BROKEN
U = UNRESOLVED
X = CONFLICTED
I = INFERRED
```

## Principle

The state machine is conservative. An implementation may move to a weaker or more qualified state when evidence is lost or contradicted. It may move to a stronger state only when admissible evidence justifies the transition.

## Allowed evidence-bearing transitions

```text
U --evidence--> C
I --evidence--> C
D --evidence--> C
X --resolution evidence--> C
B --new provenance evidence--> C
```

The target state may instead remain qualified if the new evidence is insufficient.

## Mandatory degradation transitions

```text
C --material loss--> D
C --known missing edge--> B
C --material conflict--> X
C --candidate-only reconstruction--> I
C --insufficient evidence--> U
```

## Forbidden strengthening

The following operations cannot independently cause a stronger provenance state:

```text
COPY
HASH
SIMILARITY
NORMALIZE
PUBLISH
VERIFY
REUPLOAD
REPEAT
CANONICALIZE
MODEL_CONFIDENCE
AUTHORITY_ASSERTION
```

They can record events and may provide evidence in a larger evidentiary context, but the operation itself is not the missing historical evidence.

## Transition audit

Every upward transition SHALL record:

```text
previous_state
new_state
evidence_ids
rule_set
transition_event
actor_or_process
time_status
limitations
```

If `evidence_ids` is empty, an upward transition is non-conforming unless a formally defined state normalization rule applies that does not add a historical claim.

## No total trust ordering

The six states SHALL NOT be treated as a simple total trust ranking. In particular:

- `CONFLICTED` is not simply "less trustworthy" than `BROKEN`;
- `INFERRED` is not simply "better" than `UNRESOLVED`;
- `DEGRADED` can preserve more lineage than `BROKEN` while carrying material qualification.

The state describes the condition of continuity, not a universal scalar confidence score.

## Core anti-laundering rule

> **No provenance state may become stronger merely because the system processed the same provenance claim.**

New evidence, not processing repetition, is the causal requirement for strengthening.
