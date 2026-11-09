
from src.embeddings.embedding_model import EmbeddingModel
from src.ingestion.pdf_processor import extract_pages
from src.ingestion.text_cleaner import clean_text
from src.processing.text_chunker import create_chunks

pdf_path = "data/uploads/sample_papers/research_paper.pdf"

pages = extract_pages(pdf_path)

for page in pages:
    page["text"] = clean_text(page["text"])

chunks = create_chunks(pages)

model = EmbeddingModel()

texts = [chunk["text"] for chunk in chunks[:3]]

embeddings = model.generate_embeddings(texts)

print("Number of chunks:", len(texts))
print("Embedding shape:", embeddings.shape)
print("First embedding:", embeddings[0][:10])
