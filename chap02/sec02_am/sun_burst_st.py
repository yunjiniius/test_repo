import pandas as pd
import plotly.express as px
import streamlit as st

# 가상 데이터프레임 생성
data = {
    '지역': ['서울', '서울', '서울', '부산', '부산', '대구', '대구', '대구'],
    '구': ['강남구', '강남구', '송파구', '해운대구', '수영구', '달서구', '중구', '달서구'],
    '카테고리': ['식당', '카페', '식당', '카페', '식당', '식당', '카페', '카페'],
    '매출': [500, 300, 400, 250, 150, 200, 100, 180]
}

df = pd.DataFrame(data)

# Streamlit 앱 설정
st.title('지역별 구와 카테고리별 매출 분포')

# Sunburst 차트 생성
fig = px.sunburst(df, path=['지역', '구', '카테고리'], values='매출', 
                  title='지역별 구와 카테고리별 매출 분포')

# 차트 출력
st.plotly_chart(fig)
