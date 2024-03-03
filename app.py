import streamlit as st
from streamlit_card import card

from components.navigation import navigation


st.set_page_config(
    page_title="CMaster",
    page_icon="🪄",
    layout="wide"
)


st.session_state["current_page"] = None


if "user_id" not in st.session_state:
    if st.button("hanjoo88.han 로그인"):
        st.session_state.clear()
        st.session_state["user_id"] = "hanjoo88.han"
        st.session_state["username"] = "한주형"
        st.rerun()
    if st.button("hd81.lee 로그인"):
        st.session_state.clear()
        st.session_state["user_id"] = "hd81.lee"
        st.session_state["username"] = "이호동"
        st.rerun()
else:
    navigation()

    c1, c2, _ = st.columns(3)

    with c1:
        card(
            title="DYF",
            text="DYF 마스터 아이템",
            image="https://cdn.pixabay.com/photo/2019/07/30/18/26/surface-4373559_1280.jpg",
            key="DYF",
            on_click=lambda: st.switch_page("pages/dyf.py")
        )

    with c2:
        card(
            title="CMS",
            text="준비 중",
            image="https://cdn.pixabay.com/photo/2016/07/10/19/19/sampler-1508279_1280.jpg",
            key="CMS",
            on_click=lambda: st.switch_page("pages/cms.py")
        )