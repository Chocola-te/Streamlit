import streamlit as st

st.title('Streamlit 기본 예제 1 🚀') # <h1>로 제목 표시
st.write('안녕하세요! Streamlit을 배우고 있습니다.') # 일반 텍스트

if st.button('클릭해보세요!'):
  st.write('버튼이 눌렸습니다!')