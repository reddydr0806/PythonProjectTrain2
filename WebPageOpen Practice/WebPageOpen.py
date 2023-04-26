from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(3)

username = driver.find_element(By.ID, 'user-name').send_keys('standard_user')
password = driver.find_element(By.ID, 'password').send_keys('secret_sauce')

clickLogin = driver.find_element(By.ID, 'login-button').click()

time.sleep(5)

print(driver.title)

allTags = driver.find_element(By.TAG_NAME, 'a')
print(len(allTags))


