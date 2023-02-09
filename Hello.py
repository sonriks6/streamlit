import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
# import pydeck as pdk
import streamlit as st # web development
import time # to simulate a real time data, time loop 
# import plotly.express as px # interactive charts 
import pickle
import datetime

st.set_page_config(
   page_title = 'Wildfire Dashboard',
   page_icon = '🔥',
   layout = 'centered'
)

# Dashboard title
st.title("Wildfire Dashboard DataViz")
st.markdown("Here we show data insights collected from 1992 to 2015:")

# Dataset we need to import
DATA_URL = ("https://raw.githubusercontent.com/sonriks6/streamlit/main/wildfire_compressed.parquet")

@st.cache(persist = True)
def load_data():
   data = pd.read_parquet(DATA_URL)
   return data

# Load entire dataset
data = load_data()

# plot a streamlit map
st.header("Move the sliders to visualize fires per year and category [A - G]:")
# plot the sliders
year = st.slider("Year:", 1992, 2015)
fire_class_options = ["A", "B", "C", "D", "E", "F", "G"]
default_option=fire_class_options.index("A")
fire_class = st.selectbox(":fire:", options=fire_class_options, index=default_option)
st.map(data.query("(FIRE_YEAR == @year) & (FIRE_SIZE_CLASS == @fire_class)")[["LATITUDE", "LONGITUDE"]].dropna(how ="any"))