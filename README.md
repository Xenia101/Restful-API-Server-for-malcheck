# Restful API Server for malcheck

Restful API & JWT Authentication for malcheck

## JWT 란?
~

## API List
- File Upload (**POST**)
  - 검사할 파일을 서버로 업로드 할 수 있습니다.
  
## Usage
- **Request File Upload**
  - 사용자가 보유한 파일을 분석 요청할 때 사용하는 API로 HTTP POST 방식을 이용합니다.
  - API 요청은 아래와 같은 방식을 통해 이루어집니다.

  <pre>
  <strong>URL</strong> : http://malcheck.kr/api/upload
  <strong>METHOD</strong> : POST
  <strong>Headers</strong> : Authorization API Key
  <strong>Parameter</strong>
  file (필수) : 분석 대상 파일
  </pre>
  
  - 업로드한 파일은 요청 순서대로 분석을 합니다. 서버 상황 및 분석 대기 상황에 따라 분석이 지연될 수 있습니다.
  - API 요청이 제대로 전달된 경우에는 JSON 형태의 응답을 받을 수 있습니다
  
## [Python] Request Examples
- **Get API Key** `getkey.py`
```python
import requests

params = {"username":ID, "password":Password}
response = requests.post("http://malcheck.kr/login", json=params)
json_response = response.json()

print(json_response)
```

- **Request File Upload** `upload.py`
```python
import requests

API = PrivateKey

files = {
    "file": open("test.txt", "rb"),
    }

headers = {
    "Authorization" : "Bearer {}".format(API)
    }

response = requests.post("http://malcheck.kr/api/upload", files=files, headers=headers)

print(response.json())
```

## Response Example
- **Get API Key** `getkey.py`
```javascript
{
  'access_token' : PRIVATE_API_KEY
}
```

- **Request File Upload** `upload.py`
```javascript
{
  'status' : STATUS
}
```
