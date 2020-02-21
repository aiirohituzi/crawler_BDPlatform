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
    crop_dim = (395, 230, 3440+345, 1915+120) # left top right bottom
    cropped_img = img.crop(crop_dim)
    return cropped_img

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("headless")
driver = webdriver.Chrome('./chromedriver/chromedriver',chrome_options=options)

driver.set_window_size(1920, 1080) # width , height




driver.get(config.target_login_url)
driver.maximize_window()
driver.find_element_by_xpath('/html/body/div/a[1]/img').click()
driver.find_element_by_name('userId').send_keys(config.User_id)
driver.find_element_by_name('password').send_keys(config.User_pw)
driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
print("로그인 시도 중")
# driver.implicitly_wait(5)

wait = WebDriverWait(driver, 5)
wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#iframe-content"))
)

driver.get(f'{config.target_menu_url}{config.nonsan_menu_param[0]}')
print("태블로 화면 로딩 중")
# driver.implicitly_wait(10)
time.sleep(5)
# wait = WebDriverWait(driver, 5)
# wait.until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "#centeringContainer"))
# )

print("캡쳐 중")
img_binary = driver.get_screenshot_as_png()
img = Image.open(BytesIO(img_binary))
img = crop_image(img)
img.save("screenshot.png")

# driver.save_screenshot("screenshot.png")

driver.close()
