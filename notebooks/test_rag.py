import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.embedding.embedder import get_embedding_model
from app.vectorstore.faiss_store import load_vector_store
from app.rag.pipeline import ask_question

embedding_model = get_embedding_model()

vector_store = load_vector_store(embedding_model)

question = "What is intelligent chatbot?"

response = ask_question(vector_store, question)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(response)