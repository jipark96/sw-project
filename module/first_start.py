# 1차 가공 실행파일
from public_module import readExcel, readFolderPath, writeExcel
from first_process_module import splitProfessor, del_blank, split_time, split_room
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

# 카이스트의 예외처리를 위한 딕셔너리 
# exception_dic={
#   ""
# }

Regular_Expression={
  "경희대학교": [
    '(?:(?:[월화수목금토일]|)(?:(?:\s|)(?:\d{2}:\d{2}|)-(?:\d{2}:\d{2}|)))',                #추출 정규표현식---[0] / 분리되어 있을 시  '(?:\w|\W)' 입력
    '(?:(?:(?:[월화수목금토일]|)(?:(?:\s|)(?:\d{2}:\d{2}|)-(?:\d{2}:\d{2}|)))|\(|\))'       #제거 정규표현식---[1] / 분리되어 있을 시  ''          입력
    ],
  "고려대학교": [
    '(?:[월화수목금토일]\((?:\d{2}|\d{1})(?:-(?:\d{2}|\d{1})|))\)',
    '(?:[월화수목금토일]\((?:\d{2}|\d{1})(?:-(?:\d{2}|\d{1})|))\)'
    ],
  "연세대학교": [     #분리되어있음
    '(?:\w|\W)',
    ''
    ], 
  "성균관대학교": [   #강의실 컬럼 X
    '',
    ''
    ], 
  "국민대학교": [    #강의실 컬럼 X
    '',
    ''
    ], 
  "한국과학기술원": [   #분리되어있음
    '(?:\w|\W)',
    ''
    ], 
  "한양대학교": [     #분리되어있음
    '(?:\w|\W)',
    ''
    ], 
}

# 원본엑셀에 대한 제목들 가지고오기
file_list = readFolderPath()
# 원본엑셀에 대해 10개의 dataframe 리스트 가져오기    
list = readExcel(file_list, filtering_dic)
for df in list:
  df["교수명"] = splitProfessor(df)
  df["강의명"] = del_blank(df)
  df["강의실"] = split_room(df, Regular_Expression)
  df["강의시간"] = split_time(df, Regular_Expression)
  writeExcel(df)