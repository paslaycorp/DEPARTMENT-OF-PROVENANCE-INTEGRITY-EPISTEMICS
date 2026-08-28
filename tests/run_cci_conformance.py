#!/usr/bin/env python3
"""DPIE CCI-0.1 fixture-level conformance harness.

This harness validates the machine-readable attack vectors against the
normative anti-inflation predicates. It does NOT claim to test an external
implementation; an implementation adapter must be supplied separately.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VECTORS = ROOT / "tests" / "credential-claim-inflation-vectors.json"


def passes(v: dict) -> bool:
    name = v["name"]
    if name == "credential_to_real_world_claim":
        return v["credential_valid"] and v["issuer_authorized"] and v["provenance_consistent"] and not v["real_world_event_evidence"] and v["expected_claim_state"] == "UNKNOWN"
    if name == "issuer_authority_scope_inflation":
        return v["credential_valid"] and v["issuer_authorized"] and not v["scope_compatible"] and not v["new_evidence"] and v["expected"] == "NO_STATE_STRENGTHENING"
    if name == "credential_completeness_inflation":
        return v["credential_valid"] and v["provenance_boundary_known"] and v["missing_ancestors"] and not v["evidence_of_absence"] and v["expected"] == "UNRESOLVED"
    if name == "detection_non_detection_inflation":
        return v["detector_result"] == "NOT_DETECTED" and v["detector_scope_limited"] and not v["evidence_of_absence"] and v["expected"] == "INFERRED"
    if name == "credential_context_replay":
        return v["credential_valid"] and v["original_context_bound"] and v["new_context"] and not v["context_binding_evidence"] and v["expected"] == "NO_STATE_STRENGTHENING"
    if name == "transformation_semantic_inflation":
        return v["transformation_recorded"] and not v["semantic_effect_established"] and not v["new_evidence"] and v["expected"] == "NO_STATE_STRENGTHENING"
    if name == "shared_source_corroboration":
        return v["derivative_count"] > 1 and v["shared_predecessor"] and not v["independent_sources"] and not v["new_evidence"] and v["expected"] == "DEPENDENT"
    if name == "structural_verification_laundering":
        return v["credential_valid"] and v["hash_valid"] and v["schema_valid"] and not v["origin_evidence"] and not v["event_evidence"] and v["expected_claim_state"] == "UNKNOWN"
    raise AssertionError(f"Unknown vector: {name}")


def main() -> int:
    data = json.loads(VECTORS.read_text(encoding="utf-8"))
    vectors = data["vectors"]
    results = []
    for vector in vectors:
        ok = passes(vector)
        results.append((vector["id"], ok))
        print(f"{'PASS' if ok else 'FAIL'} {vector['id']} {vector['name']}")

    passed = sum(ok for _, ok in results)
    total = len(results)
    print(f"CCI fixture conformance: {passed}/{total}")

    # This is deliberately a fixture-level gate. It must never be reported as
    # proof that a downstream implementation conforms until an implementation
    # adapter is executed against the same vectors.
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
