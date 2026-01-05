import os
from langchain_community.document_loaders import PyPDFLoader

DOC_PATH = r"c:\Users\gaikw\OneDrive\Desktop\Sales-RAG model\llm-runtime\docs\Benefit Illustration.pdf"

def debug_pdf_load():
    if not os.path.exists(DOC_PATH):
        print(f"File not found: {DOC_PATH}")
        return

    print(f"Loading {DOC_PATH} with custom parser...")
    from app.rag.pdf_parser import load_pdf_with_tables
    pages = load_pdf_with_tables(DOC_PATH)
    
    print(f"Loaded {len(pages)} pages.")
    
    # Print first 2 pages content to see how tables look
    for i, page in enumerate(pages[:2]):
        print(f"--- Page {i+1} Content Start ---")
        print(page.page_content[:1000]) # Print first 1000 chars
        print(f"--- Page {i+1} Content End ---")
        print("\n")

if __name__ == "__main__":
    debug_pdf_load()
