# from https://developers.naver.com/docs/serviceapi/search/news/news.md

import requests     # postman app 역할

# request 요청

url = "https://openapi.naver.com/v1/search/news"
params = {"query" : "인공지능"}
headers = {"X-Naver-Client-Id" : "Dg690kkPEXNzVgZMaHjF", 
           "X-Naver-Client-Secret" : "qAexsRROOI"}

response = requests.get(url, params=params, headers=headers)

# response API 응답
response.content

# resonse.content를 json으로 변환
import json
contents = json.loads(response.content)

pass