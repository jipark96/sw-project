import pandas as pd
import re

df = pd.read_excel("22년1학기강의데이터/경희대학교 국제캠퍼스22년 1학기 강의목록.xlsx")
df['대학교명']='경희대'
df['캠퍼스명']='국제캠퍼스'
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

p = re.compile('\(([^)]+)') #\(([^)]+)
rm = re.compile('\([^)]*\)') #\([^)]*\)

for t in range(0, len(df)):
    ct = str(df['강의시간'][t])
    result = p.findall(ct)
    df['강의실'][t] = ' '.join(result)
    result2 = re.sub(rm, '', ct)
    df['강의시간'][t] = result2
    
df = df[['대학교명', '캠퍼스명', '강의고유번호', '강의명', '교수명', '학년', '학점', '이수구분', '강의시간', '강의실', '특이사항']]
#         대학교명 -- 캠퍼스명 -- 강의고유번호 -- 강의명 -- 교수명 -- 학년 -- 학점 -- 이수구분 -- 강의시간 -- 강의실 -- 특이사항

print(df)


writer = pd.ExcelWriter('1차_가공/경희대학교 국제캠퍼스22년 1학기 강의목록.xlsx', engine='xlsxwriter')

# ## DataFrame을 xlsx에 쓰기
df.to_excel(writer, sheet_name='Sheet1')

# ## Pandas writer 객체 닫기
writer.close()
