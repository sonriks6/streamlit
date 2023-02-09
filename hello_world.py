import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
# import pydeck as pdk
import streamlit as st # web development
import time # to simulate a real time data, time loop 
# import plotly.express as px # interactive charts 
import pickle

st.set_page_config(
   page_title = 'Wildfire Dashboard',
   page_icon = '🔥',
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
fire_class = st.selectbox(":fire:", pd.Series({"A", "B", "C", "D", "E", "F", "G"}))
st.map(data.query("(FIRE_YEAR == @year) & (FIRE_SIZE_CLASS == @fire_class)")[["LATITUDE", "LONGITUDE"]].dropna(how ="any"))