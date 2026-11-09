import streamlit as st

st.title("SafePrompt")
st.caption("1주차 화면 테스트용입니다. 예시 문장: 김민수입니다.")

text = st.text_area("문장을 입력하세요")

if st.button("개인정보 확인"):
    if not text.strip():
        st.warning("문장을 입력해 주세요.")
    elif "김민수" in text:
        st.write("가상 탐지 결과: 김민수 (PERSON)")
    else:
        st.info("테스트하려면 '김민수입니다.'를 입력해 주세요.")
