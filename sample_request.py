import requests
import json


data = {"name": "apple", "id": 10}

r = requests.post(
    "http://127.0.0.1:8000/fruit?amount=42",
    data=json.dumps(data)
)

print(r.json())
