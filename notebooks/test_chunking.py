import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.ingestion.loader import load_documents_from_folder
from app.ingestion.chunker import split_documents

documents = load_documents_from_folder("data")

chunks = split_documents(documents)

print(f"Nombre de chunks : {len(chunks)}")

print("\n--- Premier chunk ---\n")
print(chunks[0].page_content)

print("\n--- Metadata ---\n")
print(chunks[0].metadata)