import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber Data")

DATE_COLUMN = 'date/time'

# Load CSV file into pd


@st.cache
def load_data(nrows):
    data = pd.read_csv("uber-raw-data-sep14.csv", nrows=nrows)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


data_load_state = st.text("Loading data...")
data = load_data(1000)
data_load_state.text("Loading data...done! (Cached)")

st.subheader('Raw data')
st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]

st.bar_chart(hist_values)
