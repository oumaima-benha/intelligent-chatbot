from fastapi import FastAPI
from pydantic import BaseModel

from app.embedding.embedder import get_embedding_model
from app.vectorstore.faiss_store import load_vector_store
from app.rag.pipeline import ask_question


# Initialize FastAPI app
app = FastAPI(
    title="RAG Chatbot API",
    description="API for Retrieval-Augmented Generation chatbot",
    version="1.0.0"
)


# Request schema
class QuestionRequest(BaseModel):
    question: str


# Load embedding model
embedding_model = get_embedding_model()

# Load vector store
vector_store = load_vector_store(embedding_model)


@app.get("/")
def root():

    return {
        "message": "RAG chatbot API is running"
    }


@app.post("/ask")
def ask(request: QuestionRequest):

    response = ask_question(
        vector_store=vector_store,
        question=request.question
    )

    return {
        "question": request.question,
        "answer": response
    }