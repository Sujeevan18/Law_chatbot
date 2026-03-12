import numpy as np
from app.models.vector_store import vector_store
from app.services.embedder import embed_query


def search(query: str, top_k: int = 5):
    if not vector_store.is_ready():
        return []

    q_emb = embed_query(query)
    scores = vector_store.embeddings @ q_emb
    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []
    for idx in top_indices:
        item = vector_store.records[idx].copy()
        item["score"] = float(scores[idx])
        results.append(item)

    return results