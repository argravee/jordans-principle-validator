from dataclasses import dataclass
from typing import Literal

@dataclass(frozen=True)
class FieldMetaData:
    filename: str
    upload_order : int

#submittied document information
@dataclass
class Document:
    document_id: str
    text: str
    role: str | None = None #REFACTOR: maybe constrain to enums in the future
    metadata: FieldMetaData | None = None

#presence checked facts
@dataclass
class Signals:
    # Identity & reference
    child_name_present: bool = False
    child_reference_consistent: bool = False
    guardian_name_present: bool = False
    relationship_to_child_present: bool = False

    # Service request
    service_mentioned: bool = False
    service_reference_consistent: bool = False
    service_description_present: bool = False
    service_duration_or_frequency_present: bool = False

    # Supporting documentation
    justification_document_present: bool = False
    supporting_doc_references_child: bool = False
    supporting_doc_references_service: bool = False
    rationale_language_present: bool = False

    # Author / provider
    author_name_present: bool = False
    author_role_present: bool = False
    provider_name_present: bool = False
    provider_contact_present: bool = False

    # Temporal
    document_date_present: bool = False
    assessment_date_present: bool = False
    service_start_date_present: bool = False
    service_end_or_duration_present: bool = False

    # Financial
    cost_present: bool = False
    currency_or_amount_format_present: bool = False
    cost_tied_to_service_present: bool = False

    # Authorization & consent
    consent_document_present: bool = False
    guardian_signature_present: bool = False
    signature_date_present: bool = False

    # Cross-document consistency (still presence-style)
    same_child_referenced_across_docs: bool = False
    same_service_referenced_across_docs: bool = False
    provider_consistent_where_applicable: bool = False

Severity = Literal["error","warning"]

@dataclass
class ValidationFinding:
    severity: Severity
    message: str
    rationale: str
    related_document_ids: list[str] | None = None