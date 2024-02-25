import streamlit as st
import pandas as pd
from constant import (KEK_NETFLIX, NETFLIX_PATH)


@st.cache_data
def load_data_netflix():
    if KEK_NETFLIX in st.session_state:
        return st.session_state[KEK_NETFLIX]
    else:
        data = pd.read_csv(NETFLIX_PATH)
        st.session_state[KEK_NETFLIX] = data
    return st.session_state[KEK_NETFLIX]