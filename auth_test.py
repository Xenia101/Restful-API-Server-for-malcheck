import requests

API = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODkyOTQ1ODQsIm5iZiI6MTU4OTI5NDU4NCwianRpIjoiOWIzNjA4ZDItMmI5Zi00YmQ0LTk2ZDgtNDY4NDUyZDMwMjFkIiwiZXhwIjoxNjIwODMwNTg0LCJpZGVudGl0eSI6InRlc3QiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.pqd69R3EkfHM17KDbaoR0K-fREvRJNYImdAAN0_bv1s"

headers = {
    "Authorization" : "Bearer {}".format(API)
    }

response = requests.get("http://127.0.0.1:5000/api/auth_test", headers=headers)
json_response = response.json()

print(json_response)

