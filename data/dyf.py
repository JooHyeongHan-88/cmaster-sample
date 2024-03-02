import streamlit as st
from datetime import datetime
import pandas as pd


df_version = pd.DataFrame({
    "catetory": ["public", "public", "private", "private", "eds", "eds"],
    "create_date": [datetime.strptime("2024-02-01 12:00:00", "%Y-%m-%d %H:%M:%S"), datetime.strptime("2024-03-01 12:00:00", "%Y-%m-%d %H:%M:%S"),
                    datetime.strptime("2024-02-01 00:00:00", "%Y-%m-%d %H:%M:%S"), datetime.strptime("2024-03-01 00:00:00", "%Y-%m-%d %H:%M:%S"),
                    datetime.strptime("2024-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"), datetime.strptime("2024-02-01 00:00:00", "%Y-%m-%d %H:%M:%S")],
    "comment": ["ver 1.0", "ver 2.0", "임시 ver 1", "임시 ver 2", "1월", "2월"],
    "username": ["한주형", "한주형", "한주형", "한주형", "한주형", "한주형"]
})

df_master = pd.DataFrame({
    "master_name": ["A 제품", "B 제품", "C 제품"],
    "partid_search": ["AAA", "BBB", "CCC"]
})

df_item = pd.DataFrame({
    "item": ["아이템 A1", "아이템 A2", "아이템 A3", "아이템 B1", "아이템 B2"],
    "description": ["아이템 A1 입니다.", "아이템 A2 입니다.", "아이템 A4 입니다.", "아이템 B1 입니다.", "아이템 B2 입니다."],
    "master_name": ["A 제품", "A 제품", "A 제품", "B 제품", "B 제품"]
})

df_condition = pd.DataFrame({
    "step_seq": ["AAA1", "AAA1", "AAA1", "AAA2-1", "AAA2-2", "AAA3", "BBB1"],
    "operator": [">", "=", "LIKE", "<", "=", "LIKE", "<"],
    "condition": ["조건 A1-1", "조건 A1-2", "조건 A1-3", "조건 A2-1-1", "조건 A2-2-1", "조건 A3-1", "조건 B1-1"],
    "item": ["아이템 A1", "아이템 A1", "아이템 A1", "아이템 A2", "아이템 A2", "아이템 A3", "아이템 B1"]
})

df_eds = pd.DataFrame({
    "X1": ["(1, 1)", "(2, 1)"],
    "X2": ["(1, 2)", "(2, 2)"],
    "X3": ["(1, 3)", "(2, 3)"],
    "X4": ["(1, 4)", "(2, 4)"]
})

sel_operator = st.column_config.SelectboxColumn(
    options=["<", ">", "=", "LIKE"],
    required=True
)

sel_master_public = ["ver 1.0.0", "ver 2.0.0", "ver 3.0.0"]
sel_master_private = ["ver 0.0.1", "ver 0.0.2", "ver 0.0.3"]
sel_eds_public = ["ver 1.1.0", "ver 2.1.0", "ver 3.1.0"]
sel_eds_private = ["ver 0.1.1", "ver 0.2.1", "ver 0.3.1"]

sel_master_name = sorted(list(set(df_master["master_name"])))