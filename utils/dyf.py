import streamlit as st


def load_master():
    st.session_state["main_view"] = "main"


def load_eds():
    st.session_state["main_view"] = "eds"


def create_master():
    st.session_state["main_view"] = "main"


def create_eds():
    st.session_state["main_view"] = "eds"


def save_master():
    st.session_state["main_view"] = "main"


def save_eds():
    st.session_state["main_view"] = "eds"