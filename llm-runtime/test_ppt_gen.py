import asyncio
import os
from app.ppt_generator import generate_ppt
from langchain_core.documents import Document

async def test_ppt_generation():
    print("Starting PPT Generation Test...")
    
    # Mock Context
    mock_context = [
        Document(page_content="""
        Bajaj Allianz Life Smart Protect Goal
        Death Benefit: Sum Assured of ₹50 Lakhs.
        Maturity Benefit: Return of Premium.
        Premium: ₹25,000 per annum for 10 years.
        Policy Term: 20 Years.
        Returns: At 8% assumed rate, fund value is ₹10 Lakhs.
        Allocations: 50% Death Benefit, 25% Critical Illness.
        """)
    ]
    
    query = "Generate a presentation for Rahul Sharma, DOB 12-08-1990, Sum Assured 50 Lakhs"
    
    try:
        result = await generate_ppt(query, mock_context)
        print("\nSUCCESS: PPT Generated!")
        print(f"File Path: {result['ppt_file_path']}")
        print(f"File Name: {result['ppt_file_name']}")
        
        # Verify file exists
        if os.path.exists(result['ppt_file_path']):
            print("File verified on disk.")
        else:
            print("ERROR: File not found on disk.")
            
    except Exception as e:
        print(f"\nFAILURE: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_ppt_generation())
