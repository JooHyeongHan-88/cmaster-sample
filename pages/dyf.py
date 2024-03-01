import streamlit as st

from components.navigation import navigation
from components.modal import (
    modal_create_master, modal_load_master, modal_save_master,
    modal_create_eds, modal_load_eds, modal_save_eds
)
from utils.dyf import (
    create_master, load_master, save_master,
    create_eds, load_eds, save_eds
)
from data.dyf import (
    df_master, df_item, df_condition, df_eds,
    sel_operator,
    sel_master_public, sel_master_private,
    sel_eds_public, sel_eds_private
)


# Initialize ---------------------------------------------------------------------------------

st.session_state["current_page"] = "DYF"
st.session_state["current_page_path"] = "pages/dyf.py"

if "main_view" not in st.session_state:
    st.session_state["main_view"] = "default"

if "public_mode_master" not in st.session_state:
    st.session_state["public_mode_master"] = True

if "public_mode_eds" not in st.session_state:
    st.session_state["public_mode_eds"] = True


# Main ---------------------------------------------------------------------------------------

# navigation
navigation()

# sidebar
with st.sidebar:
    st.divider()

    st.subheader("Master")
    if st.button("✒️ Create New Master", key="create_master", type="primary", use_container_width=True):
        modal_create_master.open()
    st.selectbox("Select", options=["A 제품", "B 제품", "C 제품"], label_visibility='collapsed')
    c1, c2 = st.columns([3, 2])
    if c1.button("✨ 최신 버전 열기", key="master_load_newest", use_container_width=True):
        load_master()
    if c2.button("버전 선택", key="master_load_ver", use_container_width=True):
        modal_load_master.open()

    st.markdown("")

    st.subheader("EDS Plan")
    if st.button("✒️ Create New EDS Plan", key="create_eds", type="primary", use_container_width=True):
        modal_create_eds.open()
    c1, c2 = st.columns([3, 2])
    if c1.button("✨ 최신 버전 열기", key="eds_load_newest", use_container_width=True):
        load_eds()
    if c2.button("버전 선택", key="eds_load_ver", use_container_width=True):
        modal_load_eds.open()

# main
if st.session_state["main_view"] == "default":
    st.title("DYF")
    st.divider()
    st.info("DBKM Yield Forecast를 위한 기준 정보 버전 관리 Appication입니다.", icon="ℹ️")

elif st.session_state["main_view"] == "main":
    st.title("Master")
    _, c2 = st.columns([11, 1])
    if c2.button("✔️ Save", key="master_save", type='primary', use_container_width=True):
        modal_save_master.open()

    t1, t2, t3 = st.tabs(["master", "master_item", "conditions"])

    with t1:
        st.data_editor(df_master, hide_index=True, num_rows='dynamic')

    with t2:
        st.data_editor(df_item, hide_index=True, num_rows='dynamic')

    with t3:
        st.data_editor(
            df_condition,
            hide_index=True,
            num_rows='dynamic',
            column_config={
                "operator": sel_operator
            }
        )

elif st.session_state["main_view"] == "eds":
    st.title("EDS Plan")   
    _, c2 = st.columns([11, 1])
    if c2.button("✔️ Save", key="eds_save", type='primary', use_container_width=True):
        modal_save_eds.open()
    st.data_editor(df_eds, hide_index=True, num_rows='dynamic')


# Modal Control ------------------------------------------------------------------------------------

# create 
if modal_create_master.is_open():
    with modal_create_master.container():
        _, c2 = st.columns([3, 1])
        if c2.button("신규 마스터 생성", use_container_width=True):
            create_master()
            modal_create_master.close()

if modal_create_eds.is_open():
    with modal_create_eds.container():
        _, c2 = st.columns([3, 1])
        if c2.button("빈 테이블 생성", use_container_width=True):
            create_eds()
            modal_create_eds.close()

# load
if modal_load_master.is_open():
    with modal_load_master.container():
        mode = st.radio("모드", ["개인", "공용"], label_visibility="collapsed", horizontal=True)
        if mode == "개인":
            st.selectbox("선택", sel_master_private, label_visibility="hidden")
            st.markdown("")
            _, c2 = st.columns([3, 1])
            if c2.button("📂 개인 버전 열기", use_container_width=True):
                load_master()
                modal_load_master.close()
        else:
            st.selectbox("선택", sel_master_public, label_visibility="hidden")
            st.markdown("")
            _, c2 = st.columns([3, 1])
            if c2.button("📂 공용 버전 열기", use_container_width=True):
                load_master()
                modal_load_master.close()

if modal_load_eds.is_open():
    with modal_load_eds.container():
        mode = st.radio("모드", ["개인", "공용"], label_visibility="collapsed", horizontal=True)
        if mode == "개인":
            st.selectbox("선택", sel_eds_private, label_visibility="hidden")
            st.markdown("")
            _, c2 = st.columns([3, 1])
            if c2.button("📂 개인 버전 열기", use_container_width=True):
                load_eds()
                modal_load_eds.close()
        else:
            st.selectbox("선택", sel_eds_public, label_visibility="hidden")
            st.markdown("")
            _, c2 = st.columns([3, 1])
            if c2.button("📂 공용 버전 열기", use_container_width=True):
                load_eds()
                modal_load_eds.close()

# save
if modal_save_master.is_open():
    with modal_save_master.container():
        mode = st.radio("모드", ["개인", "공용"], label_visibility="collapsed", horizontal=True)
        if mode == "개인":
            st.text_input("입력", placeholder="버전 코멘트 입력", label_visibility="hidden")
            st.markdown("")
            _, c2 = st.columns([3, 1])
            if c2.button("💾 개인 버전 저장", use_container_width=True):
                save_master()
                modal_save_master.close()
        else:
            st.text_input("입력", placeholder="버전 코멘트 입력", label_visibility="hidden")
            st.markdown("")
            _, c2 = st.columns([3, 1])
            if c2.button("💾 공용 버전 저장", use_container_width=True):
                save_master()
                modal_save_master.close()

if modal_save_eds.is_open():
    with modal_save_eds.container():
        mode = st.radio("모드", ["개인", "공용"], label_visibility="collapsed", horizontal=True)
        if mode == "개인":
            st.text_input("입력", placeholder="버전 코멘트 입력", label_visibility="hidden")
            st.markdown("")
            _, c2 = st.columns([3, 1])
            if c2.button("💾 개인 버전 저장", use_container_width=True):
                save_eds()
                modal_save_eds.close()
        else:
            st.text_input("입력", placeholder="버전 코멘트 입력", label_visibility="hidden")
            st.markdown("")
            _, c2 = st.columns([3, 1])
            if c2.button("💾 공용 버전 저장", use_container_width=True):
                save_eds()
                modal_save_eds.close()