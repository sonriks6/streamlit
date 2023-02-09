import streamlit as st
import pickle
import pandas as pd
import numpy as np
import datetime
import time

# loading the trained model
pickle_in = open('clf_rf.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(YEAR, DOY, LATITUDE, LONGITUDE, FIRE_SIZE):  
   
    prediction = classifier.predict(
        [[YEAR, DOY, LATITUDE, LONGITUDE, FIRE_SIZE, 100000, 36000, 20]])
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
    
    col1, col2 = st.columns(2)

    with col1:
        LATITUDE = st.text_input("LATITUDE", "38.5")
        LONGITUDE = st.text_input("LONGITUDE", "-120.1")
        PICK_DATE = st.date_input("Date:", min_value=datetime.date(1992, 1, 1), value=datetime.date.today())
    
    with col2:
        FIRE_SIZE_CLASS = st.radio(
            "Fire Size Class (in Acres):", 
            ("A - 0 to 0.25", "B - 0.26 to 9.9", "C - 10 to 99.9", "D - 100 to 299", "E - 300 to 999", "F - 1000 to 4999", "G - 5000+")
            )
        st.caption("Source: NWCG Standards")

    result ="?"
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        YEAR = PICK_DATE.year
        DISCOVERY_DOY = PICK_DATE.timetuple().tm_yday
        if FIRE_SIZE_CLASS == "A - 0 to 0.25":
            FIRE_SIZE_CLASS=0.1
        elif FIRE_SIZE_CLASS == "B - 0.26 to 9.9":
            FIRE_SIZE_CLASS=5
        elif FIRE_SIZE_CLASS == "C - 10 to 99.9":
            FIRE_SIZE_CLASS=50
        elif FIRE_SIZE_CLASS == "D - 100 to 299":
            FIRE_SIZE_CLASS=150
        elif FIRE_SIZE_CLASS == "E - 300 to 999":
            FIRE_SIZE_CLASS=500
        elif FIRE_SIZE_CLASS == "F - 1000 to 4999":
            FIRE_SIZE_CLASS=2500
        elif FIRE_SIZE_CLASS == "G - 5000+":
            FIRE_SIZE_CLASS=5000
        else:
            FIRE_SIZE_CLASS=10000

        result = prediction(YEAR, DISCOVERY_DOY, LATITUDE, LONGITUDE, FIRE_SIZE_CLASS)
        if result==1:
            result="natural"
        elif result==2:
            result="accidental"
        else:
            result="malicious"
    st.success('The cause is {}'.format(result))
     
if __name__=='__main__':
    main()
