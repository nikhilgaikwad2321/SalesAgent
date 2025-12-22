# Sales Agent CRM - LLM Runtime Service

This is the LLM Runtime Service for the Sales Agent CRM, built with FastAPI, Ollama, and LangChain.

## Prerequisites

1. **Python 3.10+**
2. **Ollama** installed and running (`ollama serve`).
3. **Llama3** model pulled:
   ```bash
   ollama pull llama3
   ```
4. **PDF Documents** placed in `llm-runtime/docs/`.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Ingest Documents
Before running the API, you must ingest your PDF documents into the vector store.
Place your PDFs in the `docs/` folder (create it if it doesn't exist) and run:

```bash
python -m app.rag.ingest
```

This will create a `faiss_index` directory.

### 2. Run the API Server
Start the FastAPI server:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. API Endpoints

**POST /llm/generate**

Request:
```json
{
  "intent": "product_pitch",
  "query": "Explain term insurance",
  "filters": {}
}
```

Response:
```json
{
  "response": "Term insurance is...",
  "model": "llama3"
}
```

## detailed Architecture

- **API**: FastAPI
- **LLM**: Ollama (llama3)
- **RAG**: LangChain + FAISS + BGE-Base-EN Embeddings
- **Validation**: Custom validation for banned phrases.
