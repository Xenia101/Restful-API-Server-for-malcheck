import requests

API = ""

headers = {
    "Authorization" : "Bearer {}".format(API)
    }

response = requests.get("http://127.0.0.1:5000/api/auth_test", headers=headers)
json_response = response.json()

print(json_response)

