
from src.ingestion.pdf_processor import extract_pages
from src.ingestion.text_cleaner import clean_text

pdf_path = "data/uploads/sample_papers/research_paper.pdf"

pages = extract_pages(pdf_path)

print(f"Total extracted pages: {len(pages)}")

for page in pages[:2]:
    cleaned_text = clean_text(page["text"])

    print(f"\n--- Page {page['page']} ---")
    print(cleaned_text[:500])
