import streamlit as st
st.title(" 심부전 분석")
st.write("👈 메뉴를 선택하세요")
# pages/1_데이터.py
import streamlit as st, pandas as pd
st.title("📊 데이터")
df = pd.read_csv("heart_failure.csv")
st.dataframe(df)