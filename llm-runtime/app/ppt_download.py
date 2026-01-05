from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/llm/ppt/download/{filename}")
async def download_ppt(filename: str):
    """
    Endpoint to download generated PPT files.
    """
    # Security: Only allow alphanumeric, underscore, hyphen, and dot
    if not all(c.isalnum() or c in ('_', '-', '.') for c in filename):
        raise HTTPException(status_code=400, detail="Invalid filename")
    
    if not filename.endswith('.pptx'):
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    file_path = os.path.join("temp/ppts", filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(
        path=file_path,
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        filename=filename
    )
