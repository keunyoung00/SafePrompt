# SafePrompt 1주차 UI 확인

- 실행 명령 `py -m streamlit run .\service\app.py`
- 빈 입력에서 개인정보 확인 버튼을 누르면 입력 안내가 표시됐다.
- 가상 입력 `김민수입니다. 전화번호는 010-0000-0000이고 이메일은 minsu@example.com입니다.`에서 후보 3개가 표시됐다.
- 위치는 PERSON `[0, 3)`, PHONE `[14, 27)`, EMAIL `[35, 52)`로 확인했다.
