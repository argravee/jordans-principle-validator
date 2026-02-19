from pathlib import Path
from typing import Optional, List

import pdfplumber
from pdfplumber.utils.exceptions import PdfminerException
from pdfminer.pdfdocument import PDFPasswordIncorrect
from pdfminer.pdfparser import PDFSyntaxError

from .models import Page, ExtractedDocument
from .exceptions import InvalidPasswordError, CorruptPDFError, ImageOnlyPDFError
from .normalizer import normalize_text
from .detectors.image_only_detector import is_image_only


class PDFExtractor:
    def extract_pdf(
            self,
            path: str | Path,
            password: Optional[str] = None
    ) -> ExtractedDocument:
        try:
            with pdfplumber.open(path, password=password) as pdf:

                # If it's encrypted and caller didn't provide a password,
                # treat that as "invalid/missing password" (not corrupt).
                if getattr(pdf, "is_encrypted", False) and password is None:
                    raise InvalidPasswordError()

                # Reject scanned / image-only PDFs
                if is_image_only(pdf):
                    raise ImageOnlyPDFError()

                pages: List[Page] = []

                for i, page in enumerate(pdf.pages):
                    raw_text = page.extract_text() or ""
                    normalized = normalize_text(raw_text)
                    pages.append(Page(page_number=i + 1, text=normalized))

                return ExtractedDocument(pages=pages)

        # Sometimes pdfminer throws this directly (rare with pdfplumber, but possible)
        except PDFPasswordIncorrect:
            raise InvalidPasswordError()

        # pdfplumber often wraps pdfminer errors in PdfminerException
        except PdfminerException as e:
            # pdfplumber passes the underlying exception as e.args[0]
            root = e.args[0] if e.args else e

            # Wrong password gets wrapped; detect it reliably
            if isinstance(root, PDFPasswordIncorrect) or "password" in str(root).lower() or "password" in str(e).lower():
                raise InvalidPasswordError()

            # Everything else here is "bad PDF" for our purposes
            raise CorruptPDFError()

        except PDFSyntaxError:
            raise CorruptPDFError()

        except ImageOnlyPDFError:
            raise

        except InvalidPasswordError:
            raise

        except Exception:
            raise CorruptPDFError()
