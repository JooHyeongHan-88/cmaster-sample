import streamlit as st

from components.navigation import navigation


st.session_state["current_page"] = "CMS"
st.session_state["current_page_path"] = "pages/cms.py"


navigation()

st.title("CMS")
st.divider()
st.info("준비 중입니다.", icon="ℹ️")
if st.button("돌아가기"):
    st.switch_page("app.py")