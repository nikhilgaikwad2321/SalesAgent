import google.generativeai as genai
from app.config import GOOGLE_API_KEY, GEMINI_MODEL

def configure_gemini():
    if not GOOGLE_API_KEY:
        print("WARNING: GOOGLE_API_KEY is not set. Gemini calls will fail.")
        return
    genai.configure(api_key=GOOGLE_API_KEY)

async def generate_response(prompt: str) -> str:
    try:
        configure_gemini()
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        # Fallback or re-raise depending on desired behavior. 
        # For now, we raise to let the upper layer handle it or user to see the error.
        raise e
