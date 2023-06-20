import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time
import re
from tqdm import tqdm

def get_url_list():
    with open("../data/job_fix_list.csv", encoding='cp949') as f:
        urls = f.readlines()

    url_list = [url.rstrip("\n") for url in urls]
    
    return url_list

def get_job_description(driver, url):
    
    response = requests.get(url)
    
    if response.status_code == 200:
        # url 접속하기
        driver.get(url)

        # 화면 비율을 축소해서 모든 데이터 보이게 만들기
        driver.execute_script("document.body.style.zoom='10%'")

        time.sleep(5)

        # Job Description 을 담을 딕셔너리 생성
        res = {}

        # url 에서 index 값 추출
        res['id'] = url.split("/")[-1]

        # JobHeader 클래스 가져와서 title, company, tags 추출
        job_header = driver.find_element(By.CLASS_NAME, 'JobHeader_className__HttDA')
        title = job_header.find_element(By.TAG_NAME, 'h2')
        company = job_header.find_element(By.TAG_NAME, 'a')
        location = job_header.find_element(By.CLASS_NAME, 'JobHeader_pcLocationContainer__xRwIv')
        tags = job_header.find_element(By.CLASS_NAME, 'Tags_tagsClass__mvehZ')

        # res 딕셔너리에 저장
        res['title'] = title.text
        res['company'] = company.text
        res['location'] = location.text.split(".")

        # Tag 리스트 가져와서 저장
        tag_list = list(map(str, tags.text.split('#')))
        tag_list = tag_list[1:]
        res['tags'] = tag_list

        # JobDescription 클래스 가져와서 header, contents 추출
        jd = driver.find_element(By.CLASS_NAME, 'JobDescription_JobDescription__VWfcb')
        jd_header = jd.find_elements(By.TAG_NAME, 'h6')
        jd_contents = jd.find_elements(By.TAG_NAME, 'p')

        for i in range(1, len(jd_header)+1):
            title = jd_header[i-1].text
            content = jd_contents[i].text.split("\n")

            if title == '자격요건':
                res['qualifications'] = content
            elif title == '우대사항':
                res['preferred'] = content
            elif title == '혜택 및 복지':
                res["benefits"] = content
            elif title == '기술스택 ・ 툴':
                res["skills"] = content


        jwp = driver.find_element(By.CLASS_NAME, "JobWorkPlace_className__ra6rp")
        jwp_bodies = jwp.find_elements(By.CLASS_NAME, 'body')

        if len(jwp_bodies) < 2:
            workplace = ""
        else:
            workplace = jwp_bodies[1].text
        
        res['workplace'] = workplace
    else:
        print("존재하지 않는 페이지 입니다.")
    
    return res


chrome_driver_path = "/Users/jhnam/Downloads/chromedriver_mac64/chromedriver"
options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(executable_path = chrome_driver_path, chrome_options = options)

# url 가져오기
url_list = get_url_list()

total = []

for i in tqdm(range(500)):
    res = get_job_description(driver, url_list[i])
    
    if len(res) == 0:
        print("존재하지 않는 페이지 입니다.")
        continue
    else:
        total.append(res)

driver.quit()