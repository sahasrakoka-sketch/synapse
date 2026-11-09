
def create_chunks(
    pages: list[dict],
    chunk_size: int = 500,
    overlap: int = 100
) -> list[dict]:

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be non-negative and smaller than chunk_size")

    chunks = []
    chunk_id = 0

    for page_data in pages:
        words = page_data["text"].split()
        start = 0

        while start < len(words):
            end = min(start + chunk_size, len(words))

            chunk_text = " ".join(words[start:end])

            chunks.append({
                "chunk_id": chunk_id,
                "page": page_data["page"],
                "text": chunk_text
            })

            chunk_id += 1

            if end == len(words):
                break

            start = end - overlap

    return chunks
