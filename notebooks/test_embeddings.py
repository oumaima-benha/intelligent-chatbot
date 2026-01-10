import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.embedding.embedder import get_embedding_model

embedding_model = get_embedding_model()

text = "Artificial Intelligence is transforming the world."

embedding = embedding_model.embed_query(text)

print(f"Dimension du vecteur : {len(embedding)}")

print("\nPremières valeurs du vecteur :")
print(embedding[:10])

print("\nDernières valeurs du vecteur :")
print(embedding[-10:])