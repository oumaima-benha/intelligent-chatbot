# Intelligent Chatbot with Retrieval-Augmented Generation (RAG)

An intelligent chatbot that answers questions over a custom knowledge base using **Retrieval-Augmented Generation (RAG)**.

This project combines:
- document ingestion
- text chunking
- local embeddings
- vector similarity search with FAISS
- a local LLM through Ollama
- a FastAPI backend
- a simple evaluation pipeline
- Dockerized deployment

The main goal is to build a **grounded chatbot** that answers based on your documents instead of relying only on the model’s internal knowledge.

---

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [How to Run the Project](#how-to-run-the-project)
- [API Usage](#api-usage)
- [Evaluation](#evaluation)
- [Docker](#docker)
- [Common Issues](#common-issues)
- [Roadmap](#roadmap)
- [License](#license)

---

## Overview

Traditional chatbots answer mostly from the knowledge learned during training.  
This project goes further by using a **retrieval layer** that searches inside a custom document base and injects the most relevant passages into the prompt before generating an answer.

That makes the chatbot more:
- accurate
- context-aware
- grounded in your documents
- suitable for domain-specific use cases

This repository is designed as a strong AI engineering portfolio project and demonstrates a complete RAG workflow from raw documents to API deployment.

---

## How It Works

The pipeline is divided into four main stages:

### 1. Document ingestion
Documents such as PDFs and text files are loaded and converted into a common internal format.

### 2. Chunking
Large documents are split into smaller overlapping chunks to preserve context while making retrieval more precise.

### 3. Embedding and indexing
Each chunk is converted into a vector embedding using a local HuggingFace model, then stored in a FAISS vector index.

### 4. Retrieval + generation
When a user asks a question:
- the question is embedded
- FAISS finds the most similar chunks
- the retrieved context is sent to a local LLM through Ollama
- the LLM generates a grounded answer

---

## Features

- Question answering over custom documents
- Semantic search using embeddings
- Document chunking with overlap
- Local, free embeddings using HuggingFace
- FAISS vector store for fast retrieval
- Local LLM inference with Ollama
- FastAPI backend for API access
- Basic evaluation pipeline
- Dockerized application for easy deployment

---

## Tech Stack

### Core
- **Python**
- **LangChain**
- **FAISS**
- **FastAPI**
- **Pydantic**

### NLP / AI
- **Sentence Transformers**
- **HuggingFace Embeddings**
- **Ollama**
- **Mistral**

### DevOps
- **Docker**
- **Docker Compose**

---

## Project Structure

```text
rag-chatbot/
├── app/
│   ├── api/
│   │   └── main.py
│   ├── ingestion/
│   │   ├── loader.py
│   │   └── chunker.py
│   ├── embedding/
│   │   └── embedder.py
│   ├── vectorstore/
│   │   └── faiss_store.py
│   ├── rag/
│   │   └── pipeline.py
│   └── evaluation/
│       └── eval.py
├── data/
│   ├── raw/
│   ├── processed/
│   ├── vectorstore/
│   └── evaluation_dataset.json
├── notebooks/
├── tests/
├── .env
├── .gitignore
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd rag-chatbot
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you are setting things up manually, the project typically needs:
- `langchain`
- `langchain-community`
- `langchain-core`
- `langchain-text-splitters`
- `langchain-ollama`
- `sentence-transformers`
- `faiss-cpu`
- `fastapi`
- `uvicorn`
- `python-dotenv`
- `pydantic`
- `pypdf`

---

## Environment Variables

This project is designed to work **without paid APIs** for embeddings and retrieval.

If you use Ollama locally, you do not need an API key for embeddings.

You may still create a `.env` file if you want to manage future secrets or configuration values.

Example `.env`:

```env
# Example only
APP_ENV=development
```

If you later switch to a paid provider for generation or embeddings, you can add variables such as:

```env
OPENAI_API_KEY=your_key_here
```

Make sure `.env` stays in `.gitignore`.

---

## How to Run the Project

### Step 1: Add documents

Place your PDFs or text files inside the `data/` folder or a subfolder such as `data/raw/`.

### Step 2: Build the FAISS index

Run your ingestion and indexing scripts to:
- load documents
- chunk them
- create embeddings
- store them in FAISS

### Step 3: Start Ollama

Install Ollama from the official website and make sure it is running locally.

Then pull the model:

```bash
ollama pull mistral
```

### Step 4: Start the FastAPI server

```bash
uvicorn app.api.main:app --reload
```

### Step 5: Open the documentation

Visit:

```text
http://127.0.0.1:8000/docs
```

You can test the API directly from the Swagger UI.

---

## API Usage

### Health check

```http
GET /
```

Response:

```json
{
  "message": "RAG chatbot API is running"
}
```

### Ask a question

```http
POST /ask
```

Request body:

```json
{
  "question": "What is an intelligent chatbot?"
}
```

Response:

```json
{
  "question": "What is an intelligent chatbot?",
  "answer": "..."
}
```

---

## Evaluation

This project includes a basic evaluation workflow based on a JSON dataset.

The evaluation dataset contains questions related to the contents of the knowledge base, such as:
- intelligent chatbots
- RAG
- embeddings
- semantic search
- vector databases

The evaluation script:
- loads the vector store
- runs predefined questions
- generates answers
- displays expected vs generated outputs

This is useful for:
- checking retrieval quality
- spotting weak chunking
- validating prompt behavior
- comparing improvements over time

---

## Docker

Docker makes the project easier to run in a reproducible environment.

### Build the image

```bash
docker build -t rag-chatbot .
```

### Run the container

```bash
docker run -p 8000:8000 rag-chatbot
```

### Run with Docker Compose

```bash
docker compose up --build
```

### Notes
- The FastAPI app can run inside Docker.
- Ollama is usually easier to run locally on your machine first.
- If needed, you can later dockerize the full stack, including the model runtime.

---

## Common Issues

### `ModuleNotFoundError: langchain_community`
Install the package inside your active virtual environment:

```bash
pip install langchain-community
```

### `ModuleNotFoundError: langchain.prompts`
Use:

```python
from langchain_core.prompts import PromptTemplate
```

### Docker Desktop error on Windows
If Docker says it cannot connect to the Docker API, it usually means the Docker daemon is not running. Open Docker Desktop and make sure it is fully started.

### Ollama not responding
Make sure:
- Ollama is installed
- the service is running
- the model has been pulled with `ollama pull mistral`

### Empty or bad document extraction
Some PDFs may be difficult to parse. Try:
- another PDF
- a cleaner text file
- improved loaders in the ingestion layer

---

## Roadmap

Possible next improvements:
- add a web UI with Streamlit or React
- add chat memory
- add source citations in answers
- improve retrieval with reranking
- add hybrid search
- add authentication to the API
- add logging and monitoring
- deploy to cloud infrastructure
- create CI/CD pipelines

---

## License

This project is currently provided for educational and portfolio purposes.  
---

## If you want to improve this project, here is what you can add or do

You can make this project significantly stronger by adding a real user interface, improving retrieval quality with reranking or hybrid search, storing chat history for multi-turn conversations, showing the source chunks used to generate each answer, adding proper logging and error handling, writing automated tests, creating CI/CD with GitHub Actions, and deploying the application to the cloud so it can be used like a real product. Another strong upgrade would be to benchmark different embedding models and local LLMs to compare quality, speed, and cost.
