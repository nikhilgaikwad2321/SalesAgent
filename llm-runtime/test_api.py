import httpx
import time
import sys

URL = "http://localhost:8000/api/llm/generate"

def test_generate():
    print("Waiting for server to start...")
    for i in range(30):
        try:
            httpx.get("http://localhost:8000/docs", timeout=1.0)
            print("Server is up!")
            break
        except Exception:
            time.sleep(1)
            sys.stdout.write(".")
            sys.stdout.flush()
    else:
        print("\nServer failed to start in time.")
        return

    # TEST 1: Hindi Response
    payload_hi = {
        "intent": "product_pitch",
        "query": "Explain the key features of the Gold Plan term insurance",
        "response_language": "HI",
        "filters": {}
    }
    
    print(f"\n[TEST 1] Sending HINDI request to {URL}...")
    try:
        response = httpx.post(URL, json=payload_hi, timeout=120.0)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print("\n--- HINDI RESPONSE ---")
            print(data["response"])
            print("----------------------")
        else:
            print("Error response:", response.text)
    except Exception as e:
        print(f"Request failed: {e}")

    # TEST 2: PPT Generation & Download URL Check
    payload_ppt = {
        "intent": "PPT_GENERATION",
        "query": "Create a presentation for Mr. Sharma interested in Gold Plan",
        "response_language": "EN",
        "filters": {}
    }

    print(f"\n[TEST 2] Sending PPT GENERATION request to {URL}...")
    try:
        response = httpx.post(URL, json=payload_ppt, timeout=180.0)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print("\n--- PPT RESPONSE ---")
            print(f"Status: {data['status']}")
            print(f"File Name: {data['ppt_file_name']}")
            print(f"Download Path: {data['ppt_file_path']}")
            
            # Verify Download URL format
            if data['ppt_file_path'].startswith("/api/llm/ppt/download/"):
                print("SUCCESS: Download URL format is correct.")
            else:
                print("FAILURE: Download URL format is incorrect.")
                
        else:
            print("Error response:", response.text)
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    test_generate()
