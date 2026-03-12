from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chat import router as chat_router
from app.routes.documents import router as documents_router

app = FastAPI(title="Sri Lankan Law Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(documents_router)


@app.get("/")
def root():
    return {"message": "Sri Lankan Law Chatbot API is running"}