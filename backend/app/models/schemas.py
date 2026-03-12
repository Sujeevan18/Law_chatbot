from pydantic import BaseModel
from typing import List


class ChatRequest(BaseModel):
    question: str


class SourceItem(BaseModel):
    source: str
    chunk_id: int
    score: float
    text: str


class ChatResponse(BaseModel):
    answer: str
    sources: List[SourceItem]


class DocumentStatusResponse(BaseModel):
    message: str
    total_documents: int
    total_chunks: int