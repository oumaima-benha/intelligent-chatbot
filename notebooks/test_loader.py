import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.ingestion.loader import load_documents_from_folder
    
    
    
docs = load_documents_from_folder("data")

print(f"Nombre de documents : {len(docs)}")

print("\n--- Exemple de document ---\n")
print(docs[0].page_content[:500])
print("\nMetadata :", docs[0].metadata)