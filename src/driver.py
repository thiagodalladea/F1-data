import streamlit as st
import pandas as pd
import os

df_drivers = pd.read_csv("./data/drivers/F1DriversDataset.csv")


def get_drivers():
    global df_drivers

    return df_drivers["Driver"].sort_values().values


def get_driver_info(driver):
    global df_drivers

    return df_drivers.loc[df_drivers.Driver == driver]


st.write("""
    # Driver Stats
""")

drivers = get_drivers()
option = st.selectbox(
    "***Select the driver***",
    drivers,
    index=None,
    placeholder="Driver (alphabetic order)",
)

df_driver_info = get_driver_info(option)
archives = []
df_qualifying = pd.DataFrame()

if not df_driver_info.empty:
    name = df_driver_info["Driver"].iloc[0]
    seasons = df_driver_info["Seasons"].iloc[0].split(",")
    for season in seasons:
        season = season.strip()
        directory = (
            "./data/qualifying_race_results/" + str(season) + "/Qualifying Results/"
        )
        archive = os.listdir(directory)
        for arch in archive:
            directory = (
                "./data/qualifying_race_results/"
                + str(season)
                + "/Qualifying Results/"
                + str(arch)
            )
            if df_qualifying.empty:
                df_qualifying = pd.read_csv(directory)
            else:
                df_qualifying = pd.concat(
                    [df_qualifying, pd.read_csv(directory)], axis=0
                )
    df = df_qualifying.loc[df_qualifying.Driver == option].reset_index(drop=True)
    st.write(df)

else:
    st.write("No information available.")
