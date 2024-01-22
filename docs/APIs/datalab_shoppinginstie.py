# from https://openapi.naver.com/v1/datalab/shopping/categories

import requests     # postman app 역할

# request 요청

url = "https://openapi.naver.com/v1/datalab/shopping/categories"
headers = {"X-Naver-Client-Id" : "Dg690kkPEXNzVgZMaHjF", 
           "X-Naver-Client-Secret" : "qAexsRROOI"}
bodys = {
  "startDate": "2017-08-01",
  "endDate": "2017-09-30",
  "timeUnit": "month",
  "category": [
      {"name": "패션의류", "param": [ "50000000"]},
      {"name": "화장품/미용", "param": [ "50000002"]}
  ],
  "device": "pc",
  "gender": "f",
  "ages": [ "20",  "30"]
}


response = requests.post(url, headers=headers, json=bodys)

# response API 응답
response.content

# resonse.content를 json으로 변환
import json
contents = json.loads(response.content)

pass