
from src.ingestion.pdf_processor import extract_pages
from src.ingestion.text_cleaner import clean_text
from src.processing.text_chunker import create_chunks

pdf_path = "data/uploads/sample_papers/research_paper.pdf"

pages = extract_pages(pdf_path)

for page in pages:
    page["text"] = clean_text(page["text"])

chunks = create_chunks(pages)

print("Total pages:", len(pages))
print("Total chunks:", len(chunks))

for chunk in chunks[:3]:
    print(f"\n--- Chunk {chunk['chunk_id']} | Page {chunk['page']} ---")
    print(chunk["text"][:300])
