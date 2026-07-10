import json

with open(r"D:\simontara_Json.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data["private_key"])