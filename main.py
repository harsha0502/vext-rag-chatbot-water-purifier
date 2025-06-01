import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = os.getenv("VEXT_URL")  # Example: https://payload.vextapp.com/hook/VTUK9NZT65/catch/hello

headers = {
    "Content-Type": "application/json",
    "Apikey": f"Api-Key {API_KEY}"
}

data = {
    "payload": "What’s the best water purifier you offer?"
}

response = requests.post(URL, headers=headers, json=data)
print("Bot Response:", response.text)
