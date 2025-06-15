# import os, requests

# BASE_URL = "https://api.pluggy.ai"



# resp = requests.post(
#     f"{BASE_URL}/auth", json={"clientId": CLIENT_ID, "clientSecret": CLIENT_SECRET}
# )
# resp.raise_for_status()
# api_key = resp.json()["apiKey"]
# headers = {"X-API-KEY": api_key}

# payload = {
#     'connectorId': 1
# }
# connect_token = requests.post(f"{BASE_URL}/connect_token", headers=headers, json=payload)

# print(connect_token.json())
