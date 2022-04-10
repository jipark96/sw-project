import pandas as pd
import re

##########1차 가공 2번##########

#강의시간 추출하여 입력
def split_time(df, p):
    df = df.fillna("")
    classtime = df["강의시간"]
    array = []
    for t in range(0, int(classtime.size)):
        ct = str(df['강의시간'][t])
        newrow = ''.join(p.findall(ct))  #강의시간 추출하여 입력
        array.append(newrow)
    return array

#강의시간 추출하여 제거
def split_room(df, p):
    df = df.fillna("")
    classroom = df["강의실"]
    array = []
    for t in range(0, int(classroom.size)):
        cl = str(df['강의실'][t])
        newrow = re.sub(p, '', cl)   #강의시간 제거 후 입력
        array.append(newrow)      
    return array


