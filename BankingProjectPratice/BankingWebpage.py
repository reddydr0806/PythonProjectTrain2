from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
driver.maximize_window()
time.sleep(3)

CustomerLogin = driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-lg']").click()
time.sleep(2)

your_name = driver.find_element(By.ID, 'userSelect')
select_name = Select(your_name)
select_name.select_by_value('2')
# for x in your_name:
#     print(x.text)

click_submit = driver.find_element(By.XPATH, "//button[@type='submit']").click()

org_list = driver.find_element(By.XPATH, "//select[@name = 'accountSelect']")
org_select = Select(org_list)
org_select.select_by_visible_text('1005')

click_deposit = driver.find_element(By.XPATH, "//button[@ng-click='deposit()']").click()
enter_depositamount = driver.find_element(By.XPATH, "//input[@ng-model='amount']").send_keys('5000')

deposit_amount = driver.find_element(By.XPATH, "//button[@type='submit']").click()

success_message = driver.find_element(By.XPATH, "//span[@ng-show='message']")
assert success_message.text == 'Deposit Successful'
print(success_message.text)
time.sleep(4)
Account_check = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/strong[1]')
assert Account_check.text == '1005'
print('Account Number is matching with Account selected')

Balance_Check = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/strong[2]")
print("Your current Account balance is :", Balance_Check.text)

click_withdraw = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[3]/button[3]").click()
time.sleep(2)
enter_withdrawamount = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[4]/div/form/div/input").send_keys('2000')

withdraw_amount = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[4]/div/form/button").click()

withdraw_message = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[4]/div/span")
# assert withdraw_message.text == 'Transaction successful'
print("Withdrawl status :", withdraw_message.text)

if withdraw_message.text == 'Transaction successful':
    print("Withdrawl was success")
else:
    print('Please enter the lower amount')

#Chekc the Updated balance after withdrawl
updated_balance = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/strong[2]")
print("New updated Balance of your account is :",  updated_balance.text)

# Project Automation Closure
print("Practice project successfully closed")

time.sleep(3)

driver.quit()