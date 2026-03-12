from fastapi import APIRouter
from app.config import DATA_DIR
from app.models.schemas import DocumentStatusResponse
from app.models.vector_store import vector_store
from app.services.document_loader import load_documents, chunk_text
from app.services.embedder import embed_texts

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("/index", response_model=DocumentStatusResponse)
def index_documents():
    docs = load_documents(DATA_DIR)

    chunk_records = []
    chunk_texts = []

    for doc in docs:
        chunks = chunk_text(doc["text"])
        for i, chunk in enumerate(chunks):
            chunk_records.append({
                "source": doc["source"],
                "chunk_id": i,
                "text": chunk
            })
            chunk_texts.append(chunk)

    if not chunk_texts:
        return DocumentStatusResponse(
            message="No documents found",
            total_documents=0,
            total_chunks=0
        )

    embeddings = embed_texts(chunk_texts)
    vector_store.set_data(embeddings, chunk_records)

    return DocumentStatusResponse(
        message="Documents indexed successfully",
        total_documents=len(docs),
        total_chunks=len(chunk_records)
    )