import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.ingestion.loader import load_documents_from_folder
    
    
    
# Load documents from the data folder
documents = load_documents_from_folder("data")

# Display number of loaded documents
print(f"Number of documents: {len(documents)}")

# Display sample document content
print("\n--- Sample Document ---\n")
print(documents[0].page_content[:500])

# Display document metadata
print("\nMetadata:")
print(documents[0].metadata)

