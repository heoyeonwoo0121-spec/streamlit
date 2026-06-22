import streamlit as st
import pandas as pd
df = pd.read_csv(r"D:\streamlit\heart_failure.csv")
# 왼쪽 사이드바에 필터를 둔다
st.sidebar.header(" 필터")
age = st.sidebar.slider("최대 나이",
40, 95, 70)
df = df[df['age'] <= age]
# 본문을 둘로 나눈다
c1, c2 = st.columns(2)
c1.metric("환자 수", len(df))
c2.metric("평균 나이", f"{df.age.mean():.0f}")