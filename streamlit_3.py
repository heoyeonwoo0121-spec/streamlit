import streamlit as st
import pandas as pd
df = pd.read_csv("heart_failure.csv")
#슬라이더가 고른 나이가 age_max 로
age_max = st.slider("최대 나이", 40, 95, 70)#70은 초깃값
# 선택값으로 데이터를 걸러냄
filtered = df[df['age'] <= age_max]
st.write(f"{len(filtered)}명이 조건에 맞아요")
st.dataframe(filtered)
#---슬라이더로-----------

#import streamlit as st
#import pandas as pd
#df = pd.read(r"D:\streamlit\heart_failure.csv")
#st.dataframe(df.head(10))
#avg = df['age'].mean()
#st.metric("평균 나이", f"{avg:.1f}세")

