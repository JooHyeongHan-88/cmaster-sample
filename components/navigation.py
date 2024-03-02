import streamlit as st


def navigation():
    if "username" not in st.session_state:
        st.switch_page("app.py")
    else:
        # st.sidebar.button(st.session_state["username"] + "님. 안녕하세요.", use_container_width=True, disabled=True)
        with st.sidebar.container(border=True):
            st.write(st.session_state["username"] + "님. 안녕하세요.")
        st.sidebar.page_link("app.py", label="🏠 HOME")
        if st.session_state["current_page"]:
            st.sidebar.page_link(st.session_state["current_page_path"], label=st.session_state["current_page"])
