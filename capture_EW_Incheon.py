from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import config_EW_Incheon

# ==================================================
# 대시보드 번호 (0번부터 시작)
# 0 : 01
# 1 : 02
# 2 : 03
# 3 : 04
# 4 : 05
# 5 : 06
# 6 : 07
# 7 : 08
# 8 : 09
# 9 : temp
# 10 : 화성
current_ew_index = 10
# 화면 하나당 로딩 시간 (단위: 초)
capture_delay = 10
# ==================================================

def crop_image(img):
    img_width, img_height = img.size
    crop_dim = (220, 228, 3620, 2028) # left top right bottom
    cropped_img = img.crop(crop_dim)
    return cropped_img

# top: 50px + 37px + 27px = 114
# 3840 * 2160
# 1700 * 900

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("headless")
options.add_argument("lang=ko_KR")
driver = webdriver.Chrome('./chromedriver/chromedriver',chrome_options=options)

driver.set_window_size(1920, 1080) # width , height

driver.get(config_EW_Incheon.target_login_EW_url)
driver.maximize_window()
print("태블로 로그인 페이지에 연결 ...")
time.sleep(1)
driver.find_element_by_name('username').send_keys(config_EW_Incheon.User_EW_id)
driver.find_element_by_name('password').send_keys(config_EW_Incheon.User_EW_pw)
driver.find_element_by_xpath('//*[@id="ng-app"]/div/div/div/div[2]/span/form/button').click()
print("로그인 시도 중")
time.sleep(2)


max_length = 0
if current_ew_index == 0:
    max_length = len(config_EW_Incheon.ew_cd) * len(config_EW_Incheon.field_cd)
if current_ew_index == 1:
    max_length = len(config_EW_Incheon.gugun_cd) * len(config_EW_Incheon.ew_cd) * len(config_EW_Incheon.field_cd)
if current_ew_index == 2:
    max_length = len(config_EW_Incheon.ew_cd) * len(config_EW_Incheon.field_cd)
if current_ew_index == 3:
    max_length = len(config_EW_Incheon.gugun_cd) * len(config_EW_Incheon.ew_cd) * len(config_EW_Incheon.field_cd)
if current_ew_index == 4:
    max_length = len(config_EW_Incheon.year) * len(config_EW_Incheon.month) * len(config_EW_Incheon.ew_cd) * len(config_EW_Incheon.field_cd)
if current_ew_index == 5:
    max_length = len(config_EW_Incheon.year) * len(config_EW_Incheon.month) * len(config_EW_Incheon.gugun_cd) * len(config_EW_Incheon.ew_cd)
if current_ew_index == 6:
    max_length = len(config_EW_Incheon.year) * len(config_EW_Incheon.month) * len(config_EW_Incheon.ew_cd) * len(config_EW_Incheon.field_cd)
if current_ew_index == 7:
    max_length = len(config_EW_Incheon.year) * len(config_EW_Incheon.month) * len(config_EW_Incheon.gugun_cd) * len(config_EW_Incheon.ew_cd)
if current_ew_index == 8:
    max_length = len(config_EW_Incheon.gugun_cd) * len(config_EW_Incheon.field_cd)
if current_ew_index == 9:
    max_length = len(config_EW_Incheon.temp)
if current_ew_index == 10:
    # max_length = len(config_EW_Incheon.ew_cd) * len(config_EW_Incheon.field_cd)
    max_length = len(config_EW_Incheon.ew_cd)
    

idx = 1

if current_ew_index == 0:
    for ew_cd in config_EW_Incheon.ew_cd:
        for field in config_EW_Incheon.field_cd:
            driver.get(f'{config_EW_Incheon.target_view_EW_urls[current_ew_index]}ew_cd={ew_cd}&field_cd={field}')
            print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{ew_cd}-{field}] 태블로 화면 로딩 중')
            time.sleep(capture_delay)

            print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{ew_cd}-{field}] 캡쳐 중')
            img_binary = driver.get_screenshot_as_png()
            img = Image.open(BytesIO(img_binary))
            img = crop_image(img)
            img.save(f'./_EW_/0{current_ew_index + 1}/0{current_ew_index + 2}_EW-{ew_cd}-{field}.png')

            idx += 1

if current_ew_index == 1:
    for gugun in config_EW_Incheon.gugun_cd:
        for ew_cd in config_EW_Incheon.ew_cd:
            for field in config_EW_Incheon.field_cd:
                driver.get(f'{config_EW_Incheon.target_view_EW_urls[current_ew_index]}gugun_cd={gugun}&ew_cd={ew_cd}&field_cd={field}')
                print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{gugun}-{ew_cd}-{field}] 태블로 화면 로딩 중')
                time.sleep(capture_delay)

                print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{gugun}-{ew_cd}-{field}] 캡쳐 중')
                img_binary = driver.get_screenshot_as_png()
                img = Image.open(BytesIO(img_binary))
                img = crop_image(img)
                img.save(f'./_EW_/0{current_ew_index + 1}/0{current_ew_index + 1}_EW-{gugun}-{ew_cd}-{field}.png')

                idx += 1

if current_ew_index == 2:
    for ew_cd in config_EW_Incheon.ew_cd:
        for field in config_EW_Incheon.field_cd:
            driver.get(f'{config_EW_Incheon.target_view_EW_urls[current_ew_index]}ew_cd={ew_cd}&field_cd={field}')
            print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{ew_cd}-{field}] 태블로 화면 로딩 중')
            time.sleep(capture_delay)

            print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{ew_cd}-{field}] 캡쳐 중')
            img_binary = driver.get_screenshot_as_png()
            img = Image.open(BytesIO(img_binary))
            img = crop_image(img)
            img.save(f'./_EW_/0{current_ew_index + 1}/0{current_ew_index + 1}_EW-{ew_cd}-{field}.png')

            idx += 1

if current_ew_index == 3:
    for gugun in config_EW_Incheon.gugun_cd:
        for ew_cd in config_EW_Incheon.ew_cd:
            for field in config_EW_Incheon.field_cd:
                driver.get(f'{config_EW_Incheon.target_view_EW_urls[current_ew_index]}gugun_cd={gugun}&ew_cd={ew_cd}&field_cd={field}')
                print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{gugun}-{ew_cd}-{field}] 태블로 화면 로딩 중')
                time.sleep(capture_delay)

                print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{gugun}-{ew_cd}-{field}] 캡쳐 중')
                img_binary = driver.get_screenshot_as_png()
                img = Image.open(BytesIO(img_binary))
                img = crop_image(img)
                img.save(f'./_EW_/0{current_ew_index + 1}/0{current_ew_index + 1}_EW-{gugun}-{ew_cd}-{field}.png')

                idx += 1

if current_ew_index == 4:
    for year in config_EW_Incheon.year:
        for month in config_EW_Incheon.month:
            for ew_cd in config_EW_Incheon.ew_cd:
                for field in config_EW_Incheon.field_cd:
                    driver.get(f'{config_EW_Incheon.target_view_EW_urls[current_ew_index]}year={year}&month={month}&ew_cd={ew_cd}&field_cd={field}')
                    print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{year}-{month}-{ew_cd}-{field}] 태블로 화면 로딩 중')
                    time.sleep(capture_delay)

                    print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{year}-{month}-{ew_cd}-{field}] 캡쳐 중')
                    img_binary = driver.get_screenshot_as_png()
                    img = Image.open(BytesIO(img_binary))
                    img = crop_image(img)
                    img.save(f'./_EW_/0{current_ew_index + 1}/0{current_ew_index + 1}_EW-{year}-{month}-{ew_cd}-{field}.png')

                    idx += 1

if current_ew_index == 5:
    for year in config_EW_Incheon.year:
        for month in config_EW_Incheon.month:
            for gugun in config_EW_Incheon.gugun_cd:
                for ew_cd in config_EW_Incheon.ew_cd:
                    driver.get(f'{config_EW_Incheon.target_view_EW_urls[current_ew_index]}year={year}&month={month}&gugun_cd={gugun}&ew_cd={ew_cd}')
                    print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{year}-{month}-{gugun}-{ew_cd}] 태블로 화면 로딩 중')
                    time.sleep(capture_delay)

                    print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{year}-{month}-{gugun}-{ew_cd}] 캡쳐 중')
                    img_binary = driver.get_screenshot_as_png()
                    img = Image.open(BytesIO(img_binary))
                    img = crop_image(img)
                    img.save(f'./_EW_/0{current_ew_index + 1}/0{current_ew_index + 1}_EW-{year}-{month}-{gugun}-{ew_cd}.png')

                    idx += 1

if current_ew_index == 6:
    for year in config_EW_Incheon.year:
        for month in config_EW_Incheon.month:
            for ew_cd in config_EW_Incheon.ew_cd:
                for field in config_EW_Incheon.field_cd:
                    driver.get(f'{config_EW_Incheon.target_view_EW_urls[current_ew_index]}year={year}&month={month}&ew_cd={ew_cd}&field_cd={field}')
                    print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{year}-{month}-{ew_cd}-{field}] 태블로 화면 로딩 중')
                    time.sleep(capture_delay)

                    print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{year}-{month}-{ew_cd}-{field}] 캡쳐 중')
                    img_binary = driver.get_screenshot_as_png()
                    img = Image.open(BytesIO(img_binary))
                    img = crop_image(img)
                    img.save(f'./_EW_/0{current_ew_index + 1}/0{current_ew_index + 1}_EW-{year}-{month}-{ew_cd}-{field}.png')

                    idx += 1

if current_ew_index == 7:
    for year in config_EW_Incheon.year:
        for month in config_EW_Incheon.month:
            for gugun in config_EW_Incheon.gugun_cd:
                for ew_cd in config_EW_Incheon.ew_cd:
                    driver.get(f'{config_EW_Incheon.target_view_EW_urls[current_ew_index]}year={year}&month={month}&gugun_cd={gugun}&ew_cd={ew_cd}')
                    print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{year}-{month}-{gugun}-{ew_cd}] 태블로 화면 로딩 중')
                    time.sleep(capture_delay)

                    print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{year}-{month}-{gugun}-{ew_cd}] 캡쳐 중')
                    img_binary = driver.get_screenshot_as_png()
                    img = Image.open(BytesIO(img_binary))
                    img = crop_image(img)
                    img.save(f'./_EW_/0{current_ew_index + 1}/0{current_ew_index + 1}_EW-{year}-{month}-{gugun}-{ew_cd}.png')

                    idx += 1

if current_ew_index == 8:
    for gugun in config_EW_Incheon.gugun_cd:
        for field in config_EW_Incheon.field_cd:
            driver.get(f'{config_EW_Incheon.target_view_EW_urls[current_ew_index]}gugun_cd={gugun}&field_cd={field}')
            print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{gugun}-{field}] 태블로 화면 로딩 중')
            time.sleep(capture_delay)

            print(f'({idx}/{max_length}) [param:0{current_ew_index + 1}-{gugun}-{field}] 캡쳐 중')
            img_binary = driver.get_screenshot_as_png()
            img = Image.open(BytesIO(img_binary))
            img = crop_image(img)
            img.save(f'./_EW_/0{current_ew_index + 1}/0{current_ew_index + 1}_EW-{gugun}-{field}.png')

            idx += 1

if current_ew_index == 9:
    for temp in config_EW_Incheon.temp:
        driver.get(f'{config_EW_Incheon.target_view_EW_urls[current_ew_index]}{temp}')

        str_temp = (temp.split('?')[1]).split('&')
        name = ''
        for item in str_temp:
            name += '-' + item.split('=')[1]
            
        print(f"({idx}/{max_length}) [param:{temp.split('?')[0]}{name}] 태블로 화면 로딩 중")
        time.sleep(capture_delay)

        print(f"({idx}/{max_length}) [param:{temp.split('?')[0]}{name}] 캡쳐 중")
        img_binary = driver.get_screenshot_as_png()
        img = Image.open(BytesIO(img_binary))
        img = crop_image(img)
        img.save(f"./_EW_/{(temp.split('?')[0]).split('_')[0]}/{temp.split('?')[0]}{name}.png")
        # img.save(f"./_EW_/hwaseong/{(temp.split('?')[0]).split('_')[0]}/{temp.split('?')[0]}{name}.png")

        idx += 1

if current_ew_index == 10:          # 화성 분기 크롤링
    for ew_cd in config_EW_Incheon.ew_cd:
        # for field in config_EW_Incheon.field_cd:
            # driver.get(f'{config_EW_Incheon.target_view_EW_urls[current_ew_index]}ew_cd={ew_cd}&field_cd={field}')
        driver.get(f'{config_EW_Incheon.target_view_EW_urls[current_ew_index]}ew_cd={ew_cd}')
        
        # print(f'({idx}/{max_length}) [param:02-{ew_cd}-{field}] 태블로 화면 로딩 중')
        # print(f'({idx}/{max_length}) [param:04-{ew_cd}-{field}] 태블로 화면 로딩 중')
        # print(f'({idx}/{max_length}) [param:05-{ew_cd}] 태블로 화면 로딩 중')
        print(f'({idx}/{max_length}) [param:06-{ew_cd}] 태블로 화면 로딩 중')

        time.sleep(capture_delay)

        # print(f'({idx}/{max_length}) [param:02-{ew_cd}-{field}] 캡쳐 중')
        # print(f'({idx}/{max_length}) [param:04-{ew_cd}-{field}] 캡쳐 중')
        # print(f'({idx}/{max_length}) [param:05-{ew_cd}] 캡쳐 중')
        print(f'({idx}/{max_length}) [param:06-{ew_cd}] 캡쳐 중')

        img_binary = driver.get_screenshot_as_png()
        img = Image.open(BytesIO(img_binary))
        img = crop_image(img)

        # img.save(f'./_EW_/hwaseong/02/02_EW-{ew_cd}-{field}.png')
        # img.save(f'./_EW_/hwaseong/04/04_EW-{ew_cd}-{field}.png')
        # img.save(f'./_EW_/hwaseong/05/05_EW-{ew_cd}.png')
        img.save(f'./_EW_/hwaseong/06/06_EW-{ew_cd}.png')

        idx += 1
driver.close()
