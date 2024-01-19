# 데이터명 : 한국주택금융공사_전세자금대출 금리 정보
# from : https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15082033
import requests

url = "http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list?serviceKey=NOwc2KnKKdZo0fTq9El1RuGx4DFKdnmlFSUQo0cbdgPEG7mjugWiJgvNxAQHGRAjOoCpmMg4FuvnrjUqRVzQ6A%3D%3D&pageNo=1&numOfRows=30&dataType=JSON"

# serviceKey=NOwc2KnKKdZo0fTq9El1RuGx4DFKdnmlFSUQo0cbdgPEG7mjugWiJgvNxAQHGRAjOoCpmMg4FuvnrjUqRVzQ6A%3D%3D
# &pageNo=1
# &numOfRows=10
# &dataType=JSON
params = {
            "serviceKey": "NOwc2KnKKdZo0fTq9El1RuGx4DFKdnmlFSUQo0cbdgPEG7mjugWiJgvNxAQHGRAjOoCpmMg4FuvnrjUqRVzQ6A%3D%3D",
            "pageNo": 1,
            "numOfRows": 10,
            "dataType": "JSON"
          }
response = requests.get(url)    # 해당 url 클릭

print(response.content)

pass