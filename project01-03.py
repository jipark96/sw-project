import pandas as pd
import os

# 22년1학기강의데이터 폴더에 파일을 넣으면 자동적으로 되게끔한다.
def readFolderPath():
    path='./input'
    file_list = os.listdir(path)
    # print('file_list: {}'.format(file_list))
    return file_list

# 파일 이름이 모여있는 file_list 리스트를 인자로 넣으면 dataframe를 값으로 가지는 리스트가 만들어진다.
def readExcel(file_list):
    univ_list = []
    for el in file_list:
    university = pd.read_excel(io=f"./input/{el}", )
    univ_list.append(university)
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

    
    
    
    
    
    
    
    
    # university_campus = university_info_list[1]
    # if "캠퍼스" in university_campus and not"년" in university_campus:
    #   print(university_campus)
    # for el in file_list:
    #     university_info_list = el.split(' ')[0:3]
    #     if not"년" in university_info_list:
    #       continue
    #   file_list.insert(0, )