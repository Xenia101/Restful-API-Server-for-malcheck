import requests

params = {"username":"test", "password":"test"}
response = requests.post("http://127.0.0.1:5000/login", json=params)

print(response.json())
