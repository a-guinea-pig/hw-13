

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
    
    dataset.groupby(['country']).sum().plot(
    kind='pie', y='lines', autopct='%1.0f%%')
    
    

   # m = folium.Map(location=[0,0])

   # m
