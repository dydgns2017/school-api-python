# school-api-python
해당 오픈소스는 https://github.com/agemor/school-api 를 참조하여 Python으로 json을 생성하는 목적으로 만들어졌습니다.

## 사용방법

리눅스 OS git clone 스크립트
```
git clone https://github.com/dydgns2017/school-api-python
cd school-api-python
```

윈도우 OS
```
Clone or Download를 누른 뒤,
코드 실행 시 python3 대신에 py를 입력하여 실행합니다.
ex ) py haksa.py [인자 값..] ..
```

#### 학사일정 json 파일 생성하기

다음과 같이 코드를 입력합니다.

데이터를 가지고오려면 다음과 같은 코드들이 필요합니다. [여기](https://github.com/dydgns2017/school-api-python#%EC%BD%94%EB%93%9C-%EA%B0%92%EB%93%A4%EC%97%90-%EB%8C%80%ED%95%9C-%EC%84%A4%EB%AA%85%EC%9D%80-%EB%8B%A4%EC%9D%8C%EA%B3%BC-%EA%B0%99%EC%8A%B5%EB%8B%88%EB%8B%A4)를 참조해주세요.

```
python3 haksa.py "교육청 코드" "학교 고유코드" "학교 분류코드" "연도" "월"
```

예시 ) 송파공업고등학교
```
ex )
python3 haksa.py "stu.sen.go.kr" "B100000593" "4" "2018" "11"


생성된 학사일정 파일은 haksa.json 파일로 생성됩니다.
예시로 생성된 학사 데이터를 확인하면 다음과 같습니다.

cat haksa.json

{
    "22": "군특 군부대 현장실습/3",
    "29": "None",
    "12": "None",
    "10": "토요휴업일",
    "21": "군특 군부대 현장실습/3",
    "14": "대학수학능력시험 감독관 회의",
    "15": "재량휴업일",
    "05": "None",
    "20": "군특 군부대 현장실습/3",
    "28": "None",
    "02": "1,2,3,4,3,4교시 수업",
    "19": "군특 군부대 현장실습/3",
    "08": "None",
    "03": "토요휴업일",
    "17": "토요휴업일",
    "30": "봉사활동",
    "07": "None",
    "13": "None",
    "09": "노동인권교육 실시",
    "27": "신입생 원서접수(특별전형)",
    "26": "신입생 원서접수(특별전형)",
    "23": "군특 군부대 현장실습/3",
    "06": "None",
    "16": "None",
    "24": "토요휴업일",
    "01": "None"
}
```
#### 급식 json 파일 생성하기

석식 및 다른 것들은 정규표현식 쓰는거 귀찮아서 급식 정보는 중식(점심)만 파싱합니다.
중식외에 필요한 데이터가 있으시다면, 코드를 직접확인하면서 고쳐주세요. 어렵지않습니다.

다음과 같이 코드를 입력합니다.

데이터를 가지고오려면 다음과 같은 코드들이 필요합니다. [여기](https://github.com/dydgns2017/school-api-python#%EC%BD%94%EB%93%9C-%EA%B0%92%EB%93%A4%EC%97%90-%EB%8C%80%ED%95%9C-%EC%84%A4%EB%AA%85%EC%9D%80-%EB%8B%A4%EC%9D%8C%EA%B3%BC-%EA%B0%99%EC%8A%B5%EB%8B%88%EB%8B%A4)를 참조해주세요.

```
python3 menu py "교육청 코드" "학교 고유코드" "학교 분류코드" "연도 및 월" 
```

예시 ) 송파공업고등학교

```
ex )
python3 menu.py "stu.sen.go.kr" "B100000593" "4" "201811"

생성된 급식 메뉴 파일은 menu.json 파일로 생성됩니다.
예시로 생성된 메뉴 파일을 확인하면 다음과 같습니다.

cat menu.json

{
    "24": "None",
    "25": "None",
    "15": "None",
    "3": "None",
    "23": [
        "찰현미밥",
        "동태찌개5.6.14.16.18.",
        "감자전1.2.5.6.9.13.",
        "명엽채볶음5.6.14.16.18.",
        "실곤약야채무침5.6.13.",
        "배추김치9.13."
    ],
    " ": "None",
    "10": "None",
    "28": [
        "칼슘강화쌀밥",
        "맑은콩나물국5.",
        "제육김치볶음5.6.9.10.13.",
        "비름나물무침5.6.",
        "깍두기9.13.",
        "두부숙회5.6."
    ],
    "18": "None",
    "12": [
        "옥수수쌀밥",
        "미소된장국5.6.13.",
        "닭강정1.4.5.6.12.15.",
        "취나물무침5.6.",
        "소시지야채볶음2.5.6.10.12.13.14.16.18.",
        "배추김치9.13."
    ],
    "11": "None",
    "29": [
        "참치김치찌개5.9.13.",
        "흑미밥",
        "돈육숙주굴소스볶음5.6.10.12.13.",
        "야채달걀말이1.2.5.6.10.",
        "청포묵김가루무침5.6.13.",
        "총각김치9.13."
    ],
    "19": [
        "김구이",
        "옥수수쌀밥",
        "닭개장/당면사리1.5.6.8.13.",
        "해시브라운/케첩5.12.",
        "석박지9.13.",
        "얼갈이된장무침3.5.6.18.",
        "과일(사과)"
    ],
    "2": [
        "찰현미밥",
        "해물순두부찌개1.5.9.10.13.18.",
        "수제치즈함박1.2.5.6.9.10.12.13.",
        "매콤멸치볶음4.5.6.13.",
        "브로콜리/초고추장5.6.13.",
        "석박지9.13."
    ],
    "26": [
        "강황칼슘밥",
        "매콤돈육메추리알장조림1.2.5.6.10.13.",
        "고사리나물5.6.",
        "단감사과샐러드1.2.5.11.12.13.16.",
        "오징어무국5.6.13.",
        "배추김치9.13."
    ],
    "13": [
        "장조림버터볶음밥1.2.5.6.10.12.13.",
        "우동장국1.5.6.9.13.17.",
        "톳나물무침5.13.",
        "옥수수김치전1.5.6.9.13.18.",
        "깍두기9.13.",
        "연두부샐러드/흑임자드레싱1.5.6.11.12.13."
    ],
    "14": [
        "배추겉절이9.13.",
        "찹쌀떡5.13.",
        "더덕무침5.6.13.",
        "칼슘강화쌀밥",
        "얼큰짬뽕국1.5.6.9.10.13.18.",
        "닭봉조림5.6.12.13.",
        "고춧잎나물5.6."
    ],
    "7": [
        "찰보리밥",
        "얼큰소고기무국5.6.",
        "돈육짜장볶음2.5.6.10.12.13.18.",
        "배추김치9.13.",
        "꼬시래기무침5.6.13.",
        "짬뽕만두1.5.6.10.13."
    ],
    "6": [
        "칼슘강화쌀밥",
        "매콤어묵국1.5.6.13.",
        "시금치달걀찜1.2.6.",
        "오이도라지무침5.6.",
        "총각김치9.13.",
        "수제돈까스/돈까스소스1.2.5.6.10.12.13."
    ],
    "1": [
        "칼슘강화쌀밥",
        "시금치나물5.6.",
        "꽃맛살샐러드1.5.6.8.9.",
        "매콤돈사태떡찜5.6.10.",
        "김치콩나물국5.9.13.18.",
        "깍두기9.13."
    ],
    "20": [
        "찰현미밥",
        "고추잡채/꽃빵5.6.8.10.13.16.18.",
        "물만두국1.5.6.10.13.14.16.18.",
        "쇠미역초회5.6.13.",
        "매콤콩나물무침5.",
        "배추김치9.13."
    ],
    "27": [
        "찰현미밥",
        "도토리묵무침5.6.",
        "무생채13.",
        "배추김치9.13.",
        "근대된장국5.6.",
        "닭볶음탕5.6.8.13."
    ],
    "22": [
        "찰보리밥",
        "들깨미역국5.6.13.",
        "치즈불닭2.5.6.12.13.",
        "간장두부조림5.6.",
        "참나물생채13.",
        "깍두기9.13."
    ],
    "16": [
        "미트소스스파게티1.2.5.6.10.12.13.",
        "브로콜리크림스프2.5.6.",
        "수제피자1.2.5.6.10.12.13.",
        "수제오이피클",
        "만다린샐러드1.2.5.6.11.12.13.",
        "유자주스5.13."
    ],
    "21": [
        "미트볼오므라이스1.2.5.6.10.13.15.16.18.",
        "팽이버섯장국5.6.",
        "숙주나물",
        "텐더치킨샐러드1.5.6.12.13.",
        "총각김치9.13.",
        "라이트요구르트2."
    ],
    "17": "None",
    "8": [
        "칼슘강화쌀밥",
        "감자국5.6.13.14.16.18.",
        "가자미빵가루튀김1.2.5.6.13.16.",
        "매콤볼어묵곤약조림5.6.13.",
        "깍두기9.13.",
        "가지나물5.6."
    ],
    "4": "None",
    "5": [
        "흑미밥",
        "두부새우젓국5.6.9.13.",
        "안동찜닭5.6.8.13.",
        "매콤감자조림5.6.13.",
        "배추김치9.13.",
        "파래무침5.6.13."
    ],
    "30": [
        "칼슘강화쌀밥",
        "순대국6.10.13.",
        "오이무침13.",
        "석박지9.13.",
        "어묵채볶음5.6.",
        "북채후라이드5.6.14.15.16.18.",
        "파인애플"
    ],
    "9": [
        "호박고추장찌개5.6.10.13.",
        "돈육버섯불고기5.6.10.13.",
        "국물떡볶이1.5.6.13.",
        "햄감자채볶음2.5.6.10.",
        "석박지9.13.",
        "콩나물밥5.6."
    ]
}

```

## 코드 값들에 대한 설명은 다음과 같습니다.

#### 학교 고유코드

학교 고유코드는 밑에 있는 링크로 들어가서 코드 값을 찾습니다.

https://www.meatwatch.go.kr/biz/bm/sel/schoolListPopup.do

#### 교육청 코드

교육청 코드는 다음과 같습니다.

* 서울시 교육청 : sen.go.kr
* 경기도 교육청 : goe.go.kr
* 강원도 교육청 : kwe.go.kr
* 전라남도 교육청 : jne.go.kr
* 전라북도 교육청 : jbe.go.kr
* 경상남도 교육청 : gne.go.kr
* 경상북도 교육청 : kbe.go.kr
* 부산광역시 교육청 : pen.go.kr
* 제주자치도 교육청 : jje.go.kr
* 충청남도 교육청 : cne.go.kr
* 충청북도 교육청 : cbe.go.kr
* 광주광역시 교육청 : gen.go.kr
* 울산광역시 교육청 : use.go.kr
* 대전광역시 교육청 : dje.go.kr
* 인천광역시 교육청 : ice.go.kr
* 대구광역시 교육청 : dge.go.kr

#### 학교 분류 코드

* 유치원 : 1
* 초등학교 : 2
* 중학교 : 3
* 고등학교 : 4

#### 급식 종류 코드

* 조식 : 1
* 중식 : 2
* 석식 : 3

## 만든이
* **정용훈** - *University : Sunkyul Univ* -

## 참조
* https://github.com/agemor/school-api

## 라이센스
이 소프트웨어는 [MIT 라이센스](https://github.com/agemor/school-api/blob/master/LICENSE)를 따라 자유롭게 이용하실 수 있습니다.
