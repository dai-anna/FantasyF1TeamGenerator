import streamlit as st
import datetime
import requests

st.sidebar.subheader("Inputs")

date = st.sidebar.date_input("Start Date", datetime.date(2022, 1, 1))
st.header

payload = {}
