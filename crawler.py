from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import xlsxwriter
from selenium.webdriver.common.alert import Alert
import re

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# import config
# import config_request

workbook = xlsxwriter.Workbook('kdx_1~500.xlsx')
worksheet = workbook.add_worksheet()

chrome_options = Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome('./chromedriver/chromedriver', chrome_options=chrome_options)

data = []

# for num in config_request.REQUEST_NUM:
#     print(num)
#     driver.get('https://kdx.kr/data/view?product_id=3181')
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')

#     requestName = soup.select(
#         '#id' + num + ' > td.b > a'
#     )

#     condition = soup.select(
#         '#id' + num + ' > td:nth-of-type(2)'
#         #id313290 > td:nth-child(2)
#     )

#     reward = soup.select(
#         '#id' + num + ' > td:nth-of-type(3)'
#     )

#     print('requestName : ' + requestName[0].text)
#     print('condition : ' + condition[0].text.rstrip().lstrip())
#     print('reward : ' + reward[0].text.rstrip().lstrip())

#     data.append({
#         'requestName': requestName[0].text,
#         'condition': condition[0].text.rstrip().lstrip(),
#         'reward': reward[0].text.rstrip().lstrip(),
#     })


for num in range(1, 501):
    driver.get(f'https://kdx.kr/data/view?product_id={num}')

    try:
        WebDriverWait(driver, 1).until(EC.alert_is_present())
        Alert(driver).accept()
        print(f'id:{num} 에러')
        continue
    except TimeoutException:
        print(f'id:{num} 크롤링')
        # print("Alert not found. Move on...")

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    data_set_name = soup.select(
        '#dataView > div.wrapper.w1000 > div > div.flex.sb.top > div.right_info > div.flex.sb.top > div.title'
    )
    data_descript = soup.select(
      '#dataView > div.wrapper.w1000 > div > div.desc_wrap > div > table > tbody > tr:nth-child(1) > td'
    )
    company = soup.select(
      '#dataView > div.wrapper.w1000 > div > div.flex.sb.top > div.right_info > div.company.flex.fs > div.value'
    )
    price = soup.select(
      '#dataView > div.wrapper.w1000 > div > div.flex.sb.top > div.right_info > div.price.flex.fs > div.value'
    )
    file_list = soup.select(
        '#dataView > div.wrapper.w1000 > div > div.desc_wrap > div > table > tbody > tr:nth-child(2) > td'
    )
    name = data_set_name[0].text.split('] ')
    
    # print(f'[{num}]데이터명 : {name[1]}')
    # print(f'[{num}]데이터설명 : {data_descript[0].text}')
    # print(f'[{num}]제공자 : {company[0].text}')
    # print(f'[{num}]데이터 분류1 : {name[0][1:]}')
    # print(f'[{num}]가격 : {price[0].text}')
    is_free = ''
    if price[0].text == "FREE":
        is_free = "무료"
    else:
        is_free = "유료"
    # print(f'[{num}]유/무료 : {is_free}')
    # print(f'URL : https://kdx.kr/data/view?product_id={num}')
    # for row in file_list:
    #     print(f'파일리스트 : {row.text}')

    capa_list = re.findall(r"\(([A-Za-z0-9_]+)\)", file_list[0].text)
    capa_kb = 0
    capa_mb = 0
    capa_gb = 0
    for item in capa_list:
        if re.search(r"KB", item):
            capa_kb += int(re.match(r"[0-9]+", item)[0])
        if re.search(r"MB", item):
            capa_mb += int(re.match(r"[0-9]+", item)[0])
        if re.search(r"GB", item):
            capa_gb += int(re.match(r"[0-9]+", item)[0])
    # print(capa_kb, capa_mb, capa_gb)
    capa_str = ''
    if capa_gb != 0:
        capa_str += str(capa_gb) + "GB "
    if capa_mb != 0:
        capa_str += str(capa_mb) + "MB "
    if capa_kb != 0:
        capa_str += str(capa_kb) + "KB"

    is_download = "미제공"
    file_name = ['',]
    if re.search(r"[.]csv|[.]zip", file_list[0].text):
        is_download = "제공"
        file_name = re.findall(r"[A-Za-z0-9_]+[.]csv|[A-Za-z0-9_]+[.]zip", file_list[0].text)
        # print(file_name[0])

    
        


    data.append({
        'name': name[1],
        'descript': data_descript[0].text,
        'company': company[0].text,
        'category': name[0][1:],
        'price': price[0].text,
        'url': f'https://kdx.kr/data/view?product_id={num}',
        'capacity': capa_str.rstrip(),
        'is_free': is_free,
        'is_download': is_download,
        'file_name': file_name[0]
    })


driver.close()
# data = json.dumps(data, indent=4)
# print(data)



worksheet.write('A1', '데이터셋명')
worksheet.write('B1', '데이터설명')
worksheet.write('C1', '제공자')
worksheet.write('D1', '데이터 분류1')
worksheet.write('E1', '가격')
worksheet.write('F1', '출처')
worksheet.write('G1', '용량')
worksheet.write('H1', '유료/무료')
worksheet.write('I1', '다운로드 제공여부')
worksheet.write('J1', '파일명')

row = 1
col = 0

for a in (data):
    # print(a)
    worksheet.write(row, col, a.get('name'))
    worksheet.write(row, col + 1, a.get('descript'))
    worksheet.write(row, col + 2, a.get('company'))
    worksheet.write(row, col + 3, a.get('category'))
    worksheet.write(row, col + 4, a.get('price'))
    worksheet.write(row, col + 5, a.get('url'))
    worksheet.write(row, col + 6, a.get('capacity'))
    worksheet.write(row, col + 7, a.get('is_free'))
    worksheet.write(row, col + 8, a.get('is_download'))
    worksheet.write(row, col + 8, a.get('file_name'))
    row += 1


workbook.close()