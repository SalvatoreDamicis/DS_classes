from utils import load_data_netflix
import streamlit as st
import plotly.figure_factory as ff
import plotly.express as px
import pandas as pd

def preprocessing(data):
    data_copy = data.copy()
    data_copy['date_added'] = pd.to_datetime(data_copy['date_added'])
    data_copy['year_added'] = data_copy['date_added'].dt.year
    data_copy['month_added'] = data_copy['date_added'].dt.month_name()
    data_copy['day_added'] = data_copy['date_added'].dt.day_name()
    data_copy['year-month_added'] = data_copy['date_added'].dt.to_period('M').astype(str)

    return data_copy
    

def history_release():
    data = load_data_netflix()
    data_prep = preprocessing(data)
    column_page = st.columns([1, 1, 1])
    
    type_release = column_page[0].radio( "Realese by time", ["Year", "Month"])
    flg_type = column_page[2].toggle('Activate type', value=False)
    
    if type_release == "Year":
        if flg_type:
            df = pd.DataFrame(data_prep.groupby(['year_added', 'type']).size())
            df = df.pivot_table(index='year_added', columns='type')
            df.fillna(0, inplace=True)
            df.columns = df.columns.droplevel()
            fig = px.line(df, x=df.index, y=['Movie', 'TV Show'], title='Release by year')
        else:
            df = data_prep.groupby('year_added').size()
            fig = px.line(df, x=df.index, y=df.values, title='Release by year')

    elif type_release == "Month":
        if flg_type:
            df = pd.DataFrame(data_prep.groupby(['year-month_added', 'type']).size())
            df = df.pivot_table(index='year-month_added', columns='type')
            df.fillna(0, inplace=True)
            df.columns = df.columns.droplevel()
            fig = px.line(df, x=df.index, y=['Movie', 'TV Show'], title='Release by year')
        else:
            df = data_prep.groupby(['year-month_added']).size()
            fig = px.line(df, x=df.index, y=df.values, title='Release by month')
    
    st.plotly_chart(fig) 