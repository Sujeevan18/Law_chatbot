from fastapi import APIRouter, HTTPException
from app.config import TOP_K
from app.models.schemas import ChatRequest, ChatResponse, SourceItem
from app.models.vector_store import vector_store
from app.services.retriever import search
from app.services.llm_service import generate_answer

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    if not vector_store.is_ready():
        raise HTTPException(status_code=400, detail="Documents are not indexed yet.")

    results = search(request.question, top_k=TOP_K)
    answer = generate_answer(request.question, results)

    sources = [
        SourceItem(
            source=r["source"],
            chunk_id=r["chunk_id"],
            score=r["score"],
            text=r["text"]
        )
        for r in results
    ]

    return ChatResponse(answer=answer, sources=sources)