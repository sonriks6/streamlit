import streamlit as st
from PIL import Image

# Title
st.title('CONCLUSION')

st.write(
    """
    
    
    """
)
st.write(
    """
    Wildfires in the USA are progressing over time (especially in California, Georgia, Texas) 
    as well as their size (Arizona).
    
    
    The fires are increasingly devastating in terms of area 
    (class G is growing by 28% per year) and it is likely that with global warming and very dry
    summers this number will increase (increase in natural causes of fires).

    """
)
st.write(
    """

    Construction (e.g. CA) increasingly close to forests, combined with the fact that 
    80% of the causes of fires are of human origin increases the risk. For human causes,
    prevention remains a good way to reduce the number of fires.

    """
)
st.write(
    """

    The project allowed us to apply all the technical skills acquired during the training
    Python, Matplotlib, Seaborn for data exploration and transformation:
    
        Scikitlearn, Streamlit for Machine Learning.
	    PowerBI for analysis, dashboard and presentation of results.

    All that remains is to apply this knowledge to our field of expertise!
   
    
    
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