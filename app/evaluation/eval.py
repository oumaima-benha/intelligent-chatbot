import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from app.embedding.embedder import get_embedding_model
from app.vectorstore.faiss_store import load_vector_store
from app.rag.pipeline import ask_question


def load_evaluation_dataset(path):

    with open(path, "r", encoding="utf-8") as file:
        dataset = json.load(file)

    return dataset


def evaluate_rag():

    print("Loading embedding model...")
    embedding_model = get_embedding_model()

    print("Loading vector store...")
    vector_store = load_vector_store(embedding_model)

    print("Loading evaluation dataset...")
    dataset = load_evaluation_dataset(
        "data/evaluation_dataset.json"
    )

    print("\nStarting evaluation...\n")

    for index, sample in enumerate(dataset):

        question = sample["question"]
        expected_answer = sample["expected_answer"]

        generated_answer = ask_question(
            vector_store=vector_store,
            question=question
        )

        print("=" * 80)
        print(f"Sample {index + 1}")
        print("=" * 80)

        print(f"\nQuestion:\n{question}")

        print(f"\nExpected Answer:\n{expected_answer}")

        print(f"\nGenerated Answer:\n{generated_answer}")

        print("\n")


if __name__ == "__main__":
    evaluate_rag()