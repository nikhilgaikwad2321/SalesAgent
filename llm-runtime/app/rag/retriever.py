from app.rag.vector_store import load_vector_store

def retrieve_context(query: str, k: int = 3):
    vector_store = load_vector_store()
    if not vector_store:
        return []
    
    docs = vector_store.similarity_search(query, k=k)
    return docs
