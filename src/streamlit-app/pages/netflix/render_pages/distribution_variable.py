from utils import load_data_netflix
import streamlit as st
import plotly.figure_factory as ff
import plotly.express as px



def distribution_varables():
    data = load_data_netflix()
    data_columns = data.columns
    var = st.selectbox('Select a variable', data_columns, index=1)
    flg_type = st.toggle('Activate type', value=False)
    
    if var in ['type', 'rating']:
        fig = px.histogram(data, x=var)
    elif flg_type:
        states = data[var].value_counts().head(10).index
        data_head = data[data[var].isin(states)]

        fig = px.histogram(data_head, x=var, color="type", barmode="group")
        
    else: 
        data_head = data[var].value_counts().head(10)
        
        fig = px.bar(data_head, x=data_head.index, y=data_head.values)
    
    st.plotly_chart(fig, use_container_width=True)
    