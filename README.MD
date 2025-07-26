# 🧠 LLM-Powered Medical Query Retrieval API

A fast and intelligent Retrieval-Augmented Generation (RAG) API that uses OpenAI's LLMs to process natural language medical queries and return structured, contextual answers from relevant documents.

Built as part of HackRx 2024 (by Bajaj Finserv Health) 🏥💡

---

## 🔍 Problem Statement

Design a system that:
- Accepts a medical query in natural language
- Retrieves the most relevant medical documents
- Uses an LLM to generate a structured response
- Returns JSON output with contextual answer, summary, references, and a confidence score

---

## 📦 Tech Stack

| Layer         | Technology            |
|---------------|------------------------|
| Backend API   | FastAPI                |
| AI Model      | OpenAI GPT-3.5 / GPT-4 |
| Vector DB     | FAISS                  |
| Embeddings    | OpenAI Embeddings      |
| Doc Parsing   | LangChain + PyMuPDF    |
| Deployment    | Uvicorn / Render       |

---

## ⚙️ How It Works

# 🧠 Medical Query Resolution API (LLM-Powered RAG System)

This project is an intelligent **API endpoint** that takes medical queries as input and returns concise, relevant responses by leveraging a **Large Language Model (LLM)** and **retrieval-augmented generation (RAG)** from a custom medical knowledge base.

---

## 🔧 Tech Stack

* **LLM Provider**: OpenAI GPT / Google Gemini / LLaMA (configurable)
* **Backend**: Python, FastAPI
* **Vector DB**: FAISS
* **Document Parsing**: LangChain / PyMuPDF
* **Embedding Model**: OpenAI / HuggingFace
* **Storage**: Local / Cloud (for docs)
* **Others**: CORS, Logging, Error Handling

---

## 🚀 Features

* Accepts free-text **medical queries** via POST API
* Parses and embeds **PDF documents**
* Stores chunks in a **vector store**
* Fetches top matching chunks and runs LLM with context
* Returns structured JSON response
* Easily scalable and secure

---

