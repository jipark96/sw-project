import re

#########교수명 분리##########

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

##########공백 제거##########

def del_blank(df):
    df = df.fillna("")
    classname =  df["강의명"]
    array= []
    for i in range(0, int(classname.size)):
        row = classname.iloc[i]
        newrow = row.replace(" ","")
        array.append(newrow)
    return(array)

##########강의시간 컬럼에서 강의시간만 추출##########
def split_time(df, Regular_Expression):
    array = []
    classtime = df["강의시간"]
    df = df.fillna("")
    univ_name = df['대학교명'].to_list()[0]
    reg_exp = re.compile(Regular_Expression[univ_name][0])  #re.compile(정규표현식[대학교명][0])
    
    for t in range(0, int(classtime.size)):
        newrow = Regular_Expression[univ_name][2].join(reg_exp.findall(str(df["강의시간"][t])))  #강의시간 추출하여 입력
        array.append(newrow.strip())
        
    return array

#강의시간 추출하여 제거
def split_room(df, Regular_Expression):
    array = []
    classroom = df["강의실"]
    df = df.fillna("")
    univ_name = df['대학교명'].to_list()[0]
    reg_exp = re.compile(Regular_Expression[univ_name][1])

    for t in range(0, int(classroom.size)):
        newrow = re.sub(reg_exp, '', str(df['강의실'][t]))   #강의시간 제거 후 입력
        array.append(newrow.strip())     

    return array

# 고려대 강의명 수정 함수
def editLectureName(df):
    df['강의명'] = df['강의명'].str.split('(영강)').str.get(0)     # '(' 기준으로 나누고 첫번째만 추출
    return df

# 경희대 교수명 수정 함수
def editKhuProfessorName(df):
    df['교수명'] = df['교수명'].str.replace(pat=' / ..', repl='', regex=False)    # 교수명 수정
    df['교수명'] = df['교수명'].str.replace(pat='..', repl='', regex=False)
    df['교수명'] = df['교수명'].str.replace(pat=' / ', repl=',', regex=False)
    return df


# 한국과학기술원 교수명 수정 함수
def editKaistProfessorName(df):
    df['교수명'] = df['교수명'].str.replace(pat=' 외', repl='', regex=False)    # 교수명 수정
    df['교수명'] = df['교수명'].str.replace(pat=' ,', repl=',', regex=False)
    df['교수명'] = df['교수명'].str.replace(pat='담당교수미정', repl='', regex=False)
    return df

# 한국과학기술원 과목구분, 과정구분 삭제 함수
def dropSubjectAndCourse(df):
    df = df.drop(df[df['이수구분'] == '개별연구'].index)
    df = df.drop(df[df['이수구분'] == '선택(석/박사)'].index)
    df = df.drop(df[df['이수구분'] == '졸업연구'].index)
    df = df.drop(df[df['과정구분'] == '석/박사과정'].index)
    return df