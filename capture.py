from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import config

# 지역 변경 시 이 변수만 url 맞춰서 수정
# id, pw 값은 별개로 config.py 들어가서 일일히 직접 수정해주어야 함
# 논산, 광명, 금산은 메뉴항목이 다르므로 우선순위 나중에
# local 명칭으로 폴더 하나 만들어 줘야 함
local = 'daegu'
menu_param_arr = config.sido_menu_param


def crop_image(img):
    img_width, img_height = img.size
    crop_dim = (395, 230, 3785, 2035) # left top right bottom
    cropped_img = img.crop(crop_dim)
    return cropped_img


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("headless")
driver = webdriver.Chrome('./chromedriver/chromedriver',chrome_options=options)

driver.set_window_size(1920, 1080) # width , height

driver.get(f'{config.target_login_url}{local}/')
driver.maximize_window()
driver.find_element_by_xpath('/html/body/div/a[1]/img').click()
driver.find_element_by_name('userId').send_keys(config.User_id)
driver.find_element_by_name('password').send_keys(config.User_pw)
driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
print(f"{config.target_login_url}{local}에 로그인 시도 중")
# driver.implicitly_wait(5)

wait = WebDriverWait(driver, 5)
wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#iframe-content"))
)


max_length = len(menu_param_arr)

# for params in config.nonsan_menu_param:
# for params in config.gwangmyeong_menu_param:
# for params in config.geumsan_menu_param:
# for idx, params in enumerate(config.temp_param, 1):
# for params in config.gugun_menu_param:
# for params in config.research_menu_param:
# for params in config.sido_menu_param:
# for params in config.korea_menu_param:
# for idx, params in enumerate(config.sido_menu_param, 1):
for idx, params in enumerate(menu_param_arr, 1):
    driver.get(f'{config.target_login_url}{local}{config.target_menu_url}{params}')
    print(f'({idx}/{max_length}) [param:{params}] 태블로 화면 로딩 중')
    # driver.implicitly_wait(10)
    time.sleep(15)
    # wait = WebDriverWait(driver, 5)
    # wait.until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "#centeringContainer"))
    # )

    print(f'({idx}/{max_length}) [param:{params}] 캡쳐 중')
    img_binary = driver.get_screenshot_as_png()
    img = Image.open(BytesIO(img_binary))
    img = crop_image(img)
    img.save(f'./img/{local}/{params}.png')

    # driver.save_screenshot("screenshot.png")

driver.close()
