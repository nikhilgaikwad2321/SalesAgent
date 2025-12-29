import os

# Configuration for LLM Backend
# Options: "ollama", "gemini"
LLM_BACKEND = os.getenv("LLM_BACKEND", "gemini").lower()

# Ollama Configuration
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = "llama3"

# Google Gemini Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyAoSWXeh7Cqyanf3Oe3BvljdlsUUkcDGwE")
GEMINI_MODEL = "gemini-2.5-flash"
