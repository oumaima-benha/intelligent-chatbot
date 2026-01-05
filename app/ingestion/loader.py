from langchain_community.document_loaders import PyPDFLoader, TextLoader
import os

def load_pdf(file_path: str):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents

def load_txt(file_path: str):
    loader = TextLoader(file_path)
    documents = loader.load()
    return documents

def load_documents_from_folder(folder_path: str):
    all_documents = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if filename.endswith(".pdf"):
            docs = load_pdf(file_path)
            all_documents.extend(docs)

        elif filename.endswith(".txt"):
            docs = load_txt(file_path)
            all_documents.extend(docs)

    return all_documents