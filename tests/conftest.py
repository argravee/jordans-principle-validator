import pytest
from app.ingestion.pdf_extractor import PDFExtractor

@pytest.fixture
def extractor():
    return PDFExtractor()