from public_module import readExcel, readFolderPath, writeExcel

# 필터링할 데이터 정하기
filtering_dic={
  "lecture_number_list": ['학수번호', '과목번호', '학정번호', '강좌코드'],
  "lecture_name_list": ['과목명', '강좌명'],
  "professor_name_list": ['교강사명', '교수'],
  "credit_list": ['학점'],
  "division_list": ['구분', '종별'],
  "lecture_time_list": ['시간'],
  "lecture_room_list": ['강의실'],
  "significant_list": ['특이사항', '유의사항', '비고'],
}


# 원본엑셀에 대한 제목들 가지고오기
file_list = readFolderPath()
# 원본엑셀에 대해 10개의 dataframe 리스트 가져오기    
list = readExcel(file_list, filtering_dic)
print(list[0])
# for df in list:
  # writeExcel(df)
