# 1차 가공 실행파일
from public_module import readExcel, readFolderPath, writeExcel
from first_process_module import splitProfessor, del_blank
# 필터링할 데이터 정하기
filtering_dic={
  "강의고유번호": ['학수번호', '과목번호', '학정번호', '강좌코드'],
  "강의명": ['과목명', '강좌명'],
  "교수명": ['교강사', '교수'],
  "학년":["학년"],
  "학점": ['학점'],
  "이수구분": ['구분', '종별'],
  "강의시간": ['시간'],
  "강의실": ['강의실'],
  "특이사항": ['특이사항', '유의사항', '비고'],
}


# 원본엑셀에 대한 제목들 가지고오기
file_list = readFolderPath()
# 원본엑셀에 대해 10개의 dataframe 리스트 가져오기    
list = readExcel(file_list, filtering_dic)
for df in list:
  df["교수명"] = splitProfessor(df)
  df["강의명"] = del_blank(df)
  writeExcel(df)

  
  
 
