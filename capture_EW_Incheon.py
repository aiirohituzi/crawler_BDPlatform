from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import config_EW_Incheon


def crop_image(img):
    img_width, img_height = img.size
    crop_dim = (220, 228, 3620, 2028) # left top right bottom
    cropped_img = img.crop(crop_dim)
    return cropped_img

# top: 50px + 37px + 27px = 114
# 3840 * 2160
# 1700 * 900

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# options.add_argument("headless")
# driver = webdriver.Chrome('./chromedriver/chromedriver',chrome_options=options)

# driver.set_window_size(1920, 1080) # width , height

# driver.get(config_EW.target_login_EW_url)
# driver.maximize_window()
# print("태블로 로그인 페이지에 연결 ...")
# time.sleep(1)
# driver.find_element_by_name('username').send_keys(config_EW.User_EW_id)
# driver.find_element_by_name('password').send_keys(config_EW.User_EW_pw)
# driver.find_element_by_xpath('//*[@id="ng-app"]/div/div/div/div[2]/span/form/button').click()
# print("로그인 시도 중")
# time.sleep(2)

# max_length = len(config_EW.gugun_cd) * len(config_EW.size_cd) * len(config_EW.field_cd)
# idx = 1

print(config_EW_Incheon.get_params(0))
# for num in config_EW_Incheon.param_info:
#     print(len(num))

# for gugun in config_EW.gugun_cd:
#     for size in config_EW.size_cd:
#         for field in config_EW.field_cd:
#             driver.get(f'{config_EW.target_view_EW_urls}gugun_cd={gugun}&size_cd={size}&field_cd={field}')
#             print(f'({idx}/{max_length}) [param:{gugun}-{size}-{field}] 태블로 화면 로딩 중')
#             time.sleep(15)

#             print(f'({idx}/{max_length}) [param:{gugun}-{size}-{field}] 캡쳐 중')
#             img_binary = driver.get_screenshot_as_png()
#             img = Image.open(BytesIO(img_binary))
#             img = crop_image(img)
#             img.save(f'./EW_V2_/{gugun}-{size}-{field}.png')

#             idx += 1

# driver.close()
