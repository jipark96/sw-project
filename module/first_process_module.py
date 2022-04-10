import pandas as pd

# 데이터 프레임 불러오기 (모듈 붙이기)
# df = pd.read_excel("./22년1학기강의데이터/경희대학교 국제캠퍼스22년 1학기 강의목록.xlsx", engine='openpyxl')

# 전체 공백 제거 
# ndf = df.apply(lambda df: df.str.replace(" ",""), axis = 1)

# 교수명 분리
# df = df.fillna("")
#df명 수정


def splitProfessor(df):
    df = df.fillna("")
    professor = df["교수명"]
    array = []
    for i in range(0, int(professor.size)):
        row = professor.iloc[i]
        if "/" in row:
            newrow = list(map(lambda row: row.strip(), row.split("/")))
            newrow = ','.join(newrow)
            array.append(newrow)
                         
        elif " ," in row or ", " in row:
            newrow = list(map(lambda row: row.strip(), row.split(",")))
            newrow = ','.join(newrow)
            array.append(newrow)
        else:
            array.append(row)   
    return array
          



# 3번 replace를 활용한 공백 제거

#df["강좌명강좌명"] 수정바람

def del_blank(df):
    df = df.fillna("")
    classname =  df["강의명"]
    array= []
    for i in range(0, int(classname.size)):
        row = classname.iloc[i]
        newrow = row.replace(" ","")
        array.append(newrow)
    # print(array)
    return(array)

  


# df.to_excel("professor.xlsx", sheet_name="professor", index=False)


