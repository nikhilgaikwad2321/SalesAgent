from pydantic import BaseModel, Field
from typing import Optional, Dict

class GenerateRequest(BaseModel):
    intent: str
    query: str
    response_language: str = "EN"
    filters: Optional[Dict[str, str]] = None

class GenerateResponse(BaseModel):
    response: str
    model: str
    ppt_file_path: Optional[str] = None
    ppt_file_name: Optional[str] = None
    status: str = "TEXT_RESPONSE"  # "TEXT_RESPONSE" or "PPT_GENERATED"
