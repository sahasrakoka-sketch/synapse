
from src.ingestion.pdf_processor import extract_pages
from src.ingestion.text_cleaner import clean_text
from src.processing.text_chunker import create_chunks
from src.embeddings.embedding_model import EmbeddingModel
from src.retrieval.vector_store import VectorStore

pdf_path = "data/uploads/sample_papers/research_paper.pdf"

# Extract and clean PDF
pages = extract_pages(pdf_path)

for page in pages:
    page["text"] = clean_text(page["text"])

# Create chunks
chunks = create_chunks(pages)

# Generate embeddings
model = EmbeddingModel()
texts = [chunk["text"] for chunk in chunks]
embeddings = model.generate_embeddings(texts)

# Store vectors in FAISS
store = VectorStore(dimension=384)
store.add(embeddings, chunks)

# Search using a question
question = "How does self-attention work?"
query_embedding = model.generate_embeddings([question])

results = store.search(query_embedding, top_k=3)

print("Total stored vectors:", store.index.ntotal)

for result in results:
    print("\nSimilarity score:", result["score"])
    print("Page:", result["chunk"]["page"])
    print("Text:", result["chunk"]["text"][:300])
