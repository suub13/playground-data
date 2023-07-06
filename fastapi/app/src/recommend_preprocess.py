import os
import re
import csv

import pandas as pd

from konlpy.tag import Komoran

from secrets import db_connect


"""
1. get combined_crawling_data by mysql
"""
def get_combined_crawling_data():
    conn = db_connect.connect()
    
    ccd_query = "SELECT * FROM combined_crawling_data"
    
    ccd_df = pd.read_sql(ccd_query, conn)
    
    conn.close()

    return ccd_df


"""
2. skills list 추출해서 set 함수로 중복 제거 - skillset 반환
"""

def extract_skillset():
    skills_list = []
    
    ccd_df = get_combined_crawling_data()
    
    ccd_skills_list = ccd_df['skills'].tolist()
    
    for row in ccd_skills_list:
        # row 리스트의 10번째 값을 가져와 string 을 '' 안의 단어들로 나눠서 리스트로 만들기
        skills = re.findall(r"'(.*?)'", row)
        skills_upper = [word.upper() for word in skills]

        # 나누어진 리스트를 추가
        skills_list += skills_upper

    skillset = set(skills_list)

    return skillset


"""
리스트를 딕셔너리로 변환
"""

def list_to_dict(lst):
    toDict = dict()

    for item in lst:
        toDict[item.upper()] = 0

    return toDict



print(extract_skillset())

