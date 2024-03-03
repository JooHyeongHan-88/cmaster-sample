import streamlit as st
from datetime import datetime
import pandas as pd


df_user = pd.DataFrame({
    "id": ["hanjoo88.han", "hd81.lee"],
    "username": ["한주형", "이호동"]
})

df_version = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6],
    "catetory": ["public", "public", "public", "private", "eds", "eds"],
    "create_date": [datetime.strptime("2024-02-01 12:00:00", "%Y-%m-%d %H:%M:%S"), datetime.strptime("2024-03-01 12:00:00", "%Y-%m-%d %H:%M:%S"),
                    datetime.strptime("2024-02-01 00:00:00", "%Y-%m-%d %H:%M:%S"), datetime.strptime("2024-03-01 00:00:00", "%Y-%m-%d %H:%M:%S"),
                    datetime.strptime("2024-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"), datetime.strptime("2024-02-01 00:00:00", "%Y-%m-%d %H:%M:%S")],
    "comment": ["A 공용 ver 1.0", "A 공용 ver 2.0", "B 공용 ver 1.0", "A 개인 ver 1.0", "1월 계획", "2월 계획"],
    "user_id": ["hanjoo88.han", "hanjoo88.han", "hd81.lee", "hd81.lee", "hanjoo88.han", "hanjoo88.han"]
})

df_master = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "master_name": ["A 제품", "A 제품", "B 제품", "A 제품"],
    "partid_search": ["AAA", "AAA", "BBB", "AAA"],
    "ver_id": [1, 2, 3, 4]
})

df_item = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "item": ["아이템 A1", "아이템 A2", "아이템 A3", "아이템 A1", "아이템 A2", "아이템 B1", "아이템 B2", "아이템 B3", "아이템 A1 (개인)", "아이템 A2 (개인)"],
    "description": ["아이템 A1 입니다.", "아이템 A2 입니다.", "아이템 A3 입니다.", "아이템 A1 입니다. (ver 2.0)", "아이템 A2 입니다. (ver 2.0)",
                    "아이템 B1 입니다.", "아이템 B2 입니다.", "아이템 B3 입니다.", "아이템 A1 입니다. (개인)", "아이템 A2 입니다. (개인)"],
    "master_name": ["A 제품", "A 제품", "A 제품", "A 제품", "A 제품", "B 제품", "B 제품", "B 제품", "A 제품", "A 제품"],
    "ver_id": [1, 1, 1, 2, 2, 3, 3, 3, 4, 4]
})

df_condition = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16],
    "step_seq": ["AAA1", "AAA1", "AAA1", "AAA2", "AAA2", "AAA3", "AAA1", "AAA2", "AAA3", "BBB1", "BBB2", "BBB2", "BBB3", "AAA1", "AAA2", "AAA3"],
    "operator": [">", "=", "LIKE", "<", "=", "LIKE", "<", ">", "=", "LIKE", "<", "=", "LIKE", "<", "=", "LIKE"],
    "condition": ["조건 A1-1", "조건 A1-2", "조건 A1-3", "조건 A2-1", "조건 A2-2", "조건 A3",
                  "조건 A1", "조건 A2", "조건 A3", "조건 B1", "조건 B2-1", "조건 B2-2", "조건 B3", "조건 A1-1", "조건 A1-2", "조건 A2"],
    "item_id": [1, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10]
})

df_eds = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "X1": ["(1, 1)", "(2, 1)", "(1, 1)-2", "(2, 1)-2"],
    "X2": ["(1, 2)", "(2, 2)", "(1, 2)-2", "(2, 2)-2"],
    "X3": ["(1, 3)", "(2, 3)", "(1, 3)-2", "(2, 3)-2"],
    "X4": ["(1, 4)", "(2, 4)", "(1, 4)-2", "(2, 4)-2"],
    "ver_id": [5, 5, 6, 6]
})

sel_operator = st.column_config.SelectboxColumn(
    options=["<", ">", "=", "LIKE"],
    required=True
)

sel_master_name = sorted(list(set(df_master["master_name"])))