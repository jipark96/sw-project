# 2차 가공 실행파일
from second_process_module import dropTimeAndLecture, killDistri, splitProfessorOnlyOne, dropDup, editLectureNumber
from public_module import readExcel2, readFolderPath, writeExcel

# 1차 가공 엑셀에 대한 제목들 가지고오기
file_list = readFolderPath("1차_가공")
# 1차 가공 엑셀에 대해 10개의 dataframe 리스트 가져오기    
univ_df_list = readExcel2(file_list)
for df in univ_df_list:

  df = dropTimeAndLecture(df)
  df = editLectureNumber(df)
  df = killDistri(df)
  df = splitProfessorOnlyOne(df)
  df = dropDup(df)
  
  df = df.reset_index(drop=True)
  df.index=df.index + 1
  writeExcel(df, "2차_가공", "22년 1학기 2차")