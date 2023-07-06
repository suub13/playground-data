
combined_crawling_data = '''
    CREATE TABLE IF NOT EXISTS combined_crawling_data (
        id INT PRIMARY KEY,
        url VARCHAR(255),
        job_list VARCHAR(255),
        title VARCHAR(255),
        company VARCHAR(255),
        location VARCHAR(255),
        tags VARCHAR(255),
        qualifications TEXT,
        preferred TEXT,
        benefits TEXT,
        skills TEXT,
        workplace TEXT,
        crawled_date DATE
    )
'''