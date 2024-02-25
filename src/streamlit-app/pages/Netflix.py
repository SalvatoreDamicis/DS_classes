import streamlit as st
import pandas as pd
import numpy as np
import os
from constant import *
from utils import load_data_netflix
from pages.netflix.render_pages.distribution_variable import distribution_varables
from pages.netflix.render_pages.history_release import history_release
from pages.netflix.render_pages.rating import rating

st.title('Netflix Data Analysis')

data = load_data_netflix()

task_selected = st.sidebar.selectbox(
        label='Select which task to open',
        options=[
            'Dataset Overview',
            'Distribution Variables',
            'History Release',
            'Rating'
        ]
    )

if task_selected == 'Dataset Overview':
    st.subheader('Contents added to Netflix from 2008 to 2021.')
    st.write(data.head(10))
elif task_selected == 'Distribution Variables':
    st.subheader('Distribution Variables in Netflix Data.')
    distribution_varables()
elif task_selected == 'History Release':
    st.subheader('History Release in Netflix Data.')
    history_release()
elif task_selected == 'Rating':
    st.subheader('Rating in Netflix Data.')
    rating()    