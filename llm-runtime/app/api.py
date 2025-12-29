from fastapi import APIRouter, HTTPException
from app.schemas import GenerateRequest, GenerateResponse
from app.rag.retriever import retrieve_context
from app.prompt_builder import build_prompt
from app.llm_factory import generate_response
from app.config import LLM_BACKEND, OLLAMA_MODEL, GEMINI_MODEL
from app.validator import validate_response, ComplianceError

router = APIRouter()

@router.post("/llm/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest):
    try:
        # 1. Retrieve Context
        context_docs = retrieve_context(request.query)
        
        # 2. Build Prompt
        prompt = build_prompt(request.query, context_docs)
        
        # 3. Generate Response via Ollama
        raw_response = await generate_response(prompt)
        
        # 4. Validate Response
        try:
            validated_response = validate_response(raw_response)
        except ComplianceError as e:
            # Handle compliance error (e.g., return a generic error or a modified response)
            # For now, we'll raise an HTTP exception
            raise HTTPException(status_code=422, detail=str(e))
            
        model_name = GEMINI_MODEL if LLM_BACKEND == "gemini" else OLLAMA_MODEL
        return GenerateResponse(response=validated_response, model=model_name)

    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(status_code=500, detail=str(e))
