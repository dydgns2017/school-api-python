import requests, re, json, sys

## sys.argv로 인자값을 받음
officeCode=sys.argv[1] ## 교육청 코드
schulCode=sys.argv[2] ## 학교 고유코드
schulCrseCode=sys.argv[3] ## 학교 분류코드 (고등학교, 중학교, 초등학교)
schulKndScCode="0" + str(sys.argv[3]) ## 학교 분류코드
ay=sys.argv[4]
mm=sys.argv[5]

##neis web requests
URL="https://" + officeCode + "/sts_sci_sf01_001.do"
##params = {'schulCode': 'B100000593', 'schulCrseScCode': '4', 'schulKndScCode' : '04', 'ay' : str(year)} 
params = {'schulCode': str(schulCode), 'schulCrseScCode': str(schulCrseCode), 'schulKndScCode' : str(schulKndScCode), 'ay' : str(ay), 'mm' : str(mm)}
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
