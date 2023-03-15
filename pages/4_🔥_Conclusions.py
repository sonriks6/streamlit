import streamlit as st
from PIL import Image

# Title
st.title('CONCLUSION')

st.write(
    """
    
    
    """
)
st.subheader('FIRE PROGRESSION:')
st.write(
    """

    Wildfires in the USA are progressing over time (especially in California, Georgia and Texas) 
    as well as their size (Arizona).
    
    The fires are devastating in terms of area (class G is growing by 28% per year) and it is likely 
    that with global warming and very dry summers this number will increase (growth in natural causes of fires).

    """
)
st.subheader('HUMAN CAUSES:')
st.write(
    """

    Construction (e.g. CA) is increasing close to the forests, that combined with the fact that 
    80% of the causes of fires are of human origin leads to a higher risk. For human causes,
    prevention remains a good way to reduce the number of fires.

    """
)
st.subheader("""WHAT WE'VE LEARNED:""")
st.write(
    """

    The project allowed us to apply all the technical skills acquired during the training such as:
    
    - Python, Matplotlib, Seaborn for data exploration and transformation.
    
    - Scikitlearn, Streamlit for Machine Learning.
    
    - PowerBI for analysis, dashboard and presentation of results.

    All that remains is to apply this knowledge to our field of expertise!
   
    
    """
)

st.write(
    """
    
    
    """
)

c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Data Analyst: CECILE SINNA**', icon="💡")
with c2:
    st.info('**Data Analyst: JEAN CHRISTOPHE THEAULT**', icon="💻")
with c3:
    st.info('**Data Analyst: SANTIAGO RODRIGUEZ DIAZ**', icon="🧠")

st.caption("This is part of the Project for DataScientest - Data Analyst")