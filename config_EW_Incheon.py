# 태블로 서버 로그인을 위한 메인 화면 url
target_login_EW_url = 'http://tableau.cretop.com/'

# 태블로 서버 : 홈/기본/EW/인천시_EW_보고서 urls
target_view_EW_urls = [
    'http://tableau.cretop.com/#/views/_EW_/01_EW?',
    # 'http://tableau.cretop.com/#/views/_EW__0/01__EW?',   # 광명 01

    'http://tableau.cretop.com/#/views/_EW_/02_EW?',
    'http://tableau.cretop.com/#/views/_EW_/03_EW?',
    'http://tableau.cretop.com/#/views/_EW_/04_EW?',
    'http://tableau.cretop.com/#/views/_EW_/05_EW?',
    'http://tableau.cretop.com/#/views/_EW_/06_EW?',
    'http://tableau.cretop.com/#/views/_EW_/07_EW?',
    'http://tableau.cretop.com/#/views/_EW_/08_EW?',

    'http://tableau.cretop.com/#/views/_EW_/09_EW?',
    # 'http://tableau.cretop.com/#/views/_EW__0/09_EW?',    # 광명 09

    'http://tableau.cretop.com/#/views/_EW_/',
    # 'http://tableau.cretop.com/#/views/_EW__1/',      # 화성 누락 파라메터용 url

    # 'http://tableau.cretop.com/#/views/_EW__1/02_EW?',   # 화성 첫번째 화면 (ew, field)
    # 'http://tableau.cretop.com/#/views/_EW__1/04_EW?',     # 화성 두번째 화면 (ew, field)
    # 'http://tableau.cretop.com/#/views/_EW__1/05-4_-EW?',     # 화성 세번째 화면 (ew)
    'http://tableau.cretop.com/#/views/_EW__1/06-4_-?',       # 화성 네번째 화면 (ew)
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
    {"gugun_cd", "field_cd"}
]

# 누락 화면 처리용
temp = [
    # '01_EW?ew_cd=E3&field_cd=F', 형식 예시
    # ================ 04 누락 ====================
    # '04_EW?gugun_cd=K004&ew_cd=E1&field_cd=J',
    # '04_EW?gugun_cd=K005&ew_cd=E6&field_cd=Q',
    # '04_EW?gugun_cd=K005&ew_cd=E6&field_cd=L',
    # '04_EW?gugun_cd=K005&ew_cd=E6&field_cd=H',
    # '04_EW?gugun_cd=K006&ew_cd=E1&field_cd=S',
    # '04_EW?gugun_cd=K006&ew_cd=E4&field_cd=R',
    # '04_EW?gugun_cd=K007&ew_cd=E2&field_cd=N',
    # '04_EW?gugun_cd=K007&ew_cd=E6&field_cd=G',
    # '04_EW?gugun_cd=K008&ew_cd=E0&field_cd=G',
    # '04_EW?gugun_cd=K008&ew_cd=E0&field_cd=L',
    # '04_EW?gugun_cd=K008&ew_cd=E2&field_cd=H',
    # '04_EW?gugun_cd=K008&ew_cd=E2&field_cd=D',
    # '04_EW?gugun_cd=K008&ew_cd=E7&field_cd=G',
    # '04_EW?gugun_cd=K008&ew_cd=E7&field_cd=Q',
    # '04_EW?gugun_cd=K009&ew_cd=E1&field_cd=P',
    # '04_EW?gugun_cd=K009&ew_cd=E1&field_cd=U',
    # '04_EW?gugun_cd=K009&ew_cd=E1&field_cd=K',
    # '04_EW?gugun_cd=K009&ew_cd=E1&field_cd=A',
    # '04_EW?gugun_cd=K009&ew_cd=E5&field_cd=N',
    # '04_EW?gugun_cd=K009&ew_cd=E5&field_cd=E',
    # '04_EW?gugun_cd=K009&ew_cd=E5&field_cd=I',
    # '04_EW?gugun_cd=K009&ew_cd=E5&field_cd=C',
    # '04_EW?gugun_cd=K009&ew_cd=E5&field_cd=S',
    # '04_EW?gugun_cd=K009&ew_cd=E6&field_cd=T',
    # '04_EW?gugun_cd=K009&ew_cd=E6&field_cd=F',
    # '04_EW?gugun_cd=K009&ew_cd=E6&field_cd=O',
    # '04_EW?gugun_cd=K009&ew_cd=E6&field_cd=B',
    # '04_EW?gugun_cd=K009&ew_cd=E6&field_cd=P',
    # '04_EW?gugun_cd=K009&ew_cd=E6&field_cd=U',
    # '04_EW?gugun_cd=K009&ew_cd=E6&field_cd=K',
    # '04_EW?gugun_cd=K009&ew_cd=E6&field_cd=A',
    # '04_EW?gugun_cd=K009&ew_cd=E6&field_cd=G',
    # '04_EW?gugun_cd=K009&ew_cd=E7&field_cd=M',
    # '04_EW?gugun_cd=K010&ew_cd=E1&field_cd=L',
    # '04_EW?gugun_cd=K010&ew_cd=E2&field_cd=F',
    # '04_EW?gugun_cd=K010&ew_cd=E7&field_cd=M',
    # '04_EW?gugun_cd=K010&ew_cd=E7&field_cd=J',
    # ============================================
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
    # 'B004' # 광명 시군구
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