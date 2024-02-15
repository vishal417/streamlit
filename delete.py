import streamlit as st
import pandas as pd
import numpy as np
from streamlit_gsheets import GSheetsConnection

def app():
    st.markdown("Select a Prospect and update their details.")
    conn = st.connection("gsheets", type=GSheetsConnection)

    df = conn.read(worksheet="Sheet1", usecols=list(range(20)),ttl=5)
    df=df.dropna(how="all")
    prospect_ids = df["Prospect_ID"].tolist()
    Prospect_to_update = st.selectbox("Select a Prospect to Update", options=prospect_ids)
    Prospect_data = df[df["Prospect_ID"] == Prospect_to_update].iloc[0]

    if st.button("Delete"):
        df.drop(
            df[df["Prospect_ID"] == Prospect_to_update].index,
            inplace=True,
        )
        conn.update(worksheet="Sheet1", data=df)
        st.success("Vendor successfully deleted!")