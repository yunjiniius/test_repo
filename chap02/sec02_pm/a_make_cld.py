import random
from datetime import datetime, timedelta

def generate_mock_calendar_data():
    sample_titles = [
        "팀 회의", "프로젝트 마감일", "운동", "점심 약속", "저녁 식사", "병원 방문", "친구 모임",
        "출장", "프레젠테이션 준비", "자격증 시험", "독서 모임", "화상 회의", "도서관 방문",
        "고객 상담", "음악회", "영화 보기", "가족 모임", "자전거 타기", "주간 보고서 작성", "맛있는 저녁을 위한 고민"
    ]
    sample_names = [
        "김철수", "이영희", "박민수", "정혜린", "최준혁", "한가은", "오세민", "장하준", "류지원", "신지훈"
    ]
    
    mock_data = []
    base_date = datetime(2024, 10, 31)
    
    for _ in range(20):
        person_id = random.choice(sample_names)
        cld_date = base_date + timedelta(days=random.randint(0, 10))
        cld_start_hour = random.randint(8, 18)
        cld_start_minute = random.choice([0, 30])
        cld_duration = random.randint(1, 4)
        cld_start = datetime(cld_date.year, cld_date.month, cld_date.day, cld_start_hour, cld_start_minute)
        cld_end = cld_start + timedelta(hours=cld_duration)
        cld_title = random.choice(sample_titles)
        
        mock_data.append({
            "person_id": person_id,
            "cld_date": cld_date.strftime("%Y/%m/%d"),
            "cld_start": cld_start.strftime("%H:%M"),
            "cld_end": cld_end.strftime("%H:%M"),
            "cld_title": cld_title
        })
        
    print(mock_data)
    
    return mock_data

