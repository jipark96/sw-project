import pandas as pd
import os

# 22년1학기강의데이터 폴더에 파일을 넣으면 자동적으로 되게끔한다.
def readFolderPath():
  path='./input'
  file_list = os.listdir(path)
  return file_list

# 파일 이름이 모여있는 file_list 리스트를 인자로 넣으면 dataframe를 값으로 가지는 리스트가 만들어진다.
def readExcel(file_list, filtering_dic):
  univ_list = []
  for i, el in enumerate(file_list):
    university_info_list = file_list[i].split(' ')[0:2]
    university_name = university_info_list[0]
    university_cname = university_info_list[1]
    
    university = pd.read_excel(io=f"./input/{el}", engine='openpyxl')
    df = pd.DataFrame(data = [[university_name]], columns=["대학교명"], index=university.index)
    
    # university['대학교명'] = university_name
    
    if "년" in university_cname:
      if "캠퍼스" in university_cname:
        campus_str = university_cname.split('캠퍼스')[0]
        df['캠퍼스명'] = f'{campus_str}캠퍼스'
        # university['캠퍼스명'] = f'{campus_str}캠퍼스'
      else:  
        df['캠퍼스명'] = f'{campus_str}캠퍼스'
        # university['캠퍼스명'] = ''
    else:
      df['캠퍼스명'] = university_cname
      # university['캠퍼스명'] = university_cname
      
    for col in filtering_dic['lecture_number_list']:
      for data in university.columns.to_list():
        if col in data:
          df["강의고유번호"] = university[data]
    for col in filtering_dic['lecture_name_list']:
      for data in university.columns.to_list():
        if col in data:
          df["강의명"] = university[data]
    for col in filtering_dic['professor_name_list']:
      for data in university.columns.to_list():
        if col in data:
          df["교수명"] = university[data]
    for col in filtering_dic['grade_list']:
      for data in university.columns.to_list():
        if col in data:
          df["학년"] = university[data]
    for col in filtering_dic['credit_list']:
      for data in university.columns.to_list():
        if col in data:
          df["학점"] = university[data]
    for col in filtering_dic['division_list']:
      for data in university.columns.to_list():
        if col in data:
          df["이수구분"] = university[data]
    for col in filtering_dic['lecture_time_list']:
      for data in university.columns.to_list():
        if col in data:
          df["강의시간"] = university[data]
    for col in filtering_dic['lecture_room_list']:
      for data in university.columns.to_list():
        if col in data:
          df["강의실"] = university[data]
    for col in filtering_dic['significant_list']:
      for data in university.columns.to_list():
        if col in data:
          df["특이사항"] = university[data]
    univ_list.append(df)

  return univ_list

# 파일 쓰기
def writeExcel(univ):
    univ_name = univ['대학교명'].to_list()[0]
    univ_cname = univ['캠퍼스명'].to_list()[0]
    print(univ_name, univ_cname)
    writer = pd.ExcelWriter(f'./1차_가공/{univ_name} {univ_cname} 22년 1학기 1차 가공 완료.xlsx', engine='xlsxwriter')

    ## DataFrame을 xlsx에 쓰기
    univ.to_excel(writer, sheet_name='Sheet1')

    ## Pandas writer 객체 닫기
    writer.close()

    
