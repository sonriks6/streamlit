import streamlit as st
import pandas as pd
import numpy as np

st.maxUploadSize = 500

df = pd.read_csv("https://cez.ynh.fr/nextcloud/s/CLHfSTpKXXmwStn/download/Wildfire_cleaned_dataset_4.csv")
df
