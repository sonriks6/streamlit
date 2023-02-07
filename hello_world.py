import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import pydeck as pdk
import streamlit as st # web development
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 
import pickle

st.set_page_config(
   page_title = 'Wildfire Dashboard',
   page_icon = ':-)',
   layout = 'centered'
)

# loading the trained model
pickle_in = open('clf_rf.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(LATITUDE, LONGITUDE):  
   
    prediction = classifier.predict(
        [[2015, 1, LATITUDE, LONGITUDE, 1, 100000, 36000, 20]])
    # print(prediction)
    return prediction


# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("Wildfire Machine Learning Model")
    st.markdown("Here we predict fire cause from location:")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:coral;padding:13px">
    <h1 style ="color:black;text-align:center;">Machine Learning Model</h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    LATITUDE = st.text_input("LATITUDE", "38.5")
    LONGITUDE = st.text_input("LONGITUDE", "-120.1")
    result ="?"
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(LATITUDE, LONGITUDE)
        if result==1:
            result="natural"
        elif result==2:
            result="accidental"
        else:
            result="malicious"
    st.success('The cause is {}'.format(result))
     
if __name__=='__main__':
    main()


# Dashboard title
st.title("Wildfire Dashboard DataViz")
st.markdown("Here we show data insights collected from 2010 to 2015:")

# Dataset we need to import
DATA_URL = ("https://raw.githubusercontent.com/sonriks6/streamlit/main/Wildfire_cleaned_dataset_2010_2015.csv")


@st.cache(persist = True)
def load_data():
   data = pd.read_csv(DATA_URL)
   return data

# Load entire dataset
data = load_data()

# Plot : 1
# plot a streamlit map for accident locations.
st.header("Move the sliders to visualize Fire Size per Year:")
# plot the slider that selects number of person died
year = st.slider("Year:", 2010, 2015)

fire_size_start, fire_size_end = st.select_slider(
    "Select FIRE CLASS:",
    options=["A", "B", "C", "D", "E", "F", "G"],
    value=("A", "G")
)

st.map(data.query("FIRE_YEAR == @year & (FIRE_SIZE_CLASS >= @fire_size_start & FIRE_SIZE_CLASS <= @fire_size_end")[["LATITUDE", "LONGITUDE"]].dropna(how ="any"))



start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)


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
# #     st.write(data)