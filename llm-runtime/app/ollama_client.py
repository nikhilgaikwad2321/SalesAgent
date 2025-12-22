import httpx
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

async def generate_response(prompt: str) -> str:
    async with httpx.AsyncClient() as client:
        try:
            payload = {
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            }
            response = await client.post(OLLAMA_URL, json=payload, timeout=60.0)
            response.raise_for_status()
            result = response.json()
            return result.get("response", "")
        except httpx.ConnectError:
            print("WARNING: Ollama is not running. Returning MOCK response.")
            return "(MOCK RESPONSE) Ollama is offline. This is a placeholder answer based on the retrieved context. The key features of the Gold Plan include a sum assured up to $1 Million, policy terms from 10 to 40 years, and it covers death, but excludes suicide in the first year."
        except httpx.RequestError as exc:
            print(f"An error occurred while requesting {exc.request.url!r}.")
            raise
        except httpx.HTTPStatusError as exc:
            print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
            raise
