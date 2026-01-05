import pypdf
from langchain_core.documents import Document
import os

def load_pdf_with_tables(file_path: str) -> list[Document]:
    """
    Loads a PDF file, extracting text using pypdf.
    Returns a list of LangChain Documents (one per page).
    """
    documents = []
    
    try:
        reader = pypdf.PdfReader(file_path)
        for i, page in enumerate(reader.pages):
            text_content = page.extract_text()
            
            if text_content:
                # Basic cleaning
                cleaned_text = text_content.strip()
                
                metadata = {"source": file_path, "page": i}
                documents.append(Document(page_content=cleaned_text, metadata=metadata))
            else:
                print(f"Warning: No text found on page {i} of {file_path}")
                
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        
    return documents
