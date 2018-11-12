import requests, re, json, sys
from datetime import datetime

year=datetime.now().year

URL="https://stu.sen.go.kr/sts_sci_sf01_001.do"
params = {'schulCode': 'B100000593', 'schulCrseScCode': '4', 'schulKndScCode' : '04', 'ay' : str(year)} 
response = requests.get(URL, params=params).text
data = response[response.find("<tbody>"):response.find("</tbody>")]

## re 정규표현식으로 불필요한 데이터를 자르거나 변환
regex = re.compile(r'[\n\r\t]')
data=regex.sub('',data)
rex = re.compile(r'<div class="textL">(.*?)</div>', re.S|re.M)
data=rex.findall(data)

file_json={}
for dat in data:
    date=dat[dat.find("<em>"):dat.find("</em>")][4:]
    alert=dat[dat.find("<strong>"):dat.find("</strong>")][8:]
    if date == "":
        continue
    if alert == "":
        alert="None"
    file_json.update({date : alert})

##Json 생성
with open('haksa.json', 'w', encoding='utf-8') as outfile:
       json.dump(file_json, outfile, sort_keys = False, indent=4, ensure_ascii=0)
