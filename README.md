# Jordan’s Principle Document Validator

A user facing, **NLP-assisted, rule-based system** for *pre-submission validation* of completed Jordan’s Principle application documents.

This project focuses on identifying **missing, inconsistent, or unclear information** that commonly causes administrative delays **without making eligibility or approval decisions**.


## Overview

Services responsible for processing Jordan’s Principle requests continue to face persistent backlogs, even following the Canadian Human Rights Tribunal (CHRT) orders intended to ensure timely access to services. Jordan’s Principle applications typically require multiple supporting documents such as application forms, professional assessments, invoices, consent forms, and letters of support. When submissions are incomplete, inconsistent, or unclear, requests are often returned for clarification, resulting in avoidable back-and-forth and compounding processing delays.

This tool is designed to assist applicants and service providers by identifying missing or inconsistent information at submission time, reducing administrative friction and supporting faster, more accurate request processing.

This project explores a **validation-first approach**:

- Accept completed application packages
- Analyze documents for *presence-based signals*
- Surface potential issues in a **human-readable validation report**
- Keep humans fully in the loop


## What This System Does (Phase 1 MVP)

- Accepts uploaded documents via an API  
- Extracts text from digital PDFs  
- Preserves page-level structure  
- Detects presence-based signals (e.g., service mentioned, dates present)  
- Flags potential issues as **errors** or **warnings**  
- Produces explainable, human-readable findings  


## What This System Does *Not* Do

- Determine eligibility  
- Approve or deny requests  
- Interpret or enforce policy  
- Score or rank applications  
- Predict outcomes  
- Store personal documents beyond transient processing  

These exclusions are **intentional** and enforced by design.


## Design Principles

### Presence-Based Validation
The system checks **whether required information appears to be present**, not whether it is correct or sufficient.
Internal reasoning is limited to boolean facts such as:
- “Is a service referenced?”
- “Is a date present?”
- “Is supporting documentation included?”

No extracted values (names, dates, diagnoses, costs) are stored or reasoned over.

### Human-in-the-Loop
All outputs are advisory.  
Humans remain the final decision-makers.

### Explainability First
Every finding includes a plain-language rationale explaining *why* it may affect processing.

### Ethical considerations
This project includes an ETHICS.md document outlining guiding principles around privacy, data minimization, transparency, non-substitution of human decision-making, and respect for Indigenous rights and self-determination. The tool is designed to assist, not replace, human review.

## Post MVP
A future, institution-facing version of this system is intended to extend beyond submission-level validation and into systemic process analysis. In this phase, the platform would incorporate a Delay & Failure Pattern Analyzer designed to identify, measure, and aggregate structural causes of processing delays across cases.

To ensure that institutional diagnostics remain consistent, auditable, and non-arbitrary, future versions of the system are planned to incorporate formal policy modeling and verification using Lean.
