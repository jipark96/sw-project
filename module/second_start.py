# 2차 가공 실행파일
from second_process_module import dropTheBeat, killDistri, professorOnlyOne, dropDup
from public_module import readExcel2, readFolderPath, writeExcel

# 1차 가공 엑셀에 대한 제목들 가지고오기
file_list = readFolderPath("1차_가공")
# 1차 가공 엑셀에 대해 10개의 dataframe 리스트 가져오기    
list = readExcel2(file_list)
for df in list:

  df = dropTheBeat(df)
  df = killDistri(df)
  df = professorOnlyOne(df)
  df = dropDup(df)

  writeExcel(df, "2차_가공", 2)