import requests
import os
from dotenv import load_dotenv

load_dotenv()

GROK_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROK_API_KEY = os.getenv("GROK_API_KEY")

headers = {
    "Authorization": f"Bearer {GROK_API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "mixtral-8x7b-32768",
    "messages": [
        {"role": "user", "content": "Say Hello"}
    ]
}

response = requests.post(GROK_API_URL, headers=headers, json=payload)

print(response.status_code)
print(response.text)
