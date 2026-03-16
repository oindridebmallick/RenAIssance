import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai
import traceback

def test_api():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    print(f"Testing API with key: {api_key[:5]}...{api_key[-5:]}" if api_key else "NO KEY")
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        print("Sending prompt...")
        response = model.generate_content("Say 'Hello World'")
        print(f"Success! Response: {response.text}")
    except Exception as e:
        print("\n--- ERROR CAUGHT ---")
        traceback.print_exc()

if __name__ == "__main__":
    test_api()
