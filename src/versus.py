import streamlit as st
import pandas as pd

df_drivers = pd.read_csv("./data/drivers/F1DriversDataset.csv")


def get_drivers():
    global df_drivers

    return df_drivers["Driver"].sort_values().values


def get_driver_info(driver):
    global df_drivers

    return df_drivers.loc[df_drivers.Driver == driver]


st.write("""
    # Versus
""")

col1, col2 = st.columns(2, gap="small")

with col1:
    drivers = get_drivers()
    option1 = st.selectbox(
        "***Select the first driver***",
        drivers,
        index=None,
        placeholder="First driver (alphabetic order)",
    )
    driver1 = get_driver_info(option1)

with col2:
    drivers = get_drivers()
    option2 = st.selectbox(
        "***Select the second driver***",
        drivers,
        index=None,
        placeholder="Second driver (alphabetic order)",
    )
    driver2 = get_driver_info(option2)
