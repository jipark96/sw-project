import numpy as np
import pandas as pd


# 강의고유번호 수정 함수
# 모든 대학이 '-' 뒤 삭제라서 다 똑같음
def lectureNumber(df):
    df['강의고유번호'] = df['강의고유번호'].str.split('-').str.get(0)     # '-' 기준으로 나누고 첫번째만 추출
    return df

# 경희대 교수명 수정 함수
def KhuProfessorName(df):
    df['교수명'] = df['교수명'].str.replace(pat=' / ..', repl='', regex=False)    # 교수명 수정
    df['교수명'] = df['교수명'].str.replace(pat='..', repl='', regex=False)
    df['교수명'] = df['교수명'].str.replace(pat=' / ', repl=',', regex=False)
    return df

# 고려대 강의명 수정 함수
def lectureName(df):
    df['강의명'] = df['강의명'].str.split('(').str.get(0)     # '(' 기준으로 나누고 첫번째만 추출
    return df

# 한국과학기술원 교수명 수정 함수
def KaistProfessorName(df):
    df['교수명'] = df['교수명'].str.replace(pat=' 외', repl='', regex=False)    # 교수명 수정
    df['교수명'] = df['교수명'].str.replace(pat=' ,', repl=',', regex=False)
    df['교수명'] = df['교수명'].str.replace(pat='담당교수미정', repl='', regex=False)
    return df

# 한국과학기술원 과목구분, 과정구분 삭제 함수
def subjectAndCourse(df):
    df = df.drop(df[df['과목구분'] == '개별연구'].index | df[df['과목구분'] == '선택(석/박사)'].index | df[df['과목구분'] == '졸업연구'].index | df[df['과목구분'] == '현장실습및연구'].index | df[df['과정구분'] == '석/박사과정'].index)