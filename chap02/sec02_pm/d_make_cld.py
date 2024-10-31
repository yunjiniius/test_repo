import random
from datetime import datetime, timedelta

def generate_mock_calendar_data():
    sample_titles = [
        "○ 팀 회의", "■ 프로젝트 마감일", "운동", "○ 점심 약속", "저녁 식사", "■ 병원 방문", "○ 친구 모임",
        "출장", "■ 프레젠테이션 준비", "자격증 시험", "독서 모임", "○ 화상 회의", "도서관 방문",
        "■ 고객 상담", "음악회", "영화 보기", "가족 모임", "○ 자전거 타기", "주간 보고서 작성", "맛있는 저녁을 위한 고민"
    ]
    sample_names = [
        "김철수", "이영희", "박민수", "정혜린", "최준혁", "한가은", "오세민", "장하준", "류지원", "신지훈"
    ]
    
    mock_data = []
    base_date = datetime(2024, 10, 31)
    
    for day in range(10):
        current_date = base_date + timedelta(days=day)
        start_hour = 8
        end_hour = 18 
        
        while start_hour < end_hour:
            person_id = random.choice(sample_names)
            cld_start = datetime(current_date.year, current_date.month, current_date.day, start_hour, 0)
            cld_duration = 1
            cld_end = cld_start + timedelta(hours=cld_duration)
            cld_title = random.choice(sample_titles)
            
            # 우선순위 설정
            if "○" in cld_title:
                priority = 1
            elif "■" in cld_title:
                priority = 2
            else:
                priority = 3
            
            mock_data.append({
                "person_id": person_id,
                "cld_date": current_date.strftime("%Y/%m/%d"),
                "cld_start": cld_start.strftime("%H:%M"),
                "cld_end": cld_end.strftime("%H:%M"),
                "cld_title": cld_title,
                "priority": priority
            })
            
            start_hour += cld_duration  # 다음 시간대로 이동
    
    return mock_data
