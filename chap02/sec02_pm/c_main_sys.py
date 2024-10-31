from datetime import datetime, timedelta
import streamlit as st
from b_check_cld import find_empty_slots

st.title("회의 가능 시간 추천 시스템")

empty_slots = find_empty_slots()
st.subheader("추천 회의 가능 시간")
if empty_slots:
    for slot in empty_slots:
        st.write(f"날짜: {slot['cld_date']}, 시간: {slot['slot_start']} - {slot['slot_end']}")
else:
    st.write("회의 가능 시간이 없습니다.")