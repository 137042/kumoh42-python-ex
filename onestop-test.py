import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


#드라이버 초기화
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(3)

driver.get("https://www.kumoh.ac.kr/_common/login/login.do?Return_Url=https://onestop.kumoh.ac.kr")

driver.implicitly_wait(2)

# 원스톱 로그인
driver.find_element_by_name("member_id").send_keys("20191203")
driver.find_element_by_name("member_pw").send_keys("!Spider0826")
driver.find_element_by_xpath("//input[@title='로그인']").click()
time.sleep(20)


# find the frame
wait.until(EC.element_to_be_clickable((By.ID, "wysiwygTextarea_ifr")))
frame2 = driver.find_element(By.XPATH, "//iframe[@id='wysiwygTextarea_ifr']");

# switch to frame by frame element
driver.switch_to.frame(frame2);


# 좌측 메뉴 프레임 전환
driver.switch_to_frame("LeftFrame")
time.sleep(5)
# 학사관리
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div[1]/div/table/tbody/tr[4]/td[2]').click()
time.sleep(5)
# 수강신청
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div[1]/div/table/tbody/tr[14]/td[3]').click()
time.sleep(5)
# 개설강좌 조회
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div[1]/div/table/tbody/tr[19]/td[4]').click()
time.sleep(5)

# 기본 프레임 전환
driver.switch_to.default_content()
time.sleep(5)
# 우측 메인 프레임 전환
driver.switch_to_frame("w_cre_s9241")
time.sleep(5)
# 조회 버튼 클릭
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[6]/table/tbody/tr/td[1]').click()

time.sleep(5)

# 엑셀 다운로드 클릭
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[6]/table/tbody/tr/td[2]').click()

time.sleep(5)

# 종료
driver.close()