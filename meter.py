import streamlit as st
import numpy as np
import pandas as pd
import requests

df2=pd.read_csv('app.csv')

st.sidebar.title("Meter Reading Dashboard")

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Refresh!')
if pressed:
    right_column.write("Just Refreshed!")

option=st.sidebar.selectbox("Looking for ?",('Dataset','Visualisation','Categorization'))
if option=='Dataset':
    st.title("Dataset")
    st.write(df2.head(70))
if option=='Visualisation':
    end = st.sidebar.date_input ( label='Date' , value=None , min_value=None , max_value=None , key=None )
    end=end.strftime("mm/dd/yyyy")
    df1=df2.loc[df2["Virtual_Apartment"]==3]
    df3=df1.loc[df1["date"]==end]
    time=df3.date_time.values
    series=df3.power.values
    st.title("Apartment Chart")
    #df2=df2.set_index('date')
    st.line_chart(df1['power'])
    st.title("Power Chart")    
    power=pd.DataFrame(series)
    power=power.reset_index()
    st.line_chart(df2['power'])

    
if option=='Categorization':
    df2=df2.set_index('date')
    df2.drop(['day','date_time','time','TS'],axis=1,inplace=True)
    st.bar_chart(df2)