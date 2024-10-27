import streamlit as st
import pandas as pd

# 초기 데이터 생성 (10x10 데이터프레임)
data = pd.DataFrame({
    f"Column {chr(65 + i)}": [f"Value {chr(65 + i)}{j+1}" for j in range(10)]
    for i in range(10)
})

# 데이터프레임과 새로고침 트리거를 세션 상태로 유지
if 'df' not in st.session_state:
    st.session_state.df = data.copy()
if 'refresh_trigger' not in st.session_state:
    st.session_state.refresh_trigger = 0

# 데이터프레임 화면에 표시
st.title("데이터프레임 행 추가 및 삭제")
st.dataframe(st.session_state.df)

# 행 추가 버튼
st.subheader("행 추가")
add_position = st.number_input("추가할 행 위치 (0부터 시작):", min_value=0, max_value=len(st.session_state.df), step=1)
new_row_data = {col: st.text_input(f"{col} 값 입력", key=f"add_{col}") for col in st.session_state.df.columns}

# "추가" 버튼 -> 행 추가
if st.button("추가"):
    # 새 행을 데이터프레임으로 생성
    new_row = pd.DataFrame([new_row_data])
    # 데이터프레임에 해당 위치에 삽입
    st.session_state.df = pd.concat([
        st.session_state.df.iloc[:add_position], 
        new_row, 
        st.session_state.df.iloc[add_position:]
    ]).reset_index(drop=True)
    st.success(f"행이 {add_position} 위치에 추가되었습니다.")
    # 새로고침 효과를 위해 트리거 값 변경
    st.session_state.refresh_trigger += 1

# 행 삭제 버튼
st.subheader("행 삭제")
delete_position = st.number_input("삭제할 행 위치 (0부터 시작):", min_value=0, max_value=len(st.session_state.df) - 1, step=1)

# "삭제" 버튼 -> 행 삭제
if st.button("삭제"):
    # 데이터프레임에서 해당 위치의 행 삭제
    st.session_state.df = st.session_state.df.drop(delete_position).reset_index(drop=True)
    st.success(f"{delete_position} 위치의 행이 삭제되었습니다.")
    # 새로고침 효과를 위해 트리거 값 변경
    st.session_state.refresh_trigger += 1
