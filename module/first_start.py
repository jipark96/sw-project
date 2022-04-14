# 1차 가공 실행파일
# from re import sub
from public_module import readExcel, readFolderPath, writeExcel
from first_process_module import splitProfessor, del_blank, split_time, split_room
from each_university_module import editLectureNumber, editKhuProfessorName, editLectureName, editKaistProfessorName, dropSubjectAndCourse
from regular_expression import regular_expression
import pandas as pd

# 원본엑셀에 대한 제목들 가지고오기
file_list = readFolderPath("input")
# 원본엑셀에 대해 10개의 dataframe 리스트 가져오기    
univ_df_list, filtering_dic = readExcel(file_list)
for df in univ_df_list:
  df["교수명"] = splitProfessor(df)
  df["강의명"] = del_blank(df)
  df["강의실"] = split_room(df, regular_expression)
  df["강의시간"] = split_time(df, regular_expression)
  df = editLectureNumber(df)
  
  if (df["대학교명"].to_list()[1] == '경희대학교'):
    df = editKhuProfessorName(df)
  elif (df["대학교명"].to_list()[1] == '고려대학교'):
    df = editLectureName(df)
  elif (df["대학교명"].to_list()[1] == '한국과학기술원'):
    df = editKaistProfessorName(df)
    df = dropSubjectAndCourse(df)
  df = df.dropna(axis= 0, subset=["강의고유번호"], how="any")
  
  df = df.reset_index(drop=True)
  df.index=df.index + 1
  
  writeExcel(df, "1차_가공", "22년 1학기 1차")