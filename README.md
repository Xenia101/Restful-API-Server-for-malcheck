# Restful API Server for malcheck

Restful API & JWT Authentication for malcheck

## JWT 란?
<p align=center>
  <img src="https://github.com/Xenia101/Restful-API-Server-for-malcheck/blob/master/img/jwt.png?raw=true">
</p>

> JSON 형태로 인증토큰을 만들어 통신할때 쓰는 인증방식
>
> Header에 Authorization 값을 넣어서 Authorization Server로 보내서 인증
>
> References : [jwt.io](https://jwt.io/introduction/)

**header** : 토큰의 타입과 해시 암호화 알고리즘으로 구성
- 첫 번째는 토큰의 유형 (JWT)
- 두 번째는 HMAC, SHA256 또는 RSA 등 해시 알고리즘 

**payload** : 토큰에 담을 클레임(claim) 정보 → `name : value`의 한 쌍
> 클레임 : payload에 담는 정보의 한'조각' 
- 클레임의 정보는 등록된(registered) 클레임, 공개(public) 클레임, 비공개(private) 클레임으로 총 세 종류

**signature** : Secret key를 포함하여 암호화되어 

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

## [Python] Response Example
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
