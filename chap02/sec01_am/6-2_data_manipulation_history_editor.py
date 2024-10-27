import streamlit as st
import pandas as pd
from datetime import datetime

# 초기 데이터 생성 (10x10 데이터프레임)
data = pd.DataFrame({
    f"Column {chr(65 + i)}": [f"Value {chr(65 + i)}{j+1}" for j in range(10)]
    for i in range(10)
})

# 데이터프레임과 이전 상태를 세션 상태로 유지
if 'df' not in st.session_state:
    st.session_state.df = data.copy()
if 'df_previous' not in st.session_state:
    st.session_state.df_previous = data.copy()  # 이전 상태 저장

st.title("데이터프레임 편집 (추가/수정/삭제)")
st.subheader("데이터프레임 편집 가능")

# 데이터프레임 편집
edited_df = st.data_editor(st.session_state.df, use_container_width=True, num_rows="dynamic")

# 변경사항 저장
if st.button("변경사항 저장"):
    # 수정이 일어난 셀 찾기
    changes = []
    for row in range(len(edited_df)):
        for col in edited_df.columns:
            if edited_df.at[row, col] != st.session_state.df_previous.at[row, col]:
                changes.append({
                    "row": row,
                    "column": col,
                    "new_value": edited_df.at[row, col]
                })

    # 수정된 내용을 txt 파일에 저장
    if changes:
        with open("changes.txt", "a", encoding="utf-8") as file:  # UTF-8 인코딩 추가
            file.write(f"변경 사항 저장 시간: {datetime.now()}\n")
            for change in changes:
                file.write(f"행: {change['row']}, 열: {change['column']}, 새로운 값: {change['new_value']}\n")
            file.write("\n")  # 개행 추가
        st.success("변경 사항이 'changes.txt' 파일에 저장되었습니다.")

    # 세션 상태 업데이트
    st.session_state.df = edited_df.copy()  # 편집된 데이터프레임을 세션 상태에 저장
    st.session_state.df_previous = edited_df.copy()  # 현재 상태를 이전 상태로 갱신

# 행 추가
st.subheader("새로운 행 추가")
add_position = st.number_input("추가할 행 위치 (0부터 시작):", min_value=0, max_value=len(st.session_state.df), step=1)
new_row_data = {col: st.text_input(f"{col} 값 입력", key=f"add_{col}") for col in st.session_state.df.columns}

# "행 추가" 버튼
if st.button("행 추가"):
    new_row = pd.DataFrame([new_row_data])  # 새 행 생성
    # 기존 데이터프레임을 복사하여 원하는 위치에 새 행 추가
    st.session_state.df = pd.concat([
        st.session_state.df.iloc[:add_position],
        new_row,
        st.session_state.df.iloc[add_position:]
    ]).reset_index(drop=True)
    st.session_state.df_previous = st.session_state.df.copy()  # 이전 상태 업데이트
    st.success(f"새로운 행이 {add_position} 위치에 추가되었습니다.")

# 행 삭제
st.subheader("행 삭제")
delete_position = st.number_input("삭제할 행 위치 (0부터 시작):", min_value=0, max_value=len(st.session_state.df) - 1, step=1)

# "삭제" 버튼
if st.button("행 삭제"):
    st.session_state.df = st.session_state.df.drop(delete_position).reset_index(drop=True)
    st.session_state.df_previous = st.session_state.df.copy()  # 이전 상태 업데이트
    st.success(f"{delete_position} 위치의 행이 삭제되었습니다.")
