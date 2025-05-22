import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API Key from environment
GROK_API_KEY = os.getenv("GROK_API_KEY")

# Debugging: Print the loaded API key to check if it's being loaded properly
if not GROK_API_KEY:
    raise ValueError("API Key not found in .env file. Please check your .env file.")
print("Grok API Key Loaded:", GROK_API_KEY)

GROK_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def query_grok_api(prompt):
    headers = {
        "Authorization": f"Bearer {GROK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "allam-2-7b",  # Use the new model "allam-2-7b"
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(GROK_API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        res_json = response.json()
        return res_json["choices"][0]["message"]["content"].strip()
    else:
        raise Exception(f"API Error: {response.status_code} - {response.text}")
