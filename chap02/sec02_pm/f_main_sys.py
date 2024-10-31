from datetime import datetime, timedelta
import streamlit as st
from e_check_cld import find_empty_slots

st.title("회의 가능 시간 추천 시스템")

# 공통 회의 가능 시간 및 전체 일정 가져오기
empty_slots, all_events = find_empty_slots()

# 회의 가능 시간 출력
st.subheader("추천 회의 가능 시간")
if empty_slots:
    for slot in empty_slots:
        st.write(f"날짜: {slot['cld_date']}, 시간: {slot['slot_start']} - {slot['slot_end']}")
else:
    st.write("회의 가능 시간이 없습니다.")

    # 빈 시간대가 없는 경우, 3순위 일정 리스트 표시
    st.subheader("3순위 일정 리스트")
    third_priority_events = [event for event in all_events if event["priority"] == 3]

    if third_priority_events:
        for event in third_priority_events:
            st.write(f"날짜: {event['cld_date']}, 시간: {event['cld_start']} - {event['cld_end']}, 제목: {event['cld_title']}")
    else:
        st.write("3순위 일정이 없습니다.")
