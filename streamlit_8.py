#표보기와 차트 보기의 두개의 탭을 화면에 나눠 표시
import streamlit as st
import pandas as pd
df = pd.read_csv(r"D:\streamlit\heart_failure.csv")
import matplotlib.pyplot as plt

# 2. 사이드바 필터 추가 (여기서 df를 필터링합니다)
st.sidebar.header("필터")
age = st.sidebar.slider("최대 나이", 40, 95, 70)
df = df[df['age'] <= age]  # 선택한 나이 이하의 데이터만 남깁니다.

# 3. 사이드바 필터 결과 표시 (환자 수, 평균 나이)
c1, c2 = st.columns(2)
c1.metric("환자 수", len(df))
c2.metric("평균 나이", f"{df['age'].mean():.0f}")

# 1. 탭 생성 (빈칸 채우기)
tab1, tab2 = st.tabs(["표", "차트"])

# 2. 탭별 내용 구성
with tab1:
    st.write("데이터 표")
    st.dataframe(df)

with tab2:
    st.write("나이 히스토그램")
    fig, ax = plt.subplots()
    ax.hist(df['age'])
    st.pyplot(fig)