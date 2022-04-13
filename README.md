## 강의 정보 프로젝트

## **❗** 주의사항
- 커밋 메시지 남길 때 명확한 내용을 나타내기
- 완성된 엑셀 파일은 1차_가공 폴더나 2차_가공 폴더에 넣기
---
## **🤼‍♂️** 역할
- 1차 가공 파일, 2차 가공 파일
    - 덕주: 2
    - 준석: 3,5
    - 건형: 1, 공통모듈
- 2차 가공 파일 및 1차 가공 파일의 4번 
    - 지현, 민수
---
## **🖥️** 실행 방법
- 실행위치
    - sw-project이다.
- 명령어
    - 1차 가공하기: `python module/first_start.py`
    - 2차 가공하기: `python module/second_start.py`
- sw-project의 바로 아래에 실행시키면된다.
- 폴더 구조
    - 1차_가공: 1차 가공 결과(엑셀)가 담겨질 폴더이다.
    - 2차 가공: 2차 가공 결과(엑셀)가 담겨질 폴더이다.
    - input: 원본 대학교 강의목록 엑셀파일이 담겨져 있는 폴더이다.
    - module
        - first_start.py: 1차 가공에 대한 실행 파일
        - second_start.py: 2차 가공에 대한 실행 파일
        - first_process_module.py: 1차 가공에 대한 모듈
        - second_process_module.py: 2차 가공에 대한 모듈
        - public_module.py: 공통 모듈
        - regular_expression.py: 정규표현식 모음 파일
        - filtering_dic.py: 대학교 컬럼 필터링하기 위한 딕셔너리 파일
        - each_university_module.py: 각각의 대학교에 대한 모듈 파일 
---
## 설치해야하는 패키지
- openpyxl
- pandas
- xlsxwriter


## 교수명 분류 
- 경희대 국제 : /로 구분 , (영어교수 공백)
- 경희대 서울 : /
- 고려대 서울 : ,
- 고려대 세종 : ,
- 국민대 : 분리됨 ,(영어교수 공백)
- 성균관대 : 분리됨 
- 연세대 미래 : ,
- 연세대 신촌 : ,
- 카이스트 : , 
- 한양대 : 분리됨

