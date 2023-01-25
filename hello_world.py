import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("gs://streamlit-f40ff.appspot.com/Wildfire_cleaned_dataset_4.csv")

st.dataframe(df.style.highlight_max(axis=0))