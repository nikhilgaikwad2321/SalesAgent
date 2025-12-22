import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

VECTOR_STORE_PATH = "faiss_index"
EMBEDDING_MODEL_NAME = "BAAI/bge-base-en-v1.5"

def get_embeddings():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

def save_vector_store(vector_store):
    vector_store.save_local(VECTOR_STORE_PATH)

def load_vector_store():
    if os.path.exists(VECTOR_STORE_PATH):
        return FAISS.load_local(VECTOR_STORE_PATH, get_embeddings(), allow_dangerous_deserialization=True)
    return None

def create_vector_store(chunks):
    vector_store = FAISS.from_documents(chunks, get_embeddings())
    save_vector_store(vector_store)
    return vector_store
