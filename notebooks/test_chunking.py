import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.ingestion.loader import load_documents_from_folder
from app.ingestion.chunker import split_documents

# Load documents
documents = load_documents_from_folder("data")

# Split documents into chunks
chunks = split_documents(documents)

# Display number of chunks
print(f"Number of chunks: {len(chunks)}")

# Display first chunk
print("\n--- First Chunk ---\n")
print(chunks[0].page_content)

# Display metadata
print("\n--- Metadata ---\n")
print(chunks[0].metadata)

# Display last chunk
print("\n--- Last Chunk ---\n")
print(chunks[-1].page_content)