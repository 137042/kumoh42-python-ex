import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from datetime import datetime

# 장치 오류가 발생하는 경우가 있어 아래 옵션을 추가함
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(3)
driver.get("https://www.kumoh.ac.kr/ko/schedule.do?mode=list")
html = driver.page_source
soup = bs(html, "html.parser")

driver.implicitly_wait(7)
items = soup.find_all("tr")

scheduleList = []
year = datetime.today().year

def getDates(start_date, end_date, year1, year2):
    start_date = str(year1) + "-" + start_date.replace(".","-")
    end_date = str(year2) + "-" + end_date.replace(".","-")

for item in items:
    try:
        dates = item.findAll("td")

        # len(dates)는 dates안에 담겨있는 연도를 가져오기 위하여 사용(3인 경우와 2인 경우를 구분할 때 사용)
        start_date, end_date = dates[len(dates) - 2].get_text().split(" ~ ")

        endYear = year
        if start_date.split(".")[0] == "12" and end_date.split(".")[0] == "01":
            endYear = year + 1

        getDates(start_date, end_date, year, endYear)
        title = dates[len(dates) - 1].get_text()
        
        schedule = (start_date, end_date, title)
        scheduleList.append(schedule)

    except:
        print("")

# db part
import pymysql as db

con = db.connect(
    user='xe_master',
    passwd='Wjd3TkaTj##',
    host='db-2vphn.pub-cdb.ntruss.com',
    port=3306,
    db='xe_home')

sql = 'INSERT INTO xe_application_schedule (start_date, end_date, title) VALUES(%s, %s, %s)'

val:str
val = str(year) + "-" + str(year) + "-"

for schedule in scheduleList:
    if val not in schedule[0]:
        with con.cursor() as cursor:
            try:
                cursor.execute(sql, schedule)
                print(schedule)
            except Exception as e:
                print(e)

con.commit()
con.close()