import streamlit as st
import pandas as pd
import numpy as np

st.maxUploadSize = 500

df = pd.read_csv("https://cez.ynh.fr/nextcloud/s/myctfjPrWEsWZ7R/download/Wildfire_cleaned_dataset_2.csv")

df
