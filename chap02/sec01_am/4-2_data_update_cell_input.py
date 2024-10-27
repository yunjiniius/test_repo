import streamlit as st
import pandas as pd
import re

# 가상 데이터 생성 (10x10 데이터프레임)
data = pd.DataFrame({
    f"Column {chr(65 + i)}": [f"Value {chr(65 + i)}{j+1}" for j in range(10)]
    for i in range(10)
})

# 데이터프레임을 세션 상태로 저장해 편집 가능하게 만듦
if 'df' not in st.session_state:
    st.session_state.df = data.copy()

# 데이터프레임 표시
st.title("데이터프레임 셀 선택 및 수정")
st.dataframe(st.session_state.df)

# 특정 셀 선택을 위한 Excel 스타일 input
st.subheader("셀 선택 (예: A1, B3)")
cell_input = st.text_input("셀 입력 (A1 형식):")

# Excel 형식의 셀 주소를 행, 열 인덱스로 변환
def parse_excel_address(address):
    match = re.match(r"([A-J])([1-9]|10)", address, re.I)
    if match:
        col_letter = match.group(1).upper()
        row_number = int(match.group(2)) - 1
        col_index = ord(col_letter) - 65
        return row_number, col_index
    else:
        return None, None

# 선택한 셀의 값 가져오기
row_idx, col_idx = parse_excel_address(cell_input)
if row_idx is not None and col_idx is not None:
    selected_value = st.session_state.df.iloc[row_idx, col_idx]
    st.write(f"선택한 셀의 값: {selected_value}")

    # 선택한 셀의 값 수정 input
    new_value = st.text_input("새로운 값 입력", value=selected_value)

    # 값 저장 버튼
    if st.button("저장"):
        # 데이터프레임의 해당 셀 값을 업데이트
        st.session_state.df.iloc[row_idx, col_idx] = new_value
        st.success(f"셀 {cell_input}의 값이 '{new_value}'(으)로 저장되었습니다.")
        # 데이터프레임 새로고침
        st.experimental_rerun()
else:
    st.warning("올바른 셀 주소를 입력하세요 (예: A1, B3).")
