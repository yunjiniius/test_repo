import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 난수 데이터 생성
df = pd.DataFrame({
    "A": np.random.randint(1, 100, 50),
    "B": np.random.randint(1, 100, 50)
})

# 데이터프레임 출력
st.write("아래는 데이터프레임입니다:", df)

# Matplotlib 그래프 생성
fig, ax = plt.subplots()
ax.scatter(df["A"], df["B"])
ax.set_title("Scatter Plot of A vs B")
ax.set_xlabel("A")
ax.set_ylabel("B")

# 그래프 출력
st.write(fig)
