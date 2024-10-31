from datetime import datetime, timedelta
from d_make_cld import generate_mock_calendar_data

work_start = datetime.strptime("09:00", "%H:%M")
work_end = datetime.strptime("18:00", "%H:%M")

def find_empty_slots():
    grouped_data = {}
    all_events = generate_mock_calendar_data()  # 전체 일정 데이터를 저장
    empty_slots = []

    # 각 참가자의 일정을 날짜별로 그룹화
    for entry in all_events:
        cld_date = entry["cld_date"]
        if cld_date not in grouped_data:
            grouped_data[cld_date] = []
        grouped_data[cld_date].append(entry)

    # 날짜별 공통 빈 시간대 계산
    for cld_date, events in grouped_data.items():
        # 각 참가자의 일정 순서 정렬
        events.sort(key=lambda x: datetime.strptime(x["cld_start"], "%H:%M"))
        current_time = work_start
        busy_intervals = []

        # 각 일정의 바쁜 시간대를 수집
        for event in events:
            event_start = datetime.strptime(event["cld_start"], "%H:%M")
            event_end = datetime.strptime(event["cld_end"], "%H:%M")
            busy_intervals.append((event_start, event_end))
        
        # 공통 빈 시간대 찾기
        available_start = work_start
        for start, end in busy_intervals:
            if available_start < start:
                empty_slots.append({
                    "cld_date": cld_date,
                    "slot_start": available_start.strftime("%H:%M"),
                    "slot_end": start.strftime("%H:%M")
                })
            available_start = max(available_start, end)

        # 근무 종료 시간까지 빈 시간대 확인
        if available_start < work_end:
            empty_slots.append({
                "cld_date": cld_date,
                "slot_start": available_start.strftime("%H:%M"),
                "slot_end": work_end.strftime("%H:%M")
            })

    return empty_slots, all_events  # 빈 시간대와 전체 일정 반환
