# Day 27: Working with APIs (requests), JSON
import requests
import json

response = requests.get("https://api.github.com")
data = response.json()
print(json.dumps(data, indent=2))
