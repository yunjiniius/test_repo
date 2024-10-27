import streamlit as st
import pandas as pd

# 샘플 데이터 생성
data = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Elice", "Beast", "Cinderella",
            "Alice", "Bob", "Charlie", "Elice", "Beast", "Cinderella",
            "Alice", "Bob", "Charlie", "Elice", "Beast", "Cinderella",
            "Alice", "Bob", "Charlie", "Elice", "Beast", "Cinderella",
            "Alice", "Bob", "Charlie", "Elice", "Beast", "Cinderella",
            "Alice", "Bob", "Charlie", "Elice", "Beast", "Cinderella",
            "Alice", "Bob", "Charlie", "Elice", "Beast", "Cinderella",
            "Alice", "Bob", "Charlie", "Elice", "Beast", "Cinderella",
            "Alice", "Bob", "Charlie", "Elice", "Beast", "Cinderella",
            "Alice", "Bob", "Charlie", "Elice", "Beast", "Cinderella"],
    "age": [24, 27, 22, 25, 28, 23,
           24, 27, 22, 25, 28, 23,
           24, 27, 22, 25, 28, 23,
           24, 27, 22, 25, 28, 23,
           24, 27, 22, 25, 28, 23,
           24, 27, 22, 25, 28, 23,
           24, 27, 22, 25, 28, 23,
           24, 27, 22, 25, 28, 23,
           24, 27, 22, 25, 28, 23,
           24, 27, 22, 25, 28, 23],
    "department": ["개발1팀", "개발1팀", "개발1팀", "개발2팀", "개발2팀", "개발2팀",
                  "개발1팀", "개발1팀", "개발1팀", "개발2팀", "개발2팀", "개발2팀",
                  "개발1팀", "개발1팀", "개발1팀", "개발2팀", "개발2팀", "개발2팀",
                  "개발1팀", "개발1팀", "개발1팀", "개발2팀", "개발2팀", "개발2팀",
                  "개발1팀", "개발1팀", "개발1팀", "개발2팀", "개발2팀", "개발2팀",
                  "개발1팀", "개발1팀", "개발1팀", "개발2팀", "개발2팀", "개발2팀",
                  "개발1팀", "개발1팀", "개발1팀", "개발2팀", "개발2팀", "개발2팀",
                  "개발1팀", "개발1팀", "개발1팀", "개발2팀", "개발2팀", "개발2팀",
                  "개발1팀", "개발1팀", "개발1팀", "개발2팀", "개발2팀", "개발2팀",
                  "개발1팀", "개발1팀", "개발1팀", "개발2팀", "개발2팀", "개발2팀"]
})

#
st.title("팀별 직원 목록 대시보드")
st.subheader("팀별 그룹화된 직원 목록과 다중 선택 (항상 펼쳐진 상태)")

# 데이터프레임을 팀별로 그룹화
grouped_data = data.groupby("department")

# 각 팀별로 반복하여 펼쳐진 다중 선택 상자 표시
selected_employees = {}
for department, group in grouped_data:
    with st.expander(f"{department}", expanded=True):  # 항상 펼쳐진 상태
        selected_employees[department] = st.multiselect(
            f"{department}에서 선택할 직원", 
            options=group["name"].tolist(),
            key=department  # 각 팀에 대한 multiselect 키 설정
        )

# 선택된 직원 목록 표시
st.subheader("선택된 직원들")
for department, employees in selected_employees.items():
    if employees:  # 선택된 직원이 있는 경우에만 표시
        st.write(f"{department}: {', '.join(employees)}")
