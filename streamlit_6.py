import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#한글깨짐 방지
import platform
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
df = pd.read_csv(r"D:\streamlit\heart_failure.csv")
counts = df['DEATH_EVENT'].value_counts()
#bar차트
st.bar_chart(counts)
#matplotlib차트
fig, ax = plt.subplots()
ax.bar(["생존", "사망"], counts)
st.pyplot(fig)