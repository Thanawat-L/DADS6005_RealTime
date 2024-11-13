import streamlit as st
from pinotdb import connect
import numpy as np
import pandas as pd
import plotly.express as px

conn = connect(host = '47.129.162.84', port = 8099, path = '/query/sql', schema = 'http')

# DataFrame_01
curs_01 = conn.cursor()
query_01 = """SELECT * FROM game_users_tumbling_window_topic LIMIT 100000"""

curs_01.execute(query_01)
result_01 = curs_01.fetchall()
df_01 = pd.DataFrame(result_01, columns =['GAME_NAME','GENRE','PAGE_ID','PLATFORM','PUBLISHER','RATING_COUNT','WINDOWEND','WINDOWSTART','WINDOW_END','WINDOW_START','YEAR','timestamp'])
df_01['timestamp'] = pd.to_datetime(df_01['timestamp'], unit='ms')

pd.set_option('future.no_silent_downcasting', True)

df_01 = df_01.replace("null", np.nan).replace(0, np.nan)
df_01 = df_01.infer_objects(copy=False)
df_01 = df_01.dropna(subset=[col for col in df_01.columns if col not in ['PAGE_ID', 'WINDOWEND', 'WINDOWSTART']])

# Streamlit layout
st.title("Game Sales Analysis")

