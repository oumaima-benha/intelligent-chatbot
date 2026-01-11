from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

def create_rag_pipeline(vector_store):

    llm = OllamaLLM(model="mistral")

    prompt_template = """
    You are an AI assistant for question-answering tasks.

    Use ONLY the provided context to answer the question.

    If the answer is not contained in the context, say:
    "I don't know based on the provided documents."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    return llm, prompt


def ask_question(vector_store, question):

    llm, prompt = create_rag_pipeline(vector_store)

    # Retrieve relevant chunks
    retrieved_docs = vector_store.similarity_search(question, k=3)

    # Combine retrieved chunks
    context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    # Format final prompt
    final_prompt = prompt.format(
        context=context,
        question=question
    )

    # Generate answer
    response = llm.invoke(final_prompt)

    return response