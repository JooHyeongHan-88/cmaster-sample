import streamlit as st

from components.navigation import navigation
from components.modal import (
    modal_create_master, modal_load_master, modal_save_master,
    modal_create_eds, modal_load_eds, modal_save_eds,
    modal_action
)
from utils.dyf import (
    load_master_newest, load_eds_newest,
    set_selected_master_ver_id, set_newest_eds_ver_id, get_item_id
)
from data.dyf import df_condition, sel_master_name, sel_operator


# Initialize ---------------------------------------------------------------------------------

st.session_state["current_page"] = "DYF"
st.session_state["current_page_path"] = "pages/dyf.py"

if "main_view" not in st.session_state:
    st.session_state["main_view"] = "default"


# Main ---------------------------------------------------------------------------------------

# navigation
navigation()

# sidebar
with st.sidebar:
    st.divider()

    # DBKM Master
    st.subheader("DBKM Master")
    
    if st.button("✒️ Create New Master", key="create_master", type="primary", use_container_width=True):
        modal_create_master.open()

    st.selectbox("Select", options=sel_master_name, key="selected_master", label_visibility='collapsed', on_change=set_selected_master_ver_id)

    set_selected_master_ver_id()

    c1, c2 = st.columns([3, 2])
    if c1.button("✨ 최신 버전", key="master_load_newest", use_container_width=True):
        load_master_newest()
    if c2.button("버전 선택", key="master_load_ver", use_container_width=True):
        modal_load_master.open()

    st.markdown("")

    # EDS Test Plan
    st.subheader("EDS Test Plan")
    
    if st.button("✒️ Create New EDS Test Plan", key="create_eds", type="primary", use_container_width=True):
        modal_create_eds.open()
    
    set_newest_eds_ver_id()

    c1, c2 = st.columns([3, 2])
    if c1.button("✨ 최신 버전", key="eds_load_newest", use_container_width=True):
        load_eds_newest()
    if c2.button("버전 선택", key="eds_load_ver", use_container_width=True):
        modal_load_eds.open()

# main
if st.session_state["main_view"] == "default":
    st.title("DYF")
    st.divider()
    st.info("DBKM Yield Forecast를 위한 기준 정보 버전 관리 Appication입니다.", icon="ℹ️")

elif st.session_state["main_view"] == "master":
    st.title("DBKM Master")
    _, c2 = st.columns([5, 1])
    if c2.button("✔️ Save", type='primary', use_container_width=True):
        modal_save_master.open()

    t1, t2, t3 = st.tabs(["master", "master_item", "condition"])
    with t1:
        st.session_state["view_master"] = st.data_editor(st.session_state["df_master_view"], hide_index=True)

    with t2:
        st.session_state["view_item"] = st.data_editor(st.session_state["df_item_view"], key="editor_item", num_rows='dynamic', hide_index=True)

    with t3:
        item_list = st.session_state["view_item"]["item"]
        st.session_state["view_condition"] = {}
        if len(item_list) > 0:
            for i, item in enumerate(item_list):
                st.markdown(f"**{item}**")
                if i in st.session_state["editor_item"]['edited_rows'].keys():
                    item = st.session_state["df_item_view"].iloc[i]["item"]
                item_id = get_item_id(item)
                df_condition_sub = df_condition[df_condition["item_id"] == item_id].reset_index(drop=True).drop(["id", "item_id"], axis=1)
                st.session_state["view_condition"][i] = st.data_editor(df_condition_sub, hide_index=True, num_rows='dynamic', column_config={"operator": sel_operator}, key=i)

elif st.session_state["main_view"] == "eds":
    st.title("EDS Test Plan")   
    _, c2 = st.columns([5, 1])
    if c2.button("✔️ Save", type='primary', use_container_width=True):
        modal_save_eds.open()
    st.session_state["view_eds"] = st.data_editor(st.session_state["df_eds_view"], hide_index=True, num_rows='dynamic')


# Modal Control ------------------------------------------------------------------------------------
    
modal_action()