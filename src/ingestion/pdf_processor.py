
from pathlib import Path
from pypdf import PdfReader


def extract_pages(pdf_path: str | Path) -> list[dict]:
    """
    Extract text from a PDF while preserving page numbers.
    """

    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    reader = PdfReader(str(path))

    extracted_pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()

        if text:
            extracted_pages.append({
                "page": page_number,
                "text": text
            })

    return extracted_pages
 