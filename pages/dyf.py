import streamlit as st

from components.navigation import navigation
from components.modal import (
    modal_create_master, modal_load_master, modal_save_master,
    modal_create_eds, modal_load_eds, modal_save_eds,
    modal_action
)
from utils.dyf import load_master, load_eds
from data.dyf import (
    df_condition, df_eds, df_version,
    sel_master_name, sel_operator
)


# Initialize ---------------------------------------------------------------------------------

st.session_state["current_page"] = "DYF"
st.session_state["current_page_path"] = "pages/dyf.py"

if "main_view" not in st.session_state:
    st.session_state["main_view"] = "default"

# if "public_mode_master" not in st.session_state:
#     st.session_state["public_mode_master"] = True

# if "public_mode_eds" not in st.session_state:
#     st.session_state["public_mode_eds"] = True


# Main ---------------------------------------------------------------------------------------

# navigation
navigation()

# sidebar
with st.sidebar:
    st.divider()

    st.subheader("Master")
    if st.button("✒️ Create New Master", key="create_master", type="primary", use_container_width=True):
        modal_create_master.open()
    st.selectbox("Select", options=sel_master_name, key="selected_master", label_visibility='collapsed')
    c1, c2 = st.columns([3, 2])
    if c1.button("✨ 최신 버전 열기", key="master_load_newest", use_container_width=True):
        load_master()
    if c2.button("버전 선택", key="master_load_ver", use_container_width=True):
        modal_load_master.open()

    st.markdown("")

    st.subheader("EDS Test Plan")
    if st.button("✒️ Create New EDS Test Plan", key="create_eds", type="primary", use_container_width=True):
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

elif st.session_state["main_view"] == "master":
    st.title("Master")
    _, c2 = st.columns([11, 1])
    if c2.button("✔️ Save", key="master_save", type='primary', use_container_width=True):
        modal_save_master.open()

    t1, t2, t3 = st.tabs(["master", "master_item", "condition"])

    with t1:
        st.data_editor(st.session_state["df_master_view"], hide_index=True)

    with t2:
        editor_item = st.data_editor(st.session_state["df_item_view"], key="editor_item", num_rows='dynamic', hide_index=True)

    with t3:
        item_list = editor_item["item"]
        if len(item_list) > 0:
            for i in item_list:
                st.markdown(f"**{i}**")
                df_condition_sub = df_condition[df_condition["item"] == i].reset_index(drop=True).drop(["item"], axis=1)
                st.data_editor(df_condition_sub, hide_index=True, num_rows='dynamic', column_config={"operator": sel_operator}, key=i)

elif st.session_state["main_view"] == "eds":
    st.title("EDS Plan")   
    _, c2 = st.columns([11, 1])
    if c2.button("✔️ Save", key="eds_save", type='primary', use_container_width=True):
        modal_save_eds.open()
    st.data_editor(df_eds, hide_index=True, num_rows='dynamic')


# Modal Control ------------------------------------------------------------------------------------
    
modal_action()