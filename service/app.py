import streamlit as st

st.title("SafePrompt")
st.caption("1주차 더미 탐지 화면입니다. 아래 예시를 입력하고 ‘개인정보 확인’을 눌러 보세요.")
st.write("김민수입니다. 전화번호는 010-0000-0000이고 이메일은 minsu@example.com입니다.")

text = st.text_area("문장을 입력하세요")

demo_values = {
    "김민수": "PERSON",
    "010-0000-0000": "PHONE",
    "minsu@example.com": "EMAIL",
}

if st.button("개인정보 확인"):
    if not text.strip():
        st.warning("문장을 입력해 주세요.")
    else:
        spans = []

        for value, label in demo_values.items():
            start = text.find(value)
            if start >= 0:
                spans.append({
                    "value": value,
                    "label": label,
                    "start": start,
                    "end": start + len(value),
                })

        if spans:
            st.table(spans)
        else:
            st.info("입력에서 등록된 예시 값을 찾지 못했어요.")
