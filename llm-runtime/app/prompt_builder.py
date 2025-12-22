from typing import List
from langchain_core.documents import Document

SYSTEM_INSTRUCTION = """
You are a sales assistant AI.
Use ONLY the provided context to answer the user's question.
If information is missing, say 'Information not available'.
Do not invent or assume.
"""

def build_prompt(query: str, context_docs: List[Document]) -> str:
    context_text = "\n\n".join([doc.page_content for doc in context_docs])
    
    prompt = f"""
{SYSTEM_INSTRUCTION}

Context:
{context_text}

User Query: {query}

Answer:
"""
    return prompt
