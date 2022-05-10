

import streamlit as st

import folium 

import pandas as pd

import matplotlib.pyplot as plt

with st.echo(code_location='below'):

    def print_hello(name = "World"):
        st.write(f"## Hello, {name}!")

    name = st.text_area("enter your name")
    print_hello(name)

    @st.cache
    def get_dataset():
        dataset_link = "metro_countries_total.csv"
        return pd.read_csv(dataset_link)

    dataset = get_dataset()

    dataset
    
    colorss = ['#E08DAC', '#6A7FDB', '#57E2E5', '#45CB85', '#F9C846', '#F26419']
    df = dataset[["systems", "region"]]
    df1 = df.groupby(['region']).sum()
    df2 = df1.sort_values(by=["systems"], ascending=True)
    plot = df2.plot.pie(y='systems', figsize=(10, 10), wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' }, colors=colorss)
    #st.pyplot(fig=plot, clear_figure=None, **kwargs)
    
    

    m = folium.Map(location=[0,0])

    st.map(m)
