import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 장치 오류가 발생하는 경우가 있어 아래 옵션을 추가함
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()

driver.implicitly_wait(3)
driver.get("https://www.kumoh.ac.kr/_common/login/login.do?Return_Url=https://onestop.kumoh.ac.kr")

driver.implicitly_wait(2)
# 보안상의 이유로 아이디와 비밀번호를 코드에서 삭제함
driver.find_element(By.XPATH, '/html/body/div/section/div/div/div/div[1]/form/fieldset/div/div[1]/input').send_keys('20191203')
driver.find_element(By.XPATH, '/html/body/div/section/div/div/div/div[1]/form/fieldset/div/div[2]/input').send_keys('!Spider0826')

driver.implicitly_wait(1)
driver.find_element(By.XPATH, '/html/body/div/section/div/div/div/div[1]/form/fieldset/div/input').click()

time.sleep(15)
driver.switch_to.default_content()
driver.switch_to.frame("LeftFrame")

time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div[3]/div[1]/div/table/tbody/tr[4]/td[2]').click()

time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div[3]/div[1]/div/table/tbody/tr[14]/td[3]').click()

time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div[3]/div[1]/div/table/tbody/tr[19]/td[4]').click()
driver.switch_to.default_content()
driver.switch_to.frame("w_cre_s9241")

time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div[2]/div[6]/table/tbody/tr/td[1]').click()

time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div[2]/div[6]/table/tbody/tr/td[2]/div/input').click()
time.sleep(2)