import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import pydeck as pdk
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 

# Dataset we need to import

DATA_URL = ("https://raw.githubusercontent.com/sonriks6/streamlit/main/Wildfire_cleaned_dataset_2010_2015.csv")

st.set_page_config(
   page_title = 'Wildfire Dashboard',
   page_icon = '✅',
   layout = 'wide'
)

# dashboard title

st.title("Wildfire Dashboard")
st.markdown("This app analyzes US wildfires from 2010 to 2015")

@st.cache(persist = True)
def load_data():
   data = pd.read_csv(DATA_URL)
   return data


data = load_data()

# Plot : 1
# plot a streamlit map for accident locations.
st.header("Where are the most people casualties in accidents in UK?")
# plot the slider that selects number of person died
casualties = st.slider("Number of persons died", 1, int(data["DISCOVERY_DOY"].max()))
st.map(data.query("DISCOVERY_DOY >= @casualties")[["LATITUDE", "LONGITUDE"]].dropna(how ="any"))
 
# # Plot : 2
# # plot a pydeck 3D map for the number of accident's happen between an hour interval
# st.header("How many accidents occur during a given time of day?")
# hour = st.slider("Hour to look at", 0, 23)
# original_data = data
# data = data[data['date / time'].dt.hour == hour]
 
# st.markdown("Vehicle collisions between % i:00 and % i:00" % (hour, (hour + 1) % 24))
# midpoint = (np.average(data["latitude"]), np.average(data["longitude"]))
 
# st.write(pdk.Deck(
#     map_style ="mapbox://styles / mapbox / light-v9",
#     initial_view_state ={
#       "latitude": midpoint[0],
#       "longitude": midpoint[1],
#       "zoom": 11,
#       "pitch": 50,
#     },
#     layers =[
#         pdk.Layer(
#         "HexagonLayer",
#         data = data[['date / time', 'latitude', 'longitude']],
#         get_position =["longitude", "latitude"],
#         auto_highlight = True,
#         radius = 100,
#         extruded = True,
#         pickable = True,
#         elevation_scale = 4,
#         elevation_range =[0, 1000],
#         ),
#     ],
# ))
 
# # Plot : 3
# # plot a histogram for minute of the hour atwhich accident happen
# st.subheader("Breakdown by minute between % i:00 and % i:00" % (hour, (hour + 1) % 24))
# filtered = data[
#     (data['date / time'].dt.hour >= hour) & (data['date / time'].dt.hour < (hour + 1))
# ]
# hist = np.histogram(filtered['date / time'].dt.minute, bins = 60, range =(0, 60))[0]
# chart_data = pd.DataFrame({"minute": range(60), "Accidents": hist})
# fig = px.bar(chart_data, x ='minute', y ='Accidents', hover_data =['minute', 'Accidents'], height = 400)
# st.write(fig)
 
# # The code below uses checkbox to show raw data
# st.header("Condition of Road at the time of Accidents")
# select = st.selectbox('Weather ', ['Dry', 'Wet / Damp', 'Frost / ice', 'Snow', 'Flood (Over 3cm of water)'])
 
# if select == 'Dry':
#     st.write(original_data[original_data['road_surface_conditions']=="Dry"][["weather_conditions", "light_conditions", "speed_limit", "number_of_casualties"]].sort_values(by =['number_of_casualties'], ascending = False).dropna(how ="any"))
 
# elif select == 'Wet / Damp':
#     st.write(original_data[original_data['road_surface_conditions']=="Wet / Damp"][["weather_conditions", "light_conditions", "speed_limit", "number_of_casualties"]].sort_values(by =['number_of_casualties'], ascending = False).dropna(how ="any"))
# elif select == 'Frost / ice':
#     st.write(original_data[original_data['road_surface_conditions']=="Frost / ice"][["weather_conditions", "light_conditions", "speed_limit", "number_of_casualties"]].sort_values(by =['number_of_casualties'], ascending = False).dropna(how ="any"))
 
# elif select == 'Snow':
#     st.write(original_data[original_data['road_surface_conditions']=="Snow"][["weather_conditions", "light_conditions", "speed_limit", "number_of_casualties"]].sort_values(by =['number_of_casualties'], ascending = False).dropna(how ="any"))
 
# else:
#     st.write(original_data[original_data['road_surface_conditions']=="Flood (Over 3cm of water)"][["weather_conditions", "light_conditions", "speed_limit", "number_of_casualties"]].sort_values(by =['number_of_casualties'], ascending = False).dropna(how ="any"))
 
 
# if st.checkbox("Show Raw Data", False):
#     st.subheader('Raw Data')
#     st.write(data)