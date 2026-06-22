import streamlit as st
st.title("나의 첫 앱 ")
st.write("안녕하세요, Streamlit!")
name = st.text_input("이름을 입력하세요")
st.write(f"반가워요, {name}님 ")
