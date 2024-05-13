import streamlit as st
import pandas as pd
from st_pages import Page, show_pages


show_pages(
    [
        Page("app.py", "Home"),
        Page("src/versus.py", "Versus"),
    ]
)

st.write("""
    # Home
""")
