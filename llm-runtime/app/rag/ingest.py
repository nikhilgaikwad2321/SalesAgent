import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag.vector_store import create_vector_store

DOCS_DIR = "docs"

def ingest_documents():
    if not os.path.exists(DOCS_DIR):
        os.makedirs(DOCS_DIR)
        print(f"Created {DOCS_DIR} directory. Please add PDF files there.")
        return

    documents = []
    for file in os.listdir(DOCS_DIR):
        file_path = os.path.join(DOCS_DIR, file)
        if file.endswith(".pdf"):
            print(f"Loading {file_path}...")
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())
        elif file.endswith(".txt"):
            print(f"Loading {file_path}...")
            from langchain_community.document_loaders import TextLoader
            loader = TextLoader(file_path)
            documents.extend(loader.load())

    if not documents:
        print("No documents found to ingest.")
        return

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks.")

    create_vector_store(chunks)
    print("Vector store created and saved successfully.")

if __name__ == "__main__":
    ingest_documents()
