import streamlit as st
import pandas as pd

# 가상 데이터 생성 (10x10 데이터프레임)
data = pd.DataFrame({
    f"Column {i+1}": [f"Value {i+1}-{j+1}" for j in range(10)]
    for i in range(10)
})

# 데이터프레임을 세션 상태로 저장해 편집 가능하게 만듦
if 'df' not in st.session_state:
    st.session_state.df = data.copy()

# 데이터프레임 표시
st.title("데이터프레임 셀 선택 및 수정")
st.dataframe(st.session_state.df)

# 특정 셀 선택을 위한 input
st.subheader("셀 선택")
row_input = st.number_input("Row (0~9):", min_value=0, max_value=9, step=1)
col_input = st.number_input("Column (0~9):", min_value=0, max_value=9, step=1)

# 선택한 셀의 값 가져오기
selected_value = st.session_state.df.iloc[row_input, col_input]
st.write(f"선택한 셀의 값: {selected_value}")


# 선택한 셀의 값 수정 input
new_value = st.text_input("새로운 값 입력", value=selected_value)

# 값 저장 버튼
if st.button("저장"):
    # 데이터프레임의 해당 셀 값을 업데이트
    st.session_state.df.iloc[row_input, col_input] = new_value
    st.success(f"Row {row_input}, Column {col_input}의 값이 '{new_value}'(으)로 저장되었습니다.")
    # 데이터프레임 새로고침
    st.experimental_rerun()
