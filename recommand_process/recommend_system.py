# import library
import re
import csv
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
# from tqdm import tqdm

def get_skills_list():
    # 이 부분을 database에서 가져오게 바꿔야 함
    with open("C:/codes/playground-data/recommand_process/data/combined_crawling_data.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        
        # 태그 하나씩 쪼개서 넣을 리스트 (set으로 중복 제거 전 데이터)
        skills_list = []

        # csv 파일 리더로, 한 row씩 읽기
        for row in reader:
            # row list의 10번째 element인 tags string을 ''안 단어들로 나눠서 list만들기
            skills = re.findall(r"'(.*?)'", row[10])
            skills_upper = [word.upper() for word in skills]
            
            # 각 줄의 태그를 skill_list 에 넣는다.
            skills_list += skills_upper
        
        skills_set = set(skills_list)
        
        return skills_set

# 스킬셋 그룹화를 위한 전처리
skill_mapping = {
    'AWS': ['AWS', 'AMAZON WEB SERVICE'],
    'REACT': ['REACT', 'REACT.JS', 'REACT NATIVE'],
    'GIT': ['GIT', 'GITHUB', 'GITLAB'],
    'VUE': ['VUE', 'VUEJS', 'VUE.JS'],
    'EMBEDDED': ['임베디드 시스템', '임베디드 소프트웨어', 'EMBEDDED C', 'EMBEDDED LINUX', 'WINDOWS EMBEDDED'],
    'RESTFUL': ['RESTFUL', 'REST', 'RESTFUL API', 'RESTFUL WEBSERVICES', 'RESTFUL ARCHITECTURE'],
    'RTL': ['RTL', 'RTL 설계', 'RTL 코딩', 'RTL 검증'],
    'SAP': ['SAP BW', 'SAP 포털', 'SAP MM', 'SAP FICO', 'SAP ERP', 'SAP BI', 'SAP 구현', 'SAP HR', 'SAP', 'SAP FI', 'SAP SD', 'ERP 구현', 'ERP 소프트웨어'],
    'INFRA': ['인프라'],
    '보안': ['보안', '네트워크 보안', '정보 보안', '보안 정책', '보안 관리', '보안 감사', '보안 교육', '보안 금융', '보안 운영', '클라우드 보안', '취약점 스캐닝'],
    'ORACLE': ['ORACLE', 'ORACLE SQL', 'ORACLE DATABASE', 'ORACLE RAC'],
    'GCP': ['GCP', 'GOOGLE CLOUD PLATFORM'],
    '데이터베이스': ['데이터베이스', 'CRM 데이터베이스', '데이터베이스 관리'],
    'C/C++': ['C / C++', 'C', 'C++'],
    'GO': ['GO', 'GOLANG'],
    'JQEURY': ['JQUERY', 'JQUERY UI'],
    'MSSQL': ['MSSQL', 'SQL 서버', 'MICROSOFT SERVER', 'SSRS'],
    'ML': ['ML', '기계 학습 (MACHINE LEARNING)'],
    'SPARK': ['SPARK', 'APACHE SPARK'],
    '3D': ['3D', '3D 모델링', '3D 그래픽'],
    'JSP': ['JSP', 'JSP 개발'],
    'SHELL': ['SHELL', 'SHELL SCRIPTING'],
    'AGILE': ['AGILE', '애자일 방법론', '애자일 프로젝트 관리'],
    'UX': ['UX', 'UX 기획', 'UX 디자인'],
    'WPF': ['WPF', 'WPF 개발'],
    'APACHE': ['APACHE', 'APACHE 2'],
    '.NET': ['.NET', '.NET CORE', 'VB .NET'],
    '소켓': ['소켓', 'WEB SOCKET'],
    'FPGA': ['FPGA', 'FPGA 프로토 타이핑'],
    'KOTLIN': ['KOTLIN', 'COROUTINE'],
    '네트워크': ['네트워크 관리', '네트워크 보안', '네트워크 설계', '네트워크 엔지니어링', '네트워크 운영', '네트워크 인프라', '네트워크 통신', '네트워크 프로그래밍'],
    'LINUX': ['LINUX', '리눅스', '리눅스 커널', '리눅스 시스템 관리', '리눅스 서버'],
    '로봇': ['로봇', '로봇 프로그래밍'],
    '모바일 게임': ['모바일 게임', '모바일 게임 개발'],
    '컴퓨터 비전': ['컴퓨터 비전', '머신 비전'],
    '클라우드 컴퓨팅': ['클라우드 컴퓨팅', '클라우드 응용 프로그램', '클라우드 스토리지', 'HEROKU'],
    'ASP': ['ASP', 'ASP .NET'],
    'CAD': ['CAD', 'AUTOCAD'],
    'CRM': ['CRM', 'CRM 데이터베이스', 'CRM 소프트웨어', 'CRM 통합'],
    'CSS': ['CSS', 'CSS3', 'CSS 자바 스크립트'],
    'GIS': ['GIS', 'GIS 응용 프로그램', 'GIS 시스템'],
    'IOS': ['IOS', 'IOS 개발', 'IOS 디자인', 'MAC', 'APPLE SOFTWARE'],
    'VM웨어': ['VM웨어', 'VMWARE INFRASTRUCTURE'],
    'WINDOWS': ['WINDOWS 8', 'WINDOWS 서버', 'WINDOWS 서비스', 'WINDOWS 원격 데스크톱', 'WINDOWS EMBEDDED'],
    'WORDPRESS': ['WORDPRESS', 'WORDPRESS DESIGN'],
    'ANDROID': ['ANDROID', 'ANDROID STUDIO', '안드로이드 개발', '안드로이드 SDK'],
    'ANGULAR': ['ANGULAR', 'ANGULARJS'],
    'JAVASCRIPT': ['JAVASCRIPT', 'CSS 자바 스크립트'],
    'JSON': ['JSON', 'JSONAPI'],
    'API': ['API', 'JSONAPI', 'API 개발', 'ASTERISK'],
    '하드웨어': ['하드웨어', '하드웨어 설계', '하드웨어 테스트'],
    '시스템': ['시스템 관리', '시스템 구축', '시스템 구현', '시스템 통합'], 
    'UBUNTU': ['UBUNTU', 'DEBIAN'],
    'STORAGE': ['STORAGE', '스토리지 솔루션', '스토리지 영역 네트워크', 'EMC STORAGE'],
    'DATA ANALYSIS': ['DATA ANALYSIS', '데이터 분석'],
    'HTML': ['HTML', 'HTML5', 'XHTML'],
    'BLOCKCHAIN': ['BLOCKCHAIN', 'HYPERLEDGER'],
    
}

drop_list = [
    '개발', '설계', '최적화', '컴퓨터 공학', '모델링', '수학', '검증', '영상', '제품 개발', '프로젝트 관리', '차량', 
    '자동차', '웹사이트', '카메라', '반도체', '고객 관계', '고객 중심', '고객 지원', '공공 부문', '공차 분석', 
    '교육 관리', '교육 기술', '구매 관리', '기술 개발', '기술 관리', '기술 교육', '기술 문서', '강의', '네비게이션 시스템', 
    '데이터 입력', '데이터 통합', '도메인 관리', '라이브러리 관리', '레이더', '리팩토링', '마이크로프로세서', '모델링 및 시뮬레이션',
    '모뎀', '모터 제어', '모바일 기술', '모바일 장치', '백신', '병렬 프로그래밍', '복제', '분석 개발', '분석 능력', '분석 문제 해결', 
    '브랜딩', '비즈니스 분석', '상품 기획', '샘플 관리', '샘플 준비', '생산 계획', '분석 서비스', '분석능력', '성능 측정', '위성 통신',
    '영어 실력', '요구 사항 분석', '일본어', '자동차 전자', '자산 관리', '자연 언어 처리', '재고 관리', '전력전자학', '전원 엔지니어링', 
    '전자 공학', '전자정부프레임워크', '정보관리', '제안서 작성', '제어 시스템 설계', '카산드라', '컴파일러', '클라이언트 개발', 
    '테스트 실행', '통계 모델링', '품질 관리', '품질 보증', '프레젠테이션', '프로그램 관리', '프로세스 개선', '프로젝트 납품', 
    '프로젝트 실행', '프로토 타이핑', '프로토콜 개발', '학술 연구', '학술 출판', '회로', '회로 분석', '회로 설계', 
    'HEALTH INFORMATION TECHNOLOGY', 'HP', 'PROCESSING', 'POS', '서비스 관리', '서비스 디자인', '서비스 프로세스', 
    'IT 관리', 'IT 운영', 'COMMUNICATION', '프론트엔드 개발자', '연구 및 개발', '아날로그 회로 설계', '소프트웨어 검증',
    '운영 관리', '운영체제', '유지보수', '의료 기기', '의료 산업', '의료 영상', '의료 장비', '인버터', 'CLUSTERING',
    'DEBUGGING', 'EMC 규정 준수', '데이터 구조', '관리', '알고리즘 개발', '알고리즘 설계', 'POP 디스플레이', 'RFP', 
    'QLIKVIEW', 'MS 오피스', 'TESTNG', 'KYC', '윈도우 모바일', 'CHILDREN', 'ISR', 'PALANTIR', 'OFFICE 365', 
    'PMO', '백엔드 개발',
]

# skillset_dict 만들기
def skillset_dict():
    skillset_dict = dict()
    skills_set = get_skills_list()
    mapping_values = [item for sublist in list(skill_mapping.values()) for item in sublist]
    for skill in skills_set:
        if skill in mapping_values:
            for key, mappings in skill_mapping.items():
                if skill in mappings:
                    if key in skillset_dict:
                        skillset_dict[key].append(skill)
                    else:
                        skillset_dict[key] = [skill]
        else:
            if skill not in drop_list:
                skillset_dict[skill] = [skill]
    return skillset_dict


skillset_dict = skillset_dict()
print(len(list(skillset_dict.keys())))
# print(len(skillset_dict))
# values_count = 0
# for values in skillset_dict.values():
#     values_count += len(values)
# print(skillset_dict)
# print("key count: " + str(len(skill_mapping)))
# print("values count: " + str(values_count))
# print("skilset length: " + str(len(skillset_dict)))

def skill_scaling():
    # with open("data/qual_pref_skill_scaling.csv", "w", encoding="utf-8") as f:
    #     writer = csv.writer(f)

    #     writer.writerow(["id"]+list(skills_dict.keys()))
    skills_dict = skillset_dict()
    key = list(skills_dict.keys())
    skill_df = pd.DataFrame(columns=['id']+key)
    with open("data/qual_pref_skill_combined.csv", "r", encoding="utf-8") as combined_data:
        reader = csv.reader(combined_data)
        data = list(reader)

        for row in data[1:]:

            skill_cols = skills_dict.copy()
            qps_id = row[0]
            quals = re.findall(r"'(.*?)'", row[1])
            prefs = re.findall(r"'(.*?)'", row[2])
            skills = re.findall(r"'(.*?)'", row[3])
            if qps_id == "18228":
                for key, value in skills_dict.items():
                    skill_cols[key] = 0

                    if len(quals) > 0:
                        for q in quals:
                            if q in value:
                                skill_cols[key] += 2
                                break

                    if len(prefs) > 0:
                        for p in prefs:
                            if p in value:
                                skill_cols[key] += 1
                                break

                    if len(skills) > 0:
                        for s in skills:
                            if s in value:
                                skill_cols[key] += 1
                                break
                # print(row[0])
                skill_df = pd.concat([skill_df,
                                        pd.DataFrame([[qps_id] + list(skill_cols.values())], columns = skill_df.columns)],
                                       ignore_index=True)
                # df_row = pd.DataFrame(skill_cols, index=[row[0]])
                # # print(df_row)
                # skill_df = pd.concat([skill_df, df_row])
                # skill_df.index.name = 'id'
                # print(skill_df)
    return skill_df

# skills = skill_scaling()
# for i in skills:
#     if int(skills[i]) > 0:
#         # print(i, skills[i])

# print(skill_scaling())

# 유사도 검증
# def similarity():
#     # Load the job offering dataset with one-hot encoded skills
#
#     job_data = skill_scaling()
#
#     user_skills = {
#         'MYSQL':1,
#         'PYTHON':1,
#         'JAVA':1,
#         'HTML':1,
#         'REACT':1,
#         'SPRING FRAMEWORK':1,
#         'PYTORCH':1
#     }
#     skill_df = job_data[list(user_skills.keys())]
#     print(skill_df)
#     user_profile = pd.DataFrame(0, index=[0], columns=skill_df.columns[:])
#
#     # 유저 프로필 데이터 입력
#     for skill, grade in user_skills.items():
#         skill = skill.upper()
#         if skill in user_profile.columns:
#             user_profile[skill] = grade
#     print(user_profile)
#     # 입력 값 확인
#
#     similarity_scores = cosine_similarity(user_profile, skill_df.iloc[:, :])[0].tolist()
#     ser = pd.DataFrame(data={'similarity_score':similarity_scores}, index=skill_df.index.tolist())
#
#     skill_df = pd.concat([skill_df, ser], axis=1)
#
#     recommended_jobs = skill_df.nlargest(10, 'similarity_score')
#     rocommended_urls = recommended_jobs.index.tolist()
#     recommended_score = recommended_jobs['similarity_score'].tolist()
#
#
#     print("\n\n\n ", "="*10, "링크", "="*10)
#
#     for i in range(len(rocommended_urls)):
#         print("https://www.wanted.co.kr/wd/"+str(rocommended_urls[i]))
#         print(recommended_score[i])
#
#
#
# # Sample user-item rating matrix
#
# job_data = skill_scaling()
# user_skills = {
#         'MYSQL':1,
#         'PYTHON':1,
#         'JAVA':1,
#         'HTML':1,
#         'REACT':1,
#         'SPRING FRAMEWORK':1,
#         'PYTORCH':1
#     }
# skill_df = job_data[list(user_skills.keys())]
# print(skill_df)
# user_profile = pd.DataFrame(0, index=[0], columns=skill_df.columns[:])
#
# # 유저 프로필 데이터 입력
# for skill, grade in user_skills.items():
#     skill = skill.upper()
#     if skill in user_profile.columns:
#         user_profile[skill] = grade
# print(user_profile)

# Calculate the mean rating per item
# item_means = skill_df.mean(axis=0)
# print(item_means)
#
# # Calculate the Mean Squared Difference (MSD) similarity matrix
# msd_sim_matrix = 1 / (1 + np.sqrt(np.square(skill_df.T - skill_df).mean(axis=1)))
# print(msd_sim_matrix.shape)
#
# # Replace NaN values with 0 in the original DataFrame
# df_filled = skill_df.fillna(0)
# print(df_filled.shape)
# # Calculate the MSD-based predicted ratings
# predicted_ratings = (df_filled.T.dot(msd_sim_matrix.T)) / np.abs(msd_sim_matrix).sum()

# Print the predicted ratings
# print(predicted_ratings)


# similarity()
# print(skill_scaling())
