import requests, re, json, sys

## sys.argv로 인자값을 받음
try:
    officeCode=sys.argv[1] ## 교육청 코드
    schulCode=sys.argv[2] ## 학교 고유코드
    schulCrseCode=sys.argv[3] ## 학교 분류코드 (고등학교, 중학교, 초등학교)
    schulKndScCode="0" + str(sys.argv[3]) ## 학교 분류코드
    schYm=sys.argv[4]
except:
    print("""!!ERROR.... 
            코드 인자 값이 맞지 않거나 값이 이상합니다.
            제대로 된 코드 값을 입력해주십쇼""")
    sys.exit(1)

##neis web requests
URL="https://" + officeCode + "/sts_sci_md00_001.do"
##params = {'schulCode': 'B100000593', 'schulCrseScCode': '4', 'schulKndScCode' : '04', 'ay' : str(year)} 
params = {'schulCode': str(schulCode), 'schulCrseScCode': str(schulCrseCode), 'schulKndScCode' : str(schulKndScCode), 'schYm' : str(schYm)}
response = requests.get(URL, params=params).text
data = response[response.find("<tbody>"):response.find("</tbody>")]

## re 정규표현식으로 불필요한 데이터를 자르거나 변환
regex = re.compile(r'[\n\r\t]')
data=regex.sub('',data)
rex = re.compile(r'<div>(.*?)</div>', re.S|re.M)
data=rex.findall(data)

file_json={}
for dat in data:
    date=re.findall(r"[0-3][0-9]",dat[0:2])
    menu=dat[dat.find("[중식]<br />"):]
    if not date:
        date=dat[0:1]
        if date == "" or date == " ":
            continue
    if type(date) == list:
        date=date[0]
    menu = menu.split("<br />")
    menu.remove(menu[0])
    if not menu:
        menu="None"
    file_json.update({date : menu})
    
##Json 생성
with open('menu.json', 'w', encoding='utf-8') as outfile:
       json.dump(file_json, outfile, sort_keys = False, indent=4, ensure_ascii=0)
