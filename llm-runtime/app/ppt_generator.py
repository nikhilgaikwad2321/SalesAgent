from typing import List
from langchain_core.documents import Document
from app.ppt_prompt_builder import build_ppt_prompt, parse_llm_slide_content
from app.ppt_assembler import create_charts, assemble_ppt
from app.llm_factory import generate_response
import os


async def generate_ppt(query: str, context_docs: List[Document], language: str = "EN") -> dict:
    """
    Main PPT generation orchestrator.
    
    Steps:
    1. Use LLM to generate structured slide content (JSON)
    2. Generate charts using matplotlib (deterministic)
    3. Assemble PPT using python-pptx
    
    Returns:
        dict with ppt_file_path, ppt_file_name, and status
    """
    
    # Step 1: Generate slide content using LLM
    prompt = build_ppt_prompt(query, context_docs, language)
    llm_response = await generate_response(prompt)
    slide_content = parse_llm_slide_content(llm_response)
    
    # Step 2: Generate charts (deterministic)
    chart_paths = create_charts(slide_content)
    
    # Step 3: Assemble PPT
    ppt_file_path = assemble_ppt(slide_content, chart_paths)
    
    # Extract filename
    ppt_file_name = os.path.basename(ppt_file_path)
    
    # Cleanup chart files
    for chart_path in chart_paths:
        if os.path.exists(chart_path):
            try:
                os.remove(chart_path)
            except:
                pass  # Ignore cleanup errors
    
    return {
        "ppt_file_path": ppt_file_path,
        "ppt_file_name": ppt_file_name,
        "status": "PPT_GENERATED"
    }
