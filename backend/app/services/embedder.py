from sentence_transformers import SentenceTransformer
from app.config import EMBED_MODEL_NAME

embedder = SentenceTransformer(EMBED_MODEL_NAME)


def embed_texts(texts):
    return embedder.encode(texts, convert_to_numpy=True, normalize_embeddings=True)


def embed_query(query: str):
    return embedder.encode([query], convert_to_numpy=True, normalize_embeddings=True)[0]