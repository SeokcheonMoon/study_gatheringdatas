# from https://developers.naver.com/docs/serviceapi/search/news/news.md

import requests     # postman app 역할

# request 요청

url = "https://openapi.naver.com/v1/search/shop"
params = {"query" : "인공지능"}
headers = {"X-Naver-Client-Id" : "Dg690kkPEXNzVgZMaHjF", 
           "X-Naver-Client-Secret" : "qAexsRROOI"}

response = requests.get(url, params=params, headers=headers)

# response API 응답
response.content

# resonse.content를 json으로 변환
import json
contents = json.loads(response.content)

# 몽고 DB 저장
from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["data_go_kr"]
# collection 작업
collection_shop_info = database["search_shop_info"]
collection_shop_list = database["search_shop_list"]
# insert 작업 진행
result1 = collection_shop_info.insert_one({"lastBuildDate" : contents["lastBuildDate"], "total" : contents["total"],"start" : contents["start"],"display" : contents["display"]})

result2 = collection_shop_list.insert_many(contents["items"])

value_id = collection_shop_info.find({},{'_id' : 1})
relative_id = value_id['_id']

for x in range(len(contents["items"])) :
    contents["items"][x]['relative_id'] = relative_id

collection_shop_list.insert_many(contents["items"])
# result3 = collection_shop_list[contents["items"]].insert_many(collection_shop_info["_id"])

pass