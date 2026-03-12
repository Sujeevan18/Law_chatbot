import numpy as np


class VectorStore:
    def __init__(self):
        self.embeddings = None
        self.records = []

    def set_data(self, embeddings: np.ndarray, records: list):
        self.embeddings = embeddings
        self.records = records

    def is_ready(self):
        return self.embeddings is not None and len(self.records) > 0


vector_store = VectorStore()