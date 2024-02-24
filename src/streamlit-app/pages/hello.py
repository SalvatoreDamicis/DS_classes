import streamlit as st
import pandas as pd
import numpy as np
import os
from constant import *

st.title('Uber pickups in NYC')

@st.cache_data
def load_data():
    data = pd.read_csv(NETFLIX_PATH)
    return data

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache_data)")

st.write(data.head(5))