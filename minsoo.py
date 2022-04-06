import numpy as np
import pandas as pd

df = pd.read_excel("C:/Users/minsoo/Desktop/22년 1학기 강의목록 원본/경희대학교 국제캠퍼스22년 1학기 강의목록.xlsx")

#경희대 강의고유번호
df[['강의고유번호', '지울 부분']] = df['강좌코드강좌코드'].str.split('-', n=1, expand=True)     # '-' 기준으로 나누기
df = df.drop(['강좌코드강좌코드', '지울 부분'], axis=1)     # 필요없는 열 삭제


#경희대 교수명
df['교수명'] = df['교수명교수명'].str.replace(pat=' / ..', repl='', regex=False)    # 교수명 수정
df['교수명'] = df['교수명'].str.replace(pat='..', repl='', regex=False)
df['교수명'] = df['교수명'].str.replace(pat=' / ', repl=',', regex=False)

df = df.drop(['교수명교수명'], axis=1)      # 필요없는 열 삭제