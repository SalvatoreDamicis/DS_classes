import streamlit as st
import pandas as pd
from utils import load_data_netflix
import plotly.express as px


def rating():
    data = load_data_netflix()
    flg_type = st.toggle('Activate type', value=False)
    
    if flg_type:
        columns = st.columns((1,1))
        mask_0 = data['type'] == 'Movie'
        df_0 = data[mask_0]['rating'].value_counts()
        fig_0 = px.pie(df_0, names=df_0.index,values=df_0.values, hole=.5)
        mask_1 = data['type'] == 'TV Show'
        df_1 = data[mask_1]['rating'].value_counts()
        fig_1 = px.pie(df_1, names=df_1.index,values=df_1.values, hole=.5)
        
        columns[0].write('Movies')
        columns[0].plotly_chart(fig_0, use_container_width=True)
        columns[1].write('TV Shows')
        columns[1].plotly_chart(fig_1, use_container_width=True)

    else:
        df = data['rating'].value_counts()
        fig = px.pie(df, names=df.index,values=df.values, hole=.5)
    
        st.plotly_chart(fig)