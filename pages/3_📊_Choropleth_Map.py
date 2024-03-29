import streamlit as st
import pandas as pd
import numpy as np
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# Dashboard title
st.title("Wildfire Dashboard DataViz")
st.markdown("Here we show data insights collected from 1992 to 2015:")

# Slider to select period of time
# year = st.slider("Year:", 1992, 2015, 2000, 1)

year_start, year_end = st.select_slider(
    label="Select period of years:",
    options=np.arange(1992,2016),
    value=(1992,2015)
)

# Dataset we need to import
DATA_URL = ("https://raw.githubusercontent.com/sonriks6/streamlit/main/wildfire_compressed.parquet")

@st.cache(persist = True, allow_output_mutation=True)
def load_data():
   data = pd.read_parquet(DATA_URL)
   return data

# Load entire dataset
df = load_data()

# Properly format the FIPS code
df["FIPS_COMPLETE"] = df.COUNTY_FIPS2.astype(str).str.zfill(5)

df = df[(df.FIRE_YEAR>=year_start) & (df.FIRE_YEAR<=year_end)]

df_FIPS = df.groupby(["FIPS_COMPLETE"], as_index=False)["FIRE_SIZE"].count()

import plotly.express as px

fig = px.choropleth_mapbox(df_FIPS, geojson=counties, locations='FIPS_COMPLETE', color='FIRE_SIZE',
                           color_continuous_scale="peach",
                           range_color=(0, df_FIPS.FIRE_SIZE.mean() * 2),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={
                              'FIRE_SIZE':'Count of FIRES',
                              'FIPS_COMPLETE':'County FIPS'
                              }
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()

st.plotly_chart(fig, use_container_width=True)