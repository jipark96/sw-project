import numpy as np
import pandas as pd

df = pd.read_excel("./input/경희대학교 국제캠퍼스22년 1학기 강의목록.xlsx")

# 강의고유번호 수정 함수
# 모든 대학이 '-' 뒤 삭제라서 다 똑같음
def lectureNumber():
    df['강의고유번호'] = df['강의고유번호'].str.split('-').str.get(0)     # '-' 기준으로 나누고 첫번째만 추출
    return df

# 경희대 교수명 수정 함수
def professorName():
    df['교수명'] = df['교수명'].str.replace(pat=' / ..', repl='', regex=False)    # 교수명 수정
    df['교수명'] = df['교수명'].str.replace(pat='..', repl='', regex=False)
    df['교수명'] = df['교수명'].str.replace(pat=' / ', repl=',', regex=False)
    return df

# 고려대 강의명 수정 함수
def lectureName():
    df['강의명'] = df['강의명'].str.split('(').str.get(0)     # '(' 기준으로 나누고 첫번째만 추출
    return df

# 한국과학기술원 교수명 수정 함수
def professorName():
    df['교수명'] = df['교수명'].str.replace(pat=' 외', repl='', regex=False)    # 교수명 수정
    df['교수명'] = df['교수명'].str.replace(pat=' ,', repl=',', regex=False)
    df['교수명'] = df['교수명'].str.replace(pat='담당교수미정', repl='', regex=False)
    return df