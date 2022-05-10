

import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd

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

    #from https://python-graph-gallery.com/313-bubble-map-with-folium

    m = folium.Map(location=[0,0])

    m
