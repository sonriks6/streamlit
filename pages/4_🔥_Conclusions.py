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
    
    The fires are devastating in terms of area (class G is growing year over year) and it is likely 
    that with global warming and very dry summers this number will keep increasing (growth in natural causes of fires).

    Seasonality, fire periods are longer, not only concentrated in summer, we have fires even on winter!.

    Human causes, are the main origin of wildfires, here revention remains a good way to reduce the number of fires.

    Climate zones: Mediterratean (CA) and Subtropical (South East) are the most impacted by fires.

    """
)
# st.subheader('HUMAN CAUSES:')
# st.write(
#     """

#     Human causes represent 80% of the causes of fires are of human origin leads to a higher risk. For human causes,
#     prevention remains a good way to reduce the number of fires.

#     """
# )
st.subheader("""WHAT WE'VE LEARNED:""")
st.write(
    """

    The project allowed us to apply all the technical skills acquired during the training such as:
    
    - Python, Matplotlib, Seaborn for data exploration and transformation.
    
    - Scikitlearn, Streamlit for Machine Learning.
    
    - PowerBI for analysis, dashboard and presentation of results.

    Aside the technical skills we also learned how to structure the analysis of an unknown domain, do the rearch and
    complementary data collection. All that remains is to apply this knowledge to our field of expertise!
   
    
    """
)
st.subheader("""WHAT WE'D DO WITH MORE TIME:""")
st.write(
    """
    We would complete our knowledge in this matter adding more features and extra data.
    Add interesting new feature like an Fire Risk Estimator or compare with another country.    
    We'd also try to get a robust analysis and conclusions.
    
    """
)

st.subheader("""-----------------------------------------------------------------------------------------------------""")

c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Data Analyst: CECILE SINNA**', icon="💡")
with c2:
    st.info('**Data Analyst: JEAN CHRISTOPHE THEAULT**', icon="💻")
with c3:
    st.info('**Data Analyst: SANTIAGO RODRIGUEZ DIAZ**', icon="🧠")

st.caption("This is part of the Project for DataScientest - Data Analyst")