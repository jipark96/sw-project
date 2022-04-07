import numpy as np
import pandas as pd

#엑셀 불러오기
df = pd.read_excel

#연세대학교 교수명
df = df['교수명'].str.split(',')  #split 각 행을 여러 컬럼으로 나눔
df=df.apply(lambda x: pd.Series(x))  #배열이 Series를 리턴하게 apply 적용, DataFrame 변환
df=df.stack().reset_index(level=1, drop=True).to_frame('교수명') #stack 컬럼을 행으로 변환, 인덱스 초기화
print(df)


