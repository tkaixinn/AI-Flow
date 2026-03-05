import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"


def call_ai(prompt, max_tokens=1000, temperature=0.3):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-oss-120b",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=data)

    if response.status_code != 200:
        raise Exception(f"API Error: {response.text}")

    result = response.json()

    return result["choices"][0]["message"]["content"]