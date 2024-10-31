from datetime import datetime, timedelta
from a_make_cld import generate_mock_calendar_data

work_start = datetime.strptime("09:00", "%H:%M")
work_end = datetime.strptime("18:00", "%H:%M")

empty_slots = []

def find_empty_slots():
    grouped_data = {}
    for entry in generate_mock_calendar_data():
        cld_date = entry["cld_date"]
        if cld_date not in grouped_data:
            grouped_data[cld_date] = []
        grouped_data[cld_date].append(entry)

    for cld_date, events in grouped_data.items():
        events.sort(key=lambda x: datetime.strptime(x["cld_start"], "%H:%M"))
        
        current_time = work_start
        for event in events:
            event_start = datetime.strptime(event["cld_start"], "%H:%M")
            if current_time < event_start:
                empty_slots.append({
                    "cld_date": cld_date,
                    "slot_start": current_time.strftime("%H:%M"),
                    "slot_end": event_start.strftime("%H:%M")
                })
            event_end = datetime.strptime(event["cld_end"], "%H:%M")
            current_time = max(current_time, event_end)
        
        if current_time < work_end:
            empty_slots.append({
                "cld_date": cld_date,
                "slot_start": current_time.strftime("%H:%M"),
                "slot_end": work_end.strftime("%H:%M")
            })

    print(empty_slots)
    
    return empty_slots