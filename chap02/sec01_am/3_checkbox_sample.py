import streamlit as st
import pandas as pd

# 샘플 데이터 생성
data = pd.DataFrame({
    "name": ["Alice0", "Bob0", "Charlie0", "Elice0", "Beast0", "Cinderella0",
             "Alice1", "Bob1", "Charlie1", "Elice1", "Beast1", "Cinderella1",
             "Alice2", "Bob2", "Charlie2", "Elice2", "Beast2", "Cinderella2",
             "Alice3", "Bob3", "Charlie3", "Elice3", "Beast3", "Cinderella3",
             "Alice4", "Bob4", "Charlie4", "Elice4", "Beast4", "Cinderella4",
             "Alice5", "Bob5", "Charlie5", "Elice5", "Beast5", "Cinderella5",
             "Alice6", "Bob6", "Charlie6", "Elice6", "Beast6", "Cinderella6",
             "Alice7", "Bob7", "Charlie7", "Elice7", "Beast7", "Cinderella7",
             "Alice8", "Bob8", "Charlie8", "Elice8", "Beast8", "Cinderella8",
             "Alice9", "Bob9", "Charlie9", "Elice9", "Beast9", "Cinderella9"],
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
st.subheader("팀별 그룹화된 직원 목록과 선택 (직원별 체크박스)")

# 데이터프레임을 팀별로 그룹화
grouped_data = data.groupby("department")

# 각 팀별로 반복하여 직원별 체크박스 표시
selected_employees = {}
for department, group in grouped_data:
    st.write(f"### {department}")  # 팀명 표시
    selected_employees[department] = []
    for name in group["name"]:
        # 각 직원 이름을 체크박스로 표시하고 선택된 직원들만 저장
        if st.checkbox(f"{name}", key=f"{department}_{name}"):
            selected_employees[department].append(name)

# 선택된 직원 목록 표시
st.subheader("선택된 직원들")
for department, employees in selected_employees.items():
    if employees:  # 선택된 직원이 있는 경우에만 표시
        st.write(f"{department}: {', '.join(employees)}")
