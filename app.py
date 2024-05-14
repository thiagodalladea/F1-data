import streamlit as st
from st_pages import Page, show_pages


show_pages(
    [
        Page("app.py", "Home"),
        Page("src/versus.py", "Versus"),
        Page("src/driver.py", "Driver Stats"),
    ]
)

st.write("""
    # Home
""")
