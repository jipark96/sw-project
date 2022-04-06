from public_module import readExcel, readFolderPath, writeExcel

# 원본엑셀에 대한 제목들 가지고오기
file_list = readFolderPath()
# 원본엑셀에 대해 10개의 dataframe 리스트 가져오기    
list = readExcel(file_list)

# 이 반복문부터는 학교마다 달리 해야한다.
for i, df in enumerate(list):
  university_info_list = file_list[i].split(' ')[0:2]
  university_name = university_info_list[0]
  university_cname = university_info_list[1]
  df['대학교명'] = university_name

  if "년" in university_cname:
    df['캠퍼스명'] = ''
  else:
    df['캠퍼스명'] = university_cname
  
  # 파일 쓸 때 사용하는 함수. 주로 종료할 때 사용한다.
  writeExcel(df)