import pytest
from pathlib import Path

from app.ingestion.exceptions import (
    InvalidPasswordError,
    CorruptPDFError,
    ImageOnlyPDFError,
)

FIXTURE_DIR = Path(__file__).parent / "fixtures"


# ---------------------------
# Page Boundary Preservation
# ---------------------------
def test_page_boundaries_preserved(extractor):
    result = extractor.extract_pdf(
        FIXTURE_DIR / "simple_two_page.pdf"
    )

    assert len(result.pages) == 2
    assert "page 1 header" in result.pages[0].text.lower()
    assert "page 2 header" in result.pages[1].text.lower()


# ---------------------------
# Whitespace Normalization
# ---------------------------
def test_whitespace_normalization(extractor):
    result = extractor.extract_pdf(
        FIXTURE_DIR / "whitespace_heavy.pdf"
    )

    text = result.pages[0].text

    assert "     " not in text
    assert "\t" not in text
    assert "this line has multiple spaces." in text.lower()


# ---------------------------
# Multi Page Count
# ---------------------------
def test_multi_page_count(extractor):
    result = extractor.extract_pdf(
        FIXTURE_DIR / "multi_page.pdf"
    )

    assert len(result.pages) == 3


# ---------------------------
# Password Protected (Correct)
# ---------------------------
def test_password_correct(extractor):
    result = extractor.extract_pdf(
        FIXTURE_DIR / "password_protected.pdf",
        password="123"
    )

    assert "password protected pdf" in result.pages[0].text.lower()


# ---------------------------
# Password Protected (Wrong)
# ---------------------------
def test_password_wrong(extractor):
    with pytest.raises(InvalidPasswordError):
        extractor.extract_pdf(
            FIXTURE_DIR / "password_protected.pdf",
            password="wrongpass"
        )


# ---------------------------
# Image Only PDF Rejection
# ---------------------------
def test_image_only_rejected(extractor):
    with pytest.raises(ImageOnlyPDFError):
        extractor.extract_pdf(
            FIXTURE_DIR / "image_only.pdf"
        )


# ---------------------------
# Corrupt PDF Handling
# ---------------------------
def test_corrupt_pdf(extractor):
    with pytest.raises(CorruptPDFError):
        extractor.extract_pdf(
            FIXTURE_DIR / "corrupt.pdf"
        )
