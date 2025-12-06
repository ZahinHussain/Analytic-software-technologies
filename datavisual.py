import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("nss2025.csv")

tab1, tab2, tab3 = st.tabs(["Overview", "Charts", "Search"])

with tab1:
    st.header("Overview")
    st.write("This is your overview page.")

with tab2:
    st.header("Charts")
    st.write("Matplotlib or Plotly charts go here.")

with tab3:
    st.header("Search")
    st.write("Your search filters and results go here.")
