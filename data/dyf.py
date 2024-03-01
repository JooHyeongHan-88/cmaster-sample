import streamlit as st

import pandas as pd


df_master = pd.DataFrame({
    "master_name": [None],
    "partid_search": [None]
})

df_item = pd.DataFrame({
    "item": [None],
    "description": [None]
})

df_condition = pd.DataFrame({
    "item": [None],
    "step_seq": [None],
    "operator": [None],
    "condition": [None]
})

df_eds = pd.DataFrame({
    "X1": [None],
    "X2": [None],
    "X3": [None],
    "X4": [None]
})

sel_operator = st.column_config.SelectboxColumn(
    options=["<", ">", "=", "LIKE"],
    required=True
)

sel_master_public = ["ver 1.0.0", "ver 2.0.0", "ver 3.0.0"]
sel_master_private = ["ver 0.0.1", "ver 0.0.2", "ver 0.0.3"]
sel_eds_public = ["ver 1.1.0", "ver 2.1.0", "ver 3.1.0"]
sel_eds_private = ["ver 0.1.1", "ver 0.2.1", "ver 0.3.1"]