import numpy as np
import pandas as pd


# 2차 가공 1번
def dropTimeAndLecture(df):
    df = df.drop(columns = ['강의시간', '강의실'])
    return df


# 2차 2번 (분반제거)
def killDistri(df):
    df['강의고유번호'] = df['강의고유번호'].str.slice(start=0, stop=6)
    return df


# 2차 가공 3번
# 교수명 여러개 분리 함수
def splitProfessorOnlyOne(df):
    df['교수명'] = df['교수명'].str.split(',')
    df = df.explode('교수명')
    return df


# 2차 가공 4번 (중복 강의 제거)
def dropDup(df):
    df = df.drop_duplicates(['강의고유번호', '강의명', '교수명'])
    return df

# 강의고유번호 수정 함수
# 모든 대학이 '-' 뒤 삭제라서 다 똑같음
def editLectureNumber(df):
    if (df['대학교명'].to_list()[0] == '한양대학교'):
        df['강의고유번호'] = df['강의고유번호'].str[::-1]
        df['강의고유번호'] = df['강의고유번호'].str.split('-', 1).str.get(1)
        df['강의고유번호'] = df['강의고유번호'].str[::-1]
    else:
        df['강의고유번호'] = df['강의고유번호'].str.split('-').str.get(0)
    return df

