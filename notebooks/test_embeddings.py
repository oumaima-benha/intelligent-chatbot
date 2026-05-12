import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.embedding.embedder import get_embedding_model


# Load embedding model
embedding_model = get_embedding_model()

# Sample text
text = "Artificial Intelligence is transforming the world."

# Generate embedding vector
embedding = embedding_model.embed_query(text)

# Display vector dimension
print(f"Vector dimension: {len(embedding)}")

# Display first values of the vector
print("\nFirst vector values:")
print(embedding[:10])

# Display last values of the vector
print("\nLast vector values:")
print(embedding[-10:])
