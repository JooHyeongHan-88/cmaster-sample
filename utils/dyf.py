import streamlit as st
import pandas as pd

from typing import List, Optional, Literal
from datetime import datetime
import re

from data.dyf import df_version, df_master, df_item, df_eds


def set_selected_master_ver_id() -> None:
    ver_id: List[int] = df_master[df_master["master_name"] == st.session_state["selected_master"]]["ver_id"]

    df = df_version[df_version["id"].isin(ver_id)].sort_values(by='create_date', ascending=False)

    st.session_state["sel_master_ver_id"] = df["id"]
    st.session_state["newest_master_ver_id"] = df.iloc[0]['id']


def set_newest_eds_ver_id() -> None:
    ver_id: List[int] = df_eds["ver_id"]

    df = df_version[df_version["id"].isin(ver_id)].sort_values(by='create_date', ascending=False)

    st.session_state["newest_eds_ver_id"] = df.iloc[0]['id']


def get_version_string(df: pd.DataFrame) -> List[str]:
    if len(df) > 0:
        ver_str = '[' + df['create_date'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S')) + '] ' + df['comment']
        ver_str = ver_str.tolist()
        return ver_str
    else:
        return []


def get_selected_ver_id(ver_string: str) -> int:
    match = re.match(r'\[(.*?)\]\s*(.*)', ver_string)

    create_date = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S')
    comment = match.group(2)

    ver_id = df_version[(df_version["create_date"] == create_date) & (df_version["comment"] == comment)].iloc[0]["id"]

    return ver_id


def get_item_id(item: Optional[str] = None) -> Optional[int]:
    
    try:
        item_id = df_item[
            (df_item["ver_id"] == st.session_state["current_master_ver_id"]) &
            (df_item["item"] == item)
        ].iloc[0]["id"]
    except:
        item_id = None

    return item_id


def load_master_newest() -> None:
    df_master_sub: pd.DataFrame = df_master[df_master["ver_id"] == st.session_state["newest_master_ver_id"]].reset_index(drop=True).drop(["id", "ver_id"], axis=1)
    df_item_sub: pd.DataFrame = df_item[df_item["ver_id"] == st.session_state["newest_master_ver_id"]].reset_index(drop=True).drop(["id", "master_name", "ver_id"], axis=1)
    
    st.session_state["df_master_view"] = df_master_sub
    st.session_state["df_item_view"] = df_item_sub

    st.session_state["current_master_ver_id"] = st.session_state["newest_master_ver_id"]

    st.session_state["main_view"] = "master"


def load_eds_newest() -> None:

    st.session_state["df_eds_view"] = df_eds[df_eds["ver_id"] == st.session_state["newest_eds_ver_id"]].reset_index(drop=True).drop(["id", "ver_id"], axis=1)

    st.session_state["current_eds_ver_id"] = st.session_state["newest_eds_ver_id"]

    st.session_state["main_view"] = "eds"


def load_master_ver(ver_id: int) -> None:
    df_master_sub = df_master[df_master["ver_id"] == ver_id].reset_index(drop=True).drop(["id", "ver_id"], axis=1)
    df_item_sub = df_item[df_item["ver_id"] == ver_id].reset_index(drop=True).drop(["id", "master_name", "ver_id"], axis=1)
    
    st.session_state["df_master_view"] = df_master_sub
    st.session_state["df_item_view"] = df_item_sub

    st.session_state["current_master_ver_id"] = ver_id

    st.session_state["main_view"] = "master"


def load_eds_ver(ver_id: int) -> None:
    st.session_state["df_eds_view"] = df_eds[df_eds["ver_id"] == ver_id].reset_index(drop=True).drop(["id", "ver_id"], axis=1)

    st.session_state["current_eds_ver_id"] = ver_id

    st.session_state["main_view"] = "eds"


def create_master(master_name: str, partid_search: str) -> None:
    st.session_state["df_master_view"] = pd.DataFrame({
        "master_name": [master_name],
        "partid_search": [partid_search]
    })
    st.session_state["df_item_view"] = df_item.iloc[0:0].drop(["id", "master_name", "ver_id"], axis=1)

    st.session_state["main_view"] = "master"


def create_eds() -> None:
    st.session_state["df_eds_view"] = df_eds.iloc[0:0].drop(["id", "ver_id"], axis=1)

    st.session_state["main_view"] = "eds"


def save_master(comment: str, mode: Literal["public", "private"]) -> None:
    st.divider()

    st.info(f"({mode}) [{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {comment}")
    
    st.subheader("Master")
    st.dataframe(st.session_state["view_master"], hide_index=True)

    st.subheader("Items")
    st.dataframe(st.session_state["view_item"], hide_index=True)

    st.subheader("Conditions")
    for editor_condition in st.session_state["view_condition"].values():
        st.write("조건")
        st.dataframe(editor_condition, hide_index=True)

    st.session_state["main_view"] = "master"


def save_eds(comment: str) -> None:
    st.divider()

    st.info(f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {comment}")
    
    st.subheader("EDS Test Plan")
    st.dataframe(st.session_state["view_eds"], hide_index=True)

    st.session_state["main_view"] = "eds"