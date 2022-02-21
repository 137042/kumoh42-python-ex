import os
import pandas as pd
import pymysql as db
import numpy as np
from datetime import datetime

# 파일 불러오기에 실패하여 절대 경로로 지정했으나, 이전처럼 최신 파일을 대조하여 불러오는 것이 바람직함
raw = pd.read_excel('C:/Users/mare1/Downloads/excel.xlsx')

df = raw[['교과목 종류', '교육과정명', '이수 대상 학년', '이수 구분', '교과목명', '학점', '교과목코드', '담당교수', '수강학과', '강의시간(강의실)', '제한 인원', '수강 인원','수강 꾸러미']]
df.rename(columns = {'교과목 종류' : '교과목_종류', '이수 대상 학년' : '이수_대상_학년', '이수 구분' : '이수_구분', '교과목코드' : '개설교과목코드', '강의시간(강의실)' : '강의시간강의실', '제한 인원' : '제한_인원', '수강 인원' : '수강_인원','수강 꾸러미' : '수강_꾸러미'}, inplace = True)

year_list = []    # 빈 리스트 생성
semester_list = []    # 빈 리스트 생성

year = datetime.today().year

if datetime.today().month > 6:
    semester = "2"
else:
    semester = "1"

for i in range(df.size):
    year_list.append(year)
    semester_list.append(semester)

df['년도'] = pd.Series(year_list)

df['학기'] = pd.Series(semester_list)

df = df.replace(np.nan, '', regex=True)

print(df)

# db명과 table명은 대소문자를 구분함
# 보안상의 이유로 유저, 비밀번호, 호스트를 코드에서 삭제함
con = db.connect(
    user='', 
    passwd='', 
    host='', 
    db='xe_home', 
    charset='utf8'
    )

# 금오사이 어플 내 시간표에 정보를 제공하는 db와 table은 각각 xe_home, xe_kumohtime임
sql = 'INSERT INTO xe_kumohtime (교과목_종류,교육과정명,이수_대상_학년,이수_구분,교과목명,학점,개설교과목코드,담당교수,수강학과,강의시간강의실,제한_인원,수강_인원,수강_꾸러미,년도,학기) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

curs = con.cursor(db.cursors.DictCursor)
for i in df.index:
    print(df["교과목_종류"][i])
    curs.execute(sql, (df["교과목_종류"][i], df["교육과정명"][i], df["이수_대상_학년"][i], df["이수_구분"][i], df["교과목명"][i], df["학점"][i], df["개설교과목코드"][i], df["담당교수"][i], df["수강학과"][i], df["강의시간강의실"][i], df["제한_인원"][i], df["수강_인원"][i], df["수강_꾸러미"][i], df["년도"][i], df["학기"][i]))

con.commit()
con.close()
