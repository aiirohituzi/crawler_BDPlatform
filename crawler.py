from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import xlsxwriter
import config
import config_request

workbook = xlsxwriter.Workbook('request.xlsx')
worksheet = workbook.add_worksheet()

chrome_options = Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome('./chromedriver/chromedriver', chrome_options=chrome_options)

data = []

#==================================Quest==================================================================
# for num in config.QUESTNUM_G:
#     print(num)
#     driver.get('http://wiki.mhxg.org/ida/' + num + '.html')
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')

#     # questName = soup.select(
#     #     '#quest' + num + ' > div > div.panel-heading > a:nth-of-type(2)'
#     # )
    
#     # questMap = soup.select(
#     #     '#quest' + num + ' > div > div.panel-body.view_panel_body.a_cl21913' + str(i) + ' > a'
#     # )

#     questName = soup.select(
#         '#id' + num + ' > td'
#     )

#     rating = soup.select(
#         '#main_1 > div > div.row_x > div.col-md-10 > h3'
#     )

#     questMap = soup.select(
#         '#main_1 > div > div.row_x > div.col-md-10 > table:nth-of-type(2) > tbody > tr:nth-of-type(1) > td:nth-of-type(2) > a'
#     )

#     questTime = soup.select(
#         '#main_1 > div > div.row_x > div.col-md-10 > table:nth-of-type(2) > tbody > tr:nth-of-type(1) > td:nth-of-type(3)'
#     )

#     condition_main = soup.select(
#         '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(1) > td:nth-of-type(1)'
#     )

#     condition_sub = soup.select(
#         '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(1) > td:nth-of-type(2)'
#     )

#     down_payment = soup.select(
#         '#main_1 > div > div.row_x > div.col-md-10 > table:nth-of-type(2) > tbody > tr:nth-of-type(2) > td:nth-of-type(3)'
#     )

#     rewardMoney_main = soup.select(
#         '#main_1 > div > div.row_x > div.col-md-10 > table:nth-of-type(2) > tbody > tr:nth-of-type(2) > td:nth-of-type(1)'
#     )

#     rewardMoney_sub = soup.select(
#         '#main_1 > div > div.row_x > div.col-md-10 > table:nth-of-type(2) > tbody > tr:nth-of-type(2) > td:nth-of-type(2)'
#     )

#     # print(questName)
#     # print(questMap)
#     # print(questTime)
#     # print(condition_main)
#     # print(condition_sub)
#     # print(down_payment)
#     # print(rewardMoney_main)
#     # print(rewardMoney_sub)
#     # print('--------------')

#     data.append({
#         'questName': questName[0].text.replace("\n", "").rstrip().lstrip(),
#         'rating': rating[0].text.replace(questName[0].text.replace("\n", "").rstrip().lstrip(), ""),
#         'questMap' : questMap[0].text,
#         'questTime' : questTime[0].text,
#         'condition_main' : condition_main[0].text,
#         'condition_sub' : condition_sub[0].text,
#         'down_payment' : down_payment[0].text,
#         'rewardMoney_main' : rewardMoney_main[0].text,
#         'rewardMoney_sub' : rewardMoney_sub[0].text,
#     })
#=======================================================================================================================



#=======================================Kariwaza========================================================================
# temp_category = ''
# temp_name = ''
# # config.KARIWAZA_NUM.sort()
# for num in config.KARIWAZA_NUM:
#     print(num)
#     driver.get('http://wiki.mhxg.org/data/1847.html')
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')

#     if num in config.KARIWAZA_NUM_HEAD:
#         category = soup.select(
#             '#id' + num + ' > td:nth-of-type(1)'
#         )
#         temp_category = category[0].text.replace("\n", "").rstrip().lstrip()

#         kariwazaName = soup.select(
#             '#id' + num + ' > td:nth-of-type(2)'
#         )
#         temp_name = kariwazaName[0].text.replace("\n", "").rstrip().lstrip()

#         level = soup.select(
#             '#id' + num + ' > td.c_g.b'
#         )
        
#         condition = soup.select(
#             '#id' + num + ' > td:nth-of-type(4)'
#         )
#     else:
#         if num in config.KARIWAZA_NUM_LV1:
#             kariwazaName = soup.select(
#                 '#id' + num + ' > td:nth-of-type(1)'
#             )
#             temp_name = kariwazaName[0].text.replace("\n", "").rstrip().lstrip()

#             level = soup.select(
#                 '#id' + num + ' > td.c_g.b'
#             )
            
#             condition = soup.select(
#                 '#id' + num + ' > td:nth-of-type(3)'
#             )
#         else:
#             level = soup.select(
#                 '#id' + num + ' > td.c_g.b'
#             )
            
#             condition = soup.select(
#                 '#id' + num + ' > td:nth-of-type(2)'
#             )


#     print('category : ' + temp_category)
#     print('name : ' + temp_name)
#     print('lv : ' + level[0].text.replace("\n", "").rstrip().lstrip())
#     print('con : ' + condition[0].text)

#     data.append({
#         'category': temp_category,
#         'kariwazaName': temp_name,
#         'level': level[0].text.replace("\n", "").rstrip().lstrip(),
#         'condition' : condition[0].text,
#     })
#=============================================================================================================

#=================================================Request=====================================================
for num in config_request.REQUEST_NUM:
    print(num)
    driver.get('http://wiki.mhxg.org/data/2824.html')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    requestName = soup.select(
        '#id' + num + ' > td.b > a'
    )

    condition = soup.select(
        '#id' + num + ' > td:nth-of-type(2)'
        #id313290 > td:nth-child(2)
    )

    reward = soup.select(
        '#id' + num + ' > td:nth-of-type(3)'
    )

    print('requestName : ' + requestName[0].text)
    print('condition : ' + condition[0].text.rstrip().lstrip())
    print('reward : ' + reward[0].text.rstrip().lstrip())

    data.append({
        'requestName': requestName[0].text,
        'condition': condition[0].text.rstrip().lstrip(),
        'reward': reward[0].text.rstrip().lstrip(),
    })
#=============================================================================================================



driver.close()
# data = json.dumps(data, indent=4)
# print(data)



# f = open("data.txt", 'w', encoding='utf8')

# for q in data:
#     print(q.get('questName'))
#     print(q.get('questMap'))
#     f.write(q.get('questName') + ' / ' + q.get('questMap') + '\n')
# f.close()


# worksheet.write('A1', 'questName')
# worksheet.write('B1', 'rating')
# worksheet.write('C1', 'questMap')
# worksheet.write('D1', 'questTime')
# worksheet.write('E1', 'condition_main')
# worksheet.write('F1', 'condition_sub')
# worksheet.write('G1', 'down_payment')
# worksheet.write('H1', 'rewardMoney_main')
# worksheet.write('I1', 'rewardMoney_sub')

# row = 1
# col = 0

# for a in (data):
#     worksheet.write(row, col, a.get('questName'))
#     worksheet.write(row, col + 1, a.get('rating'))
#     worksheet.write(row, col + 2, a.get('questMap'))
#     worksheet.write(row, col + 3, a.get('questTime'))
#     worksheet.write(row, col + 4, a.get('condition_main'))
#     worksheet.write(row, col + 5, a.get('condition_sub'))
#     worksheet.write(row, col + 6, a.get('down_payment'))
#     worksheet.write(row, col + 7, a.get('rewardMoney_main'))
#     worksheet.write(row, col + 8, a.get('rewardMoney_sub'))
#     row += 1



# worksheet.write('A1', 'category')
# worksheet.write('B1', 'kariwazaName')
# worksheet.write('C1', 'level')
# worksheet.write('D1', 'condition')

# row = 1
# col = 0

# for a in (data):
#     print(a)
#     worksheet.write(row, col, a.get('category'))
#     worksheet.write(row, col + 1, a.get('kariwazaName'))
#     worksheet.write(row, col + 2, a.get('level'))
#     worksheet.write(row, col + 3, a.get('condition'))
#     row += 1



worksheet.write('A1', 'requestName')
worksheet.write('B1', 'condition')
worksheet.write('C1', 'reward')

row = 1
col = 0

for a in (data):
    print(a)
    worksheet.write(row, col, a.get('requestName'))
    worksheet.write(row, col + 1, a.get('condition'))
    worksheet.write(row, col + 2, a.get('reward'))
    row += 1



workbook.close()