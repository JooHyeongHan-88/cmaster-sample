import streamlit as st
import pandas as pd

from data.dyf import df_master, df_item


def load_master():
    df_master_sub: pd.DataFrame = df_master[df_master["master_name"] == st.session_state["selected_master"]].reset_index(drop=True)
    df_item_sub: pd.DataFrame = df_item[df_item["master_name"] == st.session_state["selected_master"]].reset_index(drop=True).drop("master_name", axis=1)
    
    st.session_state["df_master_view"] = df_master_sub
    st.session_state["df_item_view"] = df_item_sub

    st.session_state["main_view"] = "master"


def load_eds():
    st.session_state["main_view"] = "eds"


def create_master():
    st.session_state["main_view"] = "master"


def create_eds():
    st.session_state["main_view"] = "eds"


def save_master():
    st.session_state["main_view"] = "master"


def save_eds():
    st.session_state["main_view"] = "eds"