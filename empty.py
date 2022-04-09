'''start.py'''
# from public_module import readExcel, readFolderPath, writeExcel

# # 필터링할 데이터 정하기
# filtering_dic={
#   "lecture_number_list": ['학수번호', '과목번호', '학정번호', '강좌코드'],
#   "lecture_name_list": ['과목명', '강좌명'],
#   "professor_name_list": ['교강사명', '교수'],
#   "credit_list": ['학점'],
#   "division_list": ['구분', '종별'],
#   "lecture_time_list": ['시간'],
#   "lecture_room_list": ['강의실'],
#   "significant_list": ['특이사항', '유의사항', '비고'],
# }


# # 원본엑셀에 대한 제목들 가지고오기
# file_list = readFolderPath()
# # 원본엑셀에 대해 10개의 dataframe 리스트 가져오기    
# list = readExcel(file_list, filtering_dic)
# print(list[0])
# # for df in list:
#   # writeExcel(df)

# # # 이 반복문부터는 학교마다 달리 해야한다.
# # for i, df in enumerate(list):
# #   university_info_list = file_list[i].split(' ')[0:2]
# #   university_name = university_info_list[0]
# #   university_cname = university_info_list[1]
# #   df['대학교명'] = university_name

# #   if "년" in university_cname:
# #     if "캠퍼스" in university_cname:
# #       campus_str = university_cname.split('캠퍼스')[0]
# #       df['캠퍼스명'] = f'{campus_str}캠퍼스'
# #     else:  
# #       df['캠퍼스명'] = ''
# #   else:
# #     df['캠퍼스명'] = university_cname
  
#   # 파일 쓸 때 사용하는 함수. 주로 종료할 때 사용한다.

'''public_module.py'''
# import pandas as pd
# import os

# # 22년1학기강의데이터 폴더에 파일을 넣으면 자동적으로 되게끔한다.
# def readFolderPath():
#   path='./input'
#   file_list = os.listdir(path)
#   # print('file_list: {}'.format(file_list))
#   return file_list

# # 파일 이름이 모여있는 file_list 리스트를 인자로 넣으면 dataframe를 값으로 가지는 리스트가 만들어진다.
# def readExcel(file_list, filtering_dic):
#   univ_list = []
#   for i, el in enumerate(file_list):
#     university_info_list = file_list[i].split(' ')[0:2]
#     university_name = university_info_list[0]
#     university_cname = university_info_list[1]
    
#     university = pd.read_excel(io=f"./input/{el}")
#     column_dic = {}
#     # linkedStr = ','.join(university.columns.to_list())
#     university['대학교명'] = university_name
    
#     if "년" in university_cname:
#       if "캠퍼스" in university_cname:
#         campus_str = university_cname.split('캠퍼스')[0]
#         university['캠퍼스명'] = f'{campus_str}캠퍼스'
#       else:  
#         university['캠퍼스명'] = ''
#     else:
#       university['캠퍼스명'] = university_cname
#     # column_dic['대학교명'] = university_name
    
#     # if "년" in university_cname:
#     #   if "캠퍼스" in university_cname:
#     #     campus_str = university_cname.split('캠퍼스')[0]
#     #     column_dic['캠퍼스명'] = f'{campus_str}캠퍼스'
#     #   else:  
#     #     column_dic['캠퍼스명'] = ''
#     # else:
#     #   column_dic['캠퍼스명'] = university_cname
      
#     for col in filtering_dic['lecture_number_list']:
#       for data in university.columns.to_list():
#         if col in data:
#           column_dic[data] = '강의고유번호'
#     for col in filtering_dic['lecture_name_list']:
#       for data in university.columns.to_list():
#         if col in data:
#           column_dic[data] = '강의명'
#     for col in filtering_dic['professor_name_list']:
#       for data in university.columns.to_list():
#         if col in data:
#           column_dic[data] = '교수명'
#     for col in filtering_dic['credit_list']:
#       for data in university.columns.to_list():
#         if col in data:
#           column_dic[data] = '학년'
#     for col in filtering_dic['division_list']:
#       for data in university.columns.to_list():
#         if col in data:
#           column_dic[data] = '학점'
#     for col in filtering_dic['lecture_time_list']:
#       for data in university.columns.to_list():
#         if col in data:
#           column_dic[data] = '이수구분'
#     for col in filtering_dic['lecture_room_list']:
#       for data in university.columns.to_list():
#         if col in data:
#           column_dic[data] = '강의시간'
#     for col in filtering_dic['significant_list']:
#       for data in university.columns.to_list():
#         if col in data:
#           column_dic[data] = '특이사항'
    
#     print(column_dic.keys())
#     university = university.rename(
#       columns=column_dic
#     )
#     # university.columns.difference()
#     univ_list.append(university)

#   return univ_list



# # 파일 쓰기
# def writeExcel(univ):
#     univ_name = univ['대학교명'].to_list()[0]
#     univ_cname = univ['캠퍼스명'].to_list()[0]
#     print(univ_name, univ_cname)
#     writer = pd.ExcelWriter(f'./1차_가공/{univ_name} {univ_cname} 22년 1학기 1차 가공 완료.xlsx', engine='xlsxwriter')

#     ## DataFrame을 xlsx에 쓰기
#     univ.to_excel(writer, sheet_name='Sheet1')

#     ## Pandas writer 객체 닫기
#     writer.close()

    
