import streamlit as st
import pandas as pd
import numpy as np

# Dashboard title
st.title("Wildfire Dashboard DataViz")
st.markdown("Here we show data insights collected from 1992 to 2015:")

# Dataset we need to import
DATA_URL = ("https://raw.githubusercontent.com/sonriks6/streamlit/main/wildfire_compressed.parquet")

@st.cache(persist = True, allow_output_mutation=True)
def load_data():
   data = pd.read_parquet(DATA_URL)
   return data

# Load entire dataset
data = load_data()

# plot a streamlit map
st.header("Move the sliders to visualize fires per year combined with category [A - G]:")
# plot the sliders
# year = st.slider("Year:", 1992, 2015)
year_start, year_end = st.select_slider(
    label="Select period of years:",
    options=np.arange(1992,2016),
    value=(1992,2015)
)

fire_class_options = ["A", "B", "C", "D", "E", "F", "G"]
default_option=fire_class_options.index("A")
fire_class = st.selectbox(":fire:", options=fire_class_options, index=default_option)
st.map(data.query("(FIRE_YEAR >= @year_start & FIRE_YEAR <= @year_end) & (FIRE_SIZE_CLASS == @fire_class)")[["LATITUDE", "LONGITUDE"]].dropna(how ="any"))