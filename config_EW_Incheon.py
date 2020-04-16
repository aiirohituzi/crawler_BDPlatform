# 태블로 서버 로그인을 위한 메인 화면 url
target_login_EW_url = 'http://tableau.cretop.com/'

# 태블로 서버 : 홈/기본/EW/인천시_EW_보고서 urls
target_view_EW_urls = [
    'http://tableau.cretop.com/#/views/_EW_/01_EW?',
    'http://tableau.cretop.com/#/views/_EW_/02_EW?',
    'http://tableau.cretop.com/#/views/_EW_/03_EW?',
    'http://tableau.cretop.com/#/views/_EW_/04_EW?',
    'http://tableau.cretop.com/#/views/_EW_/05_EW?',
    'http://tableau.cretop.com/#/views/_EW_/06_EW?',
    'http://tableau.cretop.com/#/views/_EW_/07_EW?',
    'http://tableau.cretop.com/#/views/_EW_/08_EW?',
    'http://tableau.cretop.com/#/views/_EW_/09_EW?',
    'http://tableau.cretop.com/#/views/_EW_/'
]

# 로그인 계정 정보
User_EW_id = 'admin'
User_EW_pw = 'admin'

# 필요 파라메터 정보
param_info = [
    {"ew_cd", "field_cd"},
    {"gugun_cd", "ew_cd", "field_cd"},
    {"ew_cd", "field_cd"},
    {"gugun_cd", "ew_cd", "field_cd"},
    {"year", "month", "ew_cd", "field_cd"},
    {"year", "month", "gugun_cd", "ew_cd"},
    {"year", "month", "ew_cd", "field_cd"},
    {"year", "month", "gugun_cd", "ew_cd"},
]

# def get_params(index):
#     params = param_info[index]
#     result = []

#     length = len(params)
#     for n in range(length):
#         # 
#         result.append
#     return param_info[index]

# 누락 화면 처리용
temp = [
    '01_EW?ew_cd=E3&field_cd=F',
]

# 시군구 코드
gugun_cd = [
    'K001',
    'K002',
    'K003',
    'K004',
    'K005',
    'K006',
    'K007',
    'K008',
    'K009',
    'K010'
]

# EW_GRAD
ew_cd = [
    'E0',
    'E1',
    'E2',
    'E3',
    'E4',
    'E5',
    'E6',
    'E7'
]

# 업종대분류 코드
field_cd = [
    'T',
    'F',
    'O',
    'B',
    'P',
    'U',
    'K',
    'A',
    'G',
    'Q',
    'L',
    'N',
    'E',
    'I',
    'R',
    'H',
    'D',
    'M',
    'J',
    'C',
    'S'
]

# 연도
year = [
    '2020',
    '2019',
    '2018'
]

# 월
month = [
    '01',
    '02',
    '03',
    '04',
    '05',
    '06',
    '07',
    '08',
    '09',
    '10',
    '11',
    '12'
]