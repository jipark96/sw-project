import numpy as np
import pandas as pd

#엑셀 불러오기
df = pd.read_excel

#연세대학교 교수명 여러개 분리 함수
def professorYS(df):
    df['교수명'] = df['교수명'].str.split(',')
    df = df.explode('교수명')
    return df


