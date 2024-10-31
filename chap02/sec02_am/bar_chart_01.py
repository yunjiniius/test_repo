import pandas as pd
import plotly.express as px
import streamlit as st

# 가상 데이터프레임 생성
data = {
    '과제명': ['A과제', 'B과제', 'C과제'],
    '완료예정일': [10, 15, 20],
    '실제완료일': [12, 15, 18]
}

df = pd.DataFrame(data)

# 완료율 계산
df['완료율(%)'] = (df['완료예정일'] / df['실제완료일']) * 100

# Streamlit 앱 설정
st.title('과제 완료율 비교')
st.dataframe(df)

# 막대 그래프 생성
fig = px.bar(df, x='과제명', y='완료율(%)', title='과제별 완료율 비교')

# 차트 출력
st.plotly_chart(fig)
