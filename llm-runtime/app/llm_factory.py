from app.config import LLM_BACKEND
from app import ollama_client
from app import gemini_client

async def generate_response(prompt: str) -> str:
    if LLM_BACKEND == "gemini":
        return await gemini_client.generate_response(prompt)
    else:
        # Default to Ollama
        return await ollama_client.generate_response(prompt)
