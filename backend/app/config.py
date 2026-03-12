import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
DATA_DIR = "data"
TOP_K = 5
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150
EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"