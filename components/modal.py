import streamlit as st
from streamlit_modal import Modal

from utils.dyf import (
    create_master, load_master_ver, save_master,
    create_eds, load_eds_ver, save_eds,
    get_version_string, get_selected_ver_id
)
from data.dyf import df_version, df_master


modal_create_master = Modal("Create Master", key="create_master_modal")
modal_create_eds = Modal("Create EDS Plan", key="create_eds_modal")
modal_load_master = Modal("Load Master", key="load_master_modal")
modal_load_eds = Modal("Load EDS Plan", key="load_eds_modal")
modal_save_master = Modal("Save Master", key="save_master_modal")
modal_save_eds = Modal("Save EDS Plan", key="save_eds_modal")


def modal_action():
    # create 
    if modal_create_master.is_open():
        with modal_create_master.container():
            st.warning("미완성 상태입니다.", icon="⛔")
            _, c2 = st.columns([3, 1])
            if c2.button("신규 마스터 생성", use_container_width=True):
                create_master()
                modal_create_master.close()

    if modal_create_eds.is_open():
        with modal_create_eds.container():
            st.warning("미완성 상태입니다.", icon="⛔")
            _, c2 = st.columns([3, 1])
            if c2.button("빈 테이블 생성", use_container_width=True):
                create_eds()
                modal_create_eds.close()

    # load
    if modal_load_master.is_open():
        with modal_load_master.container():
            mode = st.radio("모드", [f"{st.session_state["username"]}님 개인", "공용"], label_visibility="collapsed", horizontal=True)
            if mode == "공용":
                options = df_version.loc[(df_version["id"].isin(st.session_state["sel_master_ver_id"])) & (df_version["catetory"] == "public")]
                options = get_version_string(options)
                st.selectbox("선택", options, key="sel_public", label_visibility="hidden")
                st.markdown("")
                _, c2 = st.columns([3, 1])
                if c2.button("📂 공용 버전 열기", use_container_width=True):
                    ver_id = get_selected_ver_id(st.session_state["sel_public"])
                    load_master_ver(ver_id)
                    modal_load_master.close()
            else:
                options = df_version.loc[(df_version["id"].isin(st.session_state["sel_master_ver_id"])) & (df_version["user_id"] == st.session_state["user_id"]) & (df_version["catetory"] == "private")]
                options = get_version_string(options)
                st.selectbox("선택", options, key="sel_private", label_visibility="hidden")
                st.markdown("")
                _, c2 = st.columns([3, 1])
                if c2.button("📂 개인 버전 열기", use_container_width=True):
                    ver_id = get_selected_ver_id(st.session_state["sel_private"])
                    load_master_ver(ver_id)
                    modal_load_master.close()                

    if modal_load_eds.is_open():
        with modal_load_eds.container():
            options = df_version.loc[df_version["catetory"] == "eds"]
            options = get_version_string(options)
            st.selectbox("선택", options, key="sel_eds", label_visibility="hidden")
            st.markdown("")
            _, c2 = st.columns([3, 1])
            if c2.button("📂 공용 버전 열기", use_container_width=True):
                ver_id = get_selected_ver_id(st.session_state["sel_eds"])
                load_eds_ver(ver_id)
                modal_load_eds.close()

    # save
    if modal_save_master.is_open():
        with modal_save_master.container():
            st.warning("미완성 상태입니다.", icon="⛔")
            mode = st.radio("모드", [f"{st.session_state["username"]}님 개인", "공용"], label_visibility="collapsed", horizontal=True)
            if mode == "공용":
                st.text_input("입력", placeholder="버전 코멘트 입력", label_visibility="hidden")
                st.markdown("")
                _, c2 = st.columns([3, 1])
                if c2.button("💾 공용 버전 저장", use_container_width=True):
                    save_master()
                    modal_save_master.close()
            else:
                st.text_input("입력", placeholder="버전 코멘트 입력", label_visibility="hidden")
                st.markdown("")
                _, c2 = st.columns([3, 1])
                if c2.button("💾 개인 버전 저장", use_container_width=True):
                    save_master()
                    modal_save_master.close()

    if modal_save_eds.is_open():
        with modal_save_eds.container():
            st.warning("미완성 상태입니다.", icon="⛔")
            st.text_input("입력", placeholder="버전 코멘트 입력", label_visibility="hidden")
            st.markdown("")
            _, c2 = st.columns([3, 1])
            if c2.button("💾 공용 버전 저장", use_container_width=True):
                save_eds()
                modal_save_eds.close()