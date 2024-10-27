import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

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

st.title("팀별 직원 목록")
st.subheader("AG Grid를 사용한 팀별 그룹화와 체크박스 선택")

# AG Grid 옵션 설정
gb = GridOptionsBuilder.from_dataframe(data)
# gb.configure_pagination(paginationAutoPageSize=True)
gb.configure_column("department", rowGroup=True, hide=True)
gb.configure_column("name", headerName="직원 이름")
gb.configure_column("age", headerName="나이")
gb.configure_selection("multiple", use_checkbox=True)

# AG Grid 표시
grid_options = gb.build()
grid_response = AgGrid(
    data,
    gridOptions=grid_options,
    enable_enterprise_modules=True,  # 그룹화 기능 활성화
    theme="alpine",
    update_mode="SELECTION_CHANGED"
)

# 선택된 행 데이터 가져오기
selected_rows = grid_response["selected_rows"]
st.subheader("선택된 직원 데이터")
st.write(pd.DataFrame(selected_rows))
