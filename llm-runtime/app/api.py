from fastapi import APIRouter, HTTPException
from app.schemas import GenerateRequest, GenerateResponse
from app.rag.retriever import retrieve_context
from app.prompt_builder import build_prompt
from app.llm_factory import generate_response
from app.config import LLM_BACKEND, OLLAMA_MODEL, GEMINI_MODEL
from app.validator import validate_response, ComplianceError
from app.ppt_generator import generate_ppt

router = APIRouter()

@router.post("/llm/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest):
    try:
        # 1. Retrieve Context
        context_docs = retrieve_context(request.query)
        
        # 2. Intent-based routing
        if request.intent == "PPT_GENERATION":
            # PPT Generation Flow
            ppt_result = await generate_ppt(request.query, context_docs, request.response_language)
            
            model_name = GEMINI_MODEL if LLM_BACKEND == "gemini" else OLLAMA_MODEL
            
            # Construct Download URL (Assuming API is mounted at /api)
            # Safe filename handling
            filename = ppt_result['ppt_file_name']
            download_url = f"/api/llm/ppt/download/{filename}"
            
            return GenerateResponse(
                response=f"Presentation generated successfully: {filename}",
                model=model_name,
                ppt_file_path=download_url, # Now returning URL instead of local path for frontend
                ppt_file_name=filename,
                status=ppt_result['status']
            )
        else:
            # Existing flow for other intents
            # 3. Build Prompt
            prompt = build_prompt(request.query, context_docs, request.response_language)
            
            # 4. Generate Response via LLM
            raw_response = await generate_response(prompt)
            
            # 5. Validate Response
            try:
                validated_response = validate_response(raw_response)
            except ComplianceError as e:
                raise HTTPException(status_code=422, detail=str(e))
                
            model_name = GEMINI_MODEL if LLM_BACKEND == "gemini" else OLLAMA_MODEL
            return GenerateResponse(
                response=validated_response, 
                model=model_name,
                status="TEXT_RESPONSE"
            )

    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(status_code=500, detail=str(e))
