# Ethics & Human-in-the-Loop Commitments

## System Role

This system is designed as an **assistive, pre-submission validation tool**.
It does not make decisions, determinations, or recommendations regarding eligibility, approval, or denial of Jordan’s Principle requests.

All outputs are advisory and intended to support human review.

---

## Human-in-the-Loop Commitment

- The system does not replace caseworkers or administrators
- No automated decisions are made
- All findings are framed as potential issues, not judgments
- Humans remain the final decision-makers at all times

---

## Non-Decisional Design

The system explicitly avoids:
- eligibility scoring
- approval prediction
- prioritization of requests
- policy interpretation

Validation logic is limited to detecting **missing, inconsistent, or unclear information** that commonly causes processing delays.

---

## Privacy & Data Handling Assumptions (MVP)

For the Phase-1 MVP:

- Uploaded documents are processed transiently
- No documents or extracted text are stored after analysis
- No personal data is persisted
- No training is performed on uploaded content

Synthetic or anonymized documents are used for testing and demonstration.

---

## Independence & Non-Affiliation

This project is an independent research and engineering effort.
It is **not affiliated with, endorsed by, or representative of** Indigenous Services Canada or the Government of Canada.

---

## Ethical Design Principle

The system prioritizes:
- transparency
- explainability
- predictability of behavior
- harm minimization

Where uncertainty exists, the system errs on the side of **flagging issues conservatively** and deferring judgment to humans.
