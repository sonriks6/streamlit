import streamlit as st
from PIL import Image

# Config
st.set_page_config(page_title='Wildfire US', page_icon=':bar_chart:', layout='wide')

# Title
st.title('Wildfire US')

st.write(
    """
    Lorem ipsum...
    """
)

st.subheader('Machine Learning Model')
st.write(
    """
    We've trained a ML model using a cleaned dataset from the original database published in Kaggle (https://www.kaggle.com/datasets/rtatman/188-million-us-wildfires)
    before that, we've added County, Population and Area information and also the mean temperature per County level.

    The ML model uses a Random Forest Classifier with an accuracy of 70% (n_estimatiors=10) that could be improved up to 80%
    if we increase the number of iterations but would overflow the size of the serialized output.
    """
)

st.subheader('Map Visualization')
st.write(
    """
    For this Map we were able to compress the complete dataset to fit under the limitations of Github and Streamlit (200 Mb).
    Sliders help to select and trim points in the map per year and NWCG class of fires, using all the historic data available
    from 1992 to 2015.
    """
)

c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Data Analyst: CECILE SINNA**', icon="💡")
with c2:
    st.info('**Data Analyst: JEAN CHRISTOPHE THEAULT**', icon="💻")
with c3:
    st.info('**Data Analyst: SANTIAGO RODRIGUEZ DIAZ**', icon="🧠")