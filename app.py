import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Plot Digitizer", layout="wide")

st.title("Plot Digitizer Tool")
st.caption("Upload image → Set axis values → Calibrate 4 points → Click to extract data")

# EASIEST: keep your HTML in a separate file and load it
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=950, scrolling=True)
