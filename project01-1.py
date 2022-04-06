import pandas as pd
from pandas import DataFrame

df = pd.read_excel("/Users/edaumedo1/Desktop/22년 1학기 강의목록 원본/경희대학교 국제캠퍼스22년 1학기 강의목록.xlsx")
df['대학교명']=input('대학교명:')
df['캠퍼스명']=input('캠퍼스명:')
df['강의실']='NaN'
df = df.rename(
        columns={
            '강좌코드강좌코드':'강의고유번호', 
            '강좌명강좌명':'강의명', 
            '교수명교수명':'교수명', 
            '대상학년대상학년':'학년', 
            '학점학점':'학점', 
            '이수구분이수구분':'이수구분', 
            '강의시간/강의실강의시간/강의실':'강의시간', #강의시간/강의실
            '특이사항특이사항':'특이사항'
        }
    )
i = 0
for t in range(0, len(df)):
    text=[],[]
    lines = str((df['강의시간'][t]))
    for k, l in enumerate(lines):
        if l=='(':
            i=1
            continue
        if l==')':
            i=0
            continue
        text[i].append(l)
    df['강의시간'][t] = ''.join(text[0])
    df['강의실'][t] = ''.join(text[1])
df = df[['대학교명', '캠퍼스명', '강의고유번호', '강의명', '교수명', '학년', '학점', '이수구분', '강의시간', '강의실', '특이사항']]
#         대학교명 -- 캠퍼스명 -- 강의고유번호 -- 강의명 -- 교수명 -- 학년 -- 학점 -- 이수구분 -- 강의시간 -- 강의실 -- 특이사항
print(df)

writer = pd.ExcelWriter('/Users/edaumedo1/Desktop/22년 1학기 강의목록 1차 가공/경희대학교 국제캠퍼스22년 1학기 강의목록.xlsx', engine='xlsxwriter')

## DataFrame을 xlsx에 쓰기
df.to_excel(writer, sheet_name='Sheet1')

## Pandas writer 객체 닫기
writer.close()
