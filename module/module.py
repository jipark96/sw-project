import pandas as pd

# df.apply 및 str.replace를 활용한 공백 제거
df = pd.read_excel("./22년1학기강의데이터/경희대학교 국제캠퍼스22년 1학기 강의목록.xlsx", engine='openpyxl')

ndf = df.apply(lambda df: df.str.replace(" ",""), axis = 1)
print(ndf)

ndf.to_excel("data.xlsx", sheet_name="035420", index=False)