
import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension: int = 384):
        self.index = faiss.IndexFlatIP(dimension)
        self.metadata = []

    def add(self, embeddings, chunks):
        vectors = np.asarray(embeddings, dtype=np.float32)

        if vectors.ndim != 2:
            raise ValueError("Embeddings must be a 2D array")

        if vectors.shape[1] != self.index.d:
            raise ValueError("Embedding dimension mismatch")

        if len(vectors) != len(chunks):
            raise ValueError("Each embedding needs one chunk")

        if len(vectors) == 0:
            return

        self.index.add(vectors)
        self.metadata.extend(chunks)

    def search(self, query_embedding, top_k: int = 3):
        if top_k <= 0:
            raise ValueError("top_k must be positive")

        if self.index.ntotal == 0:
            return []

        query = np.asarray(
            query_embedding, dtype=np.float32
        ).reshape(1, -1)

        if query.shape[1] != self.index.d:
            raise ValueError("Query embedding dimension mismatch")

        scores, indices = self.index.search(
            query, min(top_k, self.index.ntotal)
        )

        results = []

        for score, index in zip(scores[0], indices[0]):
            if index == -1:
                continue

            results.append({
                "score": float(score),
                "chunk": self.metadata[index]
            })

        return results
