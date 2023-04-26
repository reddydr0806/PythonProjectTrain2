from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(3)
#
# username = driver.find_element(By.ID, 'user-name').send_keys('standard_user')
# password = driver.find_element(By.ID, 'password').send_keys('secret_sauce')
#
# clickLogin = driver.find_element(By.ID, 'login-button').click()
#
# time.sleep(5)
LinkList = driver.find_elements(By.TAG_NAME, 'a')
print(len(LinkList))

for x in LinkList:
    Link_text = x.text
    print(Link_text)
    print(x.get_attribute('href'))


ImgList = driver.find_elements(By.TAG_NAME, 'img')
print(len(ImgList))

for y in ImgList:
    Imgtext = y.text
    print(Imgtext)
    print(y.get_attribute('src'))

