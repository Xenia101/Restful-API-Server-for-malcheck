import requests

API = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODkyMzU5MTksIm5iZiI6MTU4OTIzNTkxOSwianRpIjoiMDBjZGU3MTgtZmMyYy00NDAyLWE4OTgtYTZiYzgyYmJjNGJhIiwiaWRlbnRpdHkiOiJ0ZXN0IiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.1tDZhUKcwL0lUJrVH8KdiwIu3cxknAeOP0aGZfST9SM"

files = {
    "file": open("test.txt", "rb"),
    }

headers = {
    "Authorization" : "Bearer {}".format(API)
    }

response = requests.post("http://127.0.0.1:5000/api/upload", files=files, headers=headers)

print(response.json())
