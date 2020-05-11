import requests

API = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODkyMzIwNzgsIm5iZiI6MTU4OTIzMjA3OCwianRpIjoiMjU0YzQ0MTQtNzhiYy00NmQ3LWJhMzYtZjVkODMxNTUzYWU4IiwiZXhwIjoxNTg5MjMyOTc4LCJpZGVudGl0eSI6InRlc3QiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.a1qcC-wyh0zwj6q26R31pjmwWLf2eTkxZYWXN5BQ_LM"

headers = {
    "Authorization" : "Bearer {}".format(API)
    }

response = requests.get("http://127.0.0.1:5000/api/auth_test", headers=headers)
json_response = response.json()

print(json_response)
