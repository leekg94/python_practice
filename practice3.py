import requests as req
day={"월요일":"mon","화요일":"tue","수요일":"wed","목요일":"thu","금요일":"fri","토요일":"sat","일요일":"sun"}
print(day[input])
url = "http://webtoon.daum.net/data/pc/webtoon/list_serialized/"+day[input]

response = req.get(url).json()

for toon in response["data"]:
  print(toon["title"])
  print("http://webtoon.daum.net/webtoon/view/"+ toon["nickname"])
  print("http://webtoon.daum.net/webtoon/view/"+ str(toon["latestWebtoonEpisode"]["id"]))
