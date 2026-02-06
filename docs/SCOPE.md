# Phase 1 MVP Scope — Jordan’s Principle Document Validator

## Purpose
This document defines the explicit scope and non-goals of the Phase-1 MVP to prevent scope creep and ensure ethical,
defensible system behavior.

The Phase-1 system is a **pre-submission document validation tool** designed to identify common, non-substantive
documentation issues that may cause administrative delays.

---

## In Scope (Phase 1 MVP)

The system will:

- Accept completed application forms and supporting documents (PDFs and images)
- Extract text using OCR when necessary
- Classify documents into common roles (e.g., support letter, assessment, invoice, consent)
- Detect the **presence** (not correctness) of essential information signals:
    - child reference
    - service reference
    - provider / author reference
    - date presence
    - cost presence (where applicable)
- Perform cross-document validation to identify:
    - missing document roles
    - inconsistent overlapping information
    - unclear linkage between justification documents and the requested service
- Generate a human-readable validation report with:
    - errors (likely to block processing)
    - warnings (may cause delays)
- Provide explainable, plain-language rationales for all findings

---

## Out of Scope (Explicit Non-Goals)

The system will **not**:

- Determine eligibility for Jordan’s Principle
- Approve or deny requests
- Interpret or enforce policy decisions
- Recommend specific services or documents to submit
- Predict application outcomes
- Replace or override human judgment
- Store personal documents beyond transient processing
- Integrate with government systems
- Use automated decision-making or black-box ML models

---

## Scope Control

Any feature not explicitly listed under “In Scope” is considered out of scope for Phase 1.
Future capabilities may be explored in later phases but are intentionally excluded from the MVP.
