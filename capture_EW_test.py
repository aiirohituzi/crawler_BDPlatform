from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import config


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
driver = webdriver.Chrome('./chromedriver/chromedriver',chrome_options=options)

driver.set_window_size(1920, 1080) # width , height

driver.get(config.target_login_EW_url)
driver.maximize_window()
time.sleep(1)
driver.find_element_by_name('username').send_keys(config.User_EW_id)
driver.find_element_by_name('password').send_keys(config.User_EW_pw)
driver.find_element_by_xpath('//*[@id="ng-app"]/div/div/div/div[2]/span/form/button').click()
print("로그인 시도 중")
time.sleep(1)
# wait = WebDriverWait(driver, 5)
# wait.until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "#iframe-content"))
# )


driver.get(f'{config.target_sigungu_EW_url}A001')
print(f'[param:A001] 태블로 화면 로딩 중')
# driver.implicitly_wait(10)
time.sleep(5)
# wait = WebDriverWait(driver, 5)
# wait.until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "#centeringContainer"))
# )

print(f'[param:A001] 캡쳐 중')
img_binary = driver.get_screenshot_as_png()
img = Image.open(BytesIO(img_binary))
img = crop_image(img)
img.save(f'./sigungu_EW/A001.png')

# for params in config.gugun_cd:
#     driver.get(f'{config.target_sigungu_EW_url}{params}')
#     print(f'[param:{params}] 태블로 화면 로딩 중')
#     # driver.implicitly_wait(10)
#     time.sleep(10)
#     # wait = WebDriverWait(driver, 5)
#     # wait.until(
#     #     EC.presence_of_element_located((By.CSS_SELECTOR, "#centeringContainer"))
#     # )

#     print(f'[param:{params}] 캡쳐 중')
#     img_binary = driver.get_screenshot_as_png()
#     img = Image.open(BytesIO(img_binary))
#     img = crop_image(img)
#     img.save(f'./nonsan/{params}.png')

    # driver.save_screenshot("screenshot.png")

driver.close()
