import streamlit as st
import pandas as pd

# 초기 데이터 생성 (10x10 데이터프레임)
data = pd.DataFrame({
    f"Column {chr(65 + i)}": [f"Value {chr(65 + i)}{j+1}" for j in range(10)]
    for i in range(10)
})

# 데이터프레임과 트리거를 세션 상태로 유지
if 'df' not in st.session_state:
    st.session_state.df = data.copy()
if 'update_trigger' not in st.session_state:
    st.session_state.update_trigger = 0  # 상태 업데이트를 위한 트리거

st.title("데이터프레임 편집 (추가/수정/삭제)")
st.subheader("데이터프레임 편집 가능")

# 데이터프레임 편집
edited_df = st.data_editor(st.session_state.df, use_container_width=True, num_rows="dynamic")

# 변경사항 저장 버튼
if st.button("변경사항 저장"):
    st.session_state.df = edited_df  # 편집된 데이터프레임을 세션 상태에 저장
    st.session_state.update_trigger += 1  # 트리거 값을 변경하여 페이지 업데이트
    st.success("변경사항이 저장되었습니다.")

# 행 추가
st.subheader("새로운 행 추가")
add_position = st.number_input("추가할 행 위치 (0부터 시작):", min_value=0, max_value=len(st.session_state.df), step=1)
new_row_data = {col: st.text_input(f"{col} 값 입력", key=f"add_{col}") for col in st.session_state.df.columns}

# "행 추가" 버튼 클릭
if st.button("행 추가"):
    new_row = pd.DataFrame([new_row_data])  # 새 행 생성
    # 기존 데이터프레임을 복사하여 원하는 위치에 새 행 추가
    st.session_state.df = pd.concat([
        st.session_state.df.iloc[:add_position],
        new_row,
        st.session_state.df.iloc[add_position:]
    ]).reset_index(drop=True)
    st.session_state.update_trigger += 1  # 트리거 값을 변경하여 페이지 업데이트
    st.success(f"새로운 행이 {add_position} 위치에 추가되었습니다.")

# 행 삭제
st.subheader("행 삭제")
delete_position = st.number_input("삭제할 행 위치 (0부터 시작):", min_value=0, max_value=len(st.session_state.df) - 1, step=1)

# "삭제" 버튼 클릭
if st.button("행 삭제"):
    st.session_state.df = st.session_state.df.drop(delete_position).reset_index(drop=True)
    st.session_state.update_trigger += 1  # 트리거 값을 변경하여 페이지 업데이트
    st.success(f"{delete_position} 위치의 행이 삭제되었습니다.")
