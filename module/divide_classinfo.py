import pandas as pd
import re

# 데이터 프레임 불러오기 (모듈 붙이기)
# df = pd.read_excel("./22년1학기강의데이터/경희대학교 국제캠퍼스22년 1학기 강의목록.xlsx", engine='openpyxl')

# 전체 공백 제거 
# ndf = df.apply(lambda df: df.str.replace(" ",""), axis = 1)

# 교수명 분리
# df = df.fillna("")
#df명 수정

p = re.compile('(?:\/|,|\(|)(?:[월화수목금토일](?:(?:\s|)\d{2}:\d{2}(?:-|~)\d{2}:\d{2}|\s\d{2}:\d{2}|(?:\(|-|)(?:(?:\d{2}|\d{1})-(?:\d{2}|\d{1})|\d{2}:\d{2}-\d{2}:\d{2}|\d{2}|\d{1})(?:\)|)|\d{2}:\d{2}-\d{2}:\d{2}|\d[A-B])|(?:,|\.)(?:\d{2}|\d{1})(?:[A-B]|)|시간미지정강좌|-\s)(?:\)|)') #정규표현식 완료 : 경희대, 고려대

def split_time(df):
    df = df.fillna("")
    classtime = df["강의시간"]
    array = []
    for t in range(0, int(classtime.size)):
        ct = str(df['강의시간'][t])
        newrow = ''.join(p.findall(ct))  #강의시간 추출하여 입력
        array.append(newrow)
    return array

def split_room(df):
    df = df.fillna("")
    classroom = df["강의실"]
    array = []
    for t in range(0, int(classroom.size)):
        ct = str(df['강의실'][t])
        newrow = re.sub(p, '', ct)   #강의시간 제거 후 입력
        array.append(newrow)      
    return array




# 3번 replace를 활용한 공백 제거

#df["강좌명강좌명"] 수정바람



# df.to_excel("professor.xlsx", sheet_name="professor", index=False)


