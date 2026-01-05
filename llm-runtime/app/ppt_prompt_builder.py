from typing import List
from langchain_core.documents import Document
import json

PPT_SYSTEM_INSTRUCTION = """
You are an AI assistant helping generate structured content for an insurance sales presentation.

Your goal is to create slide content that is:
- Client-specific and personalized
- Compliance-safe (no guarantees, no hallucinated data)
- Professional and trustworthy
- Based strictly on the provided RAG context

STRICT RULES:
- Use ONLY the provided context to generate content
- Do NOT invent policy features, pricing, guarantees, or returns
- Do NOT make financial promises or guarantees
- If information is missing, use placeholder text like "[To be discussed]"
- All financial illustrations must be marked as "indicative"

OUTPUT FORMAT:
You must return a valid JSON object with the following structure:
{
  "client_name": "string",
  "policy_name": "string",
  "slides": [
    {
      "title": "slide title",
      "content_type": "bullet_points|text|data",
      "content": ["list of bullet points"] or "text content",
      "data": {optional data for charts}
    }
  ]
}

REQUIRED SLIDES:
1. Customer Profile Summary (demographics, needs)
2. Why Insurance Is Needed (benefits, protection)
3. Policy Benefits (from RAG context)
4. Coverage and Premium Overview (data for chart)

Focus on family protection, financial security, and peace of mind.
"""


def build_ppt_prompt(query: str, context_docs: List[Document]) -> str:
    """
    Build a specialized prompt for PPT slide content generation.
    Returns a prompt that instructs the LLM to generate structured JSON.
    """
    context_text = "\n\n".join([doc.page_content for doc in context_docs])
    
    prompt = f"""
{PPT_SYSTEM_INSTRUCTION}

Context (Approved Policy Information):
{context_text}

Client Request: {query}

Generate slide content as a JSON object following the exact format specified above.
Ensure all content is derived from the context provided and is compliance-safe.

JSON Output:
"""
    return prompt


def parse_llm_slide_content(llm_response: str) -> dict:
    """
    Parse the LLM response to extract structured slide content.
    Handles cases where LLM might include markdown code blocks.
    """
    # Remove markdown code blocks if present
    response = llm_response.strip()
    if response.startswith("```json"):
        response = response[7:]
    if response.startswith("```"):
        response = response[3:]
    if response.endswith("```"):
        response = response[:-3]
    
    response = response.strip()
    
    try:
        return json.loads(response)
    except json.JSONDecodeError as e:
        # Fallback: create a basic structure
        return {
            "client_name": "Valued Client",
            "policy_name": "Insurance Policy",
            "slides": [
                {
                    "title": "Policy Information",
                    "content_type": "text",
                    "content": "Please contact us for detailed policy information."
                }
            ]
        }
