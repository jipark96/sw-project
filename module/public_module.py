import pandas as pd
import os

'''중첩 함수'''

def makeColumn(university, df, col, keyword_list):
  isComplte = False
  for keyword in keyword_list:
    for data in university.columns.to_list():
      if keyword in data:
        df[col] = university[data]
        isComplte = True
        break
    if col in df.columns:
      break
  if isComplte == False:
    df[col] = ""

'''싱글 함수'''

# 함수 설명: 22년1학기강의데이터 폴더에 파일을 넣으면 자동적으로 되게끔하고,
# 여러 파일 이름이 담겨진 리스트를 반환한다.
def readFolderPath():
  path='./input'
  file_list = os.listdir(path)
  return file_list
    
# file_list: 파일 이름이 담겨져 있는 리스트
# filtering_dic: 각 컬럼에 대한 필터링 키워드가 담겨져있는 딕셔너리
# 함수 설명: file_list와 filtering_dic를 인자로 사용하면,
# 여러 개의 dataframe를 가지는 리스트를 반환한다.
def readExcel(file_list, filtering_dic):
  column_name_list = list(filtering_dic.keys())
  univ_list = []
  
  for file_name in file_list:
    university_info_list = file_name.split(' ')[0:2]
    university_name = university_info_list[0]
    university_cname = university_info_list[1]
    
    university = pd.read_excel(io=f"./input/{file_name}", engine='openpyxl')
    df = pd.DataFrame(data = [[university_name]], columns=["대학교명"], index=university.index)
    
    # df의 대학교 이름과 캠퍼스 이름 컬럼 생성하기
    if "년" in university_cname:
      if "캠퍼스" in university_cname:
        campus_str = university_cname.split('캠퍼스')[0]
        df['캠퍼스명'] = f'{campus_str}캠퍼스'
      else:  
        campus_str = university_cname.split('캠퍼스')[0]
        df['캠퍼스명'] = f'{campus_str}캠퍼스'
    else:
      df['캠퍼스명'] = university_cname
      
    # df의 컬럼 생성하기
    for col in column_name_list:
      makeColumn(university, df, col, filtering_dic[col])
      
    univ_list.append(df)

  return univ_list

# 파일 쓰기
def writeExcel(univ):
    univ_name = univ['대학교명'].to_list()[0]
    univ_cname = univ['캠퍼스명'].to_list()[0]
    # print(univ_name, univ_cname)
    writer = pd.ExcelWriter(f'./1차_가공/{univ_name} {univ_cname} 22년 1학기 1차 가공 완료.xlsx', engine='xlsxwriter')

    ## DataFrame을 xlsx에 쓰기
    univ.to_excel(writer, sheet_name='Sheet1')

    ## Pandas writer 객체 닫기
    writer.close()

    
