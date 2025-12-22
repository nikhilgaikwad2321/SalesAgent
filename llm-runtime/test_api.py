import httpx
import time
import sys

URL = "http://localhost:8000/llm/generate"

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

    payload = {
        "intent": "product_pitch",
        "query": "Explain the key features of the Gold Plan term insurance",
        "filters": {}
    }
    
    print(f"\nSending request to {URL} with payload: {payload}")
    
    try:
        response = httpx.post(URL, json=payload, timeout=120.0)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print("\n--- RESPONSE ---")
            print(data["response"])
            print("----------------")
            print(f"Model used: {data['model']}")
        else:
            print("Error response:", response.text)
            
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    test_generate()
