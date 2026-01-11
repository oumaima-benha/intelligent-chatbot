import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.ingestion.loader import load_documents_from_folder
from app.ingestion.chunker import split_documents
from app.embedding.embedder import get_embedding_model
from app.vectorstore.faiss_store import (
    create_vector_store,
    save_vector_store,
    load_vector_store
)

# Load documents
documents = load_documents_from_folder("data")

# Split documents into chunks
chunks = split_documents(documents)

# Load embedding model
embedding_model = get_embedding_model()

# Create vector store
vector_store = create_vector_store(chunks, embedding_model)

# Save vector store
save_vector_store(vector_store)

print("Vector store created and saved successfully.")

# Reload vector store
loaded_vector_store = load_vector_store(embedding_model)

# Perform similarity search
query = "What is artificial intelligence?"

results = loaded_vector_store.similarity_search(query, k=3)

print("\nTop Results:\n")

for i, result in enumerate(results):

    print(f"Result {i+1}:\n")
    print(result.page_content[:300])
    print("\n" + "-"*50 + "\n")