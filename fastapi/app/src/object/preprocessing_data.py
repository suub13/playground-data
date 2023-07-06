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
    'APACHE': ['APACHE', 'APACHE2'],
    '.NET': ['.NET', '.NET CORE', 'VB .NET'],
    '소켓': ['소켓', 'WEB SOCKET'],
    'FPGA': ['FPGA', 'FPGA 프로토타이핑'],
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
    'CSS': ['CSS', 'CSS3', 'CSS 자바스크립트'],
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
    'PMO', 
]