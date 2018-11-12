# school-api-python
해당 오픈소스는 https://github.com/agemor/school-api를 참조하여 Python으로 json을 생성하는 목적으로 만들어졌습니다.

## 사용방법

#### 학사일정 json 파일 생성하기

다음과 같이 코드를 입력합니다.

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
다음과 같이 코드를 입력합니다.

```

```

예시 ) 송파공업고등학교

```
ex )

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
