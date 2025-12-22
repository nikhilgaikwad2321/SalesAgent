from pydantic import BaseModel, Field
from typing import Optional, Dict

class GenerateRequest(BaseModel):
    intent: str
    query: str
    filters: Optional[Dict[str, str]] = None

class GenerateResponse(BaseModel):
    response: str
    model: str
